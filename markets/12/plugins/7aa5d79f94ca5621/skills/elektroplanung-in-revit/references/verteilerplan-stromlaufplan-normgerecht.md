---
titel: "Verteilerplan normgerecht erstellen: Begriffe, Normen und der Weg aus dem Modell"
quelle: https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html
stand: 2026-08-25
art: artikel
fragen:
  - "Was gehört in einen normgerechten Verteilerplan?"
  - "Was ist der Unterschied zwischen Stromlaufplan, Übersichtsschaltplan, Verteilerplan und Installationsplan?"
  - "Welche Normen gelten für Verteilerplan und Stromlaufplan?"
  - "Wie entsteht ein Verteilerplan aus dem Revit-Modell?"
  - "Welche Software erzeugt einen normgerechten Verteilerplan aus Revit?"
---

# Verteilerplan normgerecht erstellen: Begriffe, Normen und der Weg aus dem Modell

Ein normgerechter Verteilerplan ist die aufgelöste, einpolige Übersicht eines Verteilers: je Abgang das Betriebsmittelkennzeichen, das Schutzorgan mit seinen Kenndaten, die RCD-Zuordnung, Kabeltyp mit Querschnitt und Klemmen, dazu Schriftfeld und Revisionsstand. Den Rahmen setzen DIN EN 61082-1 für die Dokumentation, IEC 60617 für die Schaltzeichen, EN IEC 81346 für die Kennzeichnung und DIN EN ISO 7200 für das Schriftfeld; den gebauten Verteiler selbst regelt die DIN EN IEC 61439. Aus dem Revit-Modell entsteht dieser Plan heute meist in Doppelarbeit in einem zweiten Werkzeug. Modellgespeiste Wege lesen die Stromkreisdaten aus dem Modell, erzeugen daraus den Plan und schreiben Stromkreisnummern, Sicherungen und Kabel an die Bauteile zurück.

## Das Wichtigste in Kürze

- Vier Begriffe, vier Dokumente: Die einpolige Übersicht zeigt die Struktur, der allpolige Stromlaufplan jede Ader, der Installationsplan die Lage im Grundriss, das Stromkreisverzeichnis die Tabelle je Verteiler. Selbst Fachleute fragen im elektrikforum.de nach, was was ist.
- Normrahmen: DIN EN 61082-1 (Dokumentation), IEC 60617 (Schaltzeichen, laut VDE VERLAG rund 1.900 Symbole), EN IEC 81346 (Referenzkennzeichnung), DIN EN IEC 61439 (der Verteiler als Erzeugnis), DIN EN ISO 7200 (Schriftfeld).
- Dokumentation ist Pflicht: DIN VDE 0100-510, Abschnitt 514.5 verlangt Unterlagen zu Stromkreisen, Leitern, Kabelarten und Schutzeinrichtungen. Die rechtlichen Anker liegen laut dem Fachbeitrag von Stefan Euler unter anderem in Paragraf 49 EnWG und Paragraf 13 NAV.
- Der übliche Bruch: Modell in Revit, Schema daneben. In unserer eigenen Ansprache-Kartei haben wir das bei 69 von 192 Büro-Profilen genau so vermerkt.
- Ohne Rückweg keine Konsistenz: Werden Stromkreisnummern, Sicherungen und Kabel nicht ins Modell zurückgeschrieben, laufen Plan und Modell bei der ersten Änderung auseinander.

## Überblick

| Punkt | Detail |
|---|---|
| Dokumenttyp | Übersicht (einpolig): aufgelöste Einlinien-Darstellung je Verteiler, ergänzt um das Stromkreisverzeichnis |
| Maßgebliche Normen | DIN EN 61082-1, IEC 60617, EN IEC 81346, DIN EN ISO 7200; DIN EN IEC 61439 für das Erzeugnis |
| Pflichtinhalte | Stromkreise mit Verbrauchern, Leiterzahl und Querschnitt, Kabelart, Schutzeinrichtungen samt Einbauort (DIN VDE 0100-510, Abschnitt 514.5) |
| Rechtsrahmen | Dokumentationspflichten unter anderem nach Paragraf 49 EnWG und Paragraf 13 NAV (Fachbeitrag Euler) |
| Typischer Bruch | Modell in Revit, Schema separat gezeichnet; in unserer Ansprache-Kartei bei 69 von 192 Büro-Profilen so vermerkt |
| Übergabeformate | Papier im Verteiler, mehrseitiges Vektor-PDF zur Prüfung, DXF zur Weiterbearbeitung |

