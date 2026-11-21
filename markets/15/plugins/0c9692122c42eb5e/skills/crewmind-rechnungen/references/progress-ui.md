# CrewMind-Fortschrittsanzeige

## Native Tool-Karten

Nach Bereitstellung des CrewMind-MCP-Proxys 1.1.0 liefert `https://mcp.crewmind.io/mcp` die HTML-Ressourcen und UI-Metadaten zu den bestehenden Rechnungs-Tools. Ein unterstützender Host kann die Karten bei deren normalen Aufrufen anzeigen. Die Plugin-ZIP allein installiert diese Server-Ressourcen nicht. OAuth, Kontoberechtigungen, Berechnungen und sämtliche Regeln des Hauptskills bleiben erforderlich.

Die Karte verwendet die vom Host gelieferten Tool-Eingaben und Ergebnisse sowie Fehler- und Abbruchereignisse. Eine Ladeanimation kennzeichnet einen tatsächlich ausstehenden Aufruf; sie erzeugt weder Prozentwerte noch eine erfundene Restzeit. Der Host bestimmt den Zeitpunkt der Darstellung. Er kann pro Tool-Aufruf eine eigene Karte anzeigen und muss die Karte nicht schon vor dem Ergebnis öffnen. Fehlt UI-Unterstützung, berichte dieselben belegten Zustände im Chat.

## Namen und Zähler

Wenn das tatsächliche Tool-Schema das optionale Feld `uiContext` anbietet, ergänze vorhandenen Kontext automatisch. Erfinde für die Anzeige keine Argumente und starte dafür keine zusätzlichen MCP-Aufrufe.

- `label`: höchstens 100 Zeichen; aktuelle Phase und gegebenenfalls der bereits bekannte ausgewählte Account. Keine IDs, vollständigen Profildaten, Zugangsdaten oder Download-Links.
- `position`: ganze Zahl ab 1; aktuelles Element innerhalb des bekannten, ausgewählten Umfangs derselben Phase.
- `total`: ganze Zahl ab 1; Umfang dieser Phase, nur wenn eindeutig bekannt. Eine zurückgegebene oder gefilterte Profilliste ist keine globale Zahl aller abrechnungsfähigen Konten.
- `completed`: ganze Zahl ab 0; vor diesem Aufruf tatsächlich erfolgreich abgeschlossene Elemente derselben Phase. Vorschauen, Erstellungen und Versand haben getrennte Zähler. Nach einem Fehler gilt ein Element nicht als abgeschlossen.

Lass unbekannte Felder weg. Die Proxy-Verbindung entfernt `uiContext` vor der Weiterleitung an den bestehenden Rechnungsserver; es ist ausschließlich Anzeigekontext. Benenne im Chat die Bezugsgröße der Zähler. `total` und `done` aus `member_invoice_setup` beschreiben gefundene Member beziehungsweise bereits vorhandene Monatsrechnungen. Sie sind keine in diesem Lauf neu erstellten Rechnungen. Die Zahl zurückgegebener Creator-Profile belegt weder vollständige Daten noch eine Erstellungsfreigabe für alle Profile.

Zeige „Angaben fehlen“, solange notwendige Eingaben fehlen. Ein erfolgreiches Setup, eine geladene Liste oder ein beendeter Aufruf allein bedeutet nicht „Alles bereit“. Rechnungsbeträge stammen ausschließlich aus Tool-Ergebnissen. Warnungen werden weiterhin wörtlich im Chat angezeigt; die Karte ersetzt weder deren Darstellung noch Vorschau und ausdrückliche Bestätigung vor jedem Erstellen oder Senden.

## Stoppen

„Stopp anfragen“ sendet über den Host eine Nutzer-Nachricht an den Chat. Der Knopf ruft kein Rechnungs- oder Abbruch-Tool auf und bestätigt keinen Serverabbruch. Erst ein tatsächlich empfangener Stop-Wunsch beendet die weitere Aufrufplanung. Für einen laufenden Ablauf steht außerdem der native Stopp des Hosts zur Verfügung. Schon übermittelte Aktionen können dennoch abgeschlossen werden; ein unklarer Ausgang bleibt als solcher sichtbar und wird nach neuer Nutzeranweisung über die vorhandenen List-Tools geklärt.

Es gibt keine zusätzlichen Dienste, Hintergrundabfragen oder dauerhafte UI-Speicherung. Speichere keine vollständigen Tool-Ergebnisse, Zugangsdaten oder kurzlebigen Download-Links für die Anzeige. Bei 401, 403 oder „nicht freigegeben“ stoppt der Ablauf ohne alternativen Zugriff. Ein OAuth-Fehler wird durch das Widget nicht behoben.

## Optionale Design-Demo

Die beibehaltene Vorlage `assets/progress-demo.html` ist ausschließlich eine „Demo · Ablaufwiedergabe“. Zeige sie auf ausdrücklichen Wunsch in einem unterstützten Visualisierungshost; sie ist nicht die native Live-Karte.

Für eine Momentaufnahme dürfen nach erfolgreichen, erlaubten Aufrufen ausschließlich belegte Aggregate in eine Kopie der Vorlage eingesetzt werden: `memberTotal`, `memberDone`, `creatorProfiles`, `period`, `checkedAt` und gegebenenfalls ein tatsächlich geprüftes `ratesChecked`. Unbekannte Werte bleiben `null`. Eine optionale Vorschau verwendet nur vom Tool gelieferte Beträge und Warnungen; ausdrücklich fiktive Eingaben sind mit `syntheticInputs: true` zu kennzeichnen. Fehlende Daten werden nicht für eine vollständige Demo ergänzt. Nach einer Ablehnung keine erfolgreiche Demo abspielen.

Ändere ausschließlich den JSON-Block `crewmind-demo-data`, setze `kind` auf `snapshot` und ersetze `<` beim Einbetten durch `\u003c`. Behalte die Darstellung per `textContent` bei. Speichere keine IDs, vollständigen Profile, Zugangsdaten oder Download-Links; bei entsprechenden Warnungsinhalten verwende nur die zulässige Textausgabe. Die Animation spielt abgeschlossene Ergebnisse nach. „Demo stoppen“ hält ausschließlich diese Wiedergabe an.
