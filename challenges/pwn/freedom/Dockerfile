FROM ubuntu:18.04

RUN apt-get -y update
RUN apt-get -y install xinetd vim net-tools
RUN useradd challenge
RUN mkdir /app
RUN echo 'cd /app && /app/freedom' > /launcher.sh

COPY ./freedom /app/freedom
COPY ./eagles/ /app/eagles/
COPY ./flag /flag
COPY ./config /etc/xinetd.d/pwn
CMD ["/usr/sbin/xinetd", "-dontfork"]