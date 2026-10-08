# Workflow voor SMC Schrijversstem 1.2.0-rc.15

Dit bestand beschrijft de interne uitvoering. Geen onderdeel hiervan mag als
proces-, audit- of controletaal in de klanttekst verschijnen.

# 1. Startcontrole

Controleer:

- volledige briefing;
- werkstand en hoofdprofiel;
- onderwerp en doelgroep;
- exacte H1 en kopvolgorde;
- feiten, cijfers en eenheden;
- praktische vertalingen en vergelijkingen;
- situaties;
- diensten, voorwaarden en CTA;
- woordband.

Blokkeer bij een werkelijk ontbrekende kerninput. Vul niets aan uit algemene kennis
of voorbeeldcontent.

# 2. Splits de briefing vóór het schrijven

Maak twee interne delen.

## Positieve schrijversbrief

Neem alleen op wat zichtbaar mag worden:

- goedgekeurde feiten en cijfers;
- goedgekeurde vergelijkingen;
- toegestane praktische vertalingen;
- toegestane situaties;
- zichtbare klantgrenzen;
- toegestane diensten en handelingen;
- voorwaarden;
- CTA;
- locks en woordband.

Gebruik in deze brief geen formuleringen uit verboden claims, stille beperkingen of
negatieve voorbeelden.

## Auditnotities

Bewaar apart:

- onbekende of conflicterende gegevens;
- stille beperkingen;
- verboden claims en onderwerpen;
- bronrisico’s;
- exclusiviteitsvoorwaarden;
- service- en beschikbaarheidsgrenzen.

De schrijver gebruikt alleen de positieve schrijversbrief. De auditnotities komen
pas na het concept terug.

# 3. Controleer exclusiviteit vóór de concepttekst

Maak per model of partij een overzicht van bekende, onbekende en conflicterende
waarden.

Controleer vooraf iedere mogelijke formulering met:

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

Een rangschikking is alleen toegestaan wanneer alle benodigde waarden voor de
benoemde groep bekend zijn. Een eigenschap bij model A bewijst niet dat model B die
eigenschap mist.

# 4. Kies één gedragen hoofdgedachte

Formuleer intern in gewone taal wat de lezer na afloop vooral van het model of
onderwerp mag onthouden.

De hoofdgedachte:

- bestaat volledig uit goedgekeurde inhoud;
- bevat geen nieuwe doelgroep, emotionele opbrengst of prestatie;
- wordt in de tekst voelbaar door feiten, handeling en situatie;
- wordt niet letterlijk als `karakter`, `profiel`, `richting` of `positie` benoemd.

# 5. Verdeel uitleg over de koppen

Maak per sectie een korte, positieve inhoudsregel:

```text
kop
→ welke nieuwe betekenis hier voor het eerst volledig wordt uitgelegd
→ welke goedgekeurde feiten dat dragen
→ welke toegestane handeling of situatie erbij hoort
→ welke korte terugverwijzing later eventueel nodig is
```

Regels:

1. Geef iedere belangrijke uitleg een primaire plek; werk haar voldoende uit.
2. De opening noemt onderwerp en hoofdgedachte, maar geen volledige specificatielijst.
3. Iedere H2 heeft een eigen lezersfunctie: introduceren, verduidelijken, toepassen,
   vergelijken, verbinden of afronden, steeds binnen de briefing.
4. Een verbindende of gelockte H2 mag bekende inhoud kort samenbrengen wanneer dat
   helpt. Geen tweede specificatielijst en geen lege kop met alleen trefwoorden.
5. Een modelblok stopt wanneer de goedgekeurde inhoud voldoende is uitgelegd.
   Een nieuwe zin hoeft geen nieuw feit toe te voegen.
6. Een servicegedeelte neemt geen modelcijfers over.
7. Alleen de slotsectie voert de volledige CTA uit.
8. Een slot herhaalt geen volledige vergelijking, cijfers of handelingenreeks.

