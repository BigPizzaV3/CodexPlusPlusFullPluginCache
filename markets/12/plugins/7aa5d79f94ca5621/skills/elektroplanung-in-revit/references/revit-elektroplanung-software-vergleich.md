---
titel: "Revit für Elektroplaner: Bordmittel, Add-ins oder TGA-Spezialsoftware?"
quelle: https://bimwired.com/landing/wissen/revit-elektroplanung-software-vergleich.html
stand: 2026-08-25
art: artikel
fragen:
  - "Revit oder Spezialsoftware für die Elektroplanung?"
  - "Was können die Revit-Bordmittel in der Elektroplanung?"
  - "Wann lohnt sich ein Elektro-Add-in für Revit?"
  - "Wann ist TGA- oder CAE-Spezialsoftware die bessere Wahl?"
  - "Welcher Weg passt zu welchem Planungsbüro?"
---

# Revit für Elektroplaner: Bordmittel, Add-ins oder TGA-Spezialsoftware?

Für die Elektroplanung in deutschen Büros gibt es drei Wege, die alle tragen: die Revit-Bordmittel, bei denen Schema und Nachweise Handarbeit bleiben; Revit mit einem Elektro-Add-in oder einer CAE-Kopplung; und eigenständige TGA- oder CAE-Spezialsoftware. Keiner davon ist pauschal überlegen. Die Entscheidung hängt an drei Fragen: Verlangen Ihre Auftraggeber BIM-Modelle? Welche Werkzeuge und Kenntnisse sind im Büro vorhanden? Und wo sollen Verteilerdokumentation und Berechnungen entstehen? Dieser Vergleich stützt sich auf verlinkte Quellen, und wer ihn geschrieben hat, steht gleich im ersten Abschnitt.

## Das Wichtigste in Kürze

- Die Revit-Bordmittel bilden Stromkreise und Panel Schedules nach US-Konvention. Deutsche Elektro-Beschriftungen fehlen laut Mensch und Maschine in den Standardvorlagen, eine vollständige Kabelberechnung nach DIN VDE fehlt laut BEEL.
- Elektro-Add-ins und Kopplungen (belegt sind BEEL/elkoBIM, MagiCAD und eXs) ergänzen Schemata und Fachrechnungen. Laut einem Advertorial in der tab sind die Berechnungen das zentrale Verkaufsargument solcher Erweiterungen.
- Elektro-CAD und CAE sind ein eigener Markt: Der große Vergleich auf streit-software.de behandelt neun Anbieter und erwähnt Revit nicht.
- Einen generellen BIM-Zwang gibt es nicht. Laut Bundesingenieurkammer wenden 28 % der Ingenieurbüros BIM an, 79 % berichten von fehlender Nachfrage privater Auftraggeber. Der Druck kommt projektweise.
- Transparenz: Dieser Vergleich stammt von BimWired.

## Überblick

| Punkt | Detail |
|---|---|
| Die drei Wege | Bordmittel mit Handarbeit, Revit plus Add-in oder CAE-Kopplung, eigenständige TGA-/CAE-Spezialsoftware |
| Bordmittel-Lücken | keine vollständige Kabelberechnung nach DIN VDE (BEEL); Vorlagen ohne deutsche Elektro-Beschriftungen (Mensch und Maschine) |
| CAE-Welt | eigener Markt: neun Anbieter im streit-software.de-Vergleich ohne Revit; 27 Programme in der TGA-Marktübersicht |
| Marktkontext | 28 % der Ingenieurbüros mit BIM (Bundesingenieurkammer 2022); 18 % Einsatz im Bau- und Ausbaugewerbe (Bitkom 2025) |

## Inhaltsverzeichnis

- Wer schreibt diesen Vergleich?
- Warum fehlt ein neutraler Vergleich zur Revit-Elektroplanung?
- Weg 1: Was können die Revit-Bordmittel, und was fehlt ihnen?
- Weg 2: Was leisten Elektro-Add-ins und CAE-Kopplungen für Revit?
- Weg 3: Wann bleibt TGA- oder CAE-Spezialsoftware die richtige Wahl?
- Die Vergleichstabelle
- Welcher Weg passt zu welchem Büro?
- So hilft BimWired
- Häufige Fragen (FAQ)
- Quellen

