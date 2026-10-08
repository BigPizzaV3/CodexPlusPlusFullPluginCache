---
name: proteger-concurrence
description: Use before modifying any object that may also be read or changed by another actor, tool, process, conversation, or execution.
---
# Protéger les états partagés

## Outil partagé — règle transitoire
Selon `09 — Sûreté, transactions et reprise.md`, tant qu’Axel n’a pas validé l’orchestration concurrente du plugin, un outil, connecteur ou application externe partagé n’est utilisé activement que par un acteur à la fois. Une autre fenêtre, session ou processus ne contourne pas cette exclusivité. Si sa disponibilité n’est pas établie, attendre sa libération ou utiliser un autre moyen autorisé.

Le plugin du Continuum est exempté pendant sa construction, ses essais et sa validation. Cette exception ne lève ni autorité, ni coût, ni idempotence, ni protection des états. Le parallélisme sur des outils différents reste possible.

## Procédure
1. Lire l’état courant et capturer le meilleur repère disponible : version, révision, ETag, empreinte, génération, horodatage ou équivalent.
2. Pour une écriture partagée, canonique, destructive ou difficilement récupérable, vérifier au moment d’écrire que l’état visé n’a pas changé matériellement. Une écriture ordinaire isolée ne déclenche pas ce contrôle.
3. Si l’objet a changé matériellement, ne pas l’écraser : relire, qualifier les différences et réconcilier ou replanifier.
4. Utiliser verrou, bail ou écriture conditionnelle lorsqu’ils existent et apportent une protection réelle, avec le périmètre et la durée minimaux.
5. Si un conflit ne peut pas être suffisamment détecté pour une écriture canonique, destructive ou difficilement récupérable, bloquer plutôt qu’écraser aveuglément.
6. Libérer toute réservation inutile ; un verrou expiré, perdu ou contredit ne confère aucun droit ni aucune autorité canonique.

## Preuve
Aucune écriture partagée n’écrase silencieusement un état concurrent.
