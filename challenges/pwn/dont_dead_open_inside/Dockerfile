FROM ubuntu:18.04

RUN apt-get update && apt-get install xinetd gcc -y

RUN useradd challenge
RUN mkdir /app

COPY ./src /tmp/chal
RUN gcc /tmp/chal/main.c -o /app/dont_dead_open_inside -z execstack -no-pie
RUN rm -rf /tmp/chal
RUN apt purge gcc -y

COPY ./dont_dead_open_inside_flag.txt /
COPY ./config /etc/xinetd.d/dont_dead_open_inside

RUN chown -R root:challenge /app
RUN chmod -R 555 /app

CMD ["/usr/sbin/xinetd", "-dontfork"]
