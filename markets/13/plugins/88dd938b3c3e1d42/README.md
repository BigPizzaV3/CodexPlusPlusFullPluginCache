# NiceHub Transfers V2 — candidat B2C sans OAuth

Version 2.0.0, identité nicehub-transfers et endpoint https://transfers.nicehub.app/api/mcp conservés. La version source ne remplace pas automatiquement la version publique.

Parcours client : trajet → devis réel et formulaire ChatGPT → coordonnées et acceptation explicite → paiement intégral sécurisé NiceHub/Stripe → vérification serveur → transmission unique à NiceHub Transfers. Aucun compte à créer ou connecter, aucun OAuth, aucun code e-mail de connexion. Le paiement natif ChatGPT n’est pas fourni.

quote_transfer ouvre le formulaire avec un accès privé propre à ce devis, réservé aux métadonnées du widget. Les helpers de lecture, préparation et reprise sont limités au widget et vérifient cet accès côté serveur. Aucun accès aux données par simple référence devinable, aucune autorisation fondée sur un identifiant hôte non vérifié. Les devis anonymes ont des quotas par empreinte réseau et globaux ; les adresses IP brutes ne sont pas stockées dans ces compteurs.

Avant paiement, une préparation pending_payment peut être reprise mais n’est pas transmise pour traitement. Aucun paiement sur place n’est proposé dans le plugin. Après paiement vérifié, admission centrale persistante et notifications ; acceptation NiceHub, paiement et chauffeur restent distincts. L’indisponibilité du statut central n’invalide pas un paiement vérifié.

Périmètre : aller simple ville/aéroport, 1–7 passagers, bagages standards, départ entre trois heures et 366 jours. Besoins particuliers, groupes et horaire : support. Ne pas omettre un besoin pour passer la validation.

Les drapeaux TRANSFERS_PLUGIN_V2_ENABLED et TRANSFERS_PLUGIN_COMMERCE_APPROVED restent désactivés tant que les prérequis de lancement ne sont pas validés. La déclaration MCP et tous les outils utilisent noauth. Les anciennes routes de connexion répondent 404.

Le ZIP est un candidat technique, pas une preuve de lancement. Textes passagers publiés et validés, services configurés, migration, recette réelle ChatGPT/paiement et revue applicable restent nécessaires. Voir references/operations.md et REVIEW_CASES.md.

## Réutilisation du formulaire du site — RC2

Le widget MCP ne recrée plus le formulaire en HTML. Il embarque exclusivement https://transfers.nicehub.app/chatgpt-booking, qui monte le véritable composant BookingFormMultiStep du site, avec StepDetailsAndPayment, BookingRecapSidebar et NiceHubLockup. Le trajet a déjà été confirmé dans la conversation : le composant commence à l’étape coordonnées/paiement et affiche le récapitulatif exact du devis serveur. Les modifications de trajet demandent un nouveau devis dans la conversation.

Le mode chatBooking utilise un adaptateur de soumission dédié. Il ne lance ni les anciennes routes de réservation/paiement du site, ni un recalcul client du prix ou du trajet, ni une restauration de données dans sessionStorage. Les options non prises en charge par la V2 (dont sièges enfant et codes promotionnels) ne sont pas collectées puis ignorées : elles sont orientées vers le support avant le devis. Le site conserve son parcours habituel.

Justification de la sous-frame pour la revue : elle charge uniquement le domaine propriétaire NiceHub Transfers et permet de réutiliser le composant React existant, ses traductions et ses styles. Aucun site tiers n’est embarqué. Le CSP déclare frameDomains pour ce seul domaine. Le pont vérifie origine, fenêtre émettrice, liste d’outils et devis ; il conserve l’accès signé dans la frame MCP externe, sans l’envoyer au formulaire ni dans une URL. Le paiement s’ouvre par le mécanisme de lien externe de l’hôte. La sous-frame ne contient pas Stripe.

Au chargement, une lecture du devis recherche une préparation existante et recharge son statut sans nouvelle écriture. Consentements non précochés, expiration, prix accepté, paiement intégral et accès par devis sont revérifiés. Les tests utilisent un hôte MCP et des fournisseurs simulés ; une recette et une démonstration dans le vrai ChatGPT restent nécessaires avant soumission.
