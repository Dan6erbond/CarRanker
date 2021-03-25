import { registerEnumType } from "@nestjs/graphql";

export enum TransmissionType {
  AUTOMATIC = "automatic",
  AUTOMATIC_CVT = "automatic_cvt",
  MANUAL = "manual",
}

registerEnumType(TransmissionType, {
  name: "TransmissionType",
  description:
    "Transmission type of vehicles, either automatic, CVT or manual gearboxes.",
});
