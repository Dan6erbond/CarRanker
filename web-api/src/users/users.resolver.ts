import { Selections } from "@jenyus-org/nestjs-graphql-utils";
import { UseGuards } from "@nestjs/common";
import { Args, Int, Mutation, Query, Resolver } from "@nestjs/graphql";
import { UserInputError } from "apollo-server-express";
import { GqlCurrentUser } from "../auth/decorator/gql-current-user.decorator";
import { GqlAuthGuard } from "../auth/guards/gql-auth.guard";
import { UpdateProfileInput } from "./dto/update-profile.input";
import { UserObject } from "./dto/user.object";
import { User } from "./entities/user.entity";
import { UsersService } from "./users.service";

@Resolver(() => UserObject)
export class UsersResolver {
  constructor(private readonly usersService: UsersService) {}

  @Query(() => [UserObject])
  users(@Selections("users", ["posts"]) relations: string[]) {
    return this.usersService.findAll({ relations });
  }

  @Query(() => UserObject)
  user(
    @Selections("user", ["posts"]) relations: string[],
    @Args("id", { type: () => Int, nullable: true }) id?: number,
    @Args("username", { nullable: true }) username?: string,
  ) {
    if (!id && !username) {
      throw new UserInputError("Arguments must be one of ID or username.");
    }
    return this.usersService.findOne({ id, username, relations });
  }

  @Mutation(() => UserObject)
  @UseGuards(GqlAuthGuard)
  updateProfile(
    @GqlCurrentUser() user: User,
    @Args("input") input: UpdateProfileInput,
  ) {
    return this.usersService.update(user.id, input);
  }

  @Query(() => UserObject)
  @UseGuards(GqlAuthGuard)
  me(@GqlCurrentUser() user: User) {
    return user;
  }
}