## Inhalt

- Welcher Plan heißt wie? Die Begriffe im Überblick
- Welche Normen gelten für den Verteilerplan?
- Was gehört in einen normgerechten Verteilerplan?
- Warum entsteht der Verteilerplan heute doppelt?
- Wie entsteht der Verteilerplan aus dem Revit-Modell?
- Papier, PDF oder DXF: welches Übergabeformat wofür?
- So hilft BimWired
- Häufige Fragen (FAQ)
- Quellen

## Welcher Plan heißt wie? Die Begriffe im Überblick

Übersichtsschaltplan, Stromlaufplan, Verteilerplan, Installationsplan: vier Begriffe für vier verschiedene Dokumente, die im Alltag munter durcheinandergehen. Auch in meinen Projektbesprechungen meint mit „Stromlaufplan" jeder etwas anderes. Die Foren zeigen dasselbe Bild. Im elektrikforum.de fragen Fachleute in einem Thread vom Dezember 2022, was die Planarten unterscheidet und was ein Elektroplaner nach HOAI liefern muss; brauchbare Beispiele seien online kaum zu finden. Im KNX-User-Forum sammelt ein Fragesteller für denselben Zweck Behelfe, von Stromlaufplan.de über Herstellerwerkzeuge bis Excel.

Abbildung: Vier Felder zeigen denselben Endstromkreis als einpolige Übersicht, als allpoligen Stromlaufplan mit getrennten Leitern und nummerierten Strompfaden, als Grundriss mit Symbolen und Leitungsweg und als Frontansicht des Reihenverteilers. Dieselbe Anlage, vier Dokumentarten: Schutzorgan, RCD, Kabel und Verbraucher sind in jedem Feld dieselben, nur die Sicht darauf wechselt.

| Planart | Darstellung | Zweck und typischer Inhalt | Wer ihn in der Praxis meist erstellt |
|---|---|---|---|
| Übersichtsschaltplan (Übersicht, einpolig) | Einpolig: eine Linie steht für alle Außenleiter | Struktur der Anlage: Einspeisung, Verteiler, Abgänge mit Schutzorganen und Kabeln | Elektrofachplanung |
| Stromlaufplan in aufgelöster Darstellung (allpolig) | Jeder Leiter und jedes Kontaktelement einzeln, nach Strompfaden geordnet | Wirkungsweise einzelner Schaltungen (Steuerungen, Verriegelungen, Tasterschaltungen) | Elektrofachplanung, Steuerungs- und Schaltschrankbau |
| Verteilerplan mit Stromkreisverzeichnis | Einpolige Übersicht je Verteiler plus tabellarisches Verzeichnis | Alle Abgänge eines Verteilers: Kennzeichen, Sicherung, RCD-Zuordnung, Kabel, Raum- oder Funktionstext | Elektrofachplanung, fortgeschrieben durch den Errichter |
| Installationsplan | Grundriss mit Symbolen | Lage von Auslässen, Schaltern, Leuchten und Leitungswegen für die Ausführung | Elektrofachplanung, genutzt auf der Baustelle |
| Aufbauplan (Ansicht des Verteilers) | Maßstäbliche Front- oder Innenansicht | Anordnung der Geräte und Klemmen im Schrank | Schaltschrankbau, Hersteller der Schaltgerätekombination |

„Aufgelöst" bedeutet: Die Darstellung folgt den Strompfaden und nicht der geometrischen Anordnung der Geräte. In diesem Artikel geht es um die aufgelöste einpolige Übersicht je Verteiler mit Stromkreisverzeichnis, im Sprachgebrauch „Verteilerplan" oder „Verteilerschema". Was davon in welcher Leistungsphase geschuldet ist, regeln Vertrag und Leistungsbild.

## Welche Normen gelten für den Verteilerplan?

Beim Verteilerplan greifen fünf Normbereiche ineinander: Dokumentationsregeln, Schaltzeichen, Referenzkennzeichnung, Schriftfeld samt Schrift und die Produktnorm für den gebauten Verteiler. Wer die Zuständigkeiten auseinanderhält, weiß, was die Zeichnung leisten muss und was nicht.

