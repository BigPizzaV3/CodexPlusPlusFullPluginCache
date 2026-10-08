---
name: prepare-eveos-imports
description: Analyser, transformer, enrichir et valider des fichiers Excel destinés aux imports Eveos, notamment les conférences, intervenants, participants, exposants et taxonomies. Utiliser ce skill lorsqu'il faut adapter des données client hétérogènes au modèle Eveos, préserver des clés existantes, dédupliquer des entités, nettoyer des descriptions, contrôler des références ou préparer une publication après validation humaine.
---

# Préparer les imports Eveos

Produire des fichiers d'import fiables à partir de données client variables. Laisser l'IA comprendre et transformer le contenu ; réserver les scripts aux invariants vérifiables.

## Charger le contexte utile

- Lire [references/eveos-data-model.md](references/eveos-data-model.md) pour les champs, clés, statuts et relations.
- Lire [references/ai-judgment.md](references/ai-judgment.md) lorsqu'il faut déduire une taxonomie, extraire ou enrichir des personnes, nettoyer du contenu ou rapprocher des doublons.
- Lire [references/guided-dialogue.md](references/guided-dialogue.md) avant de demander une décision à l'utilisateur ou de présenter plusieurs anomalies.
- Lire [references/copro-2026-case.md](references/copro-2026-case.md) uniquement pour un traitement Copro ou pour comprendre le cas réel ayant fondé cette méthode.
- Utiliser le skill tableur applicable pour manipuler, recalculer, rendre et vérifier visuellement les classeurs.

## Travailler en mode IA d'abord

Comprendre chaque classeur avant de fixer les correspondances. Ne pas supposer que les noms de feuilles, l'ordre des colonnes ou les libellés seront identiques à un import précédent.

1. Inventorier les feuilles, en-têtes, types de données, formules, clés, valeurs distinctes et relations apparentes.
2. Identifier le modèle cible Eveos et construire une correspondance source-cible avec un niveau de confiance.
3. Résoudre les choix évidents avec les règles métier. Demander une précision seulement lorsqu'une ambiguïté change matériellement le résultat.
4. Appliquer les transformations sémantiques avec l'IA.
5. Contrôler ensuite les invariants de manière déterministe.

## Préserver les données et les identités

- Travailler d'abord sur des fichiers locaux dérivés. Garder les fichiers sources intacts tant que le résultat n'est pas validé.
- Considérer toute clé existante comme immuable. Ne jamais la régénérer, même si le nom, le slug ou la casse semblent perfectibles.
- Ne jamais remplacer une information déjà présente dans une fiche existante par une information recherchée. Compléter uniquement les champs vides lorsque la source est suffisamment fiable.
- Générer les nouvelles clés avec le préfixe de la mission et un slug stable. Résoudre les collisions sans modifier les clés déjà attribuées.
- Rapprocher les personnes sur plusieurs indices : nom normalisé, prénom, société, fonction et contexte. Ne pas fusionner des homonymes sans preuve suffisante.

## Transformer avec discernement

Traiter comme des décisions sémantiques :

- le rapprochement flexible des colonnes ;
- l'extraction des intervenants depuis du texte libre ;
- la distinction entre une personne et une organisation animatrice ;
- la suppression des annonces d'intervenants dans `description clean` ;
- l'affectation d'une taxonomie d'après le titre et la description ;
- l'enrichissement par des sources publiques.

Conserver la description originale. Construire `description clean` uniquement dans sa colonne dédiée. Lorsque des speakers sont référencés, retirer leur bloc d'annonce sans réécrire le contenu éditorial restant.

Qualifier chaque inférence importante :

- **Certaine** : preuve explicite ; appliquer.
- **Probable** : indices concordants ; appliquer et signaler dans le rapport.
- **Ambiguë** : plusieurs interprétations plausibles ; ne pas modifier sans décision humaine.

## Utiliser l'heure locale de l'événement

Considérer par défaut les dates et heures comme des heures locales sur le lieu de l'événement. Une valeur `14:00` signifie 14 h sur place.

