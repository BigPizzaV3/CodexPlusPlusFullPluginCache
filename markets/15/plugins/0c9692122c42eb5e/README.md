# CrewMind 1.1.1

Dieses Paket aktualisiert den vorhandenen öffentlichen Einreichungsentwurf `crewmind`. Es verbindet freigegebene CrewMind-Konten mit `https://mcp.crewmind.io/mcp`. Member- und Creator-Rechnungen können vorbereitet und nach ausdrücklicher Freigabe erstellt oder gesendet werden. Der bestehende Rechnungsserver berechnet Beträge und prüft Berechtigungen. Die Installation allein gewährt keinen Datenzugriff.

Version 1.1.0 ergänzt die Anweisungen für native MCP-App-Karten und benötigt den separat bereitgestellten CrewMind-MCP-Proxy 1.1.0. Dieser liefert die UI-Ressourcen zu den vorhandenen Tools und korrigiert deren Annotations, einschließlich fünf zuvor fälschlich als rein lesend gekennzeichneter Tools. Das Paket allein ändert weder den laufenden Proxy noch den ursprünglichen Rechnungsserver.

## Korrektur von Version 1.1.0

Das Portal verlangt genau fünf positive und drei negative Testfälle. Version 1.1.1 integriert die bisher zusätzliche UI-Prüfung in P1 und enthält damit die geforderte Anzahl. Die fünf übrigen Paketdateien einschließlich MCP-Konfiguration, Skills und Assets sind gegenüber 1.1.0 unverändert.

Für dieses Update nur `crewmind-1.1.1.zip` im bestehenden OpenAI-Eintrag `crewmind` hochladen und unter Review information prüfen, dass fünf positive Fälle erscheinen. Den bereits bereitgestellten Proxy 1.1.0 weiterverwenden; kein erneuter Netlify-Deploy, keine neue Domain und keine Login-Änderung sind für diese Metadatenkorrektur nötig. Nach dem Upload gegebenenfalls vom Portal erneut verlangte Angaben prüfen. Ein tatsächlich bestandener Portal-Check wird erst nach dem Upload bestätigt.

## Ersteinrichtung, falls der Proxy noch nicht bereitgestellt wurde

1. **Zuerst den Proxy bereitstellen:** Im bestehenden Netlify-Projekt `stellular-rugelach-6bf09d` unter **Deploys → choose a folder** den vollständigen Proxy-Ordner der Version 1.1.0 auswählen. Er enthält unter anderem `netlify.toml`, `netlify/`, `src/` und `public/`. Das Projekt verwendet Netlify Drop; dafür ist kein „Trigger deploy“ nötig. Kein neues Projekt anlegen. Bestehende Domain, DNS, OAuth-Einstellungen und die Umgebungsvariable `OPENAI_DOMAIN_VERIFICATION_CODE` unverändert lassen. Den Prüfcode nicht in Dateien kopieren.
2. **Danach das Plugin aktualisieren:** Die Plugin-ZIP 1.1.1 im bereits vorhandenen OpenAI-Eintrag **`crewmind`** als neue Version hochladen. MCP-Adresse und Identität beibehalten. Anschließend die gespeicherten Einstellungen prüfen, bei Bedarf **Reconnect**, danach **Rescan** ausführen und einen frischen Chat mit CrewMind öffnen. Erst der neue Scan und ein Host-Test bestätigen die bereitgestellten Tools und Karten.

Der ältere Eintrag `crewmind-invoices` und die lokal installierte Version 1.1.0 mit direkter Supabase-Adresse werden dadurch nicht aktualisiert. Diese Anleitung ändert keine bestehende iOS-App, Upload-Dienste, Login-Schlüssel oder Berechtigungen. Der Proxy nutzt den vorhandenen Rechnungsserver; es kommen keine zusätzlichen Dienste, UI-Datenablagen oder Polling-Aufrufe hinzu.

## Anmeldung und aktueller Prüfstatus

Jeder Nutzer meldet sich selbst über CrewMind OAuth an. Member-Rechnungen erfordern Admin-Rechte, Creator-Rechnungen eine Creator-Billing-Freigabe. Das unveränderte `mcp.json` verwendet DCR, `baseScopes: ["email", "profile"]`, `defaultScopes: []` und `oidcEnabled: false`. Zugangsdaten gehören weder in die ZIP noch in Dateien oder den Chat. Reviewer-Zugangsdaten werden ausschließlich in den sicheren Portal-Feldern hinterlegt.

Am 5. November 2026 meldete der Herausgeber, dass die MCP-Einrichtung im Portal funktioniert. Der neue Screenshot zeigt fehlende Review-Angaben im Bereich Test cases, bei sechs vorhandenen positiven Fällen und der Vorgabe genau fünf. Version 1.1.1 korrigiert diese Paketangabe. Sie ändert weder OAuth noch den Proxy. Ein aktueller vollständiger Live-UI-Test wurde im Rahmen dieser Korrektur nicht ausgeführt.

