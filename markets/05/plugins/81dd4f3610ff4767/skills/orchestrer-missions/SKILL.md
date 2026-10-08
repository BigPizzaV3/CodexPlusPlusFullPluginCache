---
name: orchestrer-missions
description: Use when a Continuum task involves Noyau, Passerelle, Magistri Operis, slots, mission delegation, CREATE/CALL, queues, or mission-result routing.
---
# Orchestrer les missions

## Fonction
Préserver la mission comme transaction corrélée entre matière, acteur, signal, effet observable et résultat, sans figer une ancienne topologie.

## Protocole opératoire
1. Vérifier qu’une délégation est réellement utile; ne pas créer une mission pour une action simple réalisable directement.
2. Appeler `orchestrer-magistri`, `preparer-mission-magister` et `choisir-topologie-delegation` selon le besoin.
3. Résoudre depuis l’état actuel l’acteur, le slot, la génération, la conversation et la matière; ne jamais identifier un acteur par position visuelle.
4. Préparer la matière et le courrier avant le signal; la Passerelle transporte le signal, pas toute la matière métier.
5. Distinguer création d’une nouvelle conversation et appel d’une conversation existante; ne jamais substituer silencieusement l’une à l’autre.
6. Donner une identité stable aux opérations susceptibles d’être rejouées et appliquer `gerer-transactions`.
7. Émission, réception, exécution, dépôt et effet observé restent des états distincts.
8. Une opération ambiguë devient `INCERTAIN`; réconcilier l’effet réel avant tout replay.
9. Un résultat de mission n’est `COMPLETED` qu’après dépôt réellement observé et corrélé à la mission.
10. Pour les handoffs techniques, utiliser `transmettre-handoff-technique`; pour la clôture, `clore-mission-magister`; pour la grammaire Passerelle, `appeler-passerelle`.

## Invariants
PAUSE, STOP, disponibilité et identité des slots sont résolus depuis le système courant; aucun nombre, nom ou syntaxe historique n’est imposé par mémoire.

## Preuve
La mission possède une corrélation durable suffisante, aucune émission ambiguë n’a été rejouée aveuglément et le résultat final est relié au bon acteur et au bon effet.
