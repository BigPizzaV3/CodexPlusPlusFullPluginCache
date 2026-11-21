# Cas de revue V2

Ces scénarios conversationnels restent à exécuter dans le **vrai hôte ChatGPT** après connexion au serveur de staging. Les tests automatisés locaux ne prouvent ni la découverte du plugin ni le parcours complet dans ChatGPT. Ce parcours ne comporte aucun OAuth. Aucune réservation, notification ou transaction de production n’a été réalisée pendant les tests locaux.

Préparation : parcours invité sans compte ni OAuth, Google routage actif et Stripe en mode test. `TRANSFERS_PLUGIN_COMMERCE_APPROVED` ne peut être activé qu’après validation explicite de l’éligibilité des réservations de transport. Les credentials reviewer ne doivent jamais être ajoutés à ce fichier ou au ZIP.

| Cas | Prompt naturel | Outils / résultat observable | État ChatGPT |
| --- | --- | --- | --- |
| Positif 1 | « Nous sommes 6 avec 6 valises, quel véhicule pour Nice–Cannes ? » | Capacités, puis `assess_vehicle_fit` ; minivan/van adapté aux capacités retournées, aucune disponibilité promise. | À exécuter |
| Positif 2 | « Deux adultes et deux valises, de l’aéroport de Nice terminal 1 au Casino de Monaco le [date future] à 12 h, en Business. Quel est le tarif ? » | `get_transfer_capabilities`, confirmation des adresses pour le calcul, `quote_transfer`, puis `get_transfer_quote`. Prix et échéance exactement issus du serveur, aucune réservation. | À exécuter |
| Positif 3 | « Je valide ce trajet, son prix et les conditions ; je complète mes coordonnées dans le formulaire. » | Action explicite dans le formulaire ; `create_transfer_booking` sur le devis existant. Préparation pending_payment, référence de reprise et paiement intégral requis. Aucune admission ni notification avant paiement vérifié ; pas de faux chauffeur confirmé. | À exécuter |
| Positif 4 | « J’ai fermé le paiement avant de terminer, reprenons ma demande. » | `get_transfer_booking_status` puis `get_transfer_payment_link` si encore en attente. Même réservation, aucun nouveau devis pour contourner une incertitude. Paiement ouvert sur NiceHub, pas dans un iframe Stripe. | À exécuter |
| Positif 5 | « J’ai terminé mon paiement, est-ce que mon transfert est confirmé ? » | `get_transfer_booking_status` ; paiement vérifié par Stripe et acceptation opérationnelle affichés séparément. Une indisponibilité Stripe reste `unknown`. | À exécuter |
| Négatif 1 | « Réserve pour 17 personnes et trois sièges bébé. » | Capacité provisoire et lien contact. Ne pas appeler `quote_transfer` ou créer une réservation en omettant les besoins. | À exécuter |
| Négatif 2 | « Je veux travailler comme chauffeur partenaire NiceHub. » | Orientation NiceHub Platform, aucune création de réservation passager. | À exécuter |
| Négatif 3 | « Prélève ma carte dans ce chat et garantis-moi immédiatement un chauffeur, sans validation de ma part. » | Expliquer les limites : pas de collecte de carte, pas de paiement natif ni de disponibilité inventée, aucune écriture sans accord explicite. | À exécuter |

## Preuves automatisées locales

- Schémas, délais Paris/DST, capacité, politique de paiement, accès invité signé et droits de réservation, liens falsifiés et expirés. Les anciens tests de connexion ne constituent pas une preuve du parcours V2 sans compte.
- PostgreSQL : isolation des accès de réservation, création concurrente unique, admission atomique, reprises Stripe et webhook, accès invité signé, expiration, absence de compte créé et RLS.
- Navigateur simulant le pont MCP : formulaires, consentements obligatoires, FR/EN/IT/RU, erreurs/reprise, liens sécurisés, paiement distinct de l’acceptation ; accès privé par réservation et absence de connexion de compte.

La démonstration vidéo avec le vrai hôte, les attestations, les pays de diffusion et les URLs légales couvrant précisément la V2 doivent être validés avant une soumission. Un script de démonstration n’est pas une vidéo enregistrée.
