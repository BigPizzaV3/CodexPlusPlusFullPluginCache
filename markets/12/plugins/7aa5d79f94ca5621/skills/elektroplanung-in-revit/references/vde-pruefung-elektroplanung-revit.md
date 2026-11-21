---
titel: "Kann Revit nach VDE prüfen? Was automatisierbar ist und was Ingenieurleistung bleibt"
quelle: https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html
stand: 2026-08-25
art: artikel
fragen:
  - "Kann Revit den Spannungsfall nach VDE berechnen?"
  - "Welche VDE-Nachweise verlangt die Elektroplanung?"
  - "Spannungsfall: gelten 3 oder 5 Prozent?"
  - "Welche Prüfungen lassen sich in der Elektroplanung automatisieren?"
  - "Welche Software nutzen Büros für Leitungsdimensionierung und VDE-Nachweise?"
---

# Kann Revit nach VDE prüfen? Was automatisierbar ist und was Ingenieurleistung bleibt

Nein. Revit bringt von Haus aus keine Kabelberechnung nach den deutschen VDE-Normen mit: Spannungsfall, Strombelastbarkeit und Kurzschlussfestigkeit rechnet die Software nicht nach, das räumt selbst der Revit-Elektro-Spezialist BEEL ein. Diese Nachweise entstehen heute in Berechnungswerkzeugen, Einzelrechnern oder Excel, getrennt vom Modell. Ein Teil der Regelprüfungen lässt sich automatisieren, etwa Überlast-Plausibilität, RCD-Pflicht und Mindestquerschnitte, sobald die Stromkreisdaten strukturiert vorliegen. Die rechnerischen Nachweise und ihre Bewertung bleiben Aufgabe der Elektrofachkraft.

## Das Wichtigste in Kürze

- Die Lücke bei den Bordmitteln ist dokumentiert: Der Revit-Elektro-Spezialist BEEL schreibt selbst, dass Revit keine vollständige Kabelberechnung nach DIN VDE bietet (Spannungsfall, Kurzschlussfestigkeit, Strombelastbarkeit). Erweiterungen wie MagiCAD verkaufen laut tab-Advertorial genau diese Berechnung.
- Die Prüfkette hat feste Zuständigkeiten: DIN VDE 0100-410 (RCD-Schutz), DIN VDE 0100-520 (Spannungsfall), DIN VDE 0298-4 (Strombelastbarkeit), DIN 18015-1 (Wohngebäude), VDE-AR-N 4100 mit örtlicher TAB (Netzanschluss).
- Spannungsfall in Zahlen, jeweils laut elektro.net: 0,5 % im Hauptstromversorgungssystem (VDE-AR-N 4100 mit Paragraf 13 NAV), im Wohnbau höchstens 3 % hinter der Messeinrichtung (DIN 18015-1); Tabelle G.52.1 der DIN VDE 0100-520 nennt 3 %/5 % für Anlagentyp A und 6 %/8 % für Typ B.
- Regelhaft automatisierbar ist, was ohne Rechenmodell aus Struktur und Attributen des Plans folgt. Spannungsfall mit realen Längen, Strombelastbarkeit je Verlegeart, Selektivität und Kurzschluss bleiben Berechnung und Bewertung der Fachkraft.
- In unserer eigenen Ansprache-Kartei haben wir bei 15 von 192 Büro-Profilen die VDE-Nachweise ausdrücklich als Schmerzpunkt vermerkt: geprüft wird „Zeile für Zeile von Hand", in Excel neben dem Modell. Der Vermerk stammt von uns, nicht von den Büros.

## Überblick