| Norm | Regelt | Bedeutung für den Verteilerplan |
|---|---|---|
| DIN EN 61082-1 | Ausführung elektrotechnischer Dokumente: Dokumentarten, Darstellung, Querverweise | Grundlage für den Blattaufbau und die Verweise zwischen Blättern und Stromkreisen |
| IEC 60617 | Schaltzeichen; laut VDE VERLAG als Datenbank mit etwa 1.900 Symbolen gepflegt, welche die gedruckten Teile 2 bis 13 ersetzt | Zeichenvorrat für Schutzorgane, Zähler und Betriebsmittel |
| EN IEC 81346 | Referenzkennzeichnung über die Aspekte Funktion „=", Ort „+", Produkt „-"; Kennbuchstaben in Teil 2 (so der EPLAN-Blog) | Eindeutige Betriebsmittelkennzeichen im Plan, im Verteiler und im Modell |
| DIN EN IEC 61439 | Niederspannungs-Schaltgerätekombinationen, also das Erzeugnis Verteiler | Betrifft Bau und Nachweise des Schranks, nicht die Planzeichnung |
| DIN EN ISO 7200 und DIN EN ISO 3098 | Schriftfeld technischer Zeichnungen und die Schrift darin (Grundregeln laut technisches-zeichnen.net; Normnachweis DIN EN ISO 3098-1:2015-06) | Einheitliches Schriftfeld mit Planstand, lesbare Beschriftung |

Die DIN EN IEC 61439 wird gern mit den Zeichnungsnormen in einen Topf geworfen. Sie ist aber die Produktnorm für den Verteiler selbst. Laut ZVEI-Informationsblatt (Januar 2022) gilt die Reihe seit 2010, die Vorgängernorm DIN EN 60439 wurde 2012 ungültig, und die Teile 1 und 2 liegen seit Oktober 2021 als Edition 3 vor. Verlangt werden Bauartnachweis und Stücknachweis; der Stücknachweis ersetzt den früheren Stückprüfbericht, so erläutert es elektrofachkraft.de. Für die Planung heißt das: Der Verteilerplan dokumentiert die Stromkreise, die Nachweise für den gebauten Schrank führt der Schaltschrankbauer.

## Was gehört in einen normgerechten Verteilerplan?

Die Mindestinhalte folgen aus der Dokumentationspflicht. Nach DIN VDE 0100-510, Abschnitt 514.5 gehören zur Anlage Unterlagen, aus denen Art und Aufbau der Stromkreise hervorgehen: die versorgten Verbraucher, Anzahl und Querschnitt der Leiter, die Art der Kabel und Leitungen sowie die Merkmale, an denen sich Schutz-, Trenn- und Schalteinrichtungen erkennen und verorten lassen. Der frei zugängliche Fachbeitrag von Stefan Euler referiert diesen Katalog und nennt als rechtliche Anker unter anderem Paragraf 49 EnWG und Paragraf 13 NAV.

Ein vollständiger Verteilerplan beantwortet je Verteiler mindestens diese Punkte:

