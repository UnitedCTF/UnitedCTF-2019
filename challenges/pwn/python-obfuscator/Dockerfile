FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get -y install xinetd vim net-tools python3
RUN useradd challenge
RUN mkdir /app
COPY ./codec/server.py /app/server.py
COPY ./codec/hackme.so /app/hackme.so
COPY ./config /etc/xinetd.d/pwn
COPY ./flag /flag
CMD ["/usr/sbin/xinetd", "-dontfork"]