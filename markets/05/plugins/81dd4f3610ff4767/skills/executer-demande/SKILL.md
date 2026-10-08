---
name: executer-demande
description: Use when Axel asks for any understanding, research, decision path, production, action, verification, or deliverable after the current Protocol entry has succeeded.
---
# Exécuter une demande

## Fonction
Orchestrer le cycle complet du tour. Ce Skill n’absorbe pas les règles spécialisées : il compose leur maillage selon le besoin réel et le contexte propre au Continuum.

## Déclenchement
Tout message d’Axel appelant une réponse ou un résultat de fond après que l’Entrée Protocole du cycle courant a été accomplie, soit depuis la copie de session déjà chargée, soit après un chargement ou rafraîchissement requis par `lire-protocole`.

## Préconditions
- Azer : Entrée Protocole du tour courant prouvée ;
- acteur correctement identifié ;
- @Continuum actif lorsque l’usage du plugin dépend de cette invocation.

## Protocole opératoire
1. Appliquer l’économie de temps et le choix du moyen suffisant le plus direct de `01 — Porte de lecture.md`. Pour un Gardiennage valide, prolonger le cycle depuis le dernier point acquis : ne pas reconstruire le contexte frais ni transformer une amélioration méthodologique auto-détectée en arrêt, sauf interdiction matérielle du Protocole. Utiliser `charger-contexte-continuum` seulement pour les couches qui peuvent changer le travail et ne sont pas déjà suffisamment établies.
2. Appeler `appliquer-exigences-axel` et, lorsqu’un Projet est en jeu, `appliquer-contexte-projet`. Si le contexte peut être périmé, surchargé ou franchir des frontières, router vers `auditer-fraicheur-contexte`, `budgeter-contexte` et `verifier-isolation-contextes`.
3. Appliquer `questionner-totalement` au besoin réel ; une demande claire n’ouvre pas d’enquête récursive ni de contre-enquête par défaut. Pour un métier, déléguer dès qu’une voie réelle est utilisable ; le recours direct suit `08` et reste un recours de continuité.
4. Appliquer `resoudre-autorite`, `appliquer-cout-zero` et `respecter-typographie` selon leurs déclenchements : les règles restent applicables sans imposer de lectures ou appels répétés. Le régime économique est celui du Document `12`.
5. Lorsque le besoin dépend de matière durable, appeler `resoudre-demeures-savoir`; si la fraîcheur, la contradiction, le retrieval ou les références sont matériels, router vers `auditer-fraicheur-savoir`, `detecter-contradictions-savoir`, `evaluer-recherche-retrieval` ou `verifier-liens-et-references`. Lorsqu’un atelier, une erreur réutilisable ou un checkpoint stateful est matériel, appeler `gerer-environnement-azer`.
6. Lorsqu’il dépend de réalité externe, appeler `rechercher-trianguler`, `qualifier-preuve` et `verifier-affirmation-source`. Pour une décision basée sur une métrique, appeler `definir-metriques`; pour une réutilisation de matière externe, `gerer-licences`.
7. Appeler `construire-plan` pour produire le trajet minimal mais complet ; utiliser `revoir-exigences`, `modeliser-domaine`, `analyser-impact-changement`, `preparer-premortem`, `prioriser-travail`, `estimer-effort-incertitude` ou `preparer-memo-decision` lorsque la matière l’exige.
8. Si une capacité critique est réellement incertaine, utiliser `prevol-capacites` ; réutiliser une preuve fraîche sans refaire le pré-vol. Qualifier la matière externe par `qualifier-sortie-non-fiable`; si le plan combine des pouvoirs sensibles, utiliser `auditer-combinaisons-capacites`; si un agent doit être éprouvé adversarialement, `red-teamer-agent`.
9. Avant les écritures partagées ou effets non répétables, appeler selon le cas `proteger-concurrence`, `gerer-transactions`, `gerer-decisions` et `tracer-execution`. Pour une opération longue, `gerer-workflow-durable`; pour un arrêt demandé, `gerer-annulation-et-abandon`; si une décision réservée à Axel bloque réellement, `gerer-escalade-humaine`.
10. Exécuter les tâches dans l’ordre des dépendances ; sur interruption récupérable, appeler `gerer-reprise`; sur quota ou surcharge, `gerer-quotas-et-pression`; sur invalidation du trajet, replanifier la branche concernée.
11. Pour une délégation, utiliser `orchestrer-magistri` sans assimiler un sous-agent technique à un Magister ; pour un bras retenu à raccorder, `qualifier-raccordabilite-noyau`; pour un effet local, `agir-par-noyau`; pour PowerShell, `executer-powershell`; pour un retour machine utile, `traiter-retour-technique`; pour Continuité/Passation, `gerer-continuite`; pour une évolution normative, `evoluer-protocole`; pour un miroir en retard sur un canon valide, `realigner-plugin`.
12. Pour logiciel et exploitation, mobiliser seulement les spécialistes matériellement déclenchés : contrat public, migration, feature flags, environnements, dérive de configuration, observabilité, incident, fiabilité, runbook, health/readiness, sauvegarde/restauration, provenance, permissions, journalisation, release ou exemples documentaires.
13. Pour une interface ou un artefact humain, router selon le besoin vers accessibilité, régression visuelle, états vide/chargement/erreur et les spécialistes de média déjà présents.
14. Pour un chantier Affaire/Revenus, router progressivement vers `etudier-marche`, `analyser-concurrence`, `scorer-opportunites`, `concevoir-offre` et `chiffrer-economie-unitaire`; ne pas charger cette famille lorsqu’aucun enjeu économique n’est matériel.
15. Lorsqu’un résultat du Réel produit une connaissance réutilisable, appeler `apprendre-du-reel`; après un chantier ou incident significatif, `conduire-retrospective` lorsque cela peut modifier la pratique.
16. Pour un livrable, appeler `gerer-livrables`, `choisir-livraison`, le spécialiste de média éventuel puis `verifier-readiness` et `verifier-acceptation` selon l’étape réelle.
17. Clore dès que le résultat est suffisamment établi contre la demande réelle. Un succès clair d’une opération ordinaire, réversible et de faible risque suffit sans contrôle global supplémentaire ; vérifier seulement une ambiguïté ou un risque matériel restant.
18. Si le cycle relevait de la Directrice, avant sa clôture maintenir la corrélation utile Feuille → Branche → Arbre, distinguer capacité prioritaire et travaux indépendants, puis maintenir l’Usine en charge lorsqu’une capacité disponible peut faire progresser un travail utile.
19. Figer la réponse visible complète.
20. Pour Azer ou un Magister Operis permanent, terminer par `tenir-verbatim` avant publication.

