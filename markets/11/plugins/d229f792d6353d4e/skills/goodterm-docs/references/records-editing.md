# Schreiben und Speichern von Records

## Bearbeiten und Formatieren

Öffnen Sie ein Record aus der Liste, um es zu bearbeiten, oder starten Sie ein neues Record und schreiben Sie es. Ausgewählter editierbarer Text bietet eine Formatierungsleiste. Verfügbare Befehle umfassen fett, kursiv, Strikethrough, Code und Links; Blockbefehle enthalten Überschriften, Listen, Anführungszeichen und Codeblöcke. Wenn Sie `/` an einer Wortgrenze eingeben, wird die Befehlspalette auf Bearbeitungsflächen geöffnet, die sie unterstützen; ein Schrägstrich innerhalb eines Wort- oder Codeblocks bleibt gewöhnlicher Text.

Das Block-Typ-Steuerelement öffnet Text- und Blockoptionen; auf dem Handy ist es mit **Text** gekennzeichnet, während der Desktop den aktuellen Blocktyp anzeigt. Das **…**-Menü enthält weitere Formatierungen. Auf dem Handy sind Link, Strikethrough und Copy in diesem Menü, um Raum für Touch-Ziele zu lassen. Der Chat-Entwurf bietet auch Formatierungen, wenn editierbarer Text ausgewählt wird; dies unterscheidet sich von der Auswahl einer bereits gesendeten Nachricht, die quote/save-Aktionen bietet.

Lokales Undo/Redo arbeitet mit Bearbeitungen im aktuellen Editor. Das Auswählen von Text sendet ihn nicht zum Chat oder weist einen Assistenten an, ihn zu ändern. Das Speichern einer Passage aus schreibgeschütztem Text oder einer Chat-Nachricht wird in `references/chat.md` beschrieben.

Ein völlig leeres Record kann einen kontextbezogenen Schreibtipp anzeigen; dies ist ein Platzhalter, kein gespeicherter Inhalt. Das Anzeigeeinstellungs- und Auswahlverhalten ist in `references/interface.md` beschrieben.

## Frühere Fassungen wiederherstellen

Öffne **Versionsverlauf** im Menü des Records. Unter dem jeweiligen Datum siehst du jeden gespeicherten Stand mit Textvorschau, Bearbeiter und Uhrzeit. Klappe einen Stand auf, um seine Änderungen zu sehen. Über **Vollständige Fassung** kannst du den ganzen Text lesen. Über **Mehr laden** erreichst du ältere Einträge.

**Diese Fassung wiederherstellen** übernimmt nach Bestätigung den Text mit seiner Formatierung. Der Record behält seinen Link und der vorherige Inhalt bleibt im Verlauf erreichbar. Bei einem Konflikt prüfe den neuesten Eintrag, bevor du die Wiederherstellung erneut bestätigst. Nur der Kontoinhaber kann gespeicherte Fassungen lesen und wiederherstellen. Bei Records aus der Zeit vor Einführung dieses Verlaufs markiert **Ausgangsstand** die früheste verfügbare Fassung.

## Formatierung beim Tippen und Einfügen

Am Anfang eines Absatzes werden Präfixe im Markdown-Stil zur Formatierung, wenn Sie den folgenden Raum eingeben. Typ `-` und dann ein Leerzeichen, um eine Aufzählungsliste zu beginnen. Geben Sie `###` ein und dann ein Leerzeichen, um eine Überschrift der Ebene 3 zu beginnen. Der Raum löst die Konvertierung aus; die Symbole allein tun es nicht. Fahren Sie mit dem Listenelement oder dem Überschriftstext nach der Konvertierung fort. In ähnlicher Weise beginnt `1.`, gefolgt von einem Leerzeichen, eine nummerierte Liste, und ein bis vier `#`-Zeichen, gefolgt von einem Leerzeichen, wählen die entsprechende Überschriftebene aus.

Durch das Einfügen von Klartext mit erkanntem Markdown, wie z. B. `### Heading`, `- Item` oder `**bold**`, wird dieser ebenfalls in formatierten Inhalt umgewandelt. Diese automatische Markdown-Paste-Konvertierung gilt, wenn die Zwischenablage kein reichhaltiges HTML hat und sich der Cursor außerhalb eines Codeblocks befindet; gewöhnlicher Klartext bleibt Klartext. Rich-Text-Paste folgt einer eigenen Formatierung, und Code-Block-Paste bewahrt Text.

## Markdown für gespeicherte Records

`create` und `update` nehmen den Record-Text als Markdown entgegen. Übernimm ausdrücklich vorgegebenen Text wortgetreu. Wenn du selbst einen Record verfasst, genügt für einen kurzen Gedanken ein Absatz. Ein Titel ist optional. Setze Überschriften (`#` bis `####`) auf eigene Zeilen und trenne Absätze durch eine Leerzeile.

Verwende für einen Verweis auf einen anderen Record dessen zurückgegebene Referenz im Format `[[record:UUID]]`. Sie gehört in den Fließtext außerhalb von Inline-Code oder Codeblöcken. Für externe Webseiten verwende einen gewöhnlichen Markdown-Link.

## Formulas

