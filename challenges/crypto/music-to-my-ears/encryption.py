#!/usr/bin/env python3
import struct

#
# L'oreille humaine peut entendre les fréquences entre 20 Hz et 20 kHz, ce qui donne 19980 fréquences.
# 19980 ^ 6 == 63 616 958 720 959 616 064 000 000
# Le NIST recommande d'utiliser des mots de passe d'au moins 8 caractères.
# Il y a 95 caractères affichables.
# 95 ^ 8 == 6 634 204 312 890 625
# 63 616 958 720 959 616 064 000 000 >>> 6 634 204 312 890 625, ce qui prouve clairement que les clés sont impossibles à brute-forcer.
# C.Q.F.D.
#
# Analysé par: Ti-Bob
#

def make_key(frequencies):
    frequencies = [int(f) ^ 0xffff for f in frequencies]

    key = b""

    for f in frequencies:
        key += bytes(struct.pack("<H", f))
    
    return key

def encrypt(message, frequencies):
    key = make_key(frequencies)
    plaintext = message.encode()
    ciphertext = bytes([b ^ k for k, b in zip(plaintext, key * (len(plaintext) // len(key) + 1))])
    return ciphertext