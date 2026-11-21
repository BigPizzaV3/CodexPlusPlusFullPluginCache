---
titel: "Stromkreise in Revit planen: von der US-Logik zum deutschen Verteilerplan"
quelle: https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html
stand: 2026-08-25
art: artikel
fragen:
  - "Wie plane ich Stromkreise in Revit nach deutschen Konventionen?"
  - "Warum kann ich in Revit keinen Stromkreis anlegen?"
  - "Wie weise ich einem Verteiler in Revit ein Verteilersystem zu?"
  - "Welche Voraussetzungen müssen Revit-Familien für Stromkreise erfüllen?"
  - "Wie komme ich vom Panel Schedule zum deutschen Verteilerplan?"
---

# Stromkreise in Revit planen: von der US-Logik zum deutschen Verteilerplan

Revit kann Stromkreise bilden, Lasten je Verteiler summieren und daraus Panel Schedules erzeugen. Es denkt dabei allerdings in US-Konzepten: Ohne Spannungsdefinitionen, ohne zugewiesenes Verteilersystem (Distribution System) und ohne passende elektrische Anschlüsse in den Familien entsteht kein einziger Stromkreis. Für deutsche Projekte richten Sie deshalb zuerst die Spannungswelt mit 230 V und 400 V ein, arbeiten mit Familien, die Spannung, Polzahl und Scheinleistung tragen, und stellen die Stromkreis-Benennung um, was laut Mensch und Maschine erst seit Revit 2021 geht. Für den Verteilerplan nach deutschem Dokumentationsverständnis braucht es danach noch einen eigenen Weg, denn das Ergebnis der Bordmittel bleibt eine Tabelle nach US-Konvention.

## Das Wichtigste in Kürze

- Ein Stromkreis entsteht in Revit nur, wenn Panel Name, Verteilersystem und der elektrische Anschluss der Familie zusammenpassen. An dieser Kette scheitern Einsteiger regelmäßig; ein dokumentierter Thread im Autodesk-Forum zeigt es.
- Die Standardvorlagen enthalten laut Mensch und Maschine „keine Beschriftung für elektrische Ausstattungen wie Schalter, Steckdosen und Verteilungen“. Die Benennung elektrischer Stromkreise lässt sich erst seit Revit 2021 konfigurieren.
- Familien brauchen elektrische Anschlüsse (Connectors) mit Spannung, Polzahl und Scheinleistung in VA, sonst lässt sich kein Stromkreis bilden.
- Das Bordmittel-Ergebnis ist ein Panel Schedule, eine Verteilertabelle nach US-Konvention. Ein deutscher Verteilerplan im Umfeld der Dokumentennorm DIN EN 61082 entsteht daraus nicht von selbst.
- Deutsche Büros ergänzen die Bordmittel deshalb um gezeichnete Schemata, um Elektro-Add-ins wie BEEL/elkoBIM oder MagiCAD oder um einen modellgespeisten Editor außerhalb von Revit.

## Überblick

| Punkt | Detail |
|---|---|
| Bordmittel | Stromkreise, Lastsummen je Verteiler, Panel Schedules; Stromkreis-Benennung seit Revit 2021 konfigurierbar (Mensch und Maschine) |
| Einstiegshürde | Panel Name, Verteilersystem und Familienanschluss müssen zusammenpassen, sonst kommt kein Stromkreis zustande (Autodesk-Forum) |
| Vorlagen | Standardvorlagen ohne deutsche Beschriftungen für Schalter, Steckdosen und Verteilungen (Mensch und Maschine) |
| Familien | Pflicht ist ein elektrischer Anschluss mit Spannung, Polzahl und Scheinleistung; deutsche Schaltzeichen nach IEC 60617 bringen die Vorlagen nicht mit |
| Ergebnis | Panel Schedule als Tabelle nach US-Konvention; für den Verteilerplan nach DIN EN 61082 braucht es einen Zusatzweg (BEEL) |
| Werkzeuge | Elektro-Add-ins in Revit (BEEL/elkoBIM, MagiCAD) oder CAE-Kopplung (eXs); Kernargument sind Berechnungen und Schema-Ausgabe |

