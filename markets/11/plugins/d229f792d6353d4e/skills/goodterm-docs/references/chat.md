# Chat Kontext und gespeicherte Passagen

Ein leerer chat-entwurf kann einen kontextuellen tipp anzeigen, auch wenn sie eine bestehende konversation wieder öffnen. Aufzeichnungs- und Antwortinformationen haben Vorrang. Diese Hinweise werden nicht als Nachrichten gesendet; ihre Anzeigeeinstellung ist in `references/interface.md` beschrieben.

## Open Record

Sending a message in built-in chat includes the identity of the Record open in the editor. Wenn die Antwort beginnt, liest der Server seinen gespeicherten Inhalt, wenn Goodterm die Berechtigung zum Lesen hat. Nicht gespeicherte Edits sind nicht automatisch enthalten. Das Öffnen eines anderen Record nach dem Senden ändert nichts an dem für diese Nachricht ausgewählten Record.

Um ein offenes Record zu besprechen, lassen Sie es speichern, halten Sie es offen und fragen Sie im Chat. Besprechen Sie nur Inhalte, die tatsächlich erhalten wurden. Text, der explizit in den chat eingefügt wird, wird zu nachrichteninhalten, einschließlich nicht gespeicherter bearbeitungen. KI-Schutz entfernt keinen Text aus bereits gesendeten Nachrichten.

Referenzen wie z. B. `[[record:UUID]]` verbinden eine Konversation mit einem bestimmten Eintrag. Reservieren Sie echte zurückgegebene Referenzen außerhalb der Codeformatierung und erfinden Sie IDs nicht. Ein Verweis allein gewährt keinen Zugriff auf seinen Inhalt.

Ein externer MCP-Assistent erhält nicht automatisch den offenen Record, die Auswahl oder den Bildschirm. Geben Sie ihm einen Record-Link vom **Kopieren Sie den**, lassen Sie ihn eine erlaubte Suche durchführen oder geben Sie den Text an. Direkter MCP-Link-Abruf und seine Zugriffsnachrichten werden in `references/records-organizing.md` beschrieben.

## Bearbeiten des offenen Record durch Chat

Der Benutzer kann den eingebauten Assistenten bitten, das offene Record zu überarbeiten, beispielsweise einen Absatz zu verkürzen oder Überschriften hinzuzufügen. Dies erfordert eine zugängliche, gespeicherte Record und die Berechtigung, Records zu bearbeiten; siehe `references/access.md`. Das Öffnen eines Record allein ist keine Bearbeitungsanfrage. Behalten Sie den Wortlaut und den Umfang des Benutzers bei der Durchführung der angeforderten Änderung bei.

Wenn eine gespeicherte Änderung den geöffneten Editor erreicht, wird der Inhalt automatisch aktualisiert. Eingesetzter oder Ersatztext wird kurz grün hervorgehoben; Highlights erscheinen nacheinander und verblassen. Geänderte Codeblöcke leuchten. Der Editor versucht, zum ersten geänderten Standort zu scrollen, wenn er sich außerhalb des sichtbaren Bereichs befindet. Wenn die reduzierte Bewegung aktiviert ist, bleiben Texthighlights statisch und das automatische Scrollen wird übersprungen. Dieses visuelle Feedback zeigt bereits angewendete Änderungen, nicht einen Zeichen-für-Zeichen-Stream oder eine ausstehende Genehmigungsvorschau. Gelöschter Text wird nicht wieder als durchgestrichener Text angezeigt.

Wenn nicht gespeicherte lokale Bearbeitungen mit einer eingehenden Änderung in Konflikt stehen, fragt Goodterm, wie der Konflikt gelöst werden soll, anstatt sie stillschweigend zu ersetzen. Zur Konfliktbehandlung siehe `references/records-editing.md`.

## Starten eines Chats

Öffnen sie einen neuen chat-entwurf, schreiben sie die erste nachricht und senden sie sie. Geben Sie `/` ein, um Formatierungsbefehle zu öffnen. Die konversation wird erstellt, wenn diese erste nachricht gesendet wird; das öffnen eines entwurfs allein sendet keine anfrage. Um ein gespeichertes Record zu besprechen, halten Sie es wie oben beschrieben im Editor geöffnet. Um Passagen aus mehreren Records zu besprechen, fügen Sie den entsprechenden Text in Ihre Nachricht ein. Die Record-Liste bietet derzeit keine Auswahlaktion zum Starten eines Chats mit ausgewähltem Records.

Für Record-Auswahlsteuerungen und Filter lesen Sie `references/records-organizing.md`; für nicht verfügbaren Kontext lesen Sie `references/access.md`.

## Auswahl eines Modells

Im Menü **Chatmodell** am Eingabefeld stehen die für dein Konto verfügbaren Modelle. Die Modellauswahl gilt für dieses Gespräch. Für neue Chats merkt sich Goodterm die letzte Auswahl auf diesem Gerät. Wird das gewählte Modell für dein Konto gesperrt, kann Goodterm auf ein verfügbares Modell wechseln.

