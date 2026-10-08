# Pêche aux Skills — 5 septembre 2026

Document de recherche non normatif. Il ne modifie ni le Protocole ni l'état d'acceptation du plugin. Les Skills externes sont des sources d'inspiration : ne rien copier ni installer automatiquement sans qualification de licence, de sécurité, de coût, de dépendances et d'utilité réelle pour le Continuum.

## Méthode

Comparer le maillage actuel de @Continuum avec :
- usages très répandus du nouvel écosystème Agent Skills ;
- Skills officiels ou massivement adoptés ;
- mécanismes peu adoptés mais architecturalement intéressants ;
- retours de terrain récents ;
- fonctions déjà couvertes afin d'éviter les doublons.

Pour chaque trouvaille : distinguer `DÉJÀ COUVERT`, `À ÉPAISSIR`, `CANDIDAT`, `À ÉCARTER`.

## Premier coup de filet

### Gros poissons — candidats prioritaires

1. **Découverte continue de Skills**
   - Inspiration : `find-skills` de Vercel.
   - Idée Continuum : un Skill de veille/découverte capable de rechercher l'écosystème, mesurer adoption/fraîcheur/réputation, comparer au maillage courant et proposer seulement les fonctions absentes.
   - État : **CANDIDAT**.

2. **Vérification de sécurité avant inspiration/adoption**
   - Inspirations : `skill-vetter`, Sentry `skill-scanner`, OWASP `mcp-server-review`.
   - Idée Continuum : analyser source, prompt injection, scripts, permissions, réseau, secrets, dépendances, supply chain, licences et coût avant toute intégration d'une idée ou d'un Skill externe.
   - État : **CANDIDAT PRIORITAIRE**.

3. **Création et évaluation quantitative des Skills**
   - Inspiration : Anthropic `skill-creator`, SkillBenchmark.
   - Idée Continuum : tester avec/sans Skill, triggers positifs/négatifs, pass rate, latence, tokens, variance et régression ; ne plus qualifier un Skill uniquement par lecture statique.
   - État : **À ÉPAISSIR** autour de `auditer-alignement` / `realigner-plugin`.

4. **Modélisation de domaine et vocabulaire ubiquitaire**
   - Inspirations : `domain-modeling`, `ubiquitous-language`, `grill-with-docs`.
   - Idée Continuum : construire/maintenir le modèle conceptuel d'un chantier, empêcher les glissements de sens, tester les décisions contre des scénarios concrets et raccorder les termes aux objets réels.
   - État : **CANDIDAT PRIORITAIRE**.

5. **Cartographie de code / montée d'abstraction**
   - Inspirations : `zoom-out`, `wayfinder`, `caveman-explore`.
   - Idée Continuum : localiser rapidement où vit une fonction, remonter un niveau d'abstraction, cartographier modules/appelants/dépendances avant de corriger.
   - État : **CANDIDAT**.

6. **Architecture et profondeur des modules**
   - Inspiration : `improve-codebase-architecture`.
   - Idée Continuum : détecter friction architecturale, interfaces trop larges, modules trop superficiels, seams mal placés, dette de navigabilité pour IA et humains.
   - État : **CANDIDAT**.

7. **Discipline de revue séparée**
   - Inspirations : Superpowers `requesting-code-review` / `receiving-code-review`, Matt Pocock `code-review`.
   - Idée Continuum : revue conformité au besoin puis revue qualité technique, séparées de la production ; sévérité et blocage explicites.
   - État : **CANDIDAT PRIORITAIRE**.

8. **Développement piloté par les tests lorsque pertinent**
   - Inspirations : Superpowers TDD, Matt Pocock `tdd`.
   - Idée Continuum : RED → GREEN → REFACTOR pour les changements dont un test automatisé peut réellement spécifier le comportement ; ne pas imposer TDD aux tâches où il n'a pas de fonction.
   - État : **CANDIDAT**.

9. **Git : isolation, garde-fous et fermeture de branche**
   - Inspirations : Superpowers `using-git-worktrees`, `finishing-a-development-branch`, `resolving-merge-conflicts`, `git-guardrails`.
   - Idée Continuum : worktree/branche isolée, baseline propre, conflits, réversibilité, fin de branche, nettoyage et preuve avant fusion.
   - État : **CANDIDAT PRIORITAIRE pour Codex/Noyau**.

