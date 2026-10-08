---
name: livrer
description: Use when a visible reply, human-facing document, report, decision surface, or final deliverable must be prepared from an established Continuum result.
---
# Livrer

## Fonction
Transformer un résultat établi en surface humaine fidèle, lisible et proportionnée au statut réel des preuves.

## Protocole opératoire
1. Ne pas rouvrir le fond dans ce Skill; partir du résultat déjà établi ou convergé.
2. Identifier audience, format demandé, niveau de détail utile et contraintes de langue/typographie.
3. Appeler `gerer-livrables` et `choisir-livraison`; utiliser les spécialistes d’artefacts lorsque le format l’exige.
4. Porter exactement les statuts `PROUVE`, `NON_PROUVE`, `CONTRADICTOIRE`, `LIMITE`, décision, hypothèse ou proposition sans les promouvoir.
5. Une copie technique soutient la preuve; elle ne remplace pas la copie humaine lorsqu’une décision humaine est visée.
6. Vérifier fichiers, liens, nombres, dates et ressources annoncées; ne jamais inventer citation, URL ou artefact.
7. Garder sous le capot les logs, appels d’outils et détails d’orchestration inutiles.
8. Appeler `verifier-document-rendu` ou `verifier-coherence-multiformat` lorsqu’ils sont matériels au livrable.
9. Remettre la surface finale à `tenir-verbatim` lorsque l’exact visible doit être préservé; ce Skill n’écrit jamais lui-même le Verbatim.

## Preuve
Le livrable répond au périmètre demandé, n’amplifie aucun claim, ne contient aucune ressource inventée et est directement utilisable par son audience.
