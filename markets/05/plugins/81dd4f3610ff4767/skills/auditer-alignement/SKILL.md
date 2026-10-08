---
name: auditer-alignement
description: Use to prove whether the Continuum plugin fully covers the current canonical Protocol and whether its skills form a coherent non-contradictory implementation mesh.
---
# Auditer l’alignement

## Fonction
Remplacer l’impression « cohérent dans son principe » par une preuve de couverture et de cohérence.

## Procédure
1. Établir une copie de session complète et suffisamment fraîche selon `01 — Porte de lecture.md` ; la réutiliser si elle est déjà acquise. Ne pas créer de relecture intégrale systématique par cet audit.
2. Décomposer chaque responsabilité exécutable matérielle en unité de couverture.
3. Pour chacune, identifier le ou les Skills responsables, leurs déclenchements, préconditions, interdits, sorties, preuves et raccords.
4. Signaler toute responsabilité sans Skill, tout Skill sans responsabilité, toute duplication d’autorité, tout monolithe qui fusionne des fonctions indépendantes et toute contradiction entre Skills.
5. Vérifier les raccords transversaux : autorité, économie de temps, preuve proportionnée, régime économique, typographie, demeure, canonicalité, concurrence, transaction, reprise et acceptation. Vérifier aussi Branches/Feuilles, objets d’environnement, identité, contexte de mission et compétences spécialisées ; douze titres ne suffisent pas à couvrir le plugin.
6. Vérifier la cohérence du graphe d’invocation et les cycles intentionnels.
7. Exécuter les tests statiques disponibles puis les scénarios d’acceptation sur la version réellement chargée lorsque possible.
8. Employer `ALIGNÉ` uniquement lorsque la couche visée est effectivement couverte et vérifiée ; sinon nommer le delta exact.
9. Distinguer tests de structure, scénarios de décision effectivement évalués et comportements réellement observés. Un catalogue de scénarios non exécutés ne vaut pas acceptation.

## Sortie
Matrice de couverture, défauts précis, état de chaque couche et preuve de fermeture.
