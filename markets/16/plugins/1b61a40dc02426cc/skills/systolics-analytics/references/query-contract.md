# Abfragen und Grenzen

Diese Referenz beschreibt das native Cube-Abfrageformat des systolics-MCP. Das veröffentlichte Tool-Schema hat Vorrang. Ermittle verfügbare Modelle und Member zur Laufzeit.

## Cube-Abfrageformat

`query_cube` und `get_cube_query_sql` verwenden denselben Vertrag. Für ein auswertbares Ergebnis wähle mindestens eine Kennzahl, Gruppierungsdimension oder Zeitdimension mit Granularität. Segmente und reine Datumsfilter begrenzen die Auswahl und ersetzen keine Ergebnisspalte.

- `measures`: vollständige Member-Namen der Kennzahlen, beispielsweise `Leistungen.Geldwert`. Die Schnittstelle setzt keine feste Höchstzahl.
- `dimensions`: Dimensionen zum Gruppieren. Das Ergebnis enthält eine Zeile je Wertkombination, gegebenenfalls zusätzlich je Zeitintervall.
- `timeDimensions`: Liste von Objekten mit `dimension` (vollständiger Name einer Zeitdimension) und optional `dateRange`, `granularity` oder `compareDateRange`.
  - `dateRange`: `["YYYY-MM-DD", "YYYY-MM-DD"]`, ein einzelner Tag `["YYYY-MM-DD"]`, `this_quarter`, `quarter_to_date` oder ein relativer Zeitraum von Cube wie `"last 30 days"`, `"last month"` oder `"this year"`. Ohne Datumsfilter umfasst die Abfrage alles, was das Modell enthält. Bevorzuge explizite Grenzen für nachvollziehbare Antworten.
  - `granularity`: `day`, `week`, `month`, `quarter`, `year` (auch `hour`, `minute`, `second`) oder eine im Modell definierte eigene Granularität. Ohne Granularität erfolgt keine zeitliche Aufteilung; Gruppierungsdimensionen bleiben wirksam.
  - `compareDateRange`: mehrere Zeiträume derselben Zeitdimension anstelle von `dateRange`. Das Ergebnis enthält ein Teilergebnis je Zeitraum.
- `filters`: Bedingungen `{ "member", "operator", "values" }` auf Dimensionen oder Kennzahlen. Operatoren sind unter anderem `equals`, `notEquals`, `contains`, `notContains`, `startsWith`, `notStartsWith`, `endsWith`, `notEndsWith`, `gt`, `gte`, `lt`, `lte`, `set`, `notSet`, `inDateRange`, `notInDateRange`, `beforeDate`, `beforeOrOnDate`, `afterDate`, `afterOrOnDate` und `measureFilter`. Mit `{ "and": [...] }` und `{ "or": [...] }` lassen sich Bedingungen verschachteln. `values` können Zeichenketten, Zahlen oder Wahrheitswerte enthalten; `set` und `notSet` brauchen keine Werte. Wähle Operator und Werte passend zum Member-Typ.
- `segments`: vollständige Namen im Modell definierter Segmente, siehe `get_cube_details`.
- `order`: `{ "Leistungen.Geldwert": "desc" }` oder `[["Leistungen.Geldwert", "desc"]]`. Eine Zeitdimension kann mit Granularität sortiert werden, etwa `Leistungen.LeistungDatum.month`.
- `limit` und `offset`: Zeilenzahl und Startposition für Ranglisten und zum Blättern. `limit: 0` liefert keine Zeilen, etwa zusammen mit `total: true` für eine reine Zählung.
- `ungrouped: true`: einzelne Zeilen des Modells statt Aggregation. Nur für entsprechend angefragte Analysen verwenden und mit `order` und `limit` begrenzen.
- `total: true`: liefert zusätzlich die Gesamtzahl der Ergebniszeilen.
- `timezone`: IANA-Zeitzone, Standard `Europe/Berlin`.
- `responseFormat: "compact"`: liefert `data` als `{ members, dataset }`, die Member-Namen einmal und danach je Zeile eine Werteliste. Verwende das Format, wenn du diese Zuordnung sicher auswerten kannst.
- `renewQuery: true`: fordert aktualisierte Ergebnisse bei Cube an. Nur einsetzen, wenn ein frischer Stand ausdrücklich nötig ist.

