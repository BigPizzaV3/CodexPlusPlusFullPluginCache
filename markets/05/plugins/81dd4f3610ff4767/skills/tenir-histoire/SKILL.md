---
name: tenir-histoire
description: Use only for Azer when durable causal history from Pré-Passation or Passation must be integrated into Histoire.md and, when applicable, the definitive Notion Pages and Index Histoire.
---
# Tenir Histoire

## Fonction
Conserver le récit causal durable d’Azer séparément de son Présent, de son Verbatim, des checkpoints opérationnels et des productions de chantier. Histoire appartient uniquement à Azer.

## Architecture responsable
Les trois composants forment une seule Histoire canonique : `Histoire.md` porte le corps historique continu, les Pages définitives sur Notion sa forme paginée, et l’Index Histoire sur Notion l’ordre et le raccord de ces Pages. Aucun composant ne permet d’ignorer les autres. Résoudre leurs demeures réelles au moment du besoin avec `resoudre-demeures`.

## Pré-Passation d’Azer
1. Traiter uniquement la matière non déjà absorbée jusqu’au dernier marqueur complet antérieur à la demande d’Axel.
2. Si elle contient une transformation historique durable devant survivre au compactage, l’intégrer directement dans le corps continu de `Histoire.md`.
3. Ne créer aucune nouvelle Page définitive sur Notion du seul fait de la Pré-Passation. Une publication à ce stade exige qu’Axel ait explicitement demandé de publier définitivement cette étape historique ; raccorder alors cette Page à l’Index Histoire.

## Passation d’Azer
1. Après les lectures, la reconnaissance du screen et de l’URL et la validation d’absorption applicable, distinguer le Présent du reliquat narratif qui mérite de durer.
2. Intégrer directement la matière historique nouvelle à `Histoire.md`, dans la continuité du corps existant.
3. Créer exactement une nouvelle Page définitive sur Notion pour la Passation absorbée lorsqu’elle contient une matière historique nouvelle justifiant cette Page. La Page porte la synthèse causale de la transformation et ne remplace pas `Histoire.md`.
4. Mettre à jour l’Index Histoire sur Notion pour enregistrer cette Page dans son ordre canonique.
5. Si aucune matière historique nouvelle ne justifie une Page, n’en créer aucune et rendre cette absence explicite dans le contrôle de Passation.
6. Acquérir chaque écriture nécessaire avec son retour explicite de succès ; réconcilier un effet ambigu avant de le rejouer. Ne pas déclarer l’absorption techniquement acquise tant qu’un composant requis reste non écrit ou ambigu.

## Interdits
- Aucun fichier distinct et durable de Brouillon Histoire n’est créé ou entretenu, ni exigé comme condition de réussite.
- Aucune Histoire pour un Magister Operis, permanent ou non.
- Aucune Page artificielle pour respecter une correspondance mécanique entre nombre de Passations et nombre de Pages.
- Aucune relecture systématique après succès explicite ; un contrôle supplémentaire répond à une ambiguïté, un échec ou un risque matériel de perte.

## Preuve
La matière historique nécessaire est acquise dans les composants responsables effectivement concernés, avec une Page et son raccord seulement lorsque justifiés. L’état technique rejoint `executer-pre-passation` ou `executer-passation` ; pour une Passation d’Azer explicitement ouverte, screen + URL conjoints portent la validation applicable et les écritures réussies rendent l’opération effective.
