---
name: foil-conditions
description: Donne les conditions et le meilleur créneau pour faire du wingfoil, du windfoil ou du surffoil sur un spot ou autour d'un lieu, en croisant la météo (vent, houle, marée) avec les retours récents des riders TheFoilBuddy. À utiliser dès qu'un utilisateur demande si « ça marche », où ou quand aller naviguer en foil.
---

# Conditions et meilleur créneau de foil

## Quand l'utiliser
L'utilisateur demande les conditions, s'il peut aller naviguer, où aller ou à quelle heure, pour du wingfoil, du windfoil, du surffoil, du kitefoil ou du pumpfoil.

## Étapes
1. Trouver le spot :
   - nom de spot donné → `list_spots` ;
   - ville ou région donnée (« vers Bayonne ») → `find_spots_near`.
2. Pour chaque spot retenu (3 au plus), appeler ensemble :
   - `get_spot_conditions` : vent, rafales, direction, houle, prévisions sur 12 h ;
   - `get_spot_activity` : avis « ça ride / pas terrible », sessions récentes et messages des riders des dernières 24 h.
3. Croiser les deux sources :
   - wingfoil ou windfoil : vent établi et rafales pas trop fortes ;
   - surffoil : houle et période, avec un vent faible ou de terre ;
   - les retours récents des riders passent avant le modèle météo quand ils le contredisent.

## Réponse
- Commencer par un avis clair : « ça marche », « ça peut le faire » ou « laisse tomber ».
- Donner le meilleur créneau, avec l'heure et le vent attendu.
- Citer un ou deux retours des riders, en précisant la source : « d'après les riders TheFoilBuddy… ».
- Ne jamais inventer un retour de rider. S'il n'y a aucun message, le dire.
- Rester court : un rider lit la réponse sur son téléphone.
