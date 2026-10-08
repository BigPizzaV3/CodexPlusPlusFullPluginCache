---
name: gerer-quotas-et-pression
description: Use when rate limits, queues, concurrency, backpressure, Retry-After, or overload can alter execution.
---
# Gérer quotas et pression

## Fonction
Gérer quotas et pression sans retry aveugle.

## Procédure
1. Identifier quotas, concurrence, files, délais et coût d’une répétition.
2. Respecter signaux serveur tels que Retry-After lorsqu’ils existent.
3. Choisir backoff, jitter, backpressure, abandon ou réduction de débit selon le système réel.

## Preuve
La reprise respecte les limites et n’introduit ni doublon, ni boucle, ni surcharge supplémentaire.
