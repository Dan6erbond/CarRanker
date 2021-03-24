import { Selections } from "@jenyus-org/nestjs-graphql-utils";
import {
  Args,
  Mutation,
  Parent,
  Query,
  ResolveField,
  Resolver,
} from "@nestjs/graphql";
import { UserInputError } from "apollo-server-errors";
import { CarsService } from "./cars.service";
import { CarImageObject } from "./dto/car-image.object";
import { CarObject } from "./dto/car.object";
import { Car } from "./entities/car.entity";

const carSelections = ["**.**", { field: "images", selector: "images.image" }];

@Resolver(() => CarObject)
export class CarsResolver {
  constructor(private carsService: CarsService) {}

  @Query(() => [CarObject])
  cars(
    @Selections([
      {
        field: "cars",
        selections: [...carSelections],
      },
    ])
    relations: string[],
  ) {
    return this.carsService.findAll({ relations });
  }

  @Mutation(() => CarObject)
  async submitCar(
    @Args("url") url: string,
    @Selections([
      {
        field: "submitCar",
        selections: [...carSelections],
      },
    ])
    relations: string[],
  ) {
    try {
      const id = await this.carsService.scrapeCar(url);
      this.carsService.findOne({ id, relations });
    } catch (error) {
      throw new UserInputError(error.message);
    }
  }

  @ResolveField(() => [CarImageObject])
  async images(@Parent() car: Car) {
    if (!car.images.isInitialized()) {
      await car.images.init({ populate: ["image"] });
    }

    return car.images.getItems().map((image) => image.image);
  }
}
