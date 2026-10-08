# Banque de Skills du Continuum — V1

Document de conception non normatif. Cette Banque transforme les prises de `PECHE_AUX_SKILLS_20260905*.md` en fonctions candidates cohérentes avec @Continuum.

Le nombre de Skills n'est pas une cible. Une entrée n'est admise que si elle possède une fonction distincte, un déclenchement identifiable, un raccord au maillage, une preuve attendue et n'est pas déjà correctement couverte.

## États

- `ADOPTER` : fonction suffisamment claire pour être conçue dès maintenant côté ChatGPT/Skills sans dépendre de Noyau.
- `ÉPAISSIR` : ne justifie pas un nouveau Skill ; renforcer un Skill existant.
- `LOCAL` : fonction utile mais son comportement réel dépend d'une capacité locale/Noyau ; conception possible maintenant, validation différée.
- `VEILLE` : idée intéressante mais pas assez mûre ou pas assez utile pour entrer dans le maillage maintenant.

## A — Gouvernance du maillage

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `decouvrir-skills` | Chercher régulièrement les fonctions nouvelles ou sous-cotées de l'écosystème et comparer au maillage courant. | `maintenir-specificite-continuum`, `rechercher-trianguler` | ADOPTER |
| `qualifier-skill-externe` | Vérifier source, licence, injection, scripts, permissions, réseau, secrets, dépendances, coût et supply chain avant inspiration/adoption. | `prevol-capacites`, `qualifier-preuve`, `appliquer-cout-zero` | ADOPTER |
| `evaluer-skill` | Éprouver déclenchement/non-déclenchement, avec/sans Skill, réussite, latence, tokens, variance et régression. | `auditer-alignement`, `realigner-plugin` | ADOPTER |
| `diagnostiquer-maillage` | Détecter Skills morts, collisions, descriptions trop larges, dépendances incohérentes et coûts de contexte. | `auditer-alignement` | ADOPTER |
| `concevoir-skill` | Encadrer la création d'un Skill : responsabilité étroite, triggers, raccords, interdits, preuve et tests. | `realigner-plugin`, `maintenir-specificite-continuum` | ADOPTER |

## B — Compréhension, recherche et preuve

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `modeliser-domaine` | Construire le vocabulaire et le modèle conceptuel d'un chantier pour éviter les glissements de sens. | `questionner-totalement`, `gerer-decisions` | ADOPTER |
| `verifier-affirmation-source` | Vérifier qu'une source soutient réellement l'affirmation citée, avec portée, date et contexte. | `qualifier-preuve`, `rechercher-trianguler` | ADOPTER |
| `conduire-revue-systematique` | Pour un état de l'art : définir corpus, critères d'inclusion, extraction, contradictions et lacunes. | `rechercher-trianguler`, `gerer-savoir` | ADOPTER |
| `revoir-exigences` | Auditer une demande/spécification avant construction : ambiguïtés, incompatibilités, critères d'acceptation, dépendances et cas limites. | `questionner-totalement`, `construire-plan` | ADOPTER |
| `extraire-actions-document` | Transformer un document en faits, acteurs, obligations, échéances, risques et actions sourcées. | `qualifier-preuve`, `resoudre-autorite` | ADOPTER |

## C — Diagnostic et correction technique

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `reproduire-bug` | Réduire une plainte à un scénario reproductible minimal avec attendu, observé, environnement et preuve. | `traiter-retour-technique` | ADOPTER |
| `boucler-diagnostic` | Construire d'abord le signal pass/fail le plus rapide, puis falsifier les hypothèses par instrumentation/bisection. | `traiter-retour-technique`, `qualifier-preuve` | ADOPTER |
| `cartographier-code` | Localiser fonction, appelants, dépendances et frontières avant correction. | `construire-plan` | ADOPTER |
| `auditer-architecture` | Détecter interfaces trop larges, modules trop superficiels, couplage et friction de test/navigation. | `cartographier-code`, `revoir-exigences` | ADOPTER |
| `auditer-dette-technique` | Qualifier la dette par blast radius, coût de changement et risque observables, pas par préférence esthétique. | `cartographier-code`, `qualifier-preuve` | ADOPTER |

