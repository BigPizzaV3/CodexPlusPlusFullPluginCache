---
name: lire-protocole
description: Use to load the canonical Protocol at chat opening or refresh only the material required by its reading gate when the session changes.
---
# Lire le Protocole

## Fonction
Charger ou rafraîchir la copie de session selon `01 — Porte de lecture.md`, seule demeure responsable des conditions de lecture. Le plugin est son miroir opératoire ; il ne fixe ni une autre règle de lecture ni la géographie de la Source Canonique.

## Déclenchement
- premier tour de tout nouveau tchat d’Azer ou d’un Magister Operis ;
- lorsqu’une modification du Protocole a été validée, signalée, établie ou rendue matériellement probable ;
- lorsque la copie de session du Protocole est incomplète, indisponible ou matériellement douteuse.

Le seul fait qu’Axel envoie un nouveau message dans le même tchat ne déclenche pas une nouvelle lecture intégrale si la copie de session reste complète et suffisamment fraîche.

## Résolution de l’entrée
La demeure canonique courante du Protocole est une donnée du canon et du contexte de la Source Canonique, pas une constante du plugin. Utiliser l’ancrage réellement établi dans la session. Si nécessaire, rechercher la demeure avec les moyens de lecture autorisés et reconnaître sa fonction à partir de sa Porte ; un ancien chemin reste un indice à vérifier, pas une autorité.

Le chargement suit le chemin faisant autorité selon `03 — Demeures et canonicalité.md` : Google Drive avant validation explicite du chemin local, puis le plugin et Noyau vers la représentation locale après cette validation. Une instruction applicable d’Axel sur le moyen de lecture est prise en compte sans inventer une validation générale du chemin d’écriture.

Si cet ancrage n’est pas réellement résolu ou accessible alors qu’aucune copie de session complète et suffisamment fraîche n’est disponible, suspendre toute réponse de fond et appliquer la défaillance d’amorçage au lieu d’inventer une demeure.

## Procédure
1. Ouvrir la demeure canonique courante du Protocole et commencer par `01 — Porte de lecture.md`.
2. À l’ouverture, lire intégralement les douze fichiers normatifs `01` à `12` dans l’ordre donné par cette Porte, du premier au dernier caractère. Le nombre courant est descriptif : une évolution ultérieure de la Porte gouverne le parcours.
3. Si un retour est tronqué ou paginé, poursuivre les portions manquantes avant de tenir la lecture pour complète. Une empreinte ou un manifeste de fichiers ne prouve pas leur lecture intégrale.
4. Établir cette lecture comme copie de session et conserver l’heure réelle de sa dernière lecture intégrale. Aux tours suivants, appliquer cette copie sans retour systématique à la source. Une modification connue et circonscrite recharge seulement les Documents modifiés et leurs raccords directement affectés ; une lecture intégrale est requise si la structure change, si l’étendue des changements est incertaine ou si la copie est incomplète, indisponible ou matériellement douteuse.
5. Sous Gardiennage, lorsque deux heures réelles se sont écoulées depuis cette lecture intégrale, relire `01 → 12` avant la première nouvelle action substantielle. Ne pas interrompre une opération atomique ou non rejouable : relire au premier point sûr. Hors Gardiennage, cette échéance ne déclenche pas à elle seule une relecture.
6. Ne consulter ni Projet, mission, Continuité, Verbatim ni Index comme substitut de la lecture requise. Un prompt de Passation, une pièce jointe ou un paquet injecté ne transporte pas une copie canonique du Protocole.
7. Si une implication matérielle reste incomprise, relire jusqu’à établissement, borne explicite ou absence de matérialité.
8. Après la Porte finale, effectuer les lectures personnelles de reprise encore requises avant le premier message de fond ; utiliser ensuite l’Index de la Source Canonique pour les demeures nécessaires.

## Défaillance
Si aucun état de session complet et suffisamment frais n’est disponible et que l’un des fichiers normatifs courants est inaccessible au point d’empêcher la lecture complète requise, suspendre toute réponse de fond et produire uniquement la défaillance d’amorçage prévue par le canon.

## Preuve
Copie de session complète établie par lecture intégrale d’ouverture, puis maintenue suffisamment fraîche par le rechargement ciblé ou intégral réellement requis par la Porte. Aucun contenu tronqué n’est déclaré lu.

## Raccords
`amorcer-continuum` route ici à l’ouverture du tchat ou lorsqu’un rafraîchissement est nécessaire. `executer-demande` démarre après l’Entrée Protocole du cycle courant, laquelle peut appliquer la copie de session déjà établie sans rappeler ce Skill.
