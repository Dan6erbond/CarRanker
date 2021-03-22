import { Entity, PrimaryKey, Property } from "@mikro-orm/core";

@Entity({ tableName: "images" })
export class Image {
  @PrimaryKey()
  id: number;

  @Property()
  url: string;

  @Property({ name: "date_created" })
  createdAt: Date = new Date();

  @Property({ name: "date_modified", onUpdate: () => new Date() })
  updatedAt: Date = new Date();
}
