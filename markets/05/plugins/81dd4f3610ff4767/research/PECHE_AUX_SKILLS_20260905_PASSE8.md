# Pêche aux Skills — Passe 8 — Horizon des chantiers

Date : 5 septembre 2026

Document de recherche non normatif. Cette passe part d’un changement de stratégie explicite : ne plus limiter la pêche aux besoins immédiats de @Continuum. Une fonction peut être conservée parce qu’elle a de fortes chances de devenir utile dans un chantier futur, même si aucun travail courant ne la déclenche aujourd’hui.

État de départ observé : la version source porte `0.4.0` et le runtime du tchat courant expose 92 ressources Skills. Axel indique en outre que la 0.4 est publiée et qu’un Magister Operis nouvellement lancé a déjà mobilisé plusieurs Skills du maillage élargi. Ce constat ne vaut pas test exhaustif des 92 Skills ; il établit que la pêche peut maintenant travailler comme réserve d’évolution plutôt que comme réparation de l’ancienne architecture à huit blocs.

## États de cette passe

- `PROCHAINE VAGUE` : fonction générale, distincte, forte probabilité d’usage ; candidate prioritaire à la prochaine adoption.
- `RÉSERVE CHANTIER` : fonction crédible et potentiellement importante, mais à conserver jusqu’au chantier qui lui donnera son contexte réel.
- `ÉPAISSIR` : mécanisme à incorporer dans un Skill déjà responsable plutôt qu’à dupliquer.
- `LOCAL` : fonction dont l’effet réel dépendra de Noyau, de la Passerelle ou d’une autre capacité locale prouvée.
- `VEILLE` : idée valable mais encore trop spéculative, trop spécialisée ou sans déclenchement suffisamment net.

Aucun élément de cette passe n’est installé automatiquement. La Banque sert de vivier : proposition → qualification → décision d’adoption → conception → tests → release.

---

## A — Autonomie durable, orchestration et agents

| Candidat | Fonction | État |
|---|---|---|
| `gerer-workflow-durable` | Porter un travail long comme une suite d’étapes persistantes avec reprise depuis le dernier état prouvé, temporisations, signaux, erreurs partielles et humain dans la boucle. | PROCHAINE VAGUE |
| `gerer-annulation-et-abandon` | Distinguer annulation demandée, arrêt sûr, compensation, nettoyage et abandon irréversible ; prouver ce qui a réellement cessé. | PROCHAINE VAGUE |
| `gerer-escalade-humaine` | Escalader à Axel uniquement quand une décision, un risque ou une information l’exige réellement ; regrouper les décisions bloquantes et conserver le contexte utile. | PROCHAINE VAGUE |
| `gerer-file-travail` | Priorités, dépendances, déduplication, backpressure, vieillissement des tâches et admission contrôlée d’un flux de missions. | RÉSERVE CHANTIER |
| `gerer-portefeuille-missions` | Arbitrer plusieurs chantiers concurrents selon valeur, urgence, blocages, dépendances, capacité et décisions d’Axel. | RÉSERVE CHANTIER |
| `planifier-capacite-agentique` | Mesurer capacité réelle des acteurs/outils, saturation, goulots et parallélisme utile avant de multiplier les délégations. | RÉSERVE CHANTIER |
| `tester-chaos-agentique` | Injecter des pannes contrôlées : sortie d’outil absente, tchat saturé, connecteur lent, message dupliqué, acteur indisponible ; vérifier la reprise et les invariants. | RÉSERVE CHANTIER |
| `verifier-isolation-contextes` | Vérifier qu’un acteur, Projet ou mission ne reçoit pas de contexte, droit ou secret qui appartient à un autre périmètre. | PROCHAINE VAGUE |
| `budgeter-contexte` | Allouer le contexte par valeur pour la tâche : ce qui doit être présent, retrouvable, compressé ou exclu ; mesurer la perte de fidélité plutôt que maximiser la compression. | PROCHAINE VAGUE |
| `evaluer-retrieval-memoire` | Tester rappel, précision, fraîcheur, provenance et omissions d’un mécanisme de mémoire/retrieval avec questions représentatives. | RÉSERVE CHANTIER |
| `auditer-fraicheur-contexte` | Détecter instructions, états, routes, versions et décisions devenues périmées avant qu’elles ne gouvernent un nouveau travail. | PROCHAINE VAGUE |

## B — Savoir, mémoire et architecture de l’information