| Punkt | Detail |
|---|---|
| Bordmittel-Lage | Revit bietet laut BEEL keine vollständige Kabelberechnung nach DIN VDE; Erweiterungen verkaufen genau diese Berechnung (tab-Advertorial zu MagiCAD) |
| Maßgebliche Regelwerke | DIN VDE 0100-410, DIN VDE 0100-520, DIN VDE 0298-4, DIN 18015-1, VDE-AR-N 4100 mit örtlicher TAB |
| Spannungsfall-Grenzwerte | 0,5 % im Hauptstromversorgungssystem; höchstens 3 % dahinter im Wohnbau; Tabelle G.52.1: 3 %/5 % (Typ A) und 6 %/8 % (Typ B), jeweils laut elektro.net |
| Regelhaft automatisierbar | Überlast-Plausibilität, RCD-Pflicht, Mindestquerschnitte, Struktur- und Zählregeln |
| Ingenieurleistung | Spannungsfall mit realen Längen, Strombelastbarkeit je Verlegeart, Selektivität, Kurzschlussfestigkeit, Netzform |
| Typische Werkzeuge heute | Excel, Einzelrechner (ElekRechner), Netzberechnung (Siemens Simaris), Revit-Erweiterungen (MagiCAD, elkoBIM) |

## Inhalt

- Kann Revit nach VDE rechnen?
- Welche VDE-Nachweise verlangt die Elektroplanung?
- Warum ist der Spannungsfall ein Problemfall?
- Was ist regelhaft automatisierbar, was bleibt Ingenieurleistung?
- Wie führen deutsche Büros die VDE-Nachweise heute?
- Was fängt eine Regelprüfung im modellgespeisten Workflow ab?
- So hilft BimWired
- Häufige Fragen (FAQ)
- Quellen

## Kann Revit nach VDE rechnen?

Revit enthält keine Kabelberechnung nach den deutschen VDE-Normen. Wer Spannungsfall, Strombelastbarkeit oder Kurzschlussfestigkeit nachweisen will, braucht ein zweites Werkzeug. Der deutlichste Beleg dafür kommt von einem Anbieter, der von Revit-Elektroplanung lebt: „Revit bietet keine vollständige Kabelberechnung nach DIN VDE (Spannungsfall, Kurzschlussfestigkeit, Strombelastbarkeit)", schreibt BEEL auf der eigenen Themenseite zur Kabelplanung. Dazu passt die Werbung der Erweiterungen: Im Advertorial der Fachzeitschrift tab führt MagiCAD die eigene Spannungsfall- und Kabeldimensionierungs-Berechnung als zentrales Argument für den Zukauf an. Wäre die Berechnung Bordmittel, gäbe es dieses Verkaufsargument nicht.

Mit BIM ändern sich die Pflichten nicht. Die DKE fordert für elektrotechnische Installationen im BIM-Umfeld einheitliche Standards und stellt zugleich klar, dass die Normenreihe DIN VDE 0100 verbindlich bleibt. Ob die Nachweise geführt werden, steht also nicht zur Debatte. Offen ist nur, wo das passiert, mit welchen Daten, und wie schnell sie nach einer Umplanung wieder stimmen. Wie Sie die Stromkreis-Logik der Bordmittel auf deutsche Arbeitsweise einstellen, steht im Beitrag [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html); hier geht es um die Prüf- und Nachweisseite.

## Welche VDE-Nachweise verlangt die Elektroplanung?

Für jeden Endstromkreis muss die Elektroplanung mindestens vier Fragen beantworten: Ist der Schutz gegen elektrischen Schlag sichergestellt? Trägt die Leitung den Strom dauerhaft? Bleibt der Spannungsfall im Rahmen? Erfüllt die Anlage die Planungsgrundlagen des Gebäudetyps? Jede Frage hat ihre eigene normative Heimat und in der Praxis meist ihr eigenes Werkzeug.