## Inhaltsverzeichnis

- Was können die Revit-Bordmittel für die Elektroplanung?
- Warum kommt anfangs kein Stromkreis zustande?
- Was Ihre Familien mitbringen müssen
- Stromkreise in Revit Schritt für Schritt aufbauen
- Warum ist der Panel Schedule kein deutscher Verteilerplan?
- Welche Wege gehen deutsche Büros?
- So hilft BimWired
- Häufige Fragen (FAQ)
- Quellen

## Was können die Revit-Bordmittel für die Elektroplanung?

Revit bringt für die Elektroplanung einen Systemgedanken mit: Verbraucher hängen an Verteilern, Stromkreise fassen ihre Lasten zusammen, und Panel Schedules dokumentieren jeden Verteiler als Tabelle. Wer die Einrichtung einmal hinter sich hat, bekommt eine belastbare Grundlage. Jede Leuchte, jede Steckdose und jedes Gerät hängt dann nachvollziehbar an einem Verteiler und lässt sich mit seiner Last auswerten.

Auch die Beschriftung lässt sich inzwischen anpassen. Mensch und Maschine dokumentiert, dass die Benennung elektrischer Stromkreise seit Revit 2021 konfigurierbar ist. Derselbe Beitrag hält fest, dass die Standardvorlagen „keine Beschriftung für elektrische Ausstattungen wie Schalter, Steckdosen und Verteilungen“ enthalten. Deutsche Bezeichnungen und Symbole sind also Einrichtungsarbeit, keine Werkseinstellung.

Wo die Grenze liegt, sagt ausgerechnet ein Anbieter von Revit-Erweiterungen. „Revit ist nicht nativ auf das Zeichnen von Leitungen und die detaillierte Modellierung von elektrischen Gebäudesystemen ausgerichtet“, heißt es in einem MagiCAD-Advertorial in der Fachzeitschrift tab; Revit werde vielerorts „ausschließlich für die SHKL-Projektierung genutzt“. Ich lese das als Standortbestimmung, nicht als Urteil. Die Elektro-Bordmittel funktionieren, sie sind nur konsequent aus der US-Perspektive gebaut. Für deutsche Projekte heißt das: diese Perspektive einmal sauber einrichten und an einer Stelle einen zweiten Weg gehen.

## Warum kommt anfangs kein Stromkreis zustande?

In Revit entsteht ein Stromkreis nur, wenn drei Angaben zusammenpassen: Der Verteiler trägt einen Panel Name, ihm ist ein Verteilersystem (Distribution System) zugewiesen, und der elektrische Anschluss der gewählten Familie passt in Spannung und Polzahl zu diesem System. Fehlt ein Glied, kommt keine Zuordnung zustande.

Wie real diese Hürde ist, zeigt ein Thread im deutschsprachigen Autodesk-Forum: Ein Einsteiger scheitert daran, einem Unterverteiler ein Verteilersystem zuzuweisen, und die Antworten führen die Lösung auf genau diese US-Logik zurück, nach der Panel Name, Distribution System und der Stromanschluss in der Familie zusammenspielen müssen. In meinen Projekten war das der häufigste Grund, wenn sich ein Stromkreis partout nicht bilden ließ.

Der praktische Einstieg beginnt bei den Spannungen. Für deutsche Projekte legen Sie Spannungsdefinitionen für 230 V und 400 V an und bilden daraus die Verteilersysteme, typischerweise einphasig 230 V und dreiphasig 400/230 V. Erst wenn diese Systeme existieren, können Verteiler sie führen und Verbraucher angeschlossen werden. Die wichtigsten US-Konzepte auf einen Blick:

