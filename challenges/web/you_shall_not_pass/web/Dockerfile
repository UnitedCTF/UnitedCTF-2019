FROM php:7.0-apache

RUN apt update && apt upgrade -y
RUN apt install sqlite3 -y

RUN mkdir /web
RUN chown www-data:www-data /web
COPY db.sql /db.sql
RUN cat /db.sql | sqlite3 /web/database.db
RUN chmod 666 /web/database.db
RUN rm /db.sql

COPY apache2.conf /etc/apache2

VOLUME /var/www/html