## Wer schreibt diesen Vergleich?

Dieser Vergleich stammt von BimWired, und ich schreibe ihn als Planerin, die an genau so einem Werkzeug arbeitet: einem browserbasierten Editor für Stromkreise, Verteilerdokumentation und Familienbibliotheken rund um Revit. Ein neutraler Schiedsrichter bin ich also nicht. Damit der Text trotzdem etwas taugt, halte ich mich an drei Regeln. Jede Aussage über ein Fremdprodukt stützt sich auf eine verlinkte Quelle mit Abrufdatum. Wo mir Belege fehlen, bleibt es bei einer Aussage über die Kategorie oder bei einer Einschätzung, die als solche gekennzeichnet ist. BimWired ordne ich als einen von mehreren Wegen ein, mit seinen Grenzen. Die Quellen stehen am Artikelende; prüfen Sie sie selbst.

## Warum fehlt ein neutraler Vergleich zur Revit-Elektroplanung?

Wer die Kauffrage „Revit plus Erweiterung oder TGA-Spezialsoftware?“ recherchiert, landet in zwei getrennten Welten. Der große deutschsprachige Vergleich „Elektroplanung-Software“ auf streit-software.de stellt neun Anbieter gegenüber, und Revit kommt darin nicht vor. Die Marktübersicht der TGA-CAD-Programme auf tga-fachplaner.de (Stand 28.11.2025) listet 27 Programme in einer Tabelle, geht bei den Elektro-Workflows aber nicht in die Tiefe. Im Nova-Anwenderforum wiederum diskutieren Planer den Umstieg auf Revit, weil Hersteller ihre 3D-Daten teils nur noch als Revit-Familien liefern. Die Frage, die zwischen diesen Welten liegt, beantwortet bisher niemand. Deshalb dieser Artikel.

Zum Marktbild gehört auch, dass der BIM-Druck kleiner ist, als es oft klingt. Laut einer Umfrage der Bundesingenieurkammer (2022) wenden 28 % der Ingenieurbüros BIM an, und 79 % berichten, dass private Auftraggeber BIM nicht nachfragen. Im Bau- und Ausbaugewerbe setzen laut Bitkom (2025) 18 % der Unternehmen BIM-Software ein. Der Druck entsteht projektweise, über Auftraggeber und über Herstellerdaten.

## Weg 1: Was können die Revit-Bordmittel, und was fehlt ihnen?

Die Revit-Bordmittel bilden Stromkreise, fassen Lasten je Verteiler zusammen und dokumentieren sie als Panel Schedule, eine Verteilertabelle nach US-Konvention. Deutsche Verteilerdokumentation und Berechnungen nach DIN VDE gehören nicht zum Lieferumfang.

Die erste Hürde ist die US-Logik. Ein Stromkreis entsteht nur, wenn Panel Name, Verteilersystem (Distribution System) und der elektrische Anschluss der Familie zusammenpassen; in einem Thread im deutschsprachigen Autodesk-Forum scheitert ein Einsteiger genau daran. Deutsche Beschriftungen sind Einrichtungsarbeit. Laut Mensch und Maschine enthalten die Standardvorlagen keine Beschriftungen für elektrische Ausstattungen wie Schalter, Steckdosen und Verteilungen, und die Stromkreis-Benennung lässt sich erst seit Revit 2021 konfigurieren. Wie die Einrichtung Schritt für Schritt geht, steht im Leitfaden [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html).

Bei der Dokumentation endet der Weg vor dem deutschen Verteilerplan. BEEL hält fest, dass Revit allein die Anforderungen der Dokumentennorm DIN EN 61082 nicht vollständig erfüllt und Verteilerschemata Handarbeit bleiben. Im englischsprachigen Autodesk-Forum wird für ein Einlinienschema eine Zeichenansicht nach Art früherer AutoCAD-Zeichnungen empfohlen, oder gleich AutoCAD mit Verknüpfung. Beides hat keinen Modellbezug und aktualisiert sich nicht automatisch; wer umplant, zeichnet nach.

