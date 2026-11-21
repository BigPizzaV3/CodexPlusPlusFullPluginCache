# Finden und Organisieren von Records

## Suchen und Filtern

Verwenden Sie die Suche in der Record-Liste und ihren Filtersteuerungen. Die Liste kann nach Autor, Zeitbereich, Favorit, Pinned und AI-geschütztem Status filtern und nach Erstellung, letztem Update oder letzter angezeigter Zeit sortieren. Die zuletzt betrachtete Sortierung zeigt Records an, die geöffnet wurden. Aktive Filterpillen können entfernt oder Filter zurückgesetzt werden. Gespeicherte Listenfilter sind lokal für das Gerät und das Konto.

Der Autorfilter ist standardmäßig für alle Autoren. Wenn ein vom Assistenten erstelltes Record durch eine gespeicherte Auswahl ausgeblendet wird, wechseln Sie zu allen Autoren, Agenten oder dem entsprechenden Agenten. Überprüfen Sie auch die aktive Suche und andere Filter. Diese Ansichtsfilter ändern keine Zugriffsberechtigungen und gelten nicht automatisch für MCP-Tools. Eine Suche ohne nützliche Ergebnisse beweist nicht, dass es kein passendes Record gibt.

Wenn ein Record zu fehlen scheint, überprüfen Sie zuerst das beabsichtigte Konto, dann suchen und filtern, dann Müll. Eine leere gefilterte Liste stellt keine Löschung dar.

## Favoriten, Pins und Multiple Selection

Das Aktionsmenü eines Record ermöglicht dem Benutzer add/remove sein Lieblings-Flag, pin/unpin es, KI-Schutz umzuschalten, seinen Inhalt oder Link zu kopieren, den Verlauf zu öffnen und zu löschen. Favoriten- und Schutzindikatoren zeigen die Flags an; verwenden Sie das Menü, um sie zu ändern. Anheften und Bevorzugen sind separate Flags mit separaten Listenfiltern. AI-Schutz ändert den Assistentenzugriff; seine Grenzen sind in `references/access.md`.

Wählen Sie den Auswahlmodus aus der **Wählen**-Aktion von Record aus und wählen Sie dann weitere Records aus. Auf dem Desktop geht Ctrl/Cmd-click auch in den Auswahlmodus über; nachfolgende Klicks schalten die Auswahl um. Ctrl/Cmd + Shift-Klick wählt einen Bereich aus dem Auswahlanker aus. Die Auswahlsteuerung unterstützt Favoriten-, Pin- und Schutzänderungen und Löschung. Bei gemischten Flags aktiviert der gemeinsame Umschalter das Flag für alle ausgewählten Records; wenn alle es bereits haben, entfernt er es. Überprüfen Sie gemeldete Fehler, wenn eine Batch-Operation nur teilweise erfolgreich ist. Zum Besprechen von Record-Inhalten im Chat siehe `references/chat.md`.

## Korrigieren eines Autors von Record

Wählen Sie **Änderung Autor** (**Autor Änderung**) in einem aktiven Aktionsmenü von Record, dann wählen Sie den Besitzer, Goodterm oder einen anderen verfügbaren Agenten. Der aktuelle Autor ist markiert; ein beibehaltener inaktiver Autor kann angezeigt bleiben, kann aber nicht neu zugewiesen werden. Die Änderung behält den Inhalt und den Inhaltszeitstempel des Record bei und kann ändern, ob er mit einem Autorenfilter übereinstimmt. Wenn er aus der aktuellen Liste verschwindet, überprüfen Sie diesen Filter.

Dies ist eine explizite Korrektur durch den Kontoinhaber, einschließlich für eine geschützte Record. Gewöhnliche Assistentenbearbeitungen ändern die Urheberschaft nicht, und die MCP-Tools können sie nicht neu zuweisen. Autorschaft zeichnet einen zugewiesenen Ursprung auf, nicht den Nachweis, dass der Eigentümer mit jeder Passage einverstanden ist.

## Löschung und Abfall

