---
titel: "Verteilerplan-Checkliste: vollständig nach DIN EN 61082 und DIN VDE 0100-510"
quelle: https://bimwired.com/landing/wissen/checkliste-verteilerplan.html
stand: 2026-08-25
art: artikel
fragen:
  - "Welche Punkte prüfe ich vor der Abgabe eines Verteilerplans?"
  - "Was muss ein Verteilerplan enthalten?"
  - "Wie viele Stromkreise dürfen an einen FI-Schutzschalter?"
  - "Wie viel Reserve gehört in den Stromkreisverteiler?"
---

# Verteilerplan-Checkliste: vollständig nach DIN EN 61082 und DIN VDE 0100-510

Diese Checkliste prüft einen Verteilerplan (die einpolige Übersicht je Verteiler samt Stromkreisverzeichnis) auf Vollständigkeit: Kopf, Einspeisung, Abgänge, Reserve und Übergabeformate. Es sind 29 Punkte, gedacht je Verteiler, vor jeder Abgabe und nach jeder Revision. Die Reihenfolge ist die, in der ich selbst prüfe: erst der Kopf, dann die Einspeisung, dann jeder Abgang für sich, zuletzt Verzeichnis und Übergabe. Was am Anfang fehlt, kostet hinten am meisten.

## Block A: Kopf, Schriftfeld und Symbolik

- [ ] Das Schriftfeld nennt Projekt, Gebäude oder Bauteil, Verteilerbezeichnung, Verfasser und Datum.
- [ ] Der Planstand ist eindeutig: genau ein gültiger Index, Altstände gekennzeichnet oder eingezogen.
- [ ] Die Revisionstabelle nennt je Änderung Index, Datum, Kurzbeschreibung und Bearbeiter.
- [ ] Jedes Blatt trägt Blattnummer und Gesamtblattzahl („Blatt 2 von 6").
- [ ] Querverweise zwischen Blättern stimmen; kein Verweis läuft ins Leere.
- [ ] Alle Schaltzeichen stammen aus einer Symbolwelt nach IEC 60617, ohne Fremdsymbole.

**Warum:** Dass Schaltpläne Angaben zu Stromkreisen, Kabeln und Schutzeinrichtungen enthalten müssen, steht in DIN VDE 0100-510, Abschnitt 514.5; Stefan Euler referiert das in seinem Fachbeitrag zur Dokumentation elektrischer Anlagen. Die Schaltzeichen dazu kommen aus der IEC 60617, laut VDE VERLAG eine Datenbank mit etwa 1.900 Zeichen. Der letzte Punkt klingt banal, aber gemischte Symbolwelten fallen erst auf, wenn ein Fremder den Plan liest.

## Block B: Einspeisung und Struktur

- [ ] Die Zuleitung nennt Herkunft (Hausanschluss oder übergeordneter Verteiler), Kabeltyp und Querschnitt.
- [ ] Die Vorsicherung der Zuleitung steht mit Art und Nennstrom im Plan.
- [ ] Zähl- und Messeinrichtungen sind mit Polzahl an der richtigen Stelle eingezeichnet.
- [ ] Der Zählerplatz ist bei Wohngebäuden für mindestens 63 A Bemessungsstrom ausgelegt.
- [ ] Jeder Verteiler und Abgang trägt ein eindeutiges Betriebsmittelkennzeichen nach dokumentiertem Schema, etwa EN IEC 81346.
- [ ] Dasselbe Kennzeichen steht identisch im Plan, im Verzeichnis und am Betriebsmittel.

**Warum:** Die mindestens 63 A für den Zählerplatz nennt der Fachartikel „Elektroplanung in Wohngebäuden" („de" 12/2020) zur DIN 18015-1:2020-05. Für die Kennzeichnung gibt die EN IEC 81346 das Schema vor, laut EPLAN-Blog mit den drei Aspekten Funktion „=", Ort „+" und Produkt „-". Welches Schema Sie wählen, ist zweitrangig; entscheidend ist, dass es dokumentiert ist und überall dasselbe Kennzeichen steht.

## Block C: Je Abgang

