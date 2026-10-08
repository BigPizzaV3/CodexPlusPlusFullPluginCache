# Methodology — complex exam/mandate answers (Anwaltsprüfungs-Bauplan)

Derived from 25 real Musterlösungen (UZH/Anwaltsprüfungs-Niveau). Graders award
points per recognized problem + structure element, not per conclusion — so
structure IS substance. Use this for any multi-part Sachverhalt question.

## Modus wählen (erster Schritt, im Plan festhalten)

Wähle anhand der Aufgabe einen von drei Modi — er bestimmt Rechercheaufwand
und Antwortumfang. Im Zweifel eine Stufe höher.

- **SCHNELL** — eine einzelne, klar umrissene Lookup-Frage (ein Artikel, eine
  Definition, eine Frist, ein bekanntes Institut ohne Sachverhalt):
  Norm lesen → 1 bestätigender Leitentscheid falls einschlägig → knappe
  Antwort (Regel + Beleg + ggf. Zahl/Frist). Kein Bauplan-Overhead.
- **NORMAL** — Standard-Fallfrage mit EINEM erkennbaren Hauptpfad:
  voller Bauplan + Selbstkorrektur wie unten.
- **UMFANGREICH (Gutachten-Modus)** — mehrteilige Prüfung, mehrere Akteure/
  Ansprüche, ODER die Kernweiche ist nach der Norm-Lektüre NICHT eindeutig:
  zusätzlich **Pfad-Exploration** (unten) vor der Niederschrift; Antwort in
  Gutachtenstruktur mit Zwischenfazits.

## Pfad-Exploration (Pflicht im Modus UMFANGREICH bei unklarer Weiche)

Wenn die ergebnisentscheidende Weiche (Kernweiche, 4g) nach vollständiger
Artikel-Lektüre offen ist — zwei plausible Normen/Qualifikationen/Verfahrens-
arten konkurrieren:

1. BEIDE Pfade kurz und gezielt erkunden, bevor du dich festlegst:
   je Pfad `get_article_case_law` auf die tragende Norm (sort="citations",
   limit 3) und/oder `find_leading_cases(topic + Norm)`; die beste Fundstelle
   pro Pfad LESEN (read_chunk).
2. Entscheiden anhand der Belege (Leitentscheid schlägt Wortlaut-Intuition;
   neuere Praxis schlägt ältere; Spezialnorm schlägt Generalnorm).
