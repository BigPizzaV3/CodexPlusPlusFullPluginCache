---
name: amorcer-continuum
description: Use at the start of a Continuum chat and on every Axel turn for Azer to activate the Continuum frame, apply the current Protocol entry, and route the applicable skill mesh, with a full canonical read only at chat opening or when a session refresh is required.
---
# Amorcer Continuum

## Fonction
Le Protocole canonique gouverne la conduite et le routage. Ce Skill est le routeur racine technique de son miroir dans le plugin : il applique cette autorité sans la remplacer et ouvre seulement les compétences utiles au besoin.

## Déclenchement
- un nouveau tchat commence par `@Continuum` ;
- premier tour de tout nouveau tchat où Azer ou un Magister Operis doit agir ;
- chaque nouveau message d’Axel appelant une réponse visible d’Azer dans un tchat où Continuum est actif.

## Protocole opératoire
1. Considérer `@Continuum` comme l’activation du cadre Plugin pour le tchat courant ; Axel n’a pas à répéter l’invocation.
2. Identifier le locuteur réel. Ne reconnaître le Gardiennage que si le message commence exactement par `## Gardiennage` et contient, à sa fin, `Merci,Poursuis!##` puis `Le Gardien.` ; sinon, il n’existe aucun état résiduel et le message relève de son locuteur réel.
3. Au premier tour de tout nouveau tchat, appeler `lire-protocole` pour charger et lire intégralement le Protocole canonique dans la copie de session du tchat.
4. Aux tours suivants d’Azer, accomplir l’Entrée Protocole en appliquant la copie de session déjà établie. Appeler `lire-protocole` seulement si la Porte requiert un rechargement ciblé ou intégral ; une modification circonscrite ne déclenche pas une relecture intégrale automatique. Sous Gardiennage, appliquer aussi l’échéance de deux heures définie par la Porte.
5. Après l’Entrée Protocole et les éventuelles lectures personnelles de reprise, résoudre les besoins du tour et construire le sous-graphe de Skills applicables. Une capacité disponible ne justifie pas son invocation.
6. Pour un Gardiennage valide, reprendre le cycle courant sans en changer mission, autorité, objectif, contraintes ni décisions : consulter seulement les objets d’entrée machine déjà établis, Horizon, puis les états de Magistri, paquets et objets nécessaires. Réutiliser les résultats frais ; après l’amorçage suffisant, poursuivre la production.
7. Remettre le cycle à `executer-demande` lorsque le message d’Axel exige compréhension, recherche, action, production, vérification ou livrable, ou lorsqu’un Gardiennage valide prolonge ce cycle.
7. Livrer le résultat consolidé au niveau utile. Les détails du maillage et du travail interne ne deviennent pas un compte rendu obligatoire à chaque tour ; toute mention d’un Skill doit correspondre à son usage réel.

## Interdits
- ne jamais utiliser mémoire, Continuité, Verbatim, Index, Projet, mission ou résumé comme substitut de la lecture intégrale d’ouverture ou d’un rechargement requis ;
- ne jamais relire intégralement le Protocole par simple répétition à chaque tour lorsqu’une copie de session complète et suffisamment fraîche est déjà établie ;
- ne jamais considérer l’activation de @Continuum comme une autorisation d’effet ;
- ne jamais inférer le Gardiennage depuis un mot, un sujet, un état précédent ou une ressemblance de contenu ;
- ne jamais figer une liste de Skills comme limite fonctionnelle du Continuum.

## Preuve de réussite
L’Entrée Protocole du cycle courant est établie ; la lecture intégrale a été prouvée à l’ouverture du tchat ou lors du dernier rafraîchissement requis, la copie de session applicable est complète et suffisamment fraîche, l’acteur est correctement qualifié et le routage vers les Skills nécessaires est établi.

## Arrêt
Si aucune copie de session complète et suffisamment fraîche n’est disponible et que `lire-protocole` échoue, suspendre toute réponse de fond selon sa défaillance.