- [ ] Jeder Abgang führt sein Schutzorgan mit Art, Charakteristik und Nennstrom auf (etwa LS B16).
- [ ] Jeder FI-Schutzschalter (RCD) steht mit Bemessungsdifferenzstrom und zugeordneten Stromkreisen im Plan.
- [ ] Steckdosen-Stromkreise bis 32 A liegen hinter einem RCD mit höchstens 30 mA.
- [ ] In Wohnungen liegen auch Stromkreise mit Leuchten hinter einem RCD mit höchstens 30 mA.
- [ ] An einem zweipoligen RCD hängen höchstens zwei, an einem vierpoligen höchstens sechs einphasige Endstromkreise.
- [ ] Kabeltyp, Aderzahl und Querschnitt sind je Abgang angegeben (etwa NYM-J 3x1,5 mm²).
- [ ] Klemmen sind dort bezeichnet, wo Abgänge auf Klemmen geführt werden.
- [ ] Jeder Stromkreis trägt einen baustellenverständlichen Raum- oder Funktionstext.

**Warum:** Die 30-mA-Pflicht für Steckdosen-Stromkreise bis 32 A und für Leuchten-Stromkreise in Wohnungen erläutert der DKE-Normenhinweis zur DIN VDE 0100-410:2018-10. Die Obergrenze von zwei beziehungsweise sechs Endstromkreisen je RCD ist eine Empfehlung aus dem „de"-Fachartikel zur DIN 18015-1, keine Vorschrift; ich halte mich trotzdem daran, weil sonst beim Auslösen halbe Wohnungen dunkel sind.

## Block D: Verzeichnis und Reserve

- [ ] Das Stromkreisverzeichnis für die Verteilertür liegt bei und stimmt mit dem Plan überein.
- [ ] Das Verzeichnis nennt je Stromkreis Nummer, Absicherung, RCD-Zuordnung und Raum- oder Funktionstext.
- [ ] Reserveabgänge sind als solche beschriftet und im Verzeichnis mitgeführt.
- [ ] Rund 20 % Platzreserve im Verteiler sind eingeplant und im Plan ablesbar.

**Warum:** Die 20 % Platzreserve empfiehlt derselbe „de"-Fachartikel (12/2020) zur DIN 18015-1:2020-05. Reserveabgänge gehören ins Verzeichnis, damit man später sieht, wann die Reserve aufgebraucht ist, und nicht erst beim Öffnen der Tür.

## Block E: Übergabe

- [ ] Ein Papierexemplar von Plan und Stromkreisverzeichnis liegt im oder am Verteiler.
- [ ] Das Lieferdokument ist ein mehrseitiges, durchsuchbares Vektor-PDF, kein Scan.
- [ ] Für die Weiterbearbeitung existiert ein DXF je Blatt mit getrennten Layern; Text bleibt Text.
- [ ] Papier, PDF und DXF tragen denselben Revisionsstand.
- [ ] Festgehalten ist: Aufbau und Nachweise des gebauten Verteilers liefert der Schaltschrankbau, nicht dieser Plan.

**Warum:** Für den Verteiler als Erzeugnis gilt die DIN EN IEC 61439 (laut ZVEI-Informationsblatt seit 2010, Teile 1 und 2 seit Oktober 2021 als Edition 3). Sie betrifft den gebauten Schrank, nicht die Zeichnung, und diese Grenze sollte im Plan stehen, sonst wird sie irgendwann Ihnen zugerechnet. Zum Werkzeug: Laut BEEL erfüllt Revit allein die Anforderungen der DIN EN 61082 nicht vollständig, Verteilerschemata bleiben Handarbeit. Das deckt sich mit meiner Erfahrung.

## So nutzen Sie die Liste

Kopieren Sie die Liste in Ihr QM oder Ihre Planungsvorlage und haken Sie sie je Verteiler und Revision ab. Was nicht zutrifft, markieren Sie als „nicht zutreffend", statt es stillschweigend zu streichen; sonst weiß beim nächsten Index niemand mehr, ob der Punkt geprüft oder nur vergessen wurde. Begriffe, Normrahmen und den Weg aus dem Modell erklärt der Leitfaden [Verteilerplan normgerecht erstellen](https://bimwired.com/landing/wissen/verteilerplan-stromlaufplan-normgerecht.html). Welche Anschlussdaten das Revit-Modell dafür liefern muss, steht in [Stromkreise in Revit planen](https://bimwired.com/landing/wissen/stromkreise-in-revit-planen.html), und das [Praxisszenario Verteilerplan](https://bimwired.com/landing/wissen/praxisszenario-verteilerplan.html) rechnet den Umstieg modellhaft durch.

## Einordnung: das Werkzeug BimWired

