# Absorption des Skills larges historiques — 0.5.0

Document non normatif de traçabilité.

## Objet
La 0.5.0 conserve le maillage spécialisé de la candidate et réabsorbe les fonctions utiles des anciens Skills larges de `main` sans réintroduire leurs conventions périmées ni créer de responsabilités canoniques concurrentes.

| Ancien Skill | Fonction utile conservée | Responsabilités modernes principales |
|---|---|---|
| `capitaliser` | durabilité, responsabilité unique, absorption avant suppression | `gerer-canonicalite`, `gerer-savoir`, `integrer-savoir`, `tenir-histoire`, `gerer-continuite` |
| `choisir-capacites` | disponibilité ≠ autorité ≠ coût, choix par preuve | `prevol-capacites`, `resoudre-autorite`, `appliquer-cout-zero`, `agir-par-noyau` |
| `comprehension-architecturale` | décomposition objectif/dépendances/branches | `amorcer-continuum`, `charger-contexte-continuum`, `executer-demande`, `construire-plan` |
| `converger` | fusion traçable, indépendance des preuves, contradictions | `qualifier-preuve`, `verifier-affirmation-source`, `gerer-decisions`, `verifier-acceptation` |
| `corriger-et-reprendre` | racine prouvée, DELTA/PRESERVE, rollback, double contrôle | `reproduire-bug`, `boucler-diagnostic`, `fiabiliser-tests`, `gerer-reprise` |
| `explorer-peut-etre` | hypothèses bornées, falsification, plus petite preuve | `questionner-totalement`, `modeliser-domaine`, `rechercher-trianguler`, `qualifier-preuve` |
| `livrer` | surface humaine fidèle au statut des preuves | `gerer-livrables`, `choisir-livraison`, spécialistes d’artefacts |
| `orchestrer-missions` | mission corrélée, idempotence, état incertain | `orchestrer-magistri`, `transmettre-handoff-technique`, `appeler-passerelle`, `gerer-transactions` |
| `passation` | reprise/émission de continuité | `executer-pre-passation`, `executer-passation`, `reprendre-passation`, `gerer-continuite` |
| `prelever-verbatim` | ancien point d’entrée | compatibilité vers l’unique responsable `tenir-verbatim` |
| `produire-commandes` | bloc exécutable borné, runtime réel, preuve d’effet | `executer-powershell`, `agir-par-noyau`, `piloter-android`, `prouver-resultat` |
| `prouver-resultat` | claims décomposés, niveaux d’état, fraîcheur, absence bornée | `qualifier-preuve`, `verifier-affirmation-source`, `verifier-acceptation` |
| `retrouver-savoir` | Livre avant recherche externe, fraîcheur et lacunes | `resoudre-demeures-savoir`, `gerer-savoir`, `evaluer-recherche-retrieval` |
| `gerer-canonicalite` | responsabilité par fonction, concurrence, absorption | conservé et renforcé directement |

## Conventions volontairement non restaurées
Les anciennes prescriptions qui imposaient une architecture historique particulière, un nombre fixe de règles, une écriture Verbatim concurrente, une topologie locale figée ou des chemins/IDs mémorisés ne sont pas réintroduites.

## Résultat cible
Le plugin conserve les **141 Skills** de la 0.5.0 + Android et réintroduit **13 coordinateurs de compatibilité**, soit **154 Skills source minimum**, tout en maintenant une responsabilité moderne unique pour chaque effet canonique ou local.