Bei den Nachweisen kommt die deutlichste Aussage von einem Anbieter, der selbst Revit-Elektrowerkzeuge verkauft: BEEL schreibt, Revit biete „keine vollständige Kabelberechnung nach DIN VDE (Spannungsfall, Kurzschlussfestigkeit, Strombelastbarkeit)“. Das MagiCAD-Advertorial in der Fachzeitschrift tab ergänzt, Revit sei nicht von Haus aus auf die detaillierte Modellierung elektrischer Gebäudesysteme ausgerichtet und werde vielerorts ausschließlich für die SHKL-Projektierung genutzt. Was sich trotzdem automatisiert prüfen lässt, ordnet der Artikel [VDE-Prüfungen in der Elektroplanung mit Revit](https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html) ein. Die reinen Bordmittel passen aus meiner Sicht dorthin, wo die BIM-Koordination im Vordergrund steht und Schemata wie Nachweise in anderen Werkzeugen entstehen dürfen.

## Weg 2: Was leisten Elektro-Add-ins und CAE-Kopplungen für Revit?

Add-ins und Kopplungen setzen dort an, wo die Bordmittel aufhören: deutsche Schemata, Fachrechnungen, Massenauswertung. Es gibt zwei Muster. Ein Add-in arbeitet in Revit selbst, eine Kopplung tauscht Daten mit einer eigenständigen CAE-Software aus.

Für den Add-in-Weg steht BEEL/elkoBIM. Der Anbieter betreibt einen deutschsprachigen Themenhub, der von Stromkreisen und Verteilern bis zu 2D-Schemen und Massenauswertung reicht, und positioniert sein Add-in elkoBIM als Antwort auf die Schema-Lücke, die er selbst benennt. MagiCAD erweitert Revit ebenfalls um Elektro-Funktionen; im tab-Advertorial sind Berechnungen wie Spannungsfall und Kabeldimensionierung das zentrale Argument. Für den Kopplungs-Weg steht der CAE-Hersteller eXs: Revit-Stromkreisdaten speisen automatisch erzeugte Verteilerpläne, Sicherungskennzeichen fließen nach Revit zurück, beworben als Schließen einer wichtigen Lücke im BIM-Prozess.

Dieser Weg passt für Büros, die im Revit-Ökosystem bleiben wollen und dort deutsche Dokumentation samt Nachweisen brauchen. Weitere Werkzeuge dieser Kategorie gibt es; zu ihnen liegen mir keine geprüften Quellen vor, deshalb nenne ich sie nicht. Wie das Zieldokument aussehen sollte, beschreibt der Artikel [Verteilerplan und Stromlaufplan normgerecht erstellen](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html).

## Weg 3: Wann bleibt TGA- oder CAE-Spezialsoftware die richtige Wahl?

Die deutschsprachige Elektro-CAD- und CAE-Welt ist ein eigener, etablierter Markt. Der Vergleich auf streit-software.de behandelt neun Anbieter, ohne Revit zu erwähnen; die TGA-Marktübersicht listet 27 Programme. Ihre Stärke liegt nach meiner Einschätzung in Berechnung und Schema. Dafür spricht, dass genau diese Fähigkeiten den Revit-Erweiterungen als Verkaufsargument dienen und dass der CAE-Hersteller eXs die Brücke zu Revit selbst baut.

Reibung entsteht bei der Modellkoordination. Im Nova-Anwenderforum diskutieren Planer den Umstieg auf Revit mit Berechnungssoftware, weil Hersteller 3D-Daten teils nur noch als Revit-Familien liefern. Wo Auftraggeber Fachmodelle verlangen, muss die CAE-Welt koppeln, oder das Büro fährt zweigleisig.

Ohne Revit-Pflicht bleibt der Weg tragfähig. Eingespielte Werkzeuge, vorhandenes Know-how und ein Auftragsbestand ohne Modellanforderungen sind gute Gründe, die CAE-Landschaft zu behalten. Ich würde in dieser Lage nicht wechseln, nur um gewechselt zu haben.

