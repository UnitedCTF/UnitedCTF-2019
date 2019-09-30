#!/bin/bash

docker build . --cpuset-cpus 0-7 -t search-pwn

