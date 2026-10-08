---
name: officiele-examenvraag-oefenen
description: Herken automatisch een expliciet verzoek om een officiële Nederlandse HAVO- of VWO-examenvraag, CE-vraag of examenopgave te oefenen. Controleer eerst via AI Voor Leerlingen of officiële examendata beschikbaar is; verzin nooit een vervangende vraag, bron, antwoord of rubric.
---

# Officiële examenvraag oefenen

Roep eerst `avl_route_learning_request` aan met de letterlijke leerlingvraag, het afgeleide vak en korte kernonderwerp. Stuur `levelEvidence` alleen mee als letterlijk citaat waarin HAVO of VWO staat.

Bij `stop_unavailable` toon je alleen `studentMessage` en stop je. Zoek niet op het web, maak geen eigen examenvraag en gebruik geen algemene modelkennis om officiële inhoud na te bootsen. Bij `ask_level` stel je alleen de teruggegeven niveauvraag.

Presenteer pas een officiële vraag wanneer de router in een toekomstige vrijgegeven versie een compleet, gecontroleerd opgavepakket teruggeeft. Controleer dan dat het pakket alle benodigde context en bronnen bevat.

Toon in de officiële volgorde:

1. vak, niveau, jaar, tijdvak en vraagnummer;
2. titel en relevante context van de opgave;
3. vraaggebonden context;
4. alle vereiste bronnen met labels, onderschriften, de gekoppelde bronviewer en een klikbare noodlink;
5. de gekozen vraag.

Controleer `sourceDelivery` voordat je de bron presenteert. Bij status `viewer_ready` wordt de
MCP-bronviewer automatisch naast het toolresultaat gerenderd. Maak dan zelf geen Markdown-
afbeelding of bestandskaart; vermeld alleen bronlabel, onderschrift en de noodlink. Zeg niet dat de
kaart zichtbaar is op basis van de technische status alleen. Bij status `link_only` zeg je eerlijk
dat de bron vooraf niet kon worden gecontroleerd en laat je de leerling de noodlink openen. Doe
nooit alsof een lege of ontbrekende afbeelding zichtbaar is.

Geef geen rubric, modelantwoord of beslissende hint vóór de poging. Wacht op het antwoord van de leerling.

Als `dependencyKind` aangeeft dat eerdere vragen nodig zijn, bied de vereiste reeks aan of kies een andere vraag. Verzin nooit een ontbrekende bron of een antwoord op een voorgaande vraag.

Lees [references/opgavepakket-contract.md](references/opgavepakket-contract.md) voordat je een pakket met bronnen of afhankelijkheden presenteert.
