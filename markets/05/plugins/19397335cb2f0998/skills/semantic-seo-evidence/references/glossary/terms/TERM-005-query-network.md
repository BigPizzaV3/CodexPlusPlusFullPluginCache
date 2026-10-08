---
term_id: TERM-005
preferred_name_nl: Query Network
english_name: Query Network
cluster_id: 2
cluster_name: Zoekintentie en queryverwerking
type_context: Frameworkterm / queryanalyse / contentarchitectuur
evidence_labels:
- B
- D
- E
- F
last_checked: '2026-07-25'
source_ids:
- SRC-007
- SRC-009
- SRC-020
- SRC-021
- SRC-024
- SRC-036
related_term_ids:
- QRY-010
- QRY-015
- TERM-005A
- TERM-006
- TERM-006A
- TERM-012A
- TERM-019
- TERM-021B
- TERM-024
status: active
---

# Query Network

**Engelse term of afkorting:** Query Network  
**Term-ID:** `TERM-005`  
**Hoofdcategorie:** 2 Zoekintentie en queryverwerking  
**Type en context:** Frameworkterm / queryanalyse / contentarchitectuur  
**Bewijsbasis:** B, D, E en F  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een Query Network is binnen Semantic SEO een onderzoeks- en planningsmodel waarin verwante zoekopdrachten, zoekintenties, entiteiten, gebruikerstaken, contexten en mogelijke vervolgvragen met elkaar worden verbonden. Het model helpt makers om een informatiebehoefte systematisch te onderzoeken. Het is geen open standaard en geen openbaar bevestigd intern Google-object.

## Uitgebreide uitleg

Het woord network geeft aan dat zoekopdrachten niet uitsluitend als losse trefwoorden worden bekeken. Een brede vraag kan samenhangen met verfijningen, alternatieve formuleringen, deelvragen, vergelijkingen, voorwaarden en vervolgstappen. Wetenschappelijk onderzoek kent verwante modellen, zoals queryclusters, query-refinements en query-flow graphs. In zo’n query-flow graph kunnen opeenvolgende queries worden verbonden wanneer zij waarschijnlijk deel uitmaken van dezelfde zoekmissie. [SRC-036]

Google-onderzoek laat eveneens zien dat queryverfijningen op onderliggende gebruikersintentie kunnen worden geclusterd. Een Google-patent beschrijft queryclusters met een representative query. Google’s actuele uitleg over generatieve zoekfuncties noemt query fan-out, waarbij meerdere verwante zoekopdrachten kunnen worden uitgevoerd om aanvullende informatie op te halen. Deze bronnen ondersteunen het nut van queryrelaties, maar bevestigen niet de volledige frameworkstructuur van Query Aspect, Query Definition en Query Theme. [SRC-021] [SRC-020] [SRC-024]

Binnen het framework kunnen de drie bestaande velden blijven bestaan als redactionele hulpmiddelen. Zij moeten zichtbaar als frameworkvelden worden benoemd en niet als universele onderdelen van query processing.

| Frameworkveld | Betekenis in deze begrippenlijst | Bewijsgrens |
| --- | --- | --- |
| Query Aspect | De invalshoek of interpretatie van de vraag, bijvoorbeeld actieradius als praktisch gebruikskenmerk. | Bruikbaar frameworkveld, geen gestandaardiseerde IR-term in deze exacte betekenis. |
| Query Definition | Een volledige natuurlijke-taalformulering van wat de gebruiker waarschijnlijk wil weten of doen. | Redactionele explicitering, niet noodzakelijk de query die een platform intern gebruikt. |
| Query Theme | Het bredere onderwerp of taakgebied waarin de vraag valt. | Hulpmiddel voor inhoudelijke afbakening, geen verplichte paginaterm of rankingsignaal. |

## Aanbevolen extra velden voor 2026

| Veld | Vraag die het beantwoordt |
| --- | --- |
| Primaire gebruikerstaak | Wat moet de gebruiker na de content kunnen kiezen, begrijpen, controleren of uitvoeren? |
| Primaire entiteit | Over welk product, merk, persoon, onderwerp of concept gaat de vraag precies? |
| Contextuele kwalificaties | Welke doelgroep, plaats, tijd, beperking, uitvoering of gebruikssituatie verandert het antwoord? |
| Queryrelatie | Is dit een synonieme variant, verfijning, vergelijking, voorwaarde, probleem, vervolgvraag of alternatieve intentie? |
| Bewijsbehoefte | Welke bron, meting, deskundige of demonstratie is nodig om het antwoord betrouwbaar te maken? |
| Contentvorm | Is een pagina, sectie, tabel, video, calculator, productrecord of keuzehulp het beste antwoord? |