| US-Konzept | Rolle in Revit | Worauf deutsche Büros achten |
|---|---|---|
| Voltage Definition (Spannungsdefinition) | legt die im Projekt verfügbaren Spannungswerte fest | Einträge für 230 V und 400 V anlegen |
| Distribution System (Verteilersystem) | kombiniert Spannung, Phasen und Leiterzahl | einphasig 230 V und dreiphasig 400/230 V definieren |
| Panel Name | identifiziert den Verteiler im Projekt | Kennzeichnung wie „HV“ oder „UV EG“ von Beginn an vergeben |
| Circuit (Stromkreis) | verbindet Verbraucher mit einem Verteiler | Benennungsschema festlegen, konfigurierbar seit Revit 2021 (Mensch und Maschine) |
| Panel Schedule | tabellarische Dokumentation je Verteiler | US-Konvention; ersetzt keinen deutschen Verteilerplan |

## Was Ihre Familien mitbringen müssen

Ein Stromkreis braucht in jeder beteiligten Familie einen elektrischen Anschluss (Connector), der mindestens Spannung, Polzahl und Scheinleistung in VA trägt. Ohne diesen Anschluss kann Revit das Element keinem Verteilersystem zuordnen; die Familie bleibt für die Stromkreisbildung unsichtbar. Das gilt für Leuchten, Schalter und Steckdosen genauso wie für fest angeschlossene Geräte. Auch die Verteilerfamilie selbst muss ihren Stromanschluss mitbringen; im erwähnten Forum-Thread war genau diese Abstimmung der Knackpunkt.

Für deutsche Pläne kommt die Symbolfrage dazu. Schaltzeichen stammen hierzulande aus der IEC 60617; der VDE VERLAG beziffert die zugehörige Symboldatenbank auf etwa 1.900 Symbole für Schaltpläne. Deutsche Beschriftungen für die Elektro-Ausstattung fehlen in den Standardvorlagen (Mensch und Maschine), und deutsche Planungssymbole müssen Büros ebenfalls selbst ergänzen.

Wer jede Familie einzeln im Projekt nachrüstet, verliert den Standard schnell wieder. Ich habe das lange genug von Hand gemacht, um zu wissen, wie schnell zwei Projekte dann mit unterschiedlichen Anschlussdaten laufen. Anschlussdaten, Symbolik und Benennungen gehören in eine gepflegte Firmenbibliothek, damit jedes Projekt mit denselben Voraussetzungen startet. Wie sich so eine Bibliothek aufbauen und im Büro verteilen lässt, steht im Leitfaden [Revit-Familienbibliothek für das TGA-Büro aufbauen](https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html).

## Stromkreise in Revit Schritt für Schritt aufbauen

Die folgende Reihenfolge ist werkzeugneutral. Sie vermeidet die häufigsten Abbrüche, weil jeder Schritt die Voraussetzung für den nächsten schafft.