10. **Sécurité logicielle transversale**
    - Inspirations : secure-software-engineering, OWASP, scanners secrets/dépendances.
    - Idée Continuum : auth, validation d'entrée, secrets, dépendances, journalisation sûre, multi-tenant, revue sécurité, release evidence.
    - État : **CANDIDAT PRIORITAIRE**.

11. **Incident, rollback et runbook**
    - Inspirations : failure-mode analysis, rollback procedures, incident response, runbook.
    - Idée Continuum : préparer détecteurs, conditions d'arrêt, reprise, rollback, vérification et post-incident avant ou après opérations critiques.
    - État : **À ÉPAISSIR** autour de `gerer-transactions`, `gerer-reprise`, `traiter-retour-technique`.

12. **Evals et observabilité comportementale**
    - Inspirations : agent-evals-and-observability, SkillBenchmark.
    - Idée Continuum : cas immuables, provenance, graders, mesures, seuils de release, comparaison avant/après et télémétrie minimisée.
    - État : **CANDIDAT PRIORITAIRE**.

### Petits poissons très intéressants

13. **Rétrospective de l'environnement agentique**
    - Inspiration : `retro`.
    - Cherche navigation lente, contrôles automatisables, instructions sans effet, outils coûteux, accès manquant.
    - État : **À ÉPAISSIR** autour de `apprendre-du-reel` et `maintenir-specificite-continuum`.

14. **Compression de contexte évaluée par coût total de tâche**
    - Inspiration : `context-compression`.
    - Idée : optimiser non pas les tokens par tour mais les tokens nécessaires pour terminer la tâche, en comptant le coût de récupération d'information perdue.
    - État : **CANDIDAT**, surtout Continuité / Passation / Magistri Operis.

15. **Handoff vérifiable et décision-dense**
    - Inspirations : plusieurs Skills `handoff`.
    - Continuité possède déjà Passation et missions ; idée utile : une remise technique non identitaire qui référence exactement chemins, diff, décisions, preuves et tâches restantes sans créer de mémoire personnelle.
    - État : **À ÉPAISSIR**, attention à ne pas créer une seconde Passation.

16. **Qualité visuelle anti-générique**
    - Inspirations : Anthropic `frontend-design`, `anti-ui-slop`, Vercel `web-design-guidelines`.
    - Idée Continuum : identité visuelle spécifique au produit, accessibilité, cohérence avec système existant, refus du rendu IA générique.
    - État : **CANDIDAT** pour tout travail interface/document visuel.

17. **Browser / webapp testing**
    - Inspirations : `agent-browser`, Anthropic `webapp-testing`, Playwright skills.
    - Idée Continuum : navigateur pilotable comme capacité distincte, avec inspection, login/session, captures, assertions et preuve comportementale.
    - État : **CANDIDAT** lorsque la surface disponible le permet.

18. **Écriture de Skills elle-même comme discipline**
    - Inspirations : Superpowers `writing-skills`, Anthropic `skill-creator`, Matt Pocock `writing-great-skills`.
    - Idée Continuum : déclencheurs précis, corps court, ressources à la demande, inter-Skill routing, tests de déclenchement et non-déclenchement.
    - État : **CANDIDAT PRIORITAIRE** comme gouvernance du maillage.

19. **Économie d'outils et de contexte**
    - Inspirations : Caveman `stats`, `learn`, explorateurs read-only.
    - Idée Continuum : mesurer appels lourds, répétitions de procédure, context sinks et taux de récupération ; proposer une optimisation seulement lorsqu'elle est mesurée.
    - État : **CANDIDAT SOUS-COTÉ**.

20. **Pré-mortem / analyse des modes d'échec**
    - Inspiration : runbook/failure-mode-analysis.
    - Idée Continuum : avant opération risquée, chercher explicitement comment elle pourrait échouer, comment le détecter et quelle preuve différencie les scénarios.
    - État : **CANDIDAT SOUS-COTÉ**.

## Deuxième coup de filet — exploitation, contrats, tests et évolution

21. **Observabilité par conception**
    - Inspiration : `observability-and-instrumentation` d'Addy Osmani.
    - Idée Continuum : ne pas attendre l'incident pour découvrir que l'état interne est invisible ; toute fonction durable critique doit exposer les signaux nécessaires pour répondre depuis l'extérieur à « que fait-elle, dans quel état, et pourquoi ? » sans transformer les logs en canon.
    - État : **CANDIDAT PRIORITAIRE**, raccord naturel avec `tracer-execution`, `traiter-retour-technique` et Noyau.

