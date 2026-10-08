---
name: gerer-git
description: Use when source-control operations, branches, worktrees, merges, conflicts, or release preparation materially affect a Continuum task.
---
# Gérer Git

## Fonction
Utiliser Git comme mécanisme de sûreté et de collaboration, pas comme simple stockage de fichiers.

## Procédure
1. Lire branche, état de travail, base et modifications existantes avant écriture.
2. Isoler le travail par branche ou worktree lorsque cela réduit réellement les collisions.
3. Préserver les changements non liés et ne jamais écraser silencieusement un travail concurrent.
4. Résoudre les conflits par sens et tests, pas par choix mécanique d’un côté.
5. Avant fusion, vérifier diff, tests nécessaires et état de destination.
6. Nettoyer branches / worktrees seulement après preuve qu’ils n’ont plus de fonction.

## Preuve
Le changement est traçable, réversible au niveau permis par Git et ne détruit pas un état non lié.