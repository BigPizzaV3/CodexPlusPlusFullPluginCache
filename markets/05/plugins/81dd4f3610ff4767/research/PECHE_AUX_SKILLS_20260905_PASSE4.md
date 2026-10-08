# Pêche aux Skills — Passe 4 — Windows, .NET, SQLite et exploitation

Document de recherche non normatif, complément de `PECHE_AUX_SKILLS_20260905.md`.

Cette passe cible volontairement des poissons moins glamour mais très utiles au Continuum réel : Windows desktop, .NET/MSBuild, SQLite, processus, observabilité, résilience et automatisation de l'interface locale.

## Prises

### 49. Test d'interface Windows par UI Automation
- Inspiration : Microsoft `winui-ui-testing`.
- Point fort : UIA fonctionne au-delà de WinUI, notamment Win32, WPF et WinForms ; exploration pour découvrir les AutomationId puis batch scripté et répétable pour l'épreuve.
- Idée Continuum : un Skill `tester-interface-windows` pour éprouver Noyau depuis l'usage humain réel sans dépendre d'un clic manuel d'Axel : arbre UI, contrôles, états, dialogs, scénarios complets, captures et résultat pass/fail.
- État : **CANDIDAT PRIORITAIRE**.

### 50. Diagnostic .NET par artefacts natifs
- Inspirations : `dotnet/skills`, `build-perf-diagnostics`, `eval-performance`, binlogs, traces, dumps.
- Point fort : choisir le diagnostic selon la phase réellement lente ou fautive au lieu d'ajouter des flags au hasard ; binlog pour MSBuild, trace/dump/profiler selon symptôme.
- Idée Continuum : spécialiser le diagnostic .NET de Noyau : build, restore, test, runtime, allocation, exception, deadlock, crash et performance n'ont pas le même instrument.
- État : **CANDIDAT PRIORITAIRE** pour le chantier Noyau, probablement maillage de plusieurs petits Skills plutôt qu'un gros `.NET`.

### 51. Exécution de tests .NET adaptée au dépôt
- Inspiration : `dotnet/skills/run-tests`.
- Point fort : détecter project system / framework / runner / SDK puis choisir le plus petit scope de test ; ne pas remplacer le runner du dépôt par une commande générique.
- Idée Continuum : avant chaque boucle, résolution du test le plus rapide capable de fermer l'hypothèse ; suite complète seulement avant acceptation finale lorsque nécessaire.
- État : **CANDIDAT**, raccord avec boucle de feedback et TDD.

### 52. SQLite : intégrité, WAL et concurrence
- Inspiration : `sqlite-best-practices`.
- Point fort : WAL, timeouts, transactions, intégrité, backup, indexes et concurrence sont traités comme propriétés du moteur, pas comme simple « fichier SQL ».
- Idée Continuum : Skill SQLite pour Noyau afin de couvrir corruption, verrouillage, transactions concurrentes, migration, backup/restore, `PRAGMA integrity_check`, journal mode et preuves après écriture.
- État : **CANDIDAT PRIORITAIRE** si SQLite reste une dépendance de Noyau.

### 53. Cycle de vie processus / ressources
- Inspiration : revues backend/Tauri centrées sur handles, processus enfants, mutex, connexions et nettoyage.
- Idée Continuum : détecter processus orphelins, navigateurs multipliés, handles non libérés, tâches non annulées, shutdown incomplet, verrou oublié et ressources qui survivent à leur mission.
- État : **CANDIDAT PRIORITAIRE** — directement raccord aux épisodes Floorp/Brave et aux effets locaux de Noyau.

### 54. Corrélation de bout en bout
- Inspirations : `qa-observability`, `logging-observability`, Datadog Agent Observability.
- Idée Continuum : une identité de cycle/opération traverse UI → Noyau → Passerelle → MCP/API → processus ou destinataire ; logs, erreurs et états peuvent être recollés sans inférence temporelle fragile.
- État : **CANDIDAT PRIORITAIRE**.

### 55. Observabilité utilisée comme oracle de test
- Inspiration : `qa-observability`.
- Idée Continuum : un scénario peut être déclaré fonctionnel seulement si l'effet visible ET les états sous-jacents nécessaires concordent ; par exemple bouton → commande → opération identifiée → effet → retour, sans considérer le clic comme preuve.
- État : **À ÉPAISSIR** autour de `qualifier-preuve`, `tracer-execution`, `verifier-acceptation`.

### 56. Résilience : timeout, retry, backoff, circuit breaker
- Inspirations : familles de Skills `resilience`.
- Idée Continuum : distinguer échec transitoire/permanent, budget de temps, retry safe/non-safe, backoff, jitter, rate limit et circuit breaker ; raccorder systématiquement à idempotence et observation de l'effet avant rejeu.
- État : **À ÉPAISSIR** autour de `gerer-reprise` et `gerer-transactions`.

### 57. Modèle explicite de machine à états
- Inspiration : patterns state-machine/state-transition utilisés dans les Skills d'observabilité et d'orchestration.
- Idée Continuum : pour fonctions à états matérialisés (REPRISE, CREATE, reconciliation, slots, Passerelle, publication plugin), définir états autorisés, transitions, préconditions, invariants, transitions impossibles et preuve de chaque transition.
- État : **CANDIDAT PRIORITAIRE**. Peut réduire les bugs où l'interface affiche un état incohérent avec le moteur.

### 58. Épreuve de compatibilité interface ↔ backend
- Inspiration : contract enforcement + UI tests.
- Idée Continuum : vérifier qu'un bouton, label ou commande visible ne promet jamais une fonction différente de celle réellement routée ; interface, payload, handler, état et diagnostic doivent être raccordés.
- État : **CANDIDAT PRIORITAIRE**, très proche des défauts actuellement corrigés dans Réconcilier/Évaluer/Actualiser.

### 59. Desktop automation sans voler l'usage humain
- Inspiration : `computer-use` et outils Windows UIA.
- Idée Continuum : lorsque disponible, préférer une automatisation capable d'agir dans une session séparée ou via l'arbre d'accessibilité plutôt qu'une simulation souris/clavier qui prend le contrôle du poste d'Axel.
- État : **CANDIDAT**, dépend de capacité réellement disponible et prouvée.

### 60. Garde-fou « le diagnostic doit choisir son instrument »
- Synthèse des Skills Microsoft/.NET et performance.
- Idée Continuum : symptôme → phase fautive → instrument adapté → artefact → conclusion. Ne jamais lancer profiler, dump, trace, Event Viewer, logs complets ou tests exhaustifs par cérémonial.
- État : **CANDIDAT SOUS-COTÉ** ; pourrait devenir un routeur technique très efficace.

## Ce qui n'est pas retenu comme Skill autonome

- `memory-forensics` sécurité : hors besoin courant du Continuum ; trop spécialisé pour être intégré au maillage général. À rechercher à la demande si un incident réel le justifie.
- outils Datadog / SaaS : idées d'observabilité intéressantes, mais dépendances externes non retenues ; le verrou coût 0 et la confidentialité restent prioritaires.
- desktop control basé uniquement sur PyAutoGUI : capacité potentiellement utile en dernier recours, mais trop fragile et intrusive pour devenir la voie par défaut.

## Conclusion de la passe

Cette zone confirme un principe : **plus on s'approche du Réel local, plus les Skills doivent devenir spécialisés par type de preuve et par couche technique**. Un seul `traiter-retour-technique` ne doit pas connaître en profondeur MSBuild, SQLite, UIA, processus Windows, réseau, performance et state machines ; il doit savoir router vers les spécialistes réellement nécessaires.
