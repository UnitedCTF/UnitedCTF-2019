#!/bin/bash
set -B

rm -rf obfuscator obfuscator.tar.gz
mkdir -p obfuscator{/codec,/hackme}

make

cp codec/{client.py,hackme.so,server.py,target.py} obfuscator/codec
cp hackme/hackmemodule.c obfuscator/hackme
cp Makefile obfuscator/Makefile
tar -caf obfuscator.tar.gz obfuscator