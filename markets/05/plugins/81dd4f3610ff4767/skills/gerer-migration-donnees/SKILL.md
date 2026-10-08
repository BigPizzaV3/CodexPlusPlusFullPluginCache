---
name: gerer-migration-donnees
description: Use when data or schema must migrate without losing compatibility, integrity, or recoverability.
---
# Gérer migration données

## Fonction
Conduire une migration de données comme une coexistence contrôlée.

## Procédure
1. Qualifier schéma, volume, lecteurs, écrivains, contraintes et invariants.
2. Séparer évolution de schéma, backfill, bascule et retrait de l’ancien état.
3. Prévoir coexistence, verrouillage, idempotence, rollback ou forward-fix selon le réel.

## Preuve
L’état migré est cohérent, les invariants sont vérifiés et la stratégie de récupération est réelle.