Goodterm rendert die mathematische Notation LaTeX mit KaTeX. In einem editierbaren Record wählen Sie **Formel** (**Formel** ) aus dem **…**-Menü der Formatierungsleiste oder der `/`-Befehlspalette. Dies öffnet einen Dialog für eine Inline-Formel. Geben Sie den LaTeX-Ausdruck ohne umgebende Dollarzeichen ein, z. B. `\frac{a}{b}` oder `x^2`, überprüfen Sie die Vorschau und wählen Sie **Anwenden**. Ctrl + Enter (Cmd + Enter auf Mac) wendet ihn auch an. Klicken Sie auf eine vorhandene Formel, um ihn zu bearbeiten; der Dialog bietet auch Entfernung an. Sein Syntax-Hilfe-Link listet die unterstützte KaTeX-Notation auf; versprechen Sie keine Unterstützung für beliebige LaTeX-Dokumente

In Record Markdown stellt `$x^2$` eine Inline-Formel und `$$\frac{a}{b}$$` einen separaten Formelblock dar. Live-Typisierung hat verschiedene Verknüpfungen: `$$x^2$$` erstellt Inline-Mathematik und `$$$x^2$$$` am Anfang eines Absatzes erstellt Blockmathematik. Verwechseln Sie diese Eingabekürzel nicht mit der gespeicherten Markdown-Notation. Das Einfügen einer Formel allein ist kein garantierter Markdown-Konvertierungstrigger; Verwenden Sie den Formeldialog, wenn das Einfügen Dollarzeichen sichtbar lässt. Dollarzeichen im Code bleiben wörtlich.

## Code

Inline-Code für einen kurzen wörtlichen Ausdruck wie `count += 1`: Wählen Sie den Text und wählen Sie die Codeformatierungsaktion. Für mehrere Zeilen wählen Sie den **-Codeblock** aus dem Blocktypsteuerelement oder der `/`-Palette. Ein Codeblock bietet eine Sprachauswahl für die Syntaxhervorhebung und eine Schaltfläche zum Kopieren seines Inhalts. Formatierungscode führt ihn nicht aus.

In Markdown wickeln Sie Inline-Code in Backticks ein und verwenden Sie einen eingezäunten Block mit einem Sprachlabel für mehrere Zeilen, z. B.:

````markdown
```python
print("Hello")
```
````

Fügen Sie Rohcode in einen vorhandenen Codeblock ein, um ihn als Text zu erhalten. Um das eingezäunte Markdown-Beispiel als formatierten Inhalt einzufügen, fügen Sie es außerhalb eines Codeblocks als Klartext ein.

Vorhandene Mermaid-Diagramme erscheinen als bearbeitbarer Quelltext in Codeblöcken.

## Rechtschreibkorrektur

Wähle im Aktionsmenü eines ungeschützten Records **Rechtschreibung korrigieren** (**Correct spelling**). Der Befehl prüft den Text des gesamten Records und bietet nach einer Änderung **Rückgängig** an.

## Automatisches Sparen und Ausfällen

Record ändert sich automatisch nach einer kurzen Tipppause und auch während des anhaltenden Tippens. Das erste erfolgreiche Speichern gibt einen neuen Entwurf seines Record-Links, ohne die Cursor-, Auswahl- oder Bearbeitungsansicht zurückzusetzen. Normales Sparen ist ruhig: Das Fehlen eines anhaltenden Erfolgsabzeichens wird erwartet. Die automatische Speicherung erfordert weiterhin ein erfolgreiches Serverschreiben; nicht gespeicherter Text ist nicht im automatischen Record-Kontext des Assistenten enthalten.

Ein Save Failure zeigt eine Warnsteuerung im Editor an. Klicken Sie darauf, um es sofort zu wiederholen. Temporäre Verbindungs- oder Serverausfälle werden automatisch wiederholt, auch wenn die Verbindung zurückkehrt. Abgelehnte Speicher wie Berechtigungs- oder Validierungsfehler erfordern die Lösung des zugrunde liegenden Problems. Empfehlen Sie kein Neuladen als erste Korrektur für nicht gespeicherten Text oder versprechen Sie, dass jeder Entwurf das Schließen der App überlebt. Bevor Sie den neuesten Wortlaut im Chat besprechen, stellen Sie sicher, dass er gespeichert wurde, oder fügen Sie diesen Wortlaut direkt in die Nachricht ein.

## Konflikthafte Bearbeitungen

Wenn eine neuere Version von einem anderen Gerät oder einem Agenten kommt, während der Editor Änderungen nicht gespeichert hat, fragt Goodterm, wie der Konflikt gelöst werden soll, anstatt diese Änderungen stillschweigend zu ersetzen. Der Dialog bietet **Keep My Version** oder **Use Server Version**und kann die Unterschiede anzeigen.

**Meine Version behalten** speichert deine lokale Fassung. **Server-Version verwenden** übernimmt die gespeicherte Serverfassung in den Editor. Dies sind Wahlmöglichkeiten zwischen Versionen; beanspruchen Sie keine automatische Zusammenführung. Wenn beide nützliche Änderungen enthalten, helfen Sie dem Benutzer, den erforderlichen Wortlaut vor der Auswahl zu bewahren.
