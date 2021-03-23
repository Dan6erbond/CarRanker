import { registerEnumType } from "@nestjs/graphql";

export enum DriveType {
  AWD = "awd",
  FWD = "fwd",
  RWD = "rwd",
}

registerEnumType(DriveType, {
  name: "DriveType",
  description: "A vehicle's drivetrain, either AWD, FWD, or RWD.",
});
