# Règles de création HTML pour Systeme.io

Ces règles sont obligatoires pour toute création, modification ou correction de page.

## 1. Protéger le contenu

Utiliser le dernier contenu validé comme source de vérité.

Lorsqu’il existe plusieurs versions, identifier laquelle est la version actuelle avant de coder.

Une ancienne page peut servir de référence pour sa direction artistique, ses assets ou certains contenus uniquement lorsque leur réutilisation est autorisée.

Ne jamais :

- réintroduire un ancien texte devenu obsolète ;
- modifier silencieusement un texte validé ;
- inventer ou compléter une promesse, un résultat, un chiffre, un témoignage, un nom, un prix ou une URL ;
- reconstruire un témoignage de mémoire ;
- inventer une photo, une vidéo ou un asset présenté comme réel.

Une adaptation purement typographique peut répartir différemment une phrase sans changer son sens ni supprimer d’information.

Les suggestions de copywriting ou d’allègement doivent être distinguées des modifications réellement appliquées.

## 2. URLs et ressources

Chaque `href`, `src`, `poster` et URL CSS doit provenir de la cliente ou d’une source explicitement autorisée.

Ne jamais utiliser silencieusement :

- `#` ;
- `javascript:void(0)` ;
- un domaine d’exemple ;
- une fausse URL ;
- un faux asset.

Avant la version finale, vérifier que toutes les URL indispensables sont disponibles.

Un asset facultatif absent peut être retiré avec l’accord de la cliente au lieu de bloquer toute la page.

Les images informatives ont un `alt` utile. Les images purement décoratives utilisent `alt=""`.

Conserver le ratio et la qualité utile des images. Utiliser `object-fit: cover` uniquement lorsqu’un recadrage est intentionnel.

## 3. Direction artistique

Respecter la direction artistique validée pendant le workflow.

Construire avant le code un système visuel cohérent :

- palette ;
- typographies ;
- hiérarchie ;
- largeurs de contenu ;
- échelle d’espacement ;
- boutons ;
- rayons ;
- bordures ;
- ombres ;
- familles de compositions.

Traduire les valeurs récurrentes en variables CSS sous le conteneur racine.

Ne jamais remplacer silencieusement une couleur, une police ou un invariant de marque au nom d’une amélioration esthétique.

Le langage de formes validé doit rester cohérent : carré, légèrement arrondi ou franchement arrondi autour de 10 %.

Cette intention ne signifie pas que tous les composants doivent recevoir exactement la même valeur CSS.

## 4. Composition éditoriale

Créer une vraie mise en page éditoriale.

Ne pas transformer automatiquement :

- chaque liste en checklist ;
- chaque sous-titre en carte ;
- chaque séparateur en section indépendante ;
- chaque phrase forte en manifeste ;
- chaque ensemble comparable en grille.

Réserver les cartes aux éléments réellement comparables.

Éviter :

- la succession de petites cartes ;
- les interfaces ressemblant à un dashboard SaaS ;
- l’alternance mécanique des fonds ;
- les compositions identiques répétées ;
- le texte majoritairement centré ;
- les CTA répétés après chaque section sans justification.

Les paragraphes longs, récits, explications, objections et listes restent généralement alignés à gauche.

Les listes longues doivent être entièrement alignées à gauche.

Lorsqu’un ensemble contient uniquement des notions courtes et comparables, une grille de vignettes peut être utilisée si elle améliore la lecture.

Dans ce cas :

- centrer le texte dans les vignettes ;
- utiliser un fond suffisamment contrasté ;
- conserver des dimensions et espacements cohérents ;
- utiliser éventuellement de petites icônes linéaires monochromes en SVG intégré ou CSS lorsque leur sens est évident.

Ne jamais utiliser d’emojis décoratifs, de pictogrammes multicolores ou d’icônes SaaS génériques.

Les ornements CSS ou SVG intégrés sont autorisés lorsqu’ils guident réellement la lecture et restent cohérents avec la direction artistique.

## 5. Typographie

Conserver une excellente lisibilité.

Repères :

- corps d’environ 17 à 19 px sur ordinateur ;
- minimum 16 px pour le corps sur mobile ;
- largeur de lecture confortable d’environ 65 à 75 caractères ;
- interlignage confortable pour les paragraphes ;
- interlignage plus resserré pour les grands titres ;
- `clamp()` lorsque pertinent ;
- éviter les longs textes en majuscules.

Ne jamais réduire une information importante en micro-typographie pour la faire entrer dans une composition.

Modifier plutôt la composition.

La promesse principale de la hero doit rester à quatre lignes visuelles maximum sur ordinateur et quatre lignes maximum sur mobile aux largeurs de contrôle.

Ne jamais reformuler la promesse uniquement pour satisfaire cette contrainte.

Adapter sa largeur, sa taille, ses retours et son interlignage.

Le H1 doit rester immédiatement lisible sans monopoliser presque tout le premier écran mobile.

## 6. Boutons et CTA

Tous les boutons possèdent une ombre extérieure visible cohérente avec la direction artistique.

Le CTA principal peut avoir davantage de relief qu’un CTA secondaire.

Prévoir des états :

- `hover` ;
- `focus-visible` ;
- `active`.

Les interactions doivent rester élégantes et ne pas provoquer de déplacement gênant de la mise en page.

Utiliser des transitions courtes, généralement de 150 à 250 ms.

