import { Field, Int, ObjectType } from "@nestjs/graphql";

@ObjectType("CarImage")
export class CarImageObject {
  @Field(() => Int)
  id: number;

  @Field()
  url: string;

  @Field()
  createdAt: Date;

  @Field()
  updatedAt: Date;
}
