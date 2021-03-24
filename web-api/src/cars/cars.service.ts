import { EntityRepository } from "@mikro-orm/core";
import { InjectRepository } from "@mikro-orm/nestjs";
import { Injectable } from "@nestjs/common";
import { ProcessingService } from "src/processing/processing.service";
import { Car } from "./entities/car.entity";

interface FindAllArgs {
  relations: string[];
}

interface FindOneArgs extends FindAllArgs {
  id: number;
}

@Injectable()
export class CarsService {
  constructor(
    @InjectRepository(Car) private carsRepository: EntityRepository<Car>,
    private processingService: ProcessingService,
  ) {}

  findAll({ relations }: FindAllArgs) {
    return this.carsRepository.find({}, relations);
  }

  findOne({ id, relations }: FindOneArgs) {
    return this.carsRepository.findOne(id, relations);
  }

  scrapeCar(url: string) {
    return this.processingService.scrapeCar(url);
  }
}
