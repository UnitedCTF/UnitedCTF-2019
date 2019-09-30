# Numériemagie

## Description

On a encrypté notre flag en utilisant des technologies Numérimagique! Je suis même prêt à le mettre ici! En plus, j'ai utilisé une solution simple que je pouvais le faire de mon navigateur.

`102,108,97,103,45,99,51,36,48,98,36,99,117,114,51`

## Solution

Le but de ce défi est de comprendre les différentes façons de représenter une chaîne de caractère. La chaîne de caractère est encodée en UTF-16 avec Javascript.

Pour résoudre ce défi, il faut seulement utiliser le one-liner suivant :

```js
"102,108,97,103,45,99,51,36,48,98,36,99,117,114,51"
  .split(",")
  .map(x => String.fromCharCode(x))
  .join("");
```

## Flag

`flag-c3$0b$cur3`
