import { Entity, PrimaryKey, Property } from "@mikro-orm/core";

@Entity({ abstract: true })
export abstract class BaseEntity {
  @PrimaryKey()
  id: number;

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
