---
name: reprendre-publication
description: "Reprendre un dépôt ou un scan OpenAI interrompu, diagnostiquer ses erreurs et éviter les doublons grâce aux étapes et preuves enregistrées."
---

# Reprise d’un dépôt interrompu

Lire `etat.json` dans le dossier privé de cette conversion, puis lire l’état visible du portail avant toute action. Le helper `../convertir-gpt-en-plugin/scripts/checkpoint.py` conserve identité, étape, preuves minimales et tentatives ; il ne pilote pas le navigateur et ne connaît pas l’état du serveur.

Vérifier correspondance entre paquet, version, hash et identifiant de brouillon. En mise à jour, arrêter la mutation si l’identifiant existant n’est pas confirmé. Ne pas utiliser une nouvelle fiche comme solution implicite à un problème de mise à jour.

- Upload en cours : inspecter, attendre progressivement 2, 4, 8, 15, 30 puis 60 secondes au maximum par attente. Réouvrir le même brouillon si l’affichage paraît périmé. Avant un nouveau chargement, vérifier que la tentative précédente a échoué ou n’a créé aucun brouillon.
- Scan en cours : suivre le même scan ; ne pas relancer parce que le bouton reste grisé. La documentation indique qu’un scan peut durer jusqu’à deux heures. Après une séquence de suivi raisonnable, conserver le lien et le statut en attente. Ne pas conclure « échec » au seul dépassement du temps d’observation.
- Erreur de validation : relever le message exact, corriger son fichier source, reconstruire, revérifier et charger une nouvelle version.
- Connexion, permission ou identité : demander l’action minimale à l’utilisateur et conserver les travaux terminés.

Maximum trois tentatives de récupération par étape. Un rafraîchissement de page ne constitue pas une nouvelle soumission. Le helper refuse une quatrième tentative et ne remet pas son compteur à zéro quand la page change.

Ne pas attendre indéfiniment en silence. Donner une mise à jour lorsqu’un fait change ou que l’utilisateur doit agir. Utiliser un suivi différé uniquement quand l’utilisateur le demande ou l’autorise ; sinon remettre le statut et la prochaine étape vérifiables. Ne jamais dupliquer une opération simplement parce que son résultat n’a pas été observé.

En fin de reprise, distinguer preuve actuelle et ancienne preuve. Ni un clic ni un statut désactivé ne prouvent un succès. Reprendre seulement la prochaine étape incomplète.