Das gleiche Menü zeigt verfügbare monatliche Budgetinformationen und Zeit bis zum Reset. Für Tiervorteile und die detaillierte Nutzungsaufschlüsselung öffnen Sie [Einstellungen → Chatkontingent](https://app.goodterm.net/settings/usage) (**Einstellungen → Chatkontingent** ); siehe `references/account-data.md`. Verwenden Sie die aktuellen Modellnamen und Erklärungen der App, anstatt eine feste Modellliste oder Preise zu versprechen. Diese Auswahl steuert den eingebauten Chat von Goodterm, nicht das Modell, das von ChatGPT oder einem anderen MCP-Client verwendet wird.

## Chats finden und eine Antwort wiederherstellen

Die chat-übersicht unterstützt suche, zeitfilter, favoriten, pins, sortierung und mehrfachauswahl. Es zeigt auch laufende arbeits- und reaktionsprobleme in anderen gesprächen. Öffnen sie den entsprechenden chat, um seinen aktuellen status zu überprüfen; das wechseln von chats stoppt nicht selbst eine antwort.

Eine fehlgeschlagene oder unterbrochene Antwort kann **Retry** und **Dismiss**anbieten. Retry startet einen weiteren Versuch für diese Anfrage; Dismissing entfernt die Wiederherstellungsbenachrichtigung lokal und löscht nicht die Konversation oder rückgängig macht Record Änderungen, die bereits erfolgreich waren. Lesen Sie zuerst die angezeigte Ursache: Budget- oder Berechtigungsfehler benötigen ihre entsprechende Abhilfe, und eine nicht verfügbare Wiederholungsaktion wird nicht durch wiederholtes Senden derselben Nachricht behoben.

## Zitieren und Speichern einer Passage

Das Auswählen von Text in einer Chat-Nachricht bietet eine Zitataktion, die die Passage in den Entwurf einfügt; der Benutzer sendet sie weiterhin. Eine Auswahl allein ist keine Anweisung.

Das Auswahlmenü für schreibgeschützten Text, einschließlich Chatnachrichten, bietet auch **Save as Record** (**Als Record speichern**). Es erstellt ein neues Record aus der ausgewählten Passage, wobei die ursprüngliche Nachricht oder Record intakt bleibt. Nach einem erfolgreichen Speichern können das Menü und das Erfolgsfeedback das neue Record öffnen. Auf dem Handy bietet das Menü auch Copy. Ein editierbares Record's Auswahlmenü bietet in erster Linie Formatierung; versprechen Sie keine Speicherauswahlaktion in jedem Editor.

Du kannst Goodterm auch ausdrücklich bitten, einen Text als Record zu speichern. Dafür braucht Goodterm die Berechtigung zum Erstellen von Records. Ein Formulierungswunsch allein ist kein Speicherauftrag.

## Recherche und Antwortlänge

Der eingebaute Assistent kann das zugängliche Records während der Beantwortung einer Frage erkunden. Der Benutzer kann die Frage, den relevanten Zeitraum, den bekannten Wortlaut oder die gewünschte Breite in der Nachricht beschreiben. Es gibt keine aktuellen **Gewünschte Forschungsdatensätze** Einstellung in der Benutzeroberfläche; leiten Sie den Benutzer nicht zu einem alten Schieberegler oder versprechen Sie eine feste Anzahl von Quellen.

Der Assistent kann einen internen Forschungsagenten bitten, Records zu erkunden. Es überprüft die Ergebnisse, bevor eine weitere Runde für eine ungelöste Frage beantragt wird. Spätere Runden suchen nach zusätzlichen Quellen. Die Forschung arbeitet innerhalb der Tool- und Verarbeitungsgrenzen der Antwort. Relevanz, verfügbares Material und technische Grenzen beeinflussen das Ergebnis. Weniger Quellen können eine Frage vollständig beantworten; eine begrenzte Suche stellt nicht fest, dass andere Records nicht existieren. Externe MCP-Clients verwenden ihre eigenen verfügbaren Record-Tools und -Workflows.

Fragen Sie in der Nachricht nach der gewünschten Antwortlänge oder Detailtiefe.

## Quellen einer Antwort

Der eingebaute Chat verwendet interne Rechercheagenten, um verwandte Records zu erforschen, und erstellt dann die Antwort aus ihren Beweisen. Die **History** (**Verlauf**) zeigt seine aufgezeichnete Werkzeugaktivität. Erweitern Sie einen Werkzeugschritt, um verfügbare Suchanfragen, Record-Links und Auszüge zu inspizieren. Forschungsagent-Schritte können erweitert werden, um verfügbare Suchanfragen und Lesevorgänge zu inspizieren. Dies sind begrenzte Vorschauen, nicht unbedingt vollständige Records oder ein Transkript der Argumentation des Modells. Ältere Geschichte kann diese Details fehlen.

Eine Suche kann relevantes Material verpassen. Wenn ein bestimmter Eintrag wichtig ist, öffnen Sie ihn für die nächste Nachricht oder geben Sie seine tatsächliche Referenz an. Unterscheiden Sie eine ursprüngliche Passage von der vorgeschlagenen Verbindung eines Assistenten.

Instruction-Änderungen verwenden die gleichen separaten Genehmigungseinträge mit einem erweiterbaren before/after-Vergleich. Eine Entscheidung aktualisiert den bestehenden Eintrag, ohne eine automatische Chat-Antwort hinzuzufügen.
