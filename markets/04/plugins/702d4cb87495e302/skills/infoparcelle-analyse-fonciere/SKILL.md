---
name: infoparcelle-analyse-fonciere
description: Parcelle cadastrale, prix de vente réel (DVF), DPE et passoire thermique, zone PLU et constructibilité, permis de construire, copropriété, propriétaire personne morale, entreprises implantées à une adresse : analyse foncière et immobilière à partir des données publiques officielles Infoparcelle. Couvre la France métropolitaine et les 5 DOM (Guadeloupe, Martinique, Guyane, La Réunion, Mayotte). Ne pas utiliser hors de ce périmètre, ni pour des annonces en cours de commercialisation (ces données décrivent l'existant et les ventes conclues, pas le marché affiché).
---

# Analyse foncière avec les données Infoparcelle

Les outils `infoparcelle_*` donnent accès à des données publiques officielles
françaises (DGFiP, Cerema, ADEME, BAN, INSEE, IGN, SDES, BDNB). Ce document explique
comment les enchaîner et comment lire ce qu'ils renvoient.

## Règle générale

Ne jamais répondre de mémoire sur une parcelle, un prix ou un diagnostic : appeler
l'outil et citer la valeur obtenue. Si un outil ne renvoie rien, le dire, plutôt
que de combler par une estimation.

## Enchaînements à suivre

### 🟥 Règle qui prime sur toutes les autres

**`infoparcelle_parcelle_get` est une fiche complète, pas un simple descriptif de terrain.**
Via le paramètre `champs`, il renvoie déjà, pour la parcelle demandée :

`dvfs` (ses transactions) · `dpes` (ses diagnostics) · `zones_plu` (sa zone **et les PDF
officiels du PLU**) · `permis_construire` · `coproprietaires` · `proprietaires` ·
`occupants` (SIRENE) · `risques` · `batiments` · `consommations` · `statistiques` ·
`monuments_historiques` · `detail` · `contour`.

**Ne jamais rappeler `infoparcelle_dvf_search`, `infoparcelle_dpe_search`,
`infoparcelle_plu_search`, `infoparcelle_permis_search`, `infoparcelle_coproprietes_search`
ou `infoparcelle_occupants_search` avec le `cadastre_id` d'une parcelle déjà récupérée** :
la donnée est dans la réponse, et l'appel serait facturé pour rien.

Ces outils servent à interroger **un périmètre plus large** (commune, section, département,
zone), c'est-à-dire à comparer, pas à répéter.

### « Analyse cette adresse » / « Que peux-tu me dire sur ce bien ? »

1. `infoparcelle_geocoder_search` avec l'adresse en texte libre.
   → récupérer le `code` de la parcelle dans `parcelles[]`.
2. `infoparcelle_parcelle_get` avec ce `cadastre_id` et les `champs` utiles.
   → **cela couvre le bien lui-même** : terrain, bâti, DPE, ventes, zone PLU, occupants.
3. Seulement pour **situer le bien dans son marché**, élargir le périmètre :
   - `infoparcelle_dvf_search` avec `code_section` (voisinage immédiat) ou
     `code_municipalite` (commune), jamais avec le `cadastre_id` ;
   - `infoparcelle_dpe_search` de même, pour comparer l'étiquette du bien à celles
     du secteur.

Une adresse peut porter **plusieurs parcelles** : le géocodeur renvoie un tableau.
Les traiter toutes, ou demander laquelle retenir, mais ne pas en choisir une au hasard.

### « Est-ce constructible ? »

1. Résoudre la parcelle, puis `infoparcelle_parcelle_get` avec `champs: ["zones_plu"]`.
   → la zone (`zone`, `type_zone`, `titre`, `description`) **et** `documents.fichiers`,
   la liste des PDF officiels avec leur URL et leur catégorie : règlement, règlement
   graphique, PADD, OAP, prescriptions, servitudes d'utilité publique, PPR.
   **Pour étudier les règles applicables, c'est le document « Documents Règlementaires »
   qu'il faut ouvrir et citer**, pas la seule lettre de zone.
2. `infoparcelle_plu_search` **uniquement** pour élargir : quelles zones existent dans
   la commune (`code_municipalite` + `zone` ou `type_zone`), leurs surfaces, leur
   géométrie (`geometrie: contour`) ou les parcelles qu'elles contiennent.
3. `infoparcelle_permis_search` pour voir ce qui se construit réellement autour :
   `code_section` pour le voisinage immédiat, `code_municipalite` pour la commune,
   avec `etat: 2` (autorisé) et une borne de date.
   ⚠ **Il n'existe pas de filtre par zone PLU** sur cet outil. La section cadastrale est
   le meilleur substitut ; pour vraiment restreindre à une zone, il faut récupérer ses
   parcelles via `infoparcelle_plu_search` (`champs: ["parcelles"]`) et croiser, ce qui
   coûte plusieurs appels : ne le faire que si la question l'exige.

⚠ Une zone d'urbanisme n'est pas une autorisation. Toujours conclure en renvoyant
au règlement de zone et au service urbanisme de la commune.

### « Trouve-moi des biens qui… »

Utiliser `infoparcelle_parcelles_search_advanced` (recherche multicritère) plutôt
que d'enchaîner des recherches unitaires. Croiser ensuite avec `infoparcelle_dpe_search`
ou `infoparcelle_dvf_search` seulement sur les résultats retenus.

### « Montre-moi la parcelle » / plan, croquis, document

`infoparcelle_parcelle_preview` produit une image de la parcelle. Deux familles de thèmes :

- **techniques**, pour un dossier ou une étude : `cadastre_plan`, `plan_millimetre`,
  `architecte_blueprint`, `topographique_contour`, `notarial_officiel` ;
- **réalistes**, pour une présentation client : `realisme_terrain` (défaut),
  `commercial_premium`, et une vingtaine d'autres.

Options utiles, toutes désactivées par défaut : `afficher_surface`, `afficher_mesures`,
`afficher_perimetre`, `afficher_echelle`, `afficher_numero_parcelle`,
`afficher_coordonnees`. Pour un **plan à l'échelle coté**, combiner
`theme: "plan_millimetre"`, `afficher_mesures: true`, `afficher_echelle: true` et une
`echelle` explicite (`"200"`, `"500"`…) plutôt que `auto`.

Plusieurs parcelles se dessinent sur le même plan en séparant les identifiants par des
virgules : c'est la bonne façon de montrer une **unité foncière** ou de comparer des
terrains voisins.

⚠ Ne pas monter `width`/`height`/`dpi` sans raison : une image de présentation se lit
très bien en 800x800, et le maximum (10000 px, 180 DPI) ne sert qu'à l'impression.
⚠ Le rendu est **normalisé en carré** pour préserver l'échelle : demander 900x700
produit une image 900x900. Ne pas promettre un format précis à l'utilisateur.

**L'outil renvoie l'image ET une URL de téléchargement publique**
(`https://mcp.infoparcelle.fr/previews/...`), accessible sans authentification.
C'est cette URL qu'il faut utiliser pour **intégrer le plan dans un document produit**
(fiche, page web, flyer) : `<img src="...">` fonctionne.

🟥 **Cette URL expire au bout de 30 jours.** Quand le plan est inséré dans un livrable
que l'utilisateur va conserver, le lui dire : au-delà, l'image disparaîtra du document.
Pour un usage durable, l'utilisateur doit enregistrer l'image lui-même.

### « Fais-moi une fiche / un dossier / une page de présentation »

C'est l'usage le plus complet, et il se déroule dans cet ordre :

1. `infoparcelle_geocoder_search` pour résoudre l'adresse.
2. **Un seul** `infoparcelle_parcelle_get` avec tous les `champs` nécessaires :
   `detail`, `dpes`, `dvfs`, `zones_plu`, `coproprietaires`, `occupants`, `risques`.
3. `infoparcelle_parcelle_preview` pour le plan, en thème technique si le document est
   professionnel (`cadastre_plan`) ou réaliste s'il est commercial.
4. `infoparcelle_dvf_search` sur la **commune ou la section** pour le contexte de marché.

Soit **quatre appels**, pas davantage. Structurer ensuite le document : identification,
terrain et bâti, énergie, urbanisme, copropriété, marché local, plan.
Signaler ce qui manque plutôt que de laisser une rubrique vide sans explication.

### « Qui est derrière cette adresse ? »

Si la parcelle est déjà identifiée, **tout est dans `infoparcelle_parcelle_get`** :
`champs: ["proprietaires", "occupants", "coproprietaires"]`. Un seul appel.

Les outils dédiés ne servent qu'à chercher **sans partir d'une parcelle** :

- `infoparcelle_proprietaires_search` : retrouver le patrimoine d'une société sur un
  territoire. Propriétaires **personnes morales** uniquement.
- `infoparcelle_occupants_search` : établissements et entreprises implantés (SIRENE),
  à l'échelle d'une commune ou d'un secteur.
- `infoparcelle_coproprietes_search` : registre national des copropriétés d'un territoire.

⚠ Aucun de ces outils ne renvoie de propriétaire particulier. Si la question porte
sur une personne physique, l'indiquer clairement et ne pas contourner.

### Points d'entrée annexes

- `infoparcelle_geocoder_coordinates` : coordonnées GPS → parcelle. C'est le point
  d'entrée quand l'utilisateur fournit une position plutôt qu'une adresse.
- `infoparcelle_geocoder_ban` : récupérer une adresse par son identifiant BAN, quand
  cet identifiant est déjà connu.
- `infoparcelle_municipalites_search` : informations de commune (code INSEE, codes
  postaux). Utile pour convertir un nom de commune en `code_municipalite` avant une
  recherche élargie.

## Formats de sortie et géométries

- **`format`** : `json` (défaut) ou **`geojson`**. Demander `geojson` dès que le résultat
  doit être cartographié ou réutilisé dans un SIG ; rester en `json` sinon, c'est plus
  léger à lire.
- **`geometrie`** (fiche parcelle, zones PLU) : `centre` (défaut, un point),
  `contour` (le polygone complet) ou `bbox` (le rectangle englobant).
  ⚠ `contour` est **beaucoup plus volumineux** : ne le demander que pour tracer la forme
  réelle. Pour situer un bien, `centre` suffit.
- La **pagination** est à curseur : réutiliser `pagination.nextCursor` dans `curseur`.
  `hasMore: false` signifie qu'il n'y a plus rien à demander : ne pas insister.

## Économie des appels

Chaque appel consomme des crédits API de l'utilisateur : de 1 (géocodage, commune)
à 20 (recherche avancée de parcelles), 10 pour une fiche de parcelle, DVF ou DPE.

- **Ne jamais redemander ce que `infoparcelle_parcelle_get` a déjà renvoyé** (voir la
  règle en tête de la section précédente) : c'est de loin le gaspillage le plus fréquent.
- Toujours renseigner `champs` pour ne demander que ce qui sera utilisé. Un
  `parcelle_get` sans `champs` rapatrie l'intégralité de la fiche, y compris des blocs
  volumineux comme les documents du PLU ou la liste des occupants.
- Toujours borner `limite` : 3 à 10 résultats suffisent à répondre, 50 gaspillent.
- Ne pas rappeler un outil déjà appelé dans la conversation ; réutiliser le résultat.
- Ne pas lancer une recherche large « pour voir » avant d'avoir cadré la commune
  ou le département.

## Lire correctement les résultats

**DVF (`infoparcelle_dvf_search`)** : ce sont des ventes **réellement enregistrées**
par l'administration fiscale, pas des prix affichés. C'est leur intérêt principal :
le dire à l'utilisateur.

⚠ `valeur_fonciere` est le montant de **la mutation entière**, qui peut couvrir
plusieurs lots, locaux ou parcelles. Avant de calculer un prix au m², vérifier
`nb_locaux`, `nb_lots`, `nb_parcelles` et les surfaces : une mutation à 52 000 €
pour 110 m² n'est pas un prix de marché, c'est une vente partielle ou atypique.
Écarter les valeurs aberrantes et raisonner sur une médiane, jamais sur un seul point.

**Parcelle (`infoparcelle_parcelle_get`)**

- `superficie` = surface du **terrain**, en m². Ce n'est pas la surface habitable,
  qui se trouve dans `detail.surfaces.habitable`.
- `detail.surfaces.habitable_calculee` à `true` signale une valeur **estimée**,
  pas une donnée déclarée : le préciser si on s'en sert.
- `detail.estimations` est une **estimation**, jamais une transaction. Ne pas la
  présenter comme un prix constaté.

**DPE (`infoparcelle_dpe_search`)** : seuils officiels en kWh/m²/an :
A ≤ 70 · B 71-110 · C 111-180 · D 181-250 · E 251-330 · F 331-420 · G > 420.
Les classes **F et G** sont les passoires thermiques visées par les restrictions
de location. Un bien peut porter plusieurs DPE successifs : retenir le plus récent.

**🟥 Paris, Lyon et Marseille : chercher par ARRONDISSEMENT, jamais par le code ville**

Ces trois communes ont un code global (Paris `75056`, Lyon `69123`, Marseille `13055`)
**et** un code par arrondissement (Paris `75101`-`75120`, Lyon `69381`-`69389`,
Marseille `13201`-`13216`). Les données ne sont pas regroupées :

- Lyon `69123` renvoie **0 résultat**, alors que Lyon 3e (`69383`) en renvoie ;
- Paris `75056` renvoie des données, mais **un jeu distinct** de celui de `75111`
  (Paris 11e) : interroger l'un ne donne jamais le contenu de l'autre.

Donc : passer par `infoparcelle_geocoder_search` (qui renvoie le bon
`municipalite.code`), ou interroger les arrondissements un par un et cumuler.
**Un résultat vide sur ces trois villes ne signifie jamais « rien à signaler ».**
Vérifié le 2026-08-20.

**Référence cadastrale** : 14 caractères, par exemple `66136000AN0417` :
code INSEE de la commune (5) + préfixe (3) + section (2) + numéro (4).
Ne jamais la reconstruire à la main : la prendre telle que l'outil la renvoie.

## Périmètre et limites

- **101 départements** : les 96 de France métropolitaine (Corse comprise, codes `2A`
  et `2B`) et 5 départements d'outre-mer : Guadeloupe (971), Martinique (972),
  Guyane (973), La Réunion (974), Mayotte (976). Hors de ce périmètre, il n'y a
  pas de donnée : le dire plutôt que d'extrapoler.
- Les données décrivent l'existant et le passé (cadastre, ventes conclues,
  diagnostics déposés). Elles ne contiennent **aucune annonce en cours de vente**.
