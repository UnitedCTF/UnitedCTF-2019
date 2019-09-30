FROM php:7.0-apache
RUN apt-get update && apt-get install cowsay -y
COPY ./src /var/www/html
RUN chown -R root:www-data /var/www/html
RUN chmod 554 -R /var/www/html
