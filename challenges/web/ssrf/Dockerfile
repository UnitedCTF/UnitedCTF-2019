FROM ubuntu:18.04

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y \
    supervisor \
    redis-server \
    php php-curl php-redis php-tidy \
    apache2 libapache2-mod-php \
    gcc

COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY conf/apache2.conf /etc/apache2/sites-available/000-default.conf
COPY conf/php.ini /etc/php/7.2/apache2/php.ini

COPY flag.c /tmp
RUN gcc /tmp/flag.c -o /flag
RUN rm -rf /tmp/flag.c
RUN apt purge gcc -y
RUN chmod -R 111 /flag

RUN mkdir /var/www/html/tmp
RUN chown -R root:www-data /var/www/html/tmp
RUN chmod -R 733 /var/www/html/tmp

COPY cleanup.php /cleanup.php

ENTRYPOINT ["/usr/bin/supervisord"]