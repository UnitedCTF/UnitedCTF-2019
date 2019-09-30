# Family Tree
## Lore

Je suis en train de faire un site pour créer des arbres généalogiques. Pour respecter la vie privée, je chiffre les abres pour éviter que les autres les voient. Toutefois, je ne suis pas capable de les déchiffer. Le serveur affiche toujours l'erreur suivante:

```
An error happened while decrypting your family tree.
```

Je n'arrive pas à trouver le bug... Peux-tu le trouver à ma place? J'ai un raid à WoW Classic dans 30 minutes.

## Description

Le site chiffre les "arbres généalogiques" avec AES en mode CTR. Un bug dans la création des arbres fait en sorte
que le nonce utilisé pour chiffrer l'arbre est le mot de passe du dernier ancêtre dans la liste.

Il y a déjà deux comptes enregistrés: Lucy et son ancêtre eukaryotes. Le flag est placé à la fin de la string de l'arbre de Lucy.

Il est possible de voir la version chiffrée des arbres des autres utilisateurs en visitant leur profil.

## Hints

- Tout le code source est donné, sauf `config.php`.

## Solution

Le nonce utilisé pour chiffrer le flag peut être réutilisé en mettant eukaryotes comme dernier ancêtre de la liste.
Il suffit de faire un arbre généalogique assez long pour obtenir le keystream utilisé par Lucy, et ainsi être capable de déchiffrer le flag.

## Flag

- FLAG-f78ab0fd1b5b3c0cd2223318303017d4