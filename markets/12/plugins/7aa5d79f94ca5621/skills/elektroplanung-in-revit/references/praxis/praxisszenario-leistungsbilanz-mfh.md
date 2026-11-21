---
titel: "Praxisszenario: Hausanschluss fürs Mehrfamilienhaus mit Wärmepumpe und Wallboxen, ohne Excel-Bilanz"
quelle: https://bimwired.com/landing/wissen/praxisszenario-leistungsbilanz-mfh.html
stand: 2026-08-25
art: szenario
fragen:
  - "Wie berechne ich die Anschlussleistung für ein Mehrfamilienhaus mit Wärmepumpe und Wallboxen?"
  - "Reicht der Hausanschluss für Wallboxen und Wärmepumpe?"
  - "Welche Rolle spielt der Gleichzeitigkeitsfaktor nach DIN 18015-1?"
  - "Senkt Photovoltaik die benötigte Anschlussleistung?"
  - "Welche Software erstellt eine Leistungsbilanz nach DIN 18015-1 ohne Excel?"
---

# Praxisszenario: Hausanschluss fürs Mehrfamilienhaus mit Wärmepumpe und Wallboxen, ohne Excel-Bilanz

*Ein modellhaftes Szenario aus typischen Arbeitsabläufen deutscher Planungsbüros, kein Kundenbericht. Die Zahlen sind als Beispielrechnung gekennzeichnet.*

Ein kleines Planungsbüro bekommt den Neubau eines Mehrfamilienhauses auf den Tisch: zwölf Wohneinheiten, zentrale Wärmepumpe, Aufzug, sechs Ladepunkte, Photovoltaik. Wie kommt es zu einer Anschlussleistung, die vor dem Netzbetreiber Bestand hat? Nach DIN 18015-1:2020-05 liefern die Bedarfskurven aus Anhang A die gleichzeitige Grundlast der Wohnungen. Alle Lasten, die davon abweichen, werden separat angesetzt, und die Photovoltaik senkt den Bezug nicht, weil der Bemessungsfall die Winter-Abendspitze ist. In diesem Szenario entsteht die Bilanz nicht in einer handgepflegten Excel-Vorlage, sondern in der Leistungsbilanz von BimWired: eine Eingabemaske mit Live-Ergebnis (S_max, Bemessungsstrom, empfohlene NH-Sicherung samt Rechenweg) und ein PDF-Bericht für die Abstimmung mit dem Netzbetreiber. Ein Revit-Modell braucht es dafür nicht.

## Das Wichtigste in Kürze

- Die Bedarfskurven aus Anhang A der DIN 18015-1 liefern die gleichzeitige Grundlast der zwölf Wohneinheiten. Was vom haushaltsüblichen Bezug abweicht (Wärmepumpe, Ladepunkte, Aufzug, Photovoltaik), wird separat angesetzt.
- Die häufigste Falle ist die Doppelrechnung: Haushaltsgeräte stecken schon in den Bedarfskurven und dürfen nicht noch einmal als Sonderlast auftauchen.
- Photovoltaik senkt die berechnete Anschlussleistung nicht (Bemessungsfall Winter-Abendspitze). Erfasst wird sie trotzdem, mit Scheinleistung und Einspeiserichtung.
- Die Beispielrechnung unten kommt konservativ auf rund 7 gesparte Stunden je Projekt.

## Ausgangslage: die Bilanz lebt in einer geerbten Excel-Datei

Das Szenario: Ein Planungsbüro mit drei Personen und Schwerpunkt Wohnungsbau übernimmt die Elektroplanung für ein neues Mehrfamilienhaus. Zwölf Wohneinheiten, eine zentrale Wärmepumpe mit Heizstab, ein Aufzug, sechs Ladepunkte in der Tiefgarage, Photovoltaik auf dem Dach. Der Netzbetreiber will früh wissen, welche Anschlussleistung das Gebäude braucht.

Die Bilanz dafür lebt bisher in einer Excel-Vorlage, die ein früherer Kollege einmal aufgesetzt hat. Sie funktioniert, solange das Projekt aussieht wie das Projekt, für das sie gebaut wurde. Bei jedem neuen Planstand zieht das Büro Zellen von Hand nach, und an drei Stellen bleibt es regelmäßig unsicher: Welcher Gleichzeitigkeitsansatz ist für zwölf Einheiten realistisch? Wie gehen Wärmepumpe, Aufzug und Ladepunkte in die Rechnung ein, ohne dass etwas doppelt zählt? Und was macht die Photovoltaik mit dem Ergebnis?

