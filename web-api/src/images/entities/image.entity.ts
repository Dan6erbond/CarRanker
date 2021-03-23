import { Entity, OneToOne, PrimaryKey, Property } from "@mikro-orm/core";
import { CarImage } from "../../cars/entities/car-image.entity";
import { Car } from "../../cars/entities/car.entity";

@Entity({ tableName: "images" })
export class Image {
  @PrimaryKey()
  id: number;

  @Property()
  url: string;

  @OneToOne(() => Car, (car) => car.exteriorFrontImage, { nullable: true })
  carForExteriorFront: Car;

  @OneToOne(() => Car, (car) => car.exteriorSideImage, { nullable: true })
  carForExteriorSide: Car;

  @OneToOne(() => Car, (car) => car.exteriorBackImage, { nullable: true })
  carForExteriorBack: Car;

  @OneToOne(() => Car, (car) => car.interiorFrontImage, { nullable: true })
  carForInteriorFront: Car;

  @OneToOne(() => Car, (car) => car.interiorDashImage, { nullable: true })
  carForInteriorDash: Car;

  @OneToOne(() => Car, (car) => car.interiorBackImage, { nullable: true })
  carForInteriorBack: Car;

  @OneToOne(() => Car, (car) => car.interiorTrunkImage, { nullable: true })
  carForInteriorTrunk: Car;

  @OneToOne(() => CarImage, (carImage) => carImage.image, { nullable: true })
  carImage: CarImage;

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
