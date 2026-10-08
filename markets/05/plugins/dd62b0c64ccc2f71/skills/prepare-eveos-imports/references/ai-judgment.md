# Décisions confiées à l'IA

## Extraction des speakers

Chercher les formulations telles que `Animé par`, `Intervenants`, `Avec`, `Modération`, `Table ronde` ou leurs variantes. Utiliser aussi la ponctuation et les retours à la ligne pour distinguer :

- prénom et nom ;
- fonction ;
- entreprise ou organisation ;
- plusieurs personnes dans un même bloc.

Créer une personne uniquement lorsque le texte identifie une personne physique. Une mention comme `Animé par FONCIA` ou `Présenté par l'ANAH` décrit une organisation et ne suffit pas à créer un speaker.

Avant de créer une fiche, comparer avec les speakers existants. Normaliser les accents, la casse, les tirets et espaces seulement pour la comparaison ; ne pas réécrire les valeurs existantes.

## Nettoyage des descriptions

Toujours conserver `description` à l'identique.

Dans `description clean` :

1. Partir du contenu original.
2. Retirer uniquement le ou les blocs qui annoncent les personnes effectivement référencées dans `speakers`.
3. Conserver les paragraphes éditoriaux, listes, ponctuation et informations métier.
4. Ne pas supprimer une mention d'organisation lorsqu'aucune personne n'a été créée, sauf instruction explicite.
5. Si la description ne contient que l'annonce d'un speaker, laisser `description clean` vide.

## Affectation des taxonomies

Utiliser uniquement les valeurs techniques autorisées fournies pour la mission. Se baser sur le titre, la description, le format et le contexte de l'événement.

- Affecter automatiquement lorsque le thème est explicite.
- Signaler une affectation probable lorsque plusieurs thèmes se chevauchent.
- Laisser vide et demander une décision lorsqu'aucune valeur n'est suffisamment défendable.
- Ne jamais inventer un nouveau terme technique pour contourner une taxonomie incomplète.

## Enrichissement public

Chercher d'abord les sources officielles : site de l'organisation, biographie institutionnelle, page d'équipe, programme officiel, profil professionnel public attribué sans ambiguïté. Utiliser ensuite des sources secondaires fiables pour corroborer.

Respecter ces règles :

- ne jamais modifier un champ déjà renseigné ;
- compléter seulement les champs vides ;
- séparer les faits vérifiés des formulations de synthèse ;
- conserver les URL sources dans un onglet ou rapport dédié ;
- ne pas prendre l'image d'un résultat de moteur de recherche comme URL de photo ;
- ne pas renseigner LinkedIn si le profil exact n'est pas publiquement et durablement identifiable ;
- ne pas renseigner une photo incertaine, même si le nom correspond ;
- ne pas inventer d'adresse électronique, de téléphone ou de titre professionnel.

## Niveaux de confiance

Documenter les décisions non triviales dans le rapport :

| Niveau | Critère | Action |
|---|---|---|
| Certaine | Mention explicite ou source officielle directe | Appliquer |
| Probable | Plusieurs indices concordants | Appliquer et signaler |
| Ambiguë | Homonyme, taxonomie disputable ou source indirecte | Ne pas modifier sans validation |
