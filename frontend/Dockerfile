FROM node:18-alpine AS builder

RUN npm install -g http-server

RUN mkdir /app
WORKDIR /app

COPY . .
RUN npm install .
RUN npm run build

EXPOSE 8080

CMD http-server dist