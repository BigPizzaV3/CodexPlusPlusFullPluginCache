# 02 — Bron- en stijlbeleid 1.2.0-rc.13

## 1. Hoofdregel

De actuele briefing bepaalt alle zichtbare inhoud.

Stijlbronnen bepalen alleen:

- toon;
- ritme;
- gedachtebeweging;
- directheid;
- alineaontwikkeling;
- profielopbouw;
- de manier waarop toegestane inhoud menselijk wordt uitgelegd.

Geen stijlbron is een feiten-, scenario-, service-, proces- of beloftebron voor een
nieuwe tekst.

## 2. Positieve schrijversbrief en audit blijven gescheiden

De writer schrijft alleen vanuit een intern opgeschoonde positieve brief met:

- feiten;
- toegestane vertalingen;
- toegestane situaties;
- toegestane diensten;
- zichtbare grenzen;
- locks;
- CTA;
- woordband.

Verboden voorbeeldzinnen, historische fouten en auditformuleringen worden niet als
schrijfmateriaal aan de writer aangeboden. Zij worden pas bij de eindcontrole
gebruikt.

Dit moet voorkomen dat een negatieve formulering uit de briefing of voorbeeldenbank in de
klanttekst wordt teruggekopieerd.

## 3. Het oorspronkelijke archief blijft provenance

Het volledige IVA/SMC-archief blijft ongewijzigd als provenance. Het bevat:

- sterke schrijversvoorbeelden;
- oude en nieuwe redactielagen;
- dubbelen;
- taalfouten;
- overclaims;
- tijdgevoelige regels;
- servicebeloften;
- medische en juridische risico’s;
- zoekwoord- en redactienotities.

Die aanwezigheid maakt een passage nog niet geschikt voor de writer.

De runtime gebruikt alleen:

- 74 gecureerde micro-evidence-items;
- 29 gecureerde bronreferenties met een veilige writer-weergave;
- profielregels;
- beoordelingsregels.

## 4. Bronnenlagen

### Laag A

Sterke positieve bron voor stem en gedachtebeweging.

Gebruik voor:

- directheid;
- ritme;
- langere gedachtebogen;
- concrete uitleg;
- menselijke houding;
- feitelijk gedragen energie.

### Laag B

Ondersteunende bron voor:

- paginatype;
- asymmetrie;
- overgang;
- aanvullende toon.

### Laag C

Risicovolle of negatieve bron.

Gebruik uitsluitend voor:

- foutdetectie;
- bronkopiecontrole;
- verouderde SEO-formules;
- onveilige claims;
- juridische, medische en tijdgevoelige risico’s;
- taalfouten;
- systeem- en redactietaal.

Een C-bron levert nooit positieve schrijverszinnen.

## 5. Writer-weergaven

Gebruik exact één van deze standen:

### `RAW_STYLE_REFERENCE`

Een zorgvuldig geselecteerde passage uit een sterke bronlaag mag de productwriter
sturen.

Ook dan geldt:

- feiten en claims zijn niet overdraagbaar;
- scenario’s zijn niet overdraagbaar;
- alleen vorm, beweging en ritme mogen sturen.

### `SAFE_STYLE_PROJECTION`

De writer ziet alleen een korte factvrije beschrijving van:

- gedachtebeweging;
- ritme;
- menselijke houding;
- alineaopbouw.

Gebruik deze stand voor bronnen met risico op service, Wmo, juridische inhoud,
prijzen, concrete scenario’s, medische claims of veiligheidsclaims.

### `STRUCTURE_ONLY`

Alleen toegestaan buiten de writer-first route wanneer een profiel zonder die
structuur niet kan worden uitgevoerd. Tijdens schrijven is deze stand in de huidige laadroute uitgeschakeld.

### `ASSESSMENT_ONLY`

Alleen bij `BEOORDELEN`.

### `NEGATIVE_ONLY`

Alleen na het eerste concept bij de audit. Nooit als positieve schrijversbron.

## 6. Volledige bronpropositie-firewall

Iedere bronpassage wordt gelabeld op risico.

Mogelijke risicocategorieën:

```text
PRODUCT_SPECIFICATION
PRODUCT_PERFORMANCE
PRACTICAL_CONSEQUENCE
USER_SUITABILITY
DAILY_SCENARIO
EMOTIONAL_OUTCOME
SERVICE_AVAILABILITY
SERVICE_PROMISE
ADVISOR_BEHAVIOR
NUMBER_OF_MODELS_OR_OPTIONS
FREE_OR_NO_OBLIGATION
PRICE_OR_DISCOUNT
DELIVERY_OR_TIMING
LEGAL_OR_WMO_PROCESS
MEDICAL_OR_SAFETY
REVIEW_OR_TEST_EXPERIENCE
MARKET_WIDE_COMPARISON
```