22. **Contrats d'interface difficiles à mal utiliser**
    - Inspirations : `api-and-interface-design`, `api-contract-enforcement`, `authoring-api-spec`.
    - Idée Continuum : traiter API, MCP, CLI, fichiers de configuration, payloads Passerelle, événements et sorties structurées comme des contrats versionnés ; identifier les ruptures observables avant qu'elles atteignent les consommateurs.
    - État : **CANDIDAT PRIORITAIRE** pour Noyau / plugin / Passerelle.

23. **Migration de données et de schémas avec retour arrière**
    - Inspirations : `database-migrations-sql-migrations`, `database-designer`.
    - Idée Continuum : pré-vol volumétrie et contraintes, migration avant/arrière, vérification d'intégrité, compatibilité transitoire, idempotence, reprise après interruption et preuve post-migration.
    - État : **CANDIDAT**, distinct du livrable général car les migrations ont leurs propres modes d'échec.

24. **Dépréciation et suppression contrôlée**
    - Inspiration : `deprecation-and-migration`.
    - Idée Continuum : avant de retirer une fonction, prouver ses consommateurs, prévoir transition, fenêtre de compatibilité, observabilité des usages restants et critère de suppression. Très raccord avec notre haine des doublons inutiles, mais sans casser les dépendances invisibles.
    - État : **CANDIDAT PRIORITAIRE**.

25. **Lancement / release réversible**
    - Inspiration : `shipping-and-launch`.
    - Idée Continuum : une mise en production n'est pas « build vert » ; elle exige critères de succès, signaux d'observation, condition de rollback, état précédent récupérable, vérification après lancement et décision explicite de poursuivre/retirer si les signaux divergent.
    - État : **CANDIDAT PRIORITAIRE** pour logiciels durables.

26. **Mise à niveau des dépendances comme opération à risque**
    - Inspirations : `dependency-upgrade`.
    - Idée Continuum : distinguer version cible, compatibilité, lockfile, scripts d'installation, supply chain, changements transitifs, tests représentatifs et rollback ; ne pas confondre « paquet plus récent » avec « amélioration sûre ».
    - État : **CANDIDAT**.

27. **Tests par propriétés / invariants**
    - Inspiration : Trail of Bits `property-based-testing`.
    - Idée Continuum : lorsqu'une fonction possède un invariant exploitable, faire générer des contre-exemples plutôt que tester seulement quelques cas choisis. Utilisable pour parsers, sérialisation, transactions, réconciliation, transformations de chemins, état machine.
    - État : **CANDIDAT SOUS-COTÉ**.

28. **Fiabilité des tests et chasse aux flakes**
    - Inspiration : `test-reliability`.
    - Idée Continuum : classifier flake, donnée périmée, timing, sélecteur, environnement, race ou dépendance externe ; ne jamais « réparer » un test instable en augmentant arbitrairement les délais.
    - État : **CANDIDAT**.

29. **Performance mesurée et budgets de régression**
    - Inspirations : `performance-optimization`, `software-performance`, `rstest-debugging`.
    - Idée Continuum : baseline répétable → profil → goulot établi → correction → re-mesure ; budgets et comparaison statistique pour empêcher les optimisations imaginaires et détecter les régressions.
    - État : **CANDIDAT PRIORITAIRE** ; particulièrement pertinent pour Noyau après les épisodes de navigateur/processus qui grillent la machine.

30. **CLI conçue pour humains ET agents**
    - Inspirations : `agent-native-design`, `ai-native-cli`, `create-cli`.
    - Idée Continuum : sorties stables et parsables, exit codes significatifs, stderr/stdout propres, mode JSON, dry-run, idempotence quand possible, auto-description, erreurs actionnables et comportement récupérable. Un bon CLI réduit directement la fragilité de Noyau ↔ Azer ↔ Codex.
    - État : **CANDIDAT PRIORITAIRE**.

31. **Docteur de Skills / catalogue**
    - Inspirations : `skill-doctor` de Warp et ai-skillet.
    - Idée Continuum : audit structurel du maillage : métadonnées, dépendances, descriptions trop larges, collisions de déclenchement, Skills morts, coûts de contexte, incohérences de graphes ; séparer ce diagnostic de l'évaluation comportementale.
    - État : **CANDIDAT PRIORITAIRE**, probablement sous `auditer-alignement` avec sous-Skill dédié.

