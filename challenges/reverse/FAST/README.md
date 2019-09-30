# FAST!

## Description

Le comité du United CTF a décidé de développer un outil pour faire la validation des flags sur les ordinateurs des participants.

Pour prevenir toute tentative de retro-ingénierie, nous avons fait part d'une méthode d'encryption hors du commun!

[FAST!](./FAST)

## Solution

Avec gdb-peda, on peut inspecter l'état du programme pendant son exécution.

Lorsqu'on exécute le programme avec gdb, on peut voir une string étrange sur la stack, ("FMCJ1|n;|h>jy@\201\202\032"), qui semble être le flag encodé.

On peut confirmer cette théorie en observant la boucle, qui compare les caractères de l'entrée utilisateur et de cette string un à la fois.

De ce point, on peut prendre deux chemins, soit essayer de comprendre l'algorithme qui transforme l'entrée utilisateur, ou faire l'analyse cryptographique de cette chaine de caractere.

Approche cryptographique: sachant que le flag doit commencer par "FLAG", on peut comparer les caractères "FMCJ" à "FLAG":

"F" == "F"
"L" == "M" - 1
"A" == "C" - 2
"G" == "J" - 3

On peut appliquer ce modèle pour le reste de la chaine de caractère pour retrouver le flag.

Approche de rétro-ingénierie:

Avec IDA, on peut voir que le compteur de boucle est placé dans [rbp+var_5C], et que celui-ci est placé dans rbx au début de la boucle. 

Ensuite, rbx est comparé à rax, le résultat de strlen. C'est la vérification qu'on n'a pas atteint la fin de la string.

Dans le prochain bloc, il y a les instructions:

```
movzx  eax,BYTE PTR [rbp+rax*1-0x30]
mov    edx,eax
```

L'addresse [rbp-0x30] fait réference à la string de l'utilisateur, rax est le compteur de boucle.

On peut vérifier dans GDB, Le premier caractère qu'on a entré apparait dans eax, ensuite edx.

Par la suite, on aperçoit:

```
mov eax, [rbp+var_5C]
add eax, edx
```

On place le compteur de boucle dans eax et on additionne notre caractère par celui-ci.

```
mov     [rbp+var_5D], al
```

On place notre caractère à l'adresse [rbp+var_5C]

```
movzx   eax, byte ptr [rbp+rax+var_50]
```

On place le caractère de la string suspicieuse ("FMCJ1...") dans eax

```
cmp     [rbp+var_5D], al
```

On compare le caractère de la string suspicieuse au caractère qu'on a additionné, additionné du compteur de boucle.

Grâce à cette analyse, on sait maintenant qu'il faut soustraire chaque caractères de la string suspicieuse par son index pour retrouver le flag.


## Flag

FLAG-wh4t_4_m3ss
