---
term_id: TERM-015
preferred_name_nl: Semantische relevantie
english_name: Semantic Relevance
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval, semantiek en gebruikerstaak
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-030
- SRC-046
- SRC-047
- SRC-049
related_term_ids:
- TERM-011A
- TERM-011F
- TERM-014A
- TERM-014B
status: active
---

# Semantische relevantie

**Engelse term of afkorting:** Semantic Relevance  
**Term-ID:** `TERM-015`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval, semantiek en gebruikerstaak  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Semantische relevantie is de mate waarin informatie inhoudelijk geschikt en bruikbaar is voor een specifieke zoekvraag, gebruikerstaak en context, ook wanneer de gebruikte woorden niet sterk op elkaar lijken.

## Uitgebreide uitleg

Relevantie gaat niet alleen over betekenisoverlap. Zij gaat vooral over de vraag of een document, passage, afbeelding, video of gegeven helpt om een informatiebehoefte op te lossen. Dezelfde passage kan voor de ene vraag zeer relevant en voor een andere vraag nauwelijks relevant zijn.

Binnen Information Retrieval kan relevantie worden beoordeeld door mensen of worden geschat door een systeem. Een systeemscore is een operationele schatting binnen een model. Het is niet hetzelfde als de volledige menselijke beoordeling van juistheid, volledigheid, bruikbaarheid en vertrouwen.

Relevantie kan worden bekeken op query-documentniveau, query-passageniveau en taakniveau. Een pagina kan als geheel breed relevant zijn, terwijl slechts één sectie het concrete antwoord bevat. Omgekeerd kan een tekst de juiste woorden bevatten, maar de vraag niet beantwoorden.

Actualiteit, locatie, doelgroep, productvariant en wettelijke context kunnen relevantie veranderen. Een advies over een accupakket kan technisch correct zijn, maar ongeschikt voor een andere uitvoering of een ander gebruikspatroon.

## Belangrijke afbakening

| Begrip | Kernvraag | Voorbeeld |
| --- | --- | --- |
| Gelijkenis | Lijken de betekenissen op elkaar? | scootmobiel en elektrische mobiliteitsscooter |
| Verwantschap | Zijn de begrippen inhoudelijk verbonden? | accu en actieradius |
| Relevantie | Helpt deze informatie bij deze vraag en taak? | temperatuur, gewicht en snelheid bij een vraag over winterbereik |
| Kwaliteit of betrouwbaarheid | Is de informatie correct, controleerbaar en verantwoord? | eigen meting met methode, datum en voorwaarden |

## Voorbeeld

Zoekvraag: Hoe ver kan ik in de winter met deze scootmobiel rijden? Een passage over accucapaciteit, buitentemperatuur, snelheid, totaalgewicht, bandenspanning en ondergrond kan sterk relevant zijn, ook wanneer de exacte woorden van de zoekvraag nauwelijks worden herhaald. Een algemene geschiedenis van accu’s kan verwant zijn aan het onderwerp, maar voor deze taak weinig relevant.

## Wat is bevestigd?

- Relevantie is context- en taakafhankelijk en kan door systemen worden geschat of door beoordelaars worden beoordeeld.

- Lexicale overeenkomst en semantische gelijkenis kunnen bijdragen aan matching, maar zijn niet de volledige definitie van relevantie.

- Zoeksystemen kunnen conceptuele matching gebruiken wanneer query en pagina niet dezelfde woorden bevatten.

## Wat is niet bevestigd?

- Er bestaat geen openbare universele semantische-relevantiescore die een contentspecialist rechtstreeks kan optimaliseren.

- Het opnemen van semantisch verwante woorden bouwt niet automatisch topical authority op.

- Een relevante passage garandeert geen ranking, citatie of aanbeveling. Toegang, kwaliteit, betrouwbaarheid en andere systemen spelen ook mee.

## Praktische toepassing

- Begin iedere briefing met de gebruikerstaak en niet alleen met een zoekwoord.

- Controleer per sectie welke vraag wordt beantwoord, welke voorwaarden gelden en welke vervolgstap de gebruiker heeft.

- Vermijd pagina’s die alleen woorden uit concurrenten combineren zonder een zelfstandige bruikbare functie.

- Gebruik tabellen, eigen tests en beslismodellen wanneer die de taak beter oplossen dan extra lopende tekst.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Semantische relevantie betekent dat zoveel mogelijk begrippen uit hetzelfde onderwerp in één tekst moeten staan. Relevantie vraagt juist selectie: alleen informatie die de concrete taak, beslissing of context werkelijk ondersteunt. |
| --- |

## Zie ook

TERM-011A Relevantie in Information Retrieval, TERM-014A Semantische gelijkenis, TERM-014B Semantische verwantschap, TERM-011F Reranking.

## Verwante begrippen

- `TERM-011A`: Relevantie in Information Retrieval
- `TERM-011F`: Reranking
- `TERM-014A`: Semantische gelijkenis
- `TERM-014B`: Semantische verwantschap

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-030, SRC-046, SRC-047, SRC-049
