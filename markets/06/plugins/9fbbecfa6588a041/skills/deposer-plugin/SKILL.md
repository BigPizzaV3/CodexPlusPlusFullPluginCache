---
name: deposer-plugin
description: "Créer ou compléter un brouillon de plugin dans le portail OpenAI, charger un paquet contrôlé, traiter les erreurs visibles et suivre les scans lorsque le dépôt est demandé."
---

# Déposer le plugin demandé

Utiliser le navigateur autorisé de l’hôte, uniquement via les interfaces visibles de `https://platform.openai.com/plugins`. Ne pas appeler d’API interne, extraire un jeton ou demander une clé. Vérifier l’organisation sélectionnée et le plugin cible avant de modifier un brouillon. Une mise à jour doit viser l’identifiant publié existant.

Avant un nouveau dépôt : précontrôle réussi, ZIP final, empreinte, version, dossier de soumission et autorisation de dépôt. Si l’utilisateur a déjà demandé de préparer ou déposer ce plugin, ne pas demander une autorisation redondante pour créer son brouillon. Les confirmations sensibles imposées par l’hôte restent applicables.

1. Lire la page actuelle et chercher un brouillon correspondant avant de créer.
2. Pour un paquet sans MCP, utiliser Create plugin puis Skills only. Si la vérification d’identité bloque la création, demander à l’utilisateur de l’effectuer, poursuivre tout le travail local et conserver le point d’arrêt.
3. Suivre la documentation de téléversement du navigateur disponible. Charger uniquement le ZIP contrôlé ; aucune spécification privée ni source brute.
4. Vérifier le résultat visible : nom, identifiant, version, compétences chargées et erreurs. Ne pas confondre sélection du fichier et succès du dépôt.
5. Compléter les champs exigés avec les informations réelles du dossier, sans inventer identité, site, conditions ou intégrations.
6. Lancer les scans quand l’interface le permet. Suivre leur état avec [reprendre-publication](../reprendre-publication/SKILL.md).
7. Une erreur de paquet exige une correction locale ciblée, une nouvelle version, tous les contrôles puis un nouveau ZIP. Une erreur de droits ou de service ne se corrige pas par des changements aléatoires du contenu.

Enregistrer les preuves minimales hors du paquet : URL du brouillon observée, identifiant, version, hash, étape et statut. Ne pas sauvegarder les cookies ou captures contenant des données privées sans nécessité. La sécurité du scan OpenAI ne remplace pas le contrôle du contenu.

Quand le brouillon est complet, passer à [publier-plugin](../publier-plugin/SKILL.md). Ne pas cocher les attestations ni cliquer la soumission finale pendant la préparation du brouillon.
