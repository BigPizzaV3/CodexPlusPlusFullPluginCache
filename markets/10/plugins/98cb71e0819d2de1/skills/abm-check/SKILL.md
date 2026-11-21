---
name: abm-check
description: Prüft eine Zielkundenliste (ABM-Watchlist) gegen die Website-Besucher. Nutzen bei "prüf meine Zielkundenliste", "waren diese Unternehmen bei uns", "ABM-Check", oder wenn der Nutzer eine Liste von Firmennamen oder Domains einfügt. / Checks a target-account list (ABM watchlist) against website visitors. Use for "check my target accounts", "did these companies visit us", or when the user pastes a list of company names or domains.
---

# ABM-Check

Gleiche eine Liste von Zielkunden mit den identifizierten Website-Besuchern
ab und liefere pro Treffer die Aktivität.

## Vorgehen

1. **Liste entgegennehmen.** Namen, Website-Domains oder Webmetic-IDs,
   bis zu 50 Einträge pro Aufruf. Bei mehr als 50 in Blöcke aufteilen.
   Tippfehler nicht korrigieren, die Suche ist fehlertolerant
   (Umlaute, „Muenchen"-Schreibweisen, Wortreihenfolge).
2. **Zeitraum klären.** Standard: die letzten 30 Tage.
3. **`check_accounts` aufrufen** mit der kompletten Liste. Das Tool liefert
   pro Eintrag den Besuchsstatus und die Trefferqualität (exakt, Präfix,
   enthalten, unscharf).
4. **Treffer vertiefen:** Für jedes besuchende Unternehmen bei Bedarf
   `get_company_activity` aufrufen, um zu zeigen, was es angesehen hat.
5. **Ergebnis ausgeben:**
   - Tabelle: Zielkunde, besucht ja/nein, letzter Besuch, Sitzungen,
     auffälligste Aktivität.
   - Bei unscharfen Treffern die Trefferqualität nennen, damit der Nutzer
     Verwechslungen erkennt.
   - Abschluss: welche Zielkunden aktiv sind (mit empfohlenem nächsten
     Schritt) und welche im Zeitraum nicht identifiziert wurden.

## Stil

- In der Sprache des Nutzers antworten. Auf Deutsch: „Unternehmen"
  statt „Firma".

## Grenzen ehrlich benennen

- „Nicht identifiziert" heißt: im Zeitraum kein zuordenbarer Besuch.
  Das Unternehmen kann trotzdem da gewesen sein (Homeoffice, Mobilfunk).
- Es werden Unternehmen identifiziert, keine Personen.
