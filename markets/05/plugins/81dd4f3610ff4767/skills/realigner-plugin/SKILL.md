---
name: realigner-plugin
description: Use when the canonical Protocol is already valid but the Continuum plugin source, tests, published version, installed version, or loaded behavior is behind or inconsistent.
---
# Réaligner le plugin

## Fonction
Corriger l’implémentation sans modifier le canon pour s’adapter à une version en retard.

## Procédure
1. Identifier précisément le delta entre canon et implémentation.
   Examiner les responsabilités et règles de toutes les compétences affectées, leurs raccords, la traçabilité, les sources de contexte, les scénarios, les manifestes et la documentation active. La correction des titres ou du nombre de Documents n’est qu’un cas partiel.
2. Distinguer source, tests statiques, paquet construit, Draft publiée, version Released, installation et comportement réellement chargé.
3. Modifier uniquement les couches d’implémentation concernées.
4. Mettre à jour la traçabilité et les tests capables d’empêcher la régression.
   Préserver les fonctions spécialisées et les coordinateurs utiles ; ne pas supprimer des responsabilités pour faire correspondre une matrice au seul découpage documentaire.
5. Ne pas demander à Axel de revalider le canon lorsqu’aucune matière normative ne change.
6. Éprouver la version réellement chargée avant de déclarer le comportement aligné.

## Preuve
Aucun delta matériel connu ne subsiste entre le canon applicable et la couche déclarée alignée.
