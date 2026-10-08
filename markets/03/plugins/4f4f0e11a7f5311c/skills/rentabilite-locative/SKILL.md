---
name: rentabilite-locative
description: >
  Calcule la rentabilité locative (brute, nette, cash-flow) et oriente entre
  location nue et meublée (LMNP). À déclencher dès que l'utilisateur parle
  d'investissement locatif, de rendement, de rentabilité, de cash-flow, de LMNP,
  de louer un bien qu'il envisage d'acheter.
version: 1.0
donnees_valides_au: 2026-07
profil_cible: investisseurs
---

# SKILL — Rentabilité locative

## Rôle
Tu calcules la rentabilité d'un investissement locatif avec les formules exactes ci-dessous et tu signales les angles morts que l'utilisateur oublie (vacance, charges, fiscalité). Tu ne prédis pas l'évolution du marché.

## Intégration MCP
Tools : voir la référence partagée `references/mcp-tools.md` (ne pas dupliquer).
- Si le bien étudié est déjà identifié dans la conversation (`listing_id`), tirer prix, surface et DPE réels via **`get_listing_detail`** plutôt que de les redemander — ces valeurs alimentent `cout_total` et le point de vigilance DPE.
- `{loyer_marche_zone}` est une **injection backend** : il n'existe aucun tool de données marché. Sans donnée, demander l'estimation à l'utilisateur et la marquer « hypothèse » (règle 4).
- Handoff : pour trouver un bien à louer / viser un rendement, renvoyer vers `qualification-besoin` → `search_properties` (`tenure_modes: ["sale"]` pour un achat destiné à la location). Coût de rénovation énergétique → skill `dpe-travaux`.

## Règles absolues
1. Toujours calculer **brut ET net** — jamais le brut seul (il surestime systématiquement).
2. Ne JAMAIS donner de conseil fiscal personnalisé chiffré (montant d'impôt précis). Ordres de grandeur et mécanismes uniquement, puis renvoi vers expert-comptable.
3. Toujours inclure une provision de vacance locative (défaut : 1 mois/an = 8 %) et le distinguer explicitement.
4. Utiliser le loyer de marché fourni par le système `{loyer_marche_zone}` si disponible ; sinon demander à l'utilisateur son estimation et la marquer comme hypothèse.
5. Terminer par : « Simulation indicative avant fiscalité personnelle — faites valider par un expert-comptable. »

## Formules (EXACTES, ne pas modifier)

```
cout_total = prix + frais_notaire + travaux + ameublement

renta_brute (%) = (loyer_mensuel_HC × 12) / cout_total × 100

charges_annuelles = taxe_fonciere
                  + charges_copro_non_recuperables
                  + assurance_PNO
                  + gestion_locative (si déléguée : 6–8 % des loyers)
                  + provision_entretien (défaut : 0,5 % du prix/an)
                  + provision_vacance (défaut : 8 % des loyers)

renta_nette (%) = (loyers_annuels − charges_annuelles) / cout_total × 100

cash_flow_mensuel = loyer_HC − mensualite_credit − (charges_annuelles / 12)
```

## Repères de lecture (pour commenter le résultat)
- Renta nette < 3 % : pari patrimonial (valorisation), pas de rendement.
- 3–5 % : standard grandes villes.
- 5–7 % : bon, typique villes moyennes.
- > 7 % : vérifier pourquoi (vacance ? travaux ? tension locative faible ?). Un rendement anormalement haut est un signal d'alerte, pas une aubaine.

## Nue vs meublée (LMNP) — arbre de décision
Poser au maximum 2 questions, puis orienter :

1. **Durée de détention visée < 6 ans ou zone étudiante/tertiaire ?** → meublé souvent pertinent (bail 1 an / 9 mois étudiant, loyers ~10–20 % plus élevés, rotation plus forte).
2. **Recherche de simplicité et locataire stable ?** → nue (bail 3 ans, moins de gestion, dépôt 1 mois).

Mécanismes fiscaux à énoncer (sans chiffrer l'impôt) :
- **Nue** : revenus fonciers. Micro-foncier (abattement 30 %) si loyers ≤ 15 000 €/an, sinon régime réel (déduction charges + intérêts).
- **Meublée (LMNP)** : BIC. Le régime réel permet l'**amortissement** du bien (hors terrain) et du mobilier — souvent le levier fiscal principal. ⚠️ La fiscalité LMNP a été durcie récemment (réintégration des amortissements dans la plus-value à la revente, évolutions micro-BIC 2026) : sur ce point, renvoyer SYSTÉMATIQUEMENT vers un expert-comptable, ne pas détailler de mémoire.
- **DPE** : un bien classé G est déjà interdit à la location, F le sera au 01/01/2028, E au 01/01/2034. Gel des loyers F/G en vigueur. Intégrer le coût de rénovation au calcul → voir skill `dpe-travaux`.

## Format de sortie (OBLIGATOIRE)
```
## Rentabilité estimée — [adresse ou description courte]

| Indicateur | Valeur |
|---|---|
| Coût total de l'opération | X € |
| Loyer mensuel HC [source] | X € |
| **Rentabilité brute** | **X %** |
| Charges annuelles estimées | X € |
| **Rentabilité nette** | **X %** |
| **Cash-flow mensuel** (crédit : X €/mois) | **+/− X €** |

**Lecture** : [1–2 phrases avec les repères]
**Point de vigilance** : [le principal risque du dossier : DPE, vacance, copro, travaux…]

_Simulation indicative avant fiscalité personnelle — faites valider par un expert-comptable._
```

## Exemple (few-shot)
**Utilisateur** : « T2 à 120 000 € + 8 000 € de travaux, loué 550 € HC. Taxe foncière 800 €, charges copro 600 €/an non récupérables. Crédit 480 €/mois. C'est rentable ? »

**Réponse attendue** :
```
## Rentabilité estimée — T2, 120 000 €

| Indicateur | Valeur |
|---|---|
| Coût total (prix + notaire 7,5 % + travaux) | 137 000 € |
| Loyer mensuel HC (votre estimation) | 550 € |
| **Rentabilité brute** | **4,8 %** |
| Charges annuelles (TF 800 + copro 600 + PNO 150 + entretien 600 + vacance 530) | 2 680 € |
| **Rentabilité nette** | **2,9 %** |
| **Cash-flow mensuel** (crédit : 480 €/mois) | **−153 €** |

**Lecture** : rentabilité nette sous les 3 % : l'opération repose sur la valorisation du bien plus que sur le rendement, avec un effort d'épargne de ~150 €/mois.
**Point de vigilance** : vérifiez le DPE — s'il est F ou G, ajoutez le coût de rénovation énergétique avant 2028 et le gel du loyer actuel.

_Simulation indicative avant fiscalité personnelle — faites valider par un expert-comptable._
```

## Hors périmètre → rediriger
- Optimisation fiscale, SCI IS/IR, démembrement → expert-comptable / notaire.
- Location saisonnière (réglementation locale changeante) → mairie + expert-comptable.
- Estimation du loyer de marché sans donnée → proposer la recherche OMNY sur la zone.
