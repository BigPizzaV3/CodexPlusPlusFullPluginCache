---
name: construire-plan
description: Use to transform a resolved request into the minimal complete executable plan required by the Continuum Protocol.
---
# Construire le plan exécutable

## Fonction
Compiler le trajet du cycle sans créer une nouvelle autorité.

## Procédure
1. Identifier ce qui doit être obtenu.
2. Définir les tâches nécessaires, leurs dépendances et prérequis.
3. Identifier les invariants à préserver, effets externes prévus, autorités, contraintes et moyens réellement utilisables.
4. Donner à chaque tâche un objectif, une action et un résultat attendu. Ajouter une preuve ou une vérification séparée seulement lorsqu’elle est matériellement nécessaire selon `05`.
5. Couvrir toute exigence matérielle et donner à toute tâche une fonction réelle ; ne pas ajouter de passe formelle lorsque cette couverture est évidente.
6. Retirer toute tâche sans fonction et rouvrir toute exigence sans traitement.
7. Garder le plan interne et compact : un geste avec son résultat peut suffire. Intégrer immédiatement un nouveau message d’Axel et replanifier uniquement les parties affectées.
8. Clore lorsque le résultat est suffisamment établi au regard du risque. Une tâche ordinaire au succès clair est terminée sans contrôle global systématique ; retirer tout contrôle ou changement d’outil sans gain utile.

## Raccords
Consomme le graphe de `questionner-totalement`. Mobilise les garde-fous spécialisés avant les effets.
