---
name: detecter-derive-configuration
description: Use when desired configuration and observed runtime configuration may diverge.
---
# Détecter dérive configuration

## Fonction
Détecter la dérive entre configuration voulue et état observé.

## Procédure
1. Identifier source de configuration attendue et points d’application.
2. Lire l’état effectivement chargé.
3. Comparer valeurs, provenance et temporalité.

## Preuve
La configuration gouvernant le comportement est connue ou la divergence est explicitement bornée.
