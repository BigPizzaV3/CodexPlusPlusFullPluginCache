---
name: prelever-verbatim
description: Use when older Continuum routing refers to the legacy Verbatim entrypoint and must be mapped to the current unique Verbatim responsibility.
---
# Prélever Verbatim

## Fonction
Compatibilité uniquement. Préserver l’ancien point d’entrée sans créer une seconde écriture terminale : **`tenir-verbatim` reste l’unique responsable actuel du Verbatim**.

## Protocole opératoire
1. Ne jamais écrire, créer, déplacer ou choisir directement une cible Verbatim depuis ce Skill.
2. Transmettre à `tenir-verbatim` le besoin de préserver l’exact visible avec l’ordre, la ponctuation et la casse utiles.
3. Ne jamais corriger les mots d’Axel, reconstruire une conversation absente ou inclure chaîne de pensée, appels d’outils ou matière interne.
4. Si la cible canonique est ambiguë ou absente, laisser `tenir-verbatim` et `gerer-canonicalite` résoudre ou borner le problème.
5. Une interruption ou un résultat ambigu ne justifie jamais un double append ou un replay aveugle.
6. Ne jamais créer un marqueur, une convention de fichier ou une règle de fin concurrente de la mécanique actuelle.

## Invariant
Deux noms de Skill peuvent coexister pour compatibilité, mais une seule responsabilité d’écriture existe : `tenir-verbatim`.

## Preuve
Tout appel à `prelever-verbatim` aboutit soit au routage vers `tenir-verbatim`, soit à une limite explicite; aucune mutation Verbatim indépendante n’est produite ici.
