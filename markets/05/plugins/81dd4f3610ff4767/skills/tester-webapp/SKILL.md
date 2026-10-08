---
name: tester-webapp
description: Use when a web application or browser-visible workflow must be verified through an available browser or web interaction capability.
---
# Tester une application web

## Fonction
Éprouver le comportement utilisateur réel d’une surface web lorsque la capacité navigateur est disponible.

## Procédure
1. Effectuer le pré-vol de la capacité navigateur et de la session / authentification.
2. Définir état initial, action, résultat visible et effets sous-jacents à vérifier.
3. Utiliser sélecteurs et états stables plutôt que délais arbitraires.
4. Après mutation, rafraîchir l’observation avant l’assertion suivante.
5. Conserver captures seulement lorsqu’elles apportent une preuve distincte.
6. Croiser avec API ou données si l’interface seule ne prouve pas l’effet.

## Preuve
Le scénario utilisateur aboutit au résultat attendu avec observations reproductibles.