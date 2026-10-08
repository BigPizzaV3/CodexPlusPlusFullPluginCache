---
name: auditer-etats-vide-chargement-erreur
description: Use when an interface must remain understandable outside the happy path.
---
# Auditer états vide chargement erreur

## Fonction
Auditer les états vide, chargement et erreur d’une interface.

## Procédure
1. Identifier les parcours où aucune donnée, une attente ou un échec survient.
2. Vérifier explication, action possible, récupération et conservation de l’état utile.
3. Tester accessibilité, répétition et absence de boucle.

## Preuve
L’utilisateur comprend l’état et peut poursuivre ou récupérer sans connaissance cachée.
