# Arcane partie IV

## Description

Bien. Nous progressons bien. Cette fois-ci, nous commencerons à monter la difficulté d'un cran. Aucune ressource en ligne n'existe, car nous avons décidé d'implémenter notre propre langage, l'arcane.

Après avoir lu les spécifications, vous pouvez trouver le programme [ici](./program.arc)

## Spécifications

- L'arcane opère avec un stack.
- Les éléments du stack sont un octet de donnée.
- Chaque insertion dans le stack se fait avec un caractère du chifre romain (I, V, X...)
- Un retour à la ligne indique la fin d'une instruction, un nombre peut être mis sur l'opération XXII.
- Le programme peut retourner une chaine de caractère grâce à la commande conséquente.
- L'arcane utilise l'extension `.arc`.

Voici ses instructions. Chaque instruction qui comprend des calculs prends les deux premières valeurs au sommet du stack et réinsère le résultat dans le stack :

- I. Ajoute les deux derniers éléments du stack
- II. Soustrait les deux derniers éléments du stack
- III. Multiplie les deux derniers éléments du stack
- IV. Divise les deux derniers éléments du stack
- V. Effectue un ET logique sur les deux derniers éléments du stack
- VI. Effectue un OU logique sur les deux derniers éléments du stack
- VII. à XIX. Aucune instruction.
- XX. Imprime le stack actuel sous forme de chaîne de caractères
- XXI. Enlève le dernier élément.
- XXII. Pousse un nouvel élément dans le stack. L'élément doit être écrit en chiffre romain, mais un élément est inséré à la fois.

## Notre programme

Le flag est caché dans ce programme. Bonne chance.

## Résolution

Contrairement aux derniers challenges, le but de ce challenge est d'écrire l'intepréteur de l'arcane. Un interpréteur peut être [retrouvé ici](./arcana.js).

### Flag

`flag-XXII.L3M@t`
