import { MikroOrmModule } from "@mikro-orm/nestjs";
import { Module } from "@nestjs/common";
import { Car } from "./entities/car.entity";
import { CarsResolver } from './cars.resolver';

@Module({ imports: [MikroOrmModule.forFeature([Car])], providers: [CarsResolver] })
export class CarsModule {}