Erzeuge neue Aufrufe mit `timeDimensions`. Datumsfilter gehören in die jeweilige Zeitdimension; verwende keine obersten Felder `timeDimension` oder `dateRange`. Ein separates `cube` ist nicht nötig, weil jeder Member-Name den Cube enthält. Übergib Arrays und Objekte als JSON-Werte, nicht als Zeichenketten mit eingebettetem JSON.

Member mehrerer über Joins verbundener Cubes dürfen kombiniert werden. Die Plattform prüft die genannten Member gegen den sichtbaren Katalog. Meldet das Tool einen unbekannten Member, prüfe den Katalog mit `get_measures`, `get_dimensions` oder `get_cube_details`. Ein Ersatzname muss nachweislich dieselbe fachliche Größe bezeichnen. Gibt es keinen solchen Member, erkläre die Nichtverfügbarkeit oder kläre eine Alternative. Fehlercodes sind kein garantierter Bestandteil der MCP-Antwort.

Weitere unterstützte Cube-Parameter können an Cube weitergereicht werden. Daraus folgt nicht, dass Cube beliebige zusätzliche Felder akzeptiert. Verwende nur Parameter des veröffentlichten Schemas oder bestätigte Cube-Parameter; erfinde keine Felder wie `groupBy` oder `year_to_date`. Der authentifizierte Kontext bestimmt Organisation und Endpunkt. Freies SQL ist kein Eingabeformat.

## Beispiele

Die folgenden Member und Filterwerte sind Beispiele. Verwende sie nur, wenn der aktive Katalog und die Datenbedeutung sie bestätigen. Ermittle aktuelle Datumsgrenzen zur Laufzeit.

Gesamtwert eines Quartals:

```json
{
  "measures": ["Leistungen.Geldwert"],
  "timeDimensions": [{ "dimension": "Leistungen.LeistungDatum", "dateRange": ["2026-07-01", "2026-09-30"] }]
}
```

Monatsreihe, aufgeteilt nach Gebührenordnung:

```json
{
  "measures": ["Leistungen.Geldwert"],
  "dimensions": ["Leistungen.GOGattung"],
  "timeDimensions": [{ "dimension": "Leistungen.LeistungDatum", "granularity": "month", "dateRange": ["2026-01-01", "2026-09-30"] }],
  "order": [["Leistungen.LeistungDatum.month", "asc"], ["Leistungen.GOGattung", "asc"]]
}
```

Zwei vollständige Quartale mit identischer Kennzahl vergleichen:

```json
{
  "measures": ["Leistungen.Geldwert"],
  "timeDimensions": [{
    "dimension": "Leistungen.LeistungDatum",
    "compareDateRange": [["2026-04-01", "2026-06-30"], ["2026-07-01", "2026-09-30"]]
  }]
}
```

Die zehn EBM-Leistungsziffern mit dem höchsten Geldwert im dritten Quartal 2026, mit einer zweiten Sortierung für Gleichstände:

```json
{
  "measures": ["Leistungen.Geldwert"],
  "dimensions": ["Leistungen.Leistungsziffer"],
  "timeDimensions": [{ "dimension": "Leistungen.LeistungDatum", "dateRange": ["2026-07-01", "2026-09-30"] }],
  "filters": [{ "member": "Leistungen.GOGattung", "operator": "equals", "values": ["EBM"] }],
  "order": [["Leistungen.Geldwert", "desc"], ["Leistungen.Leistungsziffer", "asc"]],
  "limit": 10
}
```

Für eine vollständige Liste statt einer Top-10-Frage beginne mit `offset: 0` und einem passenden `limit`, etwa 100. Folgeaufrufe behalten Kennzahlen, Dimensionen, Datumsgrenzen, Filter und stabile Sortierung unverändert und erhöhen `offset` um die Seitengröße: 0, 100, 200. Löse relative Datumsbereiche dafür vorab in feste Grenzen auf. Lade nur so viele Seiten, wie die Frage benötigt; nach einer kürzeren Seite oder der bestätigten Gesamtzahl ist die Liste vollständig. Bei veränderlichen Daten bleiben Seiten zeitlich getrennte Abfragen.