## D — Tests et qualité logicielle

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `choisir-strategie-tests` | Choisir tests ciblés, TDD ou autre stratégie selon le comportement réellement spécifiable. | `construire-plan`, `verifier-acceptation` | ADOPTER |
| `tester-invariants` | Utiliser property-based testing lorsque des invariants exploitables existent. | `choisir-strategie-tests` | ADOPTER |
| `fiabiliser-tests` | Distinguer flake, race, timing, donnée périmée, sélecteur ou dépendance externe avant correction. | `traiter-retour-technique` | ADOPTER |
| `mesurer-performance` | Baseline répétable → profil → goulot prouvé → correction → re-mesure et budget de régression. | `qualifier-preuve`, `verifier-acceptation` | ADOPTER |
| `tester-agent-multisurface` | Éprouver un scénario sur UI/API/DB/logs/fichiers et produire PASS/FAIL/BLOCKED/ABORTED avec preuves. | `evaluer-skill`, `verifier-acceptation` | ADOPTER |

## E — Revue, production et release

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `revoir-production` | Séparer conformité au besoin et qualité technique ; findings actionnables seulement. | `verifier-acceptation`, `qualifier-preuve` | ADOPTER |
| `conduire-revue-adversariale` | Faire relire un livrable critique par un contexte indépendant du producteur pour réduire l'auto-validation. | `orchestrer-magistri`, `revoir-production` | ADOPTER |
| `boucler-revue-correction` | Chaque finding devient corrigé, réfuté avec preuve, bloqué par décision ou reste ouvert jusqu'à convergence. | `revoir-production`, `gerer-decisions` | ADOPTER |
| `gerer-git` | Isoler branche/worktree, baseline, conflits, fin de branche, nettoyage et preuve avant fusion. | `proteger-concurrence`, `gerer-transactions` | ADOPTER |
| `gerer-depreciation` | Prouver consommateurs et migration avant retrait d'une fonction. | `gerer-decisions`, `qualifier-preuve` | ADOPTER |
| `gerer-release` | Critères de succès, observation, rollback, vérification post-release et décision de poursuite. | `gerer-transactions`, `gerer-reprise`, `verifier-acceptation` | ADOPTER |
| `gerer-mise-a-jour-dependances` | Traiter une upgrade comme opération à risque : compatibilité, transitif, scripts, supply chain, tests et rollback. | `qualifier-skill-externe`, `gerer-release` | ADOPTER |

## F — Sécurité, confidentialité et pouvoir agentique

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `proteger-donnees-sensibles` | Classifier la matière sensible, minimiser les sorties, distinguer accès et partage, protéger logs/captures. | `resoudre-autorite`, `qualifier-preuve` | ADOPTER |
| `proteger-secrets` | Scanner clés, `.env`, historiques, captures, logs et artefacts avant commit/partage/publication. | `proteger-donnees-sensibles`, `gerer-git` | ADOPTER |
| `auditer-securite-agentique` | Examiner outils, MCP, fichiers, réseau, credentials, injection et excessive agency de l'agent lui-même. | `prevol-capacites`, `resoudre-autorite` | ADOPTER |
| `qualifier-sortie-non-fiable` | Traiter toute sortie externe comme donnée à qualifier, jamais comme instruction supérieure auto-exécutable. | `qualifier-preuve`, `resoudre-autorite` | ADOPTER |
| `auditer-combinaisons-capacites` | Examiner les risques créés par la combinaison de capacités individuellement acceptables. | `prevol-capacites`, `auditer-securite-agentique` | ADOPTER |
| `preparer-premortem` | Avant effet risqué, chercher modes d'échec, détecteurs, conditions d'arrêt et preuves discriminantes. | `construire-plan`, `gerer-transactions` | ADOPTER |

