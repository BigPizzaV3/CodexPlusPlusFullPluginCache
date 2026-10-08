---
name: collecte-hypothecaire
description: "Bâtir, compléter, contrôler et maintenir un dossier de financement hypothécaire au Québec, incluant l'entrevue, les renseignements de demande, les justificatifs et la liste client. Utiliser après la rencontre-conseil ou pour vérifier un dossier existant; ne pas l'utiliser pour une simple simulation de capacité d'emprunt sans ouverture de dossier."
---

# Collecte hypothécaire

Transformer les renseignements disponibles, même partiels, en dossier de travail exploitable puis le maintenir jusqu'à la soumission au prêteur.

## Point de départ

La première rencontre est normalement une rencontre de conseil sans collecte administrative exhaustive. Activer ce skill après l'ouverture officielle du dossier ou quand Antoine demande explicitement de bâtir, compléter ou vérifier une demande.

Commencer avec tout ce qui est déjà fourni. Ne jamais redemander une information disponible dans la conversation, les fichiers ou une source autorisée. Accepter `?`, « inconnu » et « à confirmer » comme réponses valides et poursuivre sans bloquer.

## Modes

Déterminer le mode à partir de la demande; demander seulement si le choix change réellement le travail.

- **Nouvelle collecte** : créer une première structure à partir des données disponibles.
- **Prêteur non déterminé** : constituer la base nécessaire à l'analyse et signaler les exigences susceptibles de varier.
- **Prêteur déterminé** : ajouter uniquement les exigences particulières vérifiées du prêteur visé.
- **Vérification** : examiner un dossier ou une liste existante et mettre à jour son état sans repartir de zéro.

## Méthode

1. Identifier la transaction, les emprunteurs, l'immeuble, les revenus, la mise de fonds ou l'équité, les dettes, le crédit déclaré et les particularités.
2. Séparer clairement les **renseignements à inscrire dans la demande** des **documents justificatifs à obtenir**.
3. Poser les questions manquantes une à la fois quand Antoine demande une entrevue. Prioriser ce qui influence l'admissibilité, la stratégie, le prêteur ou la liste documentaire.
4. Adapter les demandes à chaque emprunteur et à sa situation réelle. Éliminer les documents génériques non applicables.
5. Détecter contradictions, dates incompatibles, montants non conciliés, trous d'emploi, provenance de fonds incertaine et autres éléments pouvant retarder ou bloquer le dossier.
6. Maintenir la même feuille de travail lorsque de nouvelles réponses ou pièces arrivent. Ne pas recréer une liste qui perd l'historique.
7. Terminer chaque passage par une prochaine action précise.

Pour les statuts, les livrables et les contrôles détaillés, lire [référence opérationnelle](references/operation.md).

## Exigences prêteur

Ne jamais présenter une préférence habituelle comme une exigence certaine. Pour une règle propre à un prêteur, utiliser une source actuelle et autorisée lorsqu'elle est accessible; sinon écrire « à vérifier auprès du prêteur » et isoler l'élément dans les points à confirmer.

## Confidentialité

Limiter les données personnelles au nécessaire. Ne pas reproduire inutilement NAS, numéros de comptes complets, identifiants gouvernementaux ou renseignements médicaux. Dans la version client, demander la catégorie de document sans exposer les données déjà reçues.

## Renommage

Pour `/renommer`, retourner uniquement :

`RENOMMER EN : AAAA-MM-JJ — Client — Sujet`

et indiquer le Project Hypothèque existant où classer la conversation.
