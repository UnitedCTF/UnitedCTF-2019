# Encrypt me
## Lore
Si tu es capable de chiffrer la phrase secrète, tu mérites bien le flag! ;)

## Description
Le serveur permet à l'utilisateur de chiffrer n'importe quoi sauf `I want the flag :)`.
Il faut réussir à chiffrer ce message là pour avoir le flag.

Le seul paramètre connu de la clé RSA est `e`. Il faut donc trouver le N d'une certaine façon.

## Hints
- Le fichier `app.py` est donné.

## Solution
Pour trouver `N`, il faut chiffrer plusieurs messages `(m1, m2, m3...)` et noter les messages codés `(c1, c2, c3...)`.
`N` est le plus grand dénominateur commun entre tous les `(mn ** e - cn)`.

Une fois `N` trouvé il faut juste chiffrer le message demandé par le serveur et envoyer le résultat pour avoir le flag.

## Flag
FLAG-5ac1a57a6b69ceb4ab24cf5dada9626b