## G — Orchestration et Magistri Operis

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `choisir-topologie-delegation` | Choisir fan-out, pipeline, scout+worker, revue parallèle ou séquence selon dépendances et conflits. | `orchestrer-magistri` | ADOPTER |
| `construire-contexte-delegue` | Construire le contexte minimal suffisant d'une mission : objectif, sources, contraintes, décisions, frontières, preuve. | `preparer-mission-magister` | ÉPAISSIR |
| `transmettre-handoff-technique` | Remettre chemins, état, diff, décisions, preuves et tâches restantes sans créer une seconde Continuité. | `preparer-mission-magister`, `clore-mission-magister` | ADOPTER |
| `piloter-boucle-magistri` | Orchestrer lancement → retour → contrôle → mission suivante sans intervention manuelle d'Axel lorsque Noyau/Passerelle le permettent et que l'autorité est déjà acquise. | `orchestrer-magistri`, `agir-par-noyau`, `appeler-passerelle` | LOCAL |

`piloter-boucle-magistri` ne donne aucune autorité supplémentaire : il automatise seulement la circulation et la reprise des missions déjà autorisées. Son comportement réel ne pourra être déclaré acquis qu'après preuve de Noyau/Passerelle.

## H — Livrables et médias

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `verifier-document-rendu` | Produire → rendre → inspecter visuellement → corriger → rendre à nouveau lorsque la mise en page compte. | `choisir-livraison`, `verifier-acceptation` | ADOPTER |
| `traiter-pdf` | Distinguer source éditable/export, contrôler pagination, liens, images, métadonnées, accessibilité et vraie redaction. | `verifier-document-rendu` | ADOPTER |
| `traiter-tableur` | Séparer logique, recalcul, structure, valeurs et rendu visuel. | `choisir-livraison`, `verifier-acceptation` | ADOPTER |
| `traiter-presentation` | Séparer narration, structure de slide, layout, rendu, inspection et provenance. | `choisir-livraison`, `verifier-acceptation` | ADOPTER |
| `verifier-qualite-donnees` | Vérifier grain, doublons, jointures, unités, fraîcheur et valeurs manquantes avant analyse/visualisation. | `qualifier-preuve` | ADOPTER |
| `verifier-coherence-multiformat` | Contrôler valeurs, décisions, noms, dates et conclusions entre représentations humaine/machine/PDF/tableur/slides. | `verifier-acceptation` | ADOPTER |
| `comparer-documents-semantiquement` | Distinguer changement de forme, lexical et changement de sens/obligation/décision. | `qualifier-preuve`, `gerer-decisions` | ADOPTER |

## I — Navigateurs et interfaces

| Candidat | Fonction | Raccord | État |
|---|---|---|---|
| `tester-webapp` | Assertions navigateur, session/auth, snapshots après mutation, preuves visuelles/comportementales. | `verifier-acceptation`, `prevol-capacites` | ADOPTER si capacité navigateur disponible |
| `concevoir-interface-non-generique` | Cohérence produit, accessibilité et identité visuelle ; refuser le rendu IA générique. | `respecter-typographie`, `verifier-acceptation` | ADOPTER |
| `automatiser-navigateur-progressivement` | Recherche → extraction passive → interaction → navigateur visuel seulement si nécessaire. | `prevol-capacites`, `appliquer-cout-zero` | ÉPAISSIR |

## J — Branche locale / Noyau

Ces fonctions sont conservées dans la Banque mais ne sont pas considérées comme disponibles côté local avant preuve de la capacité correspondante.

