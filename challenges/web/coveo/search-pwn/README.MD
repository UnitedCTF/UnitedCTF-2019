# SearchPwn
## Description pour participants
### Level 1
On nous a envoyé ce client pour l'application SearchPwn. Il semble aller chercher ses données sur un site web quelque part. Pouvez-vous le trouver?

**Indice**: Il y a plusieurs facon de réussir ce challenge. Vous pouvez reverse le client, ou tout simplement intercepter les communications (ce n'est pas encrypté)
### Level 2
Maintenant que vous avez trouvé le site, pouvez-vous accéder à la page d'administration?

**Indice**: Vous aurez probablement besoin de recevoir des requetes HTTP. Un outil comme celui-la vous aidera : https://requestinspector.com/
### Level 3
Bonjour Admin :D
Votre but est maintenant de créer un lien vers un résultat de recherche qui fait apparaitre "Coveo is awesome!" en haut des résultats. Une fois que vous avez trouvé comment faire, aller dans le panel d'admin pour faire valider votre lien par le système.

**Indice**: Les résultats de recherche sont affichés vraiment rapidement. Il doit y avoir une cache quelque part.

## Solutions
Cette track se déroule en 3 niveaux. Le premier niveau est simplement de déterminer l'url du site web. On peut le trouver dans le client web, ou intercepter les calls HTTP avec un proxy. Une fois le site trouvé, on trouve le flag dans la page d'accueil du site.

Pour le deuxième niveau, il faut voler le cookie au robot administrateur. On remarque que l'enregistrement au mailing liste est vulnérable à un XSS (sans aucun filtrage). On a donc simplement besoin d'un script qui exfiltre le cookie de l'admin, puis de lui envoyer le lien malicieux pour vérification. On trouve le flag dans les cookies de l'administrateur.

Pour le troisième niveau, il faut lire le code source qui est envoyé. On remarque qu'en tant qu'admin, on peut ajouter un header "withTag", et que celui-ci n'est pas validé, et donc vulnerable aux CRLF injection. On a simplement à ajouter 2 sauts de ligne (CRLFCRLF), et le contenu désiré pour empoisonner la cache et obtenir le résultat voulu. En validant la recherche, on obtient le 3e flag.

## Flags
- Flag1 : flag-SKf8tdzTIY7p9pgDoAXVoBQN74gga92lEX0yr1Na
- Flag2 : flag-Nbbif49YiJJNkx7QzhXdWTwCFb7NUpSBtqt2FPHf
- Flag3 : flag-HzrWPmMFt6xSAcFrUVo5yRN5zuyTT5qg6hq1TlcG
## Organisation
### Installation locale
- npm install -g flow-remove-types@^1.2.3 flow-typed@^2.5.1 flow-bin@^0.78.0 yarn
- yarn
- run ./build.sh
- run ./start.sh
### Installation Docker
- docker-compose build
- docker-compose up
### Debuging endpoint
Un mode debug est accessible au path /debug/* et contient 4 endpoints : 
- /debug/cache
- /debug/stats
- /debug/clear-group
- /debug/clear-cache

Pour y accéder, setter comme query param 'token=<valeur_du_token>'. La valeur est écrite dans le fichier token.txt (et peut-être changée)
Le mode debug permet d'inspecter la cache des utilisateurs et de la clear. La cache est par utilisateur pour éviter de contaminer les autres participants.
Vous pouvez changer le port du bind 
### Changer le port/hostname du challenge web
Si vous voulez changer le port et le hostname, il faut les ajuster dans le docker-compose pour que le client soit lié au site web. 3 paramètres existent dans le docker-compose.yml. Prenez note que le client s'execute à partir du context du participant, donc penser à inclure le protocole https si approprié.
