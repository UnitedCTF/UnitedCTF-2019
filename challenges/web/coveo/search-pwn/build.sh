#!/bin/bash

set -e

mkdir -p bin-client
mkdir -p bin-client/pub
mkdir -p bin-server

flow check


cp client/*.css bin-client/
cp -r client/pub/* bin-client/pub/

flow-remove-types ./client/src/ -d bin-client/
flow-remove-types -p ./server/src/ -d bin-server/