| Candidat | Fonction | État |
|---|---|---|
| `tester-interface-windows` | UI Automation pour éprouver l'interface réelle sans cliquer à la place d'Axel. | LOCAL |
| `diagnostiquer-dotnet` | Router build/restore/test/runtime vers binlog, trace, dump ou profiler adapté au symptôme. | LOCAL |
| `tester-dotnet` | Choisir runner et plus petit scope de test capable de fermer l'hypothèse. | LOCAL |
| `gerer-sqlite` | Intégrité, WAL, concurrence, transactions, migration et backup/restore. | LOCAL |
| `surveiller-cycle-processus` | Détecter processus orphelins, handles, tâches non annulées et shutdown incomplet. | LOCAL |
| `correler-execution-bout-en-bout` | Propager une identité d'opération UI → Noyau → Passerelle → processus/destinataire. | LOCAL |
| `modeliser-machine-etats` | États, transitions, préconditions, invariants et transitions impossibles pour fonctions matérialisées. | LOCAL |
| `verifier-interface-backend` | Prouver que bouton, libellé, payload, handler, état et diagnostic portent la même fonction. | LOCAL |

## K — Fonctions à épaissir plutôt qu'à dupliquer

- `traiter-retour-technique` : boucle de feedback rapide et choix d'instrument de diagnostic.
- `gerer-reprise` + `gerer-transactions` : timeout, retry, backoff, jitter, rate limit, circuit breaker seulement lorsque le système réel les justifie.
- `orchestrer-magistri` : indépendance des missions, topologie et contrôle des retours.
- `choisir-livraison` : choix du média avant production.
- `verifier-acceptation` : route vers l'épreuve spécialisée du média ou de la surface.
- `auditer-alignement` : évaluation comportementale, doctor du maillage et non-régression.
- `apprendre-du-reel` : rétrospective de l'environnement et amélioration des pratiques sans conserver le bruit.
- `qualifier-preuve` : contrôle affirmation ↔ source et théorie ↔ comportement réel.

## Priorité d'adoption proposée

### Vague 1 — sûreté et qualité du plugin
1. `qualifier-skill-externe`
2. `evaluer-skill`
3. `diagnostiquer-maillage`
4. `concevoir-skill`
5. `auditer-securite-agentique`
6. `qualifier-sortie-non-fiable`
7. `auditer-combinaisons-capacites`
8. `proteger-donnees-sensibles`
9. `proteger-secrets`

### Vague 2 — qualité du travail quotidien
10. `reproduire-bug`
11. `boucler-diagnostic`
12. `revoir-exigences`
13. `verifier-affirmation-source`
14. `modeliser-domaine`
15. `revoir-production`
16. `boucler-revue-correction`
17. `choisir-topologie-delegation`
18. `transmettre-handoff-technique`

### Vague 3 — construction et livraison
19. `cartographier-code`
20. `auditer-architecture`
21. `gerer-git`
22. `choisir-strategie-tests`
23. `tester-invariants`
24. `fiabiliser-tests`
25. `mesurer-performance`
26. `gerer-release`
27. `gerer-depreciation`
28. `gerer-mise-a-jour-dependances`
29. `verifier-document-rendu`
30. `traiter-tableur`
31. `traiter-presentation`
32. `verifier-coherence-multiformat`

### Vague locale — seulement après pré-vol Noyau
- `piloter-boucle-magistri`
- `tester-interface-windows`
- `diagnostiquer-dotnet`
- `tester-dotnet`
- `gerer-sqlite`
- `surveiller-cycle-processus`
- `correler-execution-bout-en-bout`
- `modeliser-machine-etats`
- `verifier-interface-backend`

## Règle d'entrée dans le plugin

Une entrée de Banque ne devient pas un Skill du plugin parce qu'elle paraît utile. Avant adoption :

1. prouver qu'elle n'est pas déjà correctement couverte ;
2. définir son déclenchement et son non-déclenchement ;
3. définir ses raccords au graphe ;
4. vérifier sécurité, confidentialité, licence et coût 0 ;
5. écrire le Skill propre au Continuum sans copier une dépendance externe ;
6. écrire les tests de trigger, non-trigger, comportement et régression ;
7. comparer avant/après lorsque le comportement est mesurable ;
8. ne déclarer `ADOPTÉ` qu'après comportement réellement chargé et éprouvé au niveau annoncé.
