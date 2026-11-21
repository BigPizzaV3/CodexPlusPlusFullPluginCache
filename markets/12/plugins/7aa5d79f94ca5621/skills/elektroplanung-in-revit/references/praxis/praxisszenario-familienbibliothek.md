---
titel: "Praxisszenario: drei Standorte, ein Familienstand, ein TGA-Büro räumt seine Revit-Bibliothek auf"
quelle: https://bimwired.com/landing/wissen/praxisszenario-familienbibliothek.html
stand: 2026-08-25
art: szenario
fragen:
  - "Wie konsolidiert ein TGA-Büro Revit-Familien von mehreren Standorten?"
  - "Was kostet eine zentrale Revit-Familienbibliothek je Jahr?"
  - "Wie kommen Bibliotheks-Updates auf alle Revit-Arbeitsplätze?"
  - "Wie werden Duplikate in einer Revit-Familienbibliothek gefunden?"
  - "Lohnt sich eine zentrale Familienbibliothek für ein Büro mit 25 Mitarbeitenden?"
---

# Praxisszenario: drei Standorte, ein Familienstand, ein TGA-Büro räumt seine Revit-Bibliothek auf

*Ein modellhaftes Szenario aus typischen Arbeitsabläufen deutscher Planungsbüros, kein Kundenbericht. Die Zahlen sind als Beispielrechnung gekennzeichnet.*

In diesem Szenario führt ein TGA-Generalplaner mit 25 Mitarbeitenden an drei Standorten seine gewachsenen Familienablagen zu einer zentralen Revit-Bibliothek zusammen: Bestand per RFA-Sammelimport erfassen, Duplikate aussortieren, Parameter und Typen vereinheitlichen, den bereinigten Stand als Release freigeben und per Cloud-Update an alle Arbeitsplätze verteilen. Unter konservativen Annahmen liegt der Break-even zwischen dem 14. und dem 21. Monat; fällt die Zeitersparnis nur halb so hoch aus, trägt sich das Vorhaben über eingesparte Suchzeit allein nicht.

## Das Wichtigste in Kürze

- Drei Standorte, drei Familienstände: dieselbe Familie liegt in mehreren Varianten mit abweichenden Parametern vor, und niemand weiß, welche gilt. Das Muster ist branchentypisch und belegt.
- Der Weg hat fünf Stationen: RFA-Sammelimport mit Duplikat-Erkennung, Standard festziehen (Namen, Parameter, IFC, DIN 276), Herstellerdaten aus BMEcat oder CSV importieren, Release freigeben, Cloud-Update an jedem Arbeitsplatz.
- Danach gibt es genau einen verbindlichen Stand: das freigegebene Release. Laufende Projekte ändern sich nie von allein; „Familien aktualisieren" wird je Projekt bewusst angestoßen.
- Mit Konsolidierung und laufender Pflege liegt der Break-even im Modell zwischen Monat 14 und 21.

## Ausgangslage: drei Standorte, drei Wahrheiten

Das Büro in diesem Szenario plant alle sechs TGA-Gewerke, beschäftigt 25 Personen an drei Standorten und hat keinen eigenen BIM-Manager. Jeder Standort hat auf seinem Netzlaufwerk einen Ordner „Familien", gewachsen aus Jahren Projektarbeit; daneben liegen in den Projektordnern lokal angepasste Kopien. Die Symptome kenne ich aus eigenen Projekten: dieselbe Steckdosen-Familie mit drei verschiedenen Parameternamen für die Leistung, Ventilatoren mit veralteten Typwerten, Symbole, die nicht zur deutschen Planlegende passen. Wer eine Familie braucht, fragt herum oder kopiert sie aus dem letzten Projekt. So wächst der Wildwuchs weiter.

