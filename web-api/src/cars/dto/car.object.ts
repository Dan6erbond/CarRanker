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

  @Field({ nullable: true })
  fullType: string;

  @Field(() => Float)
  price: number;

  @Field(() => Int)
  horsePower: number;

  @Field(() => Int, { nullable: true })
  cylinders: number;

  @Field(() => Int)
  firstRegistrationYear: number;

  @Field({ nullable: true })
  firstRegistrationDate: Date;

  @Field(() => TransmissionType)
  transmissionType: TransmissionType;

  @Field(() => FuelType)
  fuelType: FuelType;

  @Field(() => BodyType)
  bodyType: BodyType;

  @Field(() => Int, { nullable: true })
  seats: number;

  @Field(() => Int)
  doors: number;

  @Field(() => DriveType, { nullable: true })
  driveType: DriveType;

  @Field(() => Int)
  mileage: number;

  @Field(() => Float, { nullable: true })
  consumptionCombined: number;

  @Field()
  data: string;

  @Field()
  createdAt: Date;

  @Field()
  updatedAt: Date;
}
