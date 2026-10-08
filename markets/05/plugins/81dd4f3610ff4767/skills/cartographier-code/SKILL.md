---
name: cartographier-code
description: Use before a non-trivial code change when the location, callers, dependencies, data flow, or blast radius are not already established.
---
# Cartographier le code

## Fonction
Trouver où vit réellement une fonction et ce qui dépend d’elle avant de la modifier.

## Procédure
1. Localiser points d’entrée, handlers, modules et données concernés.
2. Remonter appelants, appels sortants, dépendances et états partagés.
3. Identifier frontières d’interface et contrats traversés.
4. Repérer tests, configurations et migrations liés.
5. Produire une carte minimale orientée modification, pas un diagramme décoratif.

## Preuve
La correction peut nommer les fichiers / modules touchés, les consommateurs à préserver et les tests représentatifs.