In unserer eigenen, nicht repräsentativen Ansprache-Kartei von 192 öffentlich zugänglichen Profilen deutscher, österreichischer und Schweizer Elektro- und TGA-Planungsbüros (Stand August 2026) haben wir bei 89 Profilen Familien, Bibliothek oder Firmenstandards als Ansatzpunkt vermerkt, bei 27 davon zusätzlich mehrere Standorte mit auseinanderlaufenden Ständen. Der Vermerk stammt von uns, nicht von den Büros. Von außen sieht es ähnlich aus: Graitec nennt die Familiensuche in ungeordneten Ablagen „zeitraubend und kontraproduktiv", typische Begleiter sind inkompatible Altprojekt-Familien und fehlende Abstimmung im Team [1]. Im CAD.de-Forum scheitert schon das Anpassen einer einzelnen Familie aus der Standardbibliothek an Kategorien und Projekteinstellungen; erfahrene Nutzer raten dort, eigene Familien mit sauberer Struktur aufzubauen [2]. Mit Downloads löst man das nicht: Autodesks eigene Übersicht listet über 50 Content-Quellen für Revit-Familien, Elektro und deutsche Normelemente sind darin unterrepräsentiert [3]. Und dass kuratierte TGA-Kataloge mit einheitlicher Bezeichnungslogik als eigenes Produkt verkauft werden, zeigt den Bedarf von der anderen Seite [4].

