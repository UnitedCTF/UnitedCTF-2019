# Python Obfuscator
## Lore
Vous voulez distribuer vos programmes Python mais vous avez peur pour votre PROPRIÉTÉ INTELLECTUELLE? Utilisez notre service de compilation de code source! Afin de mieux vous servir, nous avons implémenté un offuscateur de chaînes de caractères. Il vous suffit de préfixer les chaînes de caractères à offusquer par `PWN`, comme ceci:

```python
print(PWN"allo")
```

## Description
L'offuscateur utilise un module Python en C pour offusquer les strings. Le but est d'exploiter le buffer overflow dans la fonction d'offuscation. Le stack cookie est donné lorsque l'input est assez grand, pour que ça soit plus simple.

Un client de base en Python 3 est fourni pour éviter au gens d'avoir à implémenter le protocole.

Les [indices](#Indices) seront tous donnés dès le départ pour que ça soit moins intimidant.

## Indices

## Solution
Envoyer une string de la forme suivante au serveur:

```python
PWN"{PADDING}{COOKIE}{RBP}{ROPCHAIN}"
```

```
PADDING: 'a' * 1032
COOKIE: donné par le serveur
RBP: n'importe quoi
ROPCHAIN: Une rop chain qui écrit /bin/sh à quelque part (e.g: bss) puis retourne vers system.
```

Puisque Python 3 ne vient pas avec du code _position-independent_ par défaut (du moins sur Ubuntu), on peut simplement utiliser des gadgets qui se trouvent dans le binaire de Python pour construire une rop chain et retourner vers system (voir [la solution](/solve.py)).

## Flag
Voir le fichier `flag`.