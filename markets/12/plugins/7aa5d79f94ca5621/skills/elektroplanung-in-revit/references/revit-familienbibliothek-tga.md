---
titel: "Revit-Familienbibliothek fürs TGA-Büro: vom Netzlaufwerk-Wildwuchs zum Firmenstandard"
quelle: https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html
stand: 2026-08-25
art: artikel
fragen:
  - "Wie baut ein TGA-Büro eine firmenweite Revit-Familienbibliothek auf?"
  - "Welche Namenskonvention hat sich für Revit-Familien bewährt?"
  - "Warum ersetzen Download-Portale keine Firmenbibliothek?"
  - "Wie klassifiziert man Revit-Familien mit IFC und DIN 276?"
  - "Wie kommt ein neuer Bibliotheksstand auf alle Rechner?"
  - "Wie übernimmt man den Familien-Altbestand in eine neue Bibliothek?"
---

# Revit-Familienbibliothek fürs TGA-Büro: vom Netzlaufwerk-Wildwuchs zum Firmenstandard

Eine firmenweite Revit-Familienbibliothek ist ein kuratierter Bestand: bewusst begrenzt, je Gewerk geprüft, mit einer dokumentierten Namens- und Parameterkonvention, mit IFC- und DIN-276-Klassifizierung von Anfang an, mit einem Freigabeprozess über versionierte Stände und mit einem Verteilweg, der alte Stände auf allen Rechnern verbindlich ablöst. Diese fünf Bausteine hängen an keinem bestimmten Werkzeug. Ein Büro, das sie einführt, verkürzt die Suchzeiten, bekommt belastbare Auswertungen und kann BIM-Anforderungen der Auftraggeber ohne Nacharbeit erfüllen.

## Das Wichtigste in Kürze

- Ein geprüfter Kernbestand der Objektarten, die Ihr Büro tatsächlich platziert, ist mehr wert als eine große Sammlung.
- Namensschema und gemeinsame Parameterliste werden schriftlich festgelegt, bevor die erste Familie migriert wird.
- IFC-Klasse mit PredefinedType und DIN-276-Kostengruppe gehören in jede Familie; erst damit sind Familien maschinell auswertbar und AIA-tauglich.
- Versionierte, geprüfte Stände mit Änderungsliste ersetzen das offene Netzlaufwerk.
- Ein neuer Stand löst den alten auf jedem Rechner ab; platzierte Familien in laufenden Projekten werden gezielt nachgezogen.

## Überblick

| Punkt | Detail |
|---|---|
| Problem | Projektweise gewachsene Ablagen, Duplikate, je Standort ein eigener Stand; in unserer eigenen Ansprache-Kartei der größte von uns notierte Schmerz-Cluster (89 von 192 Profilen) |
| Lösung in einem Satz | Kuratierter Kernbestand, Namenskonvention, Klassifizierung, Freigabeprozess, verbindlicher Verteilweg |
| Namenskonvention | Feste Bausteine in fester Reihenfolge: Gewerk, Objektart, Kenn-Merkmal, Herkunft |
| Klassifizierung | IFC-Klasse und PredefinedType je Familie, dazu die DIN-276-Kostengruppe (KG 400) |
| Freigabe | Geprüfte, versionierte Stände mit Änderungsliste; Fehler blockieren die Freigabe |
| Verteilung | Ein verbindlicher Stand für alle Rechner und Standorte; Updates lösen Altstände ab |
| Werkzeuge | Von der disziplinierten Ordnerstruktur bis zum Bibliotheksdienst; BimWired (Anbieter dieses Ratgebers) ist ein solcher Dienst mit Browser-Pflege, Releases und Revit-Plugin |

## Inhalt

- Woran erkennen Sie, dass Ihre Familienbibliothek zum Problem geworden ist?
- Warum ersetzen Download-Portale keine Firmenbibliothek?
- Wie sieht eine tragfähige Namens- und Parameterkonvention aus?
- Warum gehören IFC und DIN 276 von Anfang an in jede Familie?
- Warum ist ein Freigabeprozess besser als ein offenes Netzlaufwerk?
- Wie kommt der freigegebene Stand auf alle Rechner?
- Bestand übernehmen: der Migrationsweg in acht Schritten
- So hilft BimWired
- Häufige Fragen (FAQ)
- Quellen

