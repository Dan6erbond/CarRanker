import { MikroOrmModule } from "@mikro-orm/nestjs";
import { Module } from "@nestjs/common";
import { ProcessingModule } from "src/processing/processing.module";
import { CarsResolver } from "./cars.resolver";
import { CarsService } from "./cars.service";
import { Car } from "./entities/car.entity";

@Module({
  imports: [MikroOrmModule.forFeature([Car]), ProcessingModule],
  providers: [CarsResolver, CarsService],
})
export class CarsModule {}
