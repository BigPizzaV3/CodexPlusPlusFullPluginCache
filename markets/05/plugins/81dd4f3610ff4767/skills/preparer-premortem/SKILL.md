---
name: preparer-premortem
description: Use before a materially risky, destructive, public, difficult-to-reverse, or multi-step operation to expose likely failure modes in advance.
---
# Préparer un pré-mortem

## Fonction
Chercher comment l’opération pourrait échouer avant de produire l’effet.

## Procédure
1. Lister les modes d’échec capables de produire perte, incohérence, doublon ou indisponibilité.
2. Pour chacun, définir signal de détection et moment où il devient observable.
3. Définir conditions d’arrêt, restauration ou compensation réellement disponibles.
4. Vérifier qu’un état partiel peut être distingué d’un succès.
5. Ajouter au plan les contrôles dont le gain de sûreté justifie le coût.

## Preuve
Les pannes matérielles prévisibles ont un détecteur et une conduite explicite.