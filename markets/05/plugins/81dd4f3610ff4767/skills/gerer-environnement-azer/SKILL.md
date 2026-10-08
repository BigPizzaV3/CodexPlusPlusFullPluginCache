---
name: gerer-environnement-azer
description: Use when Azer's working environment, retained operational errors, or active recovery checkpoint must be read or updated.
---
# Gérer l’environnement d’Azer

## Fonction
Gérer les trois objets opérationnels distincts d’Azer dans `Environnement Continuum Azer` : `Cartographie Ordinateur Azer.md`, `Erreurs retenues.md` et `Reprise active Azer.md`. Ils ne remplacent ni Verbatim, ni Continuité, ni Histoire, ni trace d’exécution.

## Déclenchement
- un changement matériel affecte l’atelier, ses accès, capacités, chemins ou limites ;
- une erreur retenue peut éviter une répétition ou modifier une méthode ;
- un chantier long ou stateful exige un checkpoint pour reprendre sans rejouer un effet.

## Procédure
1. Résoudre les objets par l’Index de la Source Canonique et employer le chemin d’écriture faisant autorité.
2. Mettre à jour la Cartographie seulement pour l’état courant utile au travail ; remplacer ou retirer une valeur fausse au lieu de créer un historique.
3. Inscrire une erreur retenue avec identifiant durable, contexte, symptôme, cause établie ou supposée, conséquences, correction, prévention et statut, seulement si son enseignement est réutilisable.
4. Tenir `Reprise active Azer.md` comme checkpoint courant : statut, horodatage, cap, acquis, contraintes, dépendances, effets non rejouables, limites et prochaine action utile. Remplacer l’état devenu obsolète ; ne pas y recopier la conversation, les logs ou le raisonnement privé.
5. Pour une écriture canonique, appliquer `proteger-concurrence` et `gerer-transactions` seulement lorsque le risque ou l’état partagé le justifie. Un succès explicite suffit par défaut ; ne pas faire une seconde écriture de miroir par cérémonie.

## Interdits
- ne jamais transformer ces objets en journal exhaustif ou en second Verbatim ;
- ne jamais conserver un checkpoint `EN COURS` devenu faux ;
- ne jamais déduire un état volatile sans le rafraîchir lorsqu’un événement connu l’a rendu douteux.

## Preuve
Chaque objet concerné porte l’état courant suffisant à sa fonction, sur le chemin canonique autoritaire ; une reprise peut partir du checkpoint sans rejouer aveuglément un effet matériel.

## Arrêt
Ne mettre à jour aucun objet lorsqu’aucun changement matériel ne le requiert.
