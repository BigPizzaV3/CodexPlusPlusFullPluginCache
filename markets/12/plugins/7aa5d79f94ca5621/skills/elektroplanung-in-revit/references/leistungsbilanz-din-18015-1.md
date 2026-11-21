---
titel: "Wallbox, Wärmepumpe, PV: warum die Leistungsbilanz nach DIN 18015-1 wieder Planungsthema ist"
quelle: https://bimwired.com/landing/wissen/leistungsbilanz-din-18015-1.html
stand: 2026-08-25
art: artikel
fragen:
  - "Wie berechne ich die Anschlussleistung eines Mehrfamilienhauses mit Wärmepumpe und Wallboxen nach DIN 18015-1?"
  - "Woher kommt der Gleichzeitigkeitsfaktor für Wohneinheiten?"
  - "Welche Sonderlasten gehören in die Leistungsbilanz und welche nicht?"
  - "Senkt eine PV-Anlage die erforderliche Anschlussleistung?"
  - "Reichen 63 A für ein Wohngebäude mit Wallbox und Wärmepumpe?"
  - "Ist die Leistungsbilanz für den Netzbetreiber verbindlich?"
---

# Wallbox, Wärmepumpe, PV: warum die Leistungsbilanz nach DIN 18015-1 wieder Planungsthema ist

Die Anschlussleistung eines Wohngebäudes ermitteln Sie nach DIN 18015-1:2020-05 in zwei Schritten. Die Grundlast aller Wohneinheiten liefert die Bedarfskurve aus Anhang A der Norm; sie hängt von der Zahl der Wohneinheiten ab und davon, ob das Warmwasser elektrisch bereitet wird. Sonderlasten wie Wärmepumpe, Ladeeinrichtungen, Aufzug oder Gewerbeflächen setzen Sie separat mit jeweils eigener Gleichzeitigkeit an, denn sie stecken nicht im haushaltsüblichen Bedarf der Kurven. Photovoltaik senkt den Bezugswert nicht, weil der Bemessungsfall der Winterabend ohne Solarertrag ist. Verbindlich bleibt am Ende die Abstimmung mit dem Netzbetreiber nach dessen TAB.

## Das Wichtigste in Kürze

- Die Grundlast liefert die Bedarfskurve in Anhang A der DIN 18015-1:2020-05: gleichzeitige Gesamtleistung nach Zahl der Wohneinheiten, laut Initiative ELEKTRO+ mit und ohne elektrische Warmwasserbereitung.
- Sonderlasten (Wärmepumpe, Ladepunkte, Aufzug, Gewerbeflächen) zählen separat mit eigener Gleichzeitigkeit. Haushaltsgeräte stecken schon in der Kurve und dürfen nicht doppelt gezählt werden.
- Photovoltaik senkt die Bezugsbemessung nicht: Bemessungsfall ist der Winterabend ohne Solarertrag, die Einspeisung wird in der Gegenrichtung geprüft.
- Seit dem 1. Januar 2024 garantiert § 14a EnWG steuerbaren Verbrauchseinrichtungen über 4,2 kW den Netzanschluss; der Netzbetreiber darf dafür bei Engpässen laut Bundesnetzagentur temporär auf 4,2 kW dimmen.
- Verbindlich bleiben örtliche TAB und Anschlusszusage des Netzbetreibers. Die Leistungsbilanz ist Planungsgrundlage, keine Genehmigung.

## Überblick

| Punkt | Detail |
|---|---|
| Norm | DIN 18015-1:2020-05 „Elektrische Anlagen in Wohngebäuden, Teil 1: Planungsgrundlagen“ |
| Grundlast | Bedarfskurven in Anhang A: gleichzeitige Gesamtleistung nach Zahl der Wohneinheiten, mit oder ohne elektrische Warmwasserbereitung |
| Sonderlasten | Wärmepumpe, Ladeeinrichtungen, Aufzug, Gewerbeflächen: separat mit jeweils eigener Gleichzeitigkeit |
| Photovoltaik | Senkt die Bezugsbemessung nicht; die Einspeisung wird als eigene Richtung geprüft |
| Rechtsrahmen | § 14a EnWG seit 2024: garantierter Anschluss steuerbarer Einrichtungen über 4,2 kW, netzorientierte Steuerung möglich |
| Verbindlichkeit | Örtliche TAB und Anschlusszusage des Netzbetreibers; die Bilanz ist Planungsgrundlage |

