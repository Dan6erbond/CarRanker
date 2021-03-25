import { Entity, ManyToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../../database/entities/base-entity.entity";
import { User } from "../../users/entities/user.entity";
import { CarScoreWeight } from "./car-score-weight.entity";
import { Car } from "./car.entity";

@Entity({ tableName: "car_scores" })
export class CarScore extends BaseEntity {
  @ManyToOne(() => Car, { joinColumn: "car_id", onDelete: "CASCADE" })
  car: Car;

  @ManyToOne(() => User, { joinColumn: "user_id", onDelete: "CASCADE" })
  user: User;

  @ManyToOne(() => CarScoreWeight, {
    joinColumn: "car_score_weight_id",
    onDelete: "CASCADE",
  })
  weights: CarScoreWeight;

  @Property({ name: "interior_score" })
  interior: number;

  @Property({ name: "exterior_score" })
  exterior: number;

  @Property({ name: "equipment_score" })
  equipment: number;

  @Property({ name: "design_score" })
  design: number;

  @Property({ name: "run_costs_score" })
  costToRun: number;

  @Property({ name: "maintenance_score" })
  maintenance: number;
}
