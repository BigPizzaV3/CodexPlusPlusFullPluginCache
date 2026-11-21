---
name: negonest-demarrage
description: Connect, reconnect, or verify the user's personal NegoNest connection and explain the first supported step. Use for NegoNest setup, not for general negotiation advice or managing another person's account.
---

# Démarrer avec NegoNest

À l’installation ou quand la personne demande de vérifier sa connexion, établir un premier accès utile à son compte NegoNest et expliquer les droits effectivement disponibles.

La connexion vise le compte individuel NegoNest qui a autorisé OAuth. La disponibilité du plugin dans un workspace ChatGPT ne donne pas accès aux comptes NegoNest des collègues. L’offre et les règles du compte ChatGPT sont distinctes des droits du compte NegoNest. Ne pas déduire une identité, une offre ou des permissions à partir d’une carte, d’un nom de workspace ou de l’installation du plugin.

Si les outils NegoNest ne sont pas accessibles, utiliser le parcours de connexion proposé par le client. La personne s’identifie dans l’écran OAuth NegoNest et choisit elle-même les accès. Ne jamais demander de mot de passe, de code privé ou de jeton dans le chat. Si le client ne propose pas ce parcours, indiquer de retrouver le plugin dans Plugins et d’utiliser sa commande de connexion ; ne pas inventer un lien d’installation ou une connexion déjà établie.

Pour vérifier un accès après connexion, appeler `list_negotiation_templates` une seule fois. Cette vérification ne crée aucun objet et ne nécessite pas de lire une négociation privée. En cas d’expiration ou d’autorisation manquante, expliquer le retour du serveur et le parcours de reconnexion proposé ; ne pas annoncer le succès avant un résultat d’outil concluant.

Présenter brièvement le résultat : connexion vérifiée ou étape manquante ; compte individuel NegoNest autorisé ; accès attestés par le résultat, sans en inventer ; puis une prochaine action utile, par exemple choisir une trame. Ne pas afficher d’identifiant technique, de valeur privée ou de donnée de négociation inutile. Une erreur de droits NegoNest ne permet pas de déduire l’offre ChatGPT de la personne.

Avant une demande de remplissage, consulter `describe_negotiation_fields`. Respecter les accès distincts de création, de préparation privée et d’activation ; cette dernière fige la version et démarre le délai. Une modification de l’existant ou une suppression passe par une proposition et l’accord humain précis avec mot de passe récent dans NegoNest. L’envoi reste effectué par une personne. Les modèles sont des bases à relire et adapter, pas des données personnelles à inventer.

Après un accord annoncé par la personne, relire `get_confirmation_status` avec l’identifiant de la proposition déjà reçue. Annoncer un enregistrement seulement si le reçu le confirme ; `pending` ou `applying` ne signifie pas `applied`. Une fermeture de panneau ne prouve pas une révocation. Si le fournisseur refuse un appel, signaler l’échec sans annoncer d’effet ni réessayer automatiquement par un autre mode.

Terminer le démarrage sans modifier de données. Poursuivre une demande métier ensuite dans son périmètre autorisé et les outils disponibles.
