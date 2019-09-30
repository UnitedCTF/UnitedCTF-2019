# [Il fait beau dans le métro](https://www.youtube.com/watch?v=DcC31r1BxBY)

## Description

La STM déploie des données ouvertes sur le kilométrage réalisé par ses voitures de métro. Les données ouvertes permettent d'avoir beaucoup d'informations et de donner des statistiques assez inusités.

Les données ouvertes peuvent être trouvés [ici](http://donnees.ville.montreal.qc.ca/dataset/stm-kilometrage-realise-par-les-voitures-de-metro-de-la-stm/resource/c35e14b7-31b7-410d-9773-158bc30749df).

Alors, quel est le kilométrage des voitures MR-73 ayant roulé sur la ligne orange un jour de semaine? Le total doit être arrondi au kilomètre près.

Le flag sera la réponse précédé du mot `flag-`. Ainsi, si la réponse est 10.44 kilomètres, le flag serait `flag-10`.

## Résolution

Le but de ce challenge est d'écrire un solveur qui assimile toute les données d'un CSV et qui calcule une distance totale selon les critères établis.

Les critères sont:

- Le train doit avoir roulé sur la ligne orange
- Le train doit avoir roulé un jour de la semaine
- Le train doit être un MR-73 (défini par le type de matériel)

Le solveur peut être trouvé [ici](./solver.js).

### Flag

`flag-5131`