3. In der Antwort NUR den gewählten Pfad ausführen; der unterlegene Pfad
   erhält genau EINEN Abgrenzungssatz mit Beleg („Nicht einschlägig ist …,
   weil … [Zitat]"). Keine Doppel-Subsumtion, kein Hedging.

Die Exploration kostet 2–4 zusätzliche Tool-Calls und verhindert den
teuersten Fehler: eine brillant begründete Antwort auf dem falschen Pfad.

## Antwort-Bauplan (in dieser Reihenfolge)

0. **Fakten-Extrakt** (bei Fallfragen, VOR jeder rechtlichen Überlegung) —
   aus dem Sachverhalt festhalten: (a) Parteirollen: wer klagt, wer ist
   beklagt, wer handelt/unterlässt/erscheint nicht — Pronomen und
   Relativsätze explizit auflösen; (b) Streitwert und was daraus folgt
   (Verfahrensart, Kostenbefreiung, Rechtsmittelzug); (c) Daten/Fristen;
   (d) jede gestellte Teilfrage wörtlich. Vor dem Fazit jeden Prüfschritt
   gegen diesen Extrakt abgleichen — eine Subsumtion, die einer
   Extrakt-Zeile widerspricht, ist ein Konsistenzfehler.
1. **Zerlege die Frage** in alle Teilfragen/Prüfgegenstände (Personen, Ansprüche,
   Handlungen, Konstellationen). Bei ≥3 Strängen: zuerst eine Übersicht
   (z.B. Person-×-Anspruch-Matrix), Hauptteile nummerieren (1./2./3.).
2. **Restriktionen wörtlich befolgen** („… ist nicht zu prüfen"): Ausgeschlossenes
   kommt nicht vor; obsolet Gewordenes in einem Satz als obsolet kennzeichnen.
3. **Vorfragen zuerst**: Geltungsbereich, Zuständigkeit, Verfahrensart,
   Staatsvertragsvorrang — vor der materiellen Prüfung.
3b. **Reihenfolge-Check bei mehrstufigen Verfahren** (Registervollzug,
   Prozessschritte, Vollstreckung): explizit prüfen und benennen, welcher
   Schritt zwingend VOR dem beantragten kommen muss (z.B. Eintragung des
   Erbgangs vor Verfügungen über Nachlassgrundstücke; Rechtsöffnung vor
   Fortsetzung). Der übersehene Vorschritt ist ein klassischer Punkteverlust.
4. **Pro Prüfpunkt fix**: (a) Obersatz („Zu prüfen ist …"), (b) Regel als
   Voraussetzungskatalog mit Normzitat bis Abs./lit., (c) Subsumtion
   Voraussetzung für Voraussetzung mit Sachverhaltselementen („In casu … (+)/(−)"),
   (d) Zwischenergebnis in einem Satz.
5. **Zitierweise**: Norm in Klammer direkt hinter die Aussage
   („… (Art. 229 Abs. 1 lit. b ZPO)"); tragende Praxis als
   „(vgl. BGE 137 IV 13 E. 2-4)" bzw. „(BGer 4A_268/2018 vom 18.11.2019 E. 5)";
   pro Kernaussage genau EINE Fundstelle; Normzitate dominieren (5–10:1),
   Urteilszitate sind wenige, aber tragende Leitentscheide. Nach Entwicklung
   gefragt → Entscheide chronologisch mit Jahr.
6. **Ausdrücklich verneinen**, was nicht greift („fällt ausser Betracht, weil …")
   — nie stillschweigend weglassen.
7. **Nebenstränge mitprüfen**, auch bei negativem Ergebnis: Prozessuales,
   Rechtsmittel + Fristen, Aktiv-/Passivlegitimation, Rechtsmissbrauch.
8. **Lücken benennen statt füllen**: „Der Sachverhalt liefert keine Anhaltspunkte,
   dass …" → vertretbare Annahme setzen, weiterprüfen. Bei echter Kontroverse
   beide Linien ausformulieren, dann Position beziehen (nie „es kommt darauf an"
   ohne Entscheid).
9. **Eventualbegründungen** für jede ergebnisrelevante Weichenstellung:
   „Selbst wenn man annimmt, dass …, so …".
9a. **Schuldform-Kaskade bei Erfolgsdelikten**: immer zuerst Vorsatz inkl.
   Eventualvorsatz prüfen (Wissen um Risiko + Inkaufnahme), erst bei dessen
   Verneinung zur Fahrlässigkeit absteigen — nie die mildere Schuldform
   stillschweigend voraussetzen. Gleiches Muster bei Qualifikationen
   (Grundtatbestand → Qualifikation → Privilegierung explizit).
9b. **Streitstände benennen**: Ist ein Punkt in Lehre/Praxis umstritten
   (Prüfungsreihenfolge, Verwertbarkeit, Vormerkbarkeit …), die Kontroverse
   explizit machen („str.; nach h.M. …, a.A. vertretbar") und dann Position
   beziehen — Musterlösungen bepunkten das Erkennen des Streits separat vom
   Ergebnis. Indiz im Korpus: `get_citing_decisions` zeigt divergierende
   Linien; Formulierungen wie „offengelassen" in der massgebenden E.
9c. **Würdigungs-Raster bei "kritische Stellungnahme/Würdigung"-Fragen**:
   systematisch die übergeordneten Dimensionen abklopfen, nicht nur die
   Sachdogmatik: (1) Legalitätsprinzip/Wortlautgrenze (Art. 5, 31, 36 BV),
   (2) Kompetenzordnung (Bund/Kantone), (3) Grundrechte + EMRK-Parallelen,
   (4) Verhältnismässigkeit, (5) Rechtssicherheit/Vorhersehbarkeit,
   (6) praktische Konsequenzen (z.B. Überhaft, Vollzugsprobleme). Pro
   Dimension mindestens ein Satz Position — Musterlösungen bepunkten die
   Breite der Würdigung. Für ratio legis und Gesetzgeber-Argumente:
   `get_article_purpose(law, art)` / `search_materialien` (wörtliche
   Botschaft-Absätze, zitierbar als "Botschaft, BBl Jahr Seite").
10. **Zweistufig schliessen**: Zwischenfazit je Teilfrage + Gesamtfazit mit
    klarer Antwort auf JEDE gestellte Teilfrage.

## Selbstkorrektur-Protokoll (nach Entwurf, vor Abgabe — PFLICHT)

1. **Teilfragen-Gegencheck**: Frage erneut lesen; jedes Fragewort einzeln
   abhaken — hat der Entwurf dazu ein eigenes (Zwischen-)Fazit? Geforderte
   Anzahl erfüllt („vier Leitentscheide", „alle Möglichkeiten")?
2. **Restriktions-Check**: Ausführungen zu explizit Ausgeschlossenem → streichen.
3. **Vollständigkeits-Sweep**: alle Personen/Ansprüche/Varianten aus Schritt 1
   abgedeckt? Nebenstränge vorhanden? Jede „fraglich ist…"-Stelle beantwortet?
4. **`verify_citations` über ALLE Fundstellen — inklusive E.-Nummern**
   (`"BGE 129 III 426 E. 3.1.1"` prüft die Erwägung auf Chunk-Ebene mit
   Preview). Nicht Verifizierbares: Zitat entfernen, Regel behalten (nie
   umgekehrt ein Zitat erfinden). E.-Nummern NUR zitieren, wenn per
   `read_chunk` gelesen oder per `verify_citations` bestätigt. Bei
   zweifelhafter Zuordnung Inhalt↔Fundstelle: die E. gegenlesen.
4b. **Kein Verifikations-Hedging im Antworttext**: Meta-Kommentare wie
   „(nicht eigenständig verifiziert)" gehören NICHT in die Prüfungsantwort —
   anerkannte Grundsätze werden als solche gebracht; was du nicht halten
   kannst, lässt du weg (siehe 4). Der Antworttext liest sich wie eine
   Musterlösung, nicht wie ein Rechercheprotokoll.
4c. **Zahlen-Sweep**: Beträge, Fristen, Schwellen- und Grenzwerte des
   geprüften Instituts explizit nennen (z.B. Tagessatz mind. CHF 30 /
   ausnahmsweise 10; Streitwertgrenzen; Fristen in Tagen) — Korrektoren
   bepunkten genau diese Zahlen. Beim Lesen der massgebenden E./Artikel
   gezielt danach suchen.
4d. **Norm-Zitat-Gate**: auch Gesetzes-Zitate mit ungewohnten Nummern oder
   lit./Ziff.-Angaben über `get_article`/`verify_citations` prüfen — ein
   halluzinierter „Art. 2 lit. c" eines Spezialgesetzes kostet mehr als das
   fehlende Zitat. Zweiten Halbsatz und Absatz-Nummer gegenlesen.
4e. **Sachverhaltstreue-Check**: jede Tatsache in der Subsumtion muss im
   Aufgaben-Sachverhalt stehen. Nichts dazuerfinden, nichts „typischerweise"
   unterstellen; bei fehlenden Angaben: Alternativ-Subsumtion („falls X, dann…")
   statt stillschweigender Annahme.
4f. **Ergebnisdisziplin**: pro Teilfrage genau EIN klar formuliertes Ergebnis
   (kein „einerseits/andererseits" als Schluss). Bei echten Streitfragen:
   h.M./Rechtsprechung als Ergebnis, Gegenauffassung in einem Satz davor.
4g. **Kernweiche-Check (vor jedem Ergebnis)**: Identifiziere die EINE
   Weichenstellung, die das Resultat dieser Teilfrage kippen kann (die
   entscheidende Tatbestandsvoraussetzung, eine Spezialnorm, eine
   Ausnahmebestimmung, die Zuständigkeits-/Verfahrensart). Diese Weiche wird
   NACHGESCHLAGEN (Artikel vollständig lesen), nie aus dem Gedächtnis
   entschieden — eine brillante Antwort mit falsch gestellter Weiche verliert
   gegen eine mittelmässige mit richtiger.
4h. **Subsidiaritäts-Sweep nach jeder Bejahung**: Sobald ein Anspruch, eine
   Bewilligung oder eine Zuständigkeit BEJAHT ist: aktiv nach Ausschluss-,
   Subsidiaritäts- und Vorbehaltsnormen suchen (`nav_law_toc` um die
   Anspruchsnorm; Stichworte „vorbehalten", „subsidiär", „soweit nicht",
   „findet keine Anwendung"). Die häufigste Fehlerquelle ist der Anspruch,
   der an einer nachgelagerten Norm scheitert.
4i. **Kantonale Norm-Disziplin**: Ist die Frage kantonalrechtlich geprägt
   (Baurecht/PBG, kantonales Verfahrensrecht, kantonales Steuerrecht), wird
   der KONKRETE kantonale Erlass beigezogen — `search_cantonal_law` (Kanton
   setzen!) → `get_cantonal_law(id, article=…)` liefert den Artikeltext.
   Nie mit Bundesrecht oder einem anderen Kanton „analog" argumentieren, wo
   der eigene Erlass verfügbar ist.
4j. **Nebenwirkungs-Check bei Aussagen-/Behauptungsfragen** („Stimmt es,
   dass…?"): benachbarte Normen prüfen, die die Aussage einschränken oder
   erweitern — die Musterlösung erwartet fast immer das „ja, aber/nein, ausser".
4k. **Zweistufen-Fazit**: Verlangt die geprüfte Norm eine zweite Stufe
   (Interessenabwägung, „nötigenfalls", Verhältnismässigkeit, Zumutbarkeit),
   führe diese Stufe mit den konkreten Sachverhaltselementen zu Ende und
   schliesse mit einem klaren Ergebnis. „Wäre noch zu erhärten/zu gewichten"
   ist nur zulässig, wenn der Sachverhalt die nötige Angabe wirklich nicht
   enthält — dann die fehlende Angabe benennen UND das bei üblicher Sachlage
   naheliegende Ergebnis. Eine bejahte erste Stufe mit offengelassener
   zweiter Stufe ist eine unvollständige Antwort, kein vorsichtiges Fazit.
   Gleiches gilt für das Gesamtfazit: Zeigt die Analyse klar in eine
   Richtung, formuliere den Schluss entschieden — Ambivalenz trotz
   eindeutiger Analyse verschenkt das Ergebnis.
   Grenzfall-Kennzeichnung: Bei echten Wertungs-Weichen (die Kasuistik
   trägt beide Richtungen) bleibt das Fazit entschieden, benennt aber die
   Gegenposition in 1–2 Sätzen und formuliert das eigene Ergebnis als
   überwiegende Auffassung («Nach der dargestellten Praxis überwiegt …»).
   Apodiktisch («ist», «liegt vor») nur, wenn die gefundene Kasuistik
   eindeutig in eine Richtung zeigt.
4l. **Kantonale Zitat-Verifikation**: Kantonale Gerichtsentscheide (VB./VGr-,
   BRKE/BRGE-, LGVE-, RB-Nummern usw.) unterliegen derselben
   Verifikationspflicht wie BGE: vor Verwendung Datum UND Kernaussage gegen
   den Volltext prüfen (`read_chunk`/`read_full_text`/`get_cantonal_law`).
   Ist der Volltext nicht greifbar: Fundstelle ohne geratene Detailangaben
   nennen (kein Datum, keine Paraphrase der Erwägung) oder weglassen — ein
   korrektes kantonales Normzitat ohne Entscheid ist besser als ein Entscheid
   mit falschem Datum.
4m. **Vertragstext-Transparenz**: Verlangt die Aufgabe die präzise Benennung
   von Bestimmungen eines privaten Regelwerks (AVB, Police, Reglement,
   Statuten), das weder im Aufgabentext mitgeliefert noch im Korpus
   auffindbar ist: NIE konkrete Artikel-/Ziffernnummern eines nicht
   vorliegenden Textes erfinden. Stattdessen transparent machen („Die AVB
   liegen nicht vor; massgeblich ist die konkrete Deckungsklausel —
   üblicherweise geregelt als …") und die Prüfung entlang der gesetzlichen
   Struktur (VVG, OR) und der praxisüblichen Klausel-Systematik führen, mit
   ausdrücklichem Vorbehalt des konkreten Vertragswortlauts.
4n. **Kandidaten-Enumeration bei Issue-Spotting**: Verlangt die Aufgabe
   „n Besonderheiten/Probleme/Aspekte": zuerst eine Kandidatenliste mit MEHR
   als n Einträgen bilden (mindestens n+2), jeden Kandidaten in 1–2 Sätzen
   auf Ergebnisrelevanz prüfen, DANN die n stärksten wählen. Tausch-Regel:
   Endet ein gewählter Strang bei der Ausarbeitung mit „unproblematisch/ohne
   Belang", ist er gegen den nächsten Kandidaten zu tauschen — ein als
   irrelevant erkannter Punkt bleibt nie in der Antwort.
4o. **Norm-Anker und unbedingtes Fazit**: Jede tragende Aussage nennt ihre
   Norm ausgeschrieben (Art./§ mit Abs./lit. und Erlass) — „sinngemäss" oder
   nur über ein Urteil belegt genügt nicht, wenn eine konkrete Norm
   existiert. Jedes (Zwischen-)Fazit ist EIN unbedingter Satz („X ist …",
   nicht „X dürfte wohl …"); Unsicherheit gehört in die Subsumtion (dort
   benennen und auflösen), nie in den Fazit-Satz.
4p. **Kasuistik-Suchpflicht an Begriffs-Weichen**: Hängt eine Kernweiche an
   einem unbestimmten Rechtsbegriff mit reicher Einzelfall-Praxis
   (Unfallbegriff, Ungewöhnlichkeit, Adäquanz, grobe Fahrlässigkeit,
   Willkür …): zusätzlich zur Leitentscheid-Ebene IMMER eine semantische
   Suche mit den KONKRETEN Sachverhaltsmerkmalen absetzen
   (`search_semantic`/`search_hybrid` mit den Fallmerkmalen als Query, nicht
   mit dem Rechtsbegriff allein). Das sachverhaltsnächste Präjudiz lesen und
   in der Antwort diskutieren; weicht das eigene Ergebnis davon ab, die
   Abweichung ausdrücklich begründen. Ein Leitentscheid zur
   Begriffsdefinition ersetzt die Kasuistik-Suche nicht.
4q. **Normumfeld-Sweep**: Zu jeder tragenden Norm systematisch das UMFELD
   prüfen, bevor die Antwort steht: (a) zeitliche Geltung — bei
   Datums-Signalen im Sachverhalt (Altfälle, laufende Fristen, kürzliche
   Revisionen) die Übergangs-/Schlussbestimmungen des Erlasses nachschlagen
   (`nav_law_toc`, Ende des Erlasses); (b) Verordnungsebene — konkretisiert
   eine VO die Kernnorm (Zahlen, Verfahren, Berechnungen)?; (c)
   übergeordnetes Recht — drängt sich eine BV-/EMRK-Dimension auf
   (Grundrechtseingriff, Verfahrensgerechtigkeit)?; (d)
   Eingangsvoraussetzungen des Rechtsbehelfs (Frist, Form, Legitimation,
   Streitwertgrenze), bevor materiell geprüft wird. Pro Buchstabe genügt
   EIN gezielter Lookup; gefundene Umfeld-Normen ausgeschrieben zitieren.
4r. **Format-Treue**: Die Formvorgabe der Aufgabe («in wenigen Sätzen»,
   «stichwortartig», «gutachterlich», «nennen Sie», Tabellenform) wird
   wörtlich in den Fakten-Extrakt übernommen und das Antwortgerüst daran
   ausgerichtet. Massgeblich ist die Struktur, nicht eine Längenregel:
   verlangt die Aufgabe eine knappe Form, tragen wenige präzise Sätze pro
   Punkt mehr als ein volles Gutachten; verlangt sie ein Gutachten, gilt
   der Bauplan.
5. **Struktur-Check**: Regel→Subsumtion→Fazit pro Prüfpunkt sichtbar?
   Zwischenergebnisse + Gesamtfazit markiert? Positionierung bei strittigen
   Punkten vorhanden?
6. **Punkte-Heuristik**: Kann ein Korrektor jedem Absatz ein prüfbares Element
   zuordnen? Redundanzen und nicht angelegte Prüfungen streichen.