## Inhalt

1. Warum ist die Leistungsbilanz wieder Planungsthema?
2. Wie ermittelt die DIN 18015-1 die Grundlast eines Wohngebäudes?
3. Welche Sonderlasten kommen obendrauf, und mit welcher Gleichzeitigkeit?
4. Senkt Photovoltaik die erforderliche Anschlussleistung?
5. Beispielrechnung: Mehrfamilienhaus mit 12 Wohneinheiten, Wärmepumpe und 6 Ladepunkten
6. Was sagt der Netzbetreiber dazu?
7. Warum gehört die Bilanz ins Projekt und nicht in eine Excel-Datei daneben?
8. So hilft BimWired
9. Häufige Fragen zur Leistungsbilanz
10. Quellen

## Warum ist die Leistungsbilanz wieder Planungsthema?

Die Leistungsbilanz im Wohnbau war jahrzehntelang Routine, und ich habe sie lange genau so erlebt: Wohneinheiten zählen, Wert aus der Bedarfskurve ablesen, Reserve aufschlagen, fertig. Das trägt nicht mehr. Mit Wärmepumpe, Ladeinfrastruktur und Photovoltaik ziehen Lasten und Erzeuger ins Gebäude ein, die in keiner alten Faustformel stecken.

Die Norm hat darauf reagiert. Die aktuelle Ausgabe DIN 18015-1:2020-05 behandelt laut dem Fachbeitrag „Elektroplanung in Wohngebäuden“ in der Fachzeitschrift „de“ (12/2020) ausdrücklich Dauerstromverbraucher wie Wallboxen und Batteriespeicher. Auch der Rechtsrahmen hat sich verschoben: Seit dem 1. Januar 2024 fallen neue steuerbare Verbrauchseinrichtungen über 4,2 kW Netzanschlussleistung unter § 14a EnWG, also Wärmepumpen, private Wallboxen, Speicher und Klimageräte. Der Netzbetreiber darf ihre Leistung bei drohender Netzüberlastung vorübergehend auf 4,2 kW reduzieren, im Gegenzug sinken die Netzentgelte, so die Bundesnetzagentur. Die andere Hälfte der Regelung steht im Praxisratgeber des Bundesverbands Wärmepumpe: „Der Netzanschluss darf nun nicht mehr aus Gründen der Netzkapazität verweigert oder verzögert werden.“

Diese Garantie schiebt die Verantwortung in die Planung. Ob Hausanschluss, Zählerplätze und Hauptstromversorgungssystem die neuen Lasten tragen, beantwortet vorab Ihre Leistungsbilanz. Wie groß die Unsicherheit dabei ist, zeigt ein Thread im elektrikforum.de vom Juni 2023. Diskutiert wird, ob die Werte der DIN 18015 bindend sind, wie Wärmepumpe und Aufzug einzurechnen sind und ob ein 63-A-Anschluss künftige Wallboxen verkraftet; ein Gleichzeitigkeitsfaktor von 0,4 auf 78 kW installierte Leistung kam dem Fragesteller unrealistisch niedrig vor. Die Fragen kenne ich aus der eigenen Praxis, und sie sind berechtigt.

## Wie ermittelt die DIN 18015-1 die Grundlast eines Wohngebäudes?

Die Leistungsbilanz beantwortet eine einzige Frage: Welche Leistung bezieht das Gebäude im ungünstigsten Fall gleichzeitig aus dem Netz? Auf dieses Ergebnis werden Hausanschluss, Zählerplätze und Hauptleitungen bemessen.

Grundlage im Wohnbau ist die DIN 18015-1:2020-05, „Elektrische Anlagen in Wohngebäuden, Teil 1: Planungsgrundlagen“ (Normnachweis: Baunormenlexikon). Ihr Kernwerkzeug sind die Bedarfskurven in Anhang A. Laut der Initiative ELEKTRO+ liefert das Diagramm die zu erwartende gleichzeitige Gesamtleistung in Abhängigkeit von der Zahl der Wohneinheiten, in zwei Varianten: mit und ohne elektrische Warmwasserbereitung. Der Gleichzeitigkeitsfaktor liegt dabei zwischen 0 und 1.

