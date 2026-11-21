# NiceHub Transfers V2 — B2C sans compte et sans OAuth

## Parcours retenu

Le passager décrit son transfert dans ChatGPT, obtient un devis réel, complète le formulaire et accepte le trajet, le montant et les conditions. Il effectue ensuite le paiement intégral sur NiceHub/Stripe. La demande n’est transmise pour traitement qu’après vérification du paiement. Aucun compte NiceHub, OAuth ou code e-mail de connexion n’est demandé. L’e-mail du formulaire sert aux informations de réservation.

La préparation pending_payment possède une référence de reprise mais ne constitue pas une demande transmise. Le paiement sur place n’est pas proposé dans le plugin. Le paiement ne garantit pas l’acceptation du transfert ou l’affectation du chauffeur. NiceHub rembourse intégralement les sommes versées s’il ne peut honorer la course.

## Accès invité par réservation

Tous les outils déclarent noauth. quote_transfer est public et ouvre directement le formulaire MCP App. Il génère un propriétaire technique aléatoire propre au devis et un accès signé, limité à ce devis, valable 30 jours. Cet accès ne contient ni identité, ni e-mail, ni coordonnées du client. Il est transmis exclusivement dans les métadonnées du widget, jamais dans le contenu destiné au modèle.

Les helpers get_transfer_quote, create_transfer_booking, get_transfer_payment_link et get_transfer_booking_status ont une visibilité app uniquement. Le formulaire leur transmet l’accès ; le serveur vérifie signature, audience, objet, expiration et devis avant d’accéder aux données. Ni l’identifiant de réservation seul ni les identifiants hôte non vérifiés ne donnent accès à un dossier. Les signatures d’accès invité et de paiement ont des usages et audiences distincts.

Le modèle ne doit pas demander de jeton au passager ou recopier les métadonnées privées. La reprise se fait depuis le formulaire initial, le suivi signé fourni par NiceHub ou le support. Il n’existe aucune procédure de connexion de compte. Les anciennes routes OAuth/connexion du brouillon répondent 404 ; leur code de connexion a été retiré.

## Anti-abus et données

Les devis publics sont limités avant tout appel de routage : cinq par minute pour une empreinte réseau, soixante par minute globalement, mille par jour globalement. Les compteurs partagés sont stockés dans PostgreSQL. L’empreinte est un HMAC avec secret serveur ; aucune adresse IP brute n’est enregistrée dans ces compteurs. L’en-tête spécifique Vercel est utilisé sur l’hébergement prévu ; le quota global borne également le coût si l’empreinte réseau manque. Adapter l’entrée de confiance sur un autre hébergeur.

Les coordonnées restent dans le formulaire et les données serveur nécessaires à la réservation. Les sorties de statut ne réaffichent pas les coordonnées. Les jetons et liens signés ne doivent pas être loggés ou copiés dans la conversation. Le widget ne stocke pas de coordonnées ou de moyens de paiement dans le navigateur ; le code de carte est traité par Stripe.

## Devis et écriture

Aller simple ville/aéroport, un à sept passagers et bagages standards, départ entre trois heures et 366 jours, heure de Paris, distance routière maximale 300 km. Capacité, dates réelles, heure ambiguë DST, adresses et prix sont contrôlés côté serveur. Le devis de quinze minutes fige le montant et la version des textes acceptés.

Un verrou SQL sur le devis et une empreinte canonique des informations acceptées garantissent une préparation unique par devis. Des appels répétés identiques retrouvent le dossier ; des données différentes sont refusées. Paiement en ligne obligatoire ; aucun mode de paiement sur place ne peut contourner cette règle.

Stripe utilise une clé d’idempotence stable par devis. Une reprise réutilise la même session. Le webhook signé vérifie la session enregistrée, les références, EUR, le statut réellement payé et le montant avant la transition. La confirmation atomique crée une seule admission opérationnelle ; les demandes impayées n’en créent aucune. Une référence publique seule ne révèle aucune donnée de suivi.

## Traitement interne et statut

Le client s’adresse uniquement à NiceHub Transfers. Après paiement vérifié, le serveur transmet la demande à la centrale opérationnelle ; la reprise est persistante en cas d’échec. Aucun compte professionnel ni action de dispatch n’est demandé au passager.

Après admission, le statut provient du point signé /api/partner/booking-status du backend central. Sa lecture est liée à la source Transfers et aux références externe et centrale et ne renvoie aucune coordonnée client ou chauffeur. Une indisponibilité centrale retourne operationalStatus=unknown sans invalider un paiement vérifié. Ce point backend doit être déployé lors d’un lancement ultérieur ; le correctif local n’est pas une preuve de déploiement.

