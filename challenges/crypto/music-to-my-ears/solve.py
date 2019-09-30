#!/usr/bin/env python3
import base64
import hashlib
import struct

from progressbar import progressbar

def frequency(n, t = 440):
    return (2 ** (1 / 12)) ** (n - 49) * t

def make_key(frequencies):
    frequencies = [int(f) ^ 0xffff for f in frequencies]

    key = b""

    for f in frequencies:
        key += bytes(struct.pack("<H", f))
    
    return key

ciphertext = "9LiAtj3c7N+mheXXgpb2ySSJv9j81OHZ08WjxyTd4oimguODhw=="
ciphertext = base64.b64decode(ciphertext)
known = ciphertext[: 4]
tunings = []
known_keys = {}

print("Finding possible tunings...")

for t in progressbar(range(320, 2101)):
    for n1 in range(1, 89):
        for n2 in range(1, 89):
            if n1 == n2:
                continue
            
            f1 = frequency(n1, t)
            f2 = frequency(n2, t)

            key = make_key([f1, f2])
            plaintext = bytes([(b ^ k) for b, k in zip(known, key)])
            
            if plaintext == b"FLAG":
                tunings.append(t)
                known_keys[t] = [n1, n2]

print("Possible tunings: %s" % ",".join(str(t) for t in tunings))

key_increments = [2, 2, 1, 2, 2, 2, 1]
start_key = 2
possible_keys = []

i = 0
key = start_key
while key <= 88:
    possible_keys.append(key)
    key += key_increments[i]
    i = (i + 1) % len(key_increments)

for t in tunings:
    print("Trying %d Hz" % t)

    for a in progressbar(possible_keys):
        for b in possible_keys:
            for c in possible_keys:
                for d in possible_keys:
                    keys = known_keys[t] + [a, b, c, d]

                    frequencies = [frequency(k, t) for k in keys]
                    key = make_key(frequencies)
                    plaintext = bytes([(b ^ k) for b, k in zip(ciphertext, key * 10)])

                    if hashlib.md5(plaintext).hexdigest() == "31698d2f20acbd898abc8a4b5dfa648f":
                        print(f"\n{plaintext}")