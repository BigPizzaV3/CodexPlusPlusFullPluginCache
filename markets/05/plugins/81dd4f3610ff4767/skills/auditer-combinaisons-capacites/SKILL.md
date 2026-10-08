---
name: auditer-combinaisons-capacites
description: Use when individually acceptable tools or permissions can become dangerous when chained in one plan.
---
# Auditer les combinaisons de capacités

## Fonction
Analyser le risque du graphe d’actions, pas seulement celui de chaque outil isolé.

## Procédure
1. Énumérer les capacités nécessaires au trajet et les données qu’elles peuvent recevoir ou produire.
2. Chercher chaînes lecture sensible → réseau, écriture → exécution, génération → publication, ou autre composition à risque.
3. Identifier où une sortie non fiable peut influencer une capacité plus puissante.
4. Réduire permissions, casser la chaîne, ajouter validation ou isoler l’étape lorsque nécessaire.
5. Refaire le pré-vol sur le plan modifié.

## Preuve
Le plan ne contient aucune combinaison de pouvoirs non justifiée par le besoin et l’autorité.