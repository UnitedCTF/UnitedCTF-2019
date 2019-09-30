<img src="./static/images/logo-2.png" width="200" />

# Music to my Ears
## Lore

Mon ami qui habite à L.A. m'a envoyé ce message:

```
Of all the music-based crypto implementations, this one takes the crown. The cryptographers did some sterling work on this!

It's really easy to use too. All I know about piano is the Bb major scale and I was still able to encrypt this flag:

9LiAtj3c7N+mheXXgpb2ySSJv9j81OHZ08WjxyTd4oimguODhw==

I bet it's impossible to decrypt! I'll even give you the flag's MD5 hash. It's 31698d2f20acbd898abc8a4b5dfa648f.
```

Il parlait de ce site: (site du challenge).

Quelque chose me dit que leur cryptographie est moins bonne qu'il pense.

Flag format: `FLAG-...`

## Description

Le site encrypte un message à l'aide des 6 notes de piano choisies et du _tuning_.

Connaissant le format du flag (il commence par `FLAG`), il est possible de trouver tous les _tunings_
qui auraient pu être utilisés, ainsi que les 2 premières notes.

Il reste maintenant 4 notes  à trouver. Il serait techniquement possible d'essayer les 88 notes possibles, mais ça serait long
(~1h en Python sur mon laptop). Pour réduire le nombre de notes possibles, il faut utiliser le fait que notre ami ne connait que la gamme de
Bb majeure. Cela nous donne 51 notes utilisables, ce qui se brute-force très facilement.

## Hints

- Tout le code source est donné.
- La description est importante.
- La solution en Python prend environ 5 minutes à rouler. Si votre script prend plus de temps, il vous manque quelque chose.

## Flag

- FLAG-3749c760b784fd3c238a1b6429c9d1b5
- Notes: F5, A5, C6, Eb6, G6, Bb6
- Tuning: 1823