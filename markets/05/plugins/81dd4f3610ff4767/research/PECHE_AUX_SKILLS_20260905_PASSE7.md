# Pêche aux Skills — Passe 7

Date : 5 septembre 2026

Cette passe reprend après la candidate @Continuum 0.4.0. Elle ne modifie pas le paquet 0.4.0 prêt à être importé : elle alimente seulement la recherche pour une vague ultérieure.

Principe : aucune dépendance étrangère n'est installée. On pêche des mécanismes, on vérifie leur fonction, puis on décide s'ils méritent un Skill propre, l'épaississement d'un Skill existant, une branche locale ou la veille.

## Terrain ratissé

- Skills.sh : API/contrats, migrations, feature flags, SRE, incidents, contexte, ADR, documentation, supply chain, confidentialité, accessibilité, localisation, données et agents.
- Dépôts/références observés : google/mantis, OWASP Secure Agent Playbook, React, Vercel/Turborepo, wshobson/agents, borghei/claude-skills, muratcankoylan/agent-skills-for-context-engineering, magnus919/agent-skills, sylphxai/skills, JunMystery/AI-Agent-Standards, jurgendn/agent-skills, agentplugins/agent-plugins-example, riekelt/technical-writer.

## Prises solides — candidats nouveaux

| Candidat Continuum | Mécanisme pêché | Raccord probable | Classement |
|---|---|---|---|
| `verifier-contrat-public` | Traiter API HTTP, GraphQL, gRPC, SDK, CLI, événements et schémas de configuration comme des promesses consommées ; détecter tout breaking change même si les tests internes passent. | `revoir-exigences`, `choisir-strategie-tests`, `gerer-depreciation`, `verifier-acceptation` | ADOPTER |
| `gerer-migration-donnees` | Séparer schéma et backfill ; expand/contract ; locks, gros volumes, rollback/forward-fix ; migration déployée immuable ; coexistence ancien/nouveau. | `gerer-transactions`, `proteger-concurrence`, `gerer-release`, `verifier-qualite-donnees` | ADOPTER |
| `gerer-feature-flags` | Taxonomie release/ops/expérience/permission, ramp progressif, kill switch, propriétaire, expiration et dette de flags. | `gerer-release`, `resoudre-autorite`, `gerer-decisions`, `preparer-premortem` | ADOPTER |
| `observer-systeme` | Structurer logs, métriques, traces et identités de corrélation autour d'une question de preuve ; éviter la télémétrie sans décision associée. | `tracer-execution`, `qualifier-preuve`, `mesurer-performance`, `traiter-retour-technique` | ADOPTER |
| `conduire-incident` | Triage, impact, hypothèses, mitigation, communication, récupération, chronologie et preuve de retour à l'état nominal. | `traiter-retour-technique`, `gerer-reprise`, `gerer-release`, `preparer-premortem` | ADOPTER |
| `produire-retour-incident` | Après correction réellement prouvée : cause, mécanisme, blast radius, détection, correction, prévention et enseignements ; jamais écrire le post-mortem d'une hypothèse non validée. | `conduire-incident`, `apprendre-du-reel`, `gerer-savoir` | ADOPTER |
| `mesurer-fiabilite-service` | SLI/SLO, budget d'erreur, seuils, fenêtre temporelle et conditions de décision avant de déclarer un service sain ou dégradé. | `observer-systeme`, `qualifier-preuve`, `verifier-acceptation` | ADOPTER |
| `analyser-impact-changement` | Cartographier le blast radius avant modification : dépendances, consommateurs, données, interfaces et comportements touchés. | `cartographier-code`, `auditer-architecture`, `gerer-depreciation`, `construire-plan` | ADOPTER |
| `detecter-derive-documentaire` | Comparer code/contrats/configuration et docs ; distinguer drift factuel, structurel, référentiel, temporel et sémantique ; liens/ancres cassés compris. | `verifier-affirmation-source`, `gerer-release`, `revoir-production` | ADOPTER |
| `concevoir-experience` | Formuler hypothèse falsifiable, plus petite expérience discriminante, baseline équitable, métriques, confondeurs, sanity checks et règle de décision avant exécution. | `questionner-totalement`, `qualifier-preuve`, `construire-plan` | ADOPTER |
| `auditer-provenance-logicielle` | SBOM, dépendances, licences, provenance d'artefact, signatures/attestations lorsqu'elles existent et preuve de ce qui a réellement été construit. | `qualifier-skill-externe`, `gerer-mise-a-jour-dependances`, `proteger-secrets` | ADOPTER |
| `auditer-permissions-capacites` | Least privilege par capacité réelle ; distinguer lecture, mutation, destruction, réseau et accès credential ; vérifier combinaison des droits et pas seulement chaque droit isolé. | `auditer-securite-agentique`, `auditer-combinaisons-capacites`, `resoudre-autorite`, `prevol-capacites` | ADOPTER |
| `gerer-quotas-et-pression` | Rate limits, Retry-After, backoff, jitter, concurrence, backpressure, queue et abandon contrôlé ; pas de boucle de retry aveugle. | `gerer-reprise`, `gerer-transactions`, `observer-systeme` | ADOPTER |
| `concevoir-sauvegarde-restauration` | Définir quoi sauvegarder, RPO/RTO, cohérence, chiffrement, rétention et surtout preuve de restauration — une sauvegarde non restaurée n'est pas une récupération prouvée. | `gerer-reprise`, `proteger-donnees-sensibles`, `verifier-acceptation` | ADOPTER |
| `tracer-lignee-donnees` | Origine → transformations → consommateurs → fraîcheur → propriétaire ; impact d'un changement de donnée avant modification. | `verifier-qualite-donnees`, `verifier-affirmation-source`, `analyser-impact-changement` | ADOPTER |
| `distiller-source-en-skill` | Transformer une source externe utile en mécanisme Continuum : extraire responsabilité, déclencheur, invariants, anti-patterns, preuves, puis passer par qualification et conception internes. | `decouvrir-skills`, `qualifier-skill-externe`, `concevoir-skill`, `maintenir-specificite-continuum` | ADOPTER |
| `verifier-accessibilite` | Accessibilité comme critère d'usage réel séparé de l'esthétique : clavier, focus, contrastes, structure, noms accessibles et comportements essentiels. | `concevoir-interface-non-generique`, `verifier-acceptation`, `tester-webapp` | ADOPTER |

