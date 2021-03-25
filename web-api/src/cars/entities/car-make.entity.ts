import { Cascade, Entity, OneToMany, Property } from "@mikro-orm/core";
import { Collection } from "@mikro-orm/core/entity";
import { BaseEntity } from "../../database/entities/base-entity.entity";
import { CarMakeAlias } from "./car-make-alias.entity";
import { Car } from "./car.entity";

@Entity({ tableName: "makes" })
export class CarMake extends BaseEntity {
  @Property()
  name: string;

  @OneToMany(() => Car, (car) => car.make, { cascade: [Cascade.REMOVE] })
  cars = new Collection<Car>(this);

  @OneToMany(() => CarMakeAlias, (alias) => alias.make, {
    cascade: [Cascade.REMOVE],
  })
  aliases = new Collection<CarMakeAlias>(this);
}
