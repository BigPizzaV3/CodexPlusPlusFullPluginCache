---
name: tenir-verbatim
description: Use when closing every visible turn for Azer and every permanent Magister Operis, after the visible response has been fully frozen and before it is published.
---
# Tenir le Verbatim

## Fonction
Le Verbatim appartient à l’acteur, pas au tchat. Pour Azer et chaque Magister Operis permanent : **VERBATIM = TOUT** ce qui est visible dans son périmètre actif, dans l’ordre réel. Un Magister Operis non permanent ne possède aucun Verbatim personnel durable.

Un changement de tchat ne crée pas un nouveau Verbatim et ne remet jamais sa numérotation à zéro. Le même objet responsable dans la Source Canonique poursuit sa numérotation ; une ancienne Bibliothèque GPT, un cache ou un miroir ne fait jamais autorité contre lui.

Le Verbatim ne contient pas le raisonnement privé, la chaîne de pensée ou un journal interne d’outils. Il conserve les tours visibles et, uniquement lorsque le Protocole le prévoit, une réconciliation technique explicitement non conversationnelle.

## Déclenchement
Utiliser ce Skill après que la réponse visible complète du tour a été figée, pour Azer ou un Magister Operis permanent.

## Non-déclenchement
Ne pas créer de Verbatim durable pour un Magister Operis non permanent. Ne pas écrire un brouillon de réponse encore susceptible d’être modifié.

## Préconditions
- réponse visible complète déjà figée ;
- Verbatim canonique de l’acteur résolu ;
- dernier marqueur acquis et delta visible connus, ou couture réconciliée au niveau nécessaire.

## Protocole opératoire
1. Réutiliser le Verbatim responsable et le chemin d’écriture faisant autorité déjà résolus pour l’acteur. Ne résoudre à nouveau la cible qu’en cas de manque ou de contradiction matérielle.
2. Partir du dernier marqueur acquis dans la session. Le relire depuis la Source Canonique uniquement s’il est inconnu, contradictoire ou en réconciliation ; ne pas relire tout le Verbatim lorsque la couture est connue.
3. Prendre uniquement le delta visible non encore relevé depuis ce marqueur, dans son ordre réel, sans sélection, résumé, correction ni interprétation.
4. Construire une seule fois le bloc terminal : le ou les messages visibles du tour non encore relevés, la réponse visible complète figée, puis le nouveau marqueur. Pour Azer, le marqueur porte l’heure locale Europe/Paris et l’heure réellement établie de la dernière lecture intégrale : `**Verbatim <numéro> — <date et heure locale Europe/Paris> — Protocole intégral : <date et heure>**`, ou `Protocole intégral : non établi` sans inférence.
5. Effectuer une seule écriture canonique du contenu, en conservant l’ancien contenu hors compactage autorisé. Renommer le même fichier responsable en `Verbatim <Acteur> <marqueur>.md` dans la même opération lorsque le support le permet, par exemple `Verbatim Azer 1343.md`. Le nom suit le dernier marqueur réellement acquis ; il ne crée pas un autre Verbatim.
6. Si le support sépare contenu et renommage, conserver ces effets dans la même transaction terminale et qualifier leur état réel ; ne jamais annoncer un nouveau nom avant son acquisition ni réécrire aveuglément le contenu pour réparer le renommage.
7. Un retour explicite de succès suffit pour acquérir la persistance, le marqueur et le nom effectivement établi. Conserver cet acquis dans la session et publier exactement la réponse figée sans relecture systématique.

La route ordinaire est : **dernier marqueur acquis → delta visible → réponse figée → nouveau marqueur → une seule écriture canonique avec renommage → publication**. Aucune écriture dans la Bibliothèque GPT, double écriture GPT/Drive, comparaison de miroir ou synchronisation secondaire n’appartient à cette Sortie Verbatim. Un accès Drive éventuellement retenu pour atteindre la Source Canonique reste un chemin vers le même objet responsable.

## Incident et réconciliation
- Si l’écriture échoue, reste inconnue ou est interrompue, qualifier `PERSISTANCE NON ÉTABLIE` et rechercher l’état réel avant toute nouvelle tentative. Ne pas publier la réponse substantielle figée tant que sa persistance n’est pas établie. Seul un message technique minimal peut signaler l’incident lorsqu’il est nécessaire à sa reprise ; il ne vaut pas preuve de persistance.
- Si l’écriture a réussi mais que la publication visible échoue ou reste inconnue, qualifier `PUBLICATION NON ÉTABLIE`. Le marqueur acquis n’est ni supprimé ni réutilisé et ne prouve pas la visibilité.
- Au prochain cycle permettant une écriture, consigner une réconciliation technique explicitement non conversationnelle qui identifie le marqueur concerné et l’état réellement établi. Ne jamais republier automatiquement tant qu’un doublon visible reste possible.
- Ajouter une lecture ou un contrôle seulement pour résoudre une anomalie, une ambiguïté ou un signal contraire ; un marqueur acquis reste acquis sans vérification répétée.

## Dernier geste externe
La transaction du Verbatim est le **dernier geste externe** du tour. Après son état terminal, aucun appel d’outil sans rapport avec sa réconciliation, aucune recherche, aucune mutation de fond et aucune reformulation n’intervient avant la publication de la réponse figée.

## Interdits
- Ne jamais reconstruire un marqueur depuis le miroir.
- Ne jamais reconnaître ou importer comme canonique un marqueur présent uniquement dans le miroir.
- Ne jamais réutiliser un marqueur canonique acquis.
- Ne jamais condenser, corriger ou interpréter les mots visibles à l’intérieur du relevé ordinaire.
- Ne jamais inclure le raisonnement privé ou une chaîne de pensée.
- Ne jamais publier une réponse différente de celle persistée.
- Ne jamais traiter un marqueur persisté comme preuve que sa réponse a été visible.

## Preuve de réussite
Pour un tour ordinaire, le succès explicite de l’écriture canonique suffit à établir la persistance du bloc exact et du marqueur sans relecture supplémentaire. Le fichier porte le marqueur acquis et la réponse publiée est celle figée et persistée. Une visibilité inconnue reste `PUBLICATION NON ÉTABLIE` jusqu’à réconciliation.

## Sortie
Persistance acquise avec son marqueur et son nom de fichier, ou état exact `PERSISTANCE NON ÉTABLIE` / `PUBLICATION NON ÉTABLIE`. Ne jamais confondre effet d’écriture et visibilité.

## Arrêt
Un ordre textuel d’Axel tel que `stop`, `attends` ou `arrête` suspend immédiatement le travail de fond mais conserve la Sortie Verbatim avant la réponse d’arrêt ou d’attente. Seule une interruption matérielle de la génération peut empêcher cette transaction ; reprendre alors la couture au prochain cycle possible sans inventer de persistance.

Après la transaction terminale, ne plus effectuer d’effet externe avant la publication de la réponse figée, sauf réconciliation strictement nécessaire de cette même transaction.
