---
name: gerer-reprise
description: Use when an authorized tool, connector, service, local component, or execution is interrupted by a transient or potentially recoverable condition.
---
# Gérer les interruptions et la reprise

## Procédure
1. Qualifier le retour observé sans inventer sa cause.
2. Distinguer interruption récupérable et indisponibilité matérielle.
3. Si la reprise reste dans le même mandat, périmètre, autorité et contraintes, reprendre automatiquement depuis le dernier état réellement prouvé.
4. Ne répéter que les opérations sans effet indésirable ou protégées par `gerer-transactions`.
5. Adapter l’attente et le rythme sans boucle active inutile.
6. Cesser la reprise automatique lorsqu’elle exige une nouvelle autorité, change le périmètre, rencontre une interdiction ou ne peut plus être distinguée d’un échec durable.
7. Respecter immédiatement une suspension ou un arrêt d’Axel. Un timeout borne l’attente d’un appel, pas la durée du chantier ; ne pas en déduire l’échec ni terminer ou relancer un processus légitime sans qualifier son état.
8. Lorsqu’Azer reprend un chantier stateful, résoudre `Reprise active Azer.md` par l’Index unique : utiliser le checkpoint courant, rafraîchir seulement ses données volatiles rendues douteuses et reprendre la prochaine action utile. Maintenir ce checkpoint via `gerer-environnements` lorsque l’état change matériellement ; il reste distinct de la Continuité et du Verbatim.

## Preuve
La reprise conserve les acquis prouvés et n’introduit ni doublon ni supposition.
