---
name: verifier-contrat-public
description: Use when a public API, CLI, SDK, event, schema, configuration surface, or other consumer-facing contract may change.
---
# Vérifier contrat public

## Fonction
Vérifier qu’un changement ne rompt pas une promesse consommée.

## Procédure
1. Identifier le contrat réellement consommé et ses consommateurs.
2. Comparer l’état avant/après sur signatures, schémas, comportements, erreurs et compatibilités.
3. Chercher les ruptures implicites que les tests internes peuvent manquer.

## Preuve
Les consommateurs représentatifs continuent à fonctionner ou chaque rupture est explicitement qualifiée et traitée.