1. Spannungsdefinitionen anlegen: Hinterlegen Sie 230 V und 400 V in der Projektvorlage, damit jedes Projekt dieselbe Spannungswelt erbt.
2. Verteilersysteme definieren: Bilden Sie daraus mindestens ein einphasiges System mit 230 V und ein dreiphasiges mit 400/230 V.
3. Familien prüfen: Kontrollieren Sie, ob alle elektrischen Familien einen Anschluss mit Spannung, Polzahl und Scheinleistung tragen. Fehlende Werte ergänzen Sie in der Bibliothek, nicht im Einzelprojekt.
4. Verteiler platzieren und benennen: Vergeben Sie Panel Names nach Ihrem Kennzeichnungsschema, etwa „HV“ und „UV EG“, und weisen Sie jedem Verteiler sein Verteilersystem zu. Unterverteiler verbinden Sie über ihre Einspeisung mit dem übergeordneten Verteiler; genau an diesem Schritt hing der zitierte Forum-Thread.
5. Stromkreise bilden: Ordnen Sie die Verbraucher den Verteilern zu, gegliedert nach Ebenen, Räumen und Funktionen. Die Schutzorganisation gehört gleich mit dazu: Nach DIN VDE 0100-410:2018-10 sind Fehlerstrom-Schutzeinrichtungen (RCDs) mit höchstens 30 mA Bemessungsdifferenzstrom für Steckdosen in Endstromkreisen bis 32 A Bemessungsstrom vorgeschrieben, in Wohnungen auch für Endstromkreise mit Leuchten; nachzulesen im frei zugänglichen Normenhinweis der DKE.
6. Stromkreise auf FI-Gruppen verteilen: Der Fachartikel „Elektroplanung in Wohngebäuden“ in der Zeitschrift de (Ausgabe 12/2020) nennt zur DIN 18015-1:2020-05 als Regel für die Anlagenverfügbarkeit höchstens zwei einphasige Endstromkreise je zweipoligem und höchstens sechs je vierpoligem FI-Schalter.
7. Benennung konfigurieren: Stellen Sie das Benennungsschema der Stromkreise auf Ihre Konvention um, zum Beispiel Verteilerkennzeichen plus laufende Nummer. Möglich ist das seit Revit 2021 (Mensch und Maschine).
8. Im Panel Schedule kontrollieren: Prüfen Sie Lastsummen und Phasenverteilung je Verteiler und planen Sie Reserven ein. Derselbe Fachartikel zur DIN 18015-1 empfiehlt im Stromkreisverteiler eine Platzreserve von 20 %.

Damit stehen die Stromkreise sauber im Modell. Was noch fehlt, ist die deutsche Dokumentation.

## Warum ist der Panel Schedule kein deutscher Verteilerplan?

Ein Panel Schedule ist eine tabellarische Verteilerdokumentation nach US-Konvention. Ein deutscher Verteilerplan ist ein Plandokument im Umfeld der Dokumentennorm DIN EN 61082 und zeigt je Abgang Betriebsmittelkennzeichen, Absicherung, Querschnitt, Kabeltyp und RCD-Zuordnung. Diese Lücke lässt sich nicht wegkonfigurieren, sie steckt in der Struktur.

Abbildung: Gegenüberstellung: links die tabellarische Form eines Panel Schedule mit Stromkreisnummern, Auslösestrom und Lastspalten, rechts ein gezeichneter Verteilerplan als Übersicht mit Sammelschienen, Schaltzeichen, FI-Gruppe, Klemmen und Fußzeilen. Dieselben Stromkreise in zwei Dokumentformen: Die Tabelle zählt Lasten je Verteiler, das Plandokument zeigt je Abgang Schutzorgan, RCD-Zuordnung, Klemmen und Kabel.

Dafür gibt es drei Belege, die nichts miteinander zu tun haben. Der Anbieter BEEL hält fest, dass Revit allein die Anforderungen der DIN EN 61082 nicht vollständig erfüllt und Verteilerschemata Handarbeit erfordern. In einem englischsprachigen Autodesk-Forum-Thread empfehlen erfahrene Anwender für ein Einlinienschema eine Zeichenansicht mit Linien und Detailelementen nach Art früherer AutoCAD-Zeichnungen oder gleich das Zeichnen in AutoCAD mit Verknüpfung, beides ohne Modellbezug und ohne automatische Aktualisierung. Und es gibt eigene Produkte für genau diese Übergabe: Der CAE-Hersteller eXs vermarktet die Übergabe von Revit-Stromkreisdaten an automatisch erzeugte Verteilerpläne samt Rückübertragung der Sicherungskennzeichen als Schließen einer „wichtigen Lücke im BIM-Prozess“.

