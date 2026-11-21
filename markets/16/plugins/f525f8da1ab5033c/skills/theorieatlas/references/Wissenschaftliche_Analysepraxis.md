# Wissenschaftliche Analysepraxis des Theorieatlas

Diese Handreichung konkretisiert die in Bibliothek C entwickelte Erkenntnisprüfung für die interaktive Arbeit. Sie ist eine methodische Arbeitsanweisung, kein Primärtext von Niklas Luhmann und kein automatisiertes Verifikationssystem.

## Ausgangspunkt und Artikelauswahl

Die Ausgangsfrage wird zunächst unabhängig vom Theoriejargon festgehalten. Zu unterscheiden sind Gegenstand, Beobachtungseinheit und behaupteter Erklärungsbedarf. Bei verfügbarer MCP-Verbindung wird das aktuelle Register gelesen. Für thematisch offene Fragen liefert `luhmann_themenrecherche` eine **textbasierte Kandidatenliste** mit Trefferausschnitten und editorischem Status. Für begriffliche Verknüpfungen liefert `luhmann_bezugspfad` die explizit registrierten `related_ids` und eingehende Verweise. Danach werden die für die Untersuchung erforderlichen Beiträge mit `luhmann_wissenseintrag` tatsächlich gelesen. Für gewöhnliche Fachfragen genügen zwei bis fünf relevante Artikel. Nicht jeder der fünf Bibliothekspfade muss mechanisch vertreten sein; bei quellensensiblen Antworten hat der Werk- und Quellenatlas Vorrang.

### Werkzeuge und ihre Erkenntnisgrenzen

- `luhmann_wissensindex({})`: registergebundener Editions- und Themenüberblick. Das historische lokale Planungsdokument ist kein Ersatz für einen Live-Abruf.
- `luhmann_themenrecherche({"query":"Schulreform Lernklima","max_results":6})`: registrierte Atlasbeiträge lexikalisch auswählen. `score` ist ein Worttreffermaß, **kein** Relevanzurteil über die Wissenschaft. `incomplete:true` oder nichtleere `unavailable_ids` verhindern jede Vollständigkeitsbehauptung.
- `luhmann_bezugspfad({"id":"strukturelle-kopplung","depth":1})`: eingehende und ausgehende redaktionelle Verweise verfolgen. `depth:2` nur bei tatsächlichem Mehrwert verwenden. Kanten sind Lektürehinweise, kein theoretischer Nachweis.
- `luhmann_wissenseintrag({"id":"system-und-umwelt"})`: registrierten Volltext samt konkretem Quellen- und Nachweisstatus lesen. Die drei übrigen Werkzeuge ersetzen diese fachliche Quellenlektüre nicht.

Die Auswahlkette ist nachprüfbar: **Ausgangsfrage → registrierte Kandidaten → begründete Verknüpfungen → gelesene Textstellen → Gegenprüfung → Ergebnisstatus**. Zwischen Suchtreffer, Quellenbeleg und eigener Schlussfolgerung werden keine stillen Übergänge zugelassen. Keine privaten Fallakten oder unnötigen personenbezogenen Angaben als freie Suchanfrage übertragen.

Jeder verwendete Artikel behält seinen dokumentierten Nachweisumfang: `status` bezeichnet einen editorischen Stand, nicht den Rang einer Primärquellenprüfung. Bei Werkzitaten ist ausschließlich die konkret eingesehene und bezeichnete Originalstelle tragfähig. Ein Verweis, ein Abstract, ein Katalogeintrag oder ein editorischer Überblick ist kein belegtes wörtliches Zitat. Die Auswahl kann bei neuen GitHub-Editionen abweichen; die Plugin-Version ist keine Editionsauskunft.

## Analytische Operationen

**1. Beobachtungsgegenstand präzisieren.** Eine sozialtheoretische Frage beschreibt, welche Ereignisse, Entscheidungen oder Kommunikationen verstanden werden sollen. Komplexe Fälle werden nur dort in Systemtypen gegliedert, wo das einen tatsächlichen Unterschied macht.

**2. Theorieangebote rekonstruieren.** Die gewählten Luhmann-Begriffe werden in ihren Relationen entwickelt; historische Aussagen werden von späteren systematischen Rekonstruktionen getrennt. Wo sinnvoll, zeigen die Texte aus A die Begriffe, B die Quellenlage und D einen Fall.

**3. Konkurrenz und Differenz formulieren.** Es wird mindestens eine ernst zu nehmende alternative Betrachtung gewählt, wenn die Frage erklärenden Mehrwert beansprucht, etwa eine institutionelle, materielle, rechtliche oder psychologische Deutung. Nicht künstlich eine „Gegenmeinung“ hinzufügen, wenn bloß eine Begriffserklärung gefragt ist.

