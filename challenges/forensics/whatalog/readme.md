# Mais quel log!

## Description

À notre université, on a appris que certaines transactions un peu _shady_ se passaient dans le dos de la communauté étudiante. On a essayé de soutirer de l'information dans divers départements de l'université. L'intel qu'on a accumulé décrit que les transactions passent par un serveur de l'université et qu'une faille permettait de récupérer quelques logs.

On a récupéré les logs, mais on a de la difficulté à les interpréter. On se demande vraiment si on peut prendre de l'information controversée là-dedans.

## Résolution

Le but de ce défi est de trouver le flag dans le log en utilisant de la programmation.

Le flag est dissimulé avec neuf autres chaînes de mêmes longueurs et chaque chaîne a été convertie en binaire.

Il est à noter que le [`pinger`](./generator/pinger.js) ajoute les bits 0 au début de l'octet afin de donner un format uniforme. Ces octets doivent être enlevés si on veut parser le log adéquatement.

Le [solver](./solver.js) convertit le log en une chaîne binaire, puis en une chaîne de caractère. Ensuite, il divise la chaîne obtenue en 10 morceaux et retourne le flag dès qu'il le trouve. Au moment de l'écriture du challenge, le flag était l'avant-dernier _morceau_.

### Le générateur

Le générateur fonctionne en deux modules: le [serveur](./generator/server.js) et le [pinger]('./generator/pinger.js). Le serveur s'occupe de logger toutes les requêtes dans le fichier [`requests.log`](./requests.log). Le pinger s'occupe de fournir l'information nécessaire au serveur en créant les 10 blocs.

Ainsi, si on doit régénérer le log. Il faut partir le serveur et ensuite lancer le pinger. Avant de faire l'un ou l'autre, assurez-vous de lancer `npm install`.

### Flag

`flag-$0N7b3Nvv31rd¢3510G1@k01`