1. Einspeisung und Zuleitung, also die Herkunft (Hausanschluss oder übergeordneter Verteiler), das Kabel und die Vorsicherung. Wie groß der Anschluss bemessen sein muss, klärt vorab die [Leistungsbilanz nach DIN 18015-1](https://bimwired.com/landing/wissen/leistungsbilanz-din-18015-1.html).
2. Zähl- und Messplätze. Für Wohngebäude nennt der Fachartikel „Elektroplanung in Wohngebäuden" (Zeitschrift „de", Ausgabe 12/2020) zur DIN 18015-1:2020-05 mindestens 63 A Bemessungsstrom für den Zählerplatz.
3. Ein Betriebsmittelkennzeichen je Abgang, damit Plan, Verteilerbeschriftung und Modell dasselbe Element meinen. Die Systematik dafür liefert die EN IEC 81346.
4. Schutzorgane mit Kenndaten und RCD-Zuordnung: Leitungsschutzschalter mit Charakteristik und Nennstrom, RCDs mit Bemessungsdifferenzstrom und den zugeordneten Kreisen. Nach DIN VDE 0100-410:2018-10 brauchen Steckdosen-Endstromkreise bis 32 A und in Wohnungen auch Endstromkreise mit Leuchten einen RCD mit höchstens 30 mA (frei zugänglich erläutert im DKE-Normenhinweis). Derselbe „de"-Fachartikel empfiehlt höchstens zwei einphasige Endstromkreise je zweipoligem und sechs je vierpoligem RCD.
5. Kabel und Leitung je Abgang mit Typ, Aderzahl und Querschnitt, genau die Angaben, die DIN VDE 0100-510 verlangt.
6. Klemmen, Stromkreisbezeichnungen und Raumtexte. Daraus entsteht das Stromkreisverzeichnis für die Verteilertür.
7. Reserve und Revisionsstand. Der „de"-Fachartikel empfiehlt 20 % Platzreserve im Stromkreisverteiler; dokumentierte Reserveabgänge zeigen, wann sie aufgebraucht ist. Planstand und Revisionstabelle trägt das Schriftfeld nach DIN EN ISO 7200.

Abbildung: Schematisches A3-Blatt eines Verteilerplans mit Sammelschienen, Zählerplatz, RCD-Gruppe, fünf Abgängen mit Schutzorganen und Klemmen, Fußzeilen für Stromkreis, Kabel und Beschreibung sowie Schriftfeld und Revisionszeile unten rechts. Die Fahnen 1 bis 7 sitzen dort, wo die sieben Punkte der Liste im Blatt tatsächlich auftauchen.

Fehlt eine dieser Angaben, ist der Plan nicht falsch, aber unvollständig. Errichter oder Prüfer suchen sie sich dann anderswo zusammen; ich habe solche Lücken oft genug selbst gestopft, meist unter Zeitdruck.

## Warum entsteht der Verteilerplan heute doppelt?

Foren, Anbieterseiten und unsere eigene Marktrecherche sagen dasselbe: Das Modell entsteht in Revit, der Verteilerplan daneben in einem zweiten Werkzeug, und beide Stände werden von Hand synchron gehalten. In unserer eigenen Ansprache-Kartei (192 von uns durchgesehene, öffentlich zugängliche Profile von Elektro- und TGA-Planungsbüros aus Deutschland, Österreich und der Schweiz, Stand August 2026) haben wir dieses Muster bei 69 Profilen vermerkt; es ist der von uns am zweithäufigsten notierte Ansatzpunkt. Der Vermerk stammt von uns, nicht von den Büros, und die Kartei ist weder repräsentativ noch neutral erhoben. Ich habe den Plan selbst lange neben dem Modell gezeichnet und weiß, wie schnell die beiden Stände auseinanderlaufen.

Die Revit-Bordmittel füllen die Lücke nicht. Mensch und Maschine dokumentiert, dass die Standardvorlagen „keine Beschriftung für elektrische Ausstattungen wie Schalter, Steckdosen und Verteilungen" enthalten und dass sich die Stromkreis-Benennung erst seit Revit 2021 konfigurieren lässt. Als Verteilerdokumentation liefern die Bordmittel Panel Schedules, also Tabellen nach US-Konvention. Wer im Autodesk-Forum nach einem Einlinienschema fragt, bekommt von erfahrenen Anwendern den Rat, es mit Linien und Detailelementen zu zeichnen, „wie früher in AutoCAD", oder es in AutoCAD anzulegen und zu verknüpfen. Beides heißt: kein Modellbezug, keine automatische Aktualisierung.

Auch Anbieter, die von Revit leben, sprechen die Lücke offen an. BEEL, Spezialist für Revit-Elektroplanung mit eigenem Add-in, schreibt, dass Revit allein die Anforderungen der DIN EN 61082 nicht vollständig erfüllt und Verteilerschemata Handarbeit erfordern. Der CAE-Hersteller eXs bewirbt die bidirektionale Übergabe von Revit-Stromkreisdaten in automatische Verteilerpläne samt Rückübertragung der Sicherungskennzeichen als Schließen einer „wichtigen Lücke im BIM-Prozess". Wenn sich um eine Lücke ein eigener Werkzeugmarkt bildet, ist sie real.

