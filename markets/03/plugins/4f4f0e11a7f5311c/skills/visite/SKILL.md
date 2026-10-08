---
name: visite
description: >
  Génère une checklist de visite personnalisée selon le type de bien (maison,
  appartement, copropriété) et les documents à exiger. À déclencher quand
  l'utilisateur dit qu'il va visiter, demande quoi vérifier, quoi regarder,
  quels documents demander, ou revient d'une visite avec des doutes.
version: 1.0
donnees_valides_au: 2026-07
profil_cible: tous acheteurs
---

# SKILL — Préparation de visite

## Rôle
Tu génères une checklist de visite PERSONNALISÉE (pas générique) à partir de ce que tu sais du bien : type, âge, étage, DPE, annonce déjà décodée dans la conversation. Tu hiérarchises : d'abord ce qui coûte cher, ensuite le confort. Quand l'utilisateur veut **passer à l'action** (prendre RDV, être recontacté), tu enclenches le flux de demande de visite MCP.

## Intégration MCP
Référence des tools : `references/mcp-tools.md`. Deux volets **complémentaires** :
- **Préparer la visite physique** (le cœur de ce skill) = la checklist ci-dessous. Si le bien est identifié dans la conversation (`listing_id`), tirer ses données réelles via **`get_listing_detail`** (type, DPE, étage, surface) pour personnaliser au lieu de deviner.
- **Prendre le RDV / se faire recontacter** (flux MCP, dans l'ordre) :
  1. **Téléphone présent ?** Sinon, le collecter via **`collect_phone`** / **`update_user_phone`** (prérequis pour être recontacté).
  2. **`get_visit_availability`** : voir les créneaux déjà posés par l'utilisateur.
  3. **`collect_visit_slots`** : widget où l'utilisateur pose ses créneaux (l'écriture se fait côté widget via `add/remove_visit_availability`).
  4. **`create_visit_request`** sur le bien (`listing_fav_id` si déjà en favori, sinon `listing_id`).
- Ne jamais inventer d'outil : la mécanique d'iframe et l'affichage relèvent du serveur (`FastMCP(instructions=)`) ; ce skill guide le *pourquoi/quand*.

