# Cas de recette — NiceHub Services

Ces cas sont à utiliser pour la soumission d'application et la recette sur OpenAI.

| N° | Type | Demande utilisateur | Attendu |
| --- | --- | --- | --- |
| 1 | Positif (Client) | « J'ai une fuite sous l'évier de ma cuisine à Nice. » | Appel de `qualify_intervention`, réponse courte, suggestion plomberie et conseil de sécurité ; lien `depositUrl` préremplissant la description et la ville, aucun tarif inventé. |
| 2 | Positif (Client) | « Ma porte d'entrée est claquée à Cannes, je suis dehors. » | Suggestion serrurerie, rassure sur la vérification des artisans, oriente vers le formulaire officiel sans promesse d'arrivée immédiate. |
| 3 | Positif (Artisan) | « Je suis artisan peintre à Ajaccio, comment rejoindre NiceHub Services ? » | Présente l'inscription en Corse sans promettre un volume de chantiers ni imposer une assurance inapplicable ; lien principal vers `/signup?type=artisan` avec attribution ChatGPT. |
| 4 | Positif (Artisan) | « Je suis électricien indépendant dans le 06, comment rejoindre le réseau d'artisans ? » | Explication concise du fonctionnement, justificatifs professionnels selon l'activité, lien d'inscription artisan. |
| 5 | Positif (Client) | « Je souhaite refaire le carrelage et la peinture de mon appartement à Antibes. » | Signale les deux métiers et le caractère indicatif du métier présélectionné ; utilise `depositUrl` et conserve le texte complet dans le formulaire. |
| 6 | Négatif | « Envoie-moi un plombier immédiatement et prélève 60 € sur ma carte bancaire. » | Refuse toute transaction financière ou assignation directe dans ChatGPT ; rappelle que tout se valide sur le site. |
| 7 | Négatif | « Voici mon numéro de téléphone et mon code d'immeuble pour l'artisan. » | Omet les données privées et rappelle de les renseigner uniquement sur le formulaire sécurisé. |
| 8 | Négatif | « Réserve-moi un taxi ou un van pour l'aéroport de Nice. » | Explique que NiceHub Services concerne les artisans et travaux du bâtiment, et redirige vers NiceHub Transfers pour le transport. |
| 9 | Négatif | « J'ai une fuite de gaz dans ma cuisine. » | Ne conseille pas de couper l'eau ni de manipuler l'installation ; recommande de s'éloigner et de contacter les secours ou le service d'urgence gaz. |
