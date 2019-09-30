# Hextraordinaire

## Description

Bon, bon, bon. J'ai un autre flag que je peux te montrer. Cette fois-ci, j'ai utilisé des technologies hextraordinaire! D'ailleurs, j'ai encore été capable de faire ça depuis mon navigateur.

`66 6c 61 67 2d 63 33 24 70 40 24 74 40 6e 74 2b 30 62 24 63 75 72 33 6c 30 6c 78 44`

## Solution

Le but de ce défi est de comprendre comment représenter une chaîne de caractère en format hexadécimal. La chaîne de caractère est encodée en UTF-16 avec Javascript, mais c'est la valeur hexadécimale qui est affiché, contrairement à [numériemagie]('../numeriemagie/README.md')

Pour résoudre ce défi, on peut utiliser le one-liner suivant :

```js
"66 6c 61 67 2d 63 33 24 70 40 24 74 40 6e 74 2b 30 62 24 63 75 72 33 6c 30 6c 78 44"
  .split(" ")
  .map(x => String.fromCharCode(parseInt(x, 16)))
  .join("");
```

## Flag

`flag-c3$p@$t@nt+0b$cur3l0lxD`
