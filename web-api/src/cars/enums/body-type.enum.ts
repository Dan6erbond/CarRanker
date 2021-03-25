import { registerEnumType } from "@nestjs/graphql";

export enum BodyType {
  SEDAN = "sedan",
  SUV = "suv",
  MINIVAN = "minivan",
  PICKUP = "pickup",
  HATCHBACK = "hatchback",
  COUPE = "coupe",
  STATION_WAGON = "station_wagon",
}

registerEnumType(BodyType, {
  name: "BodyType",
  description:
    "A car's body type, differentiates between sedans and hatchbacks.",
});