Was die Doppelarbeit kostet, folgt immer demselben Muster: Jede Umplanung muss zweimal nachgezogen werden, und keinem der beiden Stände sieht man an, ob das passiert ist. Die Abweichungen fallen dann dort auf, wo Korrekturen am teuersten sind, in der Prüfung, auf der Baustelle oder bei der Inbetriebnahme.

## Wie entsteht der Verteilerplan aus dem Revit-Modell?

Auf einem modellgespeisten Weg ist der Verteilerplan eine Sicht auf Daten, die im Modell schon stecken, keine eigenständige Zeichnung. Unabhängig vom Werkzeug hat der Rundlauf sieben Schritte:

1. Modell qualifizieren. Leuchten, Schalter, Steckdosen und Geräte brauchen Anschlussdaten (Leistung, Spannung, Polzahl) und eine saubere Raum- und Ebenenzuordnung. Wie das in Revit aufgesetzt wird, zeigt der Artikel [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html).
2. Elementdaten strukturiert auslesen: je Element ein Datensatz mit Raum, Ebene und Anschlusswerten, kein Zeichnungsexport.
3. Stromkreise bilden und Verteiler strukturieren: Gruppen nach Ebene und Nutzung, Zähler, Vorsicherungen, Reserveabgänge.
4. Prüfen, bevor gezeichnet wird. Regeln wie RCD-Pflicht, Überlast und Mindestquerschnitte laufen auf den Daten. Was sich davon automatisieren lässt und was Ingenieurleistung bleibt, ordnet der Artikel [VDE-Prüfung in der Elektroplanung mit Revit](https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html) ein.
5. Plan nach Darstellungsregeln erzeugen: je Verteiler eine aufgelöste einpolige Übersicht mit Kennzeichen, Schutzorganen, Kabeln, Klemmen, Schriftfeld und Querverweisen.
6. Ergebnisse zurückschreiben. Stromkreisnummern, Sicherungen und Kabeltypen wandern als Parameter an die Bauteile; erst dann stimmen Beschriftungen und Listen in Revit mit dem Plan überein.
7. Änderungen wiederholen statt nachzeichnen. Bei einer Umplanung läuft derselbe Weg noch einmal, die Revisionstabelle hält den Stand fest.

Schritt 6 ist für mich der entscheidende. Ohne den Rückweg bleibt auch ein erzeugter Plan eine Zeichnung nebenher; nicht zufällig bewirbt eXs genau diese Rückübertragung. BimWired bildet den Rundlauf ebenfalls ab, mit den Revit-Befehlen „Stromkreisplan senden" und „Stromkreise übernehmen" und einem Plan-Editor im Browser.

## Papier, PDF oder DXF: welches Übergabeformat wofür?

Ein Verteilerplan wird an drei Stellen gebraucht: als Blatt im Verteiler, als Prüf- und Lieferdokument und als Datei für die Weiterbearbeitung. Jede Stelle stellt eigene Anforderungen an das Format.

- Papier im Verteiler. Stromkreisverzeichnis an der Tür und Plan beim Schrank sind gelebte Praxis. Hier zählen Lesbarkeit und ein eindeutiger Revisionsstand.
- Vektor-PDF für Prüfung und Lieferung. Mehrseitig und vektorbasiert bleibt es beim Zoomen scharf, und der Text ist durchsuchbar.
- DXF für die Weiterbearbeitung. Schaltschrankbau und CAE-Werkzeuge brauchen getrennte Layer (Rahmen, Leitungen, Symbole, Klemmen, Beschriftung) und Text, der Text bleibt, statt in Linienzüge zu zerfallen. Ein Export in Millimetern im Maßstab 1:1 erspart das Rätselraten über die Skalierung.

Wer den Plan aus Daten erzeugt, bekommt alle drei Formate aus demselben Stand. Wer von Hand zeichnet, pflegt drei Dateien.

## Einordnung: das Werkzeug BimWired

