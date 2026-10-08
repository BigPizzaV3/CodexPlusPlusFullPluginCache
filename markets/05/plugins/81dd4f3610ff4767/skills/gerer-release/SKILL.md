---
name: gerer-release
description: Use when a durable software or plugin change is about to move from candidate source into a released or installed state.
---
# Gérer une release

## Fonction
Traiter la mise en production comme un changement d’état observable et réversible au niveau réellement disponible.

## Procédure
1. Définir version, contenu exact, critères de succès et incompatibilités.
2. Établir état précédent récupérable ou procédure de repli réellement possible.
3. Vérifier tests et artefact qui sera effectivement publié.
4. Publier selon une identité de release stable.
5. Observer installation / chargement / comportement réel après release.
6. Décider poursuivre, corriger ou revenir selon les signaux établis.

## Preuve
Source, artefact, release, installation et comportement chargé sont qualifiés séparément.