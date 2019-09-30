# Le mur de Berlin

## Description

9 novembre 1989, Berlin.

« Les voyages privés vers l'étranger peuvent être autorisés sans présentation de justificatifs — motif du voyage ou lien de famille. Les autorisations seront délivrées sans retard. »

Il ne reste plus qu'à abolir le mur vous séparant de la liberté.

## Solution

Le participant est accueilli par un jeu, où il peut apercevoir un drapeau derrière un mur. 
Il ne peut pas traverser le mur dû à la collision.

En inspectant l'onglet "Network" de Chrome, on s'apercoit que le client notifie un serveur de la position du joueur à chaque déplacement, il s'agit en fait d'un jeu multijoueur!

Puisque le client est responsable d'envoyer sa position au serveur, rien ne l'empêche d'envoyer des coordonées situées de l'autre côté du mur!

Pour se faire, il faut pouvoir écrire dans le WebSocket. Il y a plusieurs façon de le faire, j'ai opté pour utiliser celui déjà initialisé dans le code javascript du jeu.

En utilisant le formatteur de Chrome, on peut rapidement trouver la variable du WebSocket grâce aux fonctions de l'api qui sont utilisées, notamment "send()".

On peut mettre un breakpoint quand la connexion est ouverte et utiliser le socket depuis la console:

```
d.send(JSON.stringify({x:8, y:4}))
```

Le flag est imprimé dans la console quand on touche le drapeau.

## Flag

FLAG-FR33D0M4TL4ST