Auslöser ist im Szenario ein Projekt, das zwei Standorte gemeinsam bearbeiten: gleiche Bauteile, unterschiedliche Familien, Auswertungen, die nicht zusammenpassen. Die Geschäftsführung beschließt, den Bestand einmal zu konsolidieren und danach zentral zu pflegen. Eine erfahrene Fachplanerin übernimmt die Pflege mit festem Wochenbudget. Wie ein solcher Standard aussieht (Benennung, Parameter, IFC, Verteilung), steht im Artikel zur [Revit-Familienbibliothek im TGA-Büro](https://bimwired.com/landing/wissen/revit-familienbibliothek-tga.html); hier geht es um den Weg dorthin aus einem gewachsenen Bestand.

## Der Weg: von rund 900 Dateien zu einem Release

Ausgangsmaterial sind rund 900 .rfa-Dateien über drei Standorte, nach erster Sichtung gut zur Hälfte Duplikate und Altlasten. Alle Schritte unten sind heutige Funktionen von BimWired; die Mengen sind Annahmen des Szenarios.

1. **Bestand einsammeln.** Die Netzlaufwerk-Ordner wandern standortweise per RFA-Sammelimport in den Editor, bis zu 200 Dateien oder 500 MB je Durchgang, hier also mindestens fünf Durchgänge. Mögliche Duplikate werden schon beim Import erkannt und sind vorab abgewählt. Die KI schlägt je Familie Name, Gewerk, Kategorie und IFC-Klasse vor; die Pflege-Rolle prüft, übernimmt oder ändert das. An der Geometrie hochgeladener Familien ändert der Editor nichts.
2. **Standard festziehen.** Aus dem Bestand wird ein Standard: eine Namenskonvention, konsolidierte Parameter (Datentyp, Typ oder Exemplar, Gruppe, Einheit, Pflichtfelder) und je Familie IFC-Klasse samt PredefinedType und DIN-276-Zuordnung. Typenkataloge bündeln Varianten, bis zu 60 Typen je Familie; große Herstellerreihen werden auf eine kuratierte Auswahl reduziert. Die Validierung liefert die Befundliste: Fehler blockieren später das Release, die Liste „Mögliche Duplikate" muss leer werden. Sammel-Reparaturen laufen nur deterministisch, KI-Vorschläge werden einzeln mit Vorher/Nachher bestätigt. Saubere Elektro-Parameter zahlen sich hier doppelt aus: Wer später [Stromkreise in Revit plant](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html), braucht Anschlusswerte wie VA, Spannung und Polzahl an den Familien.
3. **Herstellerdaten importieren.** Typreihen mit echten Gerätedaten entstehen aus BMEcat-XML mit ETIM oder aus CSV/TSV. Ich habe solche Typreihen lange genug abgetippt, um diesen Schritt zu schätzen. Deutsche Zahlen und Einheiten rechnet der Import korrekt um (etwa kW in W, m in mm), und eine Typ-Vorschau zeigt vor dem Schreiben, was entsteht. Grenzen je Durchgang: 20 Dateien, 64 MB, 5.000 Artikel.
4. **Erstes Release freigeben.** Der bereinigte Stand geht als erstes Release mit Änderungsliste raus; ab jetzt ist das Release verbindlich, der Netzlaufwerk-Ordner hat ausgedient. Stände lassen sich vergleichen, wiederherstellen und als ZIP herunterladen.
5. **Per Cloud-Update verteilen.** An jedem Arbeitsplatz holt das Revit-Plugin (Revit 2025, 2026 und 2027) das freigegebene Release per „Cloud-Update". In laufenden Projekten zieht der Befehl „Familien aktualisieren" bereits platzierte Familien nach, immer bewusst angestoßen. Die „Bauteilliste" zeigt je Projekt, welche Familien aus der Bibliothek stammen und welche fremd sind, auf Wunsch auch geladene Familien ohne Instanz; so wird der restliche Wildwuchs sichtbar.
6. Änderungen erreichen Arbeitsplätze und Projekte nur auf Bestätigung.

Abbildung: Acht Kacheln einer Familienbibliothek nebeneinander, jede mit laufender Nummer, Bezeichnung, Klassifizierung, einer Symbolvorschau sowie der Montageart, der Anzahl Parameter und den hinterlegten Typen mit ihren Kürzeln. Ausschnitt aus der öffentlichen Demo: dieselben Angaben stehen an jeder Familie, und genau diese Gleichförmigkeit ist das Ziel der Umstellung.

## Beispielrechnung: offene Annahmen, konservativ gerechnet

Eine Beispielrechnung mit eigenen Annahmen, die ich bewusst konservativ gesetzt habe; Kundendaten liegen keine zugrunde. Extern belegt ist nur qualitativ, dass ungeordnete Familienablagen Zeit kosten [1]. Rechnen Sie mit Ihren eigenen Werten nach.

| Position | Ansatz | Einordnung |
|---|---|---|
| Revit-Arbeitsplätze | 12 von 25 Mitarbeitenden | eigene Annahme |
| Heutiger Aufwand für Suchen, Prüfen, Reparieren von Familien | 2 Stunden je Woche und Arbeitsplatz | eigene Annahme, extern nur qualitativ gestützt [1] |
| Angesetzte Ersparnis nach der Konsolidierung | 1 Stunde je Woche und Arbeitsplatz (Halbierung, nicht null) | eigene Annahme |
| Arbeitswochen je Jahr | 42 | Urlaub, Krankheit, Feiertage abgezogen |

Der Break-even liegt in diesem Modell zwischen dem 14. und dem 21.

Nicht eingerechnet sind Schulung und Einarbeitung des Teams, Mehraufwand bei schlechter Datenqualität des Bestands, projektspezifische Sonderfamilien außerhalb des Standards und die schwer bezifferbaren Qualitätseffekte: konsistente Bauteillisten, sauberere IFC-Abgaben, weniger Nacharbeit in Auswertungen. Diese Rechnung ist ein Modell, kein Erfahrungswert.

## Was davon übertragbar ist

So würde ich ein solches Büro umstellen: erst einsammeln und entscheiden, dann vereinheitlichen, dann freigeben und verteilen. Die Mechanik ist übertragbar, die Zahlen sind es nicht. Drei Bedingungen halte ich für unverzichtbar:

- Jemand übernimmt die Pflege-Rolle, mit fester Kapazität. Ohne benannte Verantwortung wächst der Wildwuchs auch mit Werkzeug weiter; im Szenario sind 2 Stunden je Woche angesetzt.
- Der Bestand liegt als .rfa vor. Familien, die nur in Projektdateien stecken, müssen vorher aus Revit herausgespeichert werden.
- Konsolidieren ist Arbeit, kein Knopfdruck. Import und Duplikat-Erkennung nehmen Routine ab, die KI macht Vorschläge; welche Variante gilt und welche Parameter bleiben, entscheidet ein Mensch, und er gibt am Release frei.

Dazu die Grenzen des Werkzeugs. BimWired ist ein Cloud-Dienst: Die Bibliothek wird im Browser gepflegt, die Arbeitsplätze laden freigegebene Stände über das Revit-Plugin herunter und brauchen dafür eine Internetverbindung. Je Firma stehen 5 GB Speicher zur Verfügung. Ein Typenkatalog fasst bis zu 60 Typen je Familie, sehr große Herstellerkataloge werden deshalb kuratiert oder aufgeteilt. Das Plugin unterstützt Revit 2025, 2026 und 2027. Der Datenfluss ist bewusst eine Einbahnstraße vom Release ins Projekt, mit definierten Rückkanälen wie dem Familien-Upload; eine Live-Synchronisation zwischen Editor und Revit gibt es nicht.

## Häufige Fragen

### Wie lange dauert es, eine gewachsene Revit-Familienbibliothek zu konsolidieren?

Das hängt von Menge und Datenqualität ab. In diesem Szenario sind für rund 900 Dateien, von denen nach Duplikaten und Altlasten etwa 350 Familien im Standard verbleiben, 8 bis 12 Personentage über das erste Quartal angesetzt; das ist eine Annahme, kein Erfahrungswert. Der technische Import ist der kleinste Teil. Die Zeit geht ins Entscheiden, welche Variante gilt und welche Parameter bleiben.

### Was passiert mit laufenden Projekten, wenn sich die Bibliothek ändert?

Zunächst nichts. Änderungen werden als neues Release freigegeben, jeder Arbeitsplatz holt sie bewusst per „Cloud-Update", und bereits platzierte Familien werden erst durch den Befehl „Familien aktualisieren" nachgezogen. Automatische Änderungen an laufenden Projekten gibt es nicht.

### Funktioniert das ohne eigenen BIM-Manager?

Ja, das Szenario rechnet bewusst ohne eigene BIM-Manager-Stelle: Eine Person aus dem Planungsteam übernimmt die Pflege mit einem festen Wochenbudget. Auf den Titel kommt es aus meiner Sicht nicht an, wohl aber darauf, dass die Rolle benannt ist und Kapazität hat. Das Werkzeug nimmt Routinearbeit ab, etwa Duplikat-Erkennung, Validierung und Verteilung; die Verantwortung bleibt bei dieser Person.

## Quellen

1. Graitec Blog: „Standardisierte Revit-Familienbibliothek einrichten". https://graitec.com/de/blog/https-graitec-com-de-blog-standardisierte-revit-familienbibliothek-einrichten/ (abgerufen am 25.08.2026)
2. CAD.de Forum: Diskussion zum Anpassen von Revit-Familien aus der Standardbibliothek (Dezember 2019). https://ww3.cad.de/foren/ubb/Forum329/HTML/002479.shtml (abgerufen am 25.08.2026)
3. Autodesk BIM Blog: „Revit Content: Online-Bibliotheken mit 10.000en Familien als Download". https://blogs.autodesk.com/bimblog/revit-content-online-bibliotheken-mit-10-000en-familien-als-download-beitrag-wird-regelmasig-aktualisiert/ (abgerufen am 25.08.2026)
4. BIMpedia (Plandata): „Familienkatalog TGA". https://www.bimpedia.eu/artikel/1852-familienkatalog-tga (abgerufen am 25.08.2026)

Die im Text genannte Ansprache-Kartei von 192 Büro-Profilen ist internes, unveröffentlichtes Material von BimWired: von uns durchgesehene öffentliche Profile mit einem von uns notierten Ansatzpunkt je Büro, nicht repräsentativ und nicht öffentlich einsehbar.

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/praxisszenario-familienbibliothek.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
