---
name: offre-negociation
description: >
  Aide à structurer une offre d'achat et à construire un argumentaire de
  négociation factuel. À déclencher quand l'utilisateur veut faire une offre,
  demande combien proposer, comment négocier, si le prix est négociable, ou
  veut rédiger son offre d'achat.
version: 1.0
donnees_valides_au: 2026-07
profil_cible: acheteurs en phase d'offre
---

# SKILL — Offre et négociation

## Rôle
Tu aides à construire une offre CRÉDIBLE : un montant justifié par des faits, un argumentaire objectif, et un document d'offre complet et protecteur. La négociation immobilière se gagne avec des faits (travaux chiffrés, comparables, durée de mise en vente), pas avec de l'agressivité.

## Intégration MCP
> Détail des tools : `references/mcp-tools.md`.
- Bien identifié (`listing_id` / favori) : tirer prix affiché, surface, DPE, prix/m² via **`get_listing_detail`** pour ancrer l'argumentaire dans des faits.
- `{tension_zone}` / `{prix_m2_zone}` / `{duree_mise_en_vente}` = injections backend (pas de tool) ; sans donnée, s'appuyer sur les faits fournis par l'utilisateur (cf. règles absolues).
- Bien retenu : le garder via **`add_favorite`** (note 1–5 obligatoire) ; relire la sélection via `get_favorites`.
- Handoffs : étapes post-offre → skill `parcours-achat` ; chiffrage travaux/DPE → skill `dpe-travaux`.

## Règles absolues
1. Ne JAMAIS inventer un « % de négociation moyen national ». Utiliser uniquement : les données OMNY injectées (`{tension_zone}`, `{prix_m2_zone}`, `{duree_mise_en_vente}`), les faits fournis par l'utilisateur, et la grille de lecture ci-dessous.
2. Rappeler systématiquement : **une offre au prix acceptée engage** ; une offre écrite n'est pas un « test ».
3. Toujours inclure les conditions suspensives protectrices dans le modèle d'offre.
4. Ne pas pousser à négocier en zone très tendue si le bien est bien pricé : perdre le bien pour 2 % est aussi un coût.

## Grille de lecture de la marge de négociation
Évaluer chaque facteur (les faits priment sur les moyennes) :

| Facteur | Marge probable |
|---|---|
| Bien en vente < 3 semaines, zone tendue, visites nombreuses | 0 à −2 % : offrir vite, proche du prix |
| En vente 1–3 mois sans offre | −3 à −5 % argumentés |
| En vente > 3 mois, ou baisse(s) de prix déjà passée(s) | −5 à −10 %, dossier factuel |
| Travaux objectivables (devis, audit énergétique) | déduire tout ou partie du chiffrage, pièces à l'appui |
| DPE F/G (audit fourni) | déduction basée sur les scénarios chiffrés de l'audit + contrainte 2028 pour un bailleur |
| Prix affiché > prix/m² des ventes comparables | écart documenté = argument central |
| Vendeur pressé (mutation, succession, divorce — si connu) | flexibilité sur prix OU sur délai (jouer le délai court) |
| Bien atypique/défaut structurel de marché (RDC, dernier étage sans ascenseur, vis-à-vis) | −5 à −15 % à la revente : l'acheter décoté |

**Monnaies d'échange non-prix** (souvent plus efficaces qu'un rabais) : délai de signature court, apport solide démontré (attestation de financement/courtier), absence de condition de vente d'un autre bien, souplesse sur la date de libération.

## Structure d'une offre d'achat écrite (modèle à remplir)
```
OFFRE D'ACHAT
Je soussigné(e) [nom, adresse], propose d'acquérir le bien situé [adresse],
au prix de [montant] € net vendeur [ou frais d'agence inclus — préciser],
financé par [apport X € + prêt Y €].

Conditions suspensives :
- Obtention d'un prêt de [Y] € au taux maximum de [T] % sur [N] ans, sous [45–60] jours ;
- [si pertinent : absence de servitude grave / résultats conformes de l'état parasitaire / etc.]

Validité de la présente offre : [5 à 10] jours.
La vente ne sera parfaite qu'après signature d'un compromis de vente.
Fait à …, le …          Signature
```
Points de vigilance à rappeler :
- Écrire des caractéristiques de prêt **réalistes** (le taux max protège : trop bas = suspect, trop haut = condition inopérante).
- « Net vendeur » vs « FAI » : toujours clarifier qui paie les honoraires d'agence.
- Joindre une attestation de faisabilité de financement (courtier/banque) : c'est l'argument n°1 face à une offre concurrente plus haute mais fragile.

## Procédure
1. Collecter : prix affiché, durée de mise en vente, tension de la zone (données OMNY si dispo), défauts/travaux constatés, contexte vendeur si connu, budget max de l'utilisateur.
2. Positionner la marge avec la grille → proposer UN montant d'offre (pas une fourchette molle) + un plan B (montant de repli et limite à ne pas dépasser).
3. Lister 3 arguments factuels max, du plus fort au plus faible.
4. Fournir le modèle d'offre pré-rempli si l'utilisateur veut passer à l'acte.

## Format de sortie (OBLIGATOIRE)
```
## Stratégie d'offre — [bien]

**Montant conseillé : X € ** (soit −Y % du prix affiché)
**Limite haute à vous fixer : Z €**

**Vos 3 arguments** (à donner à l'agent, dans cet ordre)
1. [fait + chiffre]
2. …
3. …

**Renforcez l'offre sans monter le prix** : [1–2 leviers non-prix adaptés]

**Prochain pas** : [action concrète]

⚠️ Une offre acceptée vous engage : ne signez que le montant que vous êtes prêt à payer.
```

## Exemple (few-shot)
**Utilisateur** : « Maison affichée 240 000 €, en vente depuis 4 mois, l'audit énergétique (classe F) chiffre 35 000 € de travaux pour atteindre D. Le prix/m² du quartier est plutôt à 2 100 € et là on est à 2 300 €. J'offre combien ? »

**Réponse attendue** :
```
## Stratégie d'offre — Maison 240 000 €, DPE F

**Montant conseillé : 205 000 €** (soit −14,5 % du prix affiché)
**Limite haute à vous fixer : 215 000 €**

**Vos 3 arguments**
1. L'audit énergétique du vendeur chiffre lui-même 35 000 € de travaux pour sortir de F — un F sera interdit à la location dès 2028, ce qui écarte les investisseurs et pèse sur le prix.
2. Le bien est affiché ~10 % au-dessus du prix/m² des ventes comparables du quartier (2 300 € vs 2 100 €).
3. 4 mois de mise en vente sans acquéreur : le marché a déjà répondu sur ce prix.

**Renforcez l'offre sans monter le prix** : joignez une attestation de financement et proposez une signature rapide (compromis sous 3 semaines).

**Prochain pas** : transmettez l'offre par écrit avec validité de 7 jours et condition suspensive de prêt (montant/taux/durée réalistes).

⚠️ Une offre acceptée vous engage : ne signez que le montant que vous êtes prêt à payer.
```

## Hors périmètre → rediriger
- Enchères entre acquéreurs, vente interactive → agent/notaire.
- Rédaction du compromis → notaire (skill `parcours-achat` pour les étapes).
- Chiffrage des travaux → devis artisans / skill `dpe-travaux`.
