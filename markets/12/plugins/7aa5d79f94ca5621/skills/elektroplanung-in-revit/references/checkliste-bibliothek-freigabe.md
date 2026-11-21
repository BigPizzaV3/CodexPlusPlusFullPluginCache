---
titel: "Freigabe-Checkliste: Revit-Familienbibliothek als Firmenstandard ausrollen"
quelle: https://bimwired.com/landing/wissen/checkliste-bibliothek-freigabe.html
stand: 2026-08-25
art: artikel
fragen:
  - "Was prüfe ich, bevor ich eine Revit-Familienbibliothek freigebe?"
  - "Welche Parameter- und Typenkatalog-Regeln gelten für Revit-Familien?"
  - "Wie klassifiziere ich Revit-Familien mit IFC und DIN 276?"
  - "Wie kommt ein freigegebener Bibliotheksstand auf alle Rechner?"
---

# Freigabe-Checkliste: Revit-Familienbibliothek als Firmenstandard ausrollen

Mit dieser Liste prüfe ich eine Revit-Familienbibliothek, bevor ein neuer Stand als Firmenstandard freigegeben und an alle Arbeitsplätze verteilt wird. Sie hat 28 Punkte, von der Benennung bis zur Verteilung. Gehen Sie sie vor jeder Freigabe durch, bei der Erstübernahme genauso wie bei jedem Folgestand.

## Block A: Benennung und Struktur

- [ ] Jede Familie folgt der dokumentierten Namenskonvention: gleiche Bausteine, gleiche Reihenfolge, gleiche Schreibweise.
- [ ] Kein Familienname enthält Leerzeichen oder Sonderzeichen, die Dateisysteme oder Austauschformate stören.
- [ ] Namen beschreiben das Objekt, nie das Herkunftsprojekt.
- [ ] Jede Familie ist genau einem Gewerk und der passenden Revit-Kategorie zugeordnet.
- [ ] Downloads und Hersteller-Familien haben die Aufnahmeprüfung durchlaufen: umbenannt, Parameter angeglichen, klassifiziert.

**Warum:** Was ohne Konvention passiert, beschreibt der Softwarehändler Graitec: zeitraubende Familiensuche, inkompatible Familien aus Altprojekten, fehlerhafte Internet-Downloads. Ein CAD.de-Thread zeigt dasselbe Bild von innen, und der Expertenrat dort deckt sich mit meiner Erfahrung: eigene Familien mit sauberen Unterkategorien statt angepasster Fremd-Downloads.

## Block B: Parameter und Typen

- [ ] Alle gemeinsam genutzten Parameter stammen aus einer einzigen, zentral gepflegten Quelle.
- [ ] Je Parameter sind Datentyp, Einheit und die Bindung als Typ- oder Exemplarparameter festgelegt.
- [ ] Gleiche Größen tragen überall dieselbe Einheit (nicht W neben kW, mm neben m).
- [ ] Elektro-Familien tragen mindestens Spannung, Leistung und Polzahl als Pflichtparameter.
- [ ] Typenkataloge sind komma-getrennte Textdateien mit exakt dem Dateinamen der Familie (Praxisregel für Revit).
- [ ] Typenkatalog-Dateien sind als UTF-8 mit BOM gespeichert, damit Umlaute korrekt ankommen (Praxisregel).
- [ ] Sammelfamilien sind nach Anlagenteil geschnitten; kein Typenkatalog ist länger, als sich vollständig prüfen lässt.

**Warum:** Revit unterscheidet gemeinsame Parameter über eine interne Kennung, nicht über den Namen. Zwei gleichnamige Parameter aus zwei Quellen ergeben in Auswertungen deshalb zwei Spalten. Und ohne elektrische Anschlussdaten bleibt das Modell für die Stromkreisplanung stumm; welche Werte nötig sind, steht in [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html).

## Block C: Klassifizierung

