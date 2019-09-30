# Are you modular?

## Lore

Connais-tu bien ton arithmétique modulaire? Si oui, tu n'auras pas de problème à décrypter le flag de ce serveur ;)

## Description

C'est une implémentation du premier challenge du set 6 sur Cryptopals. Il y a un serveur qui décrypte tous les messages RSA encryptés (sans padding) sauf le flag
lui-même. Le but est de trouver un moyen de décrypter le flag. Le flag encrypté est donné à l'utilisateur.

## Solution
Pour réussir à décrypter le flag, il faut multiplier le flag encrypté par un nombre au hasard exposant e, décrypter le résultat, puis multiplier par l'inverse modulaire du nombre choisi:

```
s: nombre au hasard
i: inverse de s (mod n)

flag ** e == flag encrypté
s ** e * flag encrypté == s ** e * flag ** e
s ** e * flag ** e == (s * flag) ** e

Lorsqu'on le décrypte:
((s * flag) ** e) ** d == s * flag (c'est le principe de RSA)

Lorsqu'on multiplie par l'inverse:
i * s * flag == flag
```

En réalité, ça ne marche pas à tous les coups, mais on peut facilement trouver la vraie solution en essayant plusieurs nombres jusqu'à temps qu'on tombe sur le même plaintext deux fois. En règle générale, ça prend moins de 10 essais, donc ce n'est vraiment pas un challenge de brute-force.

## Hints

- Tout le code est donné

## Flag

FLAG-0842294041f07e101130252ff4e8840e