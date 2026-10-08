---
name: gerer-workflow-durable
description: Use when a long-running workflow needs persistent steps, resumability, signals, partial errors, and human checkpoints.
---
# Gérer workflow durable

## Fonction
Modéliser un travail long comme workflow durable sans inventer une persistance absente.

## Procédure
1. Découper les étapes, états, dépendances et preuves de fermeture seulement au niveau utile.
2. Identifier ce qui doit persister entre exécutions et la capacité réellement disponible pour le faire ; mettre à jour le checkpoint courant lorsqu’un jalon rendrait la reprise matériellement fausse.
3. Prévoir signaux, reprises, délais, erreurs partielles et humains dans la boucle. Un timeout borne l’attente technique, pas le chantier.
4. Sous Gardiennage, contrôler l’échéance de relecture intégrale ; à deux heures, relire au premier point sûr sans interrompre une opération atomique, non rejouable ou risquée.

## Preuve
Le workflow peut être interrompu et repris sans rejouer aveuglément les effets non répétables.