Die Daten holt der Revit-Befehl „Stromkreisplan senden" aus dem Modell (Leuchten, Schalter, Steckdosen und Elektrogeräte mit Raum, Ebene und Anschlusswerten). Im Browser strukturieren Sie Verteiler, Stromkreise, Zähler und Reservezeilen, auf Wunsch mit automatischer Aufteilung. Feste Prüfungen decken Überlast, RCD-Pflicht, Mindestquerschnitte und DIN-18015-Bezüge ab. Den Rückweg habe ich eingebaut, weil er mir beim Zeichnen von Hand am meisten gefehlt hat: „Stromkreise übernehmen" schreibt Stromkreisnummern und je Einstellung Verteiler, Funktion, Beschreibung, Sicherung, RCD, Kabel und Phasen an die Bauteile zurück, fehlende Projektparameter legt das Plugin an, und ein Rückgängig-Schritt ist vorgesehen. Exportiert wird als Druck (A3), mehrseitiges Vektor-PDF und DXF je Blatt (Millimeter, 1:1, getrennte Layer, Text bleibt Text). QR-Etiketten je Verteiler führen auf ein öffentliches, widerrufbares Lese-Stromkreisverzeichnis ohne Personennamen und Projektdaten, optional mit Codewort. Zur Einordnung: Das Blatt ist bewusst eine Übersicht (einpolig). Es ist kein Installationsplan, keine Allpolig-Darstellung, kein Aufbauplan des Schranks und zeigt keine interne Geräteverdrahtung.

## Häufige Fragen (FAQ)

### Was ist der Unterschied zwischen Stromlaufplan und Übersichtsschaltplan?

Ein Übersichtsschaltplan (meist einpolig) zeigt die Struktur einer Anlage: Einspeisung, Verteiler und Abgänge mit ihren Schutzorganen, wobei eine Linie für alle Leiter steht. Ein Stromlaufplan in aufgelöster, allpoliger Darstellung zeichnet jeden Leiter und jedes Kontaktelement einzeln; so lässt sich die Wirkungsweise einer Schaltung nachvollziehen. Für die Dokumentation eines Wohnungs- oder Etagenverteilers ist die einpolige Übersicht die übliche Form.

### Was muss ein Verteilerplan mindestens enthalten?

Aus der Dokumentation müssen nach DIN VDE 0100-510 (Abschnitt 514.5) Art und Aufbau der Stromkreise hervorgehen: versorgte Verbraucher, Anzahl und Querschnitt der Leiter, Art der Kabel und Leitungen sowie Identifizierung und Einbauorte der Schutz-, Trenn- und Schalteinrichtungen (so referiert im Fachbeitrag von Stefan Euler). In der Praxis kommen Betriebsmittelkennzeichen, RCD-Zuordnung, Klemmen, Raum- oder Funktionstexte, Reserveabgänge und eine Revisionstabelle im Schriftfeld hinzu.

### Gilt die DIN EN IEC 61439 für die Planzeichnung?

Nein. Die Reihe DIN EN IEC 61439 ist die Produktnorm für Niederspannungs-Schaltgerätekombinationen, also für den gebauten Verteiler; laut ZVEI gilt sie seit 2010, die Teile 1 und 2 liegen seit Oktober 2021 als Edition 3 vor. Sie verlangt Bauartnachweis und Stücknachweis des Herstellers (erläutert bei elektrofachkraft.de). Die Zeichnung selbst folgt den Dokumentationsnormen, allen voran der DIN EN 61082-1.

### Kann Revit ohne Zusatzwerkzeug einen deutschen Verteilerplan erzeugen?

Die Bordmittel erzeugen Panel Schedules, also Verteilertabellen nach US-Konvention, und die Standardvorlagen enthalten laut Mensch und Maschine keine Beschriftungen für Schalter, Steckdosen und Verteilungen. Für ein Einlinienschema raten erfahrene Anwender im Autodesk-Forum dazu, es mit Linien und Detailelementen zu zeichnen, „wie früher in AutoCAD". In der Praxis entsteht ein normgerechter deutscher Verteilerplan deshalb mit einem Zusatzwerkzeug oder in einem zweiten Programm.

### Ersetzt die einpolige Übersicht den Aufbauplan des Verteilers?

Nein. Die Übersicht (einpolig) dokumentiert Struktur, Absicherung und Kabel der Stromkreise; der Aufbauplan zeigt die geometrische Anordnung der Geräte im Schrank und entsteht im Schaltschrankbau. Auch die interne Geräteverdrahtung gehört nicht in die Übersicht, sondern zu den Unterlagen des Herstellers der Schaltgerätekombination nach DIN EN IEC 61439.

