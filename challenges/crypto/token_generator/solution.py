#!/usr/bin/env python3
import requests
import base64
import string
import re

URL = "http://127.0.0.1:7545/"

possible_flags = ["FL"]


while True:

    flag = possible_flags.pop()

    size_map = {}

    for c in string.printable:

        params = { "data": (flag + c) * 5 }
        response = requests.get(URL, params=params)
        text = response.text
        token = re.findall("<h4>Generated token :</h4><b>(.+?)</b>", text)[0]

        token_raw = base64.b64decode(token)
        size_map[c] = len(token_raw)

    # No difference in compression size
    if len(size_map.values()) == 1:
        continue

    smallest_size = min(size_map.values())
    possible_values = [k for k in size_map.keys() if size_map[k] == smallest_size]

    if len(possible_values) > 10:
        continue

    for value in possible_values:
        possible_flags.append(flag + value)

    print(possible_flags)
