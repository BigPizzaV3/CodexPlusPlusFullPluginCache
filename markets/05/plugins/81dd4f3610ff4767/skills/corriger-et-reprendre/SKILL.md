---
name: corriger-et-reprendre
description: Use when an error, regression, failed attempt, patch stack, or long risky operation needs a correction rooted in observed evidence.
---
# Corriger et reprendre

## Fonction
Revenir à une racine prouvée, corriger la cause avec le plus petit delta compatible puis vérifier séparément changement et non-régression.

## Protocole opératoire
1. Nommer l’écart observé, l’état attendu et la dernière racine prouvée.
2. Construire `DELTA` = ce qui doit changer et `PRESERVE` = ce qui doit rester vrai.
3. Appeler `reproduire-bug` puis `boucler-diagnostic` ou `traiter-retour-technique` jusqu’à une cause suffisamment établie pour prédire l’effet du correctif.
4. Ne jamais affaiblir un test, masquer une erreur ou modifier le critère de preuve pour faire passer le correctif.
5. Si plusieurs rustines s’empilent sans stabilisation, revenir à la dernière racine prouvée au lieu d’ajouter une nouvelle couche.
6. Définir une condition de rollback avant mutation lorsque le geste est risqué; utiliser `gerer-reprise` et `gerer-transactions` lorsque nécessaire.
7. Appliquer le plus petit correctif compatible avec la cause comprise.
8. Vérifier le `DELTA` puis le `PRESERVE` séparément; après une erreur concrète, exiger deux voies de vérification réellement indépendantes.
9. Utiliser `fiabiliser-tests` et `verifier-acceptation` avant de qualifier la correction comme réussie.
10. Si le résultat reste ambigu, ne pas rejouer aveuglément et ne pas déclarer corrigé.

## Preuve
La cause est suffisamment établie, le delta attendu est prouvé, le préservé à risque n’a pas régressé et aucun filet temporaire n’est conservé sans fonction.
