---
term_id: TERM-011B
preferred_name_nl: Sparse Retrieval
english_name: Sparse Retrieval
cluster_id: 3
cluster_name: Information Retrieval en semantische matching
type_context: Information Retrieval / lexicale retrieval
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-012
- SRC-013
- SRC-014
- SRC-016
- SRC-029
- SRC-039
- SRC-040
related_term_ids:
- IR-012
- IR-014
- TERM-011C
- TERM-011D
status: active
---

# Sparse Retrieval

**Engelse term of afkorting:** Sparse Retrieval  
**Term-ID:** `TERM-011B`  
**Hoofdcategorie:** 3 Information Retrieval en semantische matching  
**Type en context:** Information Retrieval / lexicale retrieval  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Sparse Retrieval haalt informatie op met representaties waarin slechts een klein deel van een zeer groot termen- of tokenvocabulaire een niet-nulgewicht krijgt. Klassieke voorbeelden zijn retrieval met een inverted index, TF-IDF en BM25. Moderne learned sparse modellen kunnen termgewichten leren, maar blijven schaarse representaties gebruiken.

## Hoe het werkt

Bij klassieke sparse retrieval worden documenten gekoppeld aan termen die erin voorkomen. Een inverted index maakt het mogelijk snel documenten te vinden die een queryterm bevatten. TF-IDF weegt termen op basis van frequentie in een document en zeldzaamheid in de collectie. BM25 gebruikt onder meer termfrequentie, documentlengte en verzadiging. [SRC-012] [SRC-013] [SRC-014]

| Sterk in | Waarom |
| --- | --- |
| Exacte namen en productcodes | Een zeldzame modelnaam, SKU of foutcode kan zeer onderscheidend zijn. |
| Getallen en eenheden | Exacte waarden zoals 1000 W of 45 km/u kunnen letterlijk worden gematcht. |
| Controleerbare termen | De bijdrage van querytermen is vaak beter uitlegbaar dan bij dichte vectoren. |
| Efficiënte eerste selectie | Inverted indexes kunnen grote collecties snel doorzoeken. |

| Beperking | Gevolg |
| --- | --- |
| Parafrasen zonder gedeelde termen | Een relevant document kan worden gemist wanneer de gebruiker heel andere woorden gebruikt. |
| Dubbelzinnige woorden | Letterlijke overlap zegt niet vanzelf welke betekenis bedoeld is. |
| Keyword stuffing | Meer herhaling maakt een document niet automatisch relevanter en kan de leesbaarheid schaden. |
| Losse getallen zonder context | Exacte matching kan een waarde vinden die bij een andere variant of voorwaarde hoort. |

## Belangrijke begrenzing van oude termen

- Term saturation wordt niet als zelfstandige universele SEO-metriek overgenomen. Binnen BM25 bestaat wel termfrequentieverzadiging, maar de precieze functie en parameters horen bij het model. [SRC-013]

- Length normalization is een modelcomponent die corrigeert voor documentlengte. Het is geen advies om content tot een vaste woordlengte te schrijven. [SRC-013]

- Een co-occurrence matrix kan worden gebruikt om woordrelaties te leren, maar is niet hetzelfde als sparse retrieval of een complete relevantiescore. [SRC-016]

## Praktische toepassing voor content

1. Gebruik officiële productnamen, modelcodes, technische termen, waarden en eenheden correct en zichtbaar waar zij de gebruiker helpen.

2. Gebruik synoniemen en natuurlijke alternatieve formuleringen zonder kerntermen te verbergen.

3. Voeg bij getallen altijd variant, context, bron en voorwaarden toe.

4. Maak koppen en ankerteksten beschrijvend, maar vermijd geforceerde herhaling van dezelfde zoekterm.

5. Behandel misspellings en afkortingen alleen wanneer zij echt voorkomen en de uitleg niet onprofessioneel maken.

## Wat is niet bevestigd?

- Dat een bepaalde termdichtheid of verzadigingsscore een universele Google-rankingfactor is.

- Dat een ideale documentlengte uit BM25 of length normalization kan worden afgeleid.

- Dat moderne zoekmachines uitsluitend sparse retrieval gebruiken.

- Dat exact-matchwoorden betekenis, kwaliteit, bronvertrouwen en taakgeschiktheid vervangen.

## Veelgemaakte misvatting

“Sparse retrieval betekent dat ik het zoekwoord vaak moet herhalen.” Sparse retrieval maakt exacte termen vindbaar, maar moderne systemen en goede content vereisen ook context, betekenis, bewijs en natuurlijke taal.

## Zie ook

TF-IDF, BM25, Inverted Index, Term Frequency, Length Normalization, Dense Retrieval en Hybrid Retrieval.

## Verwante begrippen

- `IR-012`: Inverted Index
- `IR-014`: BM25
- `TERM-011C`: Dense Retrieval
- `TERM-011D`: Hybrid Retrieval
- Length Normalization *(verwant concept buiten deze begrippenlijst)*
- Term Frequency *(verwant concept buiten deze begrippenlijst)*
- TF-IDF *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-012, SRC-013, SRC-014, SRC-016, SRC-029, SRC-039, SRC-040
