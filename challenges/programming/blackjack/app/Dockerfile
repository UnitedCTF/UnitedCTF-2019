FROM node:latest

COPY . /app
WORKDIR /app

ARG SERVER_URL=default
ENV SERVER_URL=${SERVER_URL}

RUN npm install
RUN npm run build
RUN npm install -g http-server

CMD ["http-server", "/app/dist"]
