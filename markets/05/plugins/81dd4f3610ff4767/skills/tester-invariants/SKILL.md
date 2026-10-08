---
name: tester-invariants
description: Use when a function has stable invariants that can be explored more effectively with generated cases than with a few hand-picked examples.
---
# Tester les invariants

## Fonction
Chercher automatiquement des contre-exemples à des propriétés stables.

## Procédure
1. Formuler l’invariant indépendamment de l’implémentation lorsque possible.
2. Définir domaine de génération, contraintes et cas pathologiques.
3. Générer des entrées et réduire les contre-exemples trouvés.
4. Reproduire tout échec avec une graine ou un cas minimal stable.
5. Conserver les exemples de régression qui apportent une protection distincte.

## Preuve
Aucun cas généré dans le domaine éprouvé ne viole l’invariant, ou un contre-exemple reproductible est fourni.