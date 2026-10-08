---
name: auditer-dette-technique
description: Use when technical debt should be prioritized by measurable change cost, risk, and blast radius rather than aesthetics.
---
# Auditer la dette technique

## Fonction
Qualifier la dette par conséquence réelle.

## Procédure
1. Identifier zones générant régressions, duplications responsables, lenteur de changement ou impossibilité de test.
2. Mesurer appelants, dépendances, fréquence de modification et incidents liés lorsque disponibles.
3. Évaluer blast radius et coût de ne rien faire.
4. Classer : dette active, dette tolérable, préférence esthétique ou inconnu.
5. Ne proposer un chantier que si le gain attendu dépasse le coût et le risque de modification.

## Preuve
Chaque dette prioritaire possède une conséquence, un périmètre et un critère de réduction.