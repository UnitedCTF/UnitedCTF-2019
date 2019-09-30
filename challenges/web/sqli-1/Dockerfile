FROM php:7.0-apache

RUN apt update && apt upgrade -y
RUN apt install sqlite3 -y

COPY db.sql /db.sql
RUN cat /db.sql | sqlite3 /database.db
RUN rm /db.sql

VOLUME /var/www/html