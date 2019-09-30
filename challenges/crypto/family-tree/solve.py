#!/usr/bin/env python3
import base64

ciphertext = "3JLLI1e+tGvvmE5XNGTft8O9Cs9ZY2vGqwTX9WwaLQwn8KV7//9aD+MK6LQqlF+yEClaVgJMTOQ1nv0+j55F"
known = "lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,lucy,eukaryotes"
known_encrypted = "1ZLDOwmrrnzzx15wPGWxic/vHq1PfmDm7SrPzFFwKDcTwPNO8N5Jecs28oBstVCcPWJMbiV4F8UUme9cotYbNlWy4oiPhmP8bDtzurC2eNJ2D50glnyWhtbKDnVnlcgjUVHJ4UIaL3NLdsVdyOmpwkVHlnsJWYPAK54mAexIXsToNGtfQbjoW8QuSIUBJHY45Niw"

ciphertext = base64.b64decode(ciphertext)
known = known.encode()
known_encrypted = base64.b64decode(known_encrypted)

keystream = [p ^ c for p, c in zip(known, known_encrypted)]
plaintext = [c ^ k for c, k in zip(ciphertext, keystream)]
plaintext = bytes(plaintext).decode()
print(plaintext)

flag = plaintext.split("|")[-1]
flag = base64.b64decode(flag).decode()
print(flag)