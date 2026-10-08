# Accès public à LUSTAT

## Sources

- Interface : https://lustat.statec.lu/
- Présentation officielle de l’API : https://data.public.lu/fr/datasets/api-de-la-base-de-donnees-lustat/
- Catalogue SDMX : https://lustat.statec.lu/rest/dataflow/LU1/all/all

Les observations doivent venir d’une extraction actuelle et sourcée, ou d’un
fichier fourni par l’utilisateur.

## Dans le navigateur

Rechercher un sujet, ouvrir le tableau, ajuster les filtres puis utiliser les
exports ou « API pour développeur ». Les valeurs affichées peuvent être limitées
aux dernières observations. Relever la fréquence, la période et les dimensions
avant de télécharger. La page interactive nécessite JavaScript ; une lecture
web vide n’implique pas que le tableau est indisponible.

## Avec les outils de code déjà disponibles

Exemple de requête de métadonnées :

```text
https://lustat.statec.lu/rest/dataflow/LU1/DF_D4111/latest?references=all
```

Accepter `application/vnd.sdmx.structure+xml;version=2.1`. Sélectionner le
`Dataflow` exact, suivre `Structure/Ref`, puis la `DimensionList` de la structure
référencée. Pour chaque dimension, résoudre la nomenclature par agence,
identifiant et version. Les contraintes `ContentConstraint` rattachées au tableau
précisent les sélections disponibles. `TIME_PERIOD` se traite par filtres temporels.

Exemple public pour les logements autorisés (à revalider si la structure change) :

```text
https://lustat.statec.lu/rest/data/LU1,DF_D4111,1.0/LU._T._T.A.CPA_F41001_41002.PNUM?startPeriod=2015&endPeriod=2025&dimensionAtObservation=AllDimensions
```

En-tête : `Accept: text/csv`. Les segments de la clé correspondent, dans cet
ordre, à `REF_AREA`, `CANTON`, `REGION`, `FREQ`, `PRODUCT_BCS`, `INDICATOR_BCS`.
Cet exemple ne s’applique pas aux autres tableaux. Construire leurs clés à partir
de leurs propres métadonnées. Préférer un fichier temporaire puis une lecture CSV
à l’affichage de milliers de lignes dans la conversation.

Une requête réseau doit avoir un délai et une taille maximale raisonnables
(par exemple 30 secondes et 16 Mio pour une sélection). Vérifier le code HTTP et
le contenu ; refuser les redirections vers des destinations inattendues et ne
pas désactiver TLS. Les séparateurs et noms de colonnes doivent être lus dans
la réponse, pas supposés. Les valeurs numériques peuvent porter des statuts.

Pour le SDMX XML, désactiver les entités externes et les DTD. Ne jamais exécuter
de code provenant de métadonnées. Réduire les extractions volumineuses par
dimensions et périodes ; une sélection totale du catalogue n’est pas nécessaire
à une analyse ordinaire.