Auf das Dokument verzichten kann ein deutsches Projekt nicht. Nach DIN VDE 0100-510, Abschnitt 514.5, gehören zur Anlage Schaltpläne, Diagramme oder Tabellen, aus denen Art und Aufbau der Stromkreise hervorgehen: versorgte Verbraucher, Leiterzahl und Querschnitt, Kabel- und Leitungsarten, dazu Merkmale und Einbauorte der Schutz-, Trenn- und Schalteinrichtungen. Der frei zugängliche Fachbeitrag von Stefan Euler zur Dokumentation elektrischer Anlagen schlüsselt diese Anforderungen auf. Für die Betriebsmittelkennzeichnung beschreibt die EN IEC 81346 drei Aspekte, nämlich Funktion, Ort und Produkt, wie der EPLAN-Blog zur Referenzkennzeichnung erläutert.

Wie der normgerechte Verteilerplan aufgebaut ist und wie er aus den Stromkreisdaten entstehen kann, steht im Artikel [Verteilerplan und Stromlaufplan normgerecht erstellen](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html).

## Welche Wege gehen deutsche Büros?

In der Praxis sehe ich drei Wege: Bordmittel mit daneben gezeichnetem Schema, Elektro-Add-ins in Revit und modellgespeiste Editoren außerhalb von Revit. Alle drei sind legitim. Sie unterscheiden sich darin, wo die Arbeit stattfindet und wie viel doppelt gepflegt wird.

Beim ersten Weg entstehen Stromkreise und Panel Schedules in Revit, das Verteilerschema daneben, in einer Zeichenansicht oder in AutoCAD (so die Empfehlungen im genannten Forum-Thread). Das kostet keine zusätzliche Software, koppelt aber Plan und Modell nicht: Jede Änderung wird zweimal nachgezogen. Ich habe lange so gearbeitet; es geht, solange sich wenig ändert. Wie das Zieldokument aussehen sollte, zeigt der Artikel [zum normgerechten Verteilerplan](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html).

Der zweite Weg sind Elektro-Add-ins in Revit. BEEL/elkoBIM betreibt dazu einen kompletten deutschsprachigen Themenhub, von Stromkreisen und Verteilern über Kabeltrassen, 2D-Schemen und Schwachstrom bis zur Massenauswertung, samt Schulungen und YouTube-Kanal. MagiCAD erweitert Revit ebenfalls um Elektro-Funktionen; laut dem tab-Advertorial sind Berechnungen wie Spannungsfall und Kabeldimensionierung das zentrale Verkaufsargument solcher Erweiterungen, weil die Bordmittel sie nicht mitbringen. Der CAE-Hersteller eXs koppelt Revit mit bidirektionaler Datenübergabe an die CAE-Welt. Diese Werkzeuge halten den Workflow in oder an Revit und ergänzen die Fachrechnungen, die den Bordmitteln fehlen.

Der dritte Weg schickt die Elementdaten aus dem Modell an einen externen Plan-Editor. Dort entsteht die Stromkreisaufteilung samt Verteilerdokumentation, und die Ergebnisse fließen als Stromkreisnummern und Parameter zurück ins Modell. So arbeitet BimWired: ein Browser-Editor, der aus gesendeten Revit-Elementdaten Verteiler und Stromkreise aufbaut.

Welcher Weg passt, hängt von Projektgrößen, vorhandener Softwarelandschaft und dem Berechnungsbedarf ab. Ohne einen dieser Wege bleibt der deutsche Verteilerplan Handarbeit neben dem Modell.

## Einordnung: das Werkzeug BimWired

Ich habe es aus der eigenen Planungsarbeit heraus gebaut, weil mich die Verteileraufteilung neben dem Modell am meisten Zeit gekostet hat. Der Rundlauf hat drei Schritte. Der Revit-Befehl „Stromkreisplan senden“ sammelt Leuchten, Schalter, Steckdosen und Elektrogeräte mit Raum, Ebene, Scheinleistung, Spannung und Polzahl. Im Browser bauen Sie dann den Plan auf: Verteiler anlegen und duplizieren, Zähler und Reserve-Zeilen ergänzen. „Automatisch aufteilen“ bildet thematische Gruppen je Ebene (Licht, Steckdosen, Durchlauferhitzer, Außenbereich), wahlweise für einen Verteiler oder automatisch je Ebene einen. Gruppenköpfe wie D0-Vorsicherung, FI-Gruppen oder Zentralschaltung, Klemmen je Zeile, Unterzeilen für Abzweige und Kabel-Vorschläge mit Typbezeichnungen gehören dazu. Feste, deterministische Prüfungen melden Überlast, fehlende RCD-Zuordnung und zu geringe Querschnitte, mit Bezügen zur DIN 18015. Zum Schluss schreibt „Stromkreise übernehmen“ die Stromkreisnummern und je Einstellung Verteiler, Sicherung, RCD, Kabel und Phasen zurück nach Revit; fehlende Projektparameter legt das Plugin an, und ein Rückgängig-Schritt ist vorgesehen.

