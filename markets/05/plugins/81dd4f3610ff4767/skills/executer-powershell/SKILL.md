---
name: executer-powershell
description: Use when a Continuum task requires designing, reviewing, handing off, or interpreting PowerShell work for Axel’s Windows environment.
---
# Travailler avec PowerShell

## Fonction
Traiter PowerShell comme un environnement technique réel du Continuum, pas comme du pseudo-code générique.

## Procédure
1. Résoudre la version et l’environnement réellement visés avant de concevoir ; ne pas supposer qu’un comportement PowerShell moderne vaut pour Windows PowerShell 5.1 ou inversement.
2. Consulter le Savoir PowerShell pertinent avant un travail substantiel et rechercher ce qui manque lorsqu’une construction n’est pas suffisamment maîtrisée.
3. Produire le moins de gestes manuels compatible avec le besoin : un seul script ou lanceur lorsque cela remplit réellement la fonction, plutôt qu’une succession de commandes décoratives.
4. Préserver les chemins, identifiants et chaînes techniques exacts lorsqu’ils appartiennent réellement à l’environnement courant ; ne pas figer comme vérité durable une route seulement historique.
5. Instrumenter les opérations critiques pour obtenir au minimum les sorties et états capables de distinguer succès, échec, timeout et étape fautive ; stdout, stderr et code de sortie sont conservés lorsqu’ils apportent la preuve utile.
6. Sur retour d’Axel, appeler `traiter-retour-technique` et corriger le premier défaut réellement établi plutôt qu’empiler des hypothèses.
7. Une exécution sur le PC n’est acquise qu’après preuve du retour réel ; un fichier `.ps1` créé n’est pas une exécution.

## Preuve
Le script est compatible avec l’environnement visé au niveau prouvé, le geste demandé à Axel est minimal, et le retour technique permet d’observer l’effet réellement obtenu.