| Candidat | Fonction | État |
|---|---|---|
| `auditer-fraicheur-savoir` | Identifier les fiches dont la date, la version ou les sources ne permettent plus de gouverner un travail actuel. | PROCHAINE VAGUE |
| `detecter-contradictions-savoir` | Chercher activement deux fiches ou affirmations responsables incompatibles et produire la couture de résolution ou l’état `DOUTE`. | PROCHAINE VAGUE |
| `gerer-obsolescence-savoir` | Remplacer, fusionner ou borner une connaissance ancienne sans effacer ce qui reste historiquement utile. | PROCHAINE VAGUE |
| `construire-taxonomie` | Concevoir catégories, relations et vocabulaire d’un corpus quand la simple arborescence ne suffit plus à retrouver correctement la matière. | RÉSERVE CHANTIER |
| `evaluer-recherche-retrieval` | Mesurer si une recherche retrouve les bonnes sources : rappel, précision, couverture, fraîcheur, classement et erreurs de récupération. | PROCHAINE VAGUE |
| `dedoublonner-matiere` | Détecter doublons exacts, quasi-doublons et responsabilités concurrentes avant conservation durable. | PROCHAINE VAGUE |
| `verifier-liens-et-references` | Contrôler ancres, URL, identifiants, références croisées, citations internes et destinations après changement structurel. | PROCHAINE VAGUE |
| `auditer-architecture-information` | Tester si une demeure, un Index ou une navigation permettent à l’acteur réel de retrouver l’objet sans connaissance tacite. | RÉSERVE CHANTIER |
| `mesurer-valeur-savoir` | Évaluer si une fiche durable réduit réellement recherche, erreurs ou temps futur ; éviter de transformer le Savoir en grenier. | RÉSERVE CHANTIER |

## C — Affaire, revenus, marché et produit

| Candidat | Fonction | État |
|---|---|---|
| `etudier-marche` | Définir marché, segments, demande, comportements, concurrents et incertitudes avec hypothèses auditables plutôt qu’un TAM inventé. | PROCHAINE VAGUE |
| `analyser-concurrence` | Comparer offres, prix, canaux, preuves, positionnement et expérience réelle ; distinguer faits publics et inférences. | PROCHAINE VAGUE |
| `scorer-opportunites` | Classer opportunités par probabilité de revenu, coût humain, délai, risque, répétabilité, concurrence et compatibilité coût 0. | PROCHAINE VAGUE |
| `definir-proposition-valeur` | Relier problème réel, bénéficiaire, résultat, preuve, différence et raison de choisir l’offre. | RÉSERVE CHANTIER |
| `concevoir-offre` | Transformer une capacité du Continuum en produit/service borné : entrée, sortie, promesse, limites, prix, preuve et charge humaine. | PROCHAINE VAGUE |
| `chiffrer-economie-unitaire` | Coût par acquisition/production/livraison, marge, commissions, temps humain et seuil de viabilité ; raisonner en net. | PROCHAINE VAGUE |
| `construire-prix` | Étudier ancrages de valeur, coûts, alternatives, segmentation et test de prix sans confondre prix optimal et prix plausible. | RÉSERVE CHANTIER |
| `mesurer-funnel` | Acquisition → activation → conversion → rétention → revenu ; définir événements et pertes plutôt que se contenter d’un total final. | RÉSERVE CHANTIER |
| `analyser-cohortes-retention` | Séparer effets de date, canal et type d’utilisateur pour comprendre rétention et répétition réelles. | RÉSERVE CHANTIER |
| `qualifier-feedback-client` | Transformer avis, tickets, commentaires et verbatims en signaux reliés à segments, fréquence, sévérité et preuve. | PROCHAINE VAGUE |
| `prioriser-demandes-produit` | Prioriser demandes par fréquence, valeur, stratégie, coût de changement, risque et clients affectés ; ne pas confondre bruit et demande. | RÉSERVE CHANTIER |
| `preparer-lancement` | Vérifier promesse, canal, instrumentation, support, rollback, conformité, contenu et critères de succès avant exposition publique. | RÉSERVE CHANTIER |
| `auditer-onboarding` | Observer le premier usage réel, mesurer frictions et points d’abandon et vérifier que la valeur promise est atteignable sans aide cachée. | RÉSERVE CHANTIER |
| `auditer-support` | Transformer support en boucle d’apprentissage : triage, sévérité, résolution, SLA éventuel, causes récurrentes et alimentation du Savoir. | RÉSERVE CHANTIER |
| `prevoir-revenu-capacite` | Relier capacité de production, demande, conversion, délai et prix pour borner un revenu plausible avec scénarios. | RÉSERVE CHANTIER |
| `auditer-facturation-reconciliation` | Rapprocher commande, facture, paiement, commission, remboursement et revenu net ; détecter écarts et doubles effets. | RÉSERVE CHANTIER |
| `planifier-distribution-canal` | Comparer canaux selon audience, règles, coût 0, dépendance plateforme, attribution et charge opérationnelle. | RÉSERVE CHANTIER |