Deze proposities zijn standaard niet overdraagbaar.

## 7. Wat wel mag worden overgenomen

Alleen vorm:

```text
sentence_movement
paragraph_movement
rhythm
directness
perspective
transition_style
concrete_explanation_method
```

Niet overdraagbaar:

- een nieuw zelfstandig naamwoord, werkwoord of bijvoeglijk woord dat een claim
  vormt;
- een concreet voorbeeld uit de bron;
- een servicehandeling;
- een emotionele uitkomst;
- een doelgroep;
- een processtap;
- een rangschikking;
- een praktijkervaring.

## 8. Service- en adviseursfirewall

Zonder expliciete briefingsteun mogen nooit uit een stijlbron worden toegevoegd:

- alle tijd nemen;
- persoonlijk meekijken;
- vragen beantwoorden;
- meerdere modellen meenemen of klaarzetten;
- gratis;
- vrijblijvend;
- afstellen;
- aanpassen;
- thuis komen;
- reserveren;
- automatische beschikbaarheid;
- levertijd;
- begeleiding;
- ontzorging.

Een actieve afzender mag alleen een handeling uitvoeren die in de briefing is
toegestaan.

## 9. Scenariofirewall

Een scenario is zichtbare inhoud.

Niet automatisch overdraagbaar:

- boodschappen;
- familiebezoek;
- school;
- vereniging;
- oprit;
- stoep;
- slecht weer;
- vakantie;
- lange tocht;
- stadsverkeer;
- winkelen.

Een scenario mag alleen worden gebruikt wanneer de briefing het expliciet noemt of
wanneer het onmiskenbaar onderdeel is van een toegestane praktische vertaling.

## 10. Selectieregels voor UITSCHRIJVEN

Gebruik bij long-form normaal:

- maximaal twee micro-evidence-items;
- maximaal één writerreferentie;
- voor `product`, `regulated` en `hybrid` geen aparte structuurreferentie;
- nooit een negatieve of assessmentreferentie.

Gebruik bij korte tekst maximaal drie micro-evidence-items en maximaal één
writerreferentie.

Selecteer alleen referenties die:

- bij het hoofdprofiel passen;
- een toegestane writer-weergave hebben;
- volgens `07_REFERENCE_SPLIT.json` voor de schrijversrol zijn toegestaan;
- geen holdout zijn;
- geen waarschijnlijk feitvermengingsrisico met hetzelfde model hebben.

Voor product mag één sterke raw style reference worden gebruikt.

Voor regulated en high-risk onderdelen heeft een veilige stijlprojectie voorrang.

Voor hybrid stuurt één passende productwriterreferentie de modelalinea’s. De
asymmetrie en serviceopbouw komen uit het profiel, niet uit een aparte
structuurreferentie.

## 11. Voorwaardelijk laden

Een service- of lokale referentie wordt alleen geladen wanneer de briefing werkelijk
een service- of lokale sectie toestaat. Voor product, regulated en hybrid is zo’n
referentie standaard niet nodig.

Ook met een servicebriefing mag de bron geen extra dienst autoriseren.

## 12. Volledige bronherkomst en eerlijke beoordeling

`07_REFERENCE_SPLIT.json` is de gezamenlijke bronindeling. Reken mee: oorspronkelijke
passages, veilige projecties, structuurafleidingen, microvoorbeelden en historische
regelafleiding. Een andere bronfamilie dan het geladen raw fragment is daarom niet
vanzelf onafhankelijk. Een heel gelezen catalogusbestand telt conservatief als
mogelijke blootstelling aan alle families in dat bestand.

Bestaande beoordelingsbronnen blijven alleen voor open kalibratie na het concept.
Zij mogen de writer niet sturen, maar worden niet als onaangeroerde holdout geteld.
De historische overlap is zichtbaar bewaard. Geen familie wordt achteraf simpelweg
hernoemd om eerdere beoordelingen onafhankelijk te verklaren. De bundel bevat nu
geen geverifieerde onafhankelijke auteursholdout. De rolverdeling is instructie,
geen technische afscherming van bestandstoegang.

Gebruik het beperkte materiaal wel om concrete tekstverschillen te bespreken.
Beoordeel de harde briefing volledig. Ontbrekende onafhankelijke evidence is geen
reden om schrijven te blokkeren en geen automatische FAIL voor een correcte tekst.
Meld bij beoordeling de bronstatus en de beperkte zekerheid van een auteursmatch.
Nieuwe evaluatie-input mag pas onafhankelijk heten wanneer herkomst, gebruiksverleden,
versie en afwezigheid uit writerinput en regelafleiding aantoonbaar zijn. Een blinde
menselijke beoordeling wordt alleen als zodanig genoemd als die werkelijk plaatsvond.