Schriftfeld, Blattnummern und Querverweise habe ich lange genug von Hand nachgezogen; die Verteilerplan-Ausgabe erzeugt je Verteiler eine Übersicht (einpolig) auf A3 quer, mit Schriftfeld nach DIN EN ISO 7200, Querverweisen nach DIN EN 61082-1 und einer Revisionstabelle, die sich pflegen lässt. Export als Druck, mehrseitiges Vektor-PDF und DXF je Blatt, mit getrennten Layern und Text, der Text bleibt. Aus Block C prüfen feste Regeln Überlast, RCD-Pflicht und Mindestquerschnitte; der Revit-Befehl „Stromkreise übernehmen" schreibt Nummern, Sicherungen und Kabel ins Modell zurück. Handarbeit bleiben die Raum- und Funktionstexte, die örtliche TAB und die fachliche Prüfung. Das Werkzeug füllt die Liste nicht aus, es sorgt dafür, dass weniger Punkte offen bleiben.

## Häufige Fragen (FAQ)

### Wie viele Stromkreise dürfen an einen FI-Schutzschalter (RCD)?

Als Empfehlung zur Anlagenverfügbarkeit nennt der Fachartikel „Elektroplanung in Wohngebäuden" („de" 12/2020) zur DIN 18015-1:2020-05 höchstens zwei einphasige Endstromkreise je zweipoligem und sechs je vierpoligem FI-Schutzschalter. Unabhängig davon gilt nach DIN VDE 0100-410:2018-10 die 30-mA-Pflicht für Steckdosen-Stromkreise bis 32 A und in Wohnungen für Stromkreise mit Leuchten (erläutert im DKE-Normenhinweis).

### Wie viel Reserve gehört in einen Stromkreisverteiler?

Der Fachartikel „Elektroplanung in Wohngebäuden" („de" 12/2020) zur DIN 18015-1:2020-05 empfiehlt 20 % Platzreserve im Stromkreisverteiler. Dokumentierte Reserveabgänge in Plan und Verzeichnis zeigen, wie viel davon verbraucht ist.

### Gehört der Aufbauplan des Schranks zum Verteilerplan?

Nein. Der Verteilerplan ist eine einpolige Übersicht der Stromkreise; Geräteanordnung im Schrank und Nachweise des gebauten Verteilers gehören zum Schaltschrankbau. Dessen Erzeugnis regelt die Normenreihe DIN EN IEC 61439 (laut ZVEI-Informationsblatt seit 2010, Teile 1 und 2 seit Oktober 2021 als Edition 3).

## Quellen

1. Stefan Euler: Dokumentation elektrischer Anlagen (Fachbeitrag, PDF). https://expertennetzwerk-elektrotechnik.de/wp-content/uploads/2018/10/Fachbeitrag_Stefan_Euler_Dokumentation-elektrischer-Anlagen.pdf (abgerufen am 25.08.2026)
2. DKE: Normenhinweis zur DIN VDE 0100-410 (Konzept der Norm). https://www.dke.de/de/arbeitsfelder/core-safety/normenhinweise/konzept-0100-410 (abgerufen am 25.08.2026)
3. elektro.net: Elektroplanung in Wohngebäuden (Zeitschrift „de" 12/2020, Volltext-PDF). https://www.elektro.net/media/file/Kwqzk199w7/fd7e48cc/DE_12_2020_31-34_EA42neu.pdf (abgerufen am 25.08.2026)
4. ZVEI: Informationsblatt DIN EN IEC 61439 Edition 3 (PDF, Januar 2022). https://www.zvei.org/fileadmin/user_upload/Presse_und_Medien/Publikationen/2022/Januar/Neue_Informationsnbroschueren_des_Fachkreises_Niederspannung/1_Informationsblatt_NeueNorm_final_2022.pdf (abgerufen am 25.08.2026)
5. EPLAN-Blog: Normgerecht strukturieren und referenzieren nach EN IEC 81346. https://www.eplan.com/de-de/blog/software/normgerecht-strukturieren-und-referenzieren (abgerufen am 25.08.2026)
6. VDE VERLAG: IEC 60617, Schaltzeichen-Datenbank (Produktseite). https://www.vde-verlag.de/iec-normen/iec-datenbanken/iec-60617-schaltzeichen.html (abgerufen am 25.08.2026)
7. BEEL: Revit Stromlaufplan. https://www.beel.de/revit/revit-stromlaufplan/ (abgerufen am 25.08.2026)

---

Quelle: Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin (B.Sc. Architektur), Inhaberin von BimWired. Veröffentlicht unter https://bimwired.com/landing/wissen/checkliste-verteilerplan.html, Stand 25. August 2026. Dieser Text stammt aus dem Praxiswissen von BimWired (https://bimwired.com) und darf unter CC BY 4.0 mit Nennung der Quelle weitergegeben werden.