- [ ] Jede Familie trägt ihre IFC-Klasse und den passenden PredefinedType.
- [ ] Ein IFC-Testexport enthält keine unerklärten generischen Stellvertreter-Objekte.
- [ ] Jede Familie trägt ihre Kostengruppe nach DIN 276, bei Elektro meist innerhalb der KG 440.
- [ ] Die zugehörigen Property-Sets (PSets) sind vorhanden und gefüllt.
- [ ] Übernommene Herstellerdaten stammen aus strukturierten Produktdaten (etwa nach VDI 3805), nicht aus Hand-Abschriften.

**Warum:** IFC ist laut BauNetz Wissen seit der Version IFC4 ein ISO-Standard (ISO 16739-1:2024-03), aktuell IFC4.3. Ohne Klassifizierung exportiert das Modell nichtssagende Stellvertreter. Die DIN 276:2018-12 führt die technischen Anlagen als KG 400 und die Starkstromanlagen als KG 440 (Baunormenlexikon; MT-Ingenieure). Die VDI 3805 standardisiert den herstellerneutralen Produktdatenaustausch in der TGA.

## Block D: Qualität und Freigabe

- [ ] Eine Prüfroutine im Werkzeug Ihrer Wahl meldet keine Fehler; verbleibende Warnungen sind gesichtet und begründet.
- [ ] Die Duplikatprüfung ist gelaufen; die Liste ist leer oder jede Dublette entschieden.
- [ ] Zum Stand existiert eine Änderungsliste, die Projektverantwortliche ohne Rückfragen verstehen.
- [ ] Der Stand ist als freigegebener, versionierter Stand erzeugt, nicht als Kopie auf ein Netzlaufwerk.
- [ ] Ein früherer Stand lässt sich nachweislich wiederherstellen.
- [ ] Freigegeben hat eine benannte Person je Gewerk oder Bibliothek.

**Warum:** Ein offenes Netzlaufwerk prüft nichts und versioniert nichts; wer dort eine Datei überschreibt, hat nichts freigegeben, sondern kopiert. Unter einer Freigabe verstehe ich einen geprüften, versionierten Stand mit Änderungsliste.

## Block E: Verteilung

- [ ] Es gibt genau eine verbindliche Quelle für den freigegebenen Stand; Altstände liegen nur lesend im Archiv.
- [ ] Jeder Arbeitsplatz an jedem Standort bezieht den Stand über denselben definierten Weg.
- [ ] Nach dem Ausrollen arbeitet kein Rechner mehr mit einem älteren Stand.
- [ ] Für jedes laufende Projekt ist entschieden und dokumentiert, ob platzierte Familien nachgezogen werden.
- [ ] Eine Kontrolle je Projekt zeigt, welche Familien nicht aus dem Firmenstandard stammen; jede Fremdfamilie ist erklärt.

**Warum:** In unserer eigenen Ansprache-Kartei (192 von uns durchgesehene Büro-Profile, Stand August 2026) haben wir bei 27 Profilen vermerkt, dass Stände über mehrere Standorte auseinanderlaufen. Wie leicht ungeprüfter Fremdinhalt hereinkommt, zeigt Autodesks eigene Linkliste mit über 50 Revit-Content-Quellen; Elektro-Inhalte und deutsche Normelemente sind dort unterrepräsentiert.

## So nutzen Sie die Liste

