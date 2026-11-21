---
titel: "Praxisszenario: Verteilerpläne ohne Zweitwerkzeug, ein Elektro-Fachbüro stellt den Rundlauf um"
quelle: https://bimwired.com/landing/wissen/praxisszenario-verteilerplan.html
stand: 2026-08-25
art: szenario
fragen:
  - "Wie entsteht ein Verteilerplan direkt aus dem Revit-Modell?"
  - "Lohnt sich der Umstieg vom CAD-Zweitwerkzeug rechnerisch?"
  - "Was muss das Revit-Modell für den Stromkreis-Rundlauf mitbringen?"
  - "Wo liegen die Grenzen gegenüber einer CAE-Software?"
---

# Praxisszenario: Verteilerpläne ohne Zweitwerkzeug, ein Elektro-Fachbüro stellt den Rundlauf um

*Ein modellhaftes Szenario aus typischen Arbeitsabläufen deutscher Planungsbüros, kein Kundenbericht. Die Zahlen sind als Beispielrechnung gekennzeichnet.*

Ein Elektro-Fachbüro mit acht Personen plant seit zwei Jahren in Revit und zeichnet seine Verteilerpläne trotzdem in einem CAD-Zweitwerkzeug, mit Excel-Listen als Zwischenschritt. In diesem Szenario entsteht derselbe Plan als Rundlauf: Stromkreisdaten aus Revit senden, im Browser zum Verteilerplan ausarbeiten, als A3-Plansatz, Vektor-PDF und DXF ausgeben, die Ergebnisse zurück ins Modell stempeln. Eine konservative Beispielrechnung ergibt einen Break-even bei rund 67 vermiedenen Doppelarbeits-Stunden im Jahr. Was der Weg nicht liefert (Aufbauplan, Allpolig-Darstellung, Kabelberechnung), steht ebenfalls drin.

## Das Wichtigste in Kürze

- Der doppelte Weg, Modell in Revit und Verteilerplan daneben im Zweitwerkzeug, ist einer der am häufigsten dokumentierten Zeitfresser in der Elektro-Fachplanung mit Revit. In unserer eigenen Ansprache-Kartei haben wir bei 69 von 192 Büro-Profilen genau dieses Muster notiert. Der Vermerk stammt von uns, nicht von den Büros.
- Der Rundlauf macht die Zwischenlisten überflüssig: „Stromkreisplan senden" in Revit, Ausarbeitung im Plan-Editor im Browser, „Stromkreise übernehmen" schreibt Nummern, Sicherung, RCD und Kabel ins Modell zurück.
- Die Ausgabe ist eine aufgelöste einpolige Übersicht als A3-Plansatz (Schriftfeld nach DIN EN ISO 7200, Querverweise nach DIN EN 61082-1), dazu mehrseitiges Vektor-PDF, DXF je Blatt und QR-Etiketten für die Schränke.
- Aufbauplan, Allpolig-Darstellung und Kabelberechnung (etwa Spannungsfall) liefert der Rundlauf nicht. Dafür bleibt ein CAE- oder Berechnungswerkzeug zuständig.

## Ausgangslage

Das Büro, das ich hier annehme, taucht in der Recherche in dieser Form immer wieder auf: acht Personen, Elektro-Fachplanung für Wohn- und Gewerbebau, Revit seit zwei Jahren im Haus. Die Modelle sind ordentlich, Grundrisse und Ansichten kommen als Planlieferung aus Revit. Nur der Verteilerplan nicht. Nach der Entwurfsplanung exportiert das Büro Geräte- und Raumlisten nach Excel, sortiert dort die Stromkreise von Hand und zeichnet die Verteilerschemata im CAD-Zweitwerkzeug neu. Jede Umplanung, ein zusätzlicher Durchlauferhitzer, eine geänderte Raumaufteilung, wird danach zweimal nachgezogen: im Modell und im Schema. Welcher Stand führt, ist im Alltag Verhandlungssache. Ich habe das lange selbst so gemacht.

