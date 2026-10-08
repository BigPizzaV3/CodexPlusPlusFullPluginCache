---
name: prioriser-travail
description: Use when tasks must be ordered by dependencies, value, risk, urgency, or cost of delay.
---
# Prioriser travail

## Fonction
Prioriser le travail selon ce qui change réellement le résultat.

## Procédure
1. Identifier dépendances dures, valeur, risque, urgence et coût d’attente.
2. Repérer les tâches qui débloquent plusieurs branches.
3. Écarter la préférence pour les tâches visibles ou faciles sans fonction.
4. Pour l’Arbre du Continuum, appliquer `07 — Arbre, Branches et Feuilles.md` : une Branche poursuit la finalité définie avec Axel ; une Feuille est un axe concret de cette Branche, jamais un log, un acteur ou un outil par sa seule existence.
5. Parmi les Feuilles dont les prérequis sont satisfaits, privilégier celle nécessaire à la suite ou débloquant le montage. Suivre les états `bourgeon`, `en construction`, `en attente d’une dépendance`, `montée et intégrée` ; l’attente n’est pas une panne.
6. Suivre construction → intégration → démonstration, puis démontage ou reconstruction seulement si nécessaire. Un élément encore non construit n’est pas traité par défaut comme une régression. Remonter l’acquis utile dans la Branche avant de considérer la Feuille intégrée.
7. Azer peut ordonner les Feuilles de la finalité déjà définie ; elle ne crée ni ne change seule une Branche. Une supervision ou un contrôle doit servir une dépendance, une intégration ou un risque réel.

## Preuve
L’ordre proposé maximise la progression utile sous les contraintes établies.
