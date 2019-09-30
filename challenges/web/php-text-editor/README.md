# PHP Text Editor
## Lore
Ce site-là a des gros cookies! Je me demande pourquoi?

## Description
Le site web en question sauvegarde le profil de l'utilisateur dans un cookie en sérialisant l'objet et en l'encodant en base64. L'utilisateur est confronté d'abord au refus de se faire servir des pages sous prétexte qu'il n'est pas développeur. Une fois le statut de développeur obtenu, il peut créer, éditer, renommer et supprimer des fichiers sur le serveur.

## Solution
Pour accéder au site web, l'utilisateur doit modifier son profil de façon à changer le booléen qui le rendra développeur. Ensuite, il peut obtenir le code source du site en ajoutant une fausse entrée dans sa liste de fichiers qui pointe vers les fichiers sources et en éditant ce fichier. Une fois le code source obtenu, l'utilisateur peut trouver où ses fichiers son téléversés et remarque qu'un fichier .htaccess est créé dans son dossier personnel. Pour exécuter du code, il doit d'abord supprimer le fichier .htaccess, puis créer un fichier contenant un webshell PHP.

## Flag
FLAG-4a8b6ab3ffa8c3b9085138b701ed225d