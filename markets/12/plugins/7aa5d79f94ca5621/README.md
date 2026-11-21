# Elektroplanung in Revit: KI-Skill und MCP-Server von BimWired

Fachwissen für die Elektroplanung mit Revit nach deutschen Normen, verpackt als Skill für ChatGPT, Claude, Codex und Cursor, plus ein öffentlicher, lesender MCP-Server, den dein Assistent direkt aufruft.

Die Texte stammen aus der Planungspraxis von Rowan Hamid, Elektrofachplanerin und BIM-Koordinatorin, veröffentlicht als [Praxiswissen auf bimwired.com](https://bimwired.com/landing/wissen/). Die Werkzeuge rechnen mit denselben Regeln wie das Werkzeug BimWired.

## Was drin ist

- **12 Fachartikel und Checklisten**: Stromkreise in Revit aufteilen, Verteilerplan und Stromlaufplan nach DIN EN 61082-1, VDE-Regelprüfung, Leistungsbilanz nach DIN 18015-1, Revit-Familienbibliothek für TGA, Familien definieren statt modellieren, Software-Vergleich.
- **3 Praxisszenarien** mit offenen Annahmen und Beispielrechnungen.
- **Glossar** mit 14 Begriffen von BCF bis Spannungsfall.
- **MCP-Server** `https://mcp.bimwired.com/mcp` (Streamable HTTP, keine Anmeldung, nur lesend) mit neun Werkzeugen:
  - `katalog_ifc`, `katalog_din276`, `katalog_parametergruppen`, `katalog_kategorien`: die Normkataloge, mit denen BimWired Familien klassifiziert.
  - `bibliothek_familien`, `bibliothek_familie`: die öffentliche Demo-Bibliothek mit Klassifizierung, Parametern und Typen.
  - `stromkreise_pruefen`, `stromkreis_vorschlag`: VDE-Plausibilitätsprüfung eines Stromkreisverzeichnisses (DIN VDE 0100-410/-430/-560/-701, DIN 18015-1) und ein Vorschlag für Sicherung, Kabel und Phasen.
  - `leistungsbilanz_rechnen`: Leistungsbilanz nach DIN 18015-1 Anhang A mit Sonderlasten, E-Mobilität, PV-Richtungsprüfung, NH-Empfehlung und vollständigem Rechenweg.

Jede Werkzeugantwort trägt die Felder `quelle` und `weiter`. Nichts wird gespeichert; der Server liest nur die Demo-Firma.

## Verbinden

**ChatGPT:** Plugin „BimWired Elektroplanung Revit" im Plugin Directory, sobald die Prüfung durch OpenAI abgeschlossen ist.

**Claude Code:**

```bash
claude mcp add --transport http bimwired https://mcp.bimwired.com/mcp
```

Dazu den Ordner `skills/elektroplanung-in-revit/` nach `~/.claude/skills/` oder `.claude/skills/` im Projekt legen: er ist das Handbuch, das dem Modell sagt, wann es welches Werkzeug ruft.

**Cursor, Codex und andere MCP-Hosts:** den Server mit der URL oben als HTTP-MCP eintragen (`.mcp.json` in diesem Ordner zeigt das Format) und den Skill-Ordner in den Skill-Pfad des Werkzeugs kopieren.

**Ohne Host, zum Ausprobieren:**

```bash
curl -s https://mcp.bimwired.com/mcp -H "Content-Type: application/json" -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"katalog_ifc","arguments":{"suche":"Steckdose"}}}'
```

## Grenzen

Alle Ergebnisse sind Planungsgrundlagen mit Normbezug. Verbindlich bleiben die TAB und die Anschlusszusage des Netzbetreibers. Nicht geprüft werden Spannungsfall, Strombelastbarkeit nach Verlegeart und Häufung, Selektivität und Kurzschlussfestigkeit; das bleibt Ingenieurleistung. Je Sitzung und insgesamt gilt eine Obergrenze an Aufrufen pro Minute.

## Mitwirken

Fehler in einem Artikel oder einer Regel: Issue in diesem Repository oder E-Mail an info@bimwired.com. Die Artikel werden aus den Quelltexten auf bimwired.com generiert; Korrekturen landen deshalb zuerst dort und dann hier. Der Quellcode des MCP-Servers liegt im Produkt-Repository von BimWired (`src/BimLibrary.McpRemote`).

## Lizenz

Texte unter `references/`: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de), Rowan Hamid / BimWired. Alles andere in diesem Ordner: MIT. Siehe `LICENSE`.

Herausgeber des Skills: Andreas Hauber. Produkt und Marke BimWired: Rowan Hamid, [bimwired.com](https://bimwired.com).