Das ist kein Einzelfall. Es gehört zu den Mustern, die uns in der eigenen Ansprache-Kartei am häufigsten begegnet sind: Wir haben bei BimWired 192 öffentlich zugängliche Profile und Internetauftritte von Elektro- und TGA-Planungsbüros aus Deutschland, Österreich und der Schweiz durchgesehen (Stand August 2026) und dabei je Büro notiert, welcher Ansatzpunkt für ein Anschreiben passt. Bei 69 Profilen haben wir vermerkt, dass der Verteiler- oder Stromlaufplan neben dem Modell entsteht. Das ist unsere Einschätzung aus dem, was diese Büros veröffentlichen, keine Aussage der Büros selbst, und die Kartei ist weder repräsentativ noch neutral erhoben. Auch außerhalb unserer Kartei ist die Lücke gut belegt. Im Autodesk-Forum raten erfahrene Anwender bis heute, ein Einlinienschema in einer Zeichenansicht mit Detaillinien zu zeichnen oder gleich in AutoCAD anzulegen und zu verknüpfen, ohne Modellbezug und ohne automatische Aktualisierung. Der Revit-Elektro-Spezialist BEEL hält fest, dass Revit allein die Anforderungen der DIN EN 61082 nicht vollständig erfüllt und Verteilerschemata Handarbeit bleiben. Der CAE-Hersteller eXs wirbt für die Übergabe von Revit-Stromkreisdaten in automatisch erzeugte Verteilerpläne ausdrücklich damit, eine Lücke im BIM-Prozess zu schließen. Wenn gleich mehrere Anbieter von dieser Lücke leben, ist die Doppelarbeit offenbar weit verbreitet.

Was fachlich in einen Verteilerplan gehört (Betriebsmittelkennzeichen, Absicherung, Querschnitt, Kabeltyp, RCD-Zuordnung), steht im Grundlagenartikel [Verteilerplan und Stromlaufplan normgerecht erstellen](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html). Hier geht es um den Ablauf.

## Der Weg

Das Revit-Modell bleibt, wie es ist. Der Ablauf hat vier Schritte.