## Voorbeeld voor ScootmobielCentrum

| Centrale gebruikersvraag<br>Welke scootmobiel past bij mijn lichaam, gebruiksomgeving en gewenste afstand? |
| --- |

| Relatie | Voorbeeldquery of informatiebehoefte | Passende inhoudsvorm |
| --- | --- | --- |
| Stabiliteit | Is een drie- of vierwielscootmobiel stabieler voor mij? | Vergelijkingssectie met voor- en nadelen en praktijktest. |
| Actieradius | Hoeveel bereik heb ik werkelijk nodig voor mijn vaste ritten? | Uitleg plus calculator of keuzehulp met testvoorwaarden. |
| Transport | Welke scootmobiel past in mijn auto? | Afmetingen, opvouwvideo en gecontroleerde kofferbaktests. |
| Bediening | Welke bediening past bij beperkte handkracht? | Demonstratie van duimgas, voetgas en remopties. |
| Comfort | Welke stoel en verstelling passen bij mijn lichaamslengte? | Meetgegevens, foto’s en afsteladvies. |
| Regels | Welke actuele regels gelden voor mijn uitvoering en snelheid? | Afzonderlijke juridisch gecontroleerde informatiebron. |

## Wat is bevestigd?

- Queries en queryverfijningen kunnen technisch worden gegroepeerd op basis van onder meer intentie, resultaatsamenhang, klik- en sessiegegevens, tekst en andere representaties. [SRC-020] [SRC-021]

- Query-flow graphs zijn een wetenschappelijk model voor relaties tussen opeenvolgende queries binnen mogelijke zoekmissies. [SRC-036]

- Google beschrijft query fan-out als onderdeel van bepaalde generatieve zoekprocessen. [SRC-024]

- Koray’s framework gebruikt queryrelaties, context en contentnetwerken als praktisch Semantic SEO-model. [SRC-007] [SRC-009]

## Wat is niet bevestigd?

- Dat één Query Network alle mogelijke woordverdelingen van een taal bevat of kan bevatten.

- Dat Google ieder onderwerp intern opslaat volgens exact de velden Query Aspect, Query Definition en Query Theme.

- Dat iedere query in het netwerk een eigen pagina moet krijgen.

- Dat het letterlijk opnemen van alle netwerktermen een rankingvoordeel oplevert.

- Dat een door een SEO-tool gegenereerd netwerk gelijk is aan het interne querymodel van een zoek- of AI-platform.

## Praktische toepassing

1. Begin met een echte gebruikerstaak en niet met een export van losse zoekwoorden.

2. Verbind queries op basis van betekenis, taak, entiteit, context, voorwaarde en vervolgactie. Noteer bij iedere verbinding waarom die bestaat.

3. Maak afzonderlijk zichtbaar welke relaties uit data komen, welke door experts zijn beoordeeld en welke nog hypotheses zijn.

4. Bepaal pas daarna of een informatiebehoefte een eigen pagina, een sectie, een tabel, een video of een hulpmiddel nodig heeft.

5. Voorkom overlap door per taak één primaire informatie-eigenaar of canonical contentbron aan te wijzen.

6. Werk het netwerk bij wanneer producten, regels, zoekgedrag, gebruikersvragen of beschikbare bewijzen wezenlijk veranderen.

## Veelgemaakte misvatting

“Een Query Network is een lijst met alle zoekwoorden die in de tekst moeten staan.” Het netwerk is in de eerste plaats een onderzoeks- en architectuurmodel. De uiteindelijke content gebruikt alleen de informatie die nodig is om de taak helder, volledig en betrouwbaar op te lossen.

## Zie ook

Query Cluster, Representative Query, Query fan-out, Search Intent, User Task, Semantic Content Network, Central Entity, Contextual Layer en Topical Map.

## Verwante begrippen

- `QRY-010`: Zoekintentie
- `QRY-015`: Query Fan-out
- `TERM-005A`: Query Cluster
- `TERM-006`: Semantisch contentnetwerk
- `TERM-006A`: Topical Map
- `TERM-012A`: Representative Query
- `TERM-019`: Central Entity
- `TERM-021B`: Gebruikerstaak
- `TERM-024`: Contextual Layer

## Bronnen en actualiteit

**Kernbronnen:** SRC-007, SRC-009, SRC-020, SRC-021, SRC-024, SRC-036