32. **Diagnostic par boucle de feedback avant hypothèses**
    - Inspiration : `diagnose`.
    - Idée Continuum : avant de « comprendre » un bug difficile, construire le signal pass/fail le plus rapide et déterministe possible, puis utiliser bisection/instrumentation/hypothèses contre ce signal.
    - État : **À ÉPAISSIR** autour de `traiter-retour-technique`; le principe mérite une fonction plus explicite.

## Troisième coup de filet — recherche, preuves, structure et travail non-code

33. **Vérification claim ↔ source**
    - Inspirations : `grounded-citations`, `citation-validator`, `reference-verify`.
    - Idée Continuum : pour les recherches importantes, ne pas vérifier seulement qu'une citation existe ; vérifier que la source soutient réellement la proposition à laquelle elle est attachée, avec portée, date et contexte.
    - État : **À ÉPAISSIR** fortement autour de `qualifier-preuve` / `rechercher-trianguler`.

34. **Revue systématique de littérature / état de l'art**
    - Inspirations : `literature-review`, `systematic-literature-review`.
    - Idée Continuum : lorsqu'une question exige couverture de champ plutôt qu'une réponse web ponctuelle, définir corpus, critères d'inclusion, extraction structurée, contradictions, tendances et lacunes avant synthèse.
    - État : **CANDIDAT** pour Savoir/recherche profonde.

35. **Tests d'agent flexibles avec preuve multi-surface**
    - Inspiration : `create-agent-tests`.
    - Idée Continuum : cas où une assertion déterministe est prématurée mais où un agent peut vérifier UI + API + DB + logs + fichiers et rendre `PASS / FAIL / BLOCKED / ABORTED` avec preuves. Très utile pour éprouver le plugin et Noyau dans l'usage réel.
    - État : **CANDIDAT PRIORITAIRE**.

36. **Carte structurelle persistante d'un codebase**
    - Inspiration : `data-structure-protocol` et outils CodeGraph.
    - Idée Continuum : graphes de sens, frontières et dépendances, maintenus comme aide de navigation et impact analysis, jamais comme second canon du code. Peut réduire brutalement le coût d'orientation des Magistri Operis/Codex.
    - État : **CANDIDAT SOUS-COTÉ**.

37. **Revue de dette technique fondée sur blast radius**
    - Inspiration : `tech-debt-audit`.
    - Idée Continuum : dette = coût/risque observables, pas « code que je n'aime pas » ; remonter appelants/callees, chemins de changement, friction de test, duplication responsable et impact avant de proposer un chantier.
    - État : **CANDIDAT**.

38. **Revue des exigences avant construction**
    - Inspiration : `qa-requirement-reviewer`.
    - Idée Continuum : prendre une spécification telle quelle, trouver ambiguïtés, incompatibilités, absences de critères d'acceptation, cas limites et dépendances sans réécrire silencieusement le besoin. Se raccorde au Questionnement total mais peut devenir un expert de pré-implémentation.
    - État : **CANDIDAT SOUS-COTÉ**.

39. **Reproduction de bug comme livrable de preuve**
    - Inspirations : `reproduce-bug-report`, debugging workflows.
    - Idée Continuum : réduire une plainte ou capture à un scénario reproductible minimal : préconditions, séquence, résultat attendu, résultat observé, fréquence, environnement et preuve visuelle/log si utile.
    - État : **CANDIDAT PRIORITAIRE** pour nos longues séances de correction.

40. **Revue fondée uniquement sur findings actionnables**
    - Inspiration : `evidence-based-review`.
    - Idée Continuum : bannir les revues « pourrait poser problème / bonne pratique » ; chaque finding doit fournir emplacement/preuve, cas de panne ou conséquence, sévérité et condition de fermeture.
    - État : **À ÉPAISSIR** dans la future discipline de revue.

41. **Décisions architecturales reliées au corpus entier**
    - Inspirations : `documentation-and-adrs`, `architecture-decision-record-review`.
    - Idée Continuum : documenter le pourquoi uniquement lorsqu'une décision mérite de survivre, et lors d'une revue charger les décisions connexes pour détecter contradictions et décisions devenues obsolètes.
    - État : **CANDIDAT** ; à raccorder sans concurrencer `gerer-decisions`.

