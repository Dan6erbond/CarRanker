import {
  Collection,
  Entity,
  ManyToOne,
  OneToMany,
  PrimaryKey,
  Property,
} from "@mikro-orm/core";
import { Image } from "../../images/entities/image.entity";
import { BodyType } from "../enums/body-type.enum";
import { DriveType } from "../enums/drive-type.enum";
import { FuelType } from "../enums/fuel-type.enum";
import { TransmissionType } from "../enums/transmission-type.enum";
import { CarImage } from "./car-image.entity";
import { CarMake } from "./car-make.entity";
import { CarScore } from "./car-score.entity";

@Entity({ tableName: "cars" })
export class Car {
  @PrimaryKey()
  id: number;

  @Property()
  url: string;

  @ManyToOne(() => CarMake, { joinColumn: "make_id", onDelete: "CASCADE" })
  make: CarMake;

  @Property()
  model: string;

  @Property()
  variant: string;

  @Property({ name: "type_full", nullable: true })
  fullType: string;

  @Property()
  price: number;

  @Property()
  horsePower: number;

  @Property({ nullable: true })
  cylinders: number;

  @Property()
  firstRegistrationYear: number;

  @Property({ nullable: true })
  firstRegistrationDate: Date;

  @Property()
  transmissionType: TransmissionType;

  @Property()
  fuelType: FuelType;

  @Property()
  bodyType: BodyType;

  @Property({ nullable: true })
  seats: number;

  @Property()
  doors: number;

  @Property({ nullable: true })
  driveType: DriveType;

  @Property()
  mileage: number;

  @Property({ nullable: true })
  consumptionCombined: number;

  @ManyToOne(() => Image, {
    joinColumn: "exterior_front_image_id",
    nullable: true,
  })
  exteriorFrontImage: Image;

  @ManyToOne(() => Image, {
    joinColumn: "exterior_side_image_id",
    nullable: true,
  })
  exteriorSideImage: Image;

  @ManyToOne(() => Image, {
    joinColumn: "exterior_back_image_id",
    nullable: true,
  })
  exteriorBackImage: Image;

  @ManyToOne(() => Image, {
    joinColumn: "interior_front_image_id",
    nullable: true,
  })
  interiorFrontImage: Image;

  @ManyToOne(() => Image, {
    joinColumn: "interior_dash_image_id",
    nullable: true,
  })
  interiorDashImage: Image;

  @ManyToOne(() => Image, {
    joinColumn: "interior_back_image_id",
    nullable: true,
  })
  interiorBackImage: Image;

  @ManyToOne(() => Image, {
    joinColumn: "interior_trunk_image_id",
    nullable: true,
  })
  interiorTrunkImage: Image;

  @OneToMany(() => CarImage, (carImage) => carImage.car)
  images = new Collection<CarImage>(this);

  @OneToMany(() => CarScore, (carScore) => carScore.car)
  scores = new Collection<CarScore>(this);

  @Property()
  data: string;

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
