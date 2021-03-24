import {
  Cascade,
  Collection,
  Entity,
  OneToMany,
  Property,
} from "@mikro-orm/core";
import { RefreshToken } from "../../auth/entities/refresh-token.entity";
import { BaseEntity } from "../../database/entities/base-entity.entity";

@Entity({ tableName: "users" })
export class User extends BaseEntity {
  @Property()
  username: string;

  @Property()
  password: string;

  @Property({ nullable: true })
  firstName: string;

  @Property({ nullable: true })
  lastName: string;

  @OneToMany(() => RefreshToken, (refreshToken) => refreshToken.user, {
    cascade: [Cascade.REMOVE],
  })
  refreshTokens = new Collection<RefreshToken>(this);
}
