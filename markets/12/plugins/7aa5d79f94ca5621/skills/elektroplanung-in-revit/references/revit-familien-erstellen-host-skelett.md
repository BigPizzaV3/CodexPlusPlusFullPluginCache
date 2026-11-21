---
titel: "Revit-Familien für die TGA erstellen: Vorlage, Host und Skelett"
quelle: https://bimwired.com/landing/wissen/revit-familien-erstellen-host-skelett.html
stand: 2026-10-11
art: artikel
fragen:
  - "Wie erstelle ich eine Revit-Familie für die TGA?"
  - "Welche Familienvorlage (.rft) ist die richtige?"
  - "Warum lässt sich eine wandbasierte Familie nicht an eine verlinkte Wand setzen?"
  - "Wandbasiert, flächenbasiert oder freistehend: was ist der Unterschied?"
  - "Welche Fehler machen Revit-Familien unbrauchbar?"
  - "Was prüfe ich, bevor eine Familie in die Bibliothek kommt?"
---

# Revit-Familien für die TGA erstellen: Vorlage, Host und Skelett

Eine Revit-Familie für die TGA entsteht aus einer Familienvorlage (.rft), und diese Vorlage legt zwei Dinge fest, die sich später kaum noch ändern lassen: die Kategorie und die Art, wie die Familie im Projekt Halt findet, ihren Host. Für Elektro- und TGA-Büros ist die zweite Entscheidung die folgenreichere, denn sie planen fast immer in einem Modell mit verlinkter Architektur, und an eine verlinkte Wand lässt sich eine wandbasierte Familie nicht setzen. Flächenbasierte Familien können das; freistehende lassen sich zwar überall setzen, verlieren dafür aber die Bindung an die Wand. Dieser Leitfaden erklärt, was eine Familie ausmacht, vergleicht die Host-Arten, nennt die Fehler, die mich beim Aufbau unserer Basisbibliothek am meisten Zeit gekostet haben, und endet mit einer Prüfliste.

## Das Wichtigste in Kürze

- Die Vorlage (.rft) entscheidet Kategorie und Host-Art. Die Kategorie lässt sich nachträglich umstellen, die Host-Art nicht; wer sie falsch wählt, baut die Familie neu.
- Wandbasierte und deckenbasierte Familien brauchen ihren Host im eigenen Modell. An Wänden und Decken eines verlinkten Architekturmodells lassen sie sich nicht platzieren; dafür braucht es flächenbasierte Familien.
- Freistehende Familien lassen sich überall setzen, kennen die Wand aber nicht: Wird sie verschoben, bleibt das Gerät stehen.
- Die Kategorie bestimmt, in welchen Filtern, Bauteillisten und Elektro-Werkzeugen eine Familie überhaupt auftaucht. Ein Schalter in der Kategorie „Allgemeines Modell" ist für die Stromkreisplanung unsichtbar.
- Revit speichert nie in eine ältere Version zurück. Familien werden in der ältesten Revit-Version gebaut, die im Büro läuft.

## Überblick

| Punkt | Detail |
|---|---|
| Vorlage (.rft) | legt Kategorie und Platzierungsart fest; die Kategorie ist später änderbar, die Host-Art nicht |
| Host-Arten | wandbasiert, deckenbasiert, flächenbasiert, freistehend (ebenenbasiert), linienbasiert |
| Kernkonflikt | TGA plant mit verlinkter Architektur; wandbasiert braucht die Wand im eigenen Modell, flächenbasiert nicht |
| Darstellung | 2D-Symbol im Grundriss, 3D-Körper in Schnitt und 3D; Sichtbarkeit je Ansichtsart und Detaillierungsgrad |
| Typen | Typenkatalog als Textdatei neben der .rfa; er füllt Werte in Parameter, die die Familie schon hat |
| Versionen | Revit öffnet ältere Dateien, nie neuere; gebaut wird in der ältesten Version des Büros |
| Zur Einordnung | BimWired (Anbieter dieses Leitfadens): Familie im Browser definieren, das Revit-Plugin baut die .rfa aus der Vorlage und misst sie nach; Wand- und Deckengeräte entstehen flächenbasiert |

