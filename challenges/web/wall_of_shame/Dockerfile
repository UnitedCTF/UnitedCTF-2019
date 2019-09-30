FROM php:7.0-apache

RUN apt-get update && apt-get install -y zlib1g-dev

RUN docker-php-ext-install zip exif mbstring

RUN a2enmod rewrite

COPY flag.txt /flag.txt

RUN mkdir /var/www/html/uploads
RUN chown -R root:www-data /var/www/html
RUN chmod -R 733 /var/www/html/uploads