1. Der Revit-Befehl „Stromkreisplan senden" sammelt Leuchten, Schalter, Steckdosen und Elektrogeräte mit Raum, Ebene, Anschlussleistung (VA), Spannung und Polzahl und übergibt sie an den Plan-Editor im Browser. Die Excel-Zwischenliste entfällt. Was der Rundlauf nicht zuordnen kann, klassifiziert auf Wunsch eine KI je Familien/Typ-Paar, mit Konfidenzangabe und Vorschau; übernommen wird nur, was Sie bestätigen. Die Grundlagen dazu stehen im Artikel [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html).
2. Im Plan-Editor bildet „Automatisch aufteilen" je Ebene einen Verteiler („UV EG", „UV 1. OG") und gruppiert thematisch: Licht, Steckdosen, Durchlauferhitzer, Außenbereich. Als Gruppenkopf wählt das Büro „Vorsicherung + FI", also eine D0-Vorsicherung, selektiv zum größten Leitungsschutzschalter der Gruppe ausgelegt (1,6-facher Nennstrom nach DIN VDE 0100-530), plus zentraler RCD je Gruppe. Danach kommt Handarbeit wie bisher, nur an einem Verzeichnis, das am Modell hängt, statt an einer losgelösten Zeichnung: Klemmen je Zeile (1 bis 6, „N entfällt" möglich), Unterzeilen für Abzweige ohne eigene Sicherung, Reserve-Zeilen, Kabel-Vorschläge mit Typbezeichnung (NYM-J 3x2,5 mm², im Außenbereich NYY-J). Feste, deterministische Prüfungen laufen mit: Überlast, RCD-Pflicht, Mindestquerschnitt, mit Bezügen zur DIN 18015. Die Aufteilung selbst bleibt regelbasiert und nachvollziehbar, und die KI ändert nie etwas am Plan.
3. Das Ergebnis ist ein A3-Plansatz im Querformat, Schriftfeld nach DIN EN ISO 7200, Querverweise nach DIN EN 61082-1: eine aufgelöste einpolige Übersicht mit Schutzorgan, Außenleitern, Klemmen und Kabel je Abgang, Revisionstabelle im Schriftfeld. Für den Planversand gibt es ein mehrseitiges Vektor-PDF, für den Schaltschrankbauer DXF je Blatt (Millimeter, Maßstab 1:1, Text bleibt Text), für die Schränke QR-Etiketten (6 je A4). Jeder Code öffnet einen widerrufbaren Lese-Link nur für diesen einen Verteiler, ohne Personennamen und Projektdaten, auf Wunsch mit Codewort geschützt.
4. „Stromkreise übernehmen" stempelt Stromkreisnummern und je Einstellung Verteiler, Funktion, Beschreibung, Sicherung, RCD, Kabel und Phasen in die Revit-Elemente. Fehlende Projektparameter legt das Plugin selbst an, und es gibt einen Rückgängig-Schritt. Bei der nächsten Umplanung läuft derselbe Rundlauf noch einmal, statt dass zwei Stände parallel gepflegt werden: Das Stromkreisverzeichnis im Editor führt, das Modell trägt die aktuellen Ergebnisse.

Abbildung: Ein A3-Verteilerplanblatt der Hauptverteilung: Sammelschienen für L1, L2, L3 und N über die volle Blattbreite, darunter Hauptschalter, Wandlermessung, Überspannungsschutz und fünf Abgänge mit Sicherungen, Klemmenleisten und Kabelangaben, unten die Fußzeilen für Stromkreis, Kabel und Beschreibung und das Schriftfeld mit Revisionstabelle. Blatt 2 aus dem Beispielprojekt der öffentlichen Demo: genau die Zeichnung, die der Editor auch als PDF und als DXF ausgibt.

## Beispielrechnung

Alle Annahmen sind meine eigenen, bewusst konservativen Schätzungen für das beschriebene Modellbüro; Kundenmessungen liegen nicht zugrunde. Setzen Sie Ihre eigenen Werte ein, die Struktur bleibt gleich.

| Position | Wert | Art |
|---|---|---|
| Projekte mit Verteilerplänen im Jahr | 10 | eigene Annahme |
| Unterverteiler je Projekt | 4 (40 im Jahr) | eigene Annahme |
| Neuzeichnen je Verteiler im Zweitwerkzeug | 3,0 h | eigene Annahme |
| Änderungs-Nachpflege je Verteiler über die Projektlaufzeit | 1,5 h | eigene Annahme |
| Verbleibender Aufwand je Verteiler im Rundlauf (Nacharbeit, Prüfung, erneutes Senden) | 1,5 bis 2,5 h | eigene Annahme |

Fallen je Verteiler im Schnitt zwei oder drei Stunden Doppelarbeit weg, ist diese Schwelle nach 23 bis 34 Verteilern erreicht, im Modellbüro also im Laufe des sechsten bis neunten Projekts eines Jahres. Bei kleinerem Pensum rückt der Punkt deutlich nach hinten: Fünf Projekte mit je zwei Unterverteilern kämen nur auf 20 bis 30 gesparte Stunden und blieben unter der Schwelle.

Nicht eingerechnet sind, in beide Richtungen:

- Einarbeitung und der einmalige Umstellungsaufwand, etwa Familien mit elektrischen Kenndaten zu versehen. Beides schiebt den Break-even im ersten Jahr nach hinten.
- Projektspezifische Abweichungen: Verteiler, für die der Auftraggeber eine Allpolig-Darstellung oder Aufbaupläne fordert, bleiben im CAE-Werkzeug und sparen nichts.
- Auf der Habenseite fehlen ebenfalls Posten: vermiedene Übertragungsfehler zwischen Excel, Schema und Modell sowie der Wert der übrigen Pro-Funktionen sind nicht beziffert.

## Was davon übertragbar ist

Ob sich das Szenario auf ein anderes Büro übertragen lässt, hängt an vier Bedingungen.

1. Das Modell muss elektrische Daten tragen: Revit-Familien mit Anschlussleistung, Spannung und Polzahl, zugeordnet zu Räumen und Ebenen. Wie eine solche Bibliothek als Firmenstandard entsteht, beschreibt der Artikel [Revit-Familienbibliothek für die TGA aufbauen](https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html).
2. Das Stromkreisverzeichnis muss die führende Quelle werden. Der Gewinn entsteht erst, wenn Änderungen über den Rundlauf laufen und nicht am Modell vorbei im Zweitwerkzeug. Das ist keine Frage der Technik, sondern der Arbeitsorganisation, und nach meiner Erfahrung der Teil der Umstellung, der Disziplin kostet.
3. Die Grenzen müssen zum Projekt passen. Der erzeugte Plan ist eine aufgelöste einpolige Übersicht nach DIN EN 61082-1, kein vollständiger Installationsplan und keine interne Geräteverdrahtung. Aufbauplan des Schranks, Allpolig-Darstellung und Kabelberechnung (Spannungsfall, Selektivität) liefert der Rundlauf nicht; wo sie gefordert sind, bleibt das bisherige Werkzeug für diese Blätter im Einsatz.

## Häufige Fragen

### Ersetzt der Rundlauf eine CAE-Software vollständig?

Nein. Er erzeugt Stromkreisverzeichnisse und aufgelöste einpolige Übersichten als Planlieferung, dazu Vektor-PDF, DXF und QR-Etiketten. Aufbaupläne, Allpolig-Darstellungen und Kabelberechnungen bleiben Aufgaben für CAE- oder Berechnungswerkzeuge. Wo die einpolige Übersicht als Verteilerdokumentation genügt, kommt das Büro mit dem Rundlauf ohne Zweitwerkzeug aus.

### Was muss das Revit-Modell mitbringen?

Familien mit elektrischen Kenndaten (Anschlussleistung in VA, Spannung, Polzahl) und eine saubere Raum- und Ebenenzuordnung. Elemente, die der Rundlauf nicht erkennt, lassen sich per KI-Vorschlag je Familien/Typ-Paar klassifizieren; die Vorschläge zeigen eine Konfidenz und werden nur nach Ihrer Bestätigung übernommen.

### Was passiert bei einer Umplanung?

Derselbe Rundlauf noch einmal: aus Revit senden, im Plan-Editor nacharbeiten, mit „Stromkreise übernehmen" zurückschreiben. Einen zweiten Planstand, der separat nachgezogen werden müsste, gibt es nicht; das Verzeichnis im Editor führt, das Modell trägt die aktuellen Nummern und Parameter. Für das Zurückschreiben gibt es einen Rückgängig-Schritt.

## Quellen

1. Autodesk Community, Revit MEP Forum: Electrical single line diagram. https://forums.autodesk.com/t5/revit-mep-forum/electrical-single-line-diagram/td-p/8667884 (abgerufen am 25.08.2026)
2. BEEL: Revit Stromlaufplan. https://www.beel.de/revit/revit-stromlaufplan/ (abgerufen am 25.08.2026)
3. eXs: Elektroplanung in BIM-Projekten. https://www.exs-cae.com/elektroplanung-in-bim-projekten/ (abgerufen am 25.08.2026)

Die 192 Büro-Profile stammen aus der eigenen Ansprache-Kartei von BimWired (Stand August 2026): von uns durchgesehene öffentliche Profile und Internetauftritte, mit einem von uns notierten Ansatzpunkt je Büro. Das Material ist unveröffentlicht und nicht öffentlich verlinkbar; die Zuordnungen sind unsere eigenen, nicht repräsentativ und keine Aussagen der genannten Büros.

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/praxisszenario-verteilerplan.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
