import { Entity, ManyToOne, PrimaryKey, Property } from "@mikro-orm/core";
import { Image } from "../../images/entities/image.entity";
import { Car } from "./car.entity";

@Entity({ tableName: "cars_images" })
export class CarImage {
  @PrimaryKey()
  id: number;

  @ManyToOne(() => Car, { joinColumn: "car_id" })
  car: Car;

  @ManyToOne(() => Image, { joinColumn: "image_id" })
  image: Image;

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
