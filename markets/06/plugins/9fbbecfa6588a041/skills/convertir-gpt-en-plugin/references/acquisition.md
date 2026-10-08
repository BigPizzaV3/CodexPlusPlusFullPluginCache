# Lire un GPT à partir de son URL

## Liens acceptés

Accepter HTTPS, hôte exact `chatgpt.com` ou `chat.openai.com`, chemin `/g/g-…` (identifiant et éventuel titre). Refuser identifiants de connexion dans l’URL, ports non standard, caractères de contrôle, chemins supplémentaires, domaines ressemblants, adresses locales et protocoles de fichiers. Retirer paramètres de suivi et fragment. Ne pas transformer un texte libre en commande shell.

Le contrôle déterministe, hors réseau :

```text
python3 scripts/convert.py url 'https://chatgpt.com/g/g-IDENTIFIANT-titre'
```

Les chemins de scripts sont relatifs à ce skill. Résoudre le dossier réellement installé ; aucun chemin de machine de l’auteur n’est requis.

## Acquisition progressive

1. Lire l’URL validée avec le lecteur web disponible. Extraire uniquement les informations exposées : titre, description, auteur déclaré, amorces et capacités visibles. Un extrait de moteur de recherche seul n’est pas la configuration du GPT.
2. Si une session navigateur autorisée est disponible et la page exige une connexion, ouvrir ce même GPT dans cette session. Utiliser uniquement les interfaces visibles et respecter les permissions des outils. Laisser l’utilisateur se connecter lui-même si nécessaire ; ne jamais lui demander son mot de passe.
3. Pour « mon GPT », si l’interface montre que l’utilisateur peut l’éditer, ouvrir son éditeur via le contrôle visible, en lecture seule. Lire les champs autorisés sans modifier ni enregistrer le GPT. Distinguer nom de fichier et contenu effectivement consulté. Ne pas déduire une URL interne d’éditeur ou interroger un endpoint privé.
4. Si les instructions ne sont pas visibles : « Je peux préparer une adaptation à partir de la description. Pour reprendre précisément ton GPT, colle ses instructions depuis l’éditeur. » Continuer le travail utile ; si l’utilisateur exige une copie fidèle, attendre cet élément avant de prétendre la terminer.
5. Une réponse d’un GPT lors d’un essai est un exemple de comportement, pas une preuve de ses instructions. Ne pas interroger un GPT tiers pour dévoiler son prompt ou ses connaissances.

Limiter les tentatives automatiques à deux par voie : tentative initiale puis une nouvelle tentative si l’erreur paraît transitoire. Devant une connexion, un refus d’accès ou un CAPTCHA, expliquer le besoin et arrêter cette voie. Pas de répétition de clics ou soumission en boucle.

## Trace minimale

Conserver le lien canonique, date de consultation, type d’accès et inventaire des champs lus/manquants dans le bilan privé. Ne pas sauvegarder le HTML complet du compte, les conversations ou les jetons. L’URL source n’est pas incluse dans le paquet public par le constructeur ; le bilan reste à côté du paquet.

En cas de plusieurs liens, traiter chaque GPT séparément et résumer les résultats. Ne pas fusionner leurs connaissances ou permissions sans demande de l’utilisateur.