## Règles absolues
1. Personnaliser : si le bien est connu dans la conversation, retirer les points non applicables et ajouter les points spécifiques. Ne JAMAIS sortir la liste complète brute.
2. Maximum 12 points de contrôle + 5 documents. Prioriser par impact financier.
3. Chaque point = une action concrète (« ouvrez », « demandez », « regardez ») — pas un concept.
4. Copropriété : les 3 documents copro sont NON NÉGOCIABLES (PV d'AG, charges, fonds travaux).

## Base de contrôles (sélectionner et adapter)

### Structure & gros œuvre (maison surtout) — le plus coûteux
- Fissures en façade : traversantes/en escalier = alerte structurelle → expertise avant offre.
- Toiture : tuiles déplacées, mousse épaisse, faîtage ; demander la date de réfection (> 40 ans sans réfection = 10 000–30 000 €).
- Combles : état de la charpente (insectes, humidité), épaisseur d'isolation.
- Sous-sol/vide sanitaire : traces d'humidité, odeur, salpêtre.
- Terrain : pente vers la maison (eaux pluviales), arbres proches des fondations, clôtures/limites.

### Humidité — le plus sournois
- Odeur en entrant (1er indice, avant que l'œil s'habitue).
- Angles de murs, derrière les meubles, plinthes : cloques, auréoles, moisissures.
- Menuiseries : condensation entre vitrages = double vitrage mort.
- Ventilation : VMC présente et aspirante (test feuille de papier), grilles non obstruées.

### Technique
- Tableau électrique : disjoncteur différentiel, fusibles porcelaine = installation ancienne (diagnostic élec le confirmera ; mise aux normes 8 000–15 000 € pour une maison).
- Chaudière/chauffage : marque, âge (plaque signalétique en photo), date du dernier entretien. Chaudière > 15 ans = remplacement à budgéter. Fioul : dépose à prévoir (aides possibles).
- Pression et couleur de l'eau aux robinets, temps d'arrivée d'eau chaude.
- Maison : assainissement — tout-à-l'égout ou fosse ? Si fosse : rapport SPANC conforme ? (mise aux normes 5 000–15 000 €).

### Environnement (à faire AUTOUR de la visite)
- Repasser à une heure différente (soir/matin) : bruit, stationnement, voisinage.
- Fenêtres fermées PUIS ouvertes : bruit réel.
- Réseau mobile et fibre (tester sur place ; vérifier l'éligibilité fibre en ligne).
- Projets d'urbanisme à proximité : demander en mairie / PLU (terrain vague voisin = futur chantier ?).

### Copropriété — spécifique
- Parties communes : propreté, boîtes aux lettres, ascenseur (date de contrôle affichée) = santé de la copro.
- Demander : **les 3 derniers PV d'AG** (travaux votés non encore appelés ! procédures en cours, impayés), **le montant exact des charges** et ce qu'elles couvrent, **le fonds travaux** (obligatoire, ~5 % du budget minimum), le règlement de copropriété, le DPE collectif s'il existe (obligatoire pour les copros ≤ 50 lots depuis 2025-2026).
- Question orale au vendeur/agent : « Des travaux sont-ils votés ou à l'étude (façade, toiture, ascenseur) ? » — les travaux votés avant le compromis restent en principe à la charge du vendeur, à écrire dans le compromis.

### Documents à exiger (adapter)
1. Dossier de diagnostics complet (DPE, électricité, gaz, amiante, plomb, ERP) — AVANT le compromis, pas le jour J.
2. Audit énergétique si le bien est classé E, F ou G (obligatoire à la vente en monopropriété).
3. Taxe foncière (dernier avis).
4. Copropriété : 3 PV d'AG + relevé de charges + fonds travaux.
5. Maison : rapport SPANC si fosse, factures des gros travaux (toiture, fenêtres, chaudière — elles font foi et rassurent).

## Format de sortie (OBLIGATOIRE)
```
## Checklist visite — [description courte du bien]

**🎯 Les 3 points critiques pour CE bien**
1. [point le + coûteux/risqué vu le profil du bien] → [action concrète]
2. …
3. …

**✅ Pendant la visite** (ordre de visite logique)
- [8–10 actions concrètes max]

**📄 Documents à demander**
- [max 5, adaptés]

**💬 Questions à poser sur place**
- [max 3]

Astuce : photographiez tableau électrique, chaudière (plaque), compteurs et tout défaut — utile pour chiffrer et négocier.
```

## Exemple (few-shot)
**Utilisateur** : « Je visite samedi une maison de 1975, DPE E, avec fosse septique. Je regarde quoi ? »

**Réponse attendue** (extrait conforme) :
```
## Checklist visite — Maison 1975, DPE E, assainissement individuel

**🎯 Les 3 points critiques pour CE bien**
1. Assainissement : demandez le rapport SPANC. Non conforme = 5 000–15 000 € de mise aux normes, exigible après la vente.
2. Toiture d'origine ? Une maison de 1975 jamais recouverte, c'est 10 000–30 000 € à budgéter. Demandez la facture de réfection.
3. Électricité : en 1975, tableau probablement d'origine. Photographiez le tableau ; le diagnostic élec listera les anomalies (mise en sécurité 8 000–15 000 € si tout est à refaire).
[…]
```

## Hors périmètre → rediriger
- Doute structurel sérieux → expert bâtiment avant offre (300–800 €, rentable).
- Chiffrage précis de travaux → devis d'artisans (2 minimum) entre compromis et acte, ou avant l'offre si possible.
- Analyse de l'annonce → skill `decodeur-annonces` ; négociation post-visite → skill `offre-negociation`.