Abbildung: Fenster „Stromkreisplan senden“ im Revit-Plugin: die erkannten Elektro-Elemente nach Kategorie gruppiert, je Zeile Familie, Typ, Ebene, Raum, Stromkreis und Leistung. Vor dem Senden zeigt das Plugin, was im Web-Editor ankommt: Familie, Typ, Raum, Ebene, Stromkreisnummer und Anschlusswerte, ausdrücklich keine Geometrie.

Zwei Dinge ersetzt BimWired absichtlich nicht: die Revit-Stromkreisfunktion selbst, denn der Editor arbeitet mit den gesendeten Elementdaten, und Ihre Fachentscheidung. Eine KI hilft nur beim Klassifizieren unerkannter Elemente, mit Konfidenzangabe und Vorschau; die Aufteilung bleibt regelbasiert, und Sie validieren das Ergebnis. Das ist mir wichtig, ich will kein Werkzeug, das der Planerin die Entscheidung abnimmt.

## Häufige Fragen (FAQ)

### Warum kann ich in Revit keinen Stromkreis anlegen?

Meist fehlt eines von drei Gliedern: der Panel Name am Verteiler, das zugewiesene Verteilersystem oder ein elektrischer Anschluss in der Familie, der in Spannung und Polzahl zum System passt. Genau daran scheitert ein Einsteiger in einem dokumentierten Thread im deutschsprachigen Autodesk-Forum. Ich prüfe die Kette immer in dieser Reihenfolge, bevor ich an die Familien gehe.

### Seit wann lässt sich die Stromkreis-Benennung in Revit anpassen?

Laut der Dokumentation von Mensch und Maschine lässt sich die Benennung elektrischer Stromkreise seit Revit 2021 konfigurieren. Die Standardvorlagen enthalten demnach zudem „keine Beschriftung für elektrische Ausstattungen wie Schalter, Steckdosen und Verteilungen“. Deutsche Benennungs- und Beschriftungsschemata richten Sie deshalb einmal in Vorlage und Bibliothek ein, nicht in jedem Projekt neu.

### Ist ein Panel Schedule ein Verteilerplan?

Nein. Ein Panel Schedule ist eine tabellarische Verteilerdokumentation nach US-Konvention, ein deutscher Verteilerplan ein Plandokument im Umfeld der Dokumentennorm DIN EN 61082. Der Anbieter BEEL hält fest, dass Revit allein die Anforderungen der DIN EN 61082 nicht vollständig erfüllt und Verteilerschemata Handarbeit erfordern.

### Kann Revit den Spannungsfall nach VDE berechnen?

Nicht mit Bordmitteln. BEEL schreibt, Revit biete „keine vollständige Kabelberechnung nach DIN VDE (Spannungsfall, Kurzschlussfestigkeit, Strombelastbarkeit)“. Solche Nachweise entstehen deshalb in Zusatzwerkzeugen oder in separaten Berechnungen. Welche Prüfungen sich im Revit-Umfeld automatisieren lassen, behandelt der Artikel über [VDE-Prüfungen in der Elektroplanung mit Revit](https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html).

### Welche Angaben braucht eine Familie für Stromkreise?

