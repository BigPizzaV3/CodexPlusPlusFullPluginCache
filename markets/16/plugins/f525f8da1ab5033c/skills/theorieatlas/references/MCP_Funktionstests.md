# MCP-Wissensbrücke: Funktionstests und wissenschaftliche Abnahme

Die vier Werkzeuge werden im öffentlichen Paket über `mcp.json` deklariert. Die fünf positiven und drei negativen Reviewfälle stehen verbindlich in `plugin.json` unter `extensions.com.openai.review.test_cases`; diese Notiz dokumentiert die beobachteten privaten Vorprüfungen und wissenschaftliche Grenzziehungen. Sie ist weder ein Luhmann-Primärtext noch ein Testprotokoll einer öffentlichen Preview.

## Beobachtete Vorprüfungen vom 7. November 2026

- Der eigenständig registrierte MCP-App-Verbindungstest meldete erfolgreiche Aufrufe von `luhmann_wissensindex`, `luhmann_themenrecherche` und `luhmann_bezugspfad`.
- Die privat integrierte Browserprobe meldete Registerabruf (17 Artikel), Themensuche (sechs Treffer) und vier vollständige Einzelartikelabrufe; das Verfahren trennte systemtheoretische und ressourcenbezogene Hypothesen sowie einen Gegenbefund.
- Ein weiterer privater Browserproben-Test meldete den Bezugspfad `id=strukturelle-kopplung`, `depth=2` (acht Knoten, elf gerichtete Kanten) sowie drei Einzelartikelabrufe; `editorial_related_id` wurde nicht als Theoriebeweis behandelt.
- Der ursprüngliche private Theorieatlas 1.0.7 meldete in einem eigenen Browser-Test erfolgreiche Aufrufe **aller vier Werkzeuge** (Index, Themensuche, Hauptartikel, Bezugspfad) über die registrierte MCP-App.
- **Noch nicht nachgewiesen** sind die Werkzeugaufrufe in der gesonderten öffentlichen Portal-Preview mit dem durch `mcp.json` deklarierten Server. Die Ergebnisse der privaten Browserkonfiguration dürfen nicht als dessen Abnahme ausgegeben werden.

## Positiv- und Negativfälle

Die reproduzierbaren Fälle (P1–P5 und N1–N3), ihre exakten Werkzeugnamen, Beispielargumente und Bestehenskriterien sind Bestandteil des Review-Manifests `plugin.json`. Die Tests decken Register, Suche und Artikelrecherche, Bezugspfad, Quellenstatus, den kontrollierten Beobachtungswechsel sowie Schreibschutz, Privatsphäre und Suchraumbegrenzung ab.

## Wissenschaftliche Grenzziehungen

- Registerangaben, Suchscores, Graphkanten und redaktionelle Quellstatusfelder sind Daten zur Auswahl und Einordnung, **keine** automatisch gesicherten wissenschaftlichen Befunde.
- Die Themenrecherche durchsucht ausschließlich öffentlich registrierte Atlasbeiträge, nicht das übrige Repository oder private Dateien.
- Eine `editorial_related_id`-Kante empfiehlt Lektüre, beweist aber keine Kausalität, theoretische Ableitung oder Primärtextstelle.
- Zusätzliche wissenschaftliche Erklärungsleistung wird erst durch begründete Mechanismen, konkurrierende Erklärungen und diskriminierende Beobachtungen beanspruchbar.
- Der Cloudflare-Worker bietet keine Schreibfunktion für GitHub und keine eigenständige empirische Untersuchung.