## Woran erkennen Sie, dass Ihre Familienbibliothek zum Problem geworden ist?

Eine Familienbibliothek ist zum Problem geworden, wenn die Suche nach der richtigen Familie länger dauert als das Platzieren und niemand verbindlich sagen kann, welcher Stand der aktuelle ist. Ich kenne beide Symptome aus eigenen Projekten, und der Softwarehändler Graitec beschreibt sie genauso: Die Familiensuche werde „zeitraubend und kontraproduktiv", Familien aus Altprojekten seien inkompatibel, Internet-Downloads fehlerhaft. Dazu passt unsere eigene Ansprache-Kartei: Wir haben 192 öffentlich zugängliche Profile von Elektro- und TGA-Planungsbüros in Deutschland, Österreich und der Schweiz durchgesehen und bei 89 davon Familien, Bibliothek, Symbole oder Firmenstandard als drängendsten Ansatzpunkt vermerkt, bei 27 zusätzlich Bestände, die über mehrere Standorte auseinanderlaufen. Der Vermerk stammt von uns, nicht von den Büros, und die Kartei ist weder repräsentativ noch neutral erhoben.

| Symptom | Typische Ursache | Folge im Projekt |
|---|---|---|
| Die Suche dauert länger als das Platzieren | Ablage nach Projekten statt nach Objektarten, kein Namensschema | Zeitverlust in jedem Projekt, Griff zur nächstbesten Kopie |
| Dieselbe Steckdose existiert in drei Varianten mit drei Namen | Projektweises Kopieren und Anpassen ohne Rückführung | Stücklisten und Auswertungen zählen falsch |
| Familien aus Altprojekten laufen im neuen Projekt nicht | Veraltete Versionsstände, gewachsene Parameter | Nacharbeit unter Termindruck |
| Jeder Standort pflegt einen eigenen Stand | Verteilung durch Kopieren auf Standort-Laufwerke | Gleiche Bauteile, unterschiedliche Daten je Standort |
| Der IFC-Export liefert nichtssagende generische Objekte | Fehlende Klassifizierung in den Familien | Prüfsoftware und modellbasierte Übergaben scheitern |

Wie tief das reicht, zeigt ein CAD.de-Thread vom Dezember 2019. Schon das Anpassen einer Familie aus der Standardbibliothek scheiterte dort an Kategorien und Projekt-Überschreibungen, und der Rat der Erfahrenen lautete, eigene Familien mit sauberen Unterkategorien aufzubauen. Nichts anderes ist ein Firmenstandard.

## Warum ersetzen Download-Portale keine Firmenbibliothek?

Download-Portale liefern Einzelteile. Jede Quelle bringt ihre eigene Namenslogik mit, ihre eigenen Parameter und ihren eigenen Detaillierungsgrad, und zu einer Bibliothek fügt sich das nicht von selbst. Wie groß das Feld ist, zeigt Autodesks laufend aktualisierte Linkliste von Revit-Content-Quellen: über 50 Anbieter, viele Hersteller nur über kommerzielle Portale erreichbar, Elektro-Inhalte und deutsche Normelemente deutlich unterrepräsentiert. Symbole nach deutscher Zeichnungslegende sind dort kaum zu finden.

Dass die Kuratierung der eigentliche Wert ist, zeigt der Markt selbst. Der Wiener Anbieter Plandata verkauft mit BIMpedia einen kuratierten TGA-Familienkatalog mit nach eigener Angabe über 1.800 Elementen und begründet ihn mit dem Bedarf an einheitlicher Bezeichnungslogik und konsistenter Parameterstruktur. Die Kunden zahlen dort für die Ordnung hinter den Dateien.

