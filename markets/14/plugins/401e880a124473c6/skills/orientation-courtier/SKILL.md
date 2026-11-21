---
name: orientation-courtier
description: Explique le rôle du courtier, prépare la synthèse des besoins d'assurance (outil build_broker_brief) et, uniquement à la demande explicite de l'utilisateur et après son consentement, le met en relation avec un courtier partenaire d'Albingia ou avec son propre courtier (outil request_broker_contact). À utiliser quand l'utilisateur veut une synthèse pour son courtier, demande à être recontacté, ou demande comment souscrire chez Albingia.
compatibility: Nécessite le serveur MCP albingia-diagnostic (outils build_broker_brief et request_broker_contact). Compatible avec tout assistant qui lit le format SKILL.md.
---

# Orientation vers un courtier

Appliquer aussi la skill `garde-fous`. Si elle n'est pas disponible, retenir au minimum : aucun tarif, aucune promesse de couverture, aucun envoi sans consentement explicite.

## Principe

Albingia ne vend pas en direct : ses contrats passent exclusivement par des courtiers, qui conseillent l'entreprise et analysent ses besoins. Le plugin ne fait que transmettre une demande.

## Préparer une synthèse (rien n'est envoyé)

Si l'utilisateur veut un document pour son courtier, appeler `build_broker_brief` avec les mêmes paramètres que le diagnostic (`activite`, `secteur`, `effectif`, etc.). Si aucun diagnostic n'a été fait, poser d'abord les questions de la skill `diagnostic-risques`.

Restituer la synthèse **telle quelle**, sans la reformuler : elle mentionne déjà sa source.

## Mise en relation — uniquement sur demande explicite

Ne commencer que si l'utilisateur a lui-même demandé à être recontacté. Suivre ces étapes dans l'ordre, sans en sauter :

1. Demander si l'entreprise a déjà un courtier. Si oui, noter le nom du cabinet : la demande lui sera adressée.
2. Recueillir uniquement ces informations :

   | Information | Paramètre | Obligatoire |
   |---|---|---|
   | Nom et prénom | `nom` | oui |
   | Raison sociale | `entreprise` | oui |
   | E-mail professionnel | `email` | oui |
   | Téléphone professionnel | `telephone` | non |
   | Département du siège (ex. `75`, `69`, `2A`) | `departement` | oui |
   | Cabinet de courtage actuel | `courtier_actuel` | non |
   | Branches concernées | `branches_interet` | oui, parmi `dommages`, `multirisques`, `risques_techniques`, `responsabilite_civile`, `construction`, `transport`, `art_precieux`, `risques_speciaux`, `individuelle_accident` |
   | Besoin en quelques phrases | `besoin` | oui, 1 000 caractères au plus |
   | Profil de l'entreprise (`activite`, `secteur`, `effectif`, etc.) | `profil` | oui, mêmes valeurs que pour `diagnose_business_risks` ; sert à rédiger la synthèse transmise. Sans diagnostic préalable, poser d'abord les questions de la skill `diagnostic-risques` |

3. Afficher la mention de consentement, **mot pour mot**, dans un message à part :

   > En confirmant, vous acceptez qu'Albingia transmette vos coordonnées professionnelles et votre synthèse à un courtier partenaire (ou au courtier que vous avez désigné) pour qu'il vous recontacte. Vos données sont conservées 3 ans au maximum. Vous pouvez exercer vos droits à : dpo@albingia.fr (adresse à confirmer).

4. Attendre la réponse de l'utilisateur. Continuer **seulement** si elle exprime clairement son accord (« oui », « j'accepte », « je confirme »). Un accord donné avant l'affichage de la mention ne compte pas. Sans accord, ne rien envoyer et le dire.
5. Appeler `request_broker_contact` avec `consentement: true`, les informations recueillies et la preuve du consentement `preuve_consentement`, exigée par le RGPD (art. 7.1) pour démontrer l'accord. Elle se limite à deux messages :
   - `message_assistant` : le texte intégral, **mot pour mot**, de votre message qui contenait la mention ;
   - `reponse_utilisateur` : le texte intégral, **mot pour mot**, de la réponse de l'utilisateur.

   Ne pas résumer ni reformuler ces deux messages : ils sont conservés comme preuve. Ne jamais y joindre d'autre partie de la conversation. Si l'outil répond que la mention est absente, l'afficher à nouveau mot pour mot et redemander l'accord.
6. Donner la référence renvoyée par l'outil et dire qui recontactera l'utilisateur. Ne promettre ni délai, ni tarif, ni acceptation du risque. Si l'outil renvoie une erreur, le dire et proposer de contacter directement un courtier, sans inventer de référence.

## Ne jamais

- Envoyer une demande que l'utilisateur n'a pas formulée.
- Remplir un champ obligatoire par supposition : le demander.
- Inclure dans `besoin` des données de santé, des données personnelles de salariés ou de tiers, ou le contenu de la conversation.