Pas de pulsation gratuite ni d’animation décorative permanente.

Respecter `prefers-reduced-motion: reduce`.

Les zones tactiles importantes doivent mesurer environ 44 px minimum.

Éviter qu’un CTA important passe maladroitement sur deux lignes.

Cadencer les CTA selon la progression de décision plutôt que de placer automatiquement un bouton après chaque section.

## 7. Fragment Systeme.io

Livrer un seul fragment autonome destiné à un élément Code HTML Systeme.io.

Le fragment ne contient :

- ni `<html>` ;
- ni `<head>` ;
- ni `<body>`.

Il possède un seul conteneur racine portant une classe suffisamment unique.

Tout le CSS doit être encapsulé sous cette classe, y compris :

- media queries ;
- pseudo-éléments ;
- états interactifs.

Ne pas utiliser :

- bibliothèque ;
- framework ;
- CDN ;
- dépendance externe non autorisée.

Utiliser HTML et CSS natifs.

Ajouter du JavaScript uniquement lorsqu’une interaction indispensable ne peut pas être obtenue autrement.

Placer le JavaScript minimal à la fin du fragment.

Utiliser des balises correctement imbriquées et fermées avec une hiérarchie de titres logique.

Éviter les hauteurs fixes sur les blocs textuels et `overflow:hidden` lorsqu’il risque de masquer du contenu.

## 8. Responsive

Le mobile doit être conçu comme une composition autonome.

Ne pas simplement réduire ou empiler la version desktop.

Pour chaque relation horizontale, définir :

- l’ordre mobile ;
- la hiérarchie ;
- les espacements ;
- les connecteurs éventuels ;
- le comportement des médias.

Sur mobile :

- transformer les frises et schémas horizontaux en parcours verticaux lisibles ;
- éviter trois ou quatre micro-cartes côte à côte ;
- adapter titres, marges et espacements ;
- utiliser la pleine largeur pour les boutons lorsque pertinent ;
- supprimer les décalages décoratifs provoquant un débordement ;
- conserver autant que possible la signature visuelle.

Aucun débordement horizontal ne doit subsister.

## 9. Vidéos

Pour un fichier vidéo direct :

```html
<video controls playsinline preload="metadata" poster="URL_DU_POSTER">
  <source src="URL_DE_LA_VIDEO" type="video/mp4">
</video>
```

Ne jamais activer l’autoplay sonore.

Ne pas transformer arbitrairement un lecteur fourni en `<video>` lorsque son URL n’est pas un fichier vidéo direct.

Pour Vimeo, conserver l’iframe et son URL d’intégration.

L’iframe doit posséder un attribut `title` accessible.

Les paramètres d’affichage Vimeo peuvent être ajustés lorsque pertinent sans supprimer les paramètres privés nécessaires.

Ne jamais prétendre modifier depuis le HTML une métadonnée qui doit être modifiée directement dans Vimeo.

## 10. Compte à rebours

Ne créer un compte à rebours qu’avec :

- date exacte ;
- heure exacte ;
- fuseau horaire ;
- texte après expiration ;
- comportement à zéro lorsqu’il diffère d’un simple remplacement.

Utiliser du JavaScript natif.

Prendre en compte le véritable décalage UTC correspondant à la date.

Afficher immédiatement jours, heures, minutes et secondes.

À zéro, arrêter le compteur et appliquer le comportement validé.

Ne jamais inventer une échéance.

Ne jamais créer un faux compteur redémarrant au rechargement sauf demande explicite d’un délai individuel.

## 11. Popup Systeme.io

Un CTA HTML ne doit jamais essayer d’ouvrir directement un popup Systeme.io à partir du seul identifiant du popup.

Utiliser un véritable bouton natif Systeme.io comme pont.

Il faut disposer :

- de l’identifiant du popup ;
- d’un bouton natif placé hors du popup ;
- de la confirmation que son action est « Afficher le popup » ;
- de l’identifiant HTML de ce bouton.

Le bouton natif doit rester présent dans le DOM sur ordinateur et mobile.

Ne pas utiliser comme pont un bouton `send-form-button` ou configuré avec `sendForm`.

Les CTA HTML déclenchent un clic sur le véritable bouton natif.

Ne jamais manipuler directement les classes ou le `display` du conteneur React du popup comme solution principale.

## 12. Footer

Lorsque nécessaires à la page finale, utiliser les URL exactes fournies pour :

- Mentions légales et CGV ;
- Politique de confidentialité ;
- avis ;
- autres liens de footer.

Ne jamais fabriquer une destination manquante.

## 13. Prévisualisation autonome

Sur demande, fournir séparément un fichier HTML complet contenant au minimum :

```html
<!doctype html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Ne jamais confondre ce fichier avec le fragment destiné au bloc Code HTML Systeme.io.

## 14. Vérification visuelle

Une lecture du code n’est pas une validation visuelle.

Lorsque des outils de rendu sont réellement disponibles :

1. créer une prévisualisation ;
2. inspecter ordinateur et mobile ;
3. inspecter la page entière ;
4. corriger débordements, recadrages, espacements, alignements, ruptures de texte et répétitions ;
5. recommencer si nécessaire.

Si aucun outil ne permet réellement cette inspection, le signaler clairement.

Ne jamais prétendre qu’un rendu a été inspecté lorsqu’il ne l’a pas été.
