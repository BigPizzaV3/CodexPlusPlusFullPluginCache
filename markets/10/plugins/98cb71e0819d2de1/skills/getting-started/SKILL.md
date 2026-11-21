---
name: getting-started
description: Einmalige Bereitschaftsprüfung für Webmetic — prüft Konto, Tracking, Plan, Ansprechpartner-Setup und Guthaben, behebt oder erklärt jeden Blocker und zeigt danach eine echte Auswertung. Nutzen bei "einrichten", "erste Schritte", "funktioniert das schon", "warum sehe ich keine Daten", "warum ist die Liste leer", "ist mein Konto bereit", "Webmetic einrichten", "richte Webmetic für mich ein", "ich bin neu hier". / One-time readiness check for Webmetic — checks the account, tracking, plan, contact setup and credits, fixes or explains every blocker, then shows real output. Use for "set up", "set up Webmetic for me", "getting started", "is this working", "why do I see no data", "why is my list empty", "is my account ready", "I am new here".
---

# Erste Schritte

Eine einmalige Prüfung, ob das Konto in einem Zustand ist, in dem Webmetic Nutzen
bringt, und was sonst zu tun ist. Kein Tutorial. Erst die Prüfungen, dann ein
Blocker oder eine echte Auswertung.

Der häufigste Grund für eine leere erste Antwort ist ein Tracking-Code, der nicht
oder nur nach der Einwilligung lädt. Diese Prüfung findet das, bevor der Nutzer
schließt, Webmetic funktioniere nicht.

## Sprache

In der Sprache des Nutzers antworten, einschließlich Tabelle und Fehlertext. Daten
nicht übersetzen: Konto-Kennung, Domains, Unternehmensnamen und Adressen bleiben
unverändert. Auf Deutsch „Unternehmen" statt „Firma".

## Wann diese Skill greift

