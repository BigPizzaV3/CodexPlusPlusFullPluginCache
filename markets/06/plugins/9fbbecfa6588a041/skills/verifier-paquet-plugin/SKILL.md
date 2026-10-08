---
name: verifier-paquet-plugin
description: "Contrôler un plugin issu d’une conversion GPT, ses assets, skills, métadonnées et ZIP avant partage ou dépôt. Produire un registre des erreurs et une archive vérifiable."
---

# Validation avant dépôt

Utiliser les scripts de `../convertir-gpt-en-plugin/scripts/` : `convert.py` assemble les skills ; `release.py preflight` contrôle les contraintes de dépôt ; `release.py package` produit le ZIP final et ses empreintes. Lire [packaging.md](../convertir-gpt-en-plugin/references/packaging.md) pour les arguments.

Faire les contrôles après les derniers changements, puis examiner la liste exacte de fichiers du ZIP. Les bilans privés, sources brutes, états de session, secrets, fichiers de compte, métadonnées macOS et données personnelles restent hors du paquet. Les scripts signalent certains secrets, jamais toutes les données sensibles : relire aussi les contenus.

Le ZIP doit contenir `.codex-plugin/plugin.json` à sa racine, tous les skills et les ressources déclarées, sans dossier englobant. Vérifier noms, versions, frontmatter, descriptions, prompts, images, liens internes et taille. Les scripts inclus ciblent le chemin skills-only : ne pas supprimer silencieusement un MCP ou une app pour faire passer l’audit. Pour ces paquets, utiliser le workflow complet de l’hôte et la soumission With MCP.

Si un validateur officiel est disponible, l’exécuter en plus du précontrôle autonome. Découvrir son chemin dans l’environnement ; ne pas supposer celui de l’auteur. En son absence, nommer le contrôle local effectué sans prétendre avoir exécuté le validateur officiel.

Pour chaque problème, noter champ/fichier, cause constatée, correction et résultat du contrôle. Ne pas réessayer un paquet inchangé contre une erreur inchangée. Une fois les contrôles passés, produire le ZIP et un bilan avec hash, version, tests exécutés et dépendances restantes.

Ne pas déduire de la validation structurelle que l’agent respecte toutes les consignes. Exécuter des essais métier et expliquer les limites des tests. La validation ne vaut ni scan OpenAI réussi, ni publication.