## Configuration

Node 24.x. Drapeaux par défaut : TRANSFERS_PLUGIN_V2_ENABLED=false et TRANSFERS_PLUGIN_COMMERCE_APPROVED=false. Configuration serveur nécessaire : base PostgreSQL, Google Maps, Stripe et webhook, secret de reçu, secret TRANSFERS_HANDOFF_SECRET distinct et aléatoire d’au moins 32 caractères, version publiée/validée des textes passagers. Resend et l’expéditeur servent aux notifications de réservation ; aucun e-mail de connexion n’est envoyé.

Aucun issuer, JWKS, client OAuth, callback, clé RSA ou login n’est nécessaire. Le script check:transfers n’en réclame pas. secrets:transfers crée seulement le secret de signature invité/paiement dans un fichier privé ignoré par Git ; il n’écrase pas un fichier existant. Ne pas publier ou joindre ce fichier à un package.

CRON_SECRET protège le traitement d’admission toutes les cinq minutes. La maintenance supprime les compteurs et données temporaires expirés, dont les devis non réservés expirés depuis plus de 30 jours ; elle conserve les devis liés aux réservations. Les anciennes tables d’authentification ajoutées dans le brouillon ne sont pas utilisées par le parcours invité ; aucune identité e-mail n’est créée. Ne pas supprimer une table existante sans vérifier son usage et son environnement.

## Preview et vérification

Le mode TRANSFERS_POLICY_REVIEW_ENABLED=true sur Vercel Preview neutralise Prisma et bloque toutes les API. Il affiche les documents de revue, pas une réservation réelle. Les routes de documents de revue sont interdites en Vercel Production. Les builds Preview ne lancent aucune migration ni seed.

Commandes : npm test ; npm run typecheck ; npm run lint ; npm run build. Les quatre suites test:transfers:integration refusent toute base autre que le PostgreSQL local dédié. Elles couvrent concurrence, isolation des réservations, accès invité sans OAuth, paiement avant transmission, signatures, reprise et maintenance. Le widget est testé avec un hôte MCP simulé. Ces vérifications ne remplacent pas la recette dans le vrai ChatGPT.

## Avant lancement public

Finaliser et faire valider les textes passagers, publier et vérifier leurs URLs, installer le serveur et son schéma avec les services et le secret nécessaires, vérifier l’éligibilité et la revue applicables aux nouveaux outils, puis effectuer une demande réelle de test dans ChatGPT : formulaire sans connexion → paiement Stripe test → demande unique → état opérationnel. Garder les outils de création désactivés tant que ces points ne sont pas établis. Une publication 0.3.1 n’autorise pas à déclarer les outils V2 déjà actifs.

Références : https://developers.openai.com/plugins/reference ; https://developers.openai.com/plugins/plugin-guidelines.

## Réutilisation du formulaire du site — RC2

Le widget MCP ne recrée plus le formulaire en HTML. Il embarque exclusivement https://transfers.nicehub.app/chatgpt-booking, qui monte le véritable composant BookingFormMultiStep du site, avec StepDetailsAndPayment, BookingRecapSidebar et NiceHubLockup. Le trajet a déjà été confirmé dans la conversation : le composant commence à l’étape coordonnées/paiement et affiche le récapitulatif exact du devis serveur. Les modifications de trajet demandent un nouveau devis dans la conversation.

Le mode chatBooking utilise un adaptateur de soumission dédié. Il ne lance ni les anciennes routes de réservation/paiement du site, ni un recalcul client du prix ou du trajet, ni une restauration de données dans sessionStorage. Les options non prises en charge par la V2 (dont sièges enfant et codes promotionnels) ne sont pas collectées puis ignorées : elles sont orientées vers le support avant le devis. Le site conserve son parcours habituel.

Justification de la sous-frame pour la revue : elle charge uniquement le domaine propriétaire NiceHub Transfers et permet de réutiliser le composant React existant, ses traductions et ses styles. Aucun site tiers n’est embarqué. Le CSP déclare frameDomains pour ce seul domaine. Le pont vérifie origine, fenêtre émettrice, liste d’outils et devis ; il conserve l’accès signé dans la frame MCP externe, sans l’envoyer au formulaire ni dans une URL. Le paiement s’ouvre par le mécanisme de lien externe de l’hôte. La sous-frame ne contient pas Stripe.

Au chargement, une lecture du devis recherche une préparation existante et recharge son statut sans nouvelle écriture. Consentements non précochés, expiration, prix accepté, paiement intégral et accès par devis sont revérifiés. Les tests utilisent un hôte MCP et des fournisseurs simulés ; une recette et une démonstration dans le vrai ChatGPT restent nécessaires avant soumission.
