FROM php:7.2-apache

RUN mkdir /var/www/html/uploads
RUN chown root:www-data /var/www/html/uploads
RUN chmod 730 /var/www/html/uploads

COPY ./flag /bet-you-cant-guess-the-path-of-this-flag
COPY ./editor.php /var/www/html/
COPY ./header.php /var/www/html/
COPY ./index.php /var/www/html/
COPY ./register.php /var/www/html/
COPY ./styles.css /var/www/html/
COPY ./user.php /var/www/html/