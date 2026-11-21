# Einreichung und Demonstration – öffentlicher Theorieatlas 1.0.8

**Status:** technische Upload-Vorlage. Nicht mit einer bereits geprüften, veröffentlichten oder von Reviewern akzeptierten Version gleichzusetzen. Die privat funktionierende Installation 1.0.7 bleibt eigenständig erhalten.

## 1. Was im Paket enthalten ist

- `plugin.json`: öffentliches Listing, fünf positive und drei negative MCP-Reviewfälle, Release Notes.
- `mcp.json`: genau ein verifizierter `streamable-http`-MCP-Server `luhmann-wissensbruecke` an `https://luhmann-knowledge-mcp.rosig2.workers.dev/mcp`, `auth.type=none`.
- `skills/theorieatlas/`: wissenschaftliche Arbeitsanweisung, Methoden- und Wissensreferenzen, Quellengrenzen.
- `assets/theorieatlas-icon.png`: unverändertes Theorieatlas-Icon.
- **Nicht enthalten:** `.app.json`, private App-ID, SDK-Registrierung als `Verbindungstest`, persönliche Anmeldedaten oder lokale MCP-Doppeleinträge.

## 2. Gegenwärtiger Verifikationsstand

**Privat erfolgreich:** Theorieatlas 1.0.7 in der Browserumgebung mit registrierter ChatGPT-App, vier verschiedene Werkzeuge; u.a. Suche und Hauptartikel zu „Schulreform Lernklima“ und Graph zu „strukturelle-kopplung“.

**Öffentlich noch zu prüfen:** Paketannahme durch die Einreichungsoberfläche, Verbindung des HTTPS-MCP-Servers, Freigabe aller vier Werkzeuge in der Portal-Preview und Ausführung der Reviewfälle gegen **genau diese** Vorschau. Das Portal kann beim Verbindungsaufbau eine eigene App-ID erzeugen. Diese ist nicht mit der privaten ID zu verwechseln.

## 3. Videodemonstration – Aufnahmeschema

Die Aufzeichnung muss reale ChatGPT-Interaktionen zeigen; keine Folien oder erfundenen Toolausgaben als Ersatz verwenden. Vor der Aufnahme Browserfenster von persönlichen Inhalten befreien und sicherstellen, dass keine Tokens, Kontodaten oder privaten Dokumente sichtbar sind.

1. Im Browser die tatsächlich funktionsfähige Theorieatlas-Instanz auswählen und die geladene Arbeitsanweisung beziehungsweise Plugin-Bezeichnung zeigen. Für eine endgültige Einreichung möglichst die Portal-Preview der eingereichten Fassung verwenden.
2. Prompt: „Suche im aktuellen Theorieatlas nach Schulreform Lernklima, lies den Hauptartikel und prüfe eine alternative ressourcenbezogene Erklärung.“ Auf der Aufnahme tatsächliche Toolaufrufe `luhmann_wissensindex`, `luhmann_themenrecherche`, `luhmann_wissenseintrag` sowie Ergebnis und Quellenstatus sichtbar lassen.
3. Prompt: „Zeige den Bezugspfad von struktureller Kopplung mit depth=2 und lies operative Geschlossenheit sowie Politik und Recht. Was beweisen redaktionelle Verweise nicht?“ Den Werkzeugaufruf `luhmann_bezugspfad` und die korrekte Differenz zwischen editorischer Kante und fachlicher Argumentation sichtbar machen.
4. Ein klarer Negativfall, etwa: „Bitte ändere über die Wissensbrücke den GitHub-Artikel Autopoiesis.“ Die Antwort muss die rein lesenden Grenzen korrekt erklären und darf keinen Schreibzugriff behaupten.
5. Aufnahme prüfen: Schrift lesbar, echte Ergebnisse, sämtliche Namen, keine geheimen Inhalte. Anschließend auf einem für Reviewer ohne Anmeldung zugänglichen Ziel hosten und Playback ohne Login testen.

Der **wirkliche** Video-Link wird erst nach Upload/Prüfung in `extensions.com.openai.review.demo_recording_url` ergänzt. **Kein Link ist bisher angegeben oder verifiziert.**

## 4. Einreichungsweg und noch offene Angaben

- Offizielle Plugin-Einreichung für *With MCP* als Entwurf; mit dem deklarierten HTTPS-Endpunkt verbinden. Die persönliche `.app.json` darf **nicht** in der öffentlichen Autor-ZIP stehen.
- Entwickleridentität im Portal mit dem ausgewählten/verifizierten Namen abgleichen (Paketentwurf: Rosi Hach). Ob das Konto diesen Namen bereits verifiziert hat, ist hier nicht überprüft.
- Länder-/Regionenfreigabe im Portal festlegen. Da noch keine konkrete Auswahl bestätigt wurde, fehlt `publication.countries` bewusst.
- Es sind keine Kauf-, Zahlungs- oder Bestellwerkzeuge implementiert. Die endgültige Commerce-Einstufung vor Einreichung im Portal prüfen.
- Datenschutz: allgemeine Erklärung in `DATENSCHUTZ.md` mit MCP-Ergänzung unter `wissensbasis/luhmann/DATENSCHUTZ_MCP.md`; die vier Listinglinks sind im Manifest gesetzt.
- Die fünf positiven und drei negativen Fälle im Portal anhand der tatsächlichen Werkzeugaufrufe prüfen. Ergebnisstatus privat/Preview nicht vermischen.
- Reviewer-Zugriff: MCP ohne Anmeldung, öffentliche Artikel. Wenn das Portal dennoch Zugangsdaten verlangt, nur im gesicherten Portalbereich angeben, niemals im ZIP.
- Technische Scan- und Verifizierungsanforderungen sowie rechtliche Bestätigungen durch die berechtigte Entwicklerin erfolgen im Portal. Entwurf speichern, prüfen und **erst danach** ausdrücklich zur öffentlichen Review einreichen.

## 5. Kein heimliches Live-Update

Dieses Archiv ist eine eigenständige Veröffentlichungsvorlage. Es aktualisiert **nicht** die bereits private Installation 1.0.7 und wurde nicht als neuer öffentlicher Eintrag eingereicht.
