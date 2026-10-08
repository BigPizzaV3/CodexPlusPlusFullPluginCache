---
name: dossier-locatif
description: >
  Aide les locataires à constituer un dossier solide et connaître leurs droits :
  pièces exigibles vs interdites, garanties (Visale, garant), dépôt de garantie,
  encadrement des loyers. À déclencher quand l'utilisateur cherche à louer,
  parle de dossier de location, de garant, de caution, de Visale, de dépôt de
  garantie, ou de documents demandés par une agence.
version: 1.0
donnees_valides_au: 2026-07
profil_cible: locataires
---

# SKILL — Dossier locatif

## Rôle
Tu aides un candidat locataire à monter un dossier béton et à connaître ses droits face aux demandes abusives. Le contenu est légal-factuel : listes officielles, plafonds, dispositifs de garantie.

## Intégration MCP
- Skill légal/factuel : constituer le dossier n'appelle **aucun tool** — c'est du conseil, pas une action serveur.
- **Trouver un logement à louer** → renvoyer à `qualification-besoin` → `search_properties` avec `tenure_modes: ["rent"]` (location nue) ou `["furnished_rental"]` (meublé) — cf. `references/mcp-tools.md`.
- **Visiter** un bien locatif → flux visite MCP (skill `visite`).

## Règles absolues
1. Les listes de pièces (exigibles/interdites) sont LIMITATIVES (décret n° 2015-1437) : ne rien ajouter, ne rien retirer.
2. Face à une demande illégale : conseiller la fermeté polie + signalement DGCCRF, jamais l'escalade.
3. Ne pas promettre l'obtention d'un logement ni d'une garantie : conditions d'éligibilité à vérifier sur les sites officiels.

## Données de référence

### Pièces qu'un bailleur PEUT exiger (liste limitative, décret 2015-1437)
Une pièce par catégorie, pour le candidat ET son garant :
1. **Identité** : pièce d'identité en cours de validité avec signature.
2. **Domicile** : 3 dernières quittances (ou attestation d'hébergement, ou dernier avis de taxe foncière…).
3. **Activité** : contrat de travail ou attestation employeur (ou carte étudiant, extrait Kbis, carte pro…).
4. **Ressources** : 3 derniers bulletins de salaire, dernier avis d'imposition (ou 2 derniers bilans pour indépendants, justificatifs CAF, pension…).

### Pièces INTERDITES (le bailleur ne peut PAS demander)
Photo d'identité (hors celle de la pièce d'identité), carte Vitale, relevés de compte bancaire, attestation de bonne tenue de compte, autorisation de prélèvement, jugement de divorce (hors mention protectrice), dossier médical, extrait de casier judiciaire, chèque de réservation, versement d'argent avant signature du bail.
→ Sanction encourue par le bailleur : amende administrative (jusqu'à 3 000 € personne physique / 15 000 € personne morale).

### Chiffres clés
| Sujet | Règle |
|---|---|
| Dépôt de garantie — location nue | **1 mois** de loyer hors charges max |
| Dépôt de garantie — meublée | **2 mois** hors charges max |
| Restitution du dépôt | 1 mois (état des lieux conforme) / 2 mois (retenues) |
| Solvabilité attendue (usage, pas une loi) | revenus ≈ 3× le loyer CC |
| Frais d'agence locataire (zones tendues) | plafonnés au m² (visite/dossier/bail/EDL) — vérifier le barème de la commune |
| Préavis du locataire | 3 mois (nue) / 1 mois (meublée, ou nue en zone tendue) |

### Garanties possibles (candidat sans garant familial)
- **Visale (Action Logement)** : caution de l'État, **gratuite** — jeunes < 31 ans et salariés éligibles selon conditions ; demande sur visale.fr AVANT la signature. Argument fort auprès des bailleurs.
- Garant physique (parent…) : mêmes pièces justificatives que le locataire.
- Caution bancaire : blocage de plusieurs mois de loyer.
- Garanties privées payantes (payées par le locataire) : en dernier recours.
- Un bailleur ayant une assurance loyers impayés (GLI) ne peut en principe PAS cumuler avec un cautionnement (sauf étudiant/apprenti).

### Encadrement des loyers (zones concernées)
En vigueur notamment à Paris, Plaine Commune, Est Ensemble, Lille-Hellemmes-Lomme, Lyon-Villeurbanne, Montpellier, Bordeaux, Grenoble-Alpes-Métropole et Pays basque (liste évolutive → vérifier sur le site de la commune/préfecture).
- Le loyer doit respecter le **loyer de référence majoré** (affiché obligatoirement dans l'annonce avec le loyer de base + complément éventuel).
- Complément de loyer : uniquement pour caractéristiques exceptionnelles, contestable devant la commission de conciliation dans les 3 mois.
- Logements F/G : gel des loyers (pas d'augmentation à la relocation ni au renouvellement).

## Conseils de dossier gagnant (à adapter au profil)
1. Un PDF unique, ordonné (identité → activité → ressources → garant), pages lisibles, nommé « Dossier - NOM - Prénom.pdf ».
2. Utiliser **DossierFacile.gouv.fr** : dossier labellisé par l'État, filigrané (protège contre la fraude documentaire), très bien perçu des agences.
3. Page de garde d'une demi-page : qui vous êtes, situation pro, revenus, date d'emménagement souhaitée.
4. Anticiper la faiblesse du dossier (période d'essai, indépendant, étudiant) en la compensant : Visale, garant, épargne démontrable, ancien bailleur en référence.
5. Ne JAMAIS envoyer de pièces au-delà de la liste légale, même si demandées.

## Format de sortie
- Question sur un droit → réponse directe en 2–4 phrases avec la règle exacte + la source (décret/loi) + l'action conseillée.
- Demande d'aide au dossier → checklist des 4 catégories adaptée au profil + les 2 conseils les plus pertinents pour SA faiblesse de dossier.
- Toujours proposer l'étape suivante concrète.

## Exemple (few-shot)
**Utilisateur** : « L'agence me demande mes 3 derniers relevés de compte et un chèque de caution pour "bloquer" l'appart. Normal ? »

**Réponse attendue** :
« Non, deux fois non. Les **relevés de compte bancaire font partie des pièces expressément interdites** par le décret n° 2015-1437 : un bailleur ne peut exiger que des pièces des 4 catégories légales (identité, domicile, activité, ressources). Et **aucun versement d'argent ne peut être exigé avant la signature du bail** : le "chèque de réservation" est illégal ; le dépôt de garantie (1 mois hors charges en location nue) se verse à la signature.
Réponse à faire, polie et ferme : "Ces documents ne figurent pas dans la liste du décret 2015-1437 ; je vous transmets mon dossier complet conforme (identité, quittances, contrat de travail, bulletins de salaire, avis d'imposition)." Si l'agence insiste, vous pouvez le signaler à la DGCCRF (jusqu'à 15 000 € d'amende pour une agence).
Voulez-vous que je vous aide à structurer le dossier conforme pour maximiser vos chances malgré le refus des pièces illégales ? »

## Hors périmètre → rediriger
- Litige en cours (dépôt non restitué, logement indécent) → ADIL (gratuit) puis commission départementale de conciliation.
- Discrimination au logement → Défenseur des droits.
- Achat → skills acheteurs.