Abbildung: Fünf Arbeitsschritte von den Familien über Stromkreise, Nachweise und Verteilerplan bis zur Umplanung, darunter drei Bahnen: die Revit-Bordmittel tragen den Anfang und brechen bei Nachweisen und Modellbezug ab, der Weg mit Add-in oder Kopplung läuft durch, die TGA- und CAE-Spezialsoftware trägt die Mitte und bleibt an beiden Modell-Enden offen. Achten Sie weniger darauf, wie viel ein Weg trägt, als darauf, an welcher Stelle er abgibt: dort entsteht im Büro die Doppelpflege.

## Die Vergleichstabelle

In der vierten Spalte ordne ich das eigene Produkt ein. Neben Add-ins und Kopplungen gibt es modellgespeiste Browser-Editoren: Sie übernehmen Stromkreisdaten aus Revit, bauen Aufteilung und Verteilerdokumentation außerhalb von Revit auf und schreiben Stromkreisnummern ins Modell zurück. BimWired gehört in diese Kategorie, mit klaren Grenzen: keine Kabelberechnung, kein Aufbauplan, keine Allpolig-Darstellung.

| Kriterium | Revit-Bordmittel | Revit + Add-in/Kopplung | TGA-/CAE-Spezialsoftware | BimWired (Einordnung) |
|---|---|---|---|---|
| Deutsche Verteilerdokumentation | Panel Schedule nach US-Konvention; Einlinienschema laut Autodesk-Forum ohne Modellbezug gezeichnet | Kernthema: BEEL positioniert elkoBIM für Verteilerschemata, eXs erzeugt Verteilerpläne aus Revit-Stromkreisdaten | traditioneller Kern der Kategorie (Einschätzung) | einpolige Übersicht nach DIN EN 61082-1 auf A3 als PDF und DXF; kein Aufbauplan, keine Allpolig-Darstellung |
| VDE-Berechnungen (Spannungsfall, Kabel) | laut BEEL keine vollständige Kabelberechnung nach DIN VDE | zentrales Verkaufsargument laut tab-Advertorial (Spannungsfall, Kabeldimensionierung) | Kernkompetenz der Kategorie (Einschätzung) | bewusst nicht enthalten; feste Prüfungen auf Überlast, RCD-Pflicht, Mindestquerschnitt mit DIN-18015-Bezügen |
| Familien und Content | Standardvorlagen laut Mensch und Maschine ohne Elektro-Beschriftungen; Familien brauchen elektrische Anschlüsse | Anbieter begleiten mit Schulungen (BEEL); Familienpflege bleibt beim Büro (Einschätzung) | Hersteller liefern 3D-Daten teils nur noch als Revit-Familien (Nova-Anwenderforum) | Familienbibliothek im Browser mit IFC- und DIN-276-Klassifizierung, Releases und Cloud-Update (Nutzung ab Basis) |
| Lernkurve und Team | US-Logik als Hürde: Panel Name, Verteilersystem und Familienanschluss müssen zusammenpassen (Autodesk-Forum) | Revit-Kenntnisse plus Werkzeugschulung; BEEL bietet Schulungen und einen YouTube-Kanal | eingespielt für Bestandsteams; der Umstieg ist im Nova-Anwenderforum ein eigenes Thema | Browser-Editor plus Revit-Plugin (Revit 2025 bis 2027); Rundlauf in drei Schritten |

Zellen mit „Einschätzung“ sind redaktionelle Einordnungen von BimWired; alles Übrige stützt sich auf die Belege im Quellenverzeichnis.

## Welcher Weg passt zu welchem Büro?

Die Empfehlungen zu den vier Profilen sind werkzeugoffen. Wo das eigene Produkt passt, sage ich es dazu, und wo es nicht reicht, auch.

### Reines Elektro-Fachbüro mit CAE-Bestand

Behalten Sie den eingespielten CAE-Weg für Berechnung und Schema. Die Revit-Frage stellt sich projektweise: wenn Auftraggeber Fachmodelle verlangen oder Herstellerdaten nur als Revit-Familien vorliegen (Nova-Anwenderforum). Für den Übergang sind Kopplungen die naheliegende Kategorie; eXs beschreibt die bidirektionale Übergabe.

### TGA-Generalist mit Revit-Pflichtprojekten

