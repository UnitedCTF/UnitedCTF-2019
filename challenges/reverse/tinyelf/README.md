# Tinyelf

## Description

`./tinyelf "<FLAG>" ; echo $?` retournera 0 si \<FLAG\> est bon.

## Solution

Bien que le binaire puisse être exécuté sans problème, la plupart des déboggueurs auront de la difficulté à le désassembler et/ou à l'exécuter puisque celui-ci ne respecte pas le standard ELF. L'exception, dans les outils que j'ai testés, était radare. On peut donc décompiler le binaire dans radare pour comprendre ce qu'il fait statiquement. Tenter de trouver une solution dynamiquement est faisable, mais plutôt difficile car l'ajout d'un breakpoint change le binaire et faussera les résultats trouvés. On peut utiliser un émulateur (ie: Unicorn) pour remédier à ce problème.

Voir [Solveur](./solver.py) en annexe pour l'implémentation de la solution.

## Flag 

`FLAG{518000d944fa1db6f97fe309c9}`

## Annexe

[Solveur](./solver.py)
