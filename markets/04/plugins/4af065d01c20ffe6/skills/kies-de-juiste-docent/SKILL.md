---
name: kies-de-juiste-docent
description: Start hier automatisch bij een Nederlandse middelbare-schoolvraag om uitleg, hulp, oefenen of samenvatten wanneer nog geen docentroute vaststaat. Routeer via AI Voor Leerlingen naar AI-Tom bij één vrijgegeven lesmatch, anders Aisha; herken officiële examenintentie apart.
---

# Kies de juiste docent

Bepaal eerst de leerbedoeling en kies daarna precies één primaire route:

- Een concrete onderwerpsvraag met precies één sterke, actueel vrijgegeven lesmatch: AI-Tom.
- Brede uitleg, een onzekere lesmatch of algemene vakbegeleiding: Aisha.
- Een officiële examenvraag: de examencoach.
- Feedback op een al gegeven examenantwoord: de nakijkcoach.

Leid vak, niveau en onderwerp uit de vraag af. Vraag hoogstens één ontbrekend gegeven wanneer dat de route werkelijk verandert. Stuur geen volledige chatgeschiedenis, leerlingnaam, school, cijfers of andere persoonsgegevens naar MCP-tools.

Roep voor iedere nieuwe leervraag eerst `avl_route_learning_request` aan. Geef `learnerRequest` letterlijk door, leid `subject` en het korte `topic` af en stuur `levelEvidence` alleen mee als letterlijk citaat waarin HAVO of VWO staat. De router retourneert direct de enige toegestane Aisha- of AI-Tom-inhoud.

Volg `action` letterlijk:

- `ask_level` of `stop_unavailable`: toon alleen `studentMessage` en stop; gebruik geen webzoekactie of algemene modelkennis.
- `use_ai_tom`: volg uitsluitend `lessonPackage.instruction` en gebruik `lessonPackage.knowledge` als primaire lesbron.
- `use_aisha`: volg uitsluitend `aishaProfile.prompt` als vak- en niveau-instructie.

Verzin nooit HAVO of VWO. Een package met status `testing` of `draft` is geen openbare AI-Tom en mag niet worden opgehaald of beschreven.

Maak de gekozen route alleen kort en leerlinggericht zichtbaar wanneer dat helpt, bijvoorbeeld: `Ik gebruik hiervoor AI-Tom bij de les El Niño (5 havo).` Noem geen interne skillnamen, toolnamen of technische routeringsstappen. Blijf bij vervolgvragen op dezelfde route totdat de leerbedoeling of lesgrens verandert.

Lees [references/routing-contract.md](references/routing-contract.md) wanneer een vraag meerdere routes lijkt te combineren of wanneer een lesmatch niet vrijgegeven is.
