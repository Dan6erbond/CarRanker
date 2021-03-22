FROM node:15.12.0

WORKDIR /usr/src/app/

ENV NODE_ENV development

COPY package.json .
COPY yarn.lock .

RUN yarn install

COPY . .

EXPOSE 3000

CMD ["./wait-for-it.sh", "db:5432", "--", "./entrypoint.sh"]
