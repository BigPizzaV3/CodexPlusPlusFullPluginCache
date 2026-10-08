---
name: gerer-transactions
description: Use for any external action whose accidental repetition or partial completion could create duplicates, loss, spending, extra deletion, multiple sends, or other material effects.
---
# Gérer transactions, idempotence et rejeu

## Procédure
1. Donner une identité d’opération stable avant le premier effet.
2. Déterminer ce qui est répétable, déduplicable, idempotent, observable avant rejeu, annulable ou non annulable.
3. Après interruption ou réponse ambiguë, rechercher l’état réel avant tout rejeu d’une action non répétable.
4. Identifier le point où chaque effet devient réel.
5. Conserver explicitement tout état partiel non atomique.
6. N’utiliser compensation ou restauration que si elles existent réellement, sont autorisées et n’aggravent pas le dommage.
7. Ne jamais promettre « exactement une fois » sans mécanisme qui le prouve.

## Preuve
L’état final ou partiel de chaque effet est qualifié et aucun rejeu aveugle n’a eu lieu.