Läuft SHKL bereits in Revit, ist Elektro eine Ergänzungsfrage: Add-in im Modell oder modellgespeister Editor daneben. Entscheidend sind die Familien. Ohne elektrische Anschlüsse und einheitliche Symbolik entsteht kein Stromkreis-Workflow, egal mit welchem Werkzeug. BimWired passt in dieses Profil, weil Stromkreis-Workflow und Familienbibliothek dort zusammenkommen; genau für diese Kombination habe ich es gebaut.

### Kleines Büro ohne CAE-Landschaft

Der Einstieg über die Bordmittel ist möglich, aber einrichtungsintensiv; der Forum-Thread zeigt, wie Einsteiger an der US-Logik hängen bleiben. Kalkulieren Sie die Handarbeit für Schema und Nachweise realistisch, sie ist erfahrungsgemäß größer als gedacht. Ein browserbasierter Weg wie BimWired senkt die Hürde bei Stromkreisen und Verteilerübersicht, ersetzt aber keine Kabelberechnung. Die Nachweise bleiben eine eigene Aufgabe.

### Büro mit BIM-Auftraggebern

Verlangen Auftraggeber Fachmodelle, führt an einem Revit-zentrierten Weg wenig vorbei. Die Verteilerdokumentation sollte dann aus den Modelldaten entstehen und nicht daneben. Wählen Sie Werkzeuge, die Modell und Dokumentation koppeln; sonst pflegen Sie jede Umplanung doppelt.

So gehen Sie die Entscheidung an:

1. Klären Sie die Auftragslage: Verlangen Auftraggeber-Informationsanforderungen oder Ausschreibungen der nächsten zwölf bis 24 Monate Fachmodelle, und in welchem Format?
2. Werkzeuge sind schneller gewechselt als eingespielte Standards.
3. Legen Sie fest, wo die Dokumente entstehen: Verteilerdokumentation und Nachweise künftig im Modellumfeld oder in der CAE-Welt?
4. Fahren Sie einen Pilot.
5. Entscheiden Sie die Familienfrage mit: Wer pflegt die Bibliothek, und wie kommen neue Stände ins Büro?

## Einordnung: das Werkzeug BimWired

BimWired ist eine Cloud-Webanwendung mit Revit-Plugin für Revit 2025, 2026 und 2027, also ein modellgespeister Browser-Editor im Sinne dieses Vergleichs. Der Revit-Befehl „Stromkreisplan senden“ sammelt Leuchten, Schalter, Steckdosen und Elektrogeräte mit Raum, Ebene, Scheinleistung, Spannung und Polzahl. Im Browser bauen Sie Verteiler und Stromkreise auf, auf Wunsch mit automatischer Aufteilung in thematische Gruppen je Ebene. „Stromkreise übernehmen“ schreibt Stromkreisnummern und je nach Einstellung Verteiler, Sicherung, RCD, Kabel und Phasen zurück; fehlende Projektparameter legt das Plugin an. Der Verteilerplan entsteht als einpolige Übersicht nach DIN EN 61082-1 auf A3, als mehrseitiges Vektor-PDF und als DXF je Blatt. Deterministische Prüfungen melden Überlast, fehlende RCD-Zuordnung und zu geringe Querschnitte mit Bezügen zur DIN 18015. Ein optionaler KI-Prüfblick liefert höchstens zehn Hinweise als zweite Meinung; er ändert nichts am Plan und ist keine Normprüfung. Bewusst nicht enthalten sind Kabel- und Spannungsfallberechnung, Aufbauplan und Allpolig-Darstellung. Das ist Absicht: Ich wollte den Rundlauf zwischen Modell und Verteilerplan sauber lösen, nicht die CAE-Welt nachbauen.

## Häufige Fragen (FAQ)

### Kann ich mit Revit-Bordmitteln einen deutschen Verteilerplan erstellen?

Nicht direkt. Das Bordmittel-Ergebnis ist ein Panel Schedule, eine Verteilertabelle nach US-Konvention, und der Anbieter BEEL hält fest, dass Revit allein die Anforderungen der Dokumentennorm DIN EN 61082 nicht vollständig erfüllt. Für den deutschen Verteilerplan braucht es ein Add-in, eine CAE-Kopplung oder einen modellgespeisten Editor.

### Welche Berechnungen fehlen den Revit-Bordmitteln?

