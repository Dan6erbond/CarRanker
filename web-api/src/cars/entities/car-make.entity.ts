import {
  Cascade,
  Entity,
  OneToMany,
  PrimaryKey,
  Property,
} from "@mikro-orm/core";
import { Collection } from "@mikro-orm/core/entity";
import { CarMakeAlias } from "./car-make-alias.entity";
import { Car } from "./car.entity";

@Entity({ tableName: "makes" })
export class CarMake {
  @PrimaryKey()
  id: number;

  @Property()
  name: string;

  @OneToMany(() => Car, (car) => car.make, { cascade: [Cascade.REMOVE] })
  cars = new Collection<Car>(this);

  @OneToMany(() => CarMakeAlias, (alias) => alias.make, {
    cascade: [Cascade.REMOVE],
  })
  aliases = new Collection<CarMakeAlias>(this);

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