## D — Pilotage de chantiers et décisions

| Candidat | Fonction | État |
|---|---|---|
| `prioriser-travail` | Ordonner tâches selon dépendances, valeur, risque, urgence et coût d’attente, pas selon visibilité ou facilité. | PROCHAINE VAGUE |
| `gerer-roadmap` | Maintenir horizon, séquences et objectifs sans transformer une projection en promesse ou en vérité du Présent. | RÉSERVE CHANTIER |
| `identifier-chemin-critique` | Trouver la chaîne qui détermine réellement la date de fin et les marges des autres tâches. | RÉSERVE CHANTIER |
| `estimer-effort-incertitude` | Donner fourchettes, hypothèses, dépendances et niveau de confiance plutôt qu’un chiffre décoratif. | PROCHAINE VAGUE |
| `gerer-risques-projet` | Registre vivant : risque, probabilité, impact, détecteur, propriétaire, mitigation et condition de fermeture. | ÉPAISSIR |
| `tenir-dependances` | Cartographier ce qui bloque quoi, l’état réel de chaque dépendance et les conséquences d’un changement. | RÉSERVE CHANTIER |
| `preparer-memo-decision` | Condenser décision, options, preuves, coûts, risques, réversibilité et recommandation sans perdre les incertitudes. | PROCHAINE VAGUE |
| `conduire-retrospective` | Après chantier : ce qui a marché, échoué, coûté, surpris, quelles pratiques changer et quelles leçons méritent le Savoir. | PROCHAINE VAGUE |
| `verifier-readiness` | Gate de passage entre conception, construction, test, publication, exploitation ou transmission avec critères propres à l’étape. | PROCHAINE VAGUE |

## E — Droit, conformité, confidentialité et gouvernance

| Candidat | Fonction | État |
|---|---|---|
| `analyser-contrat` | Extraire parties, obligations, droits, échéances, résiliation, données, propriété, risques et ambiguïtés, sans prétendre remplacer un conseil juridique. | RÉSERVE CHANTIER |
| `evaluer-impact-vie-privee` | Cartographier données, finalités, personnes concernées, flux, risques, minimisation, conservation et mesures de protection. | PROCHAINE VAGUE |
| `gerer-droits-donnees` | Identifier demandes d’accès, correction, suppression, portabilité ou opposition et leurs preuves/limites selon le régime réellement applicable. | RÉSERVE CHANTIER |
| `auditer-conformite` | Transformer obligations applicables en contrôles vérifiables, preuves attendues, écarts et remédiations. | RÉSERVE CHANTIER |
| `constituer-dossier-preuve-conformite` | Conserver preuve, version, date, propriétaire, contrôle et portée sans fabriquer une conformité à partir de documentation seule. | RÉSERVE CHANTIER |
| `gerer-licences` | Résoudre licences code, données, médias, modèles et contenus ; compatibilité, attribution, redistribution et obligations. | PROCHAINE VAGUE |
| `auditer-residence-donnees` | Localisation logique/juridique, sous-traitants, transferts, réplications et sauvegardes quand la résidence est matérielle. | VEILLE |
| `gerer-consentement-preferences` | État du consentement, finalité, version, retrait et preuve ; éviter de confondre préférence produit et base juridique. | VEILLE |

## F — Données, statistique et expérimentation

| Candidat | Fonction | État |
|---|---|---|
| `analyser-statistiquement` | Choisir statistique descriptive/inférentielle adaptée, vérifier hypothèses, incertitude, taille d’effet et limites. | PROCHAINE VAGUE |
| `analyser-causalite` | Distinguer association et causalité ; DAG/hypothèses, confondeurs, identification, expériences ou quasi-expériences lorsque nécessaires. | RÉSERVE CHANTIER |
| `detecter-anomalies` | Définir baseline, saisonnalité, seuils et coût des faux positifs avant d’étiqueter un point comme anomalie. | RÉSERVE CHANTIER |
| `prevoir-serie-temporelle` | Horizon, saisonnalité, ruptures, intervalles et backtesting ; comparer à une baseline naïve. | RÉSERVE CHANTIER |
| `profiler-donnees` | Grain, types, distributions, cardinalités, manquants, doublons, outliers, clés et dépendances avant analyse. | ÉPAISSIR |
| `evaluer-biais-echantillon` | Population cible, recrutement, couverture, non-réponse, survivants et pondération avant généralisation. | PROCHAINE VAGUE |
| `gerer-valeurs-manquantes` | Qualifier mécanisme de manque, impact, stratégie d’imputation/exclusion et sensibilité de la conclusion. | RÉSERVE CHANTIER |
| `definir-metriques` | Définition, numérateur/dénominateur, grain, fenêtre, source, propriétaire et anti-métrique pour éviter les KPI ambigus. | PROCHAINE VAGUE |
| `auditer-instrumentation-analytics` | Vérifier événements, propriétés, déclencheurs, déduplication, identité, consentement et cohérence avant d’utiliser une métrique. | RÉSERVE CHANTIER |