## Prises qui épaississent mieux l'existant

| Idée | Destination | Pourquoi pas un nouveau Skill pour l'instant |
|---|---|---|
| ADR / Architecture Decision Record | `gerer-decisions` + `modeliser-domaine` | Notre cycle de vie des décisions existe déjà. À enrichir avec contexte, alternatives, conséquences, statut proposé/accepté/remplacé et traçabilité vers le code lorsque matériel. |
| Compression de contexte | `construire-contexte-delegue` + `transmettre-handoff-technique` | Le bon objectif est la fidélité par tâche, pas la compression maximale. Cela renforce le contexte minimal suffisant des Magistri Operis plutôt qu'une mémoire concurrente. |
| Communication agent-agent structurée | `preparer-mission-magister` + `transmettre-handoff-technique` + branche locale Passerelle | Schémas, validation, corrélation et replay sont précieux ; le transport réel reste local. |
| Registre de risques | `preparer-premortem` + `gerer-decisions` | Le registre n'a d'intérêt que s'il reste relié à des détecteurs, propriétaires, conditions d'arrêt et décisions. |
| Evidence pack de release | `gerer-release` + `verifier-acceptation` | Épaissir la fermeture par un paquet de preuves plutôt que créer un cérémonial indépendant. |
| Fuzzing / mutation testing | `choisir-strategie-tests` + `tester-invariants` | Ce sont des stratégies de test à sélectionner selon le risque, pas une obligation universelle. |
| Changelog / Semantic Versioning | `gerer-release` + `gerer-git` | Utile quand un produit/version publique l'exige ; éviter de l'imposer aux artefacts sans cycle de version réel. |
| Monorepo / build graph | `cartographier-code` + `analyser-impact-changement` | Garder l'idée « affected only » et graphe de dépendances, sans lier Continuum à Turborepo/Nx. |

