---
name: diagnostiquer-maillage
description: Use when the Continuum Skill mesh needs a structural health check rather than a behavioral evaluation of one Skill.
---
# Diagnostiquer le maillage

## Fonction
Détecter les défauts structurels du catalogue de Skills.

## Procédure
1. Inventorier Skills, descriptions, dépendances et routes.
2. Détecter Skills morts, doublons fonctionnels, cycles injustifiés, descriptions trop larges ou trop étroites et responsabilités orphelines.
3. Chercher collisions de déclenchement et branches chargées inutilement.
4. Comparer `skill_graph.json`, Banque, manifeste et fichiers réellement présents.
5. Produire des deltas actionnables, sans déclarer l’alignement comportemental.

## Preuve
Chaque défaut signalé possède un emplacement, une conséquence et une condition de fermeture.