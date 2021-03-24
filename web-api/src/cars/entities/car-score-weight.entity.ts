import { Cascade, Entity, OneToMany, Property } from "@mikro-orm/core";
import { Collection } from "@mikro-orm/core/entity";
import { BaseEntity } from "../../database/entities/base-entity.entity";
import { CarScore } from "./car-score.entity";

@Entity({ tableName: "car_score_weights" })
export class CarScoreWeight extends BaseEntity {
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
}
