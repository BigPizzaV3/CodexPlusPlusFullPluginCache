---
titel: "Elektroplanung in Revit: der Leitfaden für deutsche Büros"
quelle: https://bimwired.com/landing/wissen/elektroplanung-in-revit.html
stand: 2026-08-25
art: artikel
fragen:
  - "Wie funktioniert Elektroplanung in Revit nach deutschen Normen?"
  - "Ist Revit für deutsche Elektroplanung geeignet?"
  - "Welche Normen muss ich für die Elektroplanung kennen?"
  - "Braucht Revit Zusatzsoftware für Verteilerpläne und VDE-Nachweise?"
  - "Wo fange ich mit der Elektroplanung in Revit an?"
---

# Elektroplanung in Revit: der Leitfaden für deutsche Büros

Elektroplanung in Revit funktioniert für deutsche Büros, aber nicht ab Werk. Revit denkt in US-Konzepten wie Distribution Systems und Panel Schedules; deutsche Spannungswelten, Familien mit elektrischen Anschlüssen und Beschriftungen müssen Sie zuerst selbst aufbauen. Danach modellieren die Bordmittel zuverlässig und bilden Stromkreise, nur die deutschen Ergebnis-Formate liefern sie nicht: keinen Verteilerplan nach deutschem Dokumentationsverständnis und keine Kabelberechnung nach DIN VDE. Diese Seite beantwortet die Grundsatzfragen kompakt und verlinkt für jede Aufgabe eine eigene Vertiefung, von der Leistungsbilanz über Stromkreise und Verteilerplan bis zur Familienbibliothek.

## Das Wichtigste in Kürze

- Geeignet, mit Einrichtung: Ein Stromkreis entsteht in Revit erst, wenn Spannungen, Verteilersystem und der elektrische Anschluss der Familie zusammenpassen. Die Standardvorlagen enthalten laut Mensch und Maschine „keine Beschriftung für elektrische Ausstattungen wie Schalter, Steckdosen und Verteilungen“.
- Die deutschen Ergebnis-Formate fehlen. Je Verteiler liefern die Bordmittel einen Panel Schedule nach US-Konvention, und eine Kabelberechnung nach DIN VDE bringt Revit laut dem Elektro-Spezialisten BEEL nicht mit.
- Ein Projekt läuft in fünf Etappen: Leistungsbilanz, Stromkreise, Verteilerplan, Prüfungen, und darunter die Familienbibliothek als Fundament. Zu jeder Etappe gibt es hier eine eigene Seite.
- Zur Einordnung: In einer Umfrage der Bundesingenieurkammer von Ende 2022 gaben 28 Prozent der Ingenieurbüros an, BIM anzuwenden. Die Methode wächst, flächendeckender Standard ist sie in der Planungslandschaft noch nicht.

## Überblick: welche Aufgabe, welche Seite?

Die Tabelle ist die Landkarte dieses Leitfadens. Die Grundsatzfragen beantwortet der Rest der Seite.

