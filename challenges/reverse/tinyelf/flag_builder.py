import subprocess
import sys

subprocess.run(["nasm", "-f", "bin", "-o", "tinyelf.tmp", "tinyelf.asm"])

if len(sys.argv) < 2:
    print("Usage: python flag_builder.py FLAG_GOES_HERE")
    exit()

if len(sys.argv[1]) != 32:
    print("Flag needs to be of length 32.")
    exit()

flag = sys.argv[1]

with open("tinyelf.tmp", "rb") as elf:
    data = elf.read()[0:96]
    output = bytes()
    total = 0
    for c in data:
        total = (total + c) & 0xff
    total = (total - 1) & 0xff

    for i in range(32):
        target = ord(flag[31-i]) ^ 0xdb
        if target >= total:
            next_byte = target - total
        else:
            next_byte = 256-total + target
        output += bytes([next_byte])
        total = (total + next_byte) & 0xff
    with open("tinyelf", "wb") as out:
        out.write(data+ output)

subprocess.run(["rm", "tinyelf.tmp"])