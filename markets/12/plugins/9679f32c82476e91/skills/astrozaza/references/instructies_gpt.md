# AstroZaza — invoer en berekeningen voor de plug-in

Dit is de aangepaste versie van de oorspronkelijke API-instructies. SKILL.md
bepaalt gedrag en brongebruik. De aangesloten toolschema's bepalen de toegestane
velden. Oude command/flags-voorbeelden uit CHEATSHEET.md of historische teksten
zijn geen instructie om de oude Action te gebruiken.

## Normalisatie en personen

Accepteer Nederlandse en Engelse datums en gangbare notaties; normaliseer naar
YYYY-MM-DD en HH:MM in 24-uursnotatie. Vraag bij dubbelzinnige datums gericht om
verduidelijking. Verzin geen onbekende geboortetijd. Hergebruik de gegevens uit
het gesprek bij de juiste persoon; wissel A en B niet om.

Locatie bij voorkeur city + country, zonder tz. Alternatief lat + lon + tz.
De eigen rekenserver verzorgt de plaatsomzetting; daarvoor ga je niet webzoeken.
Vraag alleen ontbrekende invoer, geen naam of contactgegevens.

Alle argumenten staan direct in de toolaanroep. Geen command/flags-object.
Onderstaande voorbeelden gebruiken uitsluitend fictieve testgegevens.

## Natal — calculateNatalChart

date, time en locatie zijn nodig.

```json
{"date":"2000-01-01","time":"12:00","country":"Nederland","city":"Amsterdam"}
```

## Synastrie — calculateSynastry

Persoon A: date, time, locatie. Persoon B: b_date, b_time, b_city, b_country
of b_lat, b_lon, b_tz. Gebruik underscores, geen CLI-streepjes.

```json
{"date":"2000-01-01","time":"12:00","country":"Nederland","city":"Amsterdam","b_date":"2001-02-03","b_time":"09:15","b_country":"Nederland","b_city":"Rotterdam"}
```

## Persoonlijke transits — calculatePersonalTransits

Altijd geboortegegevens plus mode. Eén moment: snapshot met on en eventueel at.
Een periode: peaks met period en de bijbehorende velden, of year + quarter,
of een expliciet start/end- of from/to-bereik. Kies één route per vraag.

```json
{"date":"2000-01-01","time":"12:00","country":"Nederland","city":"Amsterdam","mode":"snapshot","on":"2026-10-01","at":"12:00"}
```

```json
{"date":"2000-01-01","time":"12:00","country":"Nederland","city":"Amsterdam","mode":"peaks","year":2026,"quarter":"Q4","top":10}
```

```json
{"date":"2000-01-01","time":"12:00","country":"Nederland","city":"Amsterdam","mode":"peaks","period":"range","start":"2026-10-01","end":"2026-10-07","top":10}
```

Bij week/maand is een einddatum niet apart nodig als de periode door start en
period al vaststaat. Bij alleen 'vanaf X' zonder duur vraag je tot wanneer.
Bereken geen compleet jaar als een kwartaal of week gevraagd is. Bij een
jaarvraag gebruik je één jaarbereik; geen vier kwartalen én hetzelfde jaarbereik.
Een top-lijst van transitpeaks bewijst niet dat alle mogelijke contacten afwezig
zijn. Claim daarom geen definitief afgelopen Saturnusreturn zonder passende
berekening die de gevraagde periode dekt.

In de herstelde persoonlijke transituitvoer betekent `natal H1` de positie van
de transitplaneet binnen de geboortehuizen (Placidus). Dit geldt voor dag- én
pieksnapshots. Oude uitvoer met alleen `H4` onder `Transit snapshot` gebruikte
huizen van het transitmoment; die mag je niet als radixhuis interpreteren.
Gebruik voor zo'n oude uitvoer alleen de standen/aspecten, of vraag de berekening
opnieuw op. Raad de betekenis van een technisch veld nooit uit de modulenaam.

## Lunaties — calculateLunations

Collectief: year + collective true. Persoonlijk: year + geboortegegevens.

```json
{"year":2026,"collective":true,"tz":"Europe/Amsterdam"}
```

## Collectief — calculateCollectiveAstrology

Geen geboortegegevens vereist. Dagmoment: mode snapshot + period day + on.
Periode: mode peaks met de passende periodevelden. year/quarter en from/to
blijven toegestaan volgens het toolschema.

```json
{"mode":"snapshot","period":"day","on":"2026-10-01","tz":"Europe/Amsterdam"}
```

## Retrogrades — calculateRetrogrades

period met on/start/end/year/quarter volgens de gekozen periode, of year of
from/to. Optioneel bodies en events. Persoonlijke overlay: natal_date,
natal_time, natal_city, natal_country of natal_lat, natal_lon, natal_tz.

`tz` is de weergavetijdzone van de kalender; `natal_tz` hoort uitsluitend bij de
optionele geboorte-overlay. Voor een collectieve retrogradekalender zijn geen
geboortegegevens nodig. Vraag bij stationdatums ook `events: true`; de uiteinden
van retrograde-intervallen kunnen zoekperiodegrenzen zijn en zijn niet automatisch
stations. Alleen de afzonderlijke stationevents bewijzen een stationmoment.

```json
{"period":"quarter","year":2026,"quarter":"Q4","tz":"Europe/Amsterdam"}
```

## Fouten en uitleg

Een succesvolle tooloutput met ok true bepaalt de rekenfeiten. Geef bij een
fout geen vervangende standen, eigen efemeriden of webresultaten. Corrigeer een
herkenbare invoerfout hoogstens eenmaal. Bij een onbereikbare server of geweigerde
toegang stop je en meld je dat kort. Vraag niet opnieuw om bekende gegevens als
die de fout niet veroorzaken.

Voor duiding lees je de relevante eigen kennis. Rekenfeiten en duiding zijn twee
verschillende onderdelen: een succesvolle berekening vervangt het lezen van
natal, transits, synastrie, global, tarot of products niet. Raadpleeg INDEX.md.
