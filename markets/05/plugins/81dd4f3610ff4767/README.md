# Continuum

Source privée du **seul plugin Continuum**.

## Lignée
`continuum-0.4.0-frozen-92` conserve la source de la 0.4.0 publiée avec 92 Skills. La 0.5.0 reprend intégralement ce socle, ajoute les 48 spécialistes retenus lors de la pêche aux Skills et `piloter-android`, puis réabsorbe les 13 coordinateurs historiques utiles sous contrats modernes : **154 Skills source minimum**.

Une branche Git n’est jamais une nouvelle identité de plugin. La cible de publication reste le même `@Continuum`, mis à jour de version en version.

## Principe
Le Protocole canonique reste la méthode normative commune. Le plugin porte les fonctions exécutables du Continuum : contexte, preuve, recherche, diagnostic, qualité, sécurité, artefacts, Savoir, Continuité, Magistri Operis, Affaire, Noyau et spécialisations réellement utiles.

Une exigence durable n’a pas nécessairement son propre Skill. En revanche, aucune exigence matérielle qui distingue le Continuum d’un ChatGPT générique ne doit rester sans responsable d’implémentation, déclenchement et preuve.

## Colonne vertébrale
À l’ouverture d’un nouveau tchat : `amorcer-continuum` → `lire-protocole` → `charger-contexte-continuum` → `executer-demande` → `tenir-verbatim`.

Aux tours suivants du même tchat : `amorcer-continuum` applique l’Entrée Protocole depuis la copie de session puis route vers `charger-contexte-continuum` → `executer-demande` → `tenir-verbatim`. `lire-protocole` revient seulement lorsqu’un rechargement intégral est requis parce que la copie de session est invalidée, incomplète, indisponible ou matériellement douteuse ; sous Gardiennage, une échéance de deux heures impose la relecture au premier point sûr.

Cette chaîne ouvre un sous-graphe adapté au tour courant : **toile plus épaisse, trajet plus court**.

## Maillage 0.5.0
La 0.5.0 conserve tout le maillage 0.4 et ajoute les familles de contrats/migrations, observabilité et incidents, fraîcheur du contexte et du Savoir, sécurité/red team, accessibilité, régression visuelle, Affaire/Revenus et autonomie méthodologique. `piloter-android` complète ce maillage sans retirer un spécialiste antérieur.

Les autres prises de recherche restent dans la Banque/réserve de chantier et ne deviennent pas automatiquement des Skills. Une piste économique prometteuse devient une expérience vérifiable : bénéficiaire, valeur, livrable, moyens, canal, encaissement, coût et premier test.

## Partition Noyau / Android
`agir-par-noyau` porte la frontière des effets locaux. `piloter-android` porte la spécialisation Android. `appeler-passerelle` porte séparément le contrat de circulation des missions.

Partition autorisée :

`@Continuum` → `Noyau MCP/API local` → `relais Android maison` → `Android autorisé`.

Le paquet ne doit pas embarquer de dépendance d’exécution vers un backend SaaS, un MCP hébergé ou une API tierce. Un essai, crédit ou quota gratuit conditionnel ne devient jamais une capacité gratuite ; toute dépense reste soumise au régime du capital actif. Aucun secret, jeton, certificat privé, adresse de relais ou identifiant d’appareil ne doit entrer dans les Skills.

Tant qu’une liaison OpenAI ↔ Noyau conforme à cette partition n’est pas matériellement prouvée, l’absence de `.mcp.json`/`.app.json` distant est volontaire : ne pas déclarer disponible une capacité qui ne l’est pas.

## Bibliothèque, Savoir et Continuité
`resoudre-demeures-savoir` coordonne les demeures, la canonicalité, le miroir et le Savoir. `gerer-continuite` coordonne Continuité, Histoire, Pré-Passation, Passation et reprise. `tenir-verbatim` reste la transaction terminale correspondante.

## Sources et traçabilité
`coverage.json` relie le canon aux responsabilités. `continuum_sources.json` décrit les autres couches de contexte. `skill_graph.json` décrit le maillage. Les documents de `research/` restent non normatifs.

## États
`SOURCE` ≠ `TESTÉE` ≠ `DRAFT` ≠ `PUBLIÉE` ≠ `CHARGÉE` ≠ `MCP JOIGNABLE` ≠ `EFFET PROUVÉ`.