Dieses Muster kenne ich aus eigenen Projekten, und es ist kein Einzelfall. In einer Forendiskussion auf elektrikforum.de (Juni 2023) zur Dimensionierung eines Mehrfamilienhaus-Anschlusses zweifelt der Fragesteller an einem Gleichzeitigkeitsfaktor von 0,4 auf 78 kW und fragt, ob die Werte der DIN 18015 bindend sind, wie Wärmepumpe und Aufzug einzurechnen sind und ob 63 A künftige Wallboxen tragen. Die Initiative ELEKTRO+ erklärt die Auslegung über das Wohneinheiten-Diagramm in Anhang A der DIN 18015-1 (Gleichzeitigkeitsfaktor zwischen 0 und 1) und betont, dass alle vom haushaltsüblichen Bezug abweichenden Lasten wie Wärmepumpe, Ladeeinrichtung und Photovoltaik separat zu bewerten sind. Die Grundlagen stehen also öffentlich erklärt da. Was fehlt, ist der Weg vom konkreten Projekt zur fortgeschriebenen Bilanz. Die Normseite habe ich im Artikel [Leistungsbilanz nach DIN 18015-1](https://bimwired.com/landing/wissen/leistungsbilanz-din-18015-1.html) ausführlicher beschrieben.

Dazu kommt, dass solche Projekte inzwischen der Normalfall sind. Seit dem 1. Januar 2024 gilt laut Bundesnetzagentur der § 14a EnWG für neue steuerbare Verbrauchseinrichtungen über 4,2 kW wie Wärmepumpen und private Wallboxen; der Netzbetreiber darf sie im Engpassfall temporär auf 4,2 kW dimmen, den Anschluss aber nicht mehr wegen möglicher Netzüberlastung verweigern. Wärmepumpe und Ladepunkte gehören damit in fast jede neue Bilanz. Und die entsteht vielerorts weiter in Tabellen: In unserer eigenen Ansprache-Kartei von 192 öffentlich zugänglichen Profilen von Elektro- und TGA-Planungsbüros aus Deutschland, Österreich und der Schweiz (Stand August 2026) haben wir bei 32 Profilen Excel- und Listenhandarbeit neben dem Planungswerkzeug vermerkt.

## Der Weg: vom Projektstart zum unterschriftsreifen Bericht

So würde ich das Szenario durchspielen:

1. **Projekt anlegen, Rahmen setzen.** Das Büro legt das Projekt im Editor an und öffnet die Kachel „Leistungsbilanz". Gebäudetyp Mehrfamilienhaus, Netzbetreiber auswählen: Der Editor bringt Referenzwerte nach VDE-AR-N 4100 und TAB 2023 mit, verbindlich bleibt die örtliche TAB. Dazu eine Reserve für das, was später noch dazukommt.
2. **Wohneinheiten erfassen.** Die zwölf Einheiten kommen als Typen mit Zimmerzahl, Fläche und Anzahl in die Maske. Warmwasser läuft im Szenario zentral über die Wärmepumpe, also gilt Kurve B (ohne elektrische Warmwasserbereitung). Zwei Einheiten haben zusätzlich einen Durchlauferhitzer im Duschbad. Diesen Mischfall rechnet der Editor als Kurve B plus Kurvendifferenz für die betroffenen Wohnungen, sodass niemand das Diagramm von Hand ablesen muss.
3. **Sonderlasten ansetzen.** Die Wärmepumpe wird mit Heizstab erfasst, samt der Angabe, ob beide gleichzeitig laufen dürfen oder verriegelt sind; diese Betriebsart entscheidet mit über die Spitze. Dazu kommen Aufzug, Allgemeinstrom, die sechs Ladepunkte als Ladeeinrichtungen und bei Bedarf freie Sonderlasten für alles, was das Projekt sonst noch mitbringt. Die Photovoltaik wird mit der Scheinleistung des Wechselrichters und ihrer Einspeiserichtung eingetragen; den berechneten Bezug senkt sie nicht.
4. **Ergebnis live prüfen.** Neben der Eingabe stehen jederzeit Bilanztabelle, Bedarfskurve, S_max, Bemessungsstrom und die empfohlene NH-Sicherung, dazu Prüfhinweise und der vollständige Rechenweg. Jeder Posten ist mit seinem Ansatz sichtbar, statt in einer Zellformel zu verschwinden. Ändert sich der Planstand (zwei Ladepunkte mehr, eine größere Wärmepumpe), ändert das Büro die Werte und lässt die Formeln in Ruhe.
5. **Bericht herausgeben.** Für die Abstimmung mit dem Netzbetreiber erzeugt der Editor ein mehrseitiges Vektor-PDF im A4-Format mit Firmenkopf und Unterschriftenzeilen; CSV und JSON gehen zur Ablage in den Projektordner.
6. **Weiterarbeiten Richtung Verteiler.** Was die Bilanz bemessen hat, wird später in Stromkreise aufgeteilt und als Verteilerplan geliefert. Wie eine solche Zeichnung normseitig aussieht, steht im Artikel [Verteilerplan und Stromlaufplan normgerecht erstellen](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html).

## Beispielrechnung

### Welche Posten die Spitze treiben

Ich nenne hier bewusst keine Kilowatt-Endwerte. Jede belastbare Zahl hängt an der örtlichen TAB, der Betriebsart der Wärmepumpe und dem Ladekonzept, und eine ausgedachte Zahl sähe aus wie eine Norm-Nachrechnung, wäre aber keine. Belastbar sind die Mechanismen dahinter.

Die Wohnungen zählen nicht mit ihrer Summe. Zwölf Einheiten gehen über die Bedarfskurve ein, nicht über die Addition ihrer Einzellasten. Im Editor steckt diese Kurvenlogik hinter den Kurven A und B samt Mischfall.

Die Spitze treiben die Sonderlasten. Im Szenario sind das vor allem die Wärmepumpe (darf der Heizstab gleichzeitig laufen oder ist er verriegelt?) und die sechs Ladepunkte (welche Leistung wird je Ladepunkt angesetzt?). Aufzug und Allgemeinstrom sind daneben klein, gehören aber vollständig hinein.

Dann die Doppelrechnung, die Falle, die ich am häufigsten gesehen habe. Herd, Backofen und Waschmaschine stecken bereits in den Bedarfskurven. Wer sie zusätzlich als Sonderlast einträgt, rechnet doppelt und bemisst zu groß. In einer gewachsenen Excel-Vorlage rutscht so etwas leicht durch; im offen gelegten Rechenweg steht jeder Posten an genau einer Stelle.

Photovoltaik ändert den Bezug nicht. Der Bemessungsfall ist die Winter-Abendspitze, und in der liefert die Anlage nichts. Die PV wird deshalb mit Scheinleistung und Einspeiserichtung erfasst, das Bezugsergebnis bleibt davon unberührt.

Am Ende steht eine Planungsgrundlage. S_max, Bemessungsstrom und die empfohlene NH-Sicherung beantworten die Forenfrage (reicht der Anschluss auch mit künftigen Wallboxen?) für dieses eine Projekt statt pauschal. Verbindlich wird es erst mit der Anschlusszusage des Netzbetreibers.

### Excel-Pflege gegen Editor-Eingabe: die Gegenrechnung

Die folgende Gegenrechnung ist eine Beispielrechnung mit eigenen, bewusst konservativen Annahmen. Es sind Schätzwerte, keine Messwerte und keine Kundendaten.

| Posten | Annahme | Einordnung |
|---|---|---|
| Excel-Bilanz je Projektstand | 3,0 h | untere Kante der eigenen Schätzung (3 bis 4 h); Fehlersuche nicht eingerechnet |
| Planstände je Projekt | 3 | Entwurf, Genehmigung, Ausführung; eher niedrig angesetzt |
| Aufwand Excel je Projekt | 9,0 h | 3 Stände × 3,0 h |
| Ersteingabe im Editor | 1,0 h | eigene Schätzung |
| Je weiterem Stand im Editor | 0,5 h | großzügig angesetzt; oft sind es Minuten |
| Aufwand Editor je Projekt | 2,0 h | 1,0 h + 2 × 0,5 h |
| Ersparnis je Projekt | 7,0 h | Differenz der beiden Wege |
| Vergleichbare Projekte je Jahr | 5 | Drei-Personen-Büro mit Wohnungsbau-Schwerpunkt |

Wie viel Doppelarbeit dort steckt, zeigt das [Praxisszenario zum Verteilerplan](https://bimwired.com/landing/wissen/praxisszenario-verteilerplan.html). Pro braucht dabei nur der Arbeitsplatz, der Bilanz und Pläne tatsächlich bearbeitet.

## Was davon übertragbar ist

Der Weg ist zuerst ein Weg für den Wohnbau. Die DIN 18015-1 ist eine Norm für elektrische Anlagen in Wohngebäuden, ihre Bedarfskurven gelten für Wohneinheiten. Gewerbeflächen im Haus bildet der Editor über W/m²-Planungswerte mit eigener Gleichzeitigkeit ab. Branchenspezifische Lastprofile (Bäckerei, Praxis, Kühlhaus) sind das nicht; dort bleibt die Lastannahme Ingenieurarbeit.

Das Ergebnis ist eine Planungsgrundlage, keine Genehmigung. Verbindlich sind die örtliche TAB und die Anschlusszusage des Netzbetreibers. Der Bericht ist die Unterlage für diese Abstimmung, er ersetzt sie nicht.

Ein Lastmanagement simuliert der Editor nicht. Welche Leistung für die sechs Ladepunkte angesetzt wird (volle Anschlussleistung oder ein mit dem Netzbetreiber abgestimmter, gesteuerter Wert), bleibt eine planerische Entscheidung und gehört im Projekt dokumentiert.

Und weil die Bilanz kein Revit-Modell braucht, funktioniert der Weg auch in frühen Leistungsphasen und in Büros, die noch nicht in Revit modellieren.

## Häufige Fragen

### Braucht die Leistungsbilanz in BimWired ein Revit-Modell?

Nein. Die Bilanz entsteht vollständig im Browser-Editor, aus Eingaben zu Wohneinheiten und Sonderlasten. Ein Revit-Modell wird erst für die späteren Schritte interessant, wenn Stromkreise aus dem Modell gesammelt und Verteilerpläne erzeugt werden.

### Warum senkt die Photovoltaik die berechnete Anschlussleistung nicht?

Weil der Bemessungsfall die Winter-Abendspitze ist: Dann laufen Wärmepumpe und Ladepunkte, die Photovoltaik liefert aber nichts. Die Anlage wird trotzdem mit Wechselrichter-Scheinleistung und Einspeiserichtung erfasst, der berechnete Bezug bleibt davon unberührt.

### Ersetzt der PDF-Bericht die Abstimmung mit dem Netzbetreiber?

Nein. Die Leistungsbilanz ist eine Planungsgrundlage; verbindlich sind die örtliche TAB und die Anschlusszusage des Netzbetreibers. Der Bericht mit Firmenkopf, vollständigem Rechenweg und Unterschriftenzeilen ist die Arbeitsunterlage, mit der Sie in diese Abstimmung gehen.

## Quellen

1. elektrikforum.de: „Dimensionierung Hausanschluss Mehrfamilienhaus" (Forendiskussion, Juni 2023). https://www.elektrikforum.de/threads/dimensionierung-hausanschluss-mehrfamilienhaus.43084/ (abgerufen am 25.08.2026)
2. Initiative ELEKTRO+: „Auslegung des Hauptstromversorgungssystems". https://www.elektro-plus.com/elektroplanung/dimensionierung-netzanschluss/auslegung-hauptstromversorgungssystem (abgerufen am 25.08.2026)
3. „Elektroplanung in Wohngebäuden", Zeitschrift de, Ausgabe 12/2020 (Volltext-PDF zu den Kernanforderungen der DIN 18015-1:2020-05). https://www.elektro.net/media/file/Kwqzk199w7/fd7e48cc/DE_12_2020_31-34_EA42neu.pdf (abgerufen am 25.08.2026)
4. Bundesnetzagentur: „Steuerbare Verbrauchseinrichtungen (§ 14a EnWG)", Verbraucherportal. https://www.bundesnetzagentur.de/DE/Vportal/Energie/SteuerbareVBE/start.html (abgerufen am 25.08.2026)
5. BauNetz Wissen: „Leistungsbedarf und Anschlusswert". https://www.baunetzwissen.de/elektro/fachwissen/grundinstallationen/leistungsbedarf-und-anschlusswert-152962 (abgerufen am 25.08.2026)

Die genannte Ansprache-Kartei von 192 Büro-Profilen ist internes, unveröffentlichtes Material von BimWired (Stand August 2026): von uns durchgesehene öffentliche Profile mit einem von uns notierten Ansatzpunkt je Büro, nicht repräsentativ und nicht öffentlich einsehbar.

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/praxisszenario-leistungsbilanz-mfh.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
