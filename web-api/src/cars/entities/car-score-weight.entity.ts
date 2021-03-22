import {
  Cascade,
  Entity,
  OneToMany,
  PrimaryKey,
  Property
} from "@mikro-orm/core";
import { Collection } from "@mikro-orm/core/entity";
import { CarScore } from "./car-score.entity";

@Entity({ tableName: "car_score_weights" })
export class CarScoreWeight {
  @PrimaryKey()
  id: number;

  @OneToMany(() => CarScore, (carScore) => carScore.weights, {
    cascade: [Cascade.REMOVE],
  })
  carScores = new Collection<CarScore>(this);

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

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
