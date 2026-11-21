---
name: wochenbericht
description: Erstellt den wöchentlichen Besucherbericht aus Webmetic. Nutzen bei "Wochenbericht", "was war diese Woche auf der Website los", "Zusammenfassung der Besucher". / Builds the weekly visitor report from Webmetic. Use for "weekly report", "what happened on the website this week", "visitor summary".
---

# Wochenbericht

Erstelle einen kompakten Wochenbericht über die identifizierten Unternehmen
auf der Website. Datenquelle sind die Webmetic-MCP-Tools.

## Vorgehen

1. **Domain klären.** Wenn der Nutzer mehrere Domains im Konto hat und keine
   nennt, frage nach. Die Domain muss exakt der Schreibweise im
   Webmetic-Konto entsprechen.
2. **Zeitraum festlegen.** Standard: die letzten 7 Tage. Verwende in ALLEN
   Tool-Aufrufen denselben expliziten Zeitraum (`from_date`, `to_date`),
   damit die Zahlen konsistent sind.
3. **Daten holen** (in dieser Reihenfolge, gleiche Domain und Zeitraum):
   - `get_activity_summary` fuer Gesamtzahlen, Top-Seiten, Quellen,
     Kampagnen, Intent-Events, Branchen.
   - `list_visiting_companies` mit `sort="lead_score"`, `limit=10` fuer die
     Top-Unternehmen.
   - `get_visit_highlights` mit `highlight="intensive"` und einmal mit
     `highlight="new"` fuer intensive Sitzungen und Erstbesucher.
4. **Bericht strukturieren:**
   - **Überblick**: Anzahl identifizierter Unternehmen, Sitzungen,
     Seitenaufrufe, Vergleichston sachlich.
   - **Top-Unternehmen**: die 5 bis 10 wichtigsten mit Lead-Score und dem
     interessantesten Detail (z. B. meistbesuchte Seite).
   - **Kaufsignale**: Intent-Events der Woche (Formular-Submits,
     Kontakt-Klicks, Downloads). Bei Bedarf per
     `list_visiting_companies(event="form")` nachfassen, wer dahintersteckt.
     Fehlt die Event-Sektion in der Zusammenfassung, trackt die Domain im
     Zeitraum keine Events; den Abschnitt dann weglassen oder kurz erklären.
   - **Quellen und Kampagnen**: woher der Verkehr kam, bezahlte vs.
     organische Anteile.
   - **Neu diese Woche**: Erstbesucher, die zur Zielgruppe passen.
   - **Empfehlung**: 1 bis 3 konkrete nächste Schritte für den Vertrieb.

## Stil

- In der Sprache des Nutzers antworten (fragt er auf Englisch, ist der
  Bericht englisch). Auf Deutsch: sachlich, „Unternehmen" statt „Firma".
- Zahlen immer mit Bezugsgröße („14 von 86 Unternehmen").
- Keine erfundenen Werte: nur, was die Tools liefern. Wenn ein Zeitraum
  keine Events enthält, das ehrlich benennen (fehlendes Tracking ist nicht
  fehlendes Interesse).
- Höchstens ein Angebot pro Bericht, nie als Liste: Steht in der Spalte
  Fit nur „-", fehlt das Zielkundenprofil; dann anbieten, es aus der
  Website zu entwerfen, und erst nach Bestätigung mit `set_target_profile`
  speichern. Will der Nutzer den Bericht regelmäßig, einmal eine
  E-Mail-Benachrichtigung anbieten (`create_email_alert`, nach Bestätigung
  von Art, Tagen, Uhrzeit und Empfängern).
