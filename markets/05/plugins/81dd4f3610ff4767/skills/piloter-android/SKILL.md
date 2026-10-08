---
name: piloter-android
description: Use when a Continuum task requires observing or controlling Axel’s authorized Android device through Noyau’s local MCP/API capabilities and house relay.
---
# Piloter Android

## Fonction
Porter la branche Android du Continuum sans créer un second système de commande. Le téléphone reste un appareil autorisé de Noyau ; `@Continuum` reste la façade de travail.

## Déclenchement
Une demande exige une observation ou une action réelle sur un téléphone Android autorisé : état, informations appareil, interface, écran, presse-papiers, notifications, applications ou commandes système prévues par Noyau.

## Protocole opératoire
1. Appeler `resoudre-autorite`, `prevol-capacites`, `appliquer-cout-zero` et `agir-par-noyau` avant tout effet.
2. Exiger la présence réelle des capacités Android du MCP local/API locale de Noyau ; ne jamais déduire leur disponibilité de la seule présence de ce Skill.
3. Identifier l’appareil par la capacité de découverte Android réellement exposée ; ne jamais inventer un identifiant d’appareil.
4. Pour une lecture, exécuter uniquement l’observation nécessaire et qualifier le retour avec `qualifier-preuve`.
5. Pour une action, borner l’effet et appeler `gerer-transactions` si un rejeu pourrait produire un double effet.
6. Pour une action destructive ou difficilement réversible, appliquer l’autorité et les préconditions requises avant exécution.
7. Distinguer commande acceptée, réception par l’appareil, exécution, effet observé et résultat retourné.
8. En cas d’indisponibilité du téléphone, du relais ou du MCP local, appeler `gerer-reprise` seulement si la condition est récupérable ; sinon arrêter à la frontière prouvée.

## Partition technique
- ChatGPT / `@Continuum` porte l’intention, le routage et la méthode ;
- Noyau porte le MCP/API de contrôle en loopback sur le PC ;
- le relais Android maison porte la file de commandes et les retours ;
- le téléphone Android exécute les actions autorisées ;
- aucun fournisseur MCP/API externe n’est requis pour cette chaîne.

## Invariants
- aucun GitHub, dépôt de fichiers, backend SaaS, MCP hébergé ou API tierce ne sert de transport de commande Android ;
- aucun free tier, essai, crédit, quota gratuit ou service conditionnel n’est admissible comme dépendance d’exécution ;
- aucun secret, jeton, certificat privé, adresse figée ou identifiant d’appareil n’est porté par le Skill ;
- le transport réseau et l’authentification restent sous le capot de Noyau et du relais maison réellement chargés ;
- ne jamais présenter une action Android comme réussie sans retour terminal ou observation correspondante.

## Preuve de réussite
L’appareil réellement visé a produit le résultat demandé et ce résultat a été observé au niveau pertinent, ou la limite exacte a été établie sans effet inventé.