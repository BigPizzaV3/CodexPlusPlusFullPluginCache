---
name: prevention
description: Donne les conseils de prévention d'Albingia à une entreprise (outil get_prevention_guide) - incendie d'entrepôt, permis de feu et travaux par point chaud, événement en plein air, vol ou intempéries sur un chantier. À utiliser quand l'utilisateur demande comment réduire ou prévenir un risque de sinistre dans son activité.
compatibility: Nécessite le serveur MCP albingia-diagnostic (outil get_prevention_guide). Compatible avec tout assistant qui lit le format SKILL.md.
---

# Prévention des sinistres

Appliquer aussi la skill `garde-fous`. Si elle n'est pas disponible, retenir au minimum : aucun tarif, aucune promesse de couverture, informations attribuées à Albingia.

## Étape 1 — Choisir le sujet

| L'utilisateur parle de… | `sujet` |
|---|---|
| incendie, entrepôt, stockage | `incendie_entrepot` |
| permis de feu, point chaud, soudure, meulage, découpe | `permis_feu` |
| festival, événement en plein air, chapiteau, intempéries | `evenement_plein_air` |
| vol ou intempéries sur un chantier, travaux | `chantier` |

Si aucune ligne ne correspond, ne pas appeler l'outil : répondre avec prudence, en précisant que ces conseils ne viennent pas d'Albingia (« En complément, hors plugin Albingia : … »).

## Étape 2 — Restituer

1. Appeler `get_prevention_guide` avec `sujet`.
2. « Selon l'ingénierie prévention d'Albingia, » puis les `points_cles` sous forme de liste courte.
3. Rappeler que les mesures exigées par un contrat figurent dans ce contrat et que le courtier peut les préciser.
