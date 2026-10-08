---
name: auditer-architecture
description: Use when structural friction, excessive coupling, shallow modules, or poor navigability may be causing recurring defects or change cost.
---
# Auditer l’architecture

## Fonction
Évaluer l’architecture par son coût réel de compréhension, de changement et de test.

## Procédure
1. Partir de `cartographier-code` et de scénarios de changement concrets.
2. Chercher interfaces trop larges, responsabilités dispersées, modules superficiels, dépendances circulaires et seams mal placés.
3. Mesurer où une modification simple exige des changements disproportionnés.
4. Distinguer dette structurelle et préférence de style.
5. Proposer le plus petit déplacement de frontière qui réduit durablement la friction.

## Preuve
Chaque recommandation est reliée à un scénario de maintenance, de test ou de panne observable.