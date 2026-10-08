---
name: preparer-mission-magister
description: Use before delegating work to a Magister Operis so the mission is bounded, routable, verifiable, and small enough for a non-permanent actor to finish without Passation.
---
# Préparer une mission de Magister Operis

## Procédure
1. Qualifier l’acteur via `qualifier-magister`.
2. Définir objectif, périmètre, sources responsables, contraintes, autorité, livrable, destination, critères de réussite et preuve.
3. Construire un contexte délégué minimal suffisant : décisions applicables, état de départ, interfaces, dépendances, hors-périmètre et inconnues utiles ; ne jamais supposer que le Magister Operis « a le tchat ».
4. Identifier les dépendances partagées et protections de concurrence nécessaires.
5. Pour un non permanent, découper la mission assez finement pour qu’elle soit achevable sans Passation ; une saturation prévisible impose un redécoupage avant délégation.
6. Préparer le courrier et résoudre sa demeure ainsi que la route de mission avant tout appel local.
7. N’appeler `agir-par-noyau` ou `appeler-passerelle` que lorsque le transport ou l’effet local l’exige réellement.
8. Créer ou reprendre le Magister dans le Projet adapté sur `Chat` lorsque cette surface est disponible ; ne pas employer `Work` comme repli. Pour un permanent, préserver son Projet propre et son paquet de reprise afin qu’un moyen technique saturé puisse être remplacé sans changer l’acteur.

## Preuve
La mission peut être exécutée, contrôlée et close sans que le Magister Operis reconstruise le besoin ni reçoive du contexte sans fonction.
