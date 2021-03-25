import { Entity, ManyToOne, OneToOne } from "@mikro-orm/core";
import { BaseEntity } from "../../database/entities/base-entity.entity";
import { Image } from "../../images/entities/image.entity";
import { Car } from "./car.entity";

@Entity({ tableName: "cars_images" })
export class CarImage extends BaseEntity {
  @ManyToOne(() => Car, { joinColumn: "car_id" })
  car: Car;

  @OneToOne({ entity: () => Image, joinColumn: "image_id" })
  image: Image;
}
