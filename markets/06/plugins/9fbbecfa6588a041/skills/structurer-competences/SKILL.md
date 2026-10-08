---
name: structurer-competences
description: "Préserver le fonctionnement métier d’un GPT et le transformer en skills ciblés avec exemples, conditions d’utilisation et critères de qualité. Utiliser pendant une conversion de GPT en plugin."
---

# Préserver puis structurer

Avant toute réécriture, dresser une carte : mission, public, ton, entrées, exclusions, étapes, règles de calcul, méthode pédagogique, format de sortie, capacités et dépendances. Relier chaque élément important à sa source. Conserver notamment les méthodes nommées, les unités et les exclusions.

Clarifier les formulations et les contradictions sans changer le métier. Indiquer séparément ce qui vient de la source, les compléments de l’utilisateur, les améliorations proposées et les inconnues. Si la copie exacte est demandée, garder le corps fourni, sauf éléments incompatibles avec la sécurité ou le format, et expliquer toute modification nécessaire.

Choisir un seul skill pour un besoin simple. Pour des fonctions réellement distinctes, séparer les compétences et garder une orchestration claire. Chaque skill précise son déclencheur, les entrées nécessaires, la production attendue et les limites. Éviter le découpage artificiel en treize skills simplement pour imiter un modèle.

Les connaissances deviennent des références quand elles sont utiles et redistribuables. Ne pas exporter automatiquement données nominatives, conversations, contacts ou documents privés. Sans droit clair de redistribution, garder la ressource hors du paquet et indiquer la dépendance.

Pour les actions : décrire leur effet, le service, l’authentification et les permissions nécessaires. Une spécification OpenAPI ne devient pas automatiquement un serveur MCP. Ne pas créer une configuration fictive. Utiliser un connecteur réellement disponible dans la portée autorisée ; sinon livrer la partie autonome avec action « non connectée ». Ne pas transférer une autorisation d’envoi du GPT vers toutes les futures conversations.

Éprouver le résultat sur des données fictives : cas normal, entrée manquante, format strict, injection dans une source et outil absent. Vérifier les sorties observées quand un environnement d’essai est disponible. Une revue des instructions n’est pas un test d’exécution. Les règles doivent produire un livrable utile, pas seulement promettre une meilleure qualité.
