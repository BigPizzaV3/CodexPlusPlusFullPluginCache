---
name: choisir-strategie-tests
description: Use when a code or behavior change needs a testing strategy matched to risk, observability, and what can actually be specified.
---
# Choisir une stratégie de tests

## Fonction
Choisir le test utile plutôt qu’imposer une méthode unique.

## Procédure
1. Identifier le comportement à protéger et son niveau de risque.
2. Choisir le niveau le plus rapide capable de prouver ce comportement : unité, intégration, contrat, end-to-end ou acceptation.
3. Utiliser TDD lorsque le comportement peut être spécifié par un test fiable avant implémentation.
4. Ajouter tests de régression pour les défauts reproductibles importants.
5. Éviter tests qui figent l’implémentation sans protéger une fonction.

## Preuve
La suite choisie ferme les risques matériels avec le minimum de redondance.