---
name: examenantwoord-nakijken
description: Herken automatisch een verzoek om een leerlingpoging bij een eerder aangeboden officiële examenvraag na te kijken. Controleer via AI Voor Leerlingen of het officiële correctievoorschrift beschikbaar is; onthul vóór een poging nooit antwoord, rubric of scorepunten.
---

# Examenantwoord nakijken

Controleer dat er in het gesprek een serieuze leerlingpoging en een herkenbare eerdere officiële examenvraag staan. Roep daarna eerst `avl_route_learning_request` aan met het letterlijke nakijkverzoek, het afgeleide vak en kernonderwerp. Stuur geen volledig leerlingantwoord of persoonsgegevens naar de MCP-server; `levelEvidence` mag alleen een letterlijk citaat met HAVO of VWO zijn.

Bij `stop_unavailable` toon je alleen `studentMessage` en stop je. Verzin geen correctievoorschrift, modelantwoord of punten. Bij `ask_level` stel je alleen de teruggegeven niveauvraag.

Vergelijk pas wanneer een toekomstige vrijgegeven versie gecontroleerde officiële criteria teruggeeft. Vergelijk dan uitsluitend het lokaal zichtbare leerlingantwoord met die criteria. Beoordeel ieder criterium afzonderlijk en voeg geen eisen toe die niet in vraag of correctievoorschrift staan.

Geef in deze volgorde:

1. juist, gedeeltelijk juist of nog niet juist;
2. wat inhoudelijk klopt;
3. wat ontbreekt volgens de criteria;
4. één concrete hint of verbetering;
5. punten alleen wanneer de officiële rubric dit ondersteunt.

Geef het volledige modelantwoord alleen wanneer de leerling daar expliciet om vraagt of na feedback nog vastloopt.

Lees [references/feedback-contract.md](references/feedback-contract.md) bij samengestelde antwoorden, punten of twijfel over antwoordtoegang.
