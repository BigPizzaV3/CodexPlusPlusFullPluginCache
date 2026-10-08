---
term_id: TERM-002A
preferred_name_nl: Entiteitsvermelding
english_name: Entity Mention
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: NLP / informatiewinning
evidence_labels:
- B
- D
last_checked: '2026-07-25'
source_ids:
- SRC-046
- SRC-061
related_term_ids:
- TERM-002
- TERM-016E
- TERM-016F
- TERM-016G
- TERM-016H
status: active
---

# Entiteitsvermelding

**Engelse term of afkorting:** Entity Mention  
**Term-ID:** `TERM-002A`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** NLP / informatiewinning  
**Bewijsbasis:** B en D  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Een entiteitsvermelding is een woord, woordgroep of andere tekstspan die in een document naar een entiteit of discoursentiteit verwijst. Een vermelding is niet hetzelfde als de entiteit zelf en bevat niet automatisch een unieke identiteit.

## Vormen van vermeldingen

| Vermeldingstype | Voorbeeld | Mogelijke verwijzing |
| --- | --- | --- |
| Eigennaam | “For Motion On Four” | Een specifiek model of productlijn. |
| Verkorte naam | “On Four” | Dezelfde entiteit, wanneer de context duidelijk is. |
| Algemene naamwoordgroep | “de scootmobiel” | Een eerder geïntroduceerde of contextueel bepaalde entiteit. |
| Voornaamwoord | “hij”, “zij” of “dit model” | Een discoursentiteit via coreference. |
| Alias of spellingvariant | “ForMotion OnFour” | Mogelijk dezelfde entiteit, maar controle is nodig. |

Named Entity Recognition kan vermeldingen en typen herkennen. Entity Linking probeert daarna een vermelding aan een identifier in een externe of interne kennisbron te koppelen. Coreference Resolution verbindt verschillende vermeldingen binnen de tekst die naar dezelfde discoursentiteit verwijzen.

## Wat is bevestigd?

- Google Cloud Entity Analysis retourneert afzonderlijke mentions bij een representatieve entiteit en maakt daarmee het verschil zichtbaar. [SRC-061]

- Moderne NLP-standaardwerken behandelen mentiondetectie, linking en coreference als verschillende taken. [SRC-046]

- Een enkele entiteit kan in een document meerdere tekstvormen en posities hebben.

## Wat is niet bevestigd?

- Dat iedere vermelding correct aan één unieke externe entiteit kan worden gekoppeld.

- Dat dezelfde naam altijd dezelfde entiteit aanduidt.

- Dat voornaamwoorden of verkorte verwijzingen altijd goed worden opgelost.

- Dat een groter aantal vermeldingen een betere tekst of hogere ranking betekent.

## Praktische toepassing

1. Introduceer een entiteit eerst duidelijk voordat verkorte verwijzingen worden gebruikt.

2. Gebruik bij productvarianten voldoende context, bijvoorbeeld merk, model en accuconfiguratie.

3. Controleer of “dit model”, “deze accu” en vergelijkbare verwijzingen nog één duidelijke antecedent hebben.

4. Bewaar in een feitenregister de entiteit-ID, niet alleen de tekstvorm waarmee zij in één pagina wordt genoemd.

## Veelgemaakte misvatting

Iedere keer dat een productnaam voorkomt, is er een nieuwe entiteit. Het zijn meestal meerdere vermeldingen van dezelfde entiteit.

## Zie ook

Entiteit, Named Entity Recognition, Entity Linking, Entity Disambiguation en Coreference Resolution.

## Verwante begrippen

- `TERM-002`: Entiteit
- `TERM-016E`: Named Entity Recognition
- `TERM-016F`: Entity Linking
- `TERM-016G`: Entity Disambiguation
- `TERM-016H`: Coreference Resolution

## Bronnen en actualiteit

**Kernbronnen:** SRC-046, SRC-061