BauNetz Wissen erläutert eine Unterscheidung, die in der Praxis oft durcheinandergeht: Der Anschlusswert, also die Summe aller installierten Geräteleistungen, ist nicht die Bemessungsgröße. Bemessen wird der tatsächliche Leistungsbedarf, und der liegt wegen der Gleichzeitigkeit deutlich darunter. Der Effekt ist statistisch: Je mehr Wohnungen am selben Hausanschluss hängen, desto unwahrscheinlicher laufen alle Herde, Waschmaschinen und Ladegeräte zugleich.

Der Geltungsbereich ist begrenzt: Die Norm gilt für Wohngebäude. Gewerbeflächen im Wohngebäude ergänzt die Praxis mit W/m²-Werten und eigener Gleichzeitigkeit; für reine Nichtwohngebäude gelten andere Planungsgrundlagen.

Mit der Leistungszahl ist die DIN 18015-1 außerdem nicht am Ende. Nach dem Fachbeitrag in „de“ 12/2020 verlangt die Ausgabe 2020-05 unter anderem Zählerplätze für mindestens 63 A Bemessungsstrom, höchstens 0,5 % Spannungsfall zwischen Hausanschlusskasten und Messeinrichtung (nach Niederspannungs-Anschlussverordnung und VDE-AR-N 4100) und möglichst höchstens 3 % dahinter bis zum Verbrauchsmittel. Dazu kommen die Aufteilung der Endstromkreise auf mehrere Fehlerstrom-Schutzeinrichtungen (zweipoliger FI-Schalter: höchstens zwei, vierpoliger: höchstens sechs einphasige Endstromkreise) und 20 % empfohlene Platzreserve im Stromkreisverteiler. Die Bilanz zieht Zählerschrank und Verteiler also gleich mit.

## Welche Sonderlasten kommen obendrauf, und mit welcher Gleichzeitigkeit?

Für Sonderlasten gilt der Grundsatz, den die Initiative ELEKTRO+ formuliert: Alle Lasten, die vom haushaltsüblichen Bezug abweichen, werden separat bewertet; ausdrücklich genannt sind Wärmepumpe, Ladeeinrichtung und Photovoltaik. Die Bedarfskurve deckt nur ab, was eine Wohnung üblicherweise zieht.

Daraus folgt der Fehler, den ich in Bilanzen am häufigsten sehe: die Doppelrechnung. Herd, Backofen, Wasch- und Spülmaschine stecken bereits in den Kurvenwerten. Wer sie zusätzlich als Einzellasten addiert, bemisst denselben Bedarf zweimal und landet bei einem unnötig großen Hausanschluss.

| Posten | Behandlung in der Leistungsbilanz |
|---|---|
| Haushaltsgeräte (Herd, Backofen, Waschmaschine) | Bereits in den Bedarfskurven enthalten; nie zusätzlich ansetzen |
| Elektrische Warmwasserbereitung (Durchlauferhitzer) | Über die Kurvenwahl abgebildet, nicht als Gerätezuschlag; bei gemischter Ausstattung anteilig rechnen |
| Wärmepumpe (mit Heizstab) | Eigener Posten mit elektrischer Aufnahmeleistung; klären, ob der Heizstab gleichzeitig läuft oder verriegelt ist |
| Ladeeinrichtungen (Wallboxen, Ladepunkte) | Eigene Dauerlast je Ladepunkt; die anzusetzende Gleichzeitigkeit hängt von Steuerung und Netzbetreiber-Abstimmung ab |
| Aufzug, Lüftung, Allgemeinstrom | Separat erfassen; sie gehören nicht zum haushaltsüblichen Bedarf der Wohnungen |
| Gewerbeflächen im Wohngebäude | Mit Flächenwerten in W/m² und eigener Gleichzeitigkeit ansetzen |
| Photovoltaik (ggf. mit Speicher) | Senkt den Bezug nicht; Einspeisung als eigene Richtung bewerten |

