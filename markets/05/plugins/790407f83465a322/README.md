# Aivana Dataverse App Architect

Diese Edition plant und prüft Dataverse-Apps anhand lokaler Dateien. Sie enthält keinen
MCP-Server und führt weder Anmeldung noch Provisionierung, Veröffentlichung oder
Deployment in einer Umgebung aus.

Python 3.11 oder neuer. Im entpackten Plugin-Verzeichnis:

```powershell
python scripts/validate_app_blueprint.py assets/order-entry.blueprint.json --json
python scripts/generate_specialist_pack.py assets/order-entry.blueprint.json --output specialist-pack
python scripts/validate_solution_against_blueprint.py assets/order-entry.blueprint.json path/to/unpacked --json
```

Der Exportvergleich erwartet tatsächlich exportierte, entpackte Solution-Dateien und
prüft deklarierte Tabellen, Spalten, Typen, Pflichtfelder, Beziehungen, Formulare,
Ansichten und Navigationsziele. Nicht unterstützte Custom Pages verlangen zusätzliche
Nachweise. Ein leerer oder ungültiger Blueprint führt zum Fehler.

Planungsskills können Betriebs- oder Deploymentabläufe beschreiben. Diese Edition
erstellt daraus ausschließlich lokale Pläne für einen autorisierten Betreiber.
Checklisten belegen keine durchgeführten Rollen-, Last- oder Accessibilitytests.

Synthetische Daten sind Vorschauen mit deterministischen IDs und reservierten
`example.invalid`-Adressen. Choice-Bezeichnungen benötigen vor einem Import die
tatsächlichen numerischen Optionswerte. Datei-/Bildinhalte werden nicht erzeugt.

Die Pipeline-Datei ist ein lokales Übergabeartefakt. Ihr Betrieb, Service Connections,
Umgebungsfreigaben, Veröffentlichung und fachliche Abnahme liegen außerhalb dieser Edition.
Das Paket enthält ein `release-integrity.json` mit SHA-256-Prüfsummen.