## Prises en veille

| Idée | État | Motif |
|---|---|---|
| `gerer-localisation` | VEILLE | Réel besoin futur pour interfaces/documents multilingues, mais pas assez transversal aujourd'hui pour entrer d'office. |
| `migrer-plugin-multiclient` | VEILLE | Les travaux Agent Plugins v1 montrent une vraie discipline de migration portable, mais @Continuum est actuellement distribué par le trajet OpenAI réel ; ne pas créer une compatibilité imaginaire. |
| `formaliser-systeme-distribue` | VEILLE | CAP, consensus, CRDT, réplication, causalité : domaine puissant mais à appeler seulement lorsqu'un chantier le justifie. |
| `construire-build-reproductible` | VEILLE | Très utile dès que le paquet comporte un vrai build ou des binaires ; @Continuum reste pour l'instant Skills-only. |

## Enseignements particulièrement intéressants

1. **Le contrat public dépasse l'API HTTP.** CLI, config, événements, exports SDK et schémas de données peuvent casser un consommateur tout autant qu'une route REST.
2. **Une migration sûre est un état de coexistence contrôlée.** Le mécanisme expand/contract et les fenêtres de compatibilité valent bien au-delà des bases de données.
3. **Une sauvegarde n'est pas une preuve de restauration.** Le critère utile est la récupération effectivement éprouvée.
4. **L'observabilité doit répondre à une décision.** Loguer davantage n'est pas observer mieux ; chaque signal doit pouvoir fermer ou rouvrir une hypothèse.
5. **Les feature flags ont un cycle de vie.** Sans propriétaire, expiration et suppression, un mécanisme de sûreté devient de la dette permanente.
6. **Le contexte est une ressource à optimiser par tâche terminée.** Compresser au maximum peut augmenter le coût total si l'agent doit tout relire ou reconstruit mal.
7. **La source d'un Skill est elle-même une entrée de supply chain.** La pêche doit donc produire une distillation propre au Continuum, jamais un copier-coller d'autorité étrangère.
8. **L'accessibilité est une acceptation d'usage, pas une couche cosmétique.** Elle mérite un contrôle distinct lorsque l'interface est destinée à l'humain.

## Sources observées — exemples utiles

- Google Mantis — threat modeling : trust boundaries, surfaces d'attaque, profils d'attaquant.
- OWASP Secure Agent Playbook — MCP review : transport/auth, permissions, injection, données, sandbox et supply chain.
- JunMystery / AI-Agent-Standards — database-migrations : expand/contract, backfill, locks et rollback.
- React — feature-flags : gating et coexistence de canaux.
- borghei / feature-flags-architect : cycle de vie et dette de flags.
- laurigates / configure-api-tests et thrillmade / api-contract-enforcement : contrats consommateurs et breaking changes.
- muratcankoylan / context-compression : tokens par tâche et fidélité de compression.
- borghei / doc-drift-detector : drift documentaire multi-catégories et contrôle de liens.
- jurgendn / experiment-design : expérience minimale discriminante et critères avant run.
- wshobson / deployment-pipeline-design et architecture-decision-records : rollout/rollback et cycle de décision.
- riekelt / recording-decisions : décision durable distincte du flux de discussion.
- sylphxai / skills : backup/restore, SLO, release evidence, offline conflicts, permissions, lineage, quotas et privacy comme fonctions spécialisées.
- agentplugins / migrate-agent-plugin : inventaire complet, compatibilité additive, migration réversible et test par client.

## Frontière avec la 0.4.0

La 0.4.0 prête à importer reste inchangée par cette passe. Les prises ci-dessus forment une réserve pour une prochaine vague. Elles devront repasser par la Banque avant création de Skills et ne deviennent ni adoptées ni disponibles par leur présence dans ce fichier.
