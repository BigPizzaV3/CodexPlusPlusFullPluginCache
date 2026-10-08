---
name: lbrt-planner
description: Consulter, créer et modifier les voyages, itinéraires, étapes, notes, lieux enregistrés et budgets de l'utilisateur dans Le Bon Road Trip Planner.
---

# Le Bon Road Trip Planner

Utiliser ce workflow lorsqu'un utilisateur veut organiser ou modifier un voyage dans son compte Le Bon Road Trip Planner. Les instructions explicites de l'utilisateur priment sur ce guide.

## Identifier le voyage

- Pour une demande portant sur un voyage existant, commencer par `trips_list`, puis utiliser `itinerary_get` avant toute modification afin de préserver les données déjà présentes.
- Ne jamais inventer un identifiant de voyage, d'étape, de lieu, de média ou de dépense.
- Si plusieurs voyages correspondent au nom ou à la destination indiqués, demander lequel utiliser.
- Si le compte n'est pas connecté, inviter l'utilisateur à se connecter via le flux OAuth du Planner, sans lui demander de communiquer son mot de passe dans la conversation.

## Créer un voyage

- Recueillir uniquement les informations nécessaires qui manquent réellement, par exemple la destination, les dates, la durée ou le mode de transport lorsque ces éléments conditionnent l'itinéraire.
- Utiliser `trips_create` pour le voyage, puis ajouter les étapes dans l'ordre demandé.
- Pour une création ou une réorganisation de plusieurs étapes, préférer `itinerary_apply_plan` lorsque le plan complet est connu. Conserver les étapes existantes sauf demande explicite de remplacement ou de suppression.
- Pour une étape isolée, utiliser l'outil d'ajout le plus adapté aux informations fournies. Ne pas inventer d'adresses, de coordonnées, de réservations ou de montants.
- À la fin, résumer ce qui a été créé et fournir le lien du Planner renvoyé par l'outil lorsqu'il est disponible.

## Modifier un voyage

- Lire d'abord l'état actuel avec `itinerary_get`, puis appliquer la modification la plus petite possible.
- Utiliser les outils spécialisés pour les étapes, notes de planification, récits, journal, lieux enregistrés, médias et éléments de budget.
- Respecter les dates, l'ordre des étapes, le nombre de nuits, les devises et les statuts fournis par l'utilisateur.
- Après plusieurs changements d'étapes ou de transport, utiliser `steps_recalculate_distances` si un recalcul est utile.
- Confirmer le résultat en indiquant précisément les éléments modifiés, sans prétendre qu'une réservation ou un paiement externe a été effectué.

## Actions sensibles

- Avant `trips_delete`, `steps_remove`, `places_remove`, `media_remove` ou `budget_items_delete`, demander une confirmation explicite en nommant exactement l'élément qui sera supprimé.
- Avant une opération susceptible de remplacer ou de réordonner plusieurs données, expliquer brièvement son effet. Pour `itinerary_apply_plan`, ne jamais activer la suppression des étapes absentes sans demande explicite de l'utilisateur.
- Ne pas effectuer d'achat, de paiement, de réservation réelle, d'envoi de message ou de publication externe : le Planner enregistre uniquement des informations de voyage privées.

## Réponse attendue

- Répondre dans la langue de l'utilisateur.
- Être concis : résultat, éventuelle question bloquante, puis lien vers le Planner si disponible.
- Ne pas exposer les identifiants internes sauf s'ils sont nécessaires pour résoudre une ambiguïté technique.
