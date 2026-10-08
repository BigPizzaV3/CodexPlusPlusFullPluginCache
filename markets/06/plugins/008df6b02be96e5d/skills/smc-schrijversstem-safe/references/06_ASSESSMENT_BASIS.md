# 06 — Beoordelingsbasis 1.2.0-rc.13

Gebruik dit bestand uitsluitend in `BEOORDELEN` en bij de eindcontrole van
`FULL_VISIBLE_COPY_AFTER_PATCH`. Het is geen schrijfprompt. Historische fouten
voorspellen nooit welke fout in een nieuwe tekst aanwezig moet zijn.

## 1. Benodigde invoer

Beoordeel alleen wanneer beschikbaar zijn:

- de volledige oorspronkelijke briefing;
- de exact aangewezen volledige zichtbare tekst;
- het juiste paginaprofiel;
- beschikbare beoordelingsreferenties met hun kalibratie- of geverifieerde toetsstatus;
- de vastgelegde woordtelmethode.

Controleer voor stemvergelijking de volledige herkomst in `07_REFERENCE_SPLIT.json`,
ook microvoorbeelden, projecties en eerdere regelafleiding. De bestaande referenties
zijn open kalibratie, geen geverifieerde onafhankelijke holdout. Ontbrekende
onafhankelijkheid verhindert geen volledige toets tegen de briefing. Voer geen
`HERSTELLEN` uit en schrijf geen vervangende pagina.

## 2. Eerst de harde opdracht

Controleer vóór de schrijversstem:

- exacte H1 en verplichte H2’s, plus het antwoord dat de inhoud op iedere kop geeft;
- kopvolgorde;
- woordband;
- verplichte inhoud;
- verboden onderwerpen en claims;
- voorwaarden;
- rollen;
- CTA- en servicerechten;
- profielspecifieke locks.

Maak onderscheid tussen:

- mechanisch gecontroleerd;
- inhoudelijk gelezen;
- niet vast te stellen.

Niet vast te stellen is nooit automatisch PASS.

### Volledigheid en lengte

Een ontbrekend minimum is geen ontbrekende kerninput en wordt niet zelf ingevuld.
Beoordeel zonder minimum of de tekst volledig en voldoende uitgewerkt is binnen een
opgegeven maximum. Korter dan een vorige test is geen lengtefout; kaal of onvolledig
kan wel een redactioneel probleem zijn.

Een expliciet minimum blijft bindend. Een korte versie of blokkade bewijst niet dat
dit minimum onmogelijk is. Verlang onderbouwing vanuit ontbrekende toegestane
uitwerking, niet alleen een telling. Een hertest zonder minimum vervangt nooit de
uitslag van de oorspronkelijke lengteopdracht.

## 3. Beoordeel iedere zichtbare betekenis

Een zin kan meerdere inhoudelijke uitspraken bevatten. Beoordeel daarom ook de
betekenis in:

- hoofdzin;
- bijzin;
- voorbeeld;
- ontkenning;
- vergelijking;
- oorzaak-gevolgverbinding;
- service- of procesformulering.

Een betekenis mag alleen zichtbaar zijn wanneer zij rechtstreeks wordt gedragen door:

```text
APPROVED_FACT
APPROVED_NUMBER
EXPLICIT_PRACTICAL_TRANSLATION
APPROVED_COMPARISON
AUTHORIZED_SCENARIO
REQUIRED_VISIBLE_BOUNDARY
AUTHORIZED_SERVICE_OR_CTA
STYLE_ONLY_NO_NEW_MEANING
```

`STYLE_ONLY_NO_NEW_MEANING` mag alleen neutrale verbindende taal dragen.

## 4. Primaire classificaties

Gebruik per grondbevinding exact één primaire classificatie:

- `AANTOONBAAR_ONJUIST`;
- `NIET_GEGEVEN`;
- `BUITEN_TOEGESTANE_VERTALING`;
- `DUBBELZINNIG`;
- `UNSUPPORTED_VISIBLE_PROPOSITION`;
- `UNAUTHORIZED_SCENARIO`;
- `UNAUTHORIZED_SERVICE_PROPOSITION`;
- `SOURCE_PROPOSITION_TRANSFER`;
- `PROMPT_VISIBILITY_ERROR`;
- `INTERNE_REDENEERLEK`;
- `ZICHTBARE_VERTALINGSREGEL`;
- `ZICHTBARE_STILLE_UITSLUITING`;
- `BETEKENISHERHALING`;
- `GLOBAL_SINGLE_USE_VIOLATION`;
- `META_PROSE`;
- `UNIT_OR_CATEGORY_FILLER`;
- `EXCLUSIVITY_FROM_UNKNOWN`;
- `CHECKLIST_DRIFT`;
- `BESCHIKBAARHEIDSVOORWAARDE_FOUT`;
- `DUBBELE_CTA`;
- `MODELBLOK_RECAP`;
- `STILISTISCH_ZWAK`.

Gebruik de meest specifieke classificatie. Tel dezelfde grondfout één keer, ook
wanneer zij op meerdere plekken zichtbaar is.

### `GLOBAL_SINGLE_USE_VIOLATION`

