import { registerEnumType } from "@nestjs/graphql";

export enum FuelType {
  GASOLINE = "gasoline",
  DIESEL = "diesel",
}

registerEnumType(FuelType, {
  name: "FuelType",
  description: "Different fuel types used by vehicles.",
});
