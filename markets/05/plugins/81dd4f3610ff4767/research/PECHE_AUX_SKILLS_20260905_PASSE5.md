# Pêche aux Skills — Passe 5 — orchestration, sécurité agentique et convergence

Document de recherche non normatif, complément du carnet principal.

Cette passe cible les mécanismes qui deviennent importants quand @Continuum cesse d'être un simple paquet de procédures et devient réellement l'orchestrateur d'Azer, des Magistri Operis, des outils et des effets locaux.

## Prises

### 61. Délégation par indépendance réelle
- Inspirations : Superpowers `dispatching-parallel-agents`, `multi-agent-orchestration`, `orchestrate`.
- Idée Continuum : paralléliser seulement lorsque les sous-missions ne partagent pas d'état mutable ni de dépendance intermédiaire ; sinon séquencer. Chaque mission reçoit contexte minimal suffisant, définition de fini et preuve attendue.
- État : **À ÉPAISSIR** autour de `orchestrer-magistri` / `preparer-mission-magister`.

### 62. L'orchestrateur garde le jugement, les exécutants produisent
- Inspiration : `orchestrating-agent-delegation`.
- Idée Continuum : Azer conserve compréhension, découpage, autorité, synthèse et validation ; un Magister Operis reçoit une mission bornée et sa production revient comme matière à vérifier, sans devenir automatiquement décision ou vérité.
- État : **DÉJÀ COUVERT EN PRINCIPE**, mais utile comme critère de test du maillage Magistri Operis.

### 63. Panel de revue adversariale à contexte propre
- Inspiration : `delegated-review-loop` et panels adversariaux.
- Idée Continuum : pour livrables critiques, séparer producteur et réviseur ; un réviseur reçoit besoin + artefact + preuves nécessaires mais pas les justifications du producteur qui pourraient biaiser sa lecture. Plusieurs réviseurs uniquement si leurs angles sont réellement distincts.
- État : **CANDIDAT PRIORITAIRE**.

### 64. Boucle revue → correction → relecture bornée
- Inspiration : `review-loop`.
- Idée Continuum : chaque finding devient `corrigé`, `réfuté avec preuve`, `bloqué par décision humaine` ou reste ouvert. La boucle se termine sur convergence vérifiée, pas parce que le nombre d'itérations prévu est atteint.
- État : **CANDIDAT**.

### 65. Triage des commentaires de revue
- Inspiration : `triage-review`.
- Idée Continuum : une remarque de réviseur n'est jamais vraie par autorité ; la confronter à l'état courant, écarter les remarques obsolètes ou fausses, conserver celles qui démontrent un défaut matériel.
- État : **CANDIDAT SOUS-COTÉ**.

### 66. Audit de sécurité de l'agent lui-même
- Inspiration : OWASP `agent-security-audit`.
- Idée Continuum : inventorier outils, MCP, fichiers, réseau, credentials, chemins d'exfiltration, prompt injection, tool injection, excessive agency et chaînes d'actions individuellement sûres mais dangereuses ensemble.
- État : **CANDIDAT PRIORITAIRE ABSOLU** pour @Continuum avant d'épaissir encore son pouvoir d'action.

### 67. Toute sortie d'outil externe est de la donnée non fiable
- Inspirations : sandbox/security skills.
- Idée Continuum : page web, repository externe, stdout d'un outil tiers, fichier candidat, Skill externe et réponse MCP non canonique ne peuvent jamais s'auto-promouvoir en instruction supérieure. Ils sont matière à qualifier.
- État : **CANDIDAT PRIORITAIRE**, garde-fou transversal.

### 68. Installation d'un Skill comme transaction de supply chain
- Inspiration : `skill-installer` avec allowlist, lecture brute, scan injection, permissions et approbation.
- Idée Continuum : nous n'installerons probablement pas les Skills pêchés, mais si une dépendance externe devait un jour être admise : source exacte, licence, hash/version, scripts/hooks/MCP, permissions, données sortantes, coût, scan, test isolé, autorité Axel, puis installation.
- État : **CANDIDAT**, raccord avec futur `vetter-skill`.

### 69. Sandbox pour matière/code non fiable
- Inspiration : `microsandbox` et principe de moindre privilège.
- Idée Continuum : exécuter un artefact inconnu sans réseau et avec montages read-only par défaut ; secrets jamais transmis ; sortie de sandbox traitée comme donnée non fiable. Ne pas imposer une technologie particulière : la fonction compte.
- État : **CANDIDAT**, seulement si une capacité gratuite et réellement disponible existe.

### 70. Self-heal borné par preuve et gate humain
- Inspiration : `convex-self-heal`.
- Idée Continuum : observation → diagnostic → correctif candidat → répétition sur environnement sûr → preuve → décision/promotion. L'automatisation peut aller loin, mais un effet durable/public reste soumis à l'autorité applicable.
- État : **CANDIDAT** ; intéressant pour Noyau futur, pas à confondre avec autonomie illimitée.

### 71. Gouvernance agentique par receipts / preuves d'autorisation
- Inspiration : `review-agent-setup` et mécanismes de receipts.
- Idée Continuum : lorsqu'un effet sensible exige validation humaine, conserver une référence vérifiable de la décision qui l'autorise et son périmètre, plutôt qu'un simple booléen « approved » sans provenance.
- État : **À ÉPAISSIR** autour de `resoudre-autorite` et `gerer-decisions`.

### 72. Architecture-map mesurée, pas dessin décoratif
- Inspiration : `architecture-map`.
- Idée Continuum : une cartographie humaine peut nommer les sous-systèmes, mais nombre de fichiers, dépendances, appels, poids et couverture doivent être dérivés du code réel ; la carte signale explicitement les fichiers non mappés pour éviter de devenir une fiction jolie.
- État : **CANDIDAT SOUS-COTÉ**.

### 73. Orchestration avec stratégie adaptée à la forme du travail
- Inspiration : `orchestrate` fondé sur des centaines de dispatchs observés.
- Idée Continuum : fan-out exploratoire, partition par domaine, pipeline séquentiel, revue parallèle, scout + worker ne sont pas des rituels fixes ; choisir la topologie selon dépendances, coût de coordination, risques de conflit et preuve finale.
- État : **À ÉPAISSIR** autour de `orchestrer-magistri`.

### 74. Contexte délégué explicitement construit
- Inspiration : Superpowers et orchestrateurs multi-agent.
- Idée Continuum : un Magister Operis non permanent ne « reçoit pas le tchat » ; Azer construit ce qu'il doit savoir : objectif, sources responsables, contraintes, décisions applicables, frontières, livrable, preuves, routes. Tout le reste reste hors mission.
- État : **DÉJÀ COUVERT / À TESTER PLUS FORTEMENT**.

### 75. Sécurité combinatoire des outils
- Inspiration : OWASP excessive agency.
- Idée Continuum : ne pas auditer seulement outil par outil. Exemple : `lire fichier privé` + `requête web` peut créer une voie d'exfiltration même si chacun est acceptable séparément. Le pré-vol doit analyser les chaînes de capacités nécessaires au plan.
- État : **CANDIDAT PRIORITAIRE**.

## Conclusion

Cette passe confirme que l'épaississement du maillage exige maintenant une **couche de sûreté agentique au même niveau que la couche de productivité**. Plus @Continuum sait faire, plus il doit savoir précisément ce qu'il ne doit pas laisser une source externe, un Magister Operis, un outil ou une combinaison de capacités décider à sa place.
