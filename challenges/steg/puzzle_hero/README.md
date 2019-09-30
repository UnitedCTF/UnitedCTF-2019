# Puzzle hero

## Description

Voici un petit casse-tête pour passer le temps, pouvez-vous le résoudre?

[Pieces](./pieces.tar.gz)

Indices: 

- Il n'est pas nécessaire d'effectuer une rotation sur les pièces, elles ont la bonne orientation.
- Ne redimensionnez pas les images, pour des raisons confidentielles...

## Solution

Le but du défi est de reconstruire le casse-tête constitué de 100 pièces distinctes sous forme d'images. Si on essaye de reconstruire le casse-tête par une approche de backtracking, les solutions possibles seraient trop nombreuses. Il faut alors ajouter un heuristique pour déterminer quelles pièces essayer en premier, en fonction de la difference de couleur avec les pièces adjacentes. Un exemple de script implémentant ces règles est fourni en annexe.

Pour facilier la résolution, le solveur demande à l'utilisateur de confirmer chacune des pièces pour éviter des erreurs flagrantes.

Lorsque le casse-tête est résolu, on voit un indice sur l'image qui dit "LSB" pour least signifiant bit. Ceci fait référence à une technique de steganography commune.

Grâce à l'outil Stegsolve, on peut retrouver une image du flag dans le Red plane 0.

## Flag

FLAG-2D8AA42A0347C2D66CC86A0138DC9664
