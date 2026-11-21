---
name: hot-leads
description: Findet die heißesten Leads anhand von Kaufsignalen (Formular-Submits, Kontakt-Klicks, Downloads, Besuche wichtiger Seiten, hoher Lead-Score). Nutzen bei "heiße Leads", "wer ist kaufbereit", "wen soll der Vertrieb anrufen". / Finds the hottest leads based on buying signals (form submits, contact clicks, downloads, high-intent page visits, and lead score). Use for "hot leads", "who is ready to buy", "who should sales call".
---

# Heiße Leads

Identifiziere die Unternehmen mit den stärksten Kaufsignalen und begründe
jede Einstufung mit konkretem Verhalten.

## Vorgehen

1. **Domain und Zeitraum klären.** Standard: die letzten 7 Tage; bei wenig
   Verkehr auf 30 Tage erweitern und das im Ergebnis vermerken. Denselben
   Zeitraum in allen Aufrufen verwenden.
2. **Signale einsammeln** mit `list_visiting_companies` (gleiche Domain,
   gleicher Zeitraum, mehrere Aufrufe mit unterschiedlichen Filtern):
   - `event="form_submit"` — abgeschickte Formulare (stärkstes Signal)
   - `event="contact_click"` — Klicks auf E-Mail oder Telefonnummer
   - `event="download"` — heruntergeladene Dateien
   - `visited_page` mit dem Pfad der Preisseite. Den echten Pfad vorher in
     den Top-Seiten von `get_activity_summary` nachsehen (z. B. `/pricing`
     oder `/preise`), nicht raten.
   - `sort="lead_score"`, `min_lead_score=70` — Webmetic-Score als Basis
     (Skala 0 bis 100, ab 70 gilt ein Lead als stark)
3. **Ranking bilden.** Gewichte grob: Formular-Submit > Kontakt-Klick >
   Preisseite > Download > hoher Lead-Score allein. Wiederkehrende
   Unternehmen (mehrere Sitzungen) höher einstufen. Trackt die Domain
   keine Events (alle Event-Filter leer), auf Preisseite, Lead-Score und
   Besuchsintensität ausweichen und das im Ergebnis erwähnen.
4. **Top 3 vertiefen** mit `get_company_activity`: Was genau wurde
   angesehen, wie lange, welche Events, über welche Quelle kam das
   Unternehmen?
5. **Ergebnis ausgeben:** Rangliste mit je einer Zeile Begründung
   („Formular auf /kontakt abgeschickt, davor 6 Minuten auf der
   Preisseite") plus empfohlenem nächsten Schritt pro Lead.

## Stil

- In der Sprache des Nutzers antworten. Auf Deutsch: „Unternehmen"
  statt „Firma".
- Jede Einstufung mit beobachtetem Verhalten belegen, nie mit Vermutungen.
- Webmetic identifiziert Unternehmen, keine Personen: keine
  Ansprechpartner erfinden. Fragt der Nutzer nach Ansprechpartnern, für
  das jeweilige Unternehmen `find_contacts` nutzen; E-Mail oder Rufnummer
  nur per `reveal_contact` freischalten, wenn der Nutzer das ausdrücklich
  will.
- Steht in der Spalte Fit nur „-", ist für die Website kein
  Zielkundenprofil hinterlegt, und die Relevanz entspricht der Aktivität.
  Dann einmal anbieten, das Profil aus der Website zu entwerfen; mit
  `set_target_profile` erst speichern, wenn der Nutzer den Entwurf
  bestätigt hat.