| Norm oder Regelwerk | Kernfrage | Woher die Antwort heute kommt |
|---|---|---|
| DIN VDE 0100-410:2018-10 | Wo sind RCDs mit höchstens 30 mA Pflicht? Laut DKE-Normenhinweis bei Steckdosen-Stromkreisen bis 32 A, in Wohnungen auch bei Beleuchtungsstromkreisen | Regelwissen, Checklisten |
| DIN VDE 0100-520:2013-06 | Bleibt der Spannungsfall der Verbraucheranlage im Rahmen? Empfehlungswerte stehen in Tabelle G.52.1 | Excel, Einzelrechner, Berechnungssoftware |
| DIN VDE 0298-4:2023-06 | Trägt Kabel oder Leitung den Strom dauerhaft? Die Norm regelt die Strombelastbarkeit nach Verlegeart, laut elektrofachkraft.de inklusive der neuen Referenzverlegeart 23 | Tabellenwerk, Berechnungssoftware |
| DIN 18015-1:2020-05 | Erfüllt die Wohnbau-Anlage die Planungsgrundlagen? Unter anderem Spannungsfall 0,5 %/3 %, Zählerplatz mindestens 63 A, Aufteilung der Stromkreise auf RCDs (Fachartikel in „de" 12/2020) | Planungsregeln, Leistungsbilanz |
| VDE-AR-N 4100 und örtliche TAB | Passt der Anschluss ans Niederspannungsnetz? | Abstimmung mit dem Netzbetreiber |
| Selektivität, laut StromKompass u. a. in der DIN 18015-1 normativ verankert | Schaltet im Fehlerfall nur die unmittelbar vorgeschaltete Schutzeinrichtung ab? | Netzberechnung, Herstellerdaten |
| DIN VDE 0100-718 | Bleiben sicherheitsrelevante Anlagen wie die Sicherheitsbeleuchtung in öffentlichen Einrichtungen im Brandfall betriebsfähig (Funktionserhalt E30/E60/E90)? So erläutert bei BauNetz Wissen | Fachplanung Sicherheitstechnik |

Zur Einordnung: Die Bundesnetzagentur referenziert die VDE-AR-N 4100 als maßgebliches Anschluss-Regelwerk. Den Bundesmusterwortlaut der TAB 2023 stellt der BDEW frei bereit, verbindlich vor Ort bleibt die TAB des Netzbetreibers. VDE FNN nennt bereits die Folgeausgabe VDE-AR-N 4100:2026-04; Ausgabestände gehören deshalb in gepflegte Vorlagen. Wie aus den Vorgaben der DIN 18015-1 eine belastbare Anschlussbewertung wird, zeigt der Beitrag [Leistungsbilanz nach DIN 18015-1](https://bimwired.com/landing/wissen/leistungsbilanz-din-18015-1.html).

## Warum ist der Spannungsfall ein Problemfall?

Der Spannungsfall ist der Nachweis mit den meisten Stolperfallen: Mehrere Regelwerke greifen mit unterschiedlichen Strecken und Grenzwerten ineinander, und die maßgebliche Norm wurde jahrelang unterschiedlich gelesen.

Die Grenzwerte verteilen sich auf zwei Abschnitte der Anlage. Vom Hausanschlusskasten bis zur Messeinrichtung gilt die 0,5-Prozent-Grenze. Nach dem frei verfügbaren Fachartikel „Spannungsfall richtig koordinieren" (D. Sofic, Zeitschrift „de" 21/2020) fordert die VDE-AR-N 4100 in Abschnitt 6.2.5 mit Bezug auf Paragraf 13 NAV, dass der Spannungsfall im Hauptstromversorgungssystem 0,5 % der Nennspannung nicht überschreitet; Bezugsgröße ist der Bemessungsstrom der Hausanschlusssicherung, bei Wohngebäuden mindestens 63 A. Hinter der Messeinrichtung empfiehlt die DIN 18015-1 für Wohngebäude höchstens 3 % bis zum Verbrauchsmittel (so der Fachartikel zur Norm in „de" 12/2020). Für Verbraucheranlagen allgemein nennt Tabelle G.52.1 der DIN VDE 0100-520:2013-06 laut einem elektro.net-Praxisproblem 3 % für Beleuchtung und 5 % für andere Verbraucher bei Versorgung aus dem öffentlichen Netz (Anlagentyp A), bei eigener Einspeisung (Anlagentyp B) 6 % beziehungsweise 8 %.

Abbildung: Diagramm mit vier Geraden für die Querschnitte 1,5 bis 6 mm²: Der Spannungsfall steigt mit der Leitungslänge, eine gestrichelte Linie markiert die Grenze von 3 Prozent. Beispielrechnung für einen Endstromkreis mit 230 V und 16 A: Je kleiner der Querschnitt, desto früher ist die 3-Prozent-Marke erreicht.

Wie fehleranfällig schon das Regelwerk selbst ist, zeigt die DIN VDE 0100-520. Die Fachzeitschrift Elektropraktiker dokumentiert, wie eine missverständliche Formulierung zu massiven Fehlinterpretationen führte: In einem dokumentierten Rechenbeispiel kam je nach Lesart eine zulässige Leitungslänge von 22,6 m oder von 3,59 m heraus, und die DKE musste nacharbeiten. Wer „einfach nachrechnet", braucht also zuerst die richtige Lesart und die richtige Bezugsstrecke.

In der Praxis läuft der Nachweis deshalb meist außerhalb des Modells. Das Revit-Modell wiederum liefert ohne gepflegte Trassenführung keine belastbaren Leitungslängen; ein Luftlinien- oder Achsmaß ist keine Nachweislänge. Deshalb steht der Spannungsfall in der Tabelle unten auf der Seite der Ingenieurleistung.

## Was ist regelhaft automatisierbar, was bleibt Ingenieurleistung?

Regelhaft automatisieren lässt sich, was ohne Rechenmodell aus Struktur und Attributen des Stromkreisplans folgt. Alles, was reale Längen, Verlegearten, Netzdaten oder Kennlinien braucht, bleibt Berechnung und Bewertung der Elektrofachkraft.

| Prüfung oder Nachweis | Regelhaft automatisierbar? | Warum, und wo es hingehört |
|---|---|---|
| Überlast-Plausibilität: Nennstrom der Sicherung gegen Leitungsquerschnitt | Ja, als Regelprüfung | Feste Zuordnungslisten decken den Standardfall; Abweichungen durch Häufung oder Wärme gehören zur Strombelastbarkeits-Bewertung |
| RCD-Pflicht je Stromkreis | Ja | Kreistyp und Raumart genügen; die 30-mA-Pflichtfälle nennt der DKE-Normenhinweis zur DIN VDE 0100-410 (siehe Prüfkette oben) |
| Mindestquerschnitte, etwa für Außenbereiche | Ja | Einfache Untergrenzen je Kreisart, aus Attributen prüfbar |
| Strukturregeln der Sicherheitstechnik: eigene Kreise, nicht hinter dem RCD allgemeiner Kreise | Ja | Aus der Plantopologie ablesbar; sinnvoll als Meldung, eine stille Korrektur wäre hier falsch |
| Zählregeln wie die Aufteilung der Stromkreise auf RCDs | Ja | Der Fachartikel zur DIN 18015-1 („de" 12/2020) nennt für die Anlagenverfügbarkeit höchstens zwei einphasige Endstromkreise je zweipoligem und sechs je vierpoligem FI-Schalter |
| Vorauswahl von Vorsicherungen nach fester Staffelregel | Ja, als Vorauswahl | Eine deterministische Auswahlregel liefert einen Startwert; sie ersetzt keinen Selektivitätsnachweis über Kennlinien |
| Spannungsfall mit realen Leitungslängen | Nein | Braucht Längen, Verlegeweg, Belastung und die richtige Bezugsstrecke; Berechnungswerkzeug plus Bewertung der Fachkraft |
| Strombelastbarkeit nach DIN VDE 0298-4:2023-06 | Nein | Hängt von Verlegeart, Häufung und Umgebungstemperatur ab; Tabellenwerk der Norm und Bewertung der Fachkraft |
| Selektivität | Nein | Verlangt Kennlinienvergleich mit Herstellerdaten in der Netzberechnung; zur Definition siehe Prüfkette oben (StromKompass) |
| Kurzschlussfestigkeit und Kurzschlussströme | Nein | Hängen von den Netzverhältnissen am Einspeisepunkt ab; Netzberechnung |
| Netzform und Schutzkonzept | Nein | Planerische Grundsatzentscheidung der Elektrofachkraft |

Der Maßstab ist einfach: Automatisierbar ist, was aus Plan-Attributen wie Kreistyp, Raumart, Querschnitt, Sicherungswert und Topologie folgt und bei gleichen Eingaben dieselbe Meldung erzeugt. Sobald reale Geometrie, physikalische Randbedingungen oder Netzdaten eingehen, ist es eine Berechnung; die gehört in Nachweiswerkzeuge und in die Verantwortung der Elektrofachkraft. KI verschiebt diese Grenze nicht. Ein Sprachmodell kann auf Auffälligkeiten hinweisen, ein Hinweis ist aber keine Normprüfung, und ich würde ihn nie als eine behandeln.

## Wie führen deutsche Büros die VDE-Nachweise heute?

Die Nachweispraxis deutscher Büros ist dreigeteilt: Tabellen und Einzelrechner für den Einzelfall, Netzberechnungs- und CAE-Software für größere Anlagen, Revit-Erweiterungen für die modellnahe Berechnung.

Am weitesten verbreitet ist die Handarbeit; ich habe sie selbst lange genug betrieben. In unserer eigenen Ansprache-Kartei haben wir bei 15 von 192 Büro-Profilen die VDE-Nachweise ausdrücklich als Schmerzpunkt vermerkt, typisch von uns notiert als Prüfung „Zeile für Zeile von Hand": Excel-Tabellen und Einzelrechner, je Stromkreis neu gefüttert, ohne Verbindung zum Modell. Das funktioniert. Es veraltet nur mit jeder Umplanung, weil selten jemand alle Zeilen nachzieht.

Darüber liegt die Berechnungswelt: Netzberechnungswerkzeuge wie Siemens Simaris decken Dimensionierung und Nachweise ab, CAE-Systeme führen die Dokumentation mit eigener Datenhaltung. Wer schon eine CAE-Landschaft betreibt, führt die Nachweise dort und zahlt mit doppelter Datenpflege zwischen Modell und Berechnungsprogramm. Der dritte Weg sind Revit-Erweiterungen wie MagiCAD, die laut tab-Advertorial genau die fehlende Spannungsfall- und Kabeldimensionierung nachrüsten, oder das Schulungs- und Werkzeugumfeld von BEEL (elkoBIM). Alle drei Wege sind etabliert; für den Alltag entscheidet, wie oft Gerätelisten, Stromkreise und Nachweise doppelt gepflegt werden.

## Was fängt eine Regelprüfung im modellgespeisten Workflow ab?

Eine Regelprüfung im modellgespeisten Workflow ist ein Sicherheitsnetz, kein Nachweis: Sie wendet feste, deterministische Regeln bei jeder Planänderung neu an und meldet Konflikte sofort, statt sie bis zur Schlussdurchsicht liegen zu lassen. Werkzeugneutral beschrieben läuft das so:

1. Die Elektro-Elemente kommen mit Raum, Ebene und Leistungsdaten strukturiert aus dem Revit-Modell.
2. Die Stromkreise werden im Plan-Editor strukturiert: Verteiler, Gruppen, Reserven, Kabelvorschläge.
3. Bei jeder Änderung laufen die Regelprüfungen mit: Überlast-Plausibilität, RCD-Pflicht, Mindestquerschnitte, Struktur- und Zählregeln.
4. Die Meldungen bewertet die Elektrofachkraft; die rechnerischen Nachweise (Spannungsfall, Strombelastbarkeit, Selektivität, Kurzschluss) laufen weiter im Berechnungswerkzeug.
5. Die Ergebnisse (Stromkreisnummern, Sicherungen, Kabel) gehen zurück ins Modell, damit Plan, Modell und Nachweisliste denselben Stand behalten.

Der Gewinn liegt weniger in der Automatik als darin, dass Konflikte auffallen, solange ihre Behebung wenig kostet, und dass im ganzen Büro dieselben Regeln gelten. So ist das Stromkreis-Modul von BimWired zugeschnitten; seine Regelprüfungen laufen beim Aufteilen der Stromkreise mit. Wo das Sicherheitsnetz endet, zeigt die Tabelle oben: am ersten Nachweis, der echte Längen oder Netzdaten braucht.

## Einordnung: das Werkzeug BimWired

BimWired ist unsere Cloud-Webanwendung mit Revit-Plugin (Revit 2025, 2026 und 2027) für Planungsbüros. Sicherheitstechnik wie RWA, BMZ, EMZ oder Brandschutztüren bekommt bei der automatischen Aufteilung eigene Kreise (B16A, 3x2,5 mm²), bewusst ohne RCD hinter eigenem Gruppenkopf. Hängt ein solcher Kreis doch hinter einem RCD, meldet die Prüfung den Konflikt mit Verweis auf DIN VDE 0100-560. D0-Vorsicherungen wählt die Aufteilung selektiv zum größten nachgelagerten Leitungsschutzschalter (1,6-facher Nennstrom nach DIN VDE 0100-530). Wer möchte, schaltet den KI-Prüfblick dazu: höchstens zehn Hinweise, die nie etwas am Plan ändern, ausdrücklich keine Normprüfung, sondern eine zweite Meinung, die Sie selbst prüfen.

Mir ist genauso wichtig, was BimWired nicht tut. Es berechnet keinen Spannungsfall, keine Strombelastbarkeit nach DIN VDE 0298-4, keine Selektivität und keine Kurzschlussfestigkeit. Diese Nachweise führen Sie weiterhin in Ihren Berechnungswerkzeugen. Die Regelprüfung ersetzt sie nicht; sie hält den Plan bis dahin widerspruchsfrei, und genau dieses Nachziehen hat mich in der eigenen Planungsarbeit die meiste Zeit gekostet. Die Ergebnisse (Stromkreisnummern, Sicherungen, Kabel) schreibt das Plugin nach Revit zurück, und aus denselben Daten entsteht der [Verteilerplan als Übersicht (einpolig)](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html).

## Häufige Fragen (FAQ)

### Kann Revit den Spannungsfall nach VDE berechnen?

Nein. Der Revit-Elektro-Spezialist BEEL hält auf der eigenen Themenseite fest, dass Revit keine vollständige Kabelberechnung nach DIN VDE bietet; ausdrücklich genannt werden Spannungsfall, Kurzschlussfestigkeit und Strombelastbarkeit. Der Nachweis entsteht deshalb in Einzelrechnern, Excel oder Berechnungssoftware, oder über Revit-Erweiterungen, deren zentrales Verkaufsargument laut einem Advertorial in der Fachzeitschrift tab genau diese Kabeldimensionierung ist.

### Spannungsfall: gelten 3 oder 5 Prozent?

Beides, je nach Strecke und Verbraucher. Tabelle G.52.1 der DIN VDE 0100-520:2013-06 nennt laut elektro.net für Anlagen am öffentlichen Netz (Typ A) 3 % für Beleuchtung und 5 % für andere Verbraucher, bei eigener Einspeisung (Typ B) 6 % beziehungsweise 8 %. Für Wohngebäude empfiehlt die DIN 18015-1 höchstens 3 % hinter der Messeinrichtung; davor gilt nach VDE-AR-N 4100 und Paragraf 13 NAV die Grenze von 0,5 % im Hauptstromversorgungssystem.

### Welche Prüfungen lassen sich beim Planen automatisieren?

Regelhaft prüfbar ist, was ohne Rechenmodell aus den Plan-Attributen folgt: die Überlast-Plausibilität von Sicherung und Querschnitt, die RCD-Pflicht nach Kreistyp und Raumart, Mindestquerschnitte, Zählregeln wie die Aufteilung der Stromkreise auf mehrere RCDs und Strukturregeln wie getrennte Kreise für die Sicherheitstechnik. Solche Prüfungen arbeiten deterministisch und melden Konflikte bei jeder Planänderung sofort.

### Was bleibt trotz Software Aufgabe der Elektrofachkraft?

Alle rechnerischen Nachweise und ihre Bewertung: der Spannungsfall mit realen Leitungslängen, die Strombelastbarkeit nach DIN VDE 0298-4 je Verlegeart, die Selektivität über Auslösekennlinien, die Kurzschlussfestigkeit sowie Netzform und Schutzkonzept. Die DKE stellt für das BIM-Umfeld klar, dass die Normenreihe DIN VDE 0100 verbindlich bleibt; die Verantwortung trägt die Fachkraft, nicht das Werkzeug.

### Mit welcher Software führen deutsche Büros die VDE-Nachweise heute?

Alle drei Wege sind etabliert; sie unterscheiden sich vor allem darin, wie oft dieselben Daten doppelt gepflegt werden.

### Ersetzt eine automatische Regelprüfung die Normprüfung nach VDE?

Nein. Eine Regelprüfung ist ein Sicherheitsnetz, das feste Plausibilitäts- und Strukturregeln laufend anwendet; sie führt keine rechnerischen Nachweise und ersetzt weder die Berechnung noch die Bewertung durch die Elektrofachkraft. Ich würde jedes Versprechen einer vollautomatischen VDE-Konformität an genau dieser Grenze messen.

## Quellen

1. BEEL: Revit Kabel (Themenseite Kabelplanung). https://www.beel.de/revit/revit-kabel/ (abgerufen am 25.08.2026)
2. tab: MagiCAD-Advertorial zur Elektroplanung in Revit. https://www.tab.de/artikel/advertorial-magicad-so-koennen-sie-in-revit-auch-elektro-planen-4021922.html (abgerufen am 25.08.2026)
3. DKE: Building Information Modeling (Arbeitsfeld-Seite). https://www.dke.de/de/arbeitsfelder/industry/building-information-modeling (abgerufen am 25.08.2026)
4. DKE: Hinweise zum erleichterten Umgang mit DIN VDE 0100-410. https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/konzept-0100-410 (abgerufen am 25.08.2026)
5. elektrofachkraft.de: DIN VDE 0298-4, Strombelastbarkeit von Kabeln und Leitungen. https://www.elektrofachkraft.de/sicheres-arbeiten/din-vde-0298-4-strombelastbarkeit-von-kabeln-und-leitungen (abgerufen am 25.08.2026)
6. D. Sofic: Spannungsfall richtig koordinieren, Zeitschrift „de" 21/2020 (Volltext-PDF). https://www.elektro.net/media/file/rRnRreLDo4/570b31f0/DE_2020_21_20-26_EA41_LOW.pdf (abgerufen am 25.08.2026)
7. elektro.net: Elektroplanung in Wohngebäuden (zur DIN 18015-1:2020-05), Zeitschrift „de" 12/2020 (Volltext-PDF). https://www.elektro.net/media/file/Kwqzk199w7/fd7e48cc/DE_12_2020_31-34_EA42neu.pdf (abgerufen am 25.08.2026)
8. elektro.net Praxisproblem: Spannungsfall in Verbraucheranlagen nach VDE 0100-520, Tabelle G.52.1. https://www.elektro.net/praxisprobleme/spannungsfall-in-verbraucheranlagen-nach-vde-0100-520-tabelle-g-52-1/ (abgerufen am 25.08.2026)
9. Elektropraktiker: DIN VDE 0100-520, der Spannungsfall als Problemfall. https://www.elektropraktiker.de/nachrichten/nachricht/din-vde-0100-520-der-spannungsfall-als-problemfall?p=all (abgerufen am 25.08.2026)
10. ElekRechner: Spannungsfall-Rechner. https://www.elekrechner.com/rechner/leitung/spannungsfall (abgerufen am 25.08.2026)
11. VDE FNN: Technische Anschlussregeln Niederspannung (TAR Niederspannung). https://www.vde.com/de/fnn/themen/tar/tar-niederspannung (abgerufen am 25.08.2026)
12. BDEW: TAB 2023, Technische Anschlussbedingungen Strom. https://www.bdew.de/energie/tab-2023/ (abgerufen am 25.08.2026)
13. Bundesnetzagentur, Beschlusskammer 6: VDE-AR-N 4100 (amtliche Referenzierung). https://www.bundesnetzagentur.de/DE/Beschlusskammern/BK06/BK6_92_exLink/VDE-AR-N_4100.html (abgerufen am 25.08.2026)
14. StromKompass ElektroSpicker #008: Selektivität. https://stromkompass.de/elektrospicker/selektivitaet/ (abgerufen am 25.08.2026)
15. BauNetz Wissen: Elektroinstallation in öffentlichen Einrichtungen und Arbeitsstätten (DIN VDE 0100-718). https://www.baunetzwissen.de/elektro/fachwissen/elektroinstallation-in-gebaeuden/elektroinstallation-in-oeffentlichen-einrichtungen-und-arbeitsstaetten-5266336 (abgerufen am 25.08.2026)
16. Eigene Ansprache-Kartei von BimWired: 192 von uns durchgesehene, öffentlich zugängliche Büro-Profile mit einem von uns notierten Ansatzpunkt je Büro (Stand August 2026, unveröffentlicht, nicht repräsentativ).

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
