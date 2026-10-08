---
name: gerer-mise-a-jour-dependances
description: Use when upgrading a library, runtime, SDK, tool, model dependency, or package can change compatibility or supply-chain risk.
---
# Gérer une mise à jour de dépendances

## Fonction
Évaluer une montée de version comme une migration à risque proportionné.

## Procédure
1. Identifier version actuelle, cible et raison matérielle de l’upgrade.
2. Lire changements, ruptures, advisories et contraintes de plateforme.
3. Examiner lockfile, dépendances transitives et scripts d’installation.
4. Vérifier licence, coût et supply chain avec `qualifier-skill-externe` lorsque pertinent.
5. Tester les comportements consommateurs représentatifs.
6. Prévoir rollback ou restauration de l’état précédent.

## Preuve
La version cible est compatible avec les usages réellement testés et ses risques nouveaux sont qualifiés.