Verdeel de beschikbare inhoud bewust over de hele pagina. Gebruik niet alle feiten al
in de opening.

# 6. Volledigheid en lengte

Leg alleen werkelijk opgegeven lengtegrenzen vast. Zonder minimum blijft het
minimum leeg. Gebruik geen minimum uit een profiel, voorbeeld of eerdere test.
Behoud een opgegeven maximum. Schrijf bij een volledige tekst voldoende uitleg,
geen kunstmatig korte samenvatting en geen tekst die naar het maximum wordt gevuld.

Bij een uitdrukkelijk minimum: beoordeel eerst de dekking van verplichte onderwerpen,
toegestane praktische uitleg, situaties en vergelijkingen. Ook een bruikbare korte
terugverwijzing of afronding kan lezerswaarde hebben zonder een nieuw productfeit.
Geef zulke uitwerking ruimte, met behoud van alle inhoudelijke rechten.

Een korte eerste versie, het aantal specificaties of de telling na schrappen is
geen bewijs van onhaalbaarheid. Vul echte inhoudelijke leemten eerst in binnen de
bestaande limiet van twee verborgen reparaties. Verlaag een hard minimum niet zelf.

Alleen wanneer er een expliciet minimum is en geen verantwoorde uitwerking resteert
zonder doublures, onbewezen toevoegingen of opvulling, gebruik:

```text
BLOCKED_INSUFFICIENT_APPROVED_CONTENT_FOR_LENGTH
```

Deze status is niet beschikbaar voor een opdracht zonder minimum. Verplichte feiten,
exacte koppen, voorwaarden en overige veiligheidsblokkades blijven dan wel gelden.

# 7. Kies weinig, passende stijlankers

Gebruik bij long-form normaal:

- twee micro-evidence-items;
- maximaal één schrijversreferentie;
- geen aparte structuurreferentie tijdens de schrijverspass; het paginaprofiel en de
  koplocks bepalen de structuur.

Gebruik bij een korte tekst maximaal drie micro-evidence-items en maximaal één
schrijversreferentie.

Controleer eerst `07_REFERENCE_SPLIT.json`. Dat bestand neemt ook microherkomst mee.
Gebruik `safe_micro_example` als klantvoorbeeld; `writing_instruction` is een interne
regel en mag niet als voorbeeldzin doorlopen. Een optioneel niet-passend of ontbrekend
anker sla je over, zonder de opdracht onnodig te blokkeren.
Een bron levert nooit een nieuwe propositie. High-risk service-, lokale, regulated-
en hybridbronnen alleen als veilige stijlprojectie, niet als raw feitenbron.

# 8. Schrijf vanuit de positieve brief

## Product

Begin bij het model en één gedragen verschil. Laat eigenschappen via toegestane
handelingen en situaties leven. Houd kale technische feiten compact.

## Regulated

Zet één noodzakelijke hoofdgrens neer. Ga daarna naar dagelijkse situaties en precies
de toegestane hulp. Gebruik uitleg, geen formulier.

## Hybrid

Begin bij keuzeassen. Geef ieder model één eigen verschil en een andere
alineaontwikkeling. Cijfers bewijzen dat verschil, maar vormen niet de hele tekst.

# 9. Schrijf alinea’s die iets laten gebeuren

Een sterke alinea:

- opent met model, onderwerp of herkenbare situatie;
- legt één hoofdgedachte uit;
- gebruikt een concrete handeling wanneer die is toegestaan;
- eindigt wanneer die gedachte klaar is.

Gebruik `je` vooral in zinnen waarin de lezer iets doet of merkt.

Gebruik opdrachten als `meet`, `schrijf op`, `kijk`, `vergelijk`, `bepaal` en `neem
mee` alleen wanneer ze werkelijk nodig zijn. Drie opdrachten in één korte alinea zijn
een alarmsignaal.

# 10. Vermijd uitleg over informatie zelf

Een klantzin moet informatie geven over:

- het model;
- de handeling;
- de situatie;
- de dienst;
- de toegestane vervolgstap.

