---
name: auditer-fraicheur-contexte
description: Use when stored instructions, versions, routes, decisions, or project context may be stale.
---
# Auditer fraîcheur contexte

## Fonction
Détecter le contexte périmé avant qu’il gouverne un nouveau travail.

## Procédure
1. Identifier les éléments contextuels dont la date ou version peut changer la conduite.
2. Comparer avec les sources responsables et l’état courant.
3. Conserver les éléments historiques seulement comme tels.

## Preuve
Le contexte utilisé pour décider est actuel ou explicitement borné comme historique/incertain.
