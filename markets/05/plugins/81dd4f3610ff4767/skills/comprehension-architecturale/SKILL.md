---
name: comprehension-architecturale
description: Use when a Continuum request spans several components, responsibilities, authorities, dependencies, or execution layers and needs an explicit architectural decomposition.
---
# Compréhension architecturale

## Fonction
Préserver l’ancienne capacité de lecture architecturale comme coordinateur de compatibilité, sans créer un second bootstrap concurrent.

## Protocole opératoire
1. L’entrée normale du plugin reste portée par `amorcer-continuum`; ne pas rendre ce Skill obligatoire à chaque tour.
2. Reformuler intérieurement l’objectif réel, les objets touchés, les dépendances, inconnus, autorités et preuves attendues.
3. Appeler `charger-contexte-continuum` pour le contexte pertinent puis `executer-demande` pour l’exécution.
4. Utiliser `modeliser-domaine` lorsque la structure conceptuelle manque et `construire-plan` lorsque plusieurs dépendances matérielles doivent être ordonnées.
5. Séquence si dépendance réelle; parallélisme seulement si les branches sont indépendantes et n’écrivent pas la même cible.
6. Conserver les branches déjà prouvées lors d’un changement de contexte; ne recalculer que ce que le nouveau fait invalide.
7. Une contradiction structurante, un manque d’autorité ou un inconnu bloquant reste visible et remonte au coordinateur approprié.
8. Pour les capacités locales, ne jamais inventer une route : appeler `choisir-capacites` puis `agir-par-noyau` si le Réel l’exige.

## Invariants
Ce Skill ne remplace ni `amorcer-continuum`, ni les spécialistes, ni l’identité du Continuum. Il ne déclenche aucune Passation ou écriture terminale par réflexe.

## Preuve
Le trajet retenu correspond à l’architecture réellement touchée, les dépendances sont cohérentes et chaque branche obligatoire possède une autorité et une cible de preuve explicites.
