# Adoption Skills — candidate 0.4.0

Document non normatif.

## Objet
Cette vague transforme la Banque en implémentation source côté ChatGPT. Les fonctions classées `LOCAL` restent hors de cette adoption et ont été remises séparément pour Noyau.

## Skills ajoutés
44 spécialistes sont ajoutés dans neuf familles : gouvernance du maillage, recherche/preuve, diagnostic, tests/qualité, revue/release, sécurité agentique, orchestration, artefacts et interfaces.

## Épaississements appliqués
- `executer-demande` route vers les spécialistes sans charger toute la famille ;
- `orchestrer-magistri` choisit explicitement la topologie et peut produire un handoff technique ;
- `preparer-mission-magister` construit le contexte minimal suffisant au lieu de supposer que le destinataire possède le tchat.

## Fonctions volontairement hors plugin ChatGPT
- `piloter-boucle-magistri` ;
- `tester-interface-windows` ;
- `diagnostiquer-dotnet` ;
- `tester-dotnet` ;
- `gerer-sqlite` ;
- `surveiller-cycle-processus` ;
- `correler-execution-bout-en-bout` ;
- `modeliser-machine-etats` ;
- `verifier-interface-backend`.

Ces fonctions appartiennent à la branche locale et ne deviennent disponibles qu’après implémentation et preuve de Noyau/Passerelle.

## Statut
SOURCE INTÉGRÉE ≠ RELEASE PUBLIÉE ≠ VERSION CHARGÉE ≠ COMPORTEMENT ÉPROUVÉ.