| Ihre Aufgabe | Vertiefung | Was Sie dort finden |
|---|---|---|
| Anschlussleistung bemessen | [Leistungsbilanz nach DIN 18015-1](https://bimwired.com/landing/wissen/leistungsbilanz-din-18015-1.html) | Bedarfskurven, Sonderlasten, PV-Irrtum, Netzbetreiber |
| Stromkreise im Modell aufbauen | [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html) | US-Logik einrichten, Familien-Voraussetzungen, Schrittfolge |
| Verteilerplan liefern | [Verteilerplan und Stromlaufplan normgerecht erstellen](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html) | Begriffe, Normrahmen, Weg aus dem Modell |
| Nachweise und Prüfungen ordnen | [VDE-Prüfung in der Revit-Elektroplanung](https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html) | Was sich automatisieren lässt, was Ingenieurleistung bleibt |
| Familien als Firmenstandard | [Revit-Familienbibliothek fürs TGA-Büro](https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html) | Naming, Parameter, IFC und DIN 276, Verteilung |
| Einzelne Familie richtig bauen | [Revit-Familien für die TGA erstellen](https://bimwired.com/landing/wissen/revit-familien-erstellen-host-skelett.html) | Vorlage, Host-Arten, verlinkte Architektur, typische Fehler |
| Werkzeugfrage klären | [Software für die Revit-Elektroplanung im Vergleich](https://bimwired.com/landing/wissen/revit-elektroplanung-software-vergleich.html) | Bordmittel, Add-ins, CAE-Kopplung, Editor-Wege |
| Ablauf am Beispiel: Verteilerplan | [Praxisszenario Verteilerplan](https://bimwired.com/landing/wissen/praxisszenario-verteilerplan.html) | Umstieg vom Zweitwerkzeug, offene Beispielrechnung |
| Ablauf am Beispiel: Bibliothek | [Praxisszenario Familienbibliothek](https://bimwired.com/landing/wissen/praxisszenario-familienbibliothek.html) | Drei Standorte, ein Stand, offene Beispielrechnung |
| Ablauf am Beispiel: Bilanz | [Praxisszenario Leistungsbilanz](https://bimwired.com/landing/wissen/praxisszenario-leistungsbilanz-mfh.html) | Mehrfamilienhaus mit Wärmepumpe und Wallboxen |
| Vor der Planabgabe prüfen | [Checkliste Verteilerplan](https://bimwired.com/landing/wissen/checkliste-verteilerplan.html) | Pflichtinhalte zum Abhaken |
| Vor der Bibliotheks-Freigabe prüfen | [Checkliste Bibliotheks-Freigabe](https://bimwired.com/landing/wissen/checkliste-bibliothek-freigabe.html) | Prüfpunkte, bevor ein Stand ins Büro geht |
| Begriffe nachschlagen | [Glossar](https://bimwired.com/landing/wissen/glossar.html) | Fachbegriffe von Panel Schedule bis einpolige Übersicht |

## Inhaltsverzeichnis

- Ist Revit für deutsche Elektroplanung geeignet?
- In fünf Etappen durch das Projekt
- Was bringt Revit nicht mit?
- Drei modellhafte Szenarien
- Zum Nachschlagen: Checklisten und Glossar
- So hilft BimWired
- Häufige Fragen (FAQ)

## Ist Revit für deutsche Elektroplanung geeignet?

Ja, mit Einrichtung. Aus meiner eigenen Planungsarbeit kann ich das bestätigen: Revit modelliert Elektro zuverlässig und bildet Stromkreise samt Lastsummen je Verteiler, sobald Spannungen, Verteilersysteme und Familien mit elektrischen Anschlüssen zusammenpassen. Von allein passiert das nicht. Ein MagiCAD-Advertorial in der Fachzeitschrift tab beschreibt die Ausgangslage recht offen: Revit sei „nicht nativ auf das Zeichnen von Leitungen und die detaillierte Modellierung von elektrischen Gebäudesystemen ausgerichtet“ und werde deshalb oft „ausschließlich für die SHKL-Projektierung genutzt“. Dazu kommt die Vorlagen-Lücke, die Mensch und Maschine dokumentiert: keine deutschen Beschriftungen für Schalter, Steckdosen und Verteilungen, und die Stromkreis-Benennung lässt sich erst seit Revit 2021 konfigurieren. Beides ist lösbar. Es kostet aber Einrichtungsarbeit in Vorlage und Bibliothek, und die sollte man einplanen, bevor das erste Projekt im Modell steckt. Wie die Kette aus Spannungswelt, Verteilersystem und Familienanschluss aufgebaut wird, zeigt [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html) Schritt für Schritt.

## In fünf Etappen durch das Projekt

Ich habe die Etappen so sortiert, wie sie im Projekt aufeinander aufbauen. Jede hat hier eine eigene Vertiefung:

1. Anschlussleistung bemessen. Die Leistungsbilanz nach DIN 18015-1 setzt die Grundlast über Bedarfskurven an, Sonderlasten wie Wärmepumpe und Wallboxen zählen separat. Den Rechenweg zeigt der [Leitfaden zur Leistungsbilanz nach DIN 18015-1](https://bimwired.com/landing/wissen/leistungsbilanz-din-18015-1.html).
2. Stromkreise aufbauen. Spannungen, Verteilersysteme und Familienanschlüsse bilden die Kette, an der Einsteiger regelmäßig scheitern. Die Einrichtung führt [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html) vor.
3. Verteilerplan liefern. Aus den Stromkreisdaten entsteht die einpolige Übersicht je Verteiler mit Kennzeichen, Absicherung und Kabeln. Begriffe und Normen ordnet [Verteilerplan und Stromlaufplan normgerecht erstellen](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html).
4. Prüfen und nachweisen. Überlast, RCD-Pflicht und Querschnitte lassen sich regelhaft prüfen, Spannungsfall und Selektivität bleiben Ingenieurleistung. Wo diese Grenze verläuft, steht unter [VDE-Prüfung in der Revit-Elektroplanung](https://bimwired.com/landing/wissen/vde-pruefung-elektroplanung-revit.html).
5. Bibliothek pflegen. Ohne Familien mit sauberen Anschlüssen, Parametern und Symbolen trägt keine der anderen Etappen; die Bibliothek steht am Ende der Liste, obwohl sie zuerst dran ist. Das Fundament beschreibt [Revit-Familienbibliothek fürs TGA-Büro](https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html); wie eine einzelne Familie entsteht und warum die Host-Art über ihren Einsatz in verlinkter Architektur entscheidet, steht in [Revit-Familien für die TGA erstellen](https://bimwired.com/landing/wissen/revit-familien-erstellen-host-skelett.html).

Abbildung: Ablauf der fünf Etappen eines Elektroprojekts: Anschlussleistung bemessen, Stromkreise aufbauen, Verteilerplan liefern, Prüfen und nachweisen, darunter die Familienbibliothek als Fundament. Die Bibliothek steht zuletzt in der Liste und ist trotzdem zuerst dran: ohne sie trägt keine der vier Etappen darüber.

## Was bringt Revit nicht mit?

Drei Lieferstücke deutscher Elektroplanung sind keine Revit-Bordmittel: der Verteilerplan, die VDE-Rechnung und die deutsche Symbolik. Was Revit je Verteiler ausgibt, ist ein Panel Schedule, eine Tabelle nach US-Konvention und kein Plandokument nach deutschem Dokumentationsverständnis. Bei den Berechnungen ist die Lage dokumentiert, ausgerechnet vom Anbieter eines Elektro-Add-ins: „Revit bietet keine vollständige Kabelberechnung nach DIN VDE (Spannungsfall, Kurzschlussfestigkeit, Strombelastbarkeit)“, schreibt BEEL. Und Schaltzeichen nach deutscher Legende samt Beschriftungen liegen den Standardvorlagen ebenfalls nicht bei. Deutsche Büros schließen diese Lücken auf vier Wegen: Schema von Hand neben dem Modell, Elektro-Add-in in Revit, Kopplung an eine CAE-Software oder ein modellgespeister Editor außerhalb von Revit. Welcher Weg zu welchem Büro passt, sortiert der [Software-Vergleich zur Revit-Elektroplanung](https://bimwired.com/landing/wissen/revit-elektroplanung-software-vergleich.html).

## Drei modellhafte Szenarien

Drei Praxisszenarien spielen die Abläufe dieses Leitfadens an modellhaften Büros durch. Die Muster darin kenne ich aus eigenen Projekten, die Zahlen sind aber durchgehend als Beispielrechnung gekennzeichnet; Kundenberichte sind es nicht. Das [Praxisszenario Verteilerplan](https://bimwired.com/landing/wissen/praxisszenario-verteilerplan.html) stellt ein Elektro-Fachbüro vom CAD-Zweitwerkzeug auf den Rundlauf aus dem Modell um, mit offener Break-even-Rechnung. Das [Praxisszenario Familienbibliothek](https://bimwired.com/landing/wissen/praxisszenario-familienbibliothek.html) führt die Familienbestände dreier Standorte eines TGA-Büros zu einem verbindlichen Stand zusammen. Das [Praxisszenario Leistungsbilanz](https://bimwired.com/landing/wissen/praxisszenario-leistungsbilanz-mfh.html) bemisst den Hausanschluss eines Mehrfamilienhauses mit Wärmepumpe, Wallboxen und Photovoltaik, ohne Excel-Bilanz.

## Zum Nachschlagen: Checklisten und Glossar

Für die tägliche Arbeit gibt es drei Nachschlage-Seiten. Die [Checkliste Verteilerplan](https://bimwired.com/landing/wissen/checkliste-verteilerplan.html) fasst die Pflichtinhalte zusammen, die vor der Planabgabe geprüft gehören, vom Betriebsmittelkennzeichen bis zur RCD-Zuordnung. Die [Checkliste Bibliotheks-Freigabe](https://bimwired.com/landing/wissen/checkliste-bibliothek-freigabe.html) listet die Prüfpunkte, bevor ein neuer Bibliotheksstand verbindlich ins Büro geht. Und das [Glossar](https://bimwired.com/landing/wissen/glossar.html) erklärt die Begriffe des Themas in je wenigen Sätzen, von Panel Schedule und Distribution System bis zur einpoligen Übersicht.

## Einordnung: das Werkzeug BimWired

BimWired ist mein eigenes Werkzeug, deshalb hier nüchtern, was es tut. Es ist eine Cloud-Webanwendung mit Revit-Plugin für Revit 2025 bis 2027 und setzt die fünf Etappen als Rundlauf um. Der Revit-Befehl „Stromkreisplan senden“ sammelt Leuchten, Schalter, Steckdosen und Elektrogeräte samt Raum und Ebene. Im Browser teilen Sie die Elemente auf Verteiler und Stromkreise auf, auf Wunsch automatisch nach thematischen Gruppen je Ebene; feste Prüfungen melden dabei Überlast, RCD-Pflicht und Mindestquerschnitte mit DIN-18015-Bezügen. „Stromkreise übernehmen“ schreibt Nummern, Sicherung, RCD und Kabel zurück ins Modell. Der Verteilerplan entsteht daraus als einpolige Übersicht auf A3 mit Schriftfeld nach DIN EN ISO 7200, exportierbar als mehrseitiges Vektor-PDF und als DXF. Genau dieser Schritt hat mich in eigenen Projekten am meisten Zeit gekostet, deshalb gibt es ihn. Die Leistungsbilanz nach DIN 18015-1 rechnet komplett im Editor, ein Modell braucht sie nicht. Spannungsfall und Selektivität bleiben auch damit Ingenieurleistung. KI-Vorschläge, etwa beim Einordnen unerkannter Elemente, bleiben Vorschläge. Sie entscheiden.

## Häufige Fragen (FAQ)

### Ist Revit für deutsche Elektroplanung geeignet?

Ja, mit Einrichtung. Modellieren, Stromkreise bilden und Lasten je Verteiler zusammenfassen funktioniert, sobald Spannungen, Verteilersysteme und Familien mit elektrischen Anschlüssen eingerichtet sind. Deutsche Ergebnis-Formate wie der Verteilerplan und Kabelberechnungen nach DIN VDE sind keine Bordmittel; dafür nutzen Büros ein Add-in, eine CAE-Kopplung oder einen modellgespeisten Editor.

### Welche Normen muss ich kennen?

Für Wohngebäude die DIN 18015-1 als Planungsgrundlage, für die Anlage die Reihe DIN VDE 0100 (etwa Teil 410 zum RCD-Schutz und Teil 520 zum Spannungsfall) sowie die DIN VDE 0298-4 zur Strombelastbarkeit. Für die Dokumentation gelten DIN EN 61082-1 und die Schaltzeichen der IEC 60617, für den Verteiler als Erzeugnis die DIN EN IEC 61439, für den Netzanschluss die VDE-AR-N 4100 mit der örtlichen TAB. Wie diese Prüfkette zusammenhängt, ordnet die Seite zu den VDE-Prüfungen in diesem Leitfaden.

### Brauche ich Zusatzsoftware neben Revit?

Für Modell, Stromkreisbildung und Mengenauswertung genügt Revit. Für normgerechte Verteilerpläne, Kabelberechnungen nach DIN VDE und deutsche Schaltzeichen brauchen Büros in der Praxis einen Zusatzweg; selbst der Add-in-Anbieter BEEL dokumentiert, dass Revit diese Berechnungen nicht mitbringt. Ob Add-in, CAE-Kopplung oder modellgespeister Editor passt, hängt von den Projekten und der Werkzeuglandschaft des Büros ab.

### Wo fange ich an?

Beim Fundament, auch wenn das unspektakulär klingt: Bringen Sie zuerst die Familienbibliothek in Ordnung, denn ohne Familien mit elektrischen Anschlüssen und einheitlichen Parametern entsteht weder ein Stromkreis noch eine belastbare Auswertung. Richten Sie danach die Stromkreis-Logik im Projekt ein und klären Sie früh, auf welchem Weg der Verteilerplan entstehen soll. Die Landkarte oben führt für jede dieser Aufgaben zur passenden Anleitung.

## Quellen

1. tab: Advertorial MagiCAD, So können Sie in Revit auch Elektro planen. https://www.tab.de/artikel/advertorial-magicad-so-koennen-sie-in-revit-auch-elektro-planen-4021922.html (abgerufen am 25.08.2026)
2. Mensch und Maschine: Revit MEP 2021, Benennung elektrischer Stromkreise. https://support.mum.de/help/de-de/70-revit-mep/200-revit-mep-2021-benennung-elektrischer-stromkreise (abgerufen am 25.08.2026)
3. BEEL: Revit Kabel. https://www.beel.de/revit/revit-kabel/ (abgerufen am 25.08.2026)
4. Bundesingenieurkammer: Umfrage, Fehlende Nachfrage bremst Digitalisierung von Ingenieurbüros aus. https://bingk.de/umfrage-fehlende-nachfrage-bremst-digitalisierung-von-ingenieurbueros-aus/ (abgerufen am 25.08.2026)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/elektroplanung-in-revit.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
