---
name: choisir-topologie-delegation
description: Use when work may be split across multiple Magistri Operis or delegated agents and the dependency shape must determine the orchestration strategy.
---
# Choisir la topologie de délégation

## Fonction
Adapter la forme de l’orchestration au travail réel.

## Procédure
1. Cartographier sous-objectifs, dépendances et états mutables partagés.
2. Choisir séquence, pipeline, fan-out, scout + worker ou revue parallèle selon cette carte.
3. Paralléliser uniquement les missions réellement indépendantes ou suffisamment isolées.
4. Minimiser le coût de coordination et les risques de conflit.
5. Définir le point de synthèse et la preuve finale avant lancement.

## Preuve
Chaque relation parallèle ou séquentielle est justifiée par une dépendance réelle du plan.