Auf Downloads müssen Sie deshalb nicht verzichten. Hersteller-Familien sind Rohmaterial, meist detaillierter als nötig und nach der Logik des Herstellers parametriert. In den Firmenstandard kommen sie erst nach einer Aufnahmeprüfung: umbenennen, Parameter angleichen, klassifizieren, Geometrie prüfen. Zur Geometrieprüfung gehört die Host-Art: Viele Hersteller-Familien sind wandbasiert und lassen sich in Modellen mit verlinkter Architektur gar nicht setzen; was dahintersteckt und worauf Sie beim Bauen achten, steht in [Revit-Familien für die TGA erstellen](https://bimwired.com/landing/wissen/revit-familien-erstellen-host-skelett.html). Wer das auslässt, trägt den Wildwuchs von außen nach innen.

## Wie sieht eine tragfähige Namens- und Parameterkonvention aus?

Eine Namenskonvention ist eine verbindliche Bauanleitung für Familiennamen: dieselben Bausteine in derselben Reihenfolge und Schreibweise, ohne Ausnahmen. Sie ist das günstigste Werkzeug der ganzen Umstellung und wirkt sofort, weil Familien findbar und Duplikate sichtbar werden und Auswertungen sich sortieren lassen. Ein Schema, das sich bewährt hat, arbeitet mit vier Bausteinen:

| Baustein | Regel | Beispiel |
|---|---|---|
| Gewerk-Kürzel | fester Code je Gewerk (etwa ELT, HZG, LUF, SAN, MSR) | ELT |
| Objektart | deutsche Objektbezeichnung im Singular, ohne Abkürzungsvarianten | Steckdose |
| Kenn-Merkmal | das eine Merkmal, das die Familie von ihren Nachbarn unterscheidet | SCHUKO-AP |
| Herkunft | NN für herstellerneutral, sonst ein dokumentiertes Herstellerkürzel | NN |
| Ergebnis | Bausteine in fester Reihenfolge, getrennt durch Unterstrich | ELT_Steckdose_SCHUKO-AP_NN |

Dazu kommen wenige, harte Regeln: keine Leerzeichen und keine Sonderzeichen, die Dateisysteme oder Austauschformate stören; Abkürzungen nur aus einer dokumentierten Liste; der Name beschreibt das Objekt und nie das Projekt. Die ganze Konvention passt auf zwei Seiten und gehört in die Einarbeitung.

Abbildung: Der Familienname ELT_Steckdose_SCHUKO-AP_NN, unter seinen vier Segmenten aufgeklappt zu Gewerk-Kürzel, Objektart, Kenn-Merkmal und Herkunft, darunter zwei Namen, die gegen die Regeln verstoßen Jedes Segment hat seinen eigenen Wertevorrat; wer Reihenfolge oder Schreibweise aufweicht, verliert genau die Sortierbarkeit, für die das Schema da ist.

Für Parameter gilt dieselbe Disziplin. Eine gemeinsame Liste legt je Parameter Name, Datentyp, Einheit, Typ- oder Exemplarbindung und Pflichtstatus fest. Revit erkennt gemeinsam genutzte Parameter an einer internen Kennung, nicht am Namen; zwei gleichnamige Parameter aus verschiedenen Quellen bleiben zwei Parameter und erzeugen in Bauteillisten zwei Spalten. Deshalb stammen alle Parameter aus einer einzigen, zentral gepflegten Quelle. Für Elektro-Familien gehören die elektrischen Kennwerte auf die Pflichtliste, mindestens Spannung, Leistung und Polzahl. Ohne sie bleibt das Modell für die Stromkreisplanung stumm; welche Voraussetzungen dort im Einzelnen gelten, steht im Leitfaden [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html).

Beim Typenkatalog halte ich mich an eine Faustregel: Ein Typ entspricht einer real bestellbaren Variante, und Sammelfamilien werden nach Anlagenteil geschnitten, nicht nach dem Motto „eine Familie für alles". Sehr lange Typenlisten machen Familien träge und schwer prüfbar.

## Warum gehören IFC und DIN 276 von Anfang an in jede Familie?

Erst die IFC-Klasse mit PredefinedType und die DIN-276-Kostengruppe machen aus einer Familie einen Datensatz, den Prüfsoftware und Auswertungen verarbeiten können. IFC ist das offene, herstellerneutrale Austauschformat für Bauwerksmodelle; laut BauNetz Wissen ist es seit der Version IFC4 offizieller ISO-Standard (ISO 16739-1:2024-03), aktuell ist IFC4.3. Jede Familie bekommt deshalb ihre IFC-Klasse und den passenden PredefinedType, damit aus dem generischen Objekt eine IfcLightFixture wird und die Steckdose von der Datendose unterscheidbar bleibt. Fehlt die Zuordnung, exportiert das Modell Stellvertreter-Objekte, mit denen Prüfsoftware und Auswertungen wenig anfangen können. Die Zuordnung gehört in die Familie und nicht in nachträgliche Handarbeit im Projekt, denn nur dann stimmt sie in jedem Projekt von selbst.

Die zweite Achse ist die Kostenstruktur. Die DIN 276:2018-12 gliedert die Baukosten in Kostengruppen; die technischen Anlagen bilden die KG 400, die Starkstromanlagen darin die KG 440 (Nachweis: Baunormenlexikon; Erläuterung: MT-Ingenieure). Trägt jede Familie ihre Kostengruppe, lassen sich Kostenschätzungen und Vergabeeinheiten direkt aus dem Modell ableiten, und niemand muss Bauteillisten von Hand zuordnen.

Der dritte Grund ist vertraglich. Auftraggeber formulieren ihre Anforderungen zunehmend als Auftraggeber-Informationsanforderungen (AIA). Laut Build-Ing. münden die Informationsanforderungen nach DIN EN ISO 19650 in die AIA, deren Umsetzung der BIM-Abwicklungsplan (BAP) beschreibt. Wer seine Bibliothek heute klassifiziert, beantwortet solche Anforderungen mit einem Export statt mit Wochenendarbeit. Noch ist das die Minderheit: In einer Umfrage der Bundesingenieurkammer gaben Ende 2022 erst 28 Prozent der Ingenieurbüros an, BIM anzuwenden. Wer jetzt klassifiziert, ist lieferfähig, bevor die Nachfrage kommt. Einen Überblick über die einschlägigen Standards, von DIN EN ISO 19650 bis zur Richtlinienreihe VDI 2552, pflegt das Portal BIM Deutschland im Auftrag des Bundes.

## Warum ist ein Freigabeprozess besser als ein offenes Netzlaufwerk?

Ein offenes Netzlaufwerk kennt nur den aktuellen Zustand. Ein Freigabeprozess kennt geprüfte Stände, die nummeriert, dokumentiert und wiederherstellbar sind. Auf dem Laufwerk schreibt jeder und niemand prüft; Änderungen hinterlassen keine Spur, und ein überschriebenes Original fällt erst Wochen später auf. Ich habe lange so gearbeitet und weiß, wie schnell ein solches Laufwerk kippt.

Dafür braucht es keine große Organisation. Vier Festlegungen reichen. Erstens ein Arbeitsbereich für Änderungen, getrennt vom freigegebenen Stand, mit dem die Projekte arbeiten. Zweitens eine Prüfliste vor jeder Freigabe: Namen folgen der Konvention, Pflichtparameter sind gefüllt, die Klassifizierung ist vollständig, Duplikate sind aufgelöst. Drittens eine Änderungsliste je Stand, damit Projektverantwortliche entscheiden können, ob und wann sie nachziehen. Viertens die Möglichkeit, einen früheren Stand wiederherzustellen. Freigeben darf nur eine benannte Person je Gewerk oder Bibliothek; sonst hat man das offene Laufwerk unter anderem Namen.

Auf denselben gepflegten Kennwerten setzen später automatisierte Plausibilitätsprüfungen der Elektroplanung auf. Was sich davon automatisieren lässt und wo Ingenieurleistung bleibt, ordnet der Beitrag [VDE-Prüfungen in der Revit-Elektroplanung](https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html) ein.

## Wie kommt der freigegebene Stand auf alle Rechner?

Ein neuer Stand ersetzt den alten auf jedem Rechner. Er liegt nicht daneben. Das Kopieren auf Standort-Laufwerke erzeugt dagegen genau das Muster, das wir in unserer Ansprache-Kartei wiederholt notiert haben: „vier Standorte, vier Familienstände" ist unsere eigene Kurzformel dafür, keine Aussage der Büros. Drei Regeln verhindern es: genau eine verbindliche Quelle; Altstände nur lesend als Archiv; jeder Rechner bezieht den freigegebenen Stand über denselben definierten Weg, ob Skript, Synchronisation oder Bibliotheksdienst.

Abbildung: Flussbild von der Firmenbibliothek im Editor über die Freigabe und den HTTPS-Weg zum Arbeitsplatz mit Revit und weiter ins laufende Projekt Der Weg endet nicht am Rechner: In laufende Projekte kommt der neue Stand erst, wenn die platzierten Familien dort gezielt nachgezogen werden.

Zwei Sonderfälle brauchen eigene Regeln. Platzierte Familien leben als Kopie im Projekt; ein neuer Stand erreicht laufende Projekte erst, wenn die Familien dort gezielt neu geladen werden. Ob ein Projekt mitten in der Ausführungsplanung nachzieht, entscheidet die Projektleitung, kein Automatismus. Außerdem geraten in jedes Projekt Fremdfamilien. Eine regelmäßige Kontrolle, was nicht aus dem Firmenstandard stammt, hält Auswertungen und Übergaben sauber.

Bleibt die Frage der Kapazität. Nach derselben Auswertung haben Büros mit 11 bis 50 Beschäftigten in der Regel keinen eigenen BIM-Manager. Die Pflege funktioniert dann als Rolle statt als Stelle: je Gewerk eine benannte Person, ein fester Freigaberhythmus, kleine Arbeitspakete. Wie das über mehrere Standorte laufen kann, zeigt das [Praxisszenario zur Familienbibliothek](https://bimwired.com/landing/wissen/praxisszenario-familienbibliothek.html).

## Bestand übernehmen: der Migrationsweg in acht Schritten

Der Altbestand ist mehr wert, als er aussieht, denn in ihm steckt das reale Objektsortiment Ihres Büros. Es geht darum, dieses Sortiment zu übernehmen und den Wildwuchs zurückzulassen.

1. Stichtag setzen und Altablage einfrieren: Nichts Neues kommt mehr auf das alte Laufwerk, es bleibt lesend verfügbar.
2. Kernbestand bestimmen: Maßgeblich ist, welche Familien in den letzten Projekten tatsächlich platziert wurden, nicht, was sich angesammelt hat.
3. Konvention zuerst festlegen: Namensschema, Parameterliste und Klassifizierungsregeln werden schriftlich beschlossen, bevor die erste Familie wandert.
4. In Wellen importieren: gewerkweise, beginnend beim größten Schmerz; Duplikate werden direkt beim Import zusammengeführt.
5. Klassifizierung und Pflichtparameter ergänzen: IFC-Klasse mit PredefinedType, DIN-276-Kostengruppe und, bei Elektro, die elektrischen Kennwerte.
6. Herstellerdaten strukturiert übernehmen: Typen- und Artikeldaten aus Katalogdateien oder gepflegten Tabellen importieren statt abzutippen.
7. Validieren und ersten Stand freigeben: Die Prüfliste entscheidet; erst mit der Freigabe ist die Bibliothek verbindlich.
8. Projekte umstellen: Neue Projekte starten nur noch aus dem Firmenstandard; laufende Projekte ziehen je nach Leistungsphase bewusst nach oder laufen aus.

Für Schritt 6 gilt: nicht abtippen. Hersteller liefern Produktdaten zunehmend strukturiert, etwa als BMEcat-Katalog mit ETIM-Klassifikation oder als einfache CSV-Liste. Die Richtlinie VDI 3805 verfolgt nach Angaben ihrer Plattform vdi3805.eu genau dieses Ziel, eine einheitliche, herstellerneutrale Produktdatenbank für die TGA-Planung. Beim Import lohnt ein Blick auf deutsche Zahlen- und Einheitenformate (Komma statt Punkt, kW statt W), denn solche Fehler fallen sonst erst in der Auswertung auf.

## Einordnung: das Werkzeug BimWired

BimWired ist mein eigenes Produkt, und der hier beschriebene Weg ist der Grund, warum es genau diese Funktionen hat. Es ist eine Cloud-Webanwendung mit Revit-Plugin für Revit 2025 bis 2027. Familien pflegen Sie komplett im Browser: IFC-Klasse mit PredefinedType, DIN 276, Parameter mit Datentyp und Pflichtstatus, Typenkataloge bis 60 Typen, 2D-Symbol und 3D-Körperform. Die Geometrie entsteht wahlweise automatisch über den Skelett-Weg, ohne dass jemand modelliert, oder Sie laden fertige .rfa-Dateien hoch, deren Geometrie unangetastet bleibt.

Den Altbestand übernimmt der RFA-Sammelimport mit bis zu 200 Dateien je Durchgang samt Duplikat-Erkennung; die KI schlägt Name, Gewerk, Kategorie und IFC-Klasse vor, die Entscheidung bleibt bei Ihnen. Herstellerdaten gelangen per BMEcat mit ETIM oder CSV in den Typenkatalog, mit Vorschau vor dem Schreiben und korrekt umgerechneten deutschen Zahlen und Einheiten. Vor der Freigabe validiert der Editor die Bibliothek, und Fehler blockieren das Release. Ein IDS-Export (buildingSMART IDS 1.0) liefert Prüfregeln für Software wie Solibri, IFC-Exporter-Mappings für Revit liegen bei.

Freigegebene Stände sind Releases mit Änderungsliste, Vergleich und Wiederherstellen. Auf den Rechnern holt das Plugin per „Cloud-Update" den freigegebenen Stand, „Familien aktualisieren" zieht platzierte Familien in Projekten nach, und die „Bauteilliste" markiert je Familie die Herkunft: Bibliothek, Fremd oder Revit-Systemfamilie. Eine mitgelieferte Basis-Bibliothek dient als Startpunkt; Updates daran übernehmen Sie nur auf Bestätigung.

## Häufige Fragen (FAQ)

### Wie viele Familien braucht eine TGA-Firmenbibliothek zum Start?

Weniger, als die meisten Büros vermuten. Entscheidend ist, dass die je Gewerk am häufigsten platzierten Objektarten sauber benannt, parametriert und klassifiziert vorliegen; die Gesamtzahl sagt wenig. Für den Start zählt der geprüfte Kernbestand, der danach nach Bedarf wächst.

### Reicht ein gut sortiertes Netzlaufwerk nicht aus?

Ein Netzlaufwerk kann Ordnung halten, aber keine Verbindlichkeit erzeugen: Es kennt keine geprüften Stände, keine Änderungslisten und keine Ablösung alter Versionen auf den Rechnern. Sobald mehrere Personen oder Standorte schreiben, laufen die Bestände auseinander. Ein Freigabeprozess mit versionierten Ständen löst genau dieses Problem, unabhängig vom eingesetzten Werkzeug.

### Sollten Hersteller-Familien direkt ins Projekt übernommen werden?

Nein. Hersteller- und Portal-Familien bringen eigene Namenslogik, eigene Parameter und oft unnötig detaillierte Geometrie mit; laut Graitec sind Internet-Downloads zudem häufig fehlerhaft. Der belastbare Weg führt über die Aufnahme in den Firmenstandard: umbenennen nach Konvention, Parameter angleichen, klassifizieren, prüfen und erst dann freigeben.

### Welche Parameter gehören in jede Elektro-Familie?

Neben der Identifikation (Name nach Konvention, Gewerk, IFC-Klasse mit PredefinedType, DIN-276-Kostengruppe) braucht jede Elektro-Familie ihre elektrischen Kennwerte, mindestens Spannung, Leistung und Polzahl. Ohne diese Werte sind Stromkreisplanung, Bilanzen und automatisierte Prüfungen im Modell nicht möglich. Typ- und Artikelinformationen des Herstellers kommen dazu, sobald ein konkretes Produkt feststeht.

### Wer pflegt die Bibliothek, wenn das Büro keinen BIM-Manager hat?

In unserer eigenen Ansprache-Kartei von 192 Büro-Profilen sind Büros mit 11 bis 50 Beschäftigten die größte Gruppe, und bei ihnen haben wir häufig vermerkt, dass keine eigene BIM-Manager-Stelle besteht. Aus meiner Sicht bewährt sich eine Rolle statt einer Stelle: Eine benannte Person je Gewerk sammelt Änderungswünsche, ein fester Freigaberhythmus bündelt die Arbeit, und die Prüfliste vor der Freigabe hält den Aufwand klein. Wichtig ist nur, dass Freigeben und Verteilen definierte Handgriffe sind und nicht nebenbei passieren.

## Quellen

1. Graitec Blog: Standardisierte Revit-Familienbibliothek einrichten, https://graitec.com/de/blog/https-graitec-com-de-blog-standardisierte-revit-familienbibliothek-einrichten/ (abgerufen am 25.08.2026)
2. CAD.de Forum: Thread zum Anpassen von Familien aus der Standardbibliothek (Dezember 2019), https://ww3.cad.de/foren/ubb/Forum329/HTML/002479.shtml (abgerufen am 25.08.2026)
3. Autodesk BIM Blog: Revit Content: Online-Bibliotheken mit 10.000en Familien als Download, https://blogs.autodesk.com/bimblog/revit-content-online-bibliotheken-mit-10-000en-familien-als-download-beitrag-wird-regelmasig-aktualisiert/ (abgerufen am 25.08.2026)
4. BIMpedia (Plandata): Familienkatalog TGA, https://www.bimpedia.eu/artikel/1852-familienkatalog-tga (abgerufen am 25.08.2026)
5. BauNetz Wissen: Industry Foundation Classes (IFC), https://www.baunetzwissen.de/integrales-planen/fachwissen/standardisierung/industry-foundation-classes-ifc-5288161 (abgerufen am 25.08.2026)
6. Baunormenlexikon: DIN 276, Ausgabe 2018-12 (Normnachweis), https://www.baunormenlexikon.de/norm/din-276/c2c8d430-8f0d-465c-b1cd-bb12f1febad5 (abgerufen am 25.08.2026)
7. MT-Ingenieure: KG 440, Leistungen der Kostengruppe 440 nach DIN 276, https://www.mt-ing.de/tga-wissen/kg-440-leistungen-der-kostengruppe-440-nach-din-276/ (abgerufen am 25.08.2026)
8. Build-Ing.: Informationsanforderungen gemäß DIN EN ISO 19650, https://www.build-ing.de/fachartikel/detail/informationsanforderungen-gemaess-dineniso19650/ (abgerufen am 25.08.2026)
9. BIM Deutschland: Standards, Normen und Richtlinien, https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien (abgerufen am 25.08.2026)
10. Bundesingenieurkammer: Umfrage: Fehlende Nachfrage bremst Digitalisierung von Ingenieurbüros aus (20.12.2022), https://bingk.de/umfrage-fehlende-nachfrage-bremst-digitalisierung-von-ingenieurbueros-aus/ (abgerufen am 25.08.2026)
11. VDI 3805: Elektronischer Produktdatenaustausch in der TGA, https://www.vdi3805.eu/vdi-3805 (abgerufen am 25.08.2026)
12. Eigene Ansprache-Kartei von BimWired: 192 von uns durchgesehene, öffentlich zugängliche Profile von Elektro- und TGA-Planungsbüros in Deutschland, Österreich und der Schweiz, mit einem von uns notierten Ansatzpunkt je Büro (unveröffentlicht, Stand August 2026, nicht repräsentativ)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
