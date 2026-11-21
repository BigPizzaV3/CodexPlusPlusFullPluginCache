# LystBot in ChatGPT nutzen

Entwurf für lystbot.com und README. Erst nach Freigabe und Verfügbarkeit der
LystBot-Verbindung veröffentlichen; eine Directory-Veröffentlichung ist hiermit
nicht behauptet.

1. Öffne in der LystBot-App **Einstellungen → ChatGPT** und erzeuge einen
   Kopplungscode. In älteren Versionen geht das unter **Einstellungen → Alexa**.
2. Öffne die LystBot-Verbindung in ChatGPT und wähle Verbinden. Für einen
   autorisierten privaten Test füge zuvor den bereitgestellten MCP-Connector
   mit OAuth hinzu.
3. Gib den sechsstelligen Code auf der LystBot-Seite ein und wähle **Verbinden**.
   Der App-Code gilt zehn Minuten und kann einmal eingelöst werden.
4. Zurück in ChatGPT kannst du etwa „Zeige meine LystBot-Listen“ oder
   „Füge Äpfel zu meiner Einkaufsliste hinzu“ schreiben. Die Liste muss auf
   deinem Gerät vorhanden sein.

ChatGPT kann eigene und geteilte Listen sowie Erinnerungen deines Geräts lesen,
Listen anlegen, Einträge hinzufügen, Text oder Häkchen ändern und Erinnerungen
anlegen. Zugriff und Änderungen folgen Mitgliedschaften, Rollen und erteilten
Berechtigungen. Lösch- und Freigabe-Tools sind nicht vorhanden.
Trenne die Verbindung in ChatGPTs Verbindungsverwaltung oder unter
**Einstellungen → ChatGPT** in LystBot. Dadurch endet der Zugriff;
Listen und bisherige Chat-Inhalte bleiben bestehen.

[Datenschutz](https://lystbot.com/legal/privacy-de.html) ·
[Nutzungsbedingungen](https://lystbot.com/legal/terms-de.html) · Support: hello@touraround.io

Interne Belege: Pairing-/OAuth-/MCP-Services und `plugins/lystbot/README.md`.
Verbindungsablauf: [offizielle OpenAI-Dokumentation](https://developers.openai.com/plugins/deploy/connect-chatgpt).
