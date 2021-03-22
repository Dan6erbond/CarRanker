FROM node:15.12.0

WORKDIR /usr/src/app/

COPY package.json .
COPY yarn.lock .

RUN yarn install

RUN yarn global add rimraf request @nestjs/cli

COPY . .

EXPOSE 3000

CMD ["./wait-for-it.sh", "db:5432", "--", "./entrypoint.sh"]
