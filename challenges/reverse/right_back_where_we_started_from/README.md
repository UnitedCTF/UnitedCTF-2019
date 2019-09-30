# Right back where we started from

## Description

Ton collègue, frustré par ses conditions de travail, a decidé de supprimer tout le code source du projet sur lequel vous travailliez avant de démissionner. Heureusement pour vous, il a oublier de supprimer l'exécutable. Êtes-vous en mesure de finaliser le projet?

[Exécutable](./flag)

## Solution

Le but du défi est de recupérer le contenu de la variable "flag", qui n'est pas utilisée. Une façon simple pour recupérer les strings d'un programme est avec la commande "strings".

`strings flag | grep -i "flag"` retourne le flag.

## Flag

FLAG-lov31sg00d
