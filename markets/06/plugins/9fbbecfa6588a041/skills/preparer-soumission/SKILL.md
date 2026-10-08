---
name: preparer-soumission
description: "Préparer le dossier de soumission d’un plugin GPT vers OpenAI avec fiche publique, cas de test, notes de version et statut exact des prérequis."
---

# Dossier de soumission

Inspecter le paquet final plutôt que recopier un modèle générique. Générer `chatgpt-app-submission.json` avec l’identité du paquet, les champs de fiche, les amorces, cinq cas positifs et trois négatifs, les notes de version et les prérequis restants. Ce fichier est un dossier de travail à recopier dans le portail ; ne pas prétendre qu’il s’agit d’un format d’import officiellement accepté sans preuve.

Le helper `../convertir-gpt-en-plugin/scripts/release.py submission` vérifie la présence des champs et du nombre de cas. Les cas métier doivent être rédigés par l’agent à partir du plugin réel. Pour chaque cas : prompt, données de test non sensibles, comportement attendu, résultat attendu et exécution réelle ou non effectuée. Ne pas prétendre qu’un test est passé faute de l’avoir lancé.

Distinguer les fonctions du plugin de celles de ses futurs produits. Un convertisseur peut préparer une connexion dans un plugin généré sans fournir lui-même cette connexion. Ne déclarer des outils MCP, annotations ou schémas que s’ils existent réellement dans le paquet et la soumission.

Vérifier dans le portail les exigences applicables à Skills only : elles peuvent différer de celles de With MCP. Au 21 septembre 2026, la référence d’erreurs indique que les URL publiques sont facultatives pour un ZIP skills-only ; ne pas créer de fausses obligations en appliquant automatiquement toutes les exigences MCP. Si des URL sont fournies, elles doivent être publiques, exactes et correspondre au développeur.

L’identité de publication doit être vérifiée et correspondre à l’utilisateur ou son entreprise. La vérification d’identité, les pièces et la connexion sont accomplies par l’utilisateur lui-même. Le plugin peut ouvrir la page et expliquer l’étape ; il ne collecte pas les documents d’identité.

Présenter les pays réellement choisis pour diffusion, sans activer tous les pays par défaut. Les textes de confidentialité décrivent exactement le traitement : contenu dans l’hôte, éventuelle lecture web, fichiers de sortie, pas de collecte serveur propre si aucun serveur n’existe. Ne pas promettre une confidentialité absolue ni un accès réservé aux élèves si la fiche est publique.

Références à revérifier avant dépôt :
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors
