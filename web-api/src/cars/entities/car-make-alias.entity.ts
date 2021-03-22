import { Entity, ManyToOne, PrimaryKey, Property } from "@mikro-orm/core";
import { CarMake } from "./car-make.entity";

@Entity({ tableName: "make_aliases" })
export class CarMakeAlias {
  @PrimaryKey()
  id: number;

  @Property()
  name: string;

  @ManyToOne(() => CarMake, { joinColumn: "make_id", onDelete: "CASCADE" })
  make: CarMake;

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