Die Dateien sind ein Einreichungsentwurf. Lokale Prüfungen ersetzen weder den erneuten Portal-Scan noch eine Review-Freigabe. Eine Behebung aller Findings oder Veröffentlichung wird damit nicht behauptet. Vorhandene Listing-URLs, Logo, Länderwahl und Demo-Video bleiben erhalten; das ältere Video belegt die neue UI nicht.

## Verwendung

CrewMind im Chat auswählen und den gewünschten Monat und Auftrag nennen, zum Beispiel:

- „Zeige mir den Member-Rechnungsstatus für Oktober 2026 und meine Creator-Profile. Noch nichts erstellen oder senden.“
- „Bereite die Rechnungsvorschauen für die ausgewählten Accounts vor. Zeige fehlende Angaben und warte vor dem Erstellen auf meine Bestätigung.“

Die nativen Karten werden über die regulären MCP-Tool-Aufrufe angeboten; ein gesonderter Dashboard-Aufruf ist nicht nötig. Der Host entscheidet, wann er sie zeigt und ob einzelne Aufrufe eigene Karten erhalten. Bei bekannten Accounts und Zählern ergänzt der Skill den optionalen, im Tool-Schema angebotenen `uiContext`. Der Proxy entfernt diesen Anzeigekontext vor dem bestehenden Rechnungsserver. Ohne UI-Unterstützung erscheint der tatsächliche Status weiterhin im Chat.

Die Karten zeigen tatsächliche Aufrufzustände und belegte Ergebnisse. Eine Profilliste ist keine Zusage, dass alle Konten abrechnungsfähig sind. Vorhandene Monatsrechnungen werden von in diesem Lauf erstellten Rechnungen unterschieden. Fehlende Umsatzwerte sind nie automatisch 0; Beträge und Warnungen kommen aus den Tools. Ein abgeschlossener Aufruf ersetzt keine Prüfung auf vollständige Daten.

„Stopp anfragen“ sendet lediglich eine Nutzer-Nachricht an den Chat. Für einen laufenden Ablauf dient auch die native Stopp-Funktion des Hosts. Bereits übermittelte Serveraktionen können trotzdem abgeschlossen werden; ein Klick ist keine bestätigte Stornierung. Die optionale `assets/progress-demo.html` bleibt eine gekennzeichnete Ablaufwiedergabe. Ihr Demo-Stopp hält nur die Wiedergabe an.

## Freigaben und Fehler

Vor jedem Erstellen und Senden werden Name, Monat, Tool-Betrag und Warnungen gezeigt und ausdrücklich bestätigt. Member-Erstellungen senden automatisch eine In-App-Nachricht und benötigen die Zustimmung zu beiden Wirkungen. Creator-Erstellungen verwenden ausdrücklich `send: false`; ein späterer Versand erfordert eine eigene Bestätigung. Bei Stapeln gilt die Zustimmung nur für die gezeigten Zeilen und die bezeichnete Phase. Die UI ändert diese Regeln nicht.

Bei „nicht freigegeben“, 401 oder 403 stoppt der Ablauf sofort. Der Nutzer klärt die Berechtigung mit dem CrewMind-Administrator oder den regulären OAuth-Zugang. Keine Umgehung über Website-Klicken, Browser-Sessions, Datenbank- oder REST-Aufrufe. Kurzlebige Download-Links werden nur auf Wunsch unmittelbar angezeigt und nicht gespeichert oder protokolliert.

## Prüfung der neuen UI

Nach erfolgreichem Login den erweiterten Review-Fall P1 mit dem kontrollierten Review-Konto ausführen: Monatsstatus und Creator-Profile laden, Karten und tatsächliche Zähler prüfen, keine Rechnungen erstellen oder senden. Fehlende Werte müssen unbekannt bleiben. Ein angebotener Stopp-Wunsch darf nicht als bestätigter Serverabbruch erscheinen. Der Test benötigt keine Rate-, Vorschau-, PDF- oder ZIP-Aufrufe und keine zusätzlichen Aufrufe für Animationen.

Es gibt genau fünf positive und drei negative Review-Fälle. P1 enthält zusätzlich die lesende UI-Prüfung; P2 bis P5 und alle drei negativen Fälle bleiben unverändert. Andere Vorschau- oder Rate-Tools können produktive Cache- beziehungsweise Vorschau-Schreibwirkungen haben und sind deshalb nicht pauschal technisch schreibfrei. Die vorhandenen Testfälle sind Spezifikationen, keine Behauptung erfolgreicher neuer Ausführung; insbesondere Erstellung und Versand benötigen weiterhin die dort beschriebenen separaten Freigaben und Testvoraussetzungen.