Beim Einrichten, bei „erste Schritte" und bei jeder Frage, warum keine oder zu
wenige Daten da sind. Nicht auslösen für die normale Tagesfrage („wer war heute
da") — das ist `hot-leads` oder `wochenbericht`. Nicht bei jeder Sitzung
wiederholen: Die Prüfung ist einmalig oder auf Nachfrage.

## Ablauf

1. **Status holen** mit `get_account_status`. Ein Aufruf, kostet nichts: Domains
   mit erstem und letztem Besuch, Plan und Free-Grenze, Ansprechpartner-Setup,
   Guthaben. Meldet eine Domain keinen einzigen Besuch, liefert der Status auch
   den Tracking-Code mit der richtigen Konto-Kennung mit.
2. **Tracking prüfen**, wenn eine Domain keine Besuche hat oder seit Tagen nichts
   ankam: `check_tracking_setup` für genau diese Domain. Das Werkzeug lädt die
   Website wirklich und unterscheidet:
   - **Skript nicht gefunden** — der Code fehlt auf der geprüften Seite
   - **fremde Konto-Kennung** — es läuft ein Skript, aber für ein anderes Konto
   - **Treffer ohne Konto-Kennung** — auf der Seite steht etwas von Webmetic, aber
     keine Kennung. Das kann ein Link im Footer sein und belegt keine Erfassung
   - **erst nach Einwilligung geladen** — der Consent-Banner blockiert das Skript
   - **nicht erreichbar oder Zeitüberschreitung** — keine Aussage möglich
3. **Bericht ausgeben** nach dem festen Format unten.
4. **Echte Auswertung zeigen**, aber nur ohne harten Blocker: `get_activity_summary`
   oder `list_visiting_companies` für die letzten 7 Tage.

**Harte Blocker** (Schritt 4 entfällt, stattdessen der Fehlerblock): keine Website
im Konto, Skript nicht gefunden, fremde Konto-Kennung, Treffer ohne Kennung, erst
nach Einwilligung geladen. Eine Auswertung ohne Daten beweist nichts und bestätigt
nur den falschen Eindruck.

**Hinweise, kein Blocker**: Free-Grenze erreicht (die ersten 10 Unternehmen pro
Monat sind lesbar, der Rest bleibt verborgen — das ist kein Fehler); kein
Ansprechpartner-Setup (`find_contacts` und `reveal_contact` bleiben gesperrt, bis
der Nutzer im Chat zustimmt: `enable_contacts` nennt die drei Zustimmungen, erst
nach seinem ausdrücklichen Ja aufrufen).

## Pflicht ist nur der Tracking-Code

Für die ersten Daten braucht Webmetic genau eins: den Tracking-Code auf der
Website. Kann der Assistent die Website selbst bearbeiten (Code, CMS oder Tag
Manager), bietet er an, den Code dort einzufügen, zeigt die Änderung und ruft danach
`check_tracking_setup` auf. Sonst gibt er den Code aus dem Status mit oder schreibt
die Mail an die Person, die die Website betreut. Meldet die Prüfung den Code als
korrekt eingebunden, ist nichts weiter nötig: Die ersten Unternehmen erscheinen
nach Minuten bis Stunden.

Alles andere ist optional. Jedes Angebot nur in seinem Moment, eins pro Antwort, nie
als Liste und nie, bevor der Code live ist:

- `create_email_alert`, während der Nutzer auf die ersten Unternehmen wartet oder
  über dieselbe Frage auf dem Laufenden bleiben will
- `set_target_profile`, wenn zum ersten Mal eine Unternehmensliste gezeigt wird;
  das Profil aus der Website entwerfen und vor dem Speichern bestätigen lassen
- `enable_contacts`, nur wenn der Nutzer nach einem Ansprechpartner fragt
- `invite_user`, wenn der Nutzer Vertrieb oder Kollegen erwähnt

## Ausgabeformat

Bei jedem Lauf gleich. Überschrift, Tabelle, dann entweder die Auswertung oder
genau ein Fehlerblock mit dem wichtigsten Blocker zuerst. Das Format auch dann
nicht umbauen oder „verbessern", wenn die Skill in derselben Unterhaltung schon
einmal gelaufen ist. Nur Zeilen zeigen, die zutreffen.

```
# Webmetic — Bereitschaftsprüfung

| Prüfung | Status |
| --- | --- |
| Konto und Websites | {✅ / ⚠️ / ❌} — {eine Zeile} |
| Tracking | {✅ / ⚠️ / ❌} — {eine Zeile} |
| Plan | {✅ / ⚠️} — {eine Zeile} |
| Ansprechpartner | {✅ / ⚠️} — {eine Zeile} |
```

Ohne Blocker: **Alles bereit.** plus die Auswertung der letzten 7 Tage.

Mit Blocker: **Das zuerst: {Blocker}**, ein bis zwei Zeilen, warum es zählt, dann
der konkrete Schritt. Fehlt der Code, den Tracking-Code aus dem Status mitgeben,
damit der Nutzer ihn direkt weiterreichen kann. Danach der Satz zum erneuten
Prüfen und darunter in einem Codeblock: `Ist mein Webmetic-Konto bereit?`

## Quellenregel

Jeder Status kommt aus einer echten Antwort der Werkzeuge. Keine Konto-Kennung,
keine Domain, keine Zahl erfinden. Antwortet ein Werkzeug mit einem Fehler, die
Zeile als „nicht prüfbar" ausweisen statt zu raten. „Kein identifizierter Besuch"
ist nicht dasselbe wie „kein Besuch".

## Was nicht zu tun ist

- Keine Auswertung zeigen, wenn ein harter Blocker offen ist.
- Nichts freischalten und keine Ansprechpartner suchen. Die Prüfung kostet nichts
  und bleibt dabei.
- `check_tracking_setup` nur für die auffällige Domain aufrufen, nie nacheinander
  für mehrere.
- Für die Einrichtung nicht ins Dashboard schicken: Tracking-Code, Zielkundenprofil,
  Ansprechpartner, Kollegen und Alerts gehen im Chat.
- Keine Checkliste der optionalen Schritte zeigen.
- Kein Tutorial daraus machen.

## Beispiel

```
# Webmetic — Bereitschaftsprüfung

| Prüfung | Status |
| --- | --- |
| Konto und Websites | ✅ kunde.de, seit 12.03.2026 erfasst |
| Tracking | ❌ Code lädt erst nach der Einwilligung |
| Plan | ✅ Growth, keine Free-Grenze |
| Ansprechpartner | ✅ eingerichtet, 44 Credits |

**Das zuerst: Der Tracking-Code lädt erst nach dem Consent-Banner.**
Besucher, die den Banner wegklicken oder ignorieren, werden gar nicht erfasst.
Deshalb sehen Sie deutlich weniger Unternehmen als Besucher. Webmetic setzt keine
eigenen Cookies. Damit der Code vor der Einwilligung lädt, geben Sie ihn im
Consent-Tool frei.

Danach erneut prüfen:

Ist mein Webmetic-Konto bereit?
```
