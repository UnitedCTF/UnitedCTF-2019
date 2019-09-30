FROM php:7.0-apache

RUN apt update && apt upgrade -y
RUN apt install sqlite3  -y

COPY ./config.php /var/www/html/config.php
COPY ./crypto.php /var/www/html/crypto.php
COPY ./database.php /var/www/html/database.php
COPY ./index.php /var/www/html/index.php
COPY ./login.php /var/www/html/login.php
COPY ./logout.php /var/www/html/logout.php
COPY ./user.php /var/www/html/user.php