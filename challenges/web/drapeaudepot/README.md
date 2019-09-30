# Drapeau Dépot

## Description

Nos contacts ont identifié un site web utilisé pour la contre-bande de drapeau. Serais-tu en mesure de t'infiltrer?

## Solution

En cliquant sur le lien, le participant fait face à une page statique HTML. Après avoir exploré le site, il devrait être en mesure de trouver la section "A propos". Parmi les mises à jour se retrouve une entrée qui dit: "Migration de Subversion vers Git.". Avec cet indice, le participant doit être en mesure de trouver le répertoire `/.git` qui est visible publiquement.

Avec la commande `wget -r <url>/.git`, le participant peut télécharger le contenu du dossier sur sa machine.

Ensuite, avec le dossier `.git` de téléchargé, le participant peut visionner les commits avec `git log`. Un des secrets a pour message:

> add secret

En le visionnant avec `git show <commit_id>`, on trouve le flag.

## Flag

FLAG-e93ccf5ffc90eefcc0bdb81f87d25d1a

