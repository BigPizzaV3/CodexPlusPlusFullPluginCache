---
name: reproduire-bug
description: Use when a reported defect, screenshot, symptom, or complaint should be reduced to a reproducible case before correction.
---
# Reproduire un bug

## Fonction
Transformer un symptôme en scénario reproductible minimal.

## Procédure
1. Capturer environnement, version, préconditions et état initial.
2. Écrire la plus courte séquence d’actions reproduisant le défaut.
3. Séparer résultat attendu et observé.
4. Mesurer fréquence et conditions de non-reproduction lorsque utiles.
5. Conserver logs, capture ou état machine seulement s’ils discriminent le défaut.
6. Réduire encore le cas tant que la réduction conserve le bug.

## Preuve
Un tiers peut provoquer ou constater l’absence du défaut avec le même scénario.