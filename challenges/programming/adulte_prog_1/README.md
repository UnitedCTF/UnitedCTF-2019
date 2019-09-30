# Adulte prog 1

## Description

Il y a beaucoup de compétitions informatiques au Québec et dans les environs.
Le Conseil Étudiant pour l'Évaluation des Compétitions Informatiques des Clubs Officiels Nationaux (CÉÉCICON)
a récemment sorti les mesures de conversion officielles pour comparer le niveau de
plaisir obtenu lors de chaque compétition informatique.

Ce fichier (`conversions.txt`) est sous cette forme:

`unitéSource unitéDestination multiplicateur`

Par exemple:

`unitedCTF csGames 0.002`
 
Se lit comme suit: "un `unitedCTF` vaut 0.002 `csGames`s"

Vous devez construire un programme qui effectue les conversions
dans `aConvertir.txt` et qui somme le résultat de chaque conversion.
Arrondir le résultat à un chiffre après le point.

Les conversions à effectuer ressemblent à ça:

`244 LHGames coveoBlitz`

Se lisant comme: "244 `LHGames`s valent combien de `coveoBlitz`s?" 

Flag format: `FLAG-<totalDeLaSomme>`

Ex: `Flag-42.68`

## Solution

voir solution.py

Référence https://medium.com/@alexgolec/google-interview-problems-ratio-finder-d7aa8bf201e3

## Flag

FLAG-132235345.7