Die Gleichzeitigkeit je Sonderlast ist in erster Linie eine begründete, dokumentierte Planungsentscheidung. Zwei Stellschrauben sind legitim. Die erste ist die Verriegelung: Läuft der Heizstab einer Wärmepumpe nie gleichzeitig mit dem Verdichter, geht nicht die Summe beider Leistungen in die Spitze ein. Die zweite ist die Steuerung von Ladepunkten, die die gleichzeitige Ladeleistung technisch begrenzt. Welche Ansätze akzeptiert werden, klären Sie vor der Anschlusszusage mit dem Netzbetreiber; § 14a EnWG beschreibt zusätzlich, wann dieser steuerbare Einrichtungen selbst netzorientiert steuern darf.

## Senkt Photovoltaik die erforderliche Anschlussleistung?

Nein. Eine Photovoltaikanlage reduziert den Energiebezug übers Jahr, aber nicht die Leistung, für die der Anschluss bemessen wird. Bemessungsfall ist der ungünstigste Zeitpunkt, im Wohnbau typischerweise der Winterabend: Wärmepumpe und Ladepunkte laufen, die Küchen sind aktiv, die PV-Anlage liefert nichts. Wer die PV-Leistung abzieht, rechnet die Bilanz für genau diesen Fall schön.

Die Einspeisung verschwindet damit nicht aus der Bilanz, sie wechselt die Richtung. Geprüft wird, welche Leistung die Anlage maximal ins Netz speist und ob der Anschluss auch das trägt; die Initiative ELEKTRO+ zählt Photovoltaik folgerichtig zu den separat zu bewertenden Anlagen. Photovoltaik führen Sie also als eigenen Posten in Einspeiserichtung, nie als negativen Verbraucher. Die Frage kommt so regelmäßig, dass sie hier einen eigenen Abschnitt bekommt.

## Beispielrechnung: Mehrfamilienhaus mit 12 Wohneinheiten, Wärmepumpe und 6 Ladepunkten

Das Folgende ist eine Beispielrechnung mit offenen Annahmen, keine Normnachrechnung. Die Kurvenwerte entnehmen Sie Anhang A der Norm; hier geht es um den Mechanismus und die Fallen. Angenommen: ein Mehrfamilienhaus mit 12 Wohneinheiten ohne elektrische Warmwasserbereitung (das Warmwasser übernimmt die zentrale Wärmepumpe), Wärmepumpe mit Heizstab, 6 Ladepunkte mit je 11 kW in der Tiefgarage, Aufzug, Allgemeinstrom und Photovoltaik.

Abbildung: Ablaufschema der Leistungsbilanz: Grundlast aus der Bedarfskurve und drei Sonderlasten laufen mit je eigener Gleichzeitigkeit in eine Summe, daraus folgen Anschlussleistung und Abstimmung mit dem Netzbetreiber Die Grundlast kommt über die Bedarfskurve nach Zahl der Wohneinheiten herein, jede Sonderlast mit ihrer eigenen Gleichzeitigkeit daneben; die Photovoltaik läuft mit, senkt den Bezug aber nicht.

1. Grundlast ablesen: 12 Wohneinheiten auf der Bedarfskurve ohne elektrische Warmwasserbereitung. Das Ergebnis ist die gleichzeitige Gesamtleistung aller Wohnungen samt ihrer Haushaltsgeräte.
2. Die Wärmepumpe mit ihrer elektrischen Aufnahmeleistung ansetzen, nicht mit der Heizleistung. Dazu klären, ob der Heizstab gleichzeitig läuft oder verriegelt ist.
3. Die Ladepunkte ansetzen. 6 Ladepunkte mit je 11 kW wären ungesteuert 66 kW Dauerlast und damit womöglich der größte Einzelposten der Bilanz. Mit Ladesteuerung sinkt die anzusetzende Gleichzeitigkeit; der gewählte Wert ist eine Annahme, die Sie dokumentieren und mit dem Netzbetreiber abstimmen.
4. Aufzug, Lüftung und Allgemeinstrom als eigene Posten erfassen. Genau an dieser Stelle entsteht in Foren regelmäßig Unsicherheit.
5. Photovoltaik in Einspeiserichtung notieren, nicht als Abzug vom Bezug.
6. Ergebnis bilden und prüfen: Aus den gewichteten Posten ergibt sich die maximale Scheinleistung S_max, daraus der Bemessungsstrom und die Größenordnung der NH-Sicherung am Hausanschluss. Das Ergebnis prüfen Sie gegen die Mindestwerte für Zählerplatz und Hausanschluss und besprechen es mit dem Netzbetreiber.

