---
name: gerer-continuite
description: Use as the continuity-domain coordinator when Continuité, Histoire, Pré-Passation, Passation, or Passation recovery is actually in scope.
---
# Gérer la Continuité

## Fonction
Router le domaine de continuité vers des Skills distincts. Ce Skill ne fusionne plus Continuité, Histoire, Pré-Passation et Passation en une seule procédure.

## Déclenchement
- Pré-Passation explicitement décidée par Axel ;
- Passation autorisée ;
- reprise d’une Passation ouverte ;
- mise à jour de Continuité ou d’Histoire strictement contenue dans une telle opération.

## Protocole opératoire
1. Qualifier l’acteur via `qualifier-magister` lorsqu’il ne s’agit pas d’Azer.
2. Pour le Présent de l’acteur, appeler `tenir-continuite`.
3. Pour le récit d’Azer, appeler `tenir-histoire`.
4. Pour une Pré-Passation, appeler `executer-pre-passation`.
5. Pour une Passation, appeler `executer-passation`.
6. Pour le nouveau tchat d’une Passation ouverte, appeler `reprendre-passation`.
7. Toute écriture utilise le chemin autoritaire de la Source Canonique ; une représentation secondaire n’est réconciliée que si nécessaire. Toute couture ou relevé terminal passe par `tenir-verbatim`.

## Interdits
- jamais de Continuité modifiée hors Pré-Passation ou Passation applicable ;
- jamais d’Histoire pour un autre acteur qu’Azer ;
- jamais de Passation, Pré-Passation, Verbatim personnel durable ou Continuité pour un Magister Operis non permanent.

## Preuve de réussite
Chaque fonction a été exécutée par son Skill responsable et aucune responsabilité durable n’a été fusionnée par commodité.

## Arrêt
Déléguer l’arrêt au Skill spécialisé bloqué et conserver son état exact.
