FROM httpd:2.4.39

ARG target

COPY httpd.conf /usr/local/apache2/conf/httpd.conf
RUN sed -i "s/{{TARGET}}/$target/g" /usr/local/apache2/conf/httpd.conf