Verwijder een zin wanneer zij alleen uitlegt:

- dat twee gegevens verschillend zijn;
- dat ieder cijfer een eigen eenheid heeft;
- dat onderdelen ieder een eigen functie hebben;
- dat informatie bij elkaar komt;
- dat een model een eigen plaats, rol of profiel heeft;
- dat een vergelijking uit meerdere punten bestaat;
- dat een feit in een bepaalde sectie centraal staat.

Een nuttige test:

```text
Als modelnamen en cijfers uit de zin verdwijnen, blijft er dan alleen een uitspraak
over de opbouw van de tekst over?
```

Zo ja, verwijder of herschrijf de zin.

# 11. Controleer alinea’s op hun bijdrage aan het begrip

Vraag per alinea: wat begrijpt de lezer hier beter of waarvoor heeft hij deze
verwijzing hier nodig?

Behoud een alinea wanneer zij goedgekeurde informatie introduceert, verduidelijkt,
in een al toegestane situatie toepast, een toegestane vergelijking uitlegt of een
gedachte afrondt. Een korte terugverwijzing mag ook samenhang geven. Geen nieuwe
specificatie per zin eisen. Geen minimumaantal zinnen of alinea’s afdwingen.

Schrap een doublure wanneer boodschap én lezersfunctie al zijn vervuld. Schrap
volledige modelrecaps, een tweede rolverklaring zonder nieuwe functie, een tweede
identieke maatberekening en uitleg over de indeling van informatie. Behoud een
korte herneming wanneer daarmee een werkelijk ander, goedgekeurd punt duidelijk wordt.

Controleer na het schrappen per kop: welke vraag of verwachting staat hier, en welke
zin of alinea geeft daarop antwoord? Alleen passende trefwoorden of resterende
specificaties zijn onvoldoende. Een verbindende kop mag een kort verband tussen
bekende eigenschappen leggen. Houd exacte koppen vast en verzin geen inhoud als het
antwoord ontbreekt. Maak een passage niet langer omdat hij kort is.

Controleer de laatste zin van ieder onderdeel: geeft die extra begrip, een vereiste
grens, samenhang of een vervolgstap? Zo niet, dan mag het onderdeel stoppen zonder
samenvattende slotzin. Behoud nuttige definities, een onderbouwd reviewoordeel en
voorwaardelijke terugverwijzingen. Een nieuwe specificatie per zin blijft geen eis.

# 12. Controleer secties over de hele pagina

Na de alinea-edit:

- iedere sectie heeft een eigen bijdrage aan het begrip van de lezer;
- geen sectie bestaat grotendeels uit callbacks;
- geen modelblok eindigt met een recap;
- service bevat geen producttabel;
- het slot is geen tweede serviceblok of tweede CTA;
- de tweede helft blijft even specifiek als de opening.

Een gelockte of verbindende sectie mag een korte, nuttige samenhang of afronding
geven met bekende inhoud. Niet iedere sectie hoeft een nieuwe specificatie te bevatten.

# 13. Beschikbaarheid en service

Een specifiek model mag niet als aanwezig, te bekijken of te rijden worden
gepresenteerd vóór de vereiste aanwezigheidsvoorwaarde.

- Zet de voorwaarde één keer volledig in het servicegedeelte.
- Beschrijf daarna alleen de geautoriseerde handelingen.
- Voeg geen adviseur, tijd, aandacht, uitleg, begeleiding, gratis of vrijblijvend toe
  zonder expliciete briefingsteun.
- Een korte callback van de voorwaarde in de CTA mag alleen wanneer de CTA anders
  misleidend wordt.

# 14. Eén CTA

Markeer alle zinnen die uitnodigen, een afspraak voorstellen of een vervolgstap
uitvoeren.

- Exact één sectie voert de volledige CTA uit.
- Een eerder servicegedeelte beschrijft alleen wat mogelijk is.
- Het slot herhaalt niet opnieuw de volledige handelingenreeks.
- Verplichte vergelijkpunten mogen compact terugkomen.

