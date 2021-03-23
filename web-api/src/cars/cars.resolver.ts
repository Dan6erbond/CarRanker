import { Query, Resolver } from "@nestjs/graphql";
import { CarObject } from "./dto/car.object";

@Resolver(() => CarObject)
export class CarsResolver {
  @Query(() => [CarObject])
  async cars() {
    throw new Error("Not implemented.");
  }
}
