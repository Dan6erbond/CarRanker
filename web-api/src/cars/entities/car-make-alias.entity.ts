import { Entity, ManyToOne, Property } from "@mikro-orm/core";
import { BaseEntity } from "../../database/entities/base-entity.entity";
import { CarMake } from "./car-make.entity";

@Entity({ tableName: "make_aliases" })
export class CarMakeAlias extends BaseEntity {
  @Property()
  name: string;

  @ManyToOne(() => CarMake, { joinColumn: "make_id", onDelete: "CASCADE" })
  make: CarMake;
}