# 15. Herschrijf formele en abstracte taal

Vervang waar mogelijk:

- passieve constructies door direct onderwerp en werkwoord;
- algemene woorden als `gegevens`, `onderdelen`, `uitgangspunt`, `rol`, `positie` en
  `functie` door de concrete inhoud;
- classificatiezinnen door een echte handeling of een kort feit;
- een technische recap door één natuurlijke afsluitzin of niets.

Voorbeelden als principe:

```text
De breedte bedraagt 72 cm. → Het model is 72 cm breed.
De bijdrage bestaat uit algemene uitleg. → SMC geeft algemene uitleg.
De twee cijfers hebben ieder een eigen functie. → Verwijder, tenzij een nieuwe
briefinggedragen betekenis overblijft.
```

# 16. Voer de auditnotities pas nu uit

Controleer iedere inhoudelijke uitspraak, ook in bijzinnen.

Toegestane steun:

- goedgekeurd feit of cijfer;
- toegestane vertaling;
- goedgekeurde vergelijking;
- geautoriseerde situatie;
- zichtbare klantgrens;
- geautoriseerde dienst of CTA;
- neutrale verbinding zonder nieuwe betekenis.

Versmal of verwijder ieder niet-gedragen deel.

Controleer brontransfer, scenario’s, service, adviseursgedrag, processen en
beschikbaarheid.

Iedere zichtbare ontkenning moet een vereiste klantgrens of goedgekeurd contrast
uitvoeren. Een ontkenning die alleen een stille beperking uitlegt, wordt verwijderd.

# 17. Laatste exclusiviteitscontrole

Scan opnieuw op woorden als `alleen`, `enige`, `als enige`, `uniek`, `grootste`,
`kleinste`, `hoogste`, `laagste` en `snelste`.

Controleer de volledige vergelijkingsgroep. Onbekend is niet hetzelfde als afwezig.

# 18. Laatste tel- en kwaliteitsronde

Tel met:

```text
VISIBLE_LEXICAL_WORDS_INCLUDING_HEADINGS
```

Controleer:

- feiten, cijfers en locks;
- briefingsteun per betekenis;
- bronfirewall;
- exclusiviteit;
- zichtbare klantgrenzen;
- voldoende uitgewerkte onderdelen zonder doublures met dezelfde lezersfunctie;
- geen uitleg over eenheden of tekstopbouw;
- beschikbaarheidsvoorwaarde;
- exact één CTA;
- tweede helft;
- woordband;
- bronkopie;
- systeemtaal;
- natuurlijke SMC/IVA-stem.

Voer maximaal twee verborgen reparaties uit. Breng geschrapte inhoud niet terug om
lengte te winnen.

# 19. BEOORDELEN en HERSTELLEN

Beoordeel in deze volgorde:

1. locks en woordtelling;
2. feiten en zichtbare betekenissen;
3. scenario, service en beschikbaarheid;
4. exclusiviteit;
5. nuttige uitwerking tegenover overbodige herhaling over de hele tekst;
6. uitleg over eenheden, categorieën of tekstopbouw;
7. CTA;
8. profiel, stem, tweede helft en slot;
9. status van de bronnen: open kalibratie of aantoonbaar onafhankelijke toetsing.

Rapporteer de feitelijke laadgeschiedenis alleen voor zover bekend. Alle indirecte
bronherkomst telt mee. Een correcte tekst kan een opdracht-PASS krijgen zonder dat
daarmee onafhankelijke auteursvalidatie is bewezen. Gebruik de huidige bestaande
bronreferenties als open kalibratie, niet als onaangeroerd holdoutmateriaal.

Bij herstellen blijft een register bij van sterke passages, fouten, verboden
herintroducties, ongebruikte goedgekeurde inhoud en woordband. Haal de volledige
tekst na iedere wijziging opnieuw door stap 11 tot en met 18.