### Klantvoorbeeld en interne aanwijzing

`safe_micro_example` bevat uitsluitend een synthetisch klantvoorbeeld met placeholders,
geen letterlijk citaat van de oorspronkelijke auteur. `writing_instruction` en de
andere regelvelden beschrijven hoe de schrijver werkt; zij zijn geen klanttekst.
Oude bronverwijzingen blijven de herkomst van de afleiding tonen. Een nieuw geformuleerd
voorbeeld is niet door alleen een oud goedkeuringslabel menselijk goedgekeurd.

Iedere placeholder en iedere relatie in een voorbeeld vereist briefingsteun. Een
voorbeeld kan geen verplicht nieuw scenario, bedrag, waarschuwing, citaat, dienst of
CTA aan een opdracht toevoegen. Sla een niet-passend voorbeeld over. Negatieve
voorbeeldzinnen blijven voor de controle na het concept, niet voor de schrijfstem.
Laag-C-herkomst mag uitsluitend herleidbare abstracte structuur begeleiden; geen
letterlijke C-bronzinnen als positief auteursbewijs. Zulke synthetische patronen
bewijzen geen sterke of onafhankelijke auteursmatch.

## 13. Bronkopie

Blokkeer:

- lange letterlijke overlap;
- dezelfde bijzondere beeldspraak;
- alleen modelnaam of cijfer vervangen;
- lichte parafrase met dezelfde herkenbare zin;
- dezelfde complete alinea-opbouw;
- bronpropositie die niet in de briefing staat.

Gewone woorden, grammaticale constructies en noodzakelijke briefingfeiten zijn geen
bronkopie.

## 14. Nieuwe bronnen en menselijke goedkeuring

- C9-uitvoer is evaluatiebewijs, geen bron.
- Een herstelde tekst wordt niet automatisch positieve evidence.
- Een nieuwe passage wordt pas writerreferentie na menselijke goedkeuring.
- Oude afkeuringen worden alleen regel wanneer nieuwe analyse ze bevestigt.
- Regulated en hybrid blijven zwakker onderbouwd tot een volledige menselijke
  voorbeeldpagina is goedgekeurd.

## 15. Manifesten

- `08_SOURCE_MANIFEST.json`: 75 unieke geanalyseerde bronbestanden.
- `04_CURATED_SOURCE_EXAMPLES.json`: 29 gecureerde bronreferenties.
- `07_REFERENCE_SPLIT.json`: writerherkomst, open kalibratie, historische overlap en laadvoorwaarden.

## 16. Writer-first scheiding

Voor `UITSCHRIJVEN` wordt vóór de schrijverspass een schone positieve
schrijversbrief gemaakt.

De writer ziet daarin alleen:

- goedgekeurde feiten en cijfers;
- toegestane vergelijkingen en vertalingen;
- toegestane situaties;
- zichtbare klantgrenzen;
- geautoriseerde service en CTA;
- locks en woordband.

Niet opnemen in de positieve schrijversbrief:

- verboden claims;
- stille beperkingen;
- onbekende peerinformatie;
- negatieve voorbeeldzinnen;
- redenen waarom iets niet mag;
- bronrisicocategorieën;
- beoordelingsclassificaties.

Deze auditinformatie wordt pas na het concept gebruikt. De eindcontrole mag alleen
verwijderen, versmallen of blokkeren. Zij mag geen verdedigende uitleg aan de
klanttekst toevoegen.

## 17. Een bron stuurt vorm, niet woordkeuze uit de audit

De writer gebruikt bij long-form normaal maximaal twee micro-evidence-items, één
schrijversreferentie en geen afzonderlijke structuurreferentie.

De writer neemt uit een referentie alleen over:

- directheid;
- ritme;
- gedachteboog;
- perspectief;
- alineaontwikkeling;
- de manier waarop een toegestaan verschil via een handeling gaat leven.

Woorden en zinnen die in een bron een productclaim, scenario, dienst, positie,
exclusiviteit of emotionele uitkomst dragen, worden niet als vrije stijlvocabulaire
behandeld.

## 18. Bronstilte bij exclusiviteit

Een stijlbron mag nooit aanleiding geven tot woorden als `alleen`, `als enige`,
`uniek` of `alleen bij dit model`.

Exclusiviteit moet volledig uit de actuele briefing volgen. Dat een eigenschap bij één
model wordt genoemd, bewijst niets over modellen waarvoor die eigenschap onbekend is.
