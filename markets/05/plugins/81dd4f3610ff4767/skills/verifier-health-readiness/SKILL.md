---
name: verifier-health-readiness
description: Use when a component may be alive but not ready, healthy, functional, or able to accept work.
---
# Vérifier health readiness

## Fonction
Distinguer vie, santé, disponibilité et readiness.

## Procédure
1. Définir ce que signifient alive, healthy, ready et functional pour le composant.
2. Choisir des checks discriminants reliés aux dépendances critiques.
3. Éviter les probes qui prouvent seulement le processus lui-même.

## Preuve
Chaque état annoncé correspond à une preuve spécifique et utile.
