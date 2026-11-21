---
name: diagnostic-risques
description: Conduit un court entretien avec un dirigeant, un responsable administratif ou un risk manager d'une entreprise établie en France pour identifier ses risques à assurer, puis restitue le diagnostic Albingia (outil diagnose_business_risks). À utiliser quand l'utilisateur demande quels risques assurer, quelles assurances professionnelles examiner, si sa couverture est complète, ou décrit son activité (atelier, usine, commerce, entrepôt, chantier, bureau, événement, etc.) en vue de s'assurer. Ne pas utiliser pour les particuliers.
compatibility: Nécessite le serveur MCP albingia-diagnostic (outils diagnose_business_risks et build_broker_brief). Compatible avec tout assistant qui lit le format SKILL.md.
---

# Diagnostic des risques d'une entreprise

Appliquer aussi la skill `garde-fous`. Si elle n'est pas disponible, retenir au minimum : aucun tarif, aucune promesse de couverture, aucun conseil personnalisé, informations attribuées à Albingia.

## Quand l'utiliser

L'utilisateur représente une entreprise, une association employeuse ou un professionnel établi en France et veut savoir quels risques assurer ou quelles assurances professionnelles examiner.

Ne pas utiliser pour l'assurance des particuliers (auto, habitation, santé individuelle) : le dire en une phrase et s'arrêter là.

## Étape 1 — Poser les questions

Poser **6 questions au plus**, en un ou deux messages, en langage simple. Ne pas redemander ce que l'utilisateur a déjà dit ou ce qui découle évidemment de son activité (un restaurant reçoit du public, un entrepôt a des stocks).

| Question à poser | Paramètre de l'outil | Valeurs |
|---|---|---|
| Votre activité, en quelques mots ? | `activite` | texte, 2 à 200 caractères |
| (déduit de l'activité, ne pas demander) | `secteur` | `industrie`, `btp_construction`, `commerce_distribution`, `logistique_transport`, `services_bureaux`, `immobilier`, `evenementiel_culture`, `energie`, `sante_medico_social`, `hotellerie_restauration`, `agriculture_agroalimentaire`, `autre` |
| Combien de salariés ? Combien de sites ? | `effectif`, `nb_sites` | `"1-9"`, `"10-49"`, `"50-249"`, `"250+"` ; entier (1 par défaut) |
| Une panne de machine arrêterait-elle l'activité ? Avez-vous des stocks de valeur ? | `machines_critiques`, `stocks_importants` | oui / non |
| Fabriquez-vous ou vendez-vous des produits ? Exportez-vous vers les États-Unis ou le Canada ? Transportez-vous des marchandises ? | `produits_livres`, `export_usa_canada`, `transport_marchandises` | oui / non |
| Réalisez-vous des chantiers ? Organisez-vous des événements ? Exploitez-vous des panneaux solaires, éoliennes ou une méthanisation ? | `chantiers`, `evenements`, `installations_energie` | oui / non |
| Recevez-vous du public ? Vendez-vous du conseil ? Vos salariés se déplacent-ils souvent ? Détenez-vous des œuvres d'art ou objets précieux ? | `recoit_public`, `conseil_prestations`, `deplacements_salaries`, `oeuvres_valeurs` | oui / non |

Règles :
- Réponse inconnue ou non donnée : ne pas insister, laisser la valeur par défaut (`false`, ou `1` pour `nb_sites`).
- Ne jamais demander : chiffre d'affaires exact, données de santé, identifiants, coordonnées (sauf mise en relation, voir `orientation-courtier`).

## Étape 2 — Appeler l'outil

Appeler `diagnose_business_risks` **une seule fois**, avec tous les paramètres ci-dessus. Ne pas ajouter de risque absent du résultat.

## Étape 3 — Restituer

Suivre cet ordre :

1. Une phrase d'introduction : « Selon les informations fournies par le plugin Albingia, voici les risques à examiner pour [activité]. »
2. Les expositions de niveau **« élevé »** : pour chacune, le risque et la liste des garanties à examiner.
3. Les expositions **« à examiner »** : une ligne chacune.
4. Les autres sujets à voir avec un courtier (champ `autres_sujets_a_voir_avec_un_courtier`).
5. Les questions à poser au courtier, regroupées et sans doublon.
6. L'avertissement renvoyé par l'outil, en une phrase.

Si vous ajoutez une information qui ne vient pas de l'outil, la présenter à part : « En complément, hors plugin Albingia : … ».

## Étape 4 — Proposer la suite

Proposer en une phrase, sans insister, l'une de ces deux suites :
- préparer une synthèse à remettre au courtier : appeler `build_broker_brief` avec **les mêmes paramètres** qu'à l'étape 2 ;
- être mis en relation avec un courtier : suivre la skill `orientation-courtier`. Ne jamais appeler `request_broker_contact` directement depuis cette skill.

## Ton

Clair, concret, sans jargon non expliqué. Phrases courtes. Pas de superlatifs commerciaux sur Albingia.
