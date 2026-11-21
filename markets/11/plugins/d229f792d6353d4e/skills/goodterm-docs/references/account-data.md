# Konten, Meldungen und Daten

## Konto und Anmeldung

Öffnen Sie das Kontomenü über die avatar/name in der Navigation. Es listet die bei diesem Client angemeldeten Konten auf, markiert den aktuellen und lässt den Benutzer wechseln oder ein Konto hinzufügen. Records, Gespräche, Kontoeinstellungen und Agentenberechtigungen bleiben für jedes Konto getrennt. Überprüfen Sie dieses Menü, wenn erwarteter Inhalt fehlt.

[Einstellungen → Konto](https://app.goodterm.net/settings/account) ( **Einstellungen → Konto** ) bearbeitet Profilinformationen, einschließlich Name, Benutzername und E-Mail-Adresse. Unter **Einstellungen → Konto** gibt es eigene Bereiche für **Anmeldemethoden**, **Passkeys** und **Passwort & Sitzungen**. Folgen Sie dem gezeigten Verifizierungsfluss; verfügbare Kontrollen hängen von den Methoden des Kontos ab. Das Abmelden aller Geräte unter **Passwort & Sitzungen** umfasst dieses Gerät. Dies unterscheidet sich von dem Abmelden von Konten auf dem aktuellen Client über das Kontomenü.

### Verbinden eines Google- oder GitHub-Anmelders

Um Google oder GitHub zu einem bestehenden Goodterm-Konto hinzuzufügen, melden Sie sich zuerst mit einer bestehenden Methode an. Wählen Sie in **Einstellungen → Konto → Anmeldemethoden** die Aktion **Google verbinden** oder **GitHub verbinden**, folgen Sie der Eingabeaufforderung zur Kontobestätigung und fahren Sie mit der Anmeldung des Anbieters fort. Nach der Rückkehr bestätigen Sie den Anbieter und das Goodterm-Konto. Eine übereinstimmende E-Mail-Adresse allein verknüpft keine Konten. Ein normaler Anbieter, der sich mit einer nicht verknüpften Identität anmeldet, dessen verifizierte E-Mail bereits zu einem Goodterm-Konto gehört, wird abgelehnt und weist auf die bestehende Anmeldemethode hin; es wird kein doppeltes Konto für diese E-Mail erstellt. Ein neues Konto kann erstellt werden, wenn die verifizierte E-Mail nicht verwendet wird. Die E-Mail des Anbieters kann sich von der Goodterm-E-Mail bei expliziter Verbindung unterscheiden; die Verbindung ändert nicht die E-Mail, das Passwort oder das Girokonto von Goodterm. Eine Identität, die bereits mit einem anderen Goodterm-Konto verbunden ist, kann auf diese Weise nicht übertragen werden.

Der Verbindungsversuch erfordert eine kürzliche Anmeldung und läuft nach fünf Minuten ab. Wenn er abläuft, ändert sich das Konto oder die App fordert die Authentifizierung an, melden Sie sich erneut bei dem beabsichtigten Konto an und starten Sie einen neuen Versuch. Das Abbrechen lässt die Konten unverlinkt. Eine ältere Windows-App benötigt möglicherweise ein Update, um den Rückfluss zu unterstützen. Die Verbindung eines Anmeldeanbieters ist getrennt von der Gewährung eines externen AI-Clients Record Zugriff unter **Einstellungen → Externe Agenten**.

Ein angeschlossener Anbieter bietet **Disconnect**, mit einer separaten Bestätigung. Goodterm erfordert eine andere ausreichende Möglichkeit, sich anzumelden; folgen Sie den angezeigten Anforderungen, anstatt die zuletzt verwendbare Methode zu entfernen. Disconnecting behält die Records und bestehende Sitzungen des Kontos. Konten ohne Passwort finden die Aktion **Passwort einrichten** unter **Anmeldemethoden** oder im Trenndialog. Dafür sind eine kürzliche Anmeldung und eine bestätigte Konto-E-Mail erforderlich. Einrichten eines Passworts trennt den Anbieter nicht. Ein vorhandenes deaktiviertes Passwort wird stattdessen durch seine Anmeldemethode aktiviert.

## Tier-Vorteile und Nutzungsbudget

[Einstellungen → Chatkontingent](https://app.goodterm.net/settings/usage) (**Einstellungen → Chatkontingent**) zeigt die Tier-Vorteile des Girokontos, die monatliche Chat-Nutzung und den nächsten Reset an. Tier-Vorteile sind kumulativ für Free, Basic und Plus. Verfügbare Modelle und Budgetbeträge hängen von der aktuellen Konfiguration des Kontos ab; verwenden Sie die angezeigten Werte, anstatt eine dauerhafte Berechtigung oder einen Preis anzugeben.

Die Nutzungsleiste unterscheidet die abgeschlossenen Ausgaben vom Budget, das für noch laufende Arbeiten reserviert ist. Reservierungen können sich ändern, wenn die Arbeit abgeschlossen ist. Wo verfügbar, gliedert sich die seite nach modell und trennt den chat von der forschung. Verschiedene Modelle und Forschung können unterschiedliche Mengen verbrauchen; ein Prozentsatz ist keine feste Anzahl von verbleibenden Nachrichten. Wenn das Budget eine neue Antwort blockiert, überprüfen Sie den aktuellen Status und die Reset-Zeit, anstatt zu versprechen, dass ein sofortiger Wiederholungsversuch erfolgreich sein wird.

Das Modellmenü des integrierten Chats zeigt eine kompakte Budgetübersicht. Die Modellauswahl ist in `references/chat.md` beschrieben. Externe MCP-Clients erhalten keine Tools zum Ändern des Kontos, des Budgets oder des eingebauten Chat-Modells. Diese Einstellungen gewähren keine Record-Berechtigungen.

## Benachrichtigungen

Öffnen Sie [Einstellungen → App → Benachrichtigungen](https://app.goodterm.net/settings/notifications) (**Einstellungen → App → Benachrichtigungen**) und aktivieren Sie Benachrichtigungen, indem Sie dem Browser oder der Android-Berechtigungsaufforderung erlauben.

Einmal aktiviert, kann der Benutzer **Abgeschlossene Antworten**, **Gescheiterte und unterbrochene Antworten**und **Chat-Titel und Textvorschau**anzeigen. Textvorschau steuert, ob Benachrichtigungstext Inhalt enthält; es deaktiviert die Benachrichtigung nicht selbst. Android verbirgt Inhalte auf dem Sperrbildschirm; ein Browser kann die Vorschau auch dort anzeigen.

Benachrichtigungen werden pro Konto auf diesem Gerät konfiguriert; aktivierte Konten, die angemeldet bleiben, können nach einem Kontowechsel immer noch Benachrichtigungen erhalten. Versprechen Sie keine kontoweite Synchronisierung. Die system/browser-Berechtigung muss dort verweigert werden, bevor Goodterm Benachrichtigungen liefern kann. Auf iPhone und iPad muss die Web-App zuerst auf dem Home Screen hinzugefügt werden.

## Datenexport

Unter [Einstellungen → Daten & Datenschutz](https://app.goodterm.net/settings/data) lädt **Daten exportieren** ein Goodterm-ZIP herunter. Darin liegen Records als Markdown sowie Gespräche, Nachrichten und Einstellungen als JSON. Das Archiv enthält auch den Versionsverlauf der Records, frühere Freigaben und Tool-Aufrufe. Für Goodterm-ZIPs bietet die App den Export an. Du kannst die Datei entpacken und ihre Inhalte außerhalb von Goodterm lesen und aufbewahren.

## Kontolöschung

Die Kontolöschung wird unter **Einstellungen → Konto** angeboten und verwendet einen E-Mail-Bestätigungsfluss. Es löscht das Konto und die zugehörigen Daten dauerhaft; es ist getrennt von der Löschung eines einzelnen Record in den Papierkorb.
