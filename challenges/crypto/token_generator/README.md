# Token Generator

## Description

Ceci est une démo pour notre service générateur de jetons.

Il permet aux utilisateurs de générer des jetons compressés et chiffrés contenant des données spécifiées par l'utilisateur.

Pour détecter toute altération, nous avons ajouté un indicateur secret après les données.

## Solution

Le code source de l'application nous décrit un service qui prend notre entrée utilisateur et y ajoute un $FLAG, pour ensuite le compresser et le chiffrer.

Le fait de compresser des données qu'on contrôle avant de le chiffrer introduit une faille nous permettant de déterminer ce que la variable $FLAG contient indirectement.

Par exemple, pour un flag "FLAG{abcd}" et une entrée utilisateur "FLA", le fait de compresser
"FLAFLAG{abcd}" va générer une chaîne de caractère plus petite que la chaîne "ZKLFLAG{abcd}" (dû à la chaîne répétée FLA).

Cette différence de taille peut être utilisée pour déterminer le flag :

1. Envoyer un caractère à la fois de `a-zA-Z0-9{}_`
2. Mesurer la taille du jeton chiffré résultant
3. Le caractère générant le plus petit jeton est un caractère du flag.
4. Répéter #1 avec le prochain caractère

```python
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
```

## Flag

FLAG{unh4ck4bl3_eh}

