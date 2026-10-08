---
name: evoluer-protocole
description: Use when Axel asks to change canonical Protocol matter, or when plugin implementation must be realigned to an already valid canonical Protocol.
---
# Faire évoluer le Protocole ou son implémentation

## Fonction
Distinguer strictement deux trajets : évolution normative et réalignement d’implémentation.

## Protocole opératoire
### A. Évolution normative
1. Appliquer `resoudre-autorite` et la copie de session du canon. La Porte `01` détermine seule le rechargement ciblé ou intégral nécessaire ; cet examen ne crée pas de relecture intégrale concurrente. Utiliser `proteger-concurrence` pour le repère utile de l’état visé.
2. Préparer la formulation minimale et contrôler sa cohérence avec le canon entier.
3. Si Axel a déjà validé clairement le principe, la correction ou demandé son intégration, intégrer directement cette formulation lorsqu’elle n’ajoute aucune décision matérielle. Si elle étend le périmètre, l’autorité, les coûts, les effets externes ou tranche une ambiguïté non résolue, présenter alors le texte exact à Axel avant écriture.
4. Juste avant l’écriture, relire l’état canonique visé et vérifier qu’il correspond encore à l’état préparé. S’il a changé matériellement, suspendre, recomposer le delta et représenter à Axel toute partie candidate modifiée avant écriture.
5. Appliquer exactement le changement validé dans la demeure responsable par le chemin faisant autorité défini dans `03` ; si la liste ou le nom des fichiers normatifs change, mettre à jour `01 — Porte de lecture.md` et les raccords dans la même évolution.
6. Établir la conformité de l’écriture au changement autorisé au niveau requis. Actualiser les seuls Documents modifiés et leurs raccords dans la copie de session, sauf condition de relecture intégrale selon `01`. Utiliser `synchroniser-miroir` seulement si la concordance secondaire est matériellement nécessaire, sans seconde écriture applicative.
7. Appeler `realigner-plugin` puis `auditer-alignement` pour les comportements exécutables affectés.

### B. Réalignement d’implémentation
Si le canon est déjà valide et seul le plugin est en retard, ne pas modifier ni faire revalider le Protocole. Appeler directement `realigner-plugin`, mettre à jour les tests et exécuter `auditer-alignement`.

Un retour d’Axel qui modifie la conduite d’Azer déclenche l’examen prévu par `02` : examiner si une règle manque, est ambiguë ou doit être renforcée, puis distinguer correction d’application et formulation normative déjà autorisée ou extension à valider. Le prompt de Gardiennage ne vaut ni décision ni retour d’Axel et n’interrompt pas seul le travail pour proposer une évolution.

## Interdits
- ne jamais traiter les tests existants comme autorité normative ;
- ne jamais faire évoluer le canon pour satisfaire une implémentation en retard ;
- ne jamais appeler ALIGNÉ une version simplement modifiée dans sa source.

## Preuve de réussite
Le canon, la source, les tests, la version publiée/installée et le comportement chargé sont qualifiés séparément, et l’état déclaré correspond à la preuve disponible.

## Arrêt
S’arrêter avant toute évolution normative si la validation explicite d’Axel manque.