## Inhalt

- Was macht eine Revit-Familie aus?
- Welche Host-Art passt zu welchem Bauteil?
- Warum scheitern wandbasierte Familien an verlinkter Architektur?
- Welche Fehler machen eine Familie unbrauchbar, und wie finden Sie sie vorher?
- Prüfliste: zwölf Punkte vor der Freigabe einer Familie
- So macht es BimWired
- Häufige Fragen (FAQ)
- Quellen

## Was macht eine Revit-Familie aus?

Eine ladbare Revit-Familie ist eine .rfa-Datei, die aus einer Familienvorlage entstanden ist und Geometrie, Parameter und Verhalten eines Bauteils beschreibt. Was Familie, Typ und Exemplar unterscheidet, steht im Glossar unter [Revit-Familie](https://bimwired.com/landing/wissen/glossar/revit-familie.html); hier geht es um die Entscheidungen beim Bauen. Fünf Bausteine bestimmen, ob eine Familie im Projekt funktioniert.

**Die Vorlage.** Laut Autodesk-Hilfe sind Familienvorlagen die Bausteine, aus denen Familien entstehen: wandbasierte Vorlagen für Bauteile, „die in Wände eingefügt werden", deckenbasierte für Decken, die flächenbasierte Vorlage für arbeitsebenenbasierte Familien, unabhängige Vorlagen für Bauteile ohne Basisbauteil und linienbasierte Vorlagen für Familien, die mit zwei Klicks platziert werden. Mit der Vorlage stehen Kategorie und Platzierungsart fest. Die Kategorie lässt sich im Familieneditor über „Familienkategorie und -parameter" noch umstellen, die Platzierungsart nicht. Eine Funktion, die aus einer wandbasierten eine flächenbasierte Familie macht, gibt es in Revit nicht; der Schulungsanbieter Imaginit beschreibt nur einen Umweg über ein Hilfsprojekt. Wer die Host-Art falsch gewählt hat, baut neu.

**Referenzebenen und Ursprung.** Referenzebenen sind das Gerüst der Familie: Geometrie wird an sie gesperrt und folgt dann den Parametern, zwei Ebenen definieren den Einfügepunkt. In den Host-Vorlagen liegt dieser Ursprung nicht dort, wo man ihn vermutet. In den wandbasierten Vorlagen liegt er, in Revit 2025 gemessen, in der Mitte der 150 mm dicken Beispielwand; die Wandfläche ist die Ebene „Hinten" 75 mm davor. Nur Geometrie, die an diese Ebene gesperrt ist, folgt im Projekt der echten Fläche einer 200er oder 300er Wand; ungesperrte Geometrie bildet Revit starr ab, und sie steckt dann halb in der Wand. In der Deckenvorlage liegt die Ebene „Decke" je nach Vorlage 2,4 bis 4 m über dem Ursprung; ein 2D-Symbol auf Höhe null hängt im Projekt einen Meter unter dem Boden. Bei der flächenbasierten Vorlage geht die Hostfläche durch den Ursprung.

**Typen und Typenkatalog.** Typparameter tragen Werte je Baugröße (Breite, Leistung, Nennstrom), Exemplarparameter Werte je platziertem Element (Höhe von Ebene, Länge einer linienbasierten Familie). Der [Typenkatalog](https://bimwired.com/landing/wissen/glossar/typenkatalog.html) ist die Textdatei neben der .rfa, aus der Revit beim Laden die Typen anbietet; er füllt nur Werte in Parameter, die die Familie bereits hat, und kennt nur Typparameter.

**2D-Symbol und 3D-Körper.** Im Grundriss erwartet ein deutscher Plan das Schaltzeichen, in Schnitt und 3D den Körper. Beides lebt in derselben Familie und wird über die Sichtbarkeitseinstellungen getrennt: Laut Autodesk-Hilfe legen Sie je Geometrieelement fest, ob es in Grundriss und Deckenspiegel, in Vorder- und Rückansicht, in Seitenansichten und bei welchem Detaillierungsgrad (grob, mittel, fein) erscheint; in 3D-Ansichten erscheint Modellgeometrie immer. Eine Falle liegt bei importierten Zeichnungen: Ein als DWG oder DXF importiertes Symbol ist in einem Familiendokument nicht ansichtsgebunden, in Revit 2025 gemessen, und steht deshalb als flache Linienschar auch in 3D-Ansichten. In der Familie gibt es dagegen keinen Hebel; der sitzt in der 3D-Ansichtsvorlage des Projekts, die die Kategorie „Importe in Familien" ausblendet.

**Die Kategorie.** Sie entscheidet, in welchen Filtern, Bauteillisten und Werkzeugen eine Familie auftaucht und welche Parameter sie tragen kann. Revits Stromkreis-Werkzeuge rechnen mit Leuchten, Elektroinstallationen und Elektrogeräten; ein Schalter als „Allgemeines Modell" bekommt keinen elektrischen Anschluss und erscheint in keinem Stromkreis. Welche Voraussetzungen eine Familie für Stromkreise erfüllen muss, steht in [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html).

## Welche Host-Art passt zu welchem Bauteil?

Die Host-Art beschreibt, woran eine Familie im Projekt hängt: an einer Wand, einer Decke, einer beliebigen Fläche, an einer Ebene oder an einer gezeichneten Linie. Jede Art kann etwas, das die anderen nicht können, und jede scheitert an einer Stelle, die man beim Bauen kennen sollte.

| Host-Art | Vorlage (Beispiel) | Was sie kann | Wo sie scheitert | Typische Bauteile |
|---|---|---|---|---|
| wandbasiert | „Elektroinstallation (Wand).rft" | sitzt in der Wand, folgt ihr, kann eine Öffnung schneiden | Wand muss im eigenen Modell liegen; an verlinkten Wänden keine Platzierung; mit der Wand verschwindet die Familie | Schalter und Steckdosen in Modellen mit eigenen Wänden |
| deckenbasiert | „Leuchte (Decke).rft" | hängt an der Decke, folgt ihr | Decke muss im eigenen Modell liegen | Deckenleuchten und Melder in Modellen mit eigenen Decken |
| flächenbasiert | „Allgemeines Modell Fläche.rft", Kategorie umgestellt | auf jeder Fläche, auch im verlinkten Modell; folgt der Fläche | schneidet keine Öffnung im Link; „oben" und „vorn" müssen im Bau zur Fläche passen | fast alle TGA-Geräte an Wand und Decke |
| freistehend (ebenenbasiert) | „Elektroinstallation.rft", „Mechanische Geräte.rft" | überall setzbar, Höhe von Ebene, kein Host nötig | keine Bindung an die Wand; Wand verschoben, Gerät bleibt | Verteiler, Pumpen, Bodengeräte; mit „Arbeitsebenenbasiert" auch auf Flächen setzbar |
| linienbasiert | „Allgemeines Modell Linie.rft" | zwei Klicks, Exemplarparameter „Länge", Geometrie dehnt sich mit | nur gerade; Bögen als Kette gerader Segmente | Lichtband, Brüstungskanal, Schlitzauslass |

Zwei Dinge aus der Tabelle verdienen einen Satz mehr. Erstens liefert Revit 2025 für Elektroinstallation, Elektrogeräte und Leuchten keine eigene flächenbasierte Vorlage mit; der Weg führt über „Allgemeines Modell Fläche.rft" und das Umstellen der Kategorie. Zweitens wird eine flächenbasierte Familie in einem gedrehten Achsensystem gebaut, denn ihre „Draufsicht" ist die Hostfläche: Was in der Familie oben ist, zeigt an der Wand in den Raum, und die Sichtbarkeitseinstellung „Vorne/Hinten" steuert den Grundriss des Projekts (in Revit 2025 gemessen). Wer das nicht mitdenkt, bekommt ein Symbol, das an der Wand auf der Seite liegt.

## Warum scheitern wandbasierte Familien an verlinkter Architektur?

Eine wandbasierte Familie sucht beim Platzieren eine Wand im eigenen Projekt; eine Wand, die nur über eine Verknüpfung sichtbar ist, erkennt sie nicht als Host, und Revit setzt sie nicht. TGA-Büros bekommen das Architekturmodell praktisch immer als Verknüpfung. Damit sind wandbasierte Familien, wie sie viele Herstellerportale liefern, in genau den Modellen unbrauchbar, in denen Elektroplaner arbeiten. Imaginit formuliert es knapp: „wall-based, ceiling-based, or floor-based families will not attach to a linked Revit model", und in der Autodesk-Community wird dieselbe Frage seit über zehn Jahren mit derselben Antwort beantwortet: flächenbasiert bauen.

Abbildung: Drei Grundriss-Ausschnitte derselben verlinkten Wand mit einem Wandgerät: die wandbasierte Familie findet keinen Host und lässt sich nicht setzen, die flächenbasierte sitzt auf der Wandfläche und folgt ihr, die freistehende lässt sich setzen, bleibt aber stehen, wenn die Wand verschoben wird. Dieselbe Steckdose, dieselbe verlinkte Wand: Nur die Host-Art der Familie entscheidet, ob Revit sie setzt und ob sie der Wand später folgt.

Drei Wege führen aus dem Konflikt, und keiner ist umsonst:

1. Flächenbasiert bauen. Die Familie heftet sich an die Fläche der verlinkten Wand oder Decke und folgt ihr. Für Schalter, Steckdosen, Melder und Leuchten ist das trotzdem der belastbarste Weg, und der Grund, warum ich unsere eigenen Wand- und Deckengeräte so baue.
2. Freistehend bauen und die Höhe über „Höhe von Ebene" setzen. Die Familie lässt sich überall platzieren. Verschiebt der Architekt die Wand um zehn Zentimeter, steht der Schalter in der Luft, und niemand merkt es bis zur Kollisionsprüfung. Für Verteiler, Pumpen und Bodengeräte richtig, für Wandgeräte eine Notlösung.
3. Eine vorhandene wandbasierte Familie umbauen. Imaginit beschreibt den Umweg über ein Hilfsprojekt mit Wand, Verknüpfung und „Kopieren/Überwachen", der eine flächenbasierte Kopie erzeugt. Das geht je Familie einzeln und kostet bei Dutzenden Familien mehr Zeit als ein Neubau aus der richtigen Vorlage.

## Welche Fehler machen eine Familie unbrauchbar, und wie finden Sie sie vorher?

Die meisten Familienfehler zeigen keine Fehlermeldung. Die Familie lädt, lässt sich setzen und ist trotzdem falsch: zu tief, in der falschen Kategorie, mit einem Symbol in 3D oder mit Typen, die nie ankommen. Die Tabelle sammelt die Fehler, die ich selbst gebaut oder in fremden Familien gefunden habe, und den kürzesten Weg, sie vor der Freigabe zu entdecken.

| Fehler | Was im Projekt passiert | So finden Sie ihn vorher |
|---|---|---|
| Ein Maß steht beim Bau auf 0 | Die Extrusion hat keine Flächen, Bindungen fallen still aus; der Körper behält die Vorgabe der Vorlage | Zwei Typen mit verschiedenen Maßen durchschalten („flexen"); der Körper muss allen drei Maßen folgen |
| Falsche Kategorie | Die Familie fehlt in Filtern, Bauteillisten und Elektro-Werkzeugen; kein elektrischer Anschluss | Bauteilliste der Zielkategorie im Prüfprojekt öffnen; fehlt die Familie, stimmt die Kategorie nicht |
| Symbol erscheint in 3D | Importierte DWG/DXF-Symbole sind in der Familie nicht ansichtsgebunden | 3D-Ansicht im Prüfprojekt; Abhilfe in der Ansichtsvorlage („Importe in Familien" aus), nicht in der Familie |
| Lichtquelle der Leuchtenvorlage aktiv | Jede Leuchtenfamilie hat laut Autodesk eine Lichtquelle; bleibt sie an, vergrößert sie die Familie und rechnet in jedem Rendering mit | In „Familienkategorie und -parameter" prüfen, ob „Lichtquelle" bewusst gesetzt ist |
| Familie in zu neuer Revit-Version gespeichert | Ältere Versionen melden „saved in a later version"; Revit speichert nie zurück | Nur in der ältesten Revit-Version des Büros bauen |
| Breite, Länge und Tiefe uneinheitlich benannt | Der Typenkatalog füllt „Länge", der Körper hängt an „Tiefe": alle Typen bleiben gleich tief, ohne Meldung | Einen Typ mit auffällig anderer Bautiefe anlegen und im Schnitt nachsehen |
| Typenkatalog mit Warnfenstern | Ja/Nein als „Ja" statt 1/0, falscher Spaltentyp, Komma im Zahlwert: Revit verwirft Zelle oder Katalog | In ein leeres Projekt laden; jedes Warnfenster ist ein Katalogfehler |
| Referenzebene weit außerhalb des Körpers | Auswahlrahmen und Fangpunkte werden riesig | Im Prüfprojekt anklicken, Auswahlrahmen mit dem Körper vergleichen |
| Fremder Vorlagentyp bleibt stehen | Der Standardtyp der Vorlage landet in Bauteillisten | Typenliste vor dem Speichern durchsehen |

Drei dieser Fehler haben mich selbst getroffen, deshalb hier mit Zahlen, alle in Revit 2025 gemessen. Das Maß null: Beim Skelettbau war „Höhe" im Moment der Bindung noch leer, die Extrusion hatte keine Flächen, und alle 48 Wandfamilien kamen mit der Vorgabe der Vorlage an, 200 mm tief; ein Lichtschalter ragte 20 cm aus der Wand. Die Bautiefe: 225 von 232 Familien unserer Starterbibliothek pflegten sie unter „Länge", der Bau bemaßte aber „Tiefe", und jeder Typ kam mit Länge null und Tiefe 200 an, ohne Meldung. Der Typenkatalog: Ein Spaltentyp „HVAC_AIRFLOW" statt „HVAC_AIR_FLOW" ließ Revit bei 58 Familien den ganzen Katalog verwerfen („Invalid column type"). Keiner dieser Fehler fällt im Familieneditor auf. Alle drei fallen beim Laden in ein leeres Prüfprojekt auf, sobald man zwei Typen durchschaltet und einen Schnitt öffnet.

## Prüfliste: zwölf Punkte vor der Freigabe einer Familie

Die Liste prüft eine einzelne Familie, bevor sie in die Bibliothek kommt. Die Prüfung des ganzen Bibliotheksstands, von der Benennung bis zur Verteilung, steht in der [Checkliste Bibliotheks-Freigabe](https://bimwired.com/landing/wissen/checkliste-bibliothek-freigabe.html).

1. Host-Art passt zum Einsatz: Bei verlinkter Architektur sind Wand- und Deckengeräte flächenbasiert, Bodengeräte freistehend.
2. Die Kategorie ist die fachlich richtige, nicht „Allgemeines Modell", außer bewusst.
3. Der Einfügepunkt liegt dort, wo der Planer klickt: Wandfläche, Deckenunterseite oder Gerätemitte.
4. Zwei Typen wurden durchgeschaltet; der Körper folgt Breite, Tiefe und Höhe, kein Maß steht auf null.
5. Die Bautiefe heißt in Parametern, Typenkatalog und Körperbindung gleich; die Konvention (Breite entlang der Wand, Tiefe in den Raum, Höhe) ist dokumentiert.
6. Im Grundriss erscheint das Schaltzeichen, in 3D der Körper; was davon abweicht, regelt die Ansichtsvorlage.
7. Grob, mittel und fein zeigen, was sie zeigen sollen.
8. Bei Leuchten ist die Lichtquelle bewusst an oder aus.
9. Der Typenkatalog heißt wie die Familie, ist komma-getrennt, UTF-8 mit BOM, Zahlen mit Punkt, Ja/Nein als 1/0; das Laden in ein leeres Projekt läuft ohne Warnfenster.
10. Kein fremder Vorlagentyp ist übrig, keine Referenzebene liegt weit außerhalb des Körpers.
11. Elektro-Familien tragen Spannung, Leistung, Polzahl und den elektrischen Anschluss; jede Familie trägt IFC-Klasse und DIN-276-Kostengruppe.
12. Die Datei ist in der ältesten Revit-Version des Büros gespeichert und im Prüfprojekt in Grundriss, Deckenspiegel und 3D angesehen. Erst dann Freigabe.

## Einordnung: das Werkzeug BimWired

BimWired ist mein eigenes Werkzeug, deshalb nüchtern, was es an dieser Stelle tut. Eine Familie wird im Browser definiert: Montage (freistehend, Wand, Decke), Kategorie, Klassifizierung, Parameter, der Typenkatalog mit bis zu 60 Typen, das 2D-Symbol und die 3D-Körperform, wahlweise automatisch abgeleitet, als Archetyp wie Schalter, Steckdose, Melder oder Pumpe, oder als eigene Form mit Maßen, die an Parameter gebunden sind. Niemand modelliert in Revit. Der Revit-Befehl „Skelette bauen" erzeugt daraus die .rfa, aus der Familienvorlage der Firma oder der Revit-Installation, und Wand- und Deckengeräte entstehen dabei als flächenbasierte Familien, damit sie sich auch an verlinkte Architektur setzen lassen; im Plugin wählt ein Klick auf die Kachel die passende Platzierung vor.

Nach jedem Bau misst das Plugin die fertige Familie nach und meldet in einem Prüfbericht, wenn der Körper eines Typs nicht seinen Maßen folgt oder flach ist, ein Typ fehlt oder ein fremder Vorlagentyp daneben steht, die Lichtquelle einer Leuchtenvorlage eingeschaltet ist, eine Referenzebene weit außerhalb des Körpers liegt oder Körperteile im Grundriss erscheinen, obwohl die Familie ein Symbol hat. „Probeladen" lädt alle gebauten Familien in ein Prüfprojekt, bevor ein Release entsteht. Gebaut wird in Revit 2025, damit 2025, 2026 und 2027 dieselben Dateien laden; enthält ein Release trotzdem Familien aus einer neueren Version, nennt der Editor sie, und das Plugin warnt vor dem Platzieren. Das Release verteilt der Befehl „Cloud-Update" an alle Arbeitsplätze.

## Häufige Fragen (FAQ)

### Warum lässt sich meine wandbasierte Familie nicht an die Wand setzen?

Weil die Wand vermutlich in einem verlinkten Architekturmodell liegt. Eine wandbasierte Familie erkennt nur Wände im eigenen Projekt als Host; an Wänden einer Verknüpfung setzt Revit sie nicht. Flächenbasierte Familien heften sich dagegen an jede Fläche, auch an die einer verlinkten Wand; freistehende Familien lassen sich setzen, folgen der Wand aber nicht.

### Kann ich eine wandbasierte Familie nachträglich flächenbasiert machen?

Nicht mit Bordmitteln. Die Platzierungsart kommt aus der Vorlage und lässt sich im Familieneditor nicht umstellen. Es gibt einen Umweg über ein Hilfsprojekt, in dem die Familie an einer Wand platziert, als Verknüpfung geladen und per „Kopieren/Überwachen" kopiert wird; das Ergebnis ist flächenbasiert. Für eine ganze Bibliothek ist ein Neubau aus der flächenbasierten Vorlage meist schneller und sauberer.

### Welche Vorlage nehme ich für Schalter und Steckdosen?

In einem Modell mit eigenen Wänden die Vorlage „Elektroinstallation (Wand)". In einem Modell mit verlinkter Architektur, also im Normalfall der TGA, eine flächenbasierte Familie. Da Revit 2025 für Elektroinstallation keine eigene flächenbasierte Vorlage mitliefert, nehmen Sie „Allgemeines Modell Fläche" und stellen die Kategorie über „Familienkategorie und -parameter" auf Elektroinstallation um.

### Warum sehe ich das 2D-Symbol meiner Familie in der 3D-Ansicht?

Weil es als DWG oder DXF importiert wurde. Importierte Zeichnungen sind in einem Familiendokument nicht an eine Ansicht gebunden und erscheinen deshalb als flache Linienschar auch in 3D (in Revit 2025 gemessen). In der Familie gibt es dafür keinen Schalter; blenden Sie in der 3D-Ansichtsvorlage des Projekts die Kategorie „Importe in Familien" aus.

### Warum öffnet Revit 2025 eine Familie nicht, die ein Kollege gebaut hat?

Weil sie in Revit 2026 oder 2027 gespeichert wurde. Revit öffnet und aktualisiert ältere Dateien, kann aber nicht in eine ältere Version zurückspeichern; die Meldung lautet „saved in a later version". Bauen und speichern Sie Familien deshalb in der ältesten Revit-Version, die im Büro im Einsatz ist.

### Warum fehlt meine Familie in der Bauteilliste und in den Stromkreis-Werkzeugen?

Fast immer wegen der Kategorie. Bauteillisten, Filter und Revits Elektro-Werkzeuge arbeiten je Kategorie; eine Steckdose, die als „Allgemeines Modell" gebaut wurde, taucht in keiner Elektro-Bauteilliste auf und bekommt keinen elektrischen Anschluss. Die Kategorie lässt sich im Familieneditor umstellen, danach muss die Familie neu ins Projekt geladen werden.

## Quellen

1. Autodesk Hilfe Revit 2025: Familienvorlagen. https://help.autodesk.com/cloudhelp/2025/DEU/Revit-Customize/files/GUID-E36987A9-A68F-4121-A391-907306BAA60A.htm (abgerufen am 11.10.2026)
2. Autodesk Hilfe Revit 2025: Familiensichtbarkeit und Detaillierungsgrad. https://help.autodesk.com/cloudhelp/2025/DEU/Revit-Customize/files/GUID-B28F98C2-D3DA-486E-B198-96B8C862F28B.htm (abgerufen am 11.10.2026)
3. Autodesk Hilfe Revit 2025: Lichtquellen für Beleuchtungsfamilien. https://help.autodesk.com/cloudhelp/2025/DEU/Revit-Customize/files/GUID-52EF01D6-F429-4596-8F13-5FAB97DA1A10.htm (abgerufen am 11.10.2026)
4. Autodesk Hilfe Revit 2026 (Fehlerbehebung): Revit file cannot be opened in Revit because of Version issues. https://help.autodesk.com/cloudhelp/2026/ENU/RevitLT-Troubleshoot/files/GUID-196D6144-42AC-46E8-B8A5-E76A5DF256B5.htm (abgerufen am 11.10.2026)
5. Autodesk Support: Backward compatibility of Revit with earlier releases of the software. https://www.autodesk.com/support/technical/article/Backwards-compatibility-of-Revit-with-earlier-releases-of-the-software (abgerufen am 11.10.2026)
6. IMAGINiT Technologies: Revit tips and tricks, Convert wall-based families to face-based families (03.10.2025). https://resources.imaginit.com/support-blog/convert-wall-based-revit-families-to-face-based-families (abgerufen am 11.10.2026)
7. Autodesk Community: Wall Hosted Element in Linked File (Forum-Thread). https://forums.autodesk.com/t5/revit-architecture-forum/wall-hosted-element-in-linked-file/td-p/3720236 (abgerufen am 11.10.2026)
8. Eigene Messungen beim Aufbau der BimWired-Basisbibliothek in Revit 2025 (August bis Oktober 2026), im Text als „in Revit 2025 gemessen" gekennzeichnet (unveröffentlicht).

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/revit-familien-erstellen-host-skelett.html, Stand 11. Oktober 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