## G — Logiciel, exploitation et résilience

La Passe 7 contient déjà contrats publics, migrations, feature flags, observabilité, incidents, SLI/SLO, impact de changement, quotas et sauvegarde/restauration. Cette passe ajoute les compléments suivants.

| Candidat | Fonction | État |
|---|---|---|
| `gerer-environnements` | Séparer dev/test/staging/prod, configuration, données, secrets et différences connues ; empêcher qu’un résultat local soit généralisé sans preuve. | PROCHAINE VAGUE |
| `detecter-derive-configuration` | Comparer état voulu et état observé, identifier dérive autorisée ou accidentelle et impact. | PROCHAINE VAGUE |
| `construire-reproductiblement` | Même source + dépendances/verrous + environnement défini → artefact vérifiable ; conserver provenance et hash quand la fonction l’exige. | RÉSERVE CHANTIER |
| `verifier-determinisme` | Tester si répétition à état identique produit même résultat ou qualifier explicitement les sources de non-déterminisme. | RÉSERVE CHANTIER |
| `generer-runbook` | Transformer un incident/opération récurrente en procédure avec préconditions, diagnostics, décisions, actions, rollback et preuves. | PROCHAINE VAGUE |
| `tester-chaos` | Dégrader volontairement une dépendance dans un périmètre sûr afin d’éprouver récupération, observabilité et blast radius. | RÉSERVE CHANTIER |
| `planifier-capacite` | Charge, débit, saturation, marge, croissance et limites des dépendances avant qu’un système ne soit déclaré dimensionné. | RÉSERVE CHANTIER |
| `verifier-health-readiness` | Distinguer vivant, prêt, fonctionnel et apte à recevoir du trafic/travail ; concevoir checks réellement discriminants. | PROCHAINE VAGUE |

## H — Interface, contenu et expérience humaine

| Candidat | Fonction | État |
|---|---|---|
| `tester-regression-visuelle` | Baseline déterministe, comparaison, seuil, revue humaine des différences pertinentes et mise à jour explicite de la référence. | PROCHAINE VAGUE |
| `gerer-localisation` | Traduction, pluralisation, formats locaux, expansion du texte, direction, contenus et tests par locale. | RÉSERVE CHANTIER |
| `preserver-voix` | Maintenir style, ton, terminologie et interdits d’une marque/personne à travers formats et réécritures. | RÉSERVE CHANTIER |
| `auditer-formulaires` | Validation, erreurs, labels, clavier, autofill, données sensibles, états partiels et récupération. | RÉSERVE CHANTIER |
| `auditer-etats-vide-chargement-erreur` | Vérifier que l’interface reste compréhensible et actionnable hors du seul happy path. | PROCHAINE VAGUE |
| `auditer-notifications` | Priorité, destinataire, canal, répétition, accusé, action attendue et bruit ; éviter l’alerte sans décision. | RÉSERVE CHANTIER |
| `verifier-responsive` | Usages et ruptures sur tailles/zoom/orientation, pas seulement capture desktop. | RÉSERVE CHANTIER |
| `evaluer-decouvrabilite-recherche` | Navigation, libellés, recherche, synonymes, zéro résultat et capacité à retrouver l’objet sans connaître son chemin. | RÉSERVE CHANTIER |

## I — Sécurité et confiance

