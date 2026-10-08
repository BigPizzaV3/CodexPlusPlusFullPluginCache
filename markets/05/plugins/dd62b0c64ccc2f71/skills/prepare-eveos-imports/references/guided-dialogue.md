# Dialogue guidé avec l'utilisateur

## Principe

Présenter une décision, pas une énigme technique. Analyser d'abord les fichiers, proposer une correction concrète et demander seulement l'arbitrage indispensable.

## Forme recommandée

Utiliser ce schéma :

1. **Constat simple** : ce qui a été trouvé et combien de lignes sont concernées.
2. **Impact** : ce qui se passe si rien n'est fait.
3. **Choix** : deux ou trois options maximum.
4. **Recommandation** : placer le meilleur choix en premier et le marquer clairement.

## Questions interactives

Lorsqu'un arbitrage bloque réellement le traitement et qu'un outil de question interactive est disponible, l'utiliser en priorité.

- Préférer une seule question ; ne jamais dépasser trois questions dans la même interaction.
- Proposer deux ou trois réponses mutuellement exclusives.
- Placer la recommandation en premier. Ajouter `(Recommended)` au libellé si l'outil impose cette syntaxe.
- Donner à chaque réponse une description courte de son effet ou de son compromis.
- Employer un titre très court et un identifiant stable en `snake_case` lorsque l'outil en demande un.
- Ne jamais créer manuellement une réponse `Autre` : l'interface ajoute automatiquement le champ libre correspondant.
- Réserver ce format aux décisions réelles, pas aux messages d'avancement ou aux confirmations de règles déjà établies.
- Réutiliser la décision pendant toute la mission sans redemander le même arbitrage.

Exemple de question interactive :

> J'ai trouvé 8 clés en double. Quelle correction appliquer ?
>
> 1. **Régénérer les doublons (Recommended)** — Seules les clés en conflit changent ; toutes les autres sont préservées.
> 2. **Examiner les cas** — Je prépare la liste des 8 cas avant toute modification.
> 3. **Bloquer l'import** — Aucune clé n'est modifiée et le fichier reste non publiable.

Le champ libre `Autre réponse` est fourni par l'interface. Si aucun outil interactif n'est disponible, afficher les mêmes options sous forme numérotée et ajouter `Autre réponse : ...`.

Exemple pour des clés en double :

> J'ai trouvé 8 clés utilisées plusieurs fois. Eveos a besoin d'une clé unique par conférence.
>
> - Régénérer uniquement les clés en double (recommandé) : les autres clés restent inchangées.
> - Conserver le fichier en l'état : l'import restera bloqué.
> - Examiner les 8 cas un par un : plus lent, mais utile si certaines lignes sont de vrais doublons.

Exemple pour une taxonomie :

> 12 conférences correspondent clairement à un centre d'intérêt ; 3 restent ambiguës.
>
> - Appliquer les 12 correspondances certaines et revoir seulement les 3 ambiguës (recommandé).
> - Ne compléter aucune thématique automatiquement.

Exemple pour les dates :

> Les heures ne contiennent pas de fuseau. Je vais les conserver comme heures locales de l'événement : 14:00 restera 14:00 sur place.

Ne pas demander de choisir entre GMT, UTC, offset ou timezone IANA lorsque l'intention métier est simplement « l'heure affichée sur le programme ».

## Comportements à éviter

- Poser une liste de questions avant d'avoir inspecté le fichier.
- Montrer des noms de paramètres ou des messages techniques sans traduction.
- Demander « que voulez-vous faire ? » sans proposer de solutions.
- Demander une décision pour chaque ligne lorsqu'une règle globale suffit.
- Présenter plus de trois options sans nécessité.
- Transformer une anomalie non bloquante en interruption du traitement.

## Compte rendu

Commencer par le résultat et les points nécessitant une décision. Présenter ensuite :

- les volumes traités ;
- les corrections proposées ou appliquées ;
- les éléments laissés intacts ;
- les anomalies restantes ;
- la prochaine action possible.

Réserver les détails de cellules, identifiants techniques et traces de validation à une section secondaire ou à un rapport joint.