Kopieren Sie die Liste in Ihr QM und ergänzen Sie büroeigene Regeln (Namensschema, Pflichtparameter) als eigene Punkte. Haken Sie sie vor jeder Freigabe ab, nicht nur bei der Erstübernahme; nach meiner Erfahrung sind die Folgestände die, bei denen es nachlässt. Den Weg zum Firmenstandard beschreibt der Leitfaden [Revit-Familienbibliothek fürs TGA-Büro](https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html); wie drei Standorte zu einem Stand kommen, zeigt das [Praxisszenario zur Familienbibliothek](https://bimwired.com/landing/wissen/praxisszenario-familienbibliothek.html).

## Einordnung: das Werkzeug BimWired

Die Blöcke D und E habe ich lange von Hand organisiert. Releases sind versionierte Stände mit Änderungsliste, Vergleich und Wiederherstellen. Das Revit-Plugin holt den freigegebenen Stand per „Cloud-Update" auf jeden Arbeitsplatz; „Familien aktualisieren" zieht platzierte Familien je Projekt nach, und zwar nur, wenn jemand es bewusst auslöst. Die „Bauteilliste" markiert Fremdfamilien im Projekt, auch geladene ohne Instanz. Für die Blöcke A bis C bleibt Ihr Büro zuständig. Die KI schlägt beim Import Name, Gewerk und IFC-Klasse vor, entscheiden müssen Sie. Typenkataloge trägt der Editor bis 60 Typen je Familie.

## Häufige Fragen (FAQ)

### Warum reicht ein Netzlaufwerk nicht als Familienbibliothek?

Ein Netzlaufwerk kennt nur den aktuellen Zustand: Es prüft nichts, versioniert nichts und hält keine Änderungen fest. Die Folgen beschreibt der Softwarehändler Graitec: zeitraubende Familiensuche, inkompatible Familien aus Altprojekten, fehlerhafte Downloads. Ein Freigabeprozess ersetzt das Laufwerk durch geprüfte, versionierte Stände mit Änderungsliste und Wiederherstellung.

### Welche Klassifizierung braucht eine Revit-Familie für BIM-Projekte?

Mindestens die IFC-Klasse mit passendem PredefinedType und die Kostengruppe nach DIN 276:2018-12, für Starkstromanlagen die KG 440. IFC ist laut BauNetz Wissen seit der Version IFC4 ein ISO-Standard (ISO 16739-1:2024-03); ohne die Zuordnung exportiert das Modell nur generische Stellvertreter-Objekte.

### Müssen platzierte Familien in laufenden Projekten aktualisiert werden?

Nicht automatisch. Platzierte Familien leben als Kopie im Projekt; ein neuer Bibliotheksstand erreicht sie erst, wenn jemand sie dort gezielt neu lädt. Ob ein Projekt mitten in der Ausführung nachzieht, ist eine Projektentscheidung, und die gehört dokumentiert.

## Quellen

1. Graitec: Standardisierte Revit-Familienbibliothek einrichten. https://graitec.com/de/blog/https-graitec-com-de-blog-standardisierte-revit-familienbibliothek-einrichten/ (abgerufen am 25.08.2026)
2. CAD.de-Forum: Familien aus der Standardbibliothek anpassen (Thread). https://ww3.cad.de/foren/ubb/Forum329/HTML/002479.shtml (abgerufen am 25.08.2026)
3. Autodesk BIM Blog: Revit Content, Online-Bibliotheken als Download (Linkliste). https://blogs.autodesk.com/bimblog/revit-content-online-bibliotheken-mit-10-000en-familien-als-download-beitrag-wird-regelmasig-aktualisiert/ (abgerufen am 25.08.2026)
4. BauNetz Wissen: Industry Foundation Classes (IFC). https://www.baunetzwissen.de/integrales-planen/fachwissen/standardisierung/industry-foundation-classes-ifc-5288161 (abgerufen am 25.08.2026)
5. Baunormenlexikon: DIN 276, Ausgabe 2018-12 (Normnachweis). https://www.baunormenlexikon.de/norm/din-276/c2c8d430-8f0d-465c-b1cd-bb12f1febad5 (abgerufen am 25.08.2026)
6. MT-Ingenieure: KG 440, Leistungen der Kostengruppe 440 nach DIN 276. https://www.mt-ing.de/tga-wissen/kg-440-leistungen-der-kostengruppe-440-nach-din-276/ (abgerufen am 25.08.2026)
7. VDI 3805: Elektronischer Produktdatenaustausch in der TGA. https://www.vdi3805.eu/vdi-3805 (abgerufen am 25.08.2026)
8. Eigene Ansprache-Kartei von BimWired: 192 von uns durchgesehene, öffentlich zugängliche Büro-Profile mit einem von uns notierten Ansatzpunkt je Büro (Stand August 2026, unveröffentlicht, nicht repräsentativ).

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/checkliste-bibliothek-freigabe.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
