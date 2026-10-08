---
name: gerer-depreciation
description: Use when a function, API, route, command, configuration, or compatibility path is being retired or replaced.
---
# Gérer une dépréciation

## Fonction
Retirer une fonction seulement après avoir prouvé que ses consommateurs peuvent survivre.

## Procédure
1. Inventorier consommateurs réels et contrats dépendants.
2. Définir remplacement, période de coexistence si nécessaire et stratégie de migration.
3. Observer les usages restants lorsqu’un signal fiable existe.
4. Migrer ou adapter les consommateurs avant suppression.
5. Retirer l’ancien chemin seulement lorsque le critère de fin est prouvé.
6. Vérifier absence de régression et supprimer le bruit devenu sans fonction.

## Preuve
Aucun consommateur matériel connu ne dépend encore de la fonction supprimée.