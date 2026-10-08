---
term_id: TERM-014A
preferred_name_nl: Semantische gelijkenis
english_name: Semantic Similarity
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Semantiek, embeddings en evaluatie
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-019
- SRC-046
- SRC-047
- SRC-049
related_term_ids:
- TERM-013
- TERM-014B
- TERM-015
- TERM-016C
status: active
---

# Semantische gelijkenis

**Engelse term of afkorting:** Semantic Similarity  
**Term-ID:** `TERM-014A`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Semantiek, embeddings en evaluatie  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Semantische gelijkenis is de mate waarin twee woorden, zinnen, passages, documenten of conceptrepresentaties op elkaar lijken in betekenis, beoordeeld binnen een gekozen model, dataset, maatstaf en taak.

## Uitgebreide uitleg

Semantische gelijkenis gaat verder dan dezelfde spelling of dezelfde woorden. Twee uitingen kunnen inhoudelijk sterk op elkaar lijken terwijl zij andere formuleringen gebruiken. Omgekeerd kunnen twee teksten dezelfde woorden bevatten, maar door negatie, rolverdeling of context een andere betekenis hebben.

Gelijkenis kan op meerdere niveaus worden onderzocht, bijvoorbeeld tussen woorden, zinnen, passages, documenten of entiteiten. De uitkomst hangt af van de gekozen representatie. Een taxonomie, een kennisgraaf en een embeddingmodel kunnen hetzelfde begrippenpaar verschillend beoordelen.

Bij vectorrepresentaties wordt gelijkenis vaak geschat met een maat zoals cosinusgelijkenis of dot product. Dat cijfer is geen objectieve eigenschap van taal. Het is een uitkomst van het model, de trainingsdata, het trainingsdoel, de gekozen vectoren en de gebruikte maatstaf.

Wetenschappelijk onderzoek naar woordgelijkenis maakt bewust onderscheid tussen echte betekenisgelijkenis en bredere associatie. Woorden kunnen vaak samen voorkomen of bij hetzelfde onderwerp horen zonder werkelijk hetzelfde of bijna hetzelfde te betekenen.

## Belangrijke afbakening

| Relatie | Hoofdvraag | Voorbeeld | Opmerking |
| --- | --- | --- | --- |
| Lexicale overeenkomst | Lijken de vormen of woorden op elkaar? | scootmobiel en scootmobielen | Vormoverlap zegt nog niet alles over betekenis. |
| Semantische gelijkenis | Lijken de betekenissen op elkaar? | auto en wagen | Dit zijn in veel contexten bijna-synoniemen. |
| Semantische verwantschap | Zijn de begrippen inhoudelijk verbonden? | auto en brandstof | Sterk verbonden, maar niet vergelijkbaar in betekenis. |
| Semantische relevantie | Helpt de informatie bij de vraag of taak? | wintertemperatuur bij een vraag over actieradius | Relevant, ook zonder betekenisgelijkenis. |

## Voorbeeld

De volgende paren laten zien waarom één woord als gelijkenis vaak te grof is.

| Paar | Waarschijnlijkste relatie | Uitleg |
| --- | --- | --- |
| auto - wagen | Hoge semantische gelijkenis | De woorden kunnen in veel zinnen naar hetzelfde type object verwijzen. |
| auto - voertuig | Hiërarchische verwantschap | Een auto is een type voertuig. De woorden zijn niet volledig uitwisselbaar. |
| auto - brandstof | Functionele of thematische verwantschap | Brandstof kan met een auto samenhangen, maar is geen auto. |
| auto - recept | Zwakke algemene relatie | Er is zonder aanvullende context weinig directe betekenisverbinding. |

| Notitie: Een echt model kan andere scores geven. De tabel verduidelijkt de begrippen en is geen universele benchmark. |
| --- |

## Wat is bevestigd?

- Wetenschappelijke evaluaties onderscheiden semantische gelijkenis van bredere associatie of verwantschap.

- Embeddings kunnen woorden, zinnen of documenten als vectoren representeren en met een gekozen maatstaf vergelijken.

- De uitkomst van een gelijkenismaat is model- en taakafhankelijk.

## Wat is niet bevestigd?

- Er bestaat geen openbare universele Google-score voor semantische gelijkenis.

- Een hogere embeddinggelijkenis garandeert geen hogere ranking, AI-citatie of betere content.

- Het toevoegen van zoveel mogelijk synoniemen of semantisch vergelijkbare woorden is geen bewezen optimalisatieregel.

## Praktische toepassing

- Gebruik gelijkenis bij queryclustering, deduplicatie, passagezoeking en het vinden van parafrasen.

- Controleer altijd of twee ogenschijnlijk vergelijkbare vragen werkelijk dezelfde gebruikerstaak en voorwaarden hebben.

- Schrijf natuurlijk en precies. Gebruik alternatieve formuleringen wanneer zij de uitleg verduidelijken, niet om een vermeende semantische dichtheid te verhogen.

- Beoordeel productnamen, eenheden en juridische termen ook lexicaal. Semantische nabijheid vervangt exacte identifiers niet.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Alles wat inhoudelijk bij hetzelfde onderwerp hoort, is semantisch vergelijkbaar. In werkelijkheid kan het sterk verwant en relevant zijn zonder op elkaar te lijken in betekenis. |
| --- |

## Zie ook

TERM-014B Semantische verwantschap, TERM-015 Semantische relevantie, TERM-016C Embedding, TERM-013 Semantische afstand.

## Verwante begrippen

- `TERM-013`: Semantische afstand
- `TERM-014B`: Semantische verwantschap
- `TERM-015`: Semantische relevantie
- `TERM-016C`: Embedding

## Bronnen en actualiteit

**Kernbronnen:** SRC-019, SRC-046, SRC-047, SRC-049