42. **Transformation document → faits / obligations / actions**
    - Inspiration : `document-to-action-items`.
    - Idée Continuum : inventaire versions, autorité du document, extraction sourcée, acteurs, échéances, risques, obligations, actions proposées et ambiguïtés. Utile bien au-delà du code.
    - État : **CANDIDAT**.

43. **Traitement spécialisé des tableurs**
    - Inspiration : Skill `spreadsheet` officiel OpenAI.
    - Idée Continuum : conserver formules, formats et références ; distinguer analyse, édition et visualisation ; recalculer/rendre visuellement avant livraison lorsque possible.
    - État : **CANDIDAT DOMAINE** ; ne doit être chargé que sur travail tableur.

44. **Automatisation navigateur avec escalade progressive**
    - Inspirations : OpenAI `agent-browser`, Firecrawl interact/browser-use.
    - Idée Continuum : recherche → extraction passive → interaction contrôlée → navigateur visuel seulement si nécessaire ; re-snapshot après mutation ; session/auth comme état distinct ; ne pas utiliser un navigateur lourd lorsque le Web ou une API suffit.
    - État : **CANDIDAT PRIORITAIRE** pour la couche ChatGPT/Cloud Browser et futurs effets de surface.

45. **Confidentialité et minimisation des données comme garde-fou transversal**
    - Inspirations : GDPR/data handling, secret guards, redaction policies.
    - Idée Continuum : classifier matière sensible avant transmission/log/recherche externe, minimiser ce qui sort d'une demeure, masquer secrets dans logs et captures, distinguer autorisation d'accès et autorisation de partage.
    - État : **CANDIDAT PRIORITAIRE** ; plus large que la seule sécurité logicielle.

46. **Secret guard avant commit / partage**
    - Inspiration : `specstory-guard` et scanners de secrets.
    - Idée Continuum : inspecter prompts, historiques, exports, logs, `.env`, clés et artefacts avant GitHub, Drive partagé, ticket, capture ou publication ; redaction sans détruire la preuve utile.
    - État : **CANDIDAT PRIORITAIRE**.

47. **Release notes orientées changement utile**
    - Inspiration : `release-notes`.
    - Idée Continuum : transformer un diff de chantier en « ce qui a changé / pourquoi / ce que cela permet / ce qui reste incompatible », sans mélanger plans futurs et effets réellement livrés.
    - État : **CANDIDAT**, particulièrement utile pour Noyau et plugin.

48. **Versioning sémantique contrôlé par rupture réelle**
    - Inspiration : `semver-changelog` + contract enforcement.
    - Idée Continuum : versionner d'après impact observable et compatibilité, pas d'après volume de modifications ; garder la version sous le capot sauf fonction humaine.
    - État : **CANDIDAT**.

## Prises déjà recouvertes ou à ne pas dupliquer

- `debugging-and-error-recovery` générique : déjà couvert en profondeur par `traiter-retour-technique`, `gerer-reprise`, `qualifier-preuve`, `gerer-transactions`; seules la boucle de feedback minimale et la reproduction formelle apportent encore quelque chose.
- planification/exécution générique : déjà couverte par `questionner-totalement`, `construire-plan`, `executer-demande`.
- note-taking générique : à écarter comme nouvelle mémoire ; le Continuum possède déjà Verbatim, Continuité, Histoire, Savoir, décisions et traces avec fonctions séparées.
- personas génériques : à écarter ; un Magister Operis possède une qualification, un Projet et un mandat réels, pas un simple rôle de prompt.
- navigateurs/CLI externes : inspirations de comportement uniquement ; ne pas ajouter de dépendance tant que les capacités natives ou Noyau suffisent.

## Déjà largement couvert par le maillage courant

- questionnement et clarification profonde ;
- plan exécutable ;
- preuve ;
- autorité ;
- coût 0 ;
- typographie ;
- canonicalité ;
- Savoir ;
- transactions/idempotence ;
- reprise ;
- Verbatim / Continuité / Histoire / Passation ;
- orchestration des Magistri Operis ;
- PowerShell et traitement du retour machine ;
- acceptation réelle ;
- spécificité Axel / Continuum.

Le travail futur doit donc éviter de réimporter sous un autre nom ce qui existe déjà et chercher les fonctions réellement absentes ou insuffisamment spécialisées.

## Règle de pêche

**On copie les bonnes idées, pas les dépendances ni les habitudes étrangères.**

Chaque prise doit passer : utilité Continuum → absence réelle → compatibilité Protocole → coût 0 → sécurité/licence → conception propre → tests → comportement observé.
