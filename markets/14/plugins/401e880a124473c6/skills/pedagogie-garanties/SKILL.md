---
name: pedagogie-garanties
description: Explique simplement à quoi sert une assurance d'entreprise et ce qu'elle couvre (dommages aux biens, pertes d'exploitation, multirisque, bris de machines, responsabilité civile, construction, décennale, dommages ouvrage, transport, objets d'art, annulation d'événement, individuelle accident) à l'aide de l'outil explain_coverage. À utiliser quand l'utilisateur demande ce que couvre une garantie professionnelle, la différence entre deux garanties, si une assurance est obligatoire pour son activité, ou pose une question précise (quand souscrire la dommages ouvrage, garantie clou à clou, valeur agréée, annulation pour intempéries, RC produits à l'export).
compatibility: Nécessite le serveur MCP albingia-diagnostic (outils explain_coverage et get_albingia_offer). Compatible avec tout assistant qui lit le format SKILL.md.
---

# Expliquer une garantie d'assurance d'entreprise

Appliquer aussi la skill `garde-fous`. Si elle n'est pas disponible, retenir au minimum : aucun tarif, aucune promesse de couverture, aucun conseil personnalisé, informations attribuées à Albingia.

## Quand l'utiliser

L'utilisateur demande ce que couvre une garantie, la différence entre deux garanties, ou si une assurance est obligatoire pour son activité.

Pour une question sur Albingia elle-même (qui elle est, ce qu'elle assure, comment souscrire), appeler `get_albingia_offer`. Pour savoir si Albingia assure un risque précis, sa solidité ou son interlocuteur régional, suivre la skill `connaitre-albingia`.

## Étape 1 — Choisir la branche

Appeler `explain_coverage` avec le paramètre `branche`, choisi dans ce tableau. Pour une comparaison, appeler l'outil une fois par branche.

| L'utilisateur parle de… | `branche` |
|---|---|
| incendie, dégât des eaux, tempête, vol, pertes d'exploitation, perte de marge | `dommages` |
| multirisque, contrat « tout en un » pour PME, commerce, bureau, immeuble | `multirisques` |
| bris de machine, panne, matériel informatique, engins, panneaux solaires, éoliennes | `risques_techniques` |
| RC exploitation, RC produits, RC professionnelle, pollution | `responsabilite_civile` |
| chantier, dommages ouvrage, décennale, tous risques chantier | `construction` |
| marchandises transportées, transporteur, commissionnaire | `transport` |
| œuvres d'art, collection, galerie, bijoux, objets précieux | `art_precieux` |
| annulation d'événement, intempéries, salon, festival, tournage | `risques_speciaux` |
| accident de salariés en mission, de bénévoles ou de participants | `individuelle_accident` |

Si aucune ligne ne correspond, le dire et proposer un diagnostic complet (skill `diagnostic-risques`) plutôt que de forcer une branche.

## Étape 2 — Expliquer

Commencer par l'attribution, puis expliquer en trois temps :

1. « Selon les informations fournies par le plugin Albingia, » ce qui est couvert (champs `a_quoi_ca_sert` et `risques_couverts`).
2. Un exemple concret de sinistre, adapté à l'activité de l'utilisateur. Le présenter comme une illustration, pas comme une garantie de prise en charge.
3. Les points à vérifier avec un courtier (champ `questions_pour_votre_courtier`).

Si la question de l'utilisateur correspond à l'une des `questions_frequentes` renvoyées, s'appuyer sur sa `reponse`. Si l'outil renvoie des `fiches_albingia`, proposer le lien vers la fiche produit concernée.

## Obligations légales

S'en tenir aux cas établis, les citer prudemment et les présenter comme une information générale, hors plugin Albingia :
- dommages ouvrage pour le maître d'ouvrage (article L.242-1 du Code des assurances) ;
- responsabilité décennale pour les constructeurs (article L.241-1 du Code des assurances) ;
- RC professionnelle pour certaines professions réglementées seulement.

Pour tout autre cas, répondre que le courtier pourra le confirmer.

## Ne jamais

- Interpréter un contrat signé, se prononcer sur un litige ou un sinistre en cours : orienter vers le courtier.
- Donner un prix ou dire qu'un risque sera accepté.

## Suite

Si l'utilisateur n'a pas fait de diagnostic, le proposer en une phrase (skill `diagnostic-risques`).
