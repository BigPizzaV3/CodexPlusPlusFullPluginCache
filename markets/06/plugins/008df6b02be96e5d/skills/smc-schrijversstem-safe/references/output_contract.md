# Uitvoercontract 1.2.0-rc.15

## UITSCHRIJVEN

Bij succes toon je uitsluitend de volledige definitieve tekst.

De tekst mag alleen zichtbaar worden wanneer:

- de harde opdrachtpoort volledig PASS is;
- H1, kopvolgorde, voorwaarden, CTA-rechten en woordband kloppen;
- de inhoud iedere kop daadwerkelijk beantwoordt, ook na de laatste inkorting;
- iedere zichtbare betekenis rechtstreeks door de briefing wordt gedragen;
- de concepttekst vanuit een schone positieve schrijversbrief is geschreven;
- geen verboden claim, auditnotitie of negatieve voorbeeldformulering in die
  schrijversbrief is terechtgekomen;
- geen niet-geautoriseerd scenario, dienst of adviseursgedrag aanwezig is;
- geen inhoudelijke propositie uit een stijlbron is overgenomen;
- geen gedragsregel, stille beperking, redactionele instructie of bewijslogica
  zichtbaar is;
- iedere belangrijke uitleg een primaire plek heeft, met ruimte voor
  briefinggedragen verduidelijking en korte functionele terugverwijzingen;
- geen alinea dezelfde boodschap met dezelfde lezersfunctie opnieuw vertelt;
- alle verplichte onderdelen voldoende zijn uitgewerkt; niet iedere zin hoeft een
  nieuw feit te bevatten;
- geen modelblok eindigt met een specificatierecap;
- geen uitleg over eenheden, categorieën of de onderlinge functie van feiten
  overblijft;
- geen zin vooral beschrijft hoe de tekst of vergelijking is opgebouwd;
- iedere exclusieve formulering volledig wordt bewezen door alle relevante waarden;
- onbekende peerinformatie niet als afwezigheid wordt behandeld;
- iedere concrete showroomclaim binnen de vereiste beschikbaarheidsvoorwaarde valt;
- precies één volledige CTA aanwezig is;
- service-uitleg en CTA niet dezelfde handelingenreeks volledig herhalen;
- de tweede helft pagina-eigen blijft;
- schrijverstem en paginatype overtuigend passen;
- geen systeemtaal of herkenbare bronkopie aanwezig is.

Toon geen scores, JSON, positieve schrijversbrief, auditnotities, inhoudsverdeling,
bronselectie, bewijsredenering, herstelstappen, pluginuitleg of technische status.

### Blokkades

Gebruik bij blokkade uitsluitend één passende status:

```text
BLOCKED_MISSING_FACTS
BLOCKED_CONTRADICTORY_FACTS
BLOCKED_UNSUPPORTED_H1
BLOCKED_WRONG_PAGE_TYPE
BLOCKED_INSUFFICIENT_APPROVED_CONTENT_FOR_LENGTH
BLOCKED_INTERNAL_QUALITY_GATE
BLOCKED_OUT_OF_SCOPE
```

`BLOCKED_INSUFFICIENT_APPROVED_CONTENT_FOR_LENGTH` is alleen toegestaan wanneer:

- de gebruiker daadwerkelijk een minimum heeft opgegeven;
- alle verplichte inhoud en bruikbare toegestane uitwerking zijn gecontroleerd;
- een echt tekort niet binnen de bestaande twee verborgen reparaties is opgelost;
- de resterende lengte alleen met doublures, onbewezen inhoud of opvulling haalbaar
  zou zijn.

Zonder minimum wordt deze lengteblokkade niet gebruikt. Schrijf dan volledig naar
de inhoud en binnen een opgegeven maximum. Geen minimum uit een profiel of oude
test importeren. Kortheid alleen bewijst geen onhaalbaarheid. Bij een expliciet
minimum mag niet stilzwijgend een kortere tekst als geslaagde uitvoer worden geleverd.
Andere veiligheids- en kwaliteitsblokkades blijven bestaan.

Toon nooit een half concept.

## BEOORDELEN

Beoordeel uitsluitend de aangewezen volledige tekst. Herschrijf of herstel niet.

Gebruik deze volgorde:

