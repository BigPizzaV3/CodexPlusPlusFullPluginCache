---
term_id: TERM-016H
preferred_name_nl: Coreference Resolution
english_name: Coreference Resolution
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Discourse-analyse en entiteitsverwijzingen
evidence_labels:
- D
last_checked: '2026-07-25'
source_ids:
- SRC-046
- SRC-053
related_term_ids:
- TERM-016E
- TERM-016F
- TERM-016G
- TERM-020
status: active
---

# Coreference Resolution

**Engelse term of afkorting:** Coreference Resolution  
**Term-ID:** `TERM-016H`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Discourse-analyse en entiteitsverwijzingen  
**Bewijsbasis:** D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Kerndefinitie: Coreference resolution is het vaststellen welke tekstvermeldingen binnen een tekst of gesprek naar dezelfde discoursentiteit verwijzen.

## Uitgebreide uitleg

Een entiteit kan in een tekst met een eigennaam, zelfstandig naamwoord, beschrijving of voornaamwoord worden genoemd. Coreference resolution groepeert mentions die naar dezelfde persoon, organisatie, productvariant of ander discoursobject verwijzen.

Het begrip is breder dan alleen voornaamwoorden. “De On Four”, “dit model”, “de vierwieler” en “de scootmobiel” kunnen in één passage naar dezelfde entiteit verwijzen.

Coreferentie is niet hetzelfde als entity linking. Een systeem kan begrijpen dat meerdere mentions bij elkaar horen zonder te weten welke externe knowledge-base-ID daarbij hoort.

Lange afstanden, meerdere vergelijkbare producten, meervoudige verwijzingen en onduidelijke voornaamwoorden maken coreferentie moeilijker. Een fout kan eigenschappen aan de verkeerde variant koppelen.

## Voorbeeld

Voorbeeldtekst: “De On Four heeft een draaibare stoel. Dit model kan met verschillende accupakketten worden geleverd. De uitvoering met het grootste pakket heeft andere bereikvoorwaarden.”

| Mention | Waarschijnlijke referent | Opmerking |
| --- | --- | --- |
| De On Four | productmodel On Four | volledige eerste vermelding |
| Dit model | dezelfde On Four | anaforische verwijzing |
| De uitvoering met het grootste pakket | specifieke variant van de On Four | niet automatisch gelijk aan iedere uitvoering |

| Notitie: De derde mention versmalt de referent naar een variant. Een feitenregister moet dit verschil behouden. |
| --- |

## Wat is bevestigd?

- Coreferentiemodellen kunnen mentions en antecedenten binnen documenten clusteren.

- Voornaamwoorden, beschrijvingen en namen kunnen naar dezelfde discoursentiteit verwijzen.

- Coreferentie kan worden opgelost zonder externe entity linking.

## Wat is niet bevestigd?

- Een taalmodel lost iedere lange of complexe verwijzing foutloos op.

- Exacte herhaling van de productnaam in iedere zin is nodig voor begrip.

- Coreferentie maakt onduidelijke variantclaims veilig of feitelijk correct.

## Praktische toepassing

- Gebruik natuurlijke verwijzingen, maar herintroduceer de volledige naam wanneer meerdere modellen of varianten in dezelfde sectie voorkomen.

- Plaats belangrijke waarden dicht bij de exacte variant waarop zij betrekking hebben.

- Vermijd “deze”, “die” of “hij” wanneer meerdere mogelijke antecedenten aanwezig zijn.

- Controleer vergelijkingen en tabellen extra op verschuivende referenten.

## Veelgemaakte misvatting

| Belangrijke begrenzing: Voor zoekmachines moet de volledige entiteitsnaam in iedere zin worden herhaald. Duidelijke coreferentie kan natuurlijke variatie toelaten, terwijl overdreven herhaling de leesbaarheid verslechtert. |
| --- |

## Zie ook

TERM-016E Named Entity Recognition, TERM-016F Entity Linking, TERM-016G Entity Disambiguation, TERM-020 Primaire entiteit.

## Verwante begrippen

- `TERM-016E`: Named Entity Recognition
- `TERM-016F`: Entity Linking
- `TERM-016G`: Entity Disambiguation
- `TERM-020`: Source Context

## Bronnen en actualiteit

**Kernbronnen:** SRC-046, SRC-053