| Candidat | Fonction | État |
|---|---|---|
| `red-teamer-agent` | Construire scénarios d’abus, injection, confusion d’autorité, exfiltration et usage combiné d’outils puis vérifier les garde-fous. | PROCHAINE VAGUE |
| `detecter-exfiltration` | Repérer sorties anormalement riches en secrets/données sensibles ou destinations incohérentes avec la mission. | RÉSERVE CHANTIER |
| `auditer-journalisation` | Vérifier que logs prouvent ce qu’il faut sans exposer secrets, données inutiles ou informations privées. | PROCHAINE VAGUE |
| `classifier-donnees` | Public/interne/confidentiel/secret ou modèle adapté au contexte ; règles de stockage, sortie, partage et rétention associées. | RÉSERVE CHANTIER |
| `gerer-vulnerabilites-dependances` | Qualification CVE/advisory, exploitabilité réelle, dépendance transitive, version corrigée, regression et preuve de remédiation. | RÉSERVE CHANTIER |
| `modeliser-risque-abus-fraude` | Actifs, abuse cases, attaquants, incitations, signaux, faux positifs et réponse ; utile pour futurs services exposés. | VEILLE |

## J — Documentation et collaboration

| Candidat | Fonction | État |
|---|---|---|
| `maintenir-doc-api` | Documentation consommateur synchronisée au contrat public, exemples exécutables et versions supportées. | RÉSERVE CHANTIER |
| `verifier-exemples-doc` | Exécuter ou valider les snippets pour éviter une documentation syntaxiquement jolie mais morte. | PROCHAINE VAGUE |
| `gerer-style-guide` | Terminologie, structure, exemples, conventions et lint documentaire quand un corpus devient assez grand pour dériver. | RÉSERVE CHANTIER |
| `localiser-documentation` | Version source, traduction, dérive entre langues et liens partagés ; ne pas traduire une doc obsolète. | VEILLE |

---

## Raccords à épaissir plutôt que nouveaux Skills

- `gerer-decisions` : ADR, décision memo, statut, alternatives et conséquences peuvent partager la même responsabilité si les déclenchements restent nets.
- `preparer-premortem` : registre de risques et chaos sont des consommateurs du même modèle de modes d’échec, pas nécessairement de nouveaux garde-fous transversaux.
- `verifier-qualite-donnees` : profiling et traitement des manquants peuvent être des sous-routes jusqu’à ce que leur usage justifie un spécialiste.
- `gerer-release` : changelog, SemVer, evidence pack et readiness de release doivent rester liés à un vrai cycle de version.
- `traiter-retour-technique` + `conduire-incident` futur : runbook et post-incident ne doivent pas devenir une seconde chaîne de diagnostic concurrente.
- `choisir-topologie-delegation` : portfolio, capacité et file de travail ne doivent pas créer un deuxième orchestrateur des Magistri Operis.

## Priorité proposée si une vague 0.5 est ouverte

### Socle transversal
1. `auditer-fraicheur-contexte`
2. `budgeter-contexte`
3. `verifier-isolation-contextes`
4. `auditer-fraicheur-savoir`
5. `detecter-contradictions-savoir`
6. `evaluer-recherche-retrieval`
7. `verifier-liens-et-references`
8. `prioriser-travail`
9. `estimer-effort-incertitude`
10. `preparer-memo-decision`
11. `verifier-readiness`
12. `conduire-retrospective`
13. `gerer-licences`
14. `definir-metriques`
15. `gerer-environnements`
16. `detecter-derive-configuration`
17. `generer-runbook`
18. `verifier-health-readiness`
19. `tester-regression-visuelle`
20. `auditer-etats-vide-chargement-erreur`
21. `red-teamer-agent`
22. `auditer-journalisation`
23. `verifier-exemples-doc`

### Famille Affaire / Revenus à ouvrir dès que le chantier le demande
`etudier-marche` → `analyser-concurrence` → `scorer-opportunites` → `concevoir-offre` → `chiffrer-economie-unitaire` → puis, selon le canal, prix/funnel/rétention/distribution.

### Famille autonomie à ouvrir avec Noyau/Passerelle mûrs
`gerer-workflow-durable` + `gerer-annulation-et-abandon` + `gerer-escalade-humaine` côté méthode ; leurs effets locaux et la boucle des Magistri Operis restent raccordés à la branche locale et à la preuve de Noyau.

## Critère de conservation dans la Banque

Une idée future peut rester même sans besoin immédiat si :
1. elle représente une responsabilité distincte et réutilisable ;
2. un chantier plausible du Continuum peut la déclencher ;
3. elle ne duplique pas correctement une fonction existante ;
4. sa présence comme idée ne crée ni dépendance, ni coût, ni autorité fictive ;
5. sa valeur potentielle justifie de la retrouver plus tard.

Une idée est écartée lorsqu’elle n’apporte qu’un nouveau nom, impose un outil particulier sans nécessité, introduit une cérémonie sans décision utile, ou crée une capacité imaginaire.
