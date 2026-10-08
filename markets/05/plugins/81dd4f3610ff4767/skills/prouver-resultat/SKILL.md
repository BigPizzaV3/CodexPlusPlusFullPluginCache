---
name: prouver-resultat
description: Use when an important state, effect, installation, correction, completion claim, absence claim, or non-regression must be asserted or challenged.
---
# Prouver le résultat

## Fonction
Lier chaque affirmation importante à une observation suffisante dans le bon périmètre, sans promouvoir un niveau de statut par narration.

## Protocole opératoire
1. Décomposer les affirmations vagues en claims contrôlables avec objet, périmètre, environnement et moment de vérité.
2. Distinguer au minimum créé, installé, configuré, lancé, joignable, fonctionnel, E2E prouvé et validé; aucun état n’implique automatiquement le suivant.
3. Appeler `qualifier-preuve` et `verifier-affirmation-source` sur chaque claim important.
4. Une documentation prouve ce qui devrait être possible, pas l’état local réel; une sortie de commande ne prouve que ce qu’elle mesure.
5. Un claim d’absence exige un périmètre exhaustif; sinon dire seulement « non trouvé dans le périmètre recherché ».
6. Une preuve touchée par une mutation ultérieure devient périmée pour l’état courant jusqu’à nouvelle vérification.
7. Enregistrer les preuves contraires au lieu de les lisser; une contradiction connue bloque le statut `PROUVE` du claim concerné.
8. Après correction, vérifier séparément `DELTA` et `PRESERVE`; après une erreur concrète, obtenir deux vérifications indépendantes par mécanismes ou chemins de défaillance distincts.
9. Ne jamais muter ou détruire un objet uniquement pour fabriquer une preuve lorsqu’une observation non destructive suffit.
10. Pour une clôture globale, appeler `verifier-acceptation`; toutes les exigences bloquantes doivent être prouvées et les inconnus bloquants fermés.
11. Arrêter quand le seuil de preuve nécessaire est atteint; rigueur ne signifie pas vérification compulsive.

## Preuve
Chaque claim important possède un statut borné par ses observations réelles, ses contradictions et sa fraîcheur, et aucune clôture n’est annoncée au-delà de ce qui est effectivement prouvé.
