import { ApolloClientClientConfig } from "vue-cli-plugin-apollo/graphql-client";

export default () => {
  let httpEndpoint: string;

  if (process.env.webApiHost && process.env.webApiPort) {
    httpEndpoint = `${process.env.webApiHost}:${process.env.webApiPort}/graphql`;
  } else {
    httpEndpoint = "localhost:3000/graphql";
  }

  return {
    httpEndpoint,
    tokenName: "accessToken",
  } as ApolloClientClientConfig<any>;
};
