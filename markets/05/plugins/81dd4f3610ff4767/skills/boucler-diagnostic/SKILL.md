---
name: boucler-diagnostic
description: Use when a technical defect needs iterative diagnosis and a fast deterministic feedback signal can be constructed.
---
# Boucler un diagnostic

## Fonction
Faire progresser le diagnostic par falsification rapide plutôt que par accumulation d’hypothèses.

## Procédure
1. Construire le signal pass/fail le plus rapide et déterministe possible.
2. Classer les hypothèses par pouvoir explicatif et coût de falsification.
3. Instrumenter ou bisecter une hypothèse à la fois lorsque possible.
4. Réexécuter le signal après chaque modification pertinente.
5. Conserver les hypothèses réfutées pour éviter les retours en arrière inutiles.
6. Élargir l’instrument seulement si le signal courant ne départage plus les causes.

## Preuve
Chaque itération réduit l’espace des causes ou établit une limite explicite.