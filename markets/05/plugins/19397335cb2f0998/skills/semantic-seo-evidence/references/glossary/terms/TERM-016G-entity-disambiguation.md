---
term_id: TERM-016G
preferred_name_nl: Entity Disambiguation
english_name: Entity Disambiguation
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Entiteitsverwerking en contextinterpretatie
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-046
- SRC-051
- SRC-052
related_term_ids:
- TERM-002
- TERM-016E
- TERM-016F
- TERM-023
status: active
---

# Entity Disambiguation

**Engelse term of afkorting:** Entity Disambiguation  
**Term-ID:** `TERM-016G`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Entiteitsverwerking en contextinterpretatie  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Entity disambiguation is het bepalen welke specifieke kandidaatentiteit bij een tekstvermelding wordt bedoeld, op basis van de omliggende tekst, documentcontext en beschikbare kennisbron.

## Uitgebreide uitleg

Eén naam kan naar meerdere entiteiten verwijzen. Disambiguatie vergelijkt mogelijke kandidaten met signalen zoals omliggende woorden, documentonderwerp, co-mentions, taal, tijd, locatie en relaties tussen kandidaten.

Disambiguatie kan lokaal werken met woorden rond de mention of documentbreed met andere entiteiten en de centrale context. Moderne systemen combineren vaak beide.

Entity disambiguation overlapt met word-sense disambiguation, maar is niet hetzelfde. Word-sense disambiguation kiest meestal een betekenis van een woord, terwijl entity disambiguation een concrete entiteit uit een kennisbron kiest.

Source Context kan praktisch helpen om ambiguïteit in content te verminderen, maar het is geen garantie dat ieder systeem dezelfde kandidaat selecteert.

## Belangrijke afbakening

| Context | Mogelijke betekenis van “Pride” | Benodigde verduidelijking |
| --- | --- | --- |
| Algemene taal | trots of waardigheid | zinsbetekenis en grammaticale rol |
| Evenementencontext | Pride-evenement | plaats, datum en organisator |
| Productcontext | Nipponia Pride | merk, producttype, uitvoering en specificaties |
| Organisatiecontext | organisatie met Pride in de naam | officiële naam, locatie en identifier |

## Voorbeeld

De formulering “De Nipponia Pride is een driewielscooter met een motor van 650 watt” geeft veel meer disambiguatiecontext dan alleen “Pride”. De merknaam, het producttype en de eigenschap helpen de productkandidaat onderscheiden van andere betekenissen.

## Wat is bevestigd?

- Entity disambiguation gebruikt context om tussen meerdere kandidaatentiteiten te kiezen.

- Lokale aandacht en documentbrede gezamenlijke inferentie zijn beschreven onderzoeksmethoden.

- De uitkomst is afhankelijk van kandidaatset, knowledge base, taal en model.

## Wat is niet bevestigd?

- Een centraal zoekwoord of Central Entity zorgt niet automatisch voor foutloze disambiguatie.

- Meer herhaling van een merknaam garandeert geen juiste platformkoppeling.

- Disambiguatie bewijst niet dat de bijbehorende claims juist of actueel zijn.

## Praktische toepassing

- Gebruik bij de eerste vermelding de volledige officiële naam en productcategorie.

- Leg onderscheidende variantgegevens dichtbij de claim vast.

- Gebruik consistente identifiers in productregister, URL, structured data en feeds waar passend.

- Vermijd geïsoleerde titels of koppen die alleen uit een dubbelzinnige modelnaam bestaan.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Entity disambiguation is alleen een synoniemenprobleem. Het gaat meestal om het kiezen tussen verschillende echte entiteiten of identifiers die dezelfde of vergelijkbare naam hebben. |
| --- |

## Zie ook

TERM-016F Entity Linking, TERM-016E Named Entity Recognition, TERM-023 Contextual Domain, TERM-002 Entity.

## Verwante begrippen

- `TERM-002`: Entiteit
- `TERM-016E`: Named Entity Recognition
- `TERM-016F`: Entity Linking
- `TERM-023`: Contextual Domain

## Bronnen en actualiteit

**Kernbronnen:** SRC-046, SRC-051, SRC-052
