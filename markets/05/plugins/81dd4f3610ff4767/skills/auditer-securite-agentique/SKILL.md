---
name: auditer-securite-agentique
description: Use when an agent, plugin, MCP, or autonomous workflow gains enough tools or authority that its own attack surface must be reviewed.
---
# Auditer la sécurité agentique

## Fonction
Évaluer les risques créés par les capacités d’un agent et leur orchestration.

## Procédure
1. Inventorier outils, fichiers, réseau, credentials, écritures et effets externes accessibles.
2. Cartographier frontières de confiance et sources pouvant injecter des instructions.
3. Chercher exfiltration, excessive agency, confused deputy, escalade d’autorité et effets irréversibles.
4. Vérifier moindre privilège, pré-vol, confirmations réservées et séparation lecture / écriture.
5. Appeler `auditer-combinaisons-capacites` pour les chaînes de pouvoirs dangereuses.
6. Produire findings avec scénario d’abus et mitigation vérifiable.

## Preuve
Chaque risque important possède un chemin d’exploitation plausible ou une raison documentée de rejet.