Einen elektrischen Anschluss (Connector) mit Spannung, Polzahl und Scheinleistung in VA. Ohne ihn kann Revit das Element keinem Verteilersystem zuordnen, und ein Stromkreis lässt sich nicht bilden. Für deutsche Pläne kommen Schaltzeichen nach IEC 60617 hinzu; der VDE VERLAG beziffert die zugehörige Symboldatenbank mit etwa 1.900 Symbolen.

### Warum reicht das Revit-Modell allein nicht als Dokumentation?

Nach DIN VDE 0100-510, Abschnitt 514.5, gehören zur Anlage Schaltpläne, Diagramme oder Tabellen, aus denen Art und Aufbau der Stromkreise sowie die Schutz-, Trenn- und Schalteinrichtungen hervorgehen; der Fachbeitrag von Stefan Euler zur Dokumentation elektrischer Anlagen schlüsselt diese Anforderungen auf. Das Modell liefert die Datenbasis, das Dokument bleibt eine eigene Lieferung.

## Quellen

1. Mensch und Maschine: Revit MEP 2021, Benennung elektrischer Stromkreise. https://support.mum.de/help/de-de/70-revit-mep/200-revit-mep-2021-benennung-elektrischer-stromkreise (abgerufen am 25.08.2026)
2. tab: Advertorial MagiCAD, So können Sie in Revit auch Elektro planen. https://www.tab.de/artikel/advertorial-magicad-so-koennen-sie-in-revit-auch-elektro-planen-4021922.html (abgerufen am 25.08.2026)
3. Autodesk-Forum (Revit MEP): Hilfe bei Elektroplanung. https://forums.autodesk.com/t5/revit-mep-forum/hilfe-bei-elektroplanung/td-p/9818401 (abgerufen am 25.08.2026)
4. Autodesk-Forum (Revit MEP): Electrical single line diagram. https://forums.autodesk.com/t5/revit-mep-forum/electrical-single-line-diagram/td-p/8667884 (abgerufen am 25.08.2026)
5. BEEL: Revit Elektroplanung (Themenübersicht). https://www.beel.de/revit-elektroplanung/ (abgerufen am 25.08.2026)
6. BEEL: Revit Stromlaufplan. https://www.beel.de/revit/revit-stromlaufplan/ (abgerufen am 25.08.2026)
7. BEEL: Revit Kabel. https://www.beel.de/revit/revit-kabel/ (abgerufen am 25.08.2026)
8. eXs: Elektroplanung in BIM-Projekten. https://www.exs-cae.com/elektroplanung-in-bim-projekten/ (abgerufen am 25.08.2026)
9. DKE: Hinweise zum erleichterten Umgang mit DIN VDE 0100-410. https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/konzept-0100-410 (abgerufen am 25.08.2026)
10. Elektroplanung in Wohngebäuden. Zeitschrift de, Ausgabe 12/2020 (Volltext-PDF zur DIN 18015-1:2020-05). https://www.elektro.net/media/file/Kwqzk199w7/fd7e48cc/DE_12_2020_31-34_EA42neu.pdf (abgerufen am 25.08.2026)
11. VDE VERLAG: IEC 60617 Schaltzeichen-Datenbank (Produktseite). https://www.vde-verlag.de/iec-normen/iec-datenbanken/iec-60617-schaltzeichen.html (abgerufen am 25.08.2026)
12. Stefan Euler: Dokumentation elektrischer Anlagen. Rechtssicherheit für Errichter und Betreiber (Fachbeitrag, PDF). https://expertennetzwerk-elektrotechnik.de/wp-content/uploads/2018/10/Fachbeitrag_Stefan_Euler_Dokumentation-elektrischer-Anlagen.pdf (abgerufen am 25.08.2026)
13. EPLAN-Blog: Normgerecht strukturieren und referenzieren nach EN IEC 81346. https://www.eplan.com/de-de/blog/software/normgerecht-strukturieren-und-referenzieren (abgerufen am 25.08.2026)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