Was mir an solchen Bilanzen immer wieder auffällt: Die zwölf Wohnungen treiben die Spitze kaum, ihre Grundlast ist durch die Gleichzeitigkeit stark gedämpft. Die Spitze machen die neuen Dauerlasten, allen voran die Ladepunkte und im Winter die Wärmepumpe samt Heizstab. Zwei Annahmen, Ladegleichzeitigkeit und Heizstab-Verriegelung, können das Ergebnis um zweistellige Kilowattbeträge verschieben. Ein kW-Endergebnis nenne ich bewusst nicht: Ohne die projektspezifischen Annahmen und die Kurvenwerte der Norm gibt es keine belastbare Zahl. Ein durchgespieltes Szenario mit allen Annahmen zeigt das [Praxisszenario Leistungsbilanz im Mehrfamilienhaus](https://bimwired.com/landing/wissen/praxisszenario-leistungsbilanz-mfh.html).

## Was sagt der Netzbetreiber dazu?

Die Leistungsbilanz ist Planungsgrundlage, keine Genehmigung. Über den Netzanschluss entscheidet der Netzbetreiber auf Basis seiner Technischen Anschlussbedingungen (TAB) und der Anschlusszusage. Der BDEW stellt mit der TAB 2023 den Bundesmusterwortlaut bereit, der die TAB 2019 ablöst; verbindlich ist die jeweils örtliche Fassung.

Darüber steht die VDE-AR-N 4100, die Technischen Anschlussregeln Niederspannung, die die Bundesnetzagentur als maßgebliches Anschluss-Regelwerk referenziert. Die Themenseite des VDE FNN nennt bereits die Folgeausgabe VDE-AR-N 4100:2026-04. Schon deshalb schreibe ich den verwendeten Regelstand in jede Bilanz hinein. Greifbar wird das beim Spannungsfall: Nach dem Fachartikel „Spannungsfall richtig koordinieren“ („de“ 21/2020) darf der Spannungsfall im Hauptstromversorgungssystem 0,5 % nicht überschreiten; Bezugsgröße ist der Bemessungsstrom der Hausanschlusssicherung, für Wohngebäude mindestens 63 A.

Für die Praxis heißt das: Sprechen Sie Sonderlasten früh an, legen Sie die Bilanz mit nachvollziehbarem Rechenweg vor und lassen Sie sich die Annahmen bestätigen. § 14a EnWG garantiert steuerbaren Verbrauchseinrichtungen zwar den Anschluss, ersetzt aber weder die Anmeldung (laut Praxisratgeber des Bundesverbands Wärmepumpe meldet der Fachbetrieb die Anlage an) noch die Dimensionierung von Hausanschluss und Hauptleitungen.

## Warum gehört die Bilanz ins Projekt und nicht in eine Excel-Datei daneben?

Eine Leistungsbilanz ist keine Einmalrechnung. Sie ist eine Planungsaussage, die mit jedem Planungsstand mitlaufen muss. Aus vier Ladepunkten werden sechs, das Dachgeschoss bekommt zwei weitere Wohnungen, aus der Gastherme wird eine Wärmepumpe. Jede dieser Änderungen verschiebt die Spitze und damit womöglich Hausanschluss, Zählerschrank und Hauptleitungen.

In vielen Büros lebt die Bilanz trotzdem als Excel-Datei neben dem Projekt, und ich habe das selbst lange so gemacht. Sie wird einmal zur Genehmigungsplanung gerechnet und veraltet dann still, während Stromkreisliste und Verteilerplan weiterwachsen.

Was ich stattdessen brauche: die Bilanz am Projekt, mit ausdrücklich dokumentierten Annahmen (Ladegleichzeitigkeit, Verriegelung, Reserve), einem prüffähigen Rechenweg für die Netzbetreiber-Schleife und einem direkten Anschluss an die Folgeplanung, also die [Aufteilung in Stromkreise](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html) und den [normgerechten Verteilerplan](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html). Deshalb führt BimWired die Leistungsbilanz als Modul im Projekt und nicht als Datei daneben.

## Einordnung: das Werkzeug BimWired

Ich habe das Modul so aufgebaut, wie ich die Bilanz selbst rechne, nur ohne die Datei daneben.

Sie erfassen Gebäudetyp, Wohneinheiten, Gewerbeflächen mit W/m² und eigener Gleichzeitigkeit, Wärmepumpe mit Heizstab (gleichzeitig oder verriegelt), Lüftung, Klima, Aufzug, Allgemeinstrom, Ladeeinrichtungen, freie Sonderlasten, eine Reserve sowie Photovoltaik in Einspeiserichtung. Die Bedarfskurven aus Anhang A sind hinterlegt: Kurve A mit elektrischer Warmwasserbereitung, Kurve B ohne; den Mischfall bildet das Modul aus Kurve B plus der Kurvendifferenz für die Durchlauferhitzer-Wohnungen.

Das Ergebnis entsteht live: maximale Scheinleistung S_max, Bemessungsstrom, empfohlene NH-Sicherung, Prüfhinweise, Bilanztabelle, Bedarfskurve und der vollständige Rechenweg für die Abstimmung mit dem Netzbetreiber. Bei der Netzbetreiber-Auswahl arbeitet das Modul mit Referenzwerten nach VDE-AR-N 4100 und TAB 2023; verbindlich bleibt die örtliche TAB. Den Bericht exportieren Sie als mehrseitiges Vektor-PDF (A4, Firmenkopf, Unterschriftenzeilen), dazu CSV und JSON.

Abbildung: Die Ergebniskarte des Moduls: eine Bilanztabelle mit Position, installierter Leistung, Gleichzeitigkeit, Leistungsfaktor und Scheinleistung, darunter der Rechenweg in vier nummerierten Schritten mit den ausgeschriebenen Formeln und eine Liste der herangezogenen Normen. Der Rechenweg steht im Ergebnis, nicht in einer Fußnote. Die Zahlen stammen aus dem kleinen Beispielprojekt der öffentlichen Demo, nicht aus der Beispielrechnung weiter oben.

Ein Revit-Modell ist nicht nötig. Die Bilanz entsteht komplett im Browser und bleibt beim Projekt, direkt neben Stromkreisplanung und Verteilerplan; der Verteilerplan teilt später auf, was die Bilanz bemessen hat. Zwei Grenzen gehören dazu: Die Bilanz bleibt Planungsgrundlage, keine Genehmigung, und ein Lastmanagement ist nicht Teil des Moduls.

## Häufige Fragen zur Leistungsbilanz

### Ist die Leistungsbilanz nach DIN 18015-1 für den Netzbetreiber verbindlich?

Nein. Die Bilanz nach DIN 18015-1 ist die anerkannte Planungsgrundlage für Wohngebäude. Über den Netzanschluss entscheidet aber der Netzbetreiber auf Basis seiner Technischen Anschlussbedingungen und der Anschlusszusage. Der BDEW stellt mit der TAB 2023 den Bundesmusterwortlaut bereit; verbindlich ist die örtliche Fassung Ihres Netzbetreibers.

### Muss ich Herd, Backofen und Waschmaschine als Sonderlast ansetzen?

Nein. Haushaltsübliche Geräte stecken bereits in den Bedarfskurven des Anhangs A. Wer sie zusätzlich addiert, rechnet doppelt und dimensioniert den Anschluss zu groß. Separat bewertet wird laut der Initiative ELEKTRO+ nur, was vom haushaltsüblichen Bezug abweicht, etwa Wärmepumpe, Ladeeinrichtung oder Photovoltaik.

### Senkt eine Photovoltaikanlage die erforderliche Anschlussleistung?

Nein. Der Bezug wird für den ungünstigsten Fall bemessen, typischerweise die Abendspitze im Winter, wenn die Anlage nichts liefert. Die Einspeisung wird in der Gegenrichtung betrachtet; der Anschluss muss beide Richtungen tragen.

### Reichen 63 A für ein Wohngebäude mit Wallbox und Wärmepumpe?

63 A ist die normative Untergrenze, keine Zusage. Die DIN 18015-1:2020-05 verlangt Zählerplätze für mindestens 63 A, und nach VDE-AR-N 4100 beträgt der Bemessungsstrom der Hausanschlusssicherung für Wohngebäude mindestens 63 A. Ob das mit Wärmepumpe und Ladepunkten reicht, zeigt erst die Leistungsbilanz mit den projektspezifischen Sonderlasten; im Zweifel entscheidet die Abstimmung mit dem Netzbetreiber.

### Was bedeutet § 14a EnWG für Wärmepumpe und Wallbox in der Bilanz?

Seit dem 1. Januar 2024 gelten neue steuerbare Verbrauchseinrichtungen mit mehr als 4,2 kW, darunter Wärmepumpen und private Wallboxen, als steuerbar nach § 14a EnWG. Der Netzbetreiber darf die Leistung bei Netzengpässen laut Bundesnetzagentur temporär auf 4,2 kW reduzieren, den Anschluss aber nicht mehr wegen möglicher Netzüberlastung ablehnen. Für die Leistungsbilanz planen Sie weiterhin den regulären Betrieb; die Steuerung ist der Ausnahmefall.

## Quellen

1. „Elektroplanung in Wohngebäuden“ (zur DIN 18015-1:2020-05), Fachzeitschrift „de“, Ausgabe 12/2020, Volltext-PDF: https://www.elektro.net/media/file/Kwqzk199w7/fd7e48cc/DE_12_2020_31-34_EA42neu.pdf (abgerufen am 25.08.2026)
2. D. Sofic: „Spannungsfall richtig koordinieren“, Fachzeitschrift „de“, Ausgabe 21/2020, Volltext-PDF: https://www.elektro.net/media/file/rRnRreLDo4/570b31f0/DE_2020_21_20-26_EA41_LOW.pdf (abgerufen am 25.08.2026)
3. Initiative ELEKTRO+: „Auslegung des Hauptstromversorgungssystems“: https://www.elektro-plus.com/elektroplanung/dimensionierung-netzanschluss/auslegung-hauptstromversorgungssystem (abgerufen am 25.08.2026)
4. BauNetz Wissen: „Leistungsbedarf und Anschlusswert“: https://www.baunetzwissen.de/elektro/fachwissen/grundinstallationen/leistungsbedarf-und-anschlusswert-152962 (abgerufen am 25.08.2026)
5. Baunormenlexikon: „DIN 18015-1:2020-05“ (Normnachweis): https://www.baunormenlexikon.de/norm/din-18015-1/fc7a1835-4b1f-4165-a6da-d40fee8e0682 (abgerufen am 25.08.2026)
6. Bundesnetzagentur: „Steuerbare Verbrauchseinrichtungen (§ 14a EnWG)“, Verbraucherportal: https://www.bundesnetzagentur.de/DE/Vportal/Energie/SteuerbareVBE/start.html (abgerufen am 25.08.2026)
7. Bundesverband Wärmepumpe: „Praxisratgeber § 14a EnWG“, Ausgabe 2026, PDF: https://www.waermepumpe.de/fileadmin/user_upload/Praxisratgeber__14a_2026_WEB.pdf (abgerufen am 25.08.2026)
8. BDEW: „TAB 2023, Technische Anschlussbedingungen Strom“: https://www.bdew.de/energie/tab-2023/ (abgerufen am 25.08.2026)
9. Bundesnetzagentur, Beschlusskammer 6: „Technische Anschlussregeln Niederspannung (VDE-AR-N 4100)“: https://www.bundesnetzagentur.de/DE/Beschlusskammern/BK06/BK6_92_exLink/VDE-AR-N_4100.html (abgerufen am 25.08.2026)
10. VDE FNN: „TAR Niederspannung (VDE-AR-N 4100)“: https://www.vde.com/de/fnn/themen/tar/tar-niederspannung (abgerufen am 25.08.2026)
11. elektrikforum.de: Thread „Dimensionierung Hausanschluss Mehrfamilienhaus“ (Juni 2023): https://www.elektrikforum.de/threads/dimensionierung-hausanschluss-mehrfamilienhaus.43084/ (abgerufen am 25.08.2026)
12. ElekRechner: „Lastberechnung“ (Rechner nach DIN 18015-1): https://www.elekrechner.com/rechner/last/lastberechnung (abgerufen am 25.08.2026)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/leistungsbilanz-din-18015-1.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
