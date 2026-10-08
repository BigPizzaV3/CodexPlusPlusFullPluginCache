---
name: choisir-capacites
description: Use when several tools, Skills, plugins, connectors, local capabilities, or execution routes could satisfy the same Continuum need.
---
# Choisir les capacités

## Fonction
Choisir le trajet réel le plus adapté en séparant disponibilité, autorité, coût, effet et capacité de preuve.

## Protocole opératoire
1. Partir de l’effet ou de l’inconnue à résoudre, pas du nom d’un outil préféré.
2. Inventorier seulement les capacités réellement visibles ou prouvées dans la session.
3. Qualifier séparément `availability`, `authority`, `cost`, `side_effect`, `proofability` et dépendances.
4. Appeler `prevol-capacites`, `resoudre-autorite` et `appliquer-cout-zero` avant un trajet engageant.
5. Un accès lecture ne prouve jamais un droit d’écriture; une capacité disponible n’est jamais une autorisation.
6. Préférer le propriétaire réel de la donnée ou de l’effet et la route qui permet la preuve la plus directe.
7. Comparer les routes par simplicité globale, dépendances, sécurité, réversibilité, observabilité et preuve, pas par nombre d’outils.
8. Pour le PC ou Android, déléguer à `agir-par-noyau` puis `piloter-android` si nécessaire; le MCP/API de contrôle reste local et maison.
9. Ne jamais substituer silencieusement un moyen imposé par Axel; rendre l’alternative explicite si le moyen demandé est indisponible.
10. Un fallback n’est admissible que si l’échec principal est observable et qu’un second essai ne risque pas un double effet.

## Invariants
Un coût inconnu ne peut pas être présenté comme coût 0. Un essai, crédit ou quota gratuit conditionnel reste une contrainte à qualifier. Une option payante n’est admissible que selon le capital actif réellement disponible et les bornes de `appliquer-cout-zero` ; elle n’est jamais traitée comme gratuite par vocabulaire.

## Preuve
La capacité retenue est réellement disponible ou explicitement bornée, son autorité et son coût sont qualifiés et son trajet possède une preuve proportionnée au résultat attendu.