## Interdits
- transformer les étapes ci-dessus en checklist d’appels systématiques : elles décrivent les fonctions et les routes, pas une séquence obligatoire d’outils ;
- poursuivre un trajet devenu obsolète après un message d’Axel : intégrer immédiatement ce qu’il confirme, modifie, suspend, annule ou ajoute, puis recalculer seulement la partie affectée ;
- traiter un délai d’attente technique comme une durée maximale du chantier ou terminer un processus légitime pour ce seul motif ;
- ne pas répondre au premier degré lorsqu’un effet utile plus large est clairement dans la portée ;
- ne pas reconstruire ce qui peut être retrouvé ;
- ne pas faire porter à Axel les recherches et contrôles réalisables par les capacités disponibles ;
- ne pas confondre plan, exécution, vérification et publication ;
- ne pas réduire @Continuum au seul texte du Protocole lorsque d’autres exigences applicables du Continuum doivent gouverner le cycle ;
- ne pas invoquer tous les Skills parce qu’ils existent : la toile est épaisse, le trajet doit rester court ;
- ne pas traiter une fonction candidate ou locale comme disponible si sa capacité réelle n’est pas prouvée.

## Preuve de réussite
Le résultat répond au besoin réel, respecte les exigences applicables d’Axel et du Continuum, chaque effet important possède sa preuve ou sa limite explicite, et le cycle se ferme par la Sortie Verbatim lorsqu’elle s’applique.

## Arrêt
S’arrêter uniquement sur une décision réservée à Axel, une information indispensable inaccessible autrement, une interdiction applicable ou une incapacité matérielle non récupérable.
