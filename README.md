# CarRanker

![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v3-informational?style=flat&logo=docker)
![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat&logo=python)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-green?style=flat&logo=postgresql)
![NestJS](https://img.shields.io/badge/Vue-2.6-brightgreen?style=flat&logo=vue.js)
![NestJS](https://img.shields.io/badge/NestJS-7.5-E0234E?style=flat&logo=nestjs)

- [CarRanker](#carranker)
  - [Setup](#setup)
  - [Roadmap](#roadmap)

CarRanker is a work-in-progress fullstack web application with a Vue frontend to webscrape vehicle information from used car websites such as CarForYou and Tutti.

The scraped information will be normalized and stored in a PostgreSQL database to aggregate listings, and users can rank cars based on various factors such as interior, exterior, reliability, cost to run (CTR), etc. The overall car rating will be used by a machine learning model to figure out which aspects a user values most, and automatically attempt to rank cars and scrape listings in the future.

It consists of four services:
 - A PostgreSQL Database
 - A Python Processing Services for Machine Learning, Image Processing and webscraping
 - A NestJS API using GraphQL
 - A VueJS Frontend

The Python service can also generate shareable cards in the following forms. It uses machine learning to locate the object and determine the type of picture to lay them out accordingly in the grid:

![CarRanker Card](./docs/images/Screenshot%202021-03-02%20113143.png)

## Setup

CarRanker uses Docker to spin up all the underlying services, after cloning the Git repo all you need to do is create a `docker_postgres_password` file in the root of the repository, where the PostgreSQL password should be set for the `postgres` user, and then `docker-compose up --build` can be ran to run the services and expose ports.

## Roadmap

 - Implement Python Machine Learning
 - Update Card Design
 - Implement NestJS API
 - Implement VueJS Frontend
 - Implement Auto-Scraper CRON Job
