FROM ubuntu:18.04

RUN apt-get update && apt install xinetd gcc -y

RUN useradd challenge
RUN mkdir /app

COPY ./src /tmp/chal
RUN gcc /tmp/chal/main.c -o /app/notebook -no-pie
RUN rm -rf /tmp/chal
RUN apt purge gcc -y

COPY ./flag.txt /
COPY ./config /etc/xinetd.d/notebook

RUN chown -R root:challenge /app
RUN chmod -R 555 /app

CMD ["/usr/sbin/xinetd", "-dontfork"]