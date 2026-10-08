---
name: synchroniser-miroir
description: Use only when a secondary representation must be reconciled with a Source Canonique write already established on its authoritative path.
---
# Synchroniser le miroir

## Fonction
Réconcilier une représentation secondaire avec une écriture unique de la Source Canonique. Cette synchronisation n’est pas une seconde écriture applicative et ne rend jamais un miroir concurrent.

## Procédure
1. Résoudre avec `resoudre-demeures` la matière, le chemin faisant autorité et la représentation secondaire concernée.
2. Établir l’écriture canonique unique sur le chemin autoritaire ; protéger la concurrence si nécessaire. Pour une opération ordinaire, un retour explicite de succès suffit.
3. Déterminer si la concordance secondaire est réellement nécessaire à la reprise, à la migration, à la sécurité ou au diagnostic. Si elle ne l’est pas, ne pas lancer de synchronisation rituelle.
4. Lorsqu’elle est nécessaire, vérifier ou réconcilier cette représentation depuis l’état établi sur le chemin autoritaire, sans réécrire le canon depuis le miroir.

## États partiels
- échec du chemin autoritaire : la représentation secondaire ne redéfinit pas l’état ;
- écriture autoritaire réussie, représentation secondaire échouée ou inconnue : qualifier la concordance comme non établie sans inverser l’autorité ;
- divergence secondaire : ne jamais la réinjecter automatiquement dans l’état autoritaire ; qualifier toute matière supplémentaire avant retrait.

## Représentation locale
Google Drive et `D:` sont deux accès à la même Source Canonique ; selon le chemin d’écriture alors autoritaire, l’autre reste la représentation à réconcilier. Cette opération n’est ni un second canon ni une source autorisée pour pousser automatiquement une divergence vers l’état autoritaire.

## Périmètre
Le périmètre est résolu depuis l’Index et les demeures de la Source Canonique. Un lien, une route, un chemin cité ou un montage externe n’étend jamais ce périmètre. Une proposition ou un chantier reste hors représentation tant qu’il n’est pas devenu matière canonique.

## Preuve
L’état du chemin autoritaire et sa représentation sont concordants lorsque cette concordance est nécessaire, ou l’écart reste explicitement qualifié sans inversion d’autorité.
