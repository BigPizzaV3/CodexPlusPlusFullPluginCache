---
name: dpe-travaux
description: >
  Explique les implications réglementaires et financières du DPE (interdictions
  de location, gel des loyers, audit obligatoire, réforme 2026) et les aides à
  la rénovation (MaPrimeRénov', éco-PTZ, CEE). À déclencher dès qu'apparaissent
  les mots DPE, passoire thermique, classe énergie (A à G), rénovation
  énergétique, MaPrimeRénov, isolation, pompe à chaleur, audit énergétique.
version: 1.0
donnees_valides_au: 2026-07
profil_cible: acheteurs, investisseurs, vendeurs
---

# SKILL — DPE et travaux

## Rôle
Tu donnes l'état EXACT de la réglementation DPE et des aides à la rénovation, qui changent souvent et que les modèles de langage restituent mal de mémoire. Tu utilises UNIQUEMENT les dates et montants de ce document.

## Intégration MCP
> Détail des tools : `references/mcp-tools.md`.
- **Classe DPE d'un bien en contexte** (`listing_id`) : la lire via **`get_listing_detail`**, jamais la deviner.
- **Filtrer une recherche par performance énergétique** : argument **`dpe_max`** de `search_properties` (sémantique « au mieux cette classe » : « au moins D » ⇒ `dpe_max: "D"`) — renvoyer à `qualification-besoin` pour lancer/affiner la recherche.
- **Montants d'aides et coûts** : barèmes de ce document uniquement (aucun tool marché exposé) ; chiffrage personnalisé → simulateur / France Rénov' (cf. règles ci-dessous).
- **Handoff** : impact sur la négociation → skill `offre-negociation`.

## Règles absolues
1. Aucune date, aucun seuil, aucun montant hors de ce document. En cas de doute : « ce point évolue, vérifiez sur france-renov.gouv.fr ».
2. Toujours distinguer le point de vue : acheteur (décote/opportunité), bailleur (obligation), occupant (confort/facture).
3. Les montants d'aides sont des plafonds/ordres de grandeur : le montant réel dépend des revenus → renvoyer vers le simulateur Mes Aides Réno ou un conseiller France Rénov' (gratuit).

## Données de référence (juillet 2026)

### Calendrier d'interdiction de location (loi Climat et Résilience) — métropole
| Classe | Interdiction de nouvelle location | Statut |
|---|---|---|
| G | depuis le **1er janvier 2025** | ⛔ en vigueur |
| F | au **1er janvier 2028** | ⏳ dans moins de 2 ans |
| E | au **1er janvier 2034** | ⏳ |

- Porte sur : nouveau bail, renouvellement, reconduction tacite (logement « non décent »). Un bail en cours continue, mais le locataire peut exiger des travaux.
- Outre-mer : G en 2028, F en 2031.
- **Gel des loyers F et G depuis août 2022** : interdiction d'augmenter le loyer (relocation et renouvellement).
- Meublés touristiques : nouveaux meublés limités aux classes A–E depuis novembre 2024.

### Réforme du DPE au 1er janvier 2026 — À VÉRIFIER SYSTÉMATIQUEMENT
- Coefficient de conversion de l'électricité abaissé de 2,3 à **1,9** → **~850 000 logements sortent de F/G sans travaux** (surtout chauffage électrique et petites surfaces).
- Aucun logement ne peut être déclassé par la réforme, seulement amélioré.
- Le recalcul est **gratuit et sans nouveau diagnostic** : service en ligne de l'Observatoire DPE-Audit de l'ADEME avec le numéro ADEME du DPE existant.
- **Réflexe à donner** : tout DPE E/F/G réalisé avant 2026 avec chauffage électrique doit être recalculé AVANT de conclure quoi que ce soit (prix, travaux, interdiction).

### Audit énergétique obligatoire à la VENTE (monopropriétés)
- Classes F et G : depuis avril 2023. Classe E : depuis janvier 2025.
- Coût : ~500–1 000 €, à la charge du vendeur. L'acheteur doit l'exiger : il chiffre les scénarios de travaux.

### Aides à la rénovation (état LF 2026 — guichet rouvert le 23/02/2026)
**MaPrimeRénov' Parcours par geste** (travaux ciblés)
- Logement > 15 ans, résidence principale, artisan **RGE obligatoire**, dossier AVANT travaux.
- Exclus depuis 2026 : isolation des murs (ITI/ITE) et chaudières biomasse → basculés vers le parcours d'ampleur.
- Maisons F/G : encore éligibles au geste jusqu'au **31/12/2026**, obligation de rénovation d'ampleur à partir de 2027.
- Revenus : RFR N-1 ; 4 profils (Bleu/Jaune/Violet/Rose). Profil Rose (aisé) exclu du parcours par geste.

**MaPrimeRénov' Rénovation d'ampleur** (parcours accompagné)
- Logements **E, F ou G**, gain **≥ 2 classes DPE**, ≥ 2 gestes d'isolation, audit avant/après.
- **Mon Accompagnateur Rénov' obligatoire** + depuis 2026 **rendez-vous France Rénov' préalable obligatoire**.
- Plafonds de travaux subventionnables : **30 000 €** (gain 2 classes) / **40 000 €** (3 classes et +) ; taux jusqu'à **80 %** (très modestes), ~10 % (revenus supérieurs).
- ⚠️ À partir du **1er septembre 2026** : pas d'aide d'ampleur (maison individuelle) si un chauffage au gaz est conservé après travaux.
- Interdit de conserver fioul/charbon.

**Compléments cumulables**
- **Éco-PTZ** : jusqu'à **50 000 €** à taux zéro pour le reste à charge.
- **CEE** : cumulables avec le parcours par geste (pas avec l'ampleur), TVA 5,5 %, aides locales.

### Ordres de grandeur coûts travaux (national)
| Poste | Coût indicatif |
|---|---|
| Isolation combles perdus | 25–60 €/m² |
| Isolation murs (ITE) | 150–250 €/m² de façade |
| Fenêtres double vitrage | 400–900 €/fenêtre posée |
| PAC air/eau | 12 000–18 000 € |
| VMC double flux | 4 000–8 000 € |
| Sortie de passoire complète (maison ~100 m²) | 30 000–70 000 € |

## Arbre de réponse
1. Identifier le point de vue (acheteur / bailleur / occupant) et la classe DPE.
2. Si DPE antérieur à 2026 ET chauffage électrique → commencer par le recalcul ADEME gratuit.
3. Donner l'échéance réglementaire qui concerne l'utilisateur.
4. Si travaux nécessaires : parcours d'aide adapté + renvoi conseiller France Rénov' (gratuit).
5. Si achat d'un F/G : rappeler l'audit énergétique obligatoire (l'exiger) et le levier de négociation (voir skill `offre-negociation`).

## Format de sortie
Réponse en prose courte (5–10 phrases max) structurée : ① situation réglementaire exacte avec date, ② action immédiate, ③ aides mobilisables, ④ renvoi France Rénov'/simulateur si chiffrage nécessaire. Pas de tableau sauf si l'utilisateur compare plusieurs classes ou postes de travaux.

## Exemple (few-shot)
**Utilisateur** : « Je veux acheter une maison classée F pour la louer, c'est mort ? »

**Réponse attendue** :
« Pas forcément, mais l'horloge tourne : une maison classée F sera **interdite de mise en location au 1er janvier 2028** (nouveau bail, renouvellement et reconduction), et son loyer est déjà gelé. Premier réflexe : vérifiez la date du DPE — s'il a été fait avant 2026 et que le chauffage est électrique, faites-le recalculer gratuitement via l'Observatoire ADEME (nouvelle méthode 2026) : la maison est peut-être déjà E, ce qui repousse l'échéance à 2034.
Si elle reste F : le vendeur doit vous fournir un **audit énergétique** (obligatoire à la vente) — exigez-le, il chiffre les scénarios de travaux, et c'est votre principal levier de négociation. Côté financement, une rénovation d'ampleur (gain ≥ 2 classes, accompagnateur obligatoire) ouvre droit à MaPrimeRénov' jusqu'à 30 000–40 000 € de travaux subventionnables selon vos revenus, cumulable avec un éco-PTZ jusqu'à 50 000 €. Prenez le rendez-vous France Rénov' (gratuit et désormais obligatoire pour ce parcours) avant de déposer le dossier.
En résumé : faisable, à condition d'intégrer le coût des travaux dans votre offre et de lancer la rénovation dès l'achat — 2028, c'est demain pour un chantier. »

## Hors périmètre → rediriger
- Montant d'aide exact → simulateur Mes Aides Réno / conseiller France Rénov'.
- Contentieux DPE erroné → diagnostiqueur + protection juridique.
- Impact sur la négociation → skill `offre-negociation`.
