# Synesthésie

## Description

Mon ami Mido m'a récemment confié qu'il était atteint d'un phénomène neurologique bien étrange, celui de la synesthésie. Selon lui, celle-ci lui permet de voir des couleurs et parfois même des images à partir de sons. Il me dit qu'il peut voir une image 40x8 à partir de ce fichier audio. Je ne suis pas convaincu, peux-tu vérifier s'il dit bien la vérité?

[Fichier audio MIDI](./flag.mid)

## Solution

Le but de ce défi est de transformer le midi fourni en une image de format spécifié.

Pour y arriver, il fallait que le participant trouve la page wikipédia sur la synesthése.
Celle-ci décrit qu'il existe un type de synesthésie pour lequel chaque son est associé à une couleur. Le participant devait en déduire que chaque note unique présente dans le fichier représentent une couleur.

Avec la librairie python Mido, on peut itérer sur les notes du fichier MIDI sequentiellement. Il y avait 8 notes présente dans le MIDI, celle de la gamme de do, et pour chacune des notes dans la gamme, on pouvait assigner une couleur arbitraire doté d'un contraste relatif élevé.

Ensuite, à l'aide de la libraire Pillow en python, on peut reconstruire l'image avec les pixels de l'étape précédente.

Du code python permettant de générer un MIDI à partir d'une image et vice-versa est fourni en annexe.

## Annexe

[Synesthésie](https://fr.wikipedia.org/wiki/Synesth%C3%A9sie)

[PNG vers MIDI](./png_to_midi.py)

[MIDI vers PNG](./midi_to_png.py)

