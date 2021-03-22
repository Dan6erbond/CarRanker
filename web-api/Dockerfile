FROM node:15.12.0
RUN mkdir -p /app/
WORKDIR /app/
COPY ["package.json", "package-lock.json*", "./"]
RUN yarn
COPY . .
EXPOSE 3000
CMD ["./wait-for-it.sh", "db:5432", "--", "./entrypoint.sh"]
