# Tomographie

## Description

Notre équipe médicale perd son temps à faire de l'analyse tomographique d'objets de tous les jours. Notre patron est en colère et voudrait savoir l'objet qui a été utilisé dans cet analyse. Pourrais-tu l'aider?

[Analyse Tomographique](./ct_scan.gif)

## Solution

La [tomographie](https://fr.wikipedia.org/wiki/Tomographie) est une technique d'imagerie où une image 3D est découpée en tranche 2D.
Le fichier fourni contient une tranche 2D du modèle 3D recherché par image du GIF. À l'aide d'un script Python et de Numpy (fourni en annexe), on peut reconstruire une matrice 3D et changer l'axe de visionnement. Le modèle 3D est du texte qui contient le flag.
![flag](./decoded.gif)

## Flag

FLAG-6938704a7db9bdb33c26dffa31f498e5

## Annexe

[Decodeur tomographique](./decode.py)
