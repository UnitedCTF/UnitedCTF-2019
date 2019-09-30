# Mosh it

## Description

On essaye présentemment d'intercepter toutes les communications provenant d'un réseau interne. Cependant, depuis quelques jours, les utilisateurs et les utilisatrices s'envoient des fichiers assez bizzares. On a réussi à retirer [un fichier audio](./message.wav), mais en l'écoutant, on a eu vraiment mal aux oreilles.

En surveillant le réseaux, on a aussi constaté que les messages étaient cryptés. On a décrypté l'un de ses messages et ça disait simplement :_tord les données_.

## Disclaimer

**NE LISEZ PAS LE FICHIER AUDIO. ÇA VA FAIRE MAL À VOS OREILLES**

## Solution

Le but de ce défi est d'utiliser les techniques de databending. Il suffit d'exporter le fichier audio en fichier .RAW et d'importer ce fichier .RAW sur Gimp.

Pour résoudre ce défi, il faut changer l'extension en `.data` ou `.raw`. En ouvrant le fichier avec GIMP, il faut spécifier le type de donnée pour être _Données d'image Raw_ (sous le bouton _Sélectionner le type de fichier_) Pour voir le fichier `.data` ou `.raw`, il faut cocher l'option _Show All Files_. On peut ensuite choisir le fichier.

Ensuite, GIMP ouvrira un petit utilitaire. Là dedans, on doit spécifier le type d'image _RVB Planar_ et mettre la largeur comme étant 2761 et la hauteur comme étant 300.

Le flag sera imprimé noir sur blanc.

N.B. les chiffres utilisés pour la largeur et la hauteur sont les dimensions de l'imagine originale.

## Annexe

[La vidéo qui m'inspire](https://www.youtube.com/watch?v=ar0n1lKwdek)

[Le fichier raw exporté à partir d'audacity](./message.raw)

[Le flag exporté sous Raw](./flag.RAW) _Ce fichier permet de reconstruire message.wav si jamais nous en avons besoin._

[le flag](./flag.png) _Le flag_