```text
Harde opdracht
Uitkomst: PASS of FAIL

Mechanisch gecontroleerd
- <controle en resultaat>

Inhoudelijk gelezen
- <controle en resultaat>

Woordtelling
- methode: VISIBLE_LEXICAL_WORDS_INCLUDING_HEADINGS
- body: <aantal>
- koppen: <aantal>
- totaal: <aantal>
- vereiste band: <minimum–maximum>

Zichtbare betekenissen en briefingsteun
1. Citaat: "<exact citaat>"
   Betekenis: <concrete zichtbare uitspraak>
   Grondslag: <briefingregel, lock of NONE>
   Steunstatus: SUPPORTED | PARTIALLY_SUPPORTED | UNSUPPORTED | AMBIGUOUS
   Classificatie: AANTOONBAAR_ONJUIST | NIET_GEGEVEN |
                  BUITEN_TOEGESTANE_VERTALING | DUBBELZINNIG |
                  UNSUPPORTED_VISIBLE_PROPOSITION | UNAUTHORIZED_SCENARIO |
                  UNAUTHORIZED_SERVICE_PROPOSITION | SOURCE_PROPOSITION_TRANSFER |
                  PROMPT_VISIBILITY_ERROR | INTERNE_REDENEERLEK |
                  ZICHTBARE_VERTALINGSREGEL | ZICHTBARE_STILLE_UITSLUITING |
                  BETEKENISHERHALING | GLOBAL_SINGLE_USE_VIOLATION |
                  META_PROSE | UNIT_OR_CATEGORY_FILLER |
                  EXCLUSIVITY_FROM_UNKNOWN | CHECKLIST_DRIFT |
                  BESCHIKBAARHEIDSVOORWAARDE_FOUT | DUBBELE_CTA |
                  MODELBLOK_RECAP | STILISTISCH_ZWAK
   Ernst: HARD | REDACTIONEEL
   Aanpassingstype: <kort type, geen herschreven zin>

Bronstatus van de beoordeling
- werkwijze: OPEN_CALIBRATION | VERIFIED_INDEPENDENT | NOT_ESTABLISHED
- gebruikte bronfamilies en microherkomst: <feitelijk vastgestelde herkomst>
- schrijfrun-laadgeschiedenis: <bekend of NIET VASTGESTELD>
- onafhankelijke holdout aantoonbaar: JA | NEE | NIET VASTGESTELD
- blinde menselijke beoordeling uitgevoerd: JA | NEE | NIET VASTGESTELD

Bronfirewall
- bronfeitoverdracht: PASS | FAIL
- scenariotransfer: PASS | FAIL
- servicetransfer: PASS | FAIL
- adviseursgedragtransfer: PASS | FAIL

Schrijversstem en bruikbaarheid
- Directe opening: STERK | PASSEND | ONVOLDOENDE
- Concrete uitleg: STERK | PASSEND | ONVOLDOENDE
- Gedachteontwikkeling: STERK | PASSEND | ONVOLDOENDE
- Ondersteund model- of onderwerpsbeeld: STERK | PASSEND | ONVOLDOENDE
- Menselijke houding: STERK | PASSEND | ONVOLDOENDE
- Natuurlijke afzender: STERK | PASSEND | ONVOLDOENDE
- Ritme en profiel: STERK | PASSEND | ONVOLDOENDE
- Tweede helft en CTA: STERK | PASSEND | ONVOLDOENDE
- Zekerheid schrijversmatch: HIGH | MEDIUM | LOW

Noodzakelijk aanpassen
- <alleen harde fouten of NONE>

Redactioneel verbeteren
- <concrete punten of NONE>

Behouden
- <sterke passages of eigenschappen>

Eindstatus: PASS | PASS MET VERBETERPUNTEN | FAIL
```

Regels:

- maximaal vijf grondbevindingen;
- dezelfde grondfout één keer;
- iedere harde bevinding krijgt een exact citaat en briefingeigenaar of `NONE`;
- een historische foutlijst voorspelt geen fout in een nieuwe tekst;
- een noodzakelijk zichtbare grens is niet automatisch herhaling;
- nuttige verduidelijking, toepassing en korte terugverwijzingen zijn niet op
  zichzelf herhaling; vergelijk hun lezersfunctie en briefingsteun;
- vermeld bij afwezig minimum: geen minimum opgegeven; verzin geen ondergrens;
- een niet-geautoriseerd scenario, servicebelofte of onbewezen exclusiviteit is HARD;
- zichtbare prompt-, bron-, audit- of redeneerlogica is HARD;
- uitleg over eenheden of categorieën is REDACTIONEEL, tenzij zij de tekst vult en
  de first-visible kwaliteit structureel breekt;
- een harde fout geeft altijd `FAIL`;
- scores zijn geen rekenkundige beslismotor;
- de historische bronoverlap blijft zichtbaar; bestaande referenties zijn open kalibratie;
- onbekende laadgeschiedenis en een lege familie-intersectie bewijzen geen onafhankelijkheid;
- ontbrekende onafhankelijke bronnen zijn geen automatische tekst-FAIL of schrijfblokkade;
- een opdracht-PASS is geen bewijs van blinde menselijke validatie of een foutloze schrijver.

## HERSTELLEN

Bevries:

- correcte feiten en cijfers;
- locks;
- voorwaarden;
- sterke passages;
- goed werkend model- of onderwerpsbeeld;
- de correcte CTA.

Herstel alleen aangetoonde afwijkingen.

Controleer na iedere wijziging:

- oorspronkelijke fout weg;
- eerder opgeloste fout niet terug;
- iedere nieuwe betekenis heeft briefingsteun;
- geen nieuw scenario, servicegedrag of broninhoud toegevoegd;
- geen onbewezen exclusiviteit toegevoegd;
- herhaling en metaproza werkelijk verwijderd;
- woordband opnieuw geteld;
- tweede helft en CTA opnieuw gecontroleerd.

Bij succes toon je uitsluitend de volledige herstelde tekst.

## FULL_VISIBLE_COPY_AFTER_PATCH

Vereis de volledige zichtbare tekst. Een fragment krijgt geen PASS.

Gebruik exact één:

- `PASS_AFTER_PATCH`;
- `PASS_AFTER_PATCH_MET_VERBETERPUNTEN`;
- `FAIL_AFTER_PATCH`;
- `BLOCKED_FULL_COPY_MISSING`.

Herschrijf niets in deze werkstand.
