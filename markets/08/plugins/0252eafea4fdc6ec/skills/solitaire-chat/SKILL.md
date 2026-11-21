---
name: solitaire-chat
description: Play a Klondike solitaire game through the solitaire-chat MCP tools and interactive ChatGPT widget when the user asks to play, resume, move cards, draw, undo, or get a hint.
---

# Solitaire dans le chat

Utilise les outils MCP solitaire_* pour jouer au Klondike classique, tirage d'une carte.

- Avant de créer une partie, vérifie les résultats précédents de la conversation. Si un game_id existe déjà, ne rappelle jamais solitaire_new_game pour la même demande : appelle solitaire_resume_game avec ce game_id.
- Si aucun game_id n'est présent, appelle solitaire_new_game exactement une fois et conserve l'identifiant renvoyé. Cette réponse crée l'état et monte directement l'iframe : n'appelle aucun outil de rendu ensuite.
- solitaire_resume_game est la voie lecture seule pour reprendre une partie existante : il ne crée pas de partie et ne modifie pas l'état. Cette réponse monte directement l'iframe avec le game_id validé : n'appelle aucun outil de rendu ensuite.
- N'appelle à nouveau solitaire_new_game que si l'utilisateur demande explicitement une nouvelle donne. Ne passe jamais un game_id existant à solitaire_new_game.
- Quand un outil renvoie la ressource UI, laisse ChatGPT afficher le plateau interactif : l'utilisateur peut cliquer une carte puis sa destination, ou glisser-déposer une carte vers sa destination. Les boutons du widget couvrent aussi nouvelle partie, pioche, annulation et indice.
- Le game_id est un jeton signe qui contient l'etat de la partie; il n'est pas un identifiant a inventer ou a modifier.
- Apres chaque action qui change la partie (new_game, draw, move, undo), remplace le game_id conserve par celui renvoye dans la reponse.
- Pour reprendre une partie dans un nouveau chat, demande a l'utilisateur le dernier game_id renvoye; ne l'invente jamais.
- Appelle solitaire_get_state avant de jouer si le plateau courant n'est pas deja visible.
- Pour tirer, appelle solitaire_draw. Quand la pioche est vide, le meme outil recycle la defausse.
- Pour deplacer, appelle solitaire_move avec from, to et, pour une sequence, count. Les colonnes humaines tableau_1 a tableau_7 sont acceptees; les fondations utilisent f0 a f3 dans l'ordre pique, coeur, carreau, trefle.
- Pour conseiller sans jouer, appelle solitaire_hint; pour annuler, appelle solitaire_undo.
- Après chaque outil, résume brièvement l'action et affiche le plateau renvoyé. Ne prétends pas qu'un coup est joué si l'outil a retourné isError: true. Ne monte qu'un seul widget pour une demande de création/reprise et ne relance pas une nouvelle partie pour corriger un rendu.
- Si l'utilisateur joue depuis l'iframe, conserve le game_id renvoyé par le dernier résultat d'outil ; les clics et glisser-déposer du widget appellent directement les outils MCP et mettent à jour le plateau.
- Apres une action demandee dans le chat (draw, move, undo ou get_state/hint), conserve le game_id renvoyé et laisse le widget déjà ouvert gérer son état ; n'appelle jamais d'outil de rendu intermédiaire.

Le game_id est un secret de reprise : ne le partage pas dans une URL publique et ne le remplace pas
par un autre identifiant. Il reste autonome et ne depend pas d'un stockage de partie cote serveur.
