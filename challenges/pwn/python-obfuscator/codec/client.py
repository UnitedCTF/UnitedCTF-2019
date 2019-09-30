#!/usr/bin/env python3
import socket
import sys
import time

# Read from the socket until a string is reached
def read_until(s, end, drop = False):
    if isinstance(end, str):
        end = end.encode()

    c = s.recv(1)
    data = c

    while data[-len(end) :] != end:
        c = s.recv(1)
        data += c
    
    if drop:
        # Remove token string we were looking for from the output
        data = data[: -len(end)]
    
    return data.decode()


# Read a line from the socket
def readline(s, drop = False):
    return read_until(s, "\n")


if len(sys.argv) != 5:
    print(f"Usage: {sys.argv[0]} SERVER_IP SERVER_PORT SOURCE_FILE OUTPUT_FILE", file = sys.stderr)
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

with open(sys.argv[3], "rb") as f:
    source = f.read()

source_length = len(source)

# Time string
readline(s)

# File size prompt
read_until(s, ": ")

# Send file size. The \n is important!
s.send(f"{source_length}\n".encode())

# Make sure to wait for the server to be ready to receive input, then send Python source code
time.sleep(0.1)
s.send(source)

# Compiled obfuscated python source
compiled = s.recv(4096)

with open(sys.argv[4], "wb") as f:
    f.write(compiled)