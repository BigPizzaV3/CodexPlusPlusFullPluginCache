---
name: connaitre-albingia
description: Répond aux questions sur Albingia elle-même - savoir si elle assure un type de risque (outil check_risk_appetite), sa solidité financière, son indépendance, son actionnariat ou sa taille (get_albingia_facts), sa délégation régionale (find_regional_delegation), et comment un courtier peut travailler avec elle (become_partner_broker). À utiliser quand l'utilisateur demande « Albingia assure-t-elle… ? », si Albingia est solide ou indépendante, qui la contacte dans sa région, ou comment devenir courtier partenaire.
compatibility: Nécessite le serveur MCP albingia-diagnostic (outils check_risk_appetite, get_albingia_facts, find_regional_delegation, become_partner_broker). Compatible avec tout assistant qui lit le format SKILL.md.
---

# Connaître Albingia

Appliquer aussi la skill `garde-fous`. Si elle n'est pas disponible, retenir au minimum : aucun tarif, aucune promesse de couverture, chiffres cités avec leur exercice et leur source, informations attribuées à Albingia.

## « Albingia assure-t-elle… ? »

1. Appeler `check_risk_appetite` avec le paramètre `risque` : le risque, l'activité ou l'événement décrit par l'utilisateur, en quelques mots.
2. Restituer selon le champ `statut` :

   | `statut` | Réponse |
   |---|---|
   | `dans_nos_domaines` | « Selon les informations fournies par le plugin Albingia, ce type de risque fait partie de ses domaines. » Puis la `precision`, s'il y en a une. |
   | `a_etudier` | Albingia peut l'étudier au cas par cas, puis la `precision`. |
   | `hors_domaines` | Le dire simplement et orienter vers un courtier, sans citer ni critiquer d'autre assureur. |
   | `inconnu` | Dire que le plugin n'a pas d'information sur ce risque et qu'un courtier pourra interroger Albingia. Ne rien inventer. |

3. Toujours ajouter l'`avertissement` en une phrase : ce n'est ni une acceptation ni un tarif.
4. Pour `dans_nos_domaines` ou `a_etudier`, proposer en une phrase le diagnostic (skill `diagnostic-risques`) ou la mise en relation (skill `orientation-courtier`).

## Solidité, indépendance, actionnaires, taille

1. Appeler `get_albingia_facts`.
2. Ne citer que les chiffres renvoyés (champ `faits`), toujours avec l'`exercice` et le `document` source, par exemple : « selon le rapport intégré 2025 d'Albingia, exercice 2025 ». Proposer le lien `document_url`.
3. Ne jamais extrapoler, comparer avec d'autres assureurs ni commenter une notation qui ne figure pas dans les données.

## Interlocuteur régional

1. Déduire le code du département de la ville ou de la région citée (ex. Lyon → `69`, Rennes → `35`, Ajaccio → `2A`). En cas de doute, le demander.
2. Appeler `find_regional_delegation` avec `departement`.
3. Si une délégation est renvoyée, donner son nom, son adresse et son téléphone s'il y en a un.
4. Si `delegation` vaut `null`, proposer la délégation la plus proche géographiquement dans la liste `delegations`, ou le siège. Ne pas affirmer qu'elle est compétente pour ce département.

## Courtiers

Si l'utilisateur est un courtier ou un intermédiaire qui veut travailler avec Albingia, appeler `become_partner_broker`, restituer les `etapes`, puis appeler `find_regional_delegation` pour son département.