Zum Löschen öffnest du das Aktionsmenü des Records und verschiebst ihn in den Papierkorb. Die App kann dir direkt danach anbieten, die Aktion rückgängig zu machen. [Einstellungen → Papierkorb](https://app.goodterm.net/settings/trash) (**Einstellungen → Papierkorb**) stellt separate Listen für Records und Gespräche bereit, mit Wiederherstellungs- und permanenten Löschaktionen, einschließlich Mehrfachauswahl. Ein Record-Autorenfilter kann auch die Papierkorbliste beeinflussen; alle Autoren auswählen, wenn ein erwarteter Eintrag ausgeblendet wird.

Ein Record kann wiederhergestellt werden, während es im Müll bleibt. Permanente Löschung unterscheidet sich vom Umzug in den Müll; Versprechen Sie keine Wiederherstellung nach dieser Aktion. Kontodaten und Agent-Berechtigungen sind über Konten hinweg getrennt.

## Direkte Record Links

Jeder gespeicherte Record hat einen stabilen `https://app.goodterm.net/r/<key>`-Link. **Kopieren Sie den Link** (**Link kopieren**) in seinem Menü Kopien, die Adresse; **Kopieren Sie** kopiert den Inhalt. Das Kopieren eines Links macht den Record nicht öffentlich oder erteilt seinem Empfänger Berechtigungen. Geschützt Records kann immer noch Links haben, aber Agenten können sie nicht lesen.

Die Browseradresse folgt dem geöffneten Record, und Back/Forward besucht bewusst geöffnetes Records, nachdem anstehende Bearbeitungen gespeichert wurden. Ein neues ungespeichertes Record erhält seinen Link bei seinem ersten erfolgreichen Speichern, ohne den Entwurf zu ersetzen oder die Bearbeitungsposition zurückzusetzen.

Goodterm öffnet seine eigenen Record-Links innerhalb der aktuellen App. Ein direkter Link hat Vorrang vor der Wiederherstellung des letzten Record. Die Seitenleiste zeigt den Record an, wenn er zur aktuellen Ansicht gehört. Suche und Filter bleiben unverändert; **Zeigen Sie in der Liste Zeigen** (**In der Liste Zeigen**) löscht sie und kehrt zur Standarddatumsreihenfolge zurück, wenn der Record ausgeblendet wird.

### Einen Link im Browser öffnen

Ohne eine Sitzung zeigt die Record-Seite **Anmeldeanforderungen** (**Anmeldung**). Wählen Sie **Sign in**, um sich zu authentifizieren und zu diesem Record zurückzukehren. Verwenden Sie das Besitzkonto; die URL allein ist kein Aktienzuschuss.

**Record nicht verfügbar** (**Record nicht verfügbar**) deckt fehlende Records und Records nicht zugänglich für das angemeldete Konto. Es beweist nicht die Löschung. Überprüfen Sie das Girokonto und gegebenenfalls den Papierkorb; **Gehen Sie zu meinem Records** kehrt zum Arbeitsbereich zurück. Ein technischer Ladefehler bietet **erneut** für den gleichen Link. Es wird kein Record-Inhalt in diesen Zuständen angezeigt.

### Link zu einem externen Agenten geben

Ein externer MCP-Client kann den Link des Benutzers direkt an `get` übergeben, indem er `url` anstelle von `ids` verwendet. Absolute Links aus der verbundenen Goodterm-Bereitstellung und den relativen `/r/<key>`-Pfaden werden unterstützt. Geben Sie genau eine von `url` oder `ids` an; holen Sie die Adresse nicht als öffentliche Webseite ab oder versuchen Sie, aus dem Schlüssel auf Record-Inhalte zu schließen. Die Anmeldeinformationen eines verbundenen Agenten werden von MCP verwendet, nicht von einem gewöhnlichen Webabruf.

Ein erfolgreiches Ergebnis liefert den erlaubten Text und ein kanonisches `url` für Zitate. `offset`, `nextOffset` und `expectedRevision` funktionieren wie für eine einzelne Record ID. Nur den tatsächlich zurückgegebenen Inhalt melden. Linkfehler unterscheiden:

- `FORBIDDEN`: dem angeschlossenen Zugriff fehlt die Leseberechtigung. Der Besitzer kann sie in [Einstellungen → Externe Agenten](https://app.goodterm.net/settings/agents) (**Einstellungen → Externe Agenten** ) anpassen.
- `NOT_FOUND`: Der Record ist nicht verfügbar oder nicht zugänglich. Dies umfasst bewusst geschütztes, fremdkonto, gelöschtes und unbekanntes Records, ohne zu unterscheiden, welche Bedingung zutrifft.
- `INVALID_ARGUMENTS`: Der Link oder die Argumente werden nicht unterstützt; Verwenden Sie **Kopieren Sie den Link** in Goodterm und liefern Sie diesen Link, ohne ihn mit `ids` zu kombinieren.

Bestehende Lesevorgänge von `ids` geben unzugängliches IDs in `notFound` zurück, anstatt den gesamten Batch zu versagen. Keine der Antworten beweist, dass ein Record gelöscht wurde. Siehe `references/access.md` für AI-Schutz und Live-Berechtigungen.
