# systolics für ChatGPT und Codex

Version 1.0.2 verbindet ChatGPT und Codex mit den freigegebenen Analysedaten Ihrer Organisation. Der Analytics-Skill unterstützt die Auswahl passender Modelle und Kennzahlen, Aufteilungen, Zeitverläufe, Ranglisten, Periodenvergleiche und Erklärungen von Berechnungen, SQL und Datenstrukturen.

## Voraussetzungen und Verbindung

Die Nutzung setzt einen bestehenden systolics-Lizenzvertrag, ein systolics-Konto, freigeschalteten MCP-Zugang und die erforderlichen Leserechte voraus. Installieren Sie das systolics-Plugin in ChatGPT oder Codex und verbinden Sie den systolics-Dienst über dessen OAuth-Anmeldung. Wählen Sie Ihre Organisation sowie die Freigaben **Cube-Daten abfragen** und für Metadaten **Datenstrukturen einsehen**. Kontoberechtigungen bleiben Voraussetzung; neue Freigaben können eine erneute Autorisierung erfordern.

Die Anmeldung erfolgt unter `https://auth.services.systolics.de`. Der MCP-Endpunkt ist `https://mcp.services.systolics.de/mcp`. Zugangsdaten gehören ausschließlich ins Anmeldefenster. Fehlende Tools oder Rechte lassen sich nicht durch Skill-Anweisungen ergänzen.

## Beispiele

- Welche Analysemodelle und Kennzahlen stehen mir zur Verfügung?
- Zeige eine passende Kennzahl als Monatsverlauf für das letzte vollständige Quartal.
- Vergleiche eine Kennzahl für zwei vollständige Quartale mit denselben Filtern.
- Welche zehn Gruppen haben den höchsten Wert dieser Kennzahl?
- Wie wird die Kennzahl berechnet? Erkläre das SQL und seine Parameter.
- Welche Datenstrukturen gibt es und welche Spalten enthält dieser Eintrag?

Der Skill prüft Member anhand des aktiven Katalogs. Beispiele sind keine feste Liste verfügbarer Modelle. Fachliche Mehrdeutigkeiten werden vor der Abfrage geklärt. Abfragen verwenden den aktuellen Cube-Vertrag mit `timeDimensions`; ein zusätzliches Serverupdate ist für dieses Paket nicht erforderlich.

## Funktionen und Daten

Die zehn Tools liefern Organisations- und bei Bedarf Benutzerkontext, Analysemodelle, Kennzahlen, Dimensionen, Query-Ergebnisse, erzeugtes SQL und Datenstruktur-Metadaten. Unterstützt werden Aggregation, Gruppierung, Zeitreihen, Filter, Sortierung, Paging und Vergleiche. Die Tools ändern keine Geschäftsdaten und bieten keine freie SQL-Ausführung. Die tatsächlich verfügbaren Daten hängen von Modellen und Berechtigungen ab.

Bei Tool-Aufrufen werden die benötigten Argumente und die autorisierten Ergebnisse zwischen ChatGPT beziehungsweise Codex und systolics übertragen. Kontext-Tools können Organisationsangaben sowie Name und E-Mail des angemeldeten Benutzers liefern. Benutzerinformationen werden nur bei entsprechendem Bedarf abgefragt. Die Plugin-Dateien enthalten Skills und Verbindungskonfiguration, keine Zugangsdaten oder eigene Datensammlung. Für die Verarbeitung gelten die Bedingungen der verbundenen Dienste und die [systolics-Datenschutzhinweise](https://systolics.de/rechtliches/datenschutz-anwendung/).

## Hilfe und Lizenz

Kontakt: [systolics](https://systolics.de/#kontakt), [hi@systolics.de](mailto:hi@systolics.de). Es gilt die [proprietäre Lizenz](LICENSE) auf Grundlage des bestehenden systolics-Lizenzvertrags und der darin einbezogenen [AGB](https://systolics.de/rechtliches/allgemeinebedingungen/).

## Entwicklung und Einreichung

Die Quelle dieses OpenAI-Pakets ist `C:\dev\systolics-openai-plugin`. Die fachliche Vorlage ist das akzeptierte Anthropic-Plugin 1.1.0; die OpenAI-Paketversion wird unabhängig geführt. `plugin.json` ist die Quelle für Listing, Version und Review-Fälle; `mcp.json` für die Verbindung. Der öffentliche Auth-Service unterstützt CIMD und PKCE; die Zustimmungsauswahl `cubeDataRead`/`metaDataRead` bezeichnet keine OAuth-Scopes.

Die technische OpenAI-Paketidentität ist `systolics`, passend zur aktuellen Einreichung im Plugins-Dashboard. Der Anzeigename ist ebenfalls `systolics`. Die Identität ist mit ihrer Herkunft in `review/portal-identity.json` festgehalten; der Validator gleicht `plugin.json.name` dagegen ab. Version 1.0.2 wird als neue Version dieser Einreichung hochgeladen. Das frühere Paket mit `app-6abb580b16a88191adadadeb9eb359a4` und der Sonderaufbau über `build_new_submission.py` gehören ausschließlich zur historischen Version 1.0.1.

In einer Python-Umgebung mit den Abhängigkeiten aus `scripts/requirements.txt`:

```sh
python3 scripts/validate_plugin.py
python3 scripts/build_plugin.py
```

Das Build erzeugt `dist/systolics-openai-1.0.2.zip` und die Prüfsumme. Das separate `skills/systolics-analytics.zip` wird aus derselben Skill-Quelle erzeugt. `chatgpt-app-submission.json` enthält geprüfte Tool-Begründungen als separate Formularhilfe; es ersetzt weder den MCP-Scan noch das portable Plugin-Manifest.

Der Ablauf und die tatsächlichen Prüfgrenzen stehen in `review/submission-1.0.2.md`. Reviewer-Zugangsdaten werden im sicheren Dashboard-Feld hinterlegt. Das lokale Bauen reicht noch keine Submission ein.
