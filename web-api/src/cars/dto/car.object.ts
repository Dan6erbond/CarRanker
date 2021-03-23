import { Field, Float, Int, ObjectType } from "@nestjs/graphql";
import { BodyType } from "../enums/body-type.enum";
import { DriveType } from "../enums/drive-type.enum";
import { FuelType } from "../enums/fuel-type.enum";
import { TransmissionType } from "../enums/transmission-type.enum";

@ObjectType("Car")
export class CarObject {
  @Field(() => Int)
  id: number;

  @Field()
  url: string;

  // TODO: Add car make

  @Field()
  model: string;

  @Field()
  variant: string;

  @Field()
  fullType: string;

  @Field(() => Float)
  price: number;

  @Field(() => Int)
  horsePower: number;

  @Field(() => Int)
  cylinders: number;

  @Field(() => Int)
  firstRegistrationYear: number;

  @Field()
  firstRegistrationDate: Date;

  @Field(() => TransmissionType)
  transmissionType: TransmissionType;

  @Field(() => FuelType)
  fuelType: FuelType;

  @Field(() => BodyType)
  bodyType: BodyType;

  @Field(() => Int)
  seats: number;

  @Field(() => Int)
  doors: number;

  @Field(() => DriveType)
  driveType: DriveType;

  @Field(() => Int)
  mileage: number;

  @Field(() => Float)
  consumptionCombined: number;

  @Field()
  data: string;

  @Field()
  createdAt: Date;

  @Field()
  updatedAt: Date;
}
