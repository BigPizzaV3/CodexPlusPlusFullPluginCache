---
name: tester-agent-multisurface
description: Use when an agentic workflow must be verified across several surfaces such as UI, API, database, logs, files, or messages.
---
# Tester un agent sur plusieurs surfaces

## Fonction
Éprouver le comportement bout en bout lorsqu’aucune surface seule ne suffit à prouver le résultat.

## Procédure
1. Définir état initial, action, effets attendus et sources de preuve par surface.
2. Exécuter le scénario avec une identité d’opération stable si nécessaire.
3. Observer UI, API, données, fichiers et logs uniquement là où ils apportent une preuve distincte.
4. Rendre `PASS`, `FAIL`, `BLOCKED` ou `ABORTED` avec preuves et limites.
5. Ne pas déclarer PASS sur le seul succès d’un appel intermédiaire.

## Preuve
Le statut final est reconstructible depuis les observations réellement collectées.