## Ergebnisse und Vergleiche

Das Ergebnis enthält die ausgeführte `query`, die Definitionen der verwendeten Kennzahlen und Dimensionen, `rowCount`, die Zeilen in `data` und gegebenenfalls `lastRefreshTime`. Mit `total: true` kann `total` hinzukommen. Zeilenschlüssel sind die Member-Namen, bei Zeitreihen ergänzt um die Granularität (`Leistungen.LeistungDatum.month`). Behandle Dezimalwerte unverändert und präzise; vermeide verlustbehaftete Umwandlungen in JavaScript-Zahlen.

`this_quarter` und `quarter_to_date` werden in der Serverstandardzeitzone in konkrete Datumsgrenzen aufgelöst, im geprüften System Europe/Berlin. Das Query-Argument `timezone` stellt die Auswertungszeitzone ein, ändert aber die Auflösung dieser beiden Kürzel nicht. Bei einer anderen gewünschten Zeitzone berechne explizite Datumsgrenzen in dieser Zeitzone und übergib sie zusammen mit `timezone`. Andere relative Cube-Zeiträume können als Ausdruck in der zurückgegebenen Abfrage stehen; gib diese dann nicht als vom MCP bestätigte konkrete Grenzen aus.

Mit `compareDateRange` steht statt `data` die Liste `results` im Ergebnis: ein Teilergebnis je Zeitraum, jeweils mit eigener `query`, `rowCount` und `data`. Vergleiche die Bereiche anhand dieser Grenzen und verwechsle Teilergebnisse nicht mit Zeilen einer einzelnen Abfrage. Bei `responseFormat: "compact"` ist `data` ein Objekt mit `members` und `dataset` statt einer Zeilenliste.

Die Plattform setzt kein eigenes Zeilenlimit. Ohne `limit` gilt die Vorgabe der Cube-API. Trägt das Ergebnis `possiblyTruncated: true`, hat die Zeilenzahl das angewandte Limit erreicht und das Ergebnis kann unvollständig sein. Blättere weiter oder verdichte die Abfrage, bevor du eine vollständige Liste oder Summe daraus ableitest. Eine ausdrücklich bestellte Top-N-Rangliste darf auf N Zeilen begrenzt sein; stelle sie als Rangliste dar.

Distinct Counts sind über Zeiträume und Gruppen nicht additiv. Frage einen Gesamtwert mit einer zusätzlichen Abfrage ohne die betreffende Aufteilung oder Granularität ab. Addiere Durchschnitte und Quoten ebenfalls nicht und bilde daraus keinen ungewichteten Mittelwert. Vergleiche gleich definierte Größen mit identischen Filtern und begründe eine abweichende Periodenlänge.

## SQL einer Abfrage

`get_cube_query_sql` nimmt dieselben Parameter wie `query_cube` und führt die Ergebnisabfrage nicht aus. Cube erzeugt SQL gegen die Quelltabellen ohne Voraggregationen. Das SQL zeigt damit die Modelldefinition, nicht den Datenstand einer Voraggregation. Das Ergebnis enthält `sql` als `{ "statement", "parameters" }`, bei `compareDateRange` eine Liste mit einem Eintrag je Zeitraum. Ordne Platzhalter ihren Werten zu: `$1, $2 …` in Postgres (`parameters[n-1]`) oder `?` in der Reihenfolge der Parameter bei ClickHouse. Eine vereinfachte Darstellung muss als solche erkennbar bleiben.

## Datenstrukturen

`get_data_entities` akzeptiert optional `query`, `limit` und `offset`. Das Limit beträgt standardmäßig 25 und höchstens 100. Verwende für weitere Seiten den zurückgegebenen `nextOffset`, solange weitere Einträge für die Frage benötigt werden.

`get_data_entity_details` benötigt `entity`: einen genauen Namen oder eine ID aus dem Katalog. Das Ergebnis beschreibt die Entität und ihre Spalten; es liefert keine einzelnen Datensätze. Fehlt die Berechtigung, erkläre den fehlenden Metadatenzugriff und verweise auf die systolics-Verbindung. Weitere Freigaben stehen in [Tools und Berechtigungen](tools.md).