- Les propriétaires particuliers ne sont pas exposés.

### ⚠ Trous de couverture connus, à ne jamais confondre avec une absence de marché

**Les ventes DVF n'existent pas dans 4 départements** : Moselle (57), Bas-Rhin (67),
Haut-Rhin (68) et Mayotte (976). L'Alsace-Moselle relève du **livre foncier**, un
régime distinct du reste de la France, et son registre n'alimente pas le jeu de
données public des valeurs foncières.

Une recherche DVF y renvoie donc un résultat **vide**. Ce vide signifie « données
non publiées pour ce territoire », **jamais** « aucune vente » ni « marché atone ».
L'annoncer explicitement à l'utilisateur et se rabattre sur les autres sources
(cadastre, DPE, permis de construire), qui, elles, couvrent bien ces départements :
la Moselle, le Bas-Rhin et le Haut-Rhin totalisent à eux seuls plus de 4 millions de
parcelles en base.

Vérifié le 2026-08-20 : Strasbourg (67482), Metz (57463) et Mamoudzou (97611)
renvoient 0 mutation, tandis que Guadeloupe, Martinique, Guyane et La Réunion
renvoient des transactions récentes.

## Si un outil renvoie une erreur

- **432** : aucun abonnement actif sur le compte.
- **434** : quota de crédits API épuisé pour la période en cours.
- **435** : fonctionnalité non comprise dans l'offre de l'utilisateur.

Dans ces trois cas, expliquer sobrement la situation et inviter l'utilisateur à
consulter son espace Infoparcelle. Ne pas insister, ne pas proposer de contournement,
et ne pas répondre à la question avec des données inventées.

## Forme de la réponse

- Citer les chiffres obtenus tels quels, avec leur unité.
- Donner la **référence cadastrale** dès qu'une parcelle est identifiée : c'est la
  clé qui permet à l'utilisateur de retrouver le bien.
- Distinguer visiblement ce qui est **mesuré** (superficie, vente enregistrée,
  étiquette DPE) de ce qui est **estimé** (valeur, surface habitable calculée).
- Pour une synthèse, structurer en : identification · terrain et bâti · énergie ·
  urbanisme · marché local.
