import { MikroOrmModule } from "@mikro-orm/nestjs";
import { Module } from "@nestjs/common";
import { Car } from "./entities/car.entity";

@Module({ imports: [MikroOrmModule.forFeature([Car])] })
export class CarsModule {}
