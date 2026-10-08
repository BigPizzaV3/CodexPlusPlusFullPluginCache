---
name: tracer-execution
description: Use when an operational trace is materially useful for diagnosis, replay safety, recovery, or audit of machine execution.
---
# Tracer l’exécution

## Fonction
Conserver les événements opérationnels utiles sans créer un second Verbatim ni exposer le raisonnement privé.

## Peut contenir
Identité du cycle et du plan, révisions, états des tâches, capacités mobilisées, repères d’objets, effets demandés et observés, références de preuve, conflits, transactions, erreurs, corrections, rejeux évités, replanifications, décisions appliquées et état final.

## Interdits
- chaîne de pensée ou raisonnement privé ;
- narration de la conversation ;
- affirmation de réussite sans référence à une preuve ;
- écriture séparée après la persistance canonique du Verbatim et avant publication.

## Preuve
La trace permet diagnostic ou reprise sans se substituer aux objets responsables.