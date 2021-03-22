import {
  Collection,
  Entity,
  ManyToOne,
  OneToMany,
  PrimaryKey,
  Property,
} from "@mikro-orm/core";
import { Image } from "../../images/entities/image.entity";
import { CarImage } from "./car-image.entity";
import { CarMake } from "./car-make.entity";
import { CarScore } from "./car-score.entity";

export enum TransmissionType {
  AUTOMATIC = "automatic",
  AUTOMATIC_CVT = "automatic_cvt",
  MANUAL = "manual",
}

export enum FuelType {
  GASOLINE = "gasoline",
  DIESEL = "diesel",
}

export enum BodyType {
  SEDAN = "sedan",
  SUV = "suv",
  MINIVAN = "minivan",
  PICKUP = "pickup",
  HATCHBACK = "hatchback",
  COUPE = "coupe",
  STATION_WAGON = "station_wagon",
}

export enum DriveType {
  AWD = "awd",
  FWD = "fwd",
  RWD = "rwd",
}

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

  @ManyToOne(() => Image, { joinColumn: "exterior_front_image_id" })
  exteriorFrontImage: Image;

  @ManyToOne(() => Image, { joinColumn: "exterior_side_image_id" })
  exteriorSideImage: Image;

  @ManyToOne(() => Image, { joinColumn: "exterior_back_image_id" })
  exteriorBackImage: Image;

  @ManyToOne(() => Image, { joinColumn: "interior_front_image_id" })
  interiorFrontImage: Image;

  @ManyToOne(() => Image, { joinColumn: "interior_dash_image_id" })
  interiorDashImage: Image;

  @ManyToOne(() => Image, { joinColumn: "interior_back_image_id" })
  interiorBackImage: Image;

  @ManyToOne(() => Image, { joinColumn: "interior_trunk_image_id" })
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
