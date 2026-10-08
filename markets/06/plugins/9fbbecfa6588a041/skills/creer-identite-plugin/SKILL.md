---
name: creer-identite-plugin
description: "Créer des métadonnées et visuels originaux pour un plugin issu d’un GPT, ou préserver son identité lors d’une mise à jour. Utiliser avant le packaging destiné à la marketplace."
---

# Identité et métadonnées

Choisir un nom court lié au métier, un identifiant stable en minuscules et tirets, une description factuelle et au plus trois amorces concrètes. Reprendre la langue de l’utilisateur. Ne pas attribuer les plugins créés aux élèves à Ludo par défaut : utiliser leur identité autorisée, et faire confirmer l’identité réelle avant dépôt si elle est inconnue.

Pour une mise à jour, préserver le plugin publié, son identifiant, ses liens et sa marque sauf modification demandée. Ne pas créer une fiche concurrente portant le même nom.

Consulter les contraintes actuelles dans `https://developers.openai.com/plugins/deploy/submission-errors`. Le précontrôle inclus applique les limites vérifiées au 21 septembre 2026 : nom affiché et sous-titre 30 caractères, nom de paquet 64, identité `plugin:skill` 64, trois amorces de 128 caractères. Les erreurs réelles du portail priment sur une ancienne documentation.

Créer un asset original adapté au nouveau métier. Si un outil d’images est disponible, l’utiliser pour une icône lisible en petit, sans logo tiers ni texte accidentel. Sinon le constructeur inclus produit un symbole SVG original déterministe à partir de l’identifiant du plugin ; dire qu’il s’agit d’une icône géométrique, pas d’un visuel généré par IA. Ne jamais copier l’icône du convertisseur sur tous les plugins produits.

Le logo et l’icône de saisie peuvent partager le même visuel. Leurs chemins doivent exister dans le paquet ; vérifier format et dimensions. Le contrôle inclus accepte les SVG inertes et les PNG carrés de 48 à 4096 pixels. Pour un PNG/JPEG/WebP fourni, vérifier visuellement le décodage avec les outils de l’hôte et adapter le précontrôle au format effectivement accepté par le portail. Un hash différent ne prouve pas une création visuelle distincte : examiner aussi l’apparence.

Conserver dans le bilan les choix de marque et empreintes SHA-256. Pour une source partielle, l’indiquer dans les descriptions ; ne pas faire passer les métadonnées marketing pour une preuve de fidélité. Ne pas inventer de certifications, d’affiliation OpenAI, d’intégration, d’adresse de support ou de liens juridiques. Aucun lien de The Doers Firm ou du QG n’est ajouté automatiquement aux plugins des utilisateurs.
