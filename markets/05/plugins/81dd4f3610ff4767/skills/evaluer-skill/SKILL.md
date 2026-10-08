---
name: evaluer-skill
description: Use when a Skill must be proven useful, correctly triggered, and non-regressive before release.
---
# Évaluer un Skill

## Fonction
Éprouver le comportement réel d’un Skill au-delà de sa lecture statique.

## Procédure
1. Définir cas positifs, négatifs et limites de déclenchement.
2. Comparer lorsque possible le même travail avec et sans le Skill.
3. Mesurer réussite, erreurs, latence, coût de contexte, répétitions et variance utiles.
4. Vérifier qu’il n’empiète pas sur un Skill voisin et qu’il sait ne pas se déclencher.
5. Répéter les cas critiques après modification.
6. Remettre les résultats à `auditer-alignement` pour la qualification de release.

## Preuve
Le Skill améliore le comportement attendu sans introduire de collision ou de régression matérielle.