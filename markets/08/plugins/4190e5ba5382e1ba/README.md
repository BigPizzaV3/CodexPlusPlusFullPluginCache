# screeningpass 4.0.0

Demandez les dernières offres de M&A en Espagne, les offres publiées depuis deux semaines ou les postes ouverts chez un employeur. Le catalogue est accessible sans compte. Les campagnes nécessitent un compte candidat, un profil autorisé et un CV.

Pour candidater par email, indiquez les offres qui vous intéressent en une demande. screeningpass recherche le contact recommandé pour chaque offre et prépare les messages. La campagne présente les destinataires, la fiabilité des adresses, les textes, la pièce jointe et les offres écartées. Si screeningpass ne trouve aucune adresse utilisable, l’offre figure parmi les offres écartées avec son motif. Décochez les emails à retirer, puis validez l’envoi depuis votre Gmail connecté. Vous pouvez aussi donner votre accord dans la conversation après la relecture. Le suivi distingue les envois confirmés, les échecs et les résultats incertains.

Chaque nouvelle recherche de contact pour une offre débite un crédit de votre compte dès son démarrage. Si la recherche échoue, le crédit est remboursé. Une recherche déjà effectuée pour la même offre est réutilisée sans nouveau débit. Les crédits disponibles déterminent combien de nouvelles recherches peuvent être lancées. La relecture indique le quota d’envoi disponible aujourd’hui. Au-delà, les emails validés partent les jours suivants.

## Fiche OpenAI

Ce paquet cible la fiche publiée `app-6a8c7c0e49e88191acbbaf7abcede485`. Sa connexion MCP est `https://www.screeningpass.fr/mcp`. Le site et l’émetteur OAuth sont sur `www.screeningpass.ai`. Les outils campagne utilisent les droits existants `contacts:prepare`, `contacts:read` et `contacts:send`.

Le composant de relecture est servi par le MCP. Le serveur 4.0 doit être déployé avant le scan et la soumission du paquet.