Laut BEEL fehlt eine vollständige Kabelberechnung nach DIN VDE, also Spannungsfall, Kurzschlussfestigkeit und Strombelastbarkeit. Genau diese Berechnungen nennt das MagiCAD-Advertorial in der tab als zentrales Argument für Revit-Erweiterungen. Die Nachweise entstehen deshalb in Zusatzwerkzeugen, in der CAE-Welt oder als separate Berechnung.

### Muss ein deutsches Elektro-Planungsbüro auf Revit umsteigen?

Nein, einen generellen Zwang gibt es nicht. Laut Bundesingenieurkammer (2022) wenden 28 % der Ingenieurbüros BIM an, und 79 % berichten, dass private Auftraggeber BIM nicht nachfragen. Druck entsteht projektweise, über Anforderungen der Auftraggeber und über Hersteller, die 3D-Daten teils nur noch als Revit-Familien liefern, wie Planer im Nova-Anwenderforum berichten.

### Ist BimWired ein Ersatz für CAE-Software?

Nein. BimWired baut aus gesendeten Revit-Daten Stromkreise und eine einpolige Verteilerübersicht nach DIN EN 61082-1 auf und schreibt Nummern und Parameter zurück nach Revit. Für Netzberechnungen bleiben CAE-Werkzeuge oder separate Nachweise nötig.

## Quellen

1. streit-software.de: Elektroplanung-Software (Vergleich). https://www.streit-software.de/wissen/elektroplanung-software (abgerufen am 25.08.2026)
2. tga-fachplaner.de: Marktübersicht TGA-CAD-Programme und Trends im Überblick (Stand 28.11.2025). https://www.tga-fachplaner.de/projektierung/marktuebersicht-tga-cad-programme-und-trends-im-ueberblick (am 25.08.2026 im Browser geprüft)
3. Nova-Anwenderforum: Autodesk Revit mit Berechnungssoftware. http://novauser.xobor.de/t1427f36-Autodesk-Revit-mit-Berechnungssoftware.html (abgerufen am 25.08.2026)
4. Mensch und Maschine: Revit MEP 2021, Benennung elektrischer Stromkreise. https://support.mum.de/help/de-de/70-revit-mep/200-revit-mep-2021-benennung-elektrischer-stromkreise (abgerufen am 25.08.2026)
5. tab: Advertorial MagiCAD, So können Sie in Revit auch Elektro planen. https://www.tab.de/artikel/advertorial-magicad-so-koennen-sie-in-revit-auch-elektro-planen-4021922.html (abgerufen am 25.08.2026)
6. Autodesk-Forum (Revit MEP): Hilfe bei Elektroplanung. https://forums.autodesk.com/t5/revit-mep-forum/hilfe-bei-elektroplanung/td-p/9818401 (abgerufen am 25.08.2026)
7. Autodesk-Forum (Revit MEP): Electrical single line diagram. https://forums.autodesk.com/t5/revit-mep-forum/electrical-single-line-diagram/td-p/8667884 (abgerufen am 25.08.2026)
8. BEEL: Revit Elektroplanung. https://www.beel.de/revit-elektroplanung/ (abgerufen am 25.08.2026)
9. BEEL: Revit Stromlaufplan. https://www.beel.de/revit/revit-stromlaufplan/ (abgerufen am 25.08.2026)
10. BEEL: Revit Kabel. https://www.beel.de/revit/revit-kabel/ (abgerufen am 25.08.2026)
11. eXs: Elektroplanung in BIM-Projekten. https://www.exs-cae.com/elektroplanung-in-bim-projekten/ (abgerufen am 25.08.2026)
12. Bundesingenieurkammer: Umfrage. Fehlende Nachfrage bremst Digitalisierung von Ingenieurbüros aus (20.12.2022). https://bingk.de/umfrage-fehlende-nachfrage-bremst-digitalisierung-von-ingenieurbueros-aus/ (abgerufen am 25.08.2026)
13. Bitkom: Bauwesen: BIM-Software erst bei knapp einem Fünftel im Einsatz (19.09.2025). https://www.bitkom.org/Presse/Presseinformation/Bauwesen-BIM-Software-Einsatz (abgerufen am 25.08.2026)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/revit-elektroplanung-software-vergleich.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