Gebruik alleen wanneer dezelfde boodschap met dezelfde lezersfunctie over
meerdere alinea’s of secties opnieuw volledig wordt uitgelegd. Toon de eerdere en
latere passage. Een nieuwe specificatie per zin is geen eis. Ondersteunde
verduidelijking, toepassing of een korte functionele terugverwijzing is niet op
zichzelf een overtreding.

### `META_PROSE`

Gebruik wanneer een zin vooral beschrijft:

- hoe feiten zijn geordend;
- welke rol, plaats, functie, positie of richting iets in de tekst heeft;
- dat gegevens samen een geheel of profiel vormen;
- dat punten afzonderlijk worden bekeken;
- hoe de vergelijking is opgebouwd.

### `UNIT_OR_CATEGORY_FILLER`

Gebruik wanneer de tekst zonder klantwaarde uitlegt:

- dat snelheid in km/u staat;
- dat vermogen in watt staat;
- dat bereik in kilometer staat;
- dat breedte en draaicirkel verschillende maten zijn;
- dat mand en USB verschillende functies hebben;
- andere vanzelfsprekende categorie-indelingen.

### `EXCLUSIVITY_FROM_UNKNOWN`

Gebruik wanneer een exclusieve formulering wordt afgeleid uit ontbrekende informatie
bij andere modellen of partijen.

Voorbeelden:

- `als enige twee zitplaatsen`, terwijl peer-zitplaatsen onbekend zijn;
- `alleen dit model heeft een mand`, terwijl de andere modellen daarop niet zijn
  beschreven;
- `uniek`, zonder volledige vergelijkingsbasis.

### `CHECKLIST_DRIFT`

Gebruik wanneer een gereguleerde, advies- of servicepagina vooral een reeks
opdrachten en invulstappen wordt, terwijl vloeiende uitleg was gevraagd.

## 5. Globale eenmaligheidscontrole

Maak een compacte lijst van de hoofdbetekenissen in de tekst.

Controleer per betekenis:

- waar zij voor het eerst volledig wordt uitgelegd;
- of zij later alleen kort en noodzakelijk terugkomt;
- of een latere alinea dezelfde betekenis opnieuw opbouwt;
- of een slot opnieuw alle feiten of handelingen groepeert.

Bekijk na de alinea-edit afzonderlijk kop en laatste zin. Een correcte kop met alleen
losse cijfers kan zijn belofte missen. Een slotzin die de uitleg alleen opnieuw
benoemt kan vervallen. Benoem dit concreet als redactioneel punt; behoud verplichte
inhoud, nuttige definities, korte verbindingen en een onderbouwd reviewoordeel.

Een andere formulering maakt een betekenis niet nieuw. Omgekeerd is dezelfde
feitverwijzing niet automatisch een doublure. Benoem wat de latere passage voor
begrip, toepassing, samenhang of afronding toevoegt. Keur niet alleen op gelijke
woorden, cijfers of afwezigheid van nieuwe specificaties af.

## 6. Exclusiviteitscontrole

Scan iedere formulering met:

- alleen;
- enige;
- uitsluitend;
- als enige;
- uniek;
- grootste;
- kleinste;
- hoogste;
- laagste;
- snelste.

Controleer alle relevante waarden en eigenschappen binnen de genoemde groep.
Onbekend is niet hetzelfde als afwezig.

## 7. Bron- en servicefirewall

Controleer dat geen stijlbron nieuwe inhoud heeft geleverd, waaronder:

- productfeit;
- scenario;
- emotionele opbrengst;
- doelgroep;
- service;
- tijd of aandacht;
- adviseursgedrag;
- aantal modellen;
- gratis of vrijblijvend;
- afstellen;
- levering of beschikbaarheid;
- Wmo-, juridische of medische procesinformatie;
- reviewervaring.

## 8. Schrijversstem

Beoordeel daarna:

- directe opening;
- model- of onderwerpsbeeld;
- concrete handelingen;
- gedachteontwikkeling;
- menselijke houding;
- ritme;
- vraag- en opdrachtendichtheid;
- tweede helft;
- slot en CTA.

Een tekst kan feitelijk correct en toch onvoldoende als SMC/IVA-schrijver zijn.

## 9. Bronzekerheid

Gebruik:

```text
HIGH
MEDIUM
LOW
```

Vermeld waarop de bronzekerheid berust, niet alleen het profiel. Directe productbronnen
zijn rijker vertegenwoordigd dan sommige andere genres. Een laag bronrisico of hoge
stijlovereenkomst bewijst geen onafhankelijkheid. Vermeld afzonderlijk:

- `OPEN_CALIBRATION` voor de bestaande referenties;
- `VERIFIED_INDEPENDENT` uitsluitend met aantoonbare afscherming en herkomst;
- `NOT_ESTABLISHED` als het gebruiksverleden niet is vastgesteld.

Het huidige pakket heeft geen geverifieerde onafhankelijke holdout. Een opdracht-PASS
is geen blinde menselijke goedkeuring, stabiele release of garantie voor alle teksten.

## 10. Eindstatus

Gebruik exact één:

```text
PASS
PASS MET VERBETERPUNTEN
FAIL
```

Een harde fout geeft altijd `FAIL`. Een score compenseert geen harde fout.