**4. Die vier Erkenntnisdimensionen prüfen.** C1 Beobachtungsgewinn: Welche zuvor unklare Differenz wird sichtbar? C2 Zusammenhangsgewinn: Welche nachweisbaren Anschlusswege oder Abhängigkeiten werden genauer beschrieben? C3 Erklärungsgewinn: Welche unter benennbaren Bedingungen unterschiedlichen Verläufe erwartet die Deutung, und was würde sie schwächen? C4 Beobachtungsverlust: Welche für die Frage relevanten Gesichtspunkte werden ausgeblendet? Diese Dimensionen sind keine additiven Punktzahlen.

**5. Ergebnisstatus bestimmen.** Ein begrifflicher Ordnungsgewinn ist kein empirischer Beweis; eine Prozesshypothese kein gemessener Kausalzusammenhang; ein bibliografischer Treffer keine Volltextprüfung. Ein beanspruchter empirischer Mehrwert braucht geeignete Beobachtungen, Vergleiche, Alternativerklärungen und benannte mögliche Gegenbefunde.

**6. Forschung anschließen.** Wenn die Frage danach verlangt, folgt eine konkrete Prüffrage mit möglichen Beobachtungseinheiten, Datenquellen und einem Gegenbefund, der die bevorzugte Lesart schwächen würde. Offene Punkte können auf den Forschungs- und Revisionspfad E bezogen werden, soweit der betreffende Eintrag tatsächlich gelesen wurde.

## Wissenschaftliche Antwortgestalt

Der Haupttext ist zusammenhängende Fachprosa. Als nützliche Gliederung kommen in Frage: Problem und Gegenstand; theoretische Rekonstruktion; relevante Kontrastanalyse; Erkenntnisleistung und Grenzen; Quellennachweise und Forschungsanschluss. Die Bezeichnungen C1–C4 erscheinen nur, wo sie einer vergleichenden Darstellung dienen. Für kurze Fragen genügt eine knappe, präzise Antwort.

Bei Live-Abrufen werden Edition und Artikelkennungen nur entsprechend tatsächlich zurückgelieferter Registerdaten genannt. Verweise auf den öffentlich verfügbaren Text ersetzen keine überprüfte Luhmann-Originalquelle. Scheitert MCP, können lokal verfügbare Begriffsreferenzen verwendet werden, aber keine nicht erfolgte Live-Lektüre behauptet werden.

## Prüffall: Schulreform und Lernklima

**Explanandum:** Weshalb verbessert eine organisatorisch beschlossene Reform das von Lernenden erlebte Unterrichtsklima möglicherweise nicht?

**Unterscheidungen:** Reformbeschluss der Schulorganisation und Interaktion im Unterricht sind unterschiedliche Vorgänge. Relevant ist, wie neue Regeln in wiederkehrenden Kommunikationen aufgegriffen werden.

**Alternative:** Hohe Arbeitsbelastung, personelle Unterdeckung oder Prüfungsdruck können den Verlauf ebenfalls erklären. Eine systemtheoretische Bezeichnung allein entscheidet nicht zwischen diesen Ursachen.

**C1:** Beschluss und Unterrichtsgespräch werden getrennt beobachtet. **C2:** Die Übertragung einer Vorgabe in Unterrichtsroutinen wird als Prozessfrage untersucht. **C3:** Ein Mehrwert entsteht erst, wenn Unterschiede in den anschließenden Routinen bei vergleichbaren Voraussetzungen den beobachteten Unterschied mit erklären; dies bleibt ohne Daten eine Hypothese. **C4:** Individuelles Erleben und Ressourcenverteilung könnten unterbelichtet bleiben.

**Prüfbares Anschlussdesign:** Zwei vergleichbare Klassen mit gleicher Reformvorgabe, dokumentierten Unterrichtssequenzen, anonymen Schülerbefragungen, Ressourcen- und Bewertungsbedingungen. Gegenbefund: Bleibt der beobachtete Unterschied nach Kontrolle der tatsächlichen Gesprächsroutinen ausschließlich mit Ressourcen- oder Prüfungsbedingungen verbunden, schwächt das die behauptete zusätzliche Erklärung der Kommunikationsanalyse. Dieses Beispiel ist konstruiert und kein empirischer Befund.

## Methodischer Mehrwert gegenüber bloßer Textauslagerung

Der Atlas verbindet einen stabilen analytischen Umgang mit Quellen und kontrastierenden Erklärungen mit einem unabhängig aktualisierbaren, versionierten Artikelbestand. Die MCP-Werkzeuge ermöglichen Register- und Einzelabruf sowie lexikalische Themensuche und redaktionelle Bezugspfad-Navigation. Weder das Ranking noch ein Graphverweis verifizieren Primärtexte oder erzeugen eigenständig eine wissenschaftliche Erklärung. Die vergleichende Analyse erfolgt durch das Sprachmodell unter diesen Arbeitsregeln. Wert und Grenzen beider Komponenten sind getrennt zu benennen.
