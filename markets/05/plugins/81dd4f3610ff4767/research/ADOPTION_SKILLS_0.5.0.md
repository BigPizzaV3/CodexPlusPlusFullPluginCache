# Adoption Skills — candidate 0.5.0

Document non normatif.

## Décision de version
Axel conserve la version 0.4.0 publiée comme version de travail avec les 92 Skills actuels. La source exacte de cette génération est conservée sur la branche `continuum-0.4.0-frozen-92`.

La branche `continuum-0.5.0-candidate` prépare la suite sans publication ni activation automatique.

## Composition
La candidate 0.5.0 ajoute 48 Skills aux 92 de la 0.4.0, soit 140 Skills source attendus.

### Passe 7 — 17 spécialistes
- `verifier-contrat-public`
- `gerer-migration-donnees`
- `gerer-feature-flags`
- `observer-systeme`
- `conduire-incident`
- `produire-retour-incident`
- `mesurer-fiabilite-service`
- `analyser-impact-changement`
- `detecter-derive-documentaire`
- `concevoir-experience`
- `auditer-provenance-logicielle`
- `auditer-permissions-capacites`
- `gerer-quotas-et-pression`
- `concevoir-sauvegarde-restauration`
- `tracer-lignee-donnees`
- `distiller-source-en-skill`
- `verifier-accessibilite`

### Passe 8 — socle transversal — 23 spécialistes
- `auditer-fraicheur-contexte`
- `budgeter-contexte`
- `verifier-isolation-contextes`
- `auditer-fraicheur-savoir`
- `detecter-contradictions-savoir`
- `evaluer-recherche-retrieval`
- `verifier-liens-et-references`
- `prioriser-travail`
- `estimer-effort-incertitude`
- `preparer-memo-decision`
- `verifier-readiness`
- `conduire-retrospective`
- `gerer-licences`
- `definir-metriques`
- `gerer-environnements`
- `detecter-derive-configuration`
- `generer-runbook`
- `verifier-health-readiness`
- `tester-regression-visuelle`
- `auditer-etats-vide-chargement-erreur`
- `red-teamer-agent`
- `auditer-journalisation`
- `verifier-exemples-doc`

### Affaire / Revenus — 5 spécialistes
- `etudier-marche`
- `analyser-concurrence`
- `scorer-opportunites`
- `concevoir-offre`
- `chiffrer-economie-unitaire`

### Autonomie méthodologique — 3 spécialistes
- `gerer-workflow-durable`
- `gerer-annulation-et-abandon`
- `gerer-escalade-humaine`

## Frontière locale
Les fonctions remises au chantier Noyau restent hors de cette adoption. La 0.5 n’invente aucune disponibilité locale et n’ajoute aucune autorité à Noyau/Passerelle.

## Réserve
Les autres fonctions de `PECHE_AUX_SKILLS_20260905_PASSE7.md` et `PECHE_AUX_SKILLS_20260905_PASSE8.md` restent des idées de Banque ou de chantier. Elles ne sont ni adoptées ni rejetées par leur simple absence de cette vague.

## Activation
Aucune publication OpenAI n’est effectuée par la préparation GitHub. Axel décidera ultérieurement s’il souhaite publier/activer cette candidate.

## Preuve attendue avant activation
1. structure du paquet cohérente ;
2. manifestes 0.5.0 concordants ;
3. 140 dossiers de Skills avec front matter valide ;
4. tests statiques adaptés à la 0.5 ;
5. import OpenAI accepté ;
6. chargement observé ;
7. tests comportementaux représentatifs, sans régression de la 0.4.

`SOURCE CANDIDATE` ≠ `VERSION ACTIVE`.
