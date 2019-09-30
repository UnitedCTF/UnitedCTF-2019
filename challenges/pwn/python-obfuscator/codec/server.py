#!/usr/bin/env python3
import os
import re
import sys
import tempfile

from io import BytesIO
from py_compile import compile

import hackme

def pwn_replace(match):
    delim = match.group(1)
    contents = match.group(2)
    obfuscated = hackme.obfuscate(contents, len(contents))
    result = b"decode_string(" + delim + obfuscated + delim + b")"
    return result

def pwn_obfuscate(data):
    reader = BytesIO(data)
    decoded = b"""
def decode_string(string):
    decoded = [chr(ord(b) ^ 0x04) for b in string]
    return "".join(decoded)

"""

    for line in reader.readlines():
        if not line.startswith(b"#"):
            decoded += re.sub(rb"""PWN("|')(.*)(?<!\\)\1""", pwn_replace, line)
    
    return decoded

print("Time: ", end="", flush=True)
os.system("date")

size = int(input("File size: "))

if size > 1024:
    hackme.cookie()

data = sys.stdin.buffer.read(size)
data = pwn_obfuscate(data)

_, temp_source = tempfile.mkstemp(suffix = ".py", prefix = "target_")
temp_compiled = temp_source + "c"

with open(temp_source, "wb") as f:
    f.write(data)

compiled = compile(temp_source, temp_compiled)

with open(temp_compiled, "rb") as f:
    sys.stdout.buffer.write(f.read())
    sys.stdout.buffer.flush()

os.remove(temp_source)
os.remove(temp_compiled)