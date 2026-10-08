# Référence partagée — Tools & comportements du MCP Omny

> **Rôle de ce fichier.** Source de vérité **unique** (DRY) des outils exposés par
> le serveur MCP Omny (`mcp.omny.fr`) et de leurs comportements. Les `SKILL.md`
> renvoient ici plutôt que de dupliquer ces détails. **Ce n'est pas un skill**
> (pas de `SKILL.md`, dossier `_`-préfixé, ignoré par la validation).
>
> **Autorité.** Les règles conversationnelles de bas niveau (affichage widget,
> quand afficher, séquencement) sont posées côté serveur dans
> `FastMCP(instructions=)` (`server/main.py`) et font foi au runtime. Les skills
> **ne les redéfinissent pas** : ils orchestrent le *quand* métier (quel tool
> pour quel besoin) sans contredire le serveur.
>
> **Packaging.** À la soumission d'un plugin OpenAI, un skill s'uploade en bundle
> **autonome** : un renvoi `_shared/mcp-tools.md` ne se résout pas hors du repo.
> Ce fichier est donc canonique **dans le repo** ; le packaging plugin
> (`just mcp-skills-package` → `scripts/package_skills.py`) l'inline dans
> `references/mcp-tools.md` de chaque skill et réécrit les renvois (artefact
> `skills-dist/omny-plugin.zip`). Ne pas s'appuyer sur sa présence côté ChatGPT au
> runtime — les skills restent lisibles sans lui.

---

## 1. Ce que le MCP N'EXPOSE PAS (la cage — critique)

Le serveur **n'a aucun tool de données marché** (`get_market_context` et
`proximity_search` sont volontairement omis — cf. `mcp-chatgpt-app/CLAUDE.md`
§ WEA-889). Les placeholders suivants restent des **injections backend** ou des
**questions à l'utilisateur** — **jamais** des appels d'outil :

| Placeholder | Nature | Sans la donnée |
|---|---|---|
| `{taux_actuels}` | taux de crédit moyens (backend) | demander le taux banque, sinon hypothèse signalée |
| `{{TABLE_PLAFONDS_PTZ}}` | table plafonds PTZ (base Omny) | pas de montant PTZ → simulateur ANIL |
| `{prix_m2_zone}` | prix/m² comparables (backend) | demander à l'utilisateur, marquer « hypothèse » |
| `{loyer_marche_zone}` | loyer de marché (backend) | idem |
| `{tension_zone}` | tension du marché local (backend) | idem |
| `{duree_mise_en_vente}` | ancienneté de l'annonce (backend) | fait fourni par l'utilisateur |

**Règle de la cage (inchangée) : sans donnée injectée, le modèle ne chiffre pas**
— il demande, ou renvoie vers la source officielle. Ne jamais présenter ces
placeholders comme des outils MCP, ne jamais inventer `get_market_context`.

---

## 2. Catalogue des tools (tous protégés OAuth Supabase)

### Recherche & affichage

| Tool | Entrée clé | Comportement à connaître |
|---|---|---|
| `search_properties` | critères (cf. §3) | **Localisation obligatoire**, résolue en interne (texte → IRIS). Pré-check : **> 50 biens ⇒ `too_many_results`** (aucun détail renvoyé, il faut affiner). **Max 15 biens** rendus. Rend son widget. |
| `show_search_results` | liste d'`id` | Ré-affiche/rafraîchit une sélection déjà trouvée (re-fetch par IDs, galerie photos). |
| `get_listing_detail` | `listing_id` (string) | Détail d'UN bien via RPC `get_public_listing` + photos S3. **GPS obfusquées (~200 m)**, jamais l'adresse exacte. `listing_id` = celui renvoyé par `search_properties`. |

### Favoris (la « sélection » de l'utilisateur)

| Tool | Entrée clé | Comportement |
|---|---|---|
| `add_favorite` | `listing_id`, `rating` (**int 1–5 obligatoire**), `personal_note` | Enregistre/actualise un favori. **Si l'utilisateur n'a pas donné de note, la demander avant d'écrire.** Ré-enregistrer un bien = mise à jour (pas de doublon). |
| `reject_favorite` | `listing_id` | Écarte un bien non pertinent. |
| `get_favorites` | — | Liste la sélection courante. |
| `get_favorite` | `listing_id`/`fav_id` | Détail d'un favori. |

Un favori est le **prérequis** naturel d'une demande de visite (`create_visit_request` accepte un `listing_fav_id`).

### Flux visite & contact

| Tool | Entrée clé | Rôle dans le flux |
|---|---|---|
| `update_user_phone` | `phone` (E.164) | **Écriture.** Enregistre le téléphone (prérequis pour être recontacté). |
| `collect_phone` | — | Widget de saisie du téléphone (rendu). |
| `get_visit_availability` | — | Liste les créneaux déjà posés par l'utilisateur. |
| `add_visit_availability` | `slot_date`, `slot_start`, `slot_end`, `acknowledge_far_date` | Ajoute un créneau de disponibilité (1 h). Au-delà de la fenêtre `VISIT_MAX_MONTHS_AHEAD` (3 mois), renvoie `needs_confirmation` sauf `acknowledge_far_date=true`. |
| `remove_visit_availability` | `slot_id` | Retire un créneau. |
| `collect_visit_slots` | — | **Widget picker** de créneaux (scène `visit_slots`). Rendu pur ; le widget écrit via les 3 tools availability. |
| `create_visit_request` | `listing_id` **OU** `listing_fav_id` | Crée la demande de visite finale (un des deux, l'autre `null`). |
| `get_visit_requests` | — | Liste les demandes de visite existantes. |

**Flux visite recommandé** : (1) téléphone présent ? sinon `collect_phone` /
`update_user_phone` → (2) `get_visit_availability` → (3) `collect_visit_slots`
(l'utilisateur pose ses créneaux) → (4) `create_visit_request` sur le bien
(favori de préférence). Le picker et l'écriture sont côté widget ; le skill
guide le *pourquoi/quand*, pas la mécanique d'iframe.

---

## 3. `search_properties` — mapping critères métier → arguments

Le skill `qualification-besoin` (et tout skill qui lance une recherche) doit
émettre des arguments **conformes à l'inputSchema réel** (`SEARCH_TOOL_SCHEMA`,
`server/main.py`). Vocabulaire métier → argument :

| Besoin exprimé | Argument `search_properties` | Notes |
|---|---|---|
| Budget max | `price_max` (int, EUR) | + `price_min` si plancher |
| Type de bien (maison/appart…) | `property_types` (array **enum**) | voir enum ci-dessous |
| Vente / location / viager… | `tenure_modes` (array **enum**) | défaut usuel : `["sale"]` |
| Chambres minimum | `bedrooms_min` (int) | ⚠️ pas `rooms_min` (= pièces) |
| Pièces minimum | `rooms_min` (int) | distinct des chambres |
| Surface | `surface_min` / `surface_max` (m²) | |
| Extérieur (jardin, balcon…) | `exteriors` (array **enum**) | |
| Étage | `floor_min` / `floor_max` | |
| Parking / places | `parking_min` (int) | |
| DPE « au moins D » | `dpe_max` (**string A–G**) | ⚠️ **sémantique** : « ≥ D » ⇒ `dpe_max="D"` (on borne la mauvaise classe) |
| Orientation | `orientations` (array **enum**) | |
| Zone : ville | `city_name` (string) | résolu en interne |
| Zone : quartier | `neighborhood_name` (string) | |
| Zone : code postal | `postal_code` (`^[0-9]{5}$`) | |
| Zone : code commune INSEE | `commune_code` (string) | |
| Zone : point + rayon | `latitude` + `longitude` + `radius_km` | trio GPS |
| Codes IRIS directs | `iris_codes` (array) | usage avancé |
| Tri | `sort_by` | selon enum serveur |

**Enums (valeurs EXACTES à émettre)** :

- `property_types` : `apartment`, `house`, `loft`, `parking`, `land`, `building`,
  `office`, `shop`, `castle`, `property`, `business`.
- `tenure_modes` : `sale`, `rent`, `viager`, `bare_ownership`, `furnished_rental`,
  `leasehold_transfer`, `business_goodwill`.
- `exteriors` : `balcony`, `garden`, `terrace`, `parking_outdoor`, `cellar`,
  `pool`, `loggia`, `veranda`, `courtyard`, `attic`, `garage`.
- `orientations` : `north`, `north_east`, `east`, `south_east`, `south`,
  `south_west`, `west`, `north_west`.
- `dpe_max` : `A` `B` `C` `D` `E` `F` `G`.

**Comportements à encoder dans le skill** :

1. **Localisation obligatoire** : sans zone exploitable, ne pas appeler
   `search_properties` — la demander d'abord.
2. **`too_many_results` (> 50)** : la recherche renvoie vide + ce signal ⇒
   proposer 1–2 affinages concrets (resserrer la zone, baisser `price_max`,
   ajouter un critère strict) puis relancer. Ne pas prétendre « aucun bien ».
3. **Max 15 rendus** : ne jamais promettre une liste exhaustive ; présenter la
   sélection comme les meilleurs résultats.
4. **Critère absent = `null`/omis**, jamais une valeur inventée.

---

## 4. Convention de handoff entre skills

Les renvois « → skill `x` » sont des **instructions d'orchestration** : le skill
actif signale le besoin, l'orchestrateur re-route (un seul skill actif à la fois,
cf. `README.md`). Côté tools, un handoff se traduit par l'appel du tool adéquat :
« je lance la recherche » = `search_properties` ; « je prépare la visite » = flux
visite ; « je garde ce bien » = `add_favorite`.
