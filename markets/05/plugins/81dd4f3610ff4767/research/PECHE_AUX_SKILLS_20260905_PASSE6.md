# Pêche aux Skills — Passe 6 — artefacts, documents, données et rendu final

Document de recherche non normatif, complément du carnet principal.

Cette passe cherche les fonctions qui transforment un résultat correct en livrable réellement fini : document, tableur, PDF, présentation, visualisation, guide utilisateur ou autre artefact destiné à être utilisé hors du tchat.

## Prises

### 76. Rendu visuel obligatoire des documents
- Inspirations : Skills `doc` et `pdf` officiels OpenAI.
- Idée Continuum : pour tout artefact où la mise en page est une partie de la fonction, extraction textuelle ≠ validation. Produire → rendre → inspecter les pages → corriger → rendre à nouveau avant livraison.
- État : **CANDIDAT PRIORITAIRE** comme garde-fou de production documentaire.

### 77. PDF comme artefact de release, pas source éditable par défaut
- Inspirations : OpenAI `pdf`, `document-pdf`.
- Idée Continuum : distinguer source éditable et export final ; vérifier fidélité, liens, images, pagination, métadonnées, accessibilité et vraie redaction lorsqu'elle s'applique.
- État : **CANDIDAT DOMAINE**.

### 78. Tableur : logique, structure et rendu sont trois preuves distinctes
- Inspirations : OpenAI `spreadsheet` / `spreadsheets`.
- Idée Continuum : préserver formules/références, analyser les valeurs, puis vérifier visuellement la feuille. Une formule présente n'est pas une preuve qu'elle recalcule correctement ; une grille correcte n'est pas encore un livrable lisible.
- État : **CANDIDAT PRIORITAIRE** pour les travaux tableur.

### 79. Visualisation orientée question, pas décoration
- Inspirations : `visualize-data`, `charting`.
- Idée Continuum : sélectionner le graphique d'après la question à répondre et la forme des données ; le graphique doit porter une conclusion lisible, conserver provenance et unités, et rester accessible.
- État : **CANDIDAT DOMAINE**.

### 80. Source lineage dans les présentations
- Inspiration : `pptx-deck-context`.
- Idée Continuum : chaque métrique, citation, chiffre ou affirmation factuelle d'une présentation possède une source résoluble ; la narration et le design ne peuvent jamais rendre la provenance invisible.
- État : **CANDIDAT PRIORITAIRE** pour présentations et rapports.

### 81. Slides : message, coordonnées et rendu séparés
- Inspirations : `pptx-slide-specification`, `pptx-visual-assets`.
- Idée Continuum : narration → structure de slide → layout final → rendu → inspection. Ne pas laisser un moteur de rendu décider silencieusement de réduire, déplacer ou cacher du contenu essentiel.
- État : **CANDIDAT DOMAINE**.

### 82. Actifs visuels avec provenance et droits
- Inspiration : `pptx-visual-assets`.
- Idée Continuum : une image/icône n'entre dans un livrable que si sa fonction, sa source, ses droits et son texte alternatif éventuel sont connus ; aucune image décorative ne remplace une donnée qui doit rester éditable/lisible.
- État : **CANDIDAT**.

### 83. Guide utilisateur jugé sur accomplissement réel
- Inspiration : `reviewing-user-guide`.
- Idée Continuum : un guide est accepté si son utilisateur cible peut accomplir ses objectifs avec le produit réel sans demander à l'auteur ; étapes, libellés et captures doivent correspondre au comportement courant.
- État : **CANDIDAT SOUS-COTÉ**.

### 84. Contrôle de cohérence multi-format
- Synthèse des Skills documents/tableurs/slides.
- Idée Continuum : lorsqu'un même résultat existe en version humaine, machine, PDF, tableur ou présentation, vérifier que les valeurs, décisions, noms, dates et conclusions ne divergent pas entre représentations.
- État : **CANDIDAT PRIORITAIRE**.

### 85. Choix du média avant production
- Inspiration : séparation report/dashboard/spreadsheet/slides des plugins OpenAI.
- Idée Continuum : ne pas fabriquer le format demandé littéralement si le besoin réel impose un autre artefact sans clarifier ; inversement, ne pas imposer un dashboard ou un PDF lorsque le tchat ou un simple fichier suffit. `choisir-livraison` peut devenir le routeur vers les spécialistes de média.
- État : **À ÉPAISSIR** autour de `choisir-livraison`.

### 86. Tableau de bord = instrument de suivi, pas rapport décoratif
- Inspiration : OpenAI `build-dashboard`.
- Idée Continuum : dashboard seulement lorsque le bénéficiaire doit surveiller, comprendre ou agir de manière répétée ; définir métriques, fraîcheur, sources, seuils et états d'erreur avant le layout.
- État : **CANDIDAT DOMAINE**.

### 87. Data quality avant visualisation
- Inspiration : écosystème analytics OpenAI.
- Idée Continuum : avant de rendre une métrique, vérifier grain, doublons, jointures, unités, fraîcheur, valeurs manquantes et définitions ; une belle visualisation ne répare pas une donnée fausse.
- État : **CANDIDAT PRIORITAIRE** pour travail analytique.

### 88. Diff sémantique de documents
- Idée issue de plusieurs workflows de review/versioning.
- Idée Continuum : comparer deux versions en distinguant changement de mise en page, changement lexical et changement de sens/obligation/décision ; ne pas noyer Axel sous un diff de bruit typographique lorsque le sens est la cible.
- État : **CANDIDAT SOUS-COTÉ**.

### 89. Acceptance gate spécialisé par média
- Synthèse.
- Idée Continuum : `verifier-acceptation` reste coordinateur, puis appelle une épreuve spécialisée : document rendu, tableur recalculé, slide inspectée, interface utilisée, script exécuté, archive décompressée, etc.
- État : **À ÉPAISSIR**.

### 90. Nettoyage des intermédiaires sans perdre les sources responsables
- Inspiration : Skills officiels OpenAI qui nettoient les artefacts temporaires après vérification.
- Idée Continuum : distinguer source responsable, livrable final, preuves nécessaires et fichiers temporaires ; retirer le bruit seulement après preuve que sa fonction est reprise.
- État : **DÉJÀ COUVERT EN PRINCIPE**, à spécialiser dans les Skills de média.

## Conclusion

Cette passe confirme que `choisir-livraison` et `verifier-acceptation` ne doivent pas devenir des encyclopédies de tous les formats. Ils doivent **router vers des Skills de média spécialisés**, chargés seulement quand le résultat final l'exige. Cela renforce encore le modèle « toile plus épaisse, trajet plus court ».
