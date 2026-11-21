# Solitaire dans ChatGPT

Package du plugin ChatGPT pour jouer au Klondike classique depuis une conversation.

Le package distribué contient le manifeste portable, la configuration MCP et les Skills. Le
serveur MCP est une infrastructure HTTPS séparée, dans mcp-server/. Il fournit aussi un widget
MCP Apps pour afficher le plateau interactif dans l'iframe ChatGPT.

## Etat du package

Le serveur distant est déclaré dans `mcp.json` avec son endpoint HTTPS public et sans
authentification utilisateur. Après upload du ZIP, il faut ouvrir l'onglet MCPs, cliquer sur
Connect, valider le domaine, puis lancer le scan des outils.

## Serveur MCP

Le serveur est sans stockage de partie : chaque reponse renvoie un game_id signe contenant l'etat
de la partie. Le client doit utiliser le dernier game_id renvoye apres chaque coup. Aucun Durable
Object, KV ou base de donnees n'est necessaire.

Les instructions de deploiement et d'enregistrement se trouvent dans mcp-server/README.md.
Le widget reutilise les ressources publiques du site (`https://solitaire-en-ligne.com/style.css`
et `https://solitaire-en-ligne.com/assets/cardmeister.full.js`) pour conserver le rendu visuel
des cartes et de la marque.
Le bouton `Fermer` ferme l'UI dans ChatGPT et une partie inactive est automatiquement fermee
apres 15 minutes. Cette fermeture ne supprime pas les rendus deja inscrits dans l'historique
d'une conversation ; une nouvelle conversation permet de repartir avec un seul plateau.

## Outils

- solitaire_new_game : cree une partie et ouvre directement le widget ; appeler cet outil une seule fois.
- solitaire_resume_game : reprend une partie existante en lecture seule et ouvre directement le widget.
- solitaire_get_state : affiche la position actuelle.
- solitaire_draw : tire ou recycle la defausse.
- solitaire_move : deplace une carte ou une sequence legale.
- solitaire_undo : annule la derniere action.
- solitaire_hint : propose un coup sans le jouer.
