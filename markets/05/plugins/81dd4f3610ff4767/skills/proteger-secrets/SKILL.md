---
name: proteger-secrets
description: Use before committing, publishing, sharing, attaching, or logging material that may contain credentials, tokens, keys, passwords, or secret configuration.
---
# Protéger les secrets

## Fonction
Empêcher qu’un secret soit incorporé à un artefact ou canal qui ne doit pas le recevoir.

## Procédure
1. Scanner fichiers ciblés, diff, historiques utiles, logs, captures, `.env` et configurations pertinentes.
2. Distinguer secret réel, valeur factice et identifiant public.
3. Retirer ou masquer le secret avant partage sans détruire la preuve nécessaire.
4. Si un secret a déjà été exposé, qualifier l’exposition et la nécessité de rotation selon l’autorité applicable.
5. Re-scan après correction.

## Preuve
L’artefact remis ou publié ne contient aucun secret matériel détectable dans le périmètre contrôlé.