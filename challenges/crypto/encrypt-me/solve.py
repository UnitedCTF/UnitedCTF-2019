#!/usr/bin/env python2
from pwn import *
import sys
import time

import gmpy2
from progressbar import progressbar
from Crypto.Util.number import inverse, bytes_to_long, long_to_bytes

def menu():
    r.recvuntil("choice:\n")

def get_flag(n):
    menu()
    r.sendline("1")
    r.recvuntil("number:\n")
    r.sendline(str(n))
    return r.recvuntil("\n").strip()

def encrypt(data):
    menu()
    r.sendline("2")
    r.recvuntil("encrypt:\n")
    r.sendline(data)
    return int(r.recvuntil("\n"))

r = remote("localhost", 3006)
e = 65537
m1 = "aaaa"
m2 = "bbbb"
c1 = encrypt(m1)
c2 = encrypt(m2)
N = gmpy2.gcd(bytes_to_long(m1) ** e - c1, bytes_to_long(m2) ** e - c2)

sys.stdout.write("Finding N... ")
for attempt in range(10):
    m = "c" * attempt
    c = encrypt(m)
    N = gmpy2.gcd(bytes_to_long(m) ** e - c, N)

print("done!")

plaintext = "I want the flag :)"
flag = get_flag(pow(bytes_to_long(plaintext), e, N))
print(flag)