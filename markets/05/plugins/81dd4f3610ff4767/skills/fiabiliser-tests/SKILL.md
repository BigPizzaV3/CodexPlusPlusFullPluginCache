---
name: fiabiliser-tests
description: Use when a test is flaky, timing-sensitive, intermittently failing, or suspected of producing unreliable evidence.
---
# Fiabiliser les tests

## Fonction
Réparer la cause d’instabilité du test sans masquer le signal.

## Procédure
1. Reproduire la variabilité sur plusieurs exécutions contrôlées.
2. Classer : race, timing, dépendance externe, donnée périmée, ordre, sélecteur, fuite d’état ou environnement.
3. Instrumenter le premier point où les exécutions divergent.
4. Corriger synchronisation, isolation ou dépendance responsable.
5. Ne jamais augmenter arbitrairement un délai comme preuve de correction.
6. Rejouer suffisamment pour établir la stabilité utile.

## Preuve
Le test redevient un signal fiable et la cause d’instabilité est identifiée ou explicitement bornée.