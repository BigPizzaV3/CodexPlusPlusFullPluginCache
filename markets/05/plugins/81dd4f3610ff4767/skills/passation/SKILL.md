---
name: passation
description: Use when Axel explicitly requests a Passation or when a controlled reprise after saturation or conversation change materially requires Continuum continuity state.
---
# Passation

## Fonction
Conserver l’entrée historique `passation` comme coordinateur de compatibilité vers la mécanique moderne de Continuité, sans créer un second système de reprise.

## Protocole opératoire
1. Distinguer `REPRISE` et `EMISSION`; une continuation ordinaire n’est jamais une émission de Passation.
2. Ne pas déclencher une reprise par réflexe au premier tour; l’utiliser seulement sur demande explicite ou manque matériel de continuité.
3. Pour préparer une émission, appeler `executer-pre-passation` puis `executer-passation`.
4. Pour reprendre une Passation existante, appeler `reprendre-passation`.
5. Appeler `gerer-continuite` pour résoudre les états de continuité réellement responsables et `tenir-histoire` uniquement lorsque le passé causal durable est nécessaire.
6. Ne jamais reconstruire un passé plausible lorsqu’une source de continuité réelle peut être lue.
7. Une trace extérieure potentiellement périmée reste une trace jusqu’à vérification du Réel actuel.
8. Les transformations durables suivent `capitaliser` et `gerer-canonicalite`; aucune duplication canonique de convenance n’est créée.
9. L’exact visible reste sous la responsabilité unique de `tenir-verbatim`; ce Skill n’écrit pas le Verbatim.

## Preuve
Le point de reprise ou la Passation obtenue provient des sources responsables réellement résolues, les limites et travaux ouverts restent visibles et aucun canon concurrent n’a été créé.