- Ne jamais convertir une heure locale vers GMT ou UTC pour l'import Eveos.
- Si une source indique explicitement UTC ou un décalage, convertir vers le fuseau local connu de l'événement avant de produire le fichier.
- Si la source est ambiguë entre heure locale et GMT, choisir l'heure locale de l'événement sans imposer une question technique à l'utilisateur.
- Signaler clairement toute conversion qui change l'heure ou la date civile.

## Guider l'utilisateur

Faire l'analyse technique avant de poser une question. Ne pas demander à l'utilisateur de deviner une colonne, un identifiant, un fuseau ou une stratégie de correction que l'agent peut proposer.

Lorsqu'une décision humaine reste nécessaire :

1. Expliquer le problème en une phrase simple avec son volume et son impact.
2. Présenter deux ou trois options concrètes et mutuellement exclusives.
3. Mettre l'option recommandée en premier et expliquer brièvement son effet.
4. Permettre une réponse courte, idéalement un clic ou un numéro.
5. Grouper les anomalies similaires au lieu de questionner ligne par ligne.

Quand un outil de question interactive est disponible, l'utiliser pour ces arbitrages plutôt qu'une question en texte libre. Préférer une seule question et ne jamais en afficher plus de trois à la fois. Pour chaque question :

- proposer deux ou trois choix mutuellement exclusifs ;
- placer le choix recommandé en premier et suffixer son libellé par `(Recommended)` lorsque l'outil l'exige ;
- résumer l'effet de chaque choix en une phrase courte ;
- utiliser un titre court et un identifiant stable ;
- ne pas ajouter une option `Autre`, car l'interface fournit automatiquement un champ de réponse libre.

Si l'outil interactif n'est pas disponible, présenter les mêmes choix sous forme numérotée et terminer par `Autre réponse : ...`.

Ne pas ouvrir un arbitrage pour une règle déjà tranchée par ce skill, comme la conservation de l'heure locale de l'événement. Appliquer la règle et l'expliquer simplement. Conserver les décisions de l'utilisateur pendant toute la mission et les rappeler dans le bilan lorsqu'elles ont eu un effet matériel.

Ne poser qu'une à trois questions courtes à la fois. Continuer les contrôles non bloqués pendant l'attente. Éviter le jargon technique dans les messages destinés à l'utilisateur ; conserver les détails dans le rapport si nécessaire.

## Valider les invariants

Vérifier au minimum :

- unicité et conservation des clés ;
- valeurs de statut autorisées ;
- types, formats, ordre et plage des dates ;
- appartenance des valeurs aux taxonomies autorisées ;
- existence de chaque clé référencée ;
- séparateur attendu pour les relations multiples ;
- absence de formules en erreur ;
- réouverture correcte des fichiers exportés.

Pour une paire conférences/speakers au format `.xlsx`, générer une configuration adaptée à la mission puis exécuter le validateur en lecture seule :

```bash
python3 scripts/validate_eveos_import.py \
  --conferences /chemin/conferences.xlsx \
  --speakers /chemin/speakers.xlsx \
  --baseline-conferences /chemin/conferences-source.xlsx \
  --baseline-speakers /chemin/speakers-source.xlsx \
  --config /chemin/config.json \
  --report /chemin/validation-report.json
```

Adapter la configuration au fichier réellement observé ; ne pas reprendre aveuglément l'exemple Copro.

## Présenter puis publier

Produire avant toute publication :

- les fichiers locaux proposés ;
- un bilan chiffré ;
- la liste des corrections et ajouts ;
- les éléments ambigus ou laissés vides ;
- la confirmation que les clés existantes sont inchangées ;
- le résultat des contrôles déterministes.

Obtenir une autorisation explicite avant d'écrire sur une source distante ou la production. Juste avant l'écriture, relire les métadonnées ou la version actuelle et réconcilier toute modification concurrente. Mettre à jour l'identifiant exact fourni ; ne jamais sélectionner une cible par son seul titre. Après écriture, vérifier l'identifiant, le nom, le type MIME, la taille et la date de modification.

Ne jamais présenter un fichier comme prêt pour la production tant qu'une erreur bloquante subsiste.
