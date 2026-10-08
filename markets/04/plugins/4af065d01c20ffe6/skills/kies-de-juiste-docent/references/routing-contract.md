# Routingcontract

## Beslisvolgorde

1. Herken expliciete examenintentie aan woorden als `officieel`, `examen`, `tijdvak`, `correctievoorschrift`, `punten` of `kijk mijn antwoord na`.
2. Behoud bij een vervolgbericht de eerder gekozen route zolang de leerbedoeling en lesgrens niet veranderen.
3. Herken expliciete lesintentie aan een lesnaam, video, lescode, AI-Tom of een eerder gekozen lespackage.
4. Gebruik voor een nieuwe leervraag altijd `avl_route_learning_request`; de server controleert niveau, dekking, lesmatch en releasestatus.
5. Volg de teruggegeven `action` zonder zelf een ontbrekende route of bron aan te vullen.

## Acties

- `ask_level`: toon alleen `studentMessage`, wacht op HAVO of VWO en routeer de vervolgvraag opnieuw.
- `use_ai_tom`: gebruik uitsluitend het teruggegeven vrijgegeven lespackage.
- `use_aisha`: gebruik uitsluitend het teruggegeven Aisha-profiel.
- `stop_unavailable`: toon alleen `studentMessage` en stop zonder webzoekactie of algemene modelkennis.

## Grenzen

- Verzin geen niveau. `levelEvidence` is alleen een letterlijk gebruikerscitaat met HAVO of VWO.
- Een niet-vrijgegeven les valt publiek terug op Aisha; doe niet alsof een transcriptie is geladen.
- Officiële examenvragen en correctievoorschriften mogen alleen worden aangeboden wanneer de router ze aantoonbaar als vrijgegeven inhoud teruggeeft.
- Stuur geen leerlingnaam, school, cijfers, volledig leerlingantwoord of andere persoonsgegevens naar de MCP-server.
- Meng Aisha- en AI-Tom-instructies niet stilletjes in één antwoord.

## Voorbeelden

- `Leg uit wat El Niño is voor 5 havo`: routeer eerst; AI-Tom alleen bij één sterke vrijgegeven lesmatch, anders Aisha.
- `Leg het klimaat van Zuid-Amerika uit voor 6 vwo`: routeer eerst; een brede vraag gaat normaal naar Aisha.
- `Geef een officiële examenvraag over El Niño`: routeer als examenintentie en respecteer een eventuele beschikbaarheidsgrens.
- `Leg El Niño uit`: vraag via de router eerst naar HAVO of VWO.
