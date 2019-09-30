FROM node:latest

RUN apt-get update && apt-get install -y \
    apache2 \
    supervisor

COPY /public /var/www/html
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app
COPY /server /app
RUN npm install

ENTRYPOINT ["/usr/bin/supervisord"]
