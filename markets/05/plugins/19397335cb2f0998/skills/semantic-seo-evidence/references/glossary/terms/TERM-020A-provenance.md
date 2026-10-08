---
term_id: TERM-020A
preferred_name_nl: Provenance
english_name: Provenance
cluster_id: 1
cluster_name: Basis, entiteiten en kennisstructuren
type_context: Open standaard / herkomst- en verantwoordelijkheidsinformatie
evidence_labels:
- A
last_checked: '2026-07-25'
source_ids:
- SRC-077
- SRC-078
related_term_ids:
- GOV-011
- QLT-021
- TERM-020
status: active
---

# Provenance

**Engelse term of afkorting:** Provenance  
**Term-ID:** `TERM-020A`  
**Hoofdcategorie:** 1 Basis, entiteiten en kennisstructuren  
**Type en context:** Open standaard / herkomst- en verantwoordelijkheidsinformatie  
**Bewijsbasis:** A  
**Laatst gecontroleerd:** 25 juli 2026

## Kerndefinitie

Provenance is informatie over de entiteiten, activiteiten en verantwoordelijke personen of organisaties die betrokken waren bij het maken, beïnvloeden, afleiden, wijzigen of leveren van een gegeven, claim, document, afbeelding of ander informatieobject.

## Formele basis

W3C PROV-DM definieert provenance als informatie over entiteiten, activiteiten en mensen die betrokken zijn bij het produceren van data of een ander object. Die informatie kan worden gebruikt bij de beoordeling van kwaliteit, betrouwbaarheid en vertrouwen. [SRC-077]

PROV-O biedt een OWL-ontologie om provenance uit te wisselen. De kern bestaat onder meer uit Entity, Activity en Agent, met relaties voor generatie, gebruik, afleiding, toeschrijving, revisie en primaire bron. [SRC-078]

Provenance is breder dan een bronvermelding. Een link kan vertellen waar informatie staat; provenance kan ook vastleggen wie mat, met welke methode, wanneer, op basis van welke eerdere gegevens en welke versie is gepubliceerd.

## Kernonderdelen

- Entity: het gegeven, document, beeld, productrecord of de claim.

- Activity: de test, meting, redactie, berekening, revisie of publicatiehandeling.

- Agent: de persoon, organisatie of software die verantwoordelijkheid draagt of betrokken was.

- Derivation: van welk eerder informatieobject iets is afgeleid.

- Attribution: aan wie het object of resultaat wordt toegeschreven.

- Primary source: de oorspronkelijke bron met directe ervaring of kennis, binnen de conventies van het vakgebied.

- Revision en tijd: welke versie is aangepast, wanneer en waarom.

## Wat provenance niet bewijst

- Provenance maakt herkomst controleerbaar, maar bewijst niet automatisch dat een claim waar, volledig of onbevooroordeeld is.

- Een primaire bron kan fouten bevatten. Een fabrikant kan de juiste bron voor een technische specificatie zijn en tegelijk een commercieel belang hebben.

- Een AI-citatie of hyperlink is niet hetzelfde als een volledige provenanceketen.

## Praktische toepassing

1. Geef iedere belangrijke claim een Claim-ID en koppel die aan een bron, methode, datum, verantwoordelijke en toepassingsvoorwaarden.

2. Bewaar revisies en noteer welke pagina’s een claim gebruiken.

3. Leg voor eigen tests vast welk model, welke uitvoering, accu, route, temperatuur, bestuurder en meetmethode zijn gebruikt.

4. Noteer bronconflicten en geef aan waarom één bron voor een bepaalde claim zwaarder weegt dan een andere.

5. Gebruik provenance als basis voor correcties, updates, hergebruik en controle door mensen en systemen.

## Praktijkvoorbeeld

| PROV-onderdeel | Voorbeeld bij een actieradiustest | Vast te leggen |
| --- | --- | --- |
| Entity | Testresultaat van model X | Claim-ID, waarde, eenheid en uitvoering. |
| Activity | Praktijktest op vaste route | Methode, datum, temperatuur, snelheid en meetapparatuur. |
| Agent | Tester en controlerende productexpert | Naam, rol en verantwoordelijkheid. |
| Primary source | Ruwe meetgegevens en acculog | Bestandslocatie, versie en toegangsdatum. |
| Derivation | Samenvatting in artikel en video | Welke publicaties van het meetrecord zijn afgeleid. |
| Revision | Nieuwe test met andere accu | Versienummer, wijzigingsreden en vervangen waarde. |

## Veelgemaakte misvatting

Een bronlink onderaan de pagina is volledige provenance. Een bruikbare herkomstregistratie koppelt de concrete claim ook aan methode, agent, datum, versie en voorwaarden.

## Zie ook

- Source Context

- Primary Source

- Derivation

- Revision

- Evidence ledger

- Claim-ID

- Data Quality

## Verwante begrippen

- `GOV-011`: Primary Source
- `QLT-021`: Data Quality
- `TERM-020`: Source Context
- Claim-ID *(verwant concept buiten deze begrippenlijst)*
- Derivation *(verwant concept buiten deze begrippenlijst)*
- Evidence ledger *(verwant concept buiten deze begrippenlijst)*
- Revision *(verwant concept buiten deze begrippenlijst)*

## Bronnen en actualiteit

**Kernbronnen:** SRC-077, SRC-078