## Quellen

1. BEEL: Revit Stromlaufplan. https://www.beel.de/revit/revit-stromlaufplan/ (abgerufen am 25.08.2026)
2. Autodesk-Forum (Revit MEP): Electrical single line diagram. https://forums.autodesk.com/t5/revit-mep-forum/electrical-single-line-diagram/td-p/8667884 (abgerufen am 25.08.2026)
3. eXs: Elektroplanung in BIM-Projekten. https://www.exs-cae.com/elektroplanung-in-bim-projekten/ (abgerufen am 25.08.2026)
4. elektrikforum.de: Unterschied verschiedener Planarten. https://www.elektrikforum.de/threads/unterschied-verschiedener-planarten.41491/ (abgerufen am 25.08.2026)
5. KNX-User-Forum: Verteilerplan, wie komme ich zu einem Plan für den Stromverteiler. https://knx-user-forum.de/forum/supportforen/stromlaufplan-de/1823759-verteilerplan-wie-komme-ich-zu-einem-plan-f%C3%BCr-den-stromverteiler (abgerufen am 25.08.2026)
6. Mensch und Maschine: Revit MEP 2021, Benennung elektrischer Stromkreise. https://support.mum.de/help/de-de/70-revit-mep/200-revit-mep-2021-benennung-elektrischer-stromkreise (abgerufen am 25.08.2026)
7. ZVEI: Informationsblatt Norm für Niederspannungs-Schaltgerätekombinationen DIN EN IEC 61439 Edition 3 (PDF, Januar 2022). https://www.zvei.org/fileadmin/user_upload/Presse_und_Medien/Publikationen/2022/Januar/Neue_Informationsnbroschueren_des_Fachkreises_Niederspannung/1_Informationsblatt_NeueNorm_final_2022.pdf (abgerufen am 25.08.2026)
8. elektrofachkraft.de: DIN EN 61439, Anforderungen an Niederspannungs-Schaltgerätekombinationen. https://www.elektrofachkraft.de/sicheres-arbeiten/normenreihe-din-en-61439-niederspannungs-schaltgeraetekombination (abgerufen am 25.08.2026)
9. EPLAN-Blog: Normgerecht strukturieren und referenzieren nach EN IEC 81346. https://www.eplan.com/de-de/blog/software/normgerecht-strukturieren-und-referenzieren (abgerufen am 25.08.2026)
10. VDE VERLAG: IEC 60617, Schaltzeichen-Datenbank (Produktseite). https://www.vde-verlag.de/iec-normen/iec-datenbanken/iec-60617-schaltzeichen.html (abgerufen am 25.08.2026)
11. technisches-zeichnen.net: Schriftelemente und Schrift. https://www.technisches-zeichnen.net/technisches-zeichnen/grundkurs-01/schrift.php (abgerufen am 25.08.2026)
12. DIN Media: DIN EN ISO 3098-1:2015-06 (Normnachweis). https://www.dinmedia.de/en/standard/din-en-iso-3098-1/232192579 (abgerufen am 25.08.2026)
13. Stefan Euler: Dokumentation elektrischer Anlagen. Rechtssicherheit für Errichter und Betreiber (Fachbeitrag, PDF). https://expertennetzwerk-elektrotechnik.de/wp-content/uploads/2018/10/Fachbeitrag_Stefan_Euler_Dokumentation-elektrischer-Anlagen.pdf (abgerufen am 25.08.2026)
14. DKE: Hinweise zum erleichterten Umgang mit DIN VDE 0100-410. https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/konzept-0100-410 (abgerufen am 25.08.2026)
15. elektro.net: Elektroplanung in Wohngebäuden (Fachartikel, Zeitschrift „de" 12/2020, Volltext-PDF). https://www.elektro.net/media/file/Kwqzk199w7/fd7e48cc/DE_12_2020_31-34_EA42neu.pdf (abgerufen am 25.08.2026)
16. Eigene Ansprache-Kartei von BimWired: 192 von uns durchgesehene, öffentlich zugängliche Büro-Profile mit einem von uns notierten Ansatzpunkt je Büro (Stand August 2026, unveröffentlicht, nicht repräsentativ).

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
