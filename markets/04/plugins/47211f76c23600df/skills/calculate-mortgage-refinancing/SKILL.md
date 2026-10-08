---
name: calculate-mortgage-refinancing
description: Berechnet und erläutert mit dem MCP-Tool getMortgageOffersRefinancing Angebote zur Anschlussfinanzierung eines bestehenden Immobiliendarlehens. Verwenden bei Fragen zu Anschlussfinanzierung, auslaufender Zinsbindung, Forward-Finanzierung, Restschuld, neuer Monatsrate, neuen Tilgungssätzen oder einem Vergleich neuer Zinsbindungen. Nicht für Kauf oder Neubau verwenden.
---

# Anschlussfinanzierung berechnen

## Ablauf

1. Sicherstellen, dass eine bestehende Immobilienfinanzierung mit auslaufender Zinsbindung gemeint ist. Für Kauf oder Neubau stattdessen den Skill `calculate-mortgage-purchase-or-build` verwenden.
2. Vor dem Tool-Aufruf auf Deutsch mindestens diese Angaben erfragen, sofern sie nicht bereits eindeutig vorliegen:
   - Ablaufdatum der aktuellen Zinsbindung im Format `YYYY-MM-DD`
   - aktueller Immobilienwert in Euro
   - verbleibende Restschuld in Euro
3. Optionale Angaben übernehmen: fünfstellige Postleitzahl, gewünschte Zinsbindungen, Tilgungssätze und gewünschte Monatsrate.
4. Bei Vergleichen mehrere Werte als Arrays übergeben. Nur unterstützte Zinsbindungen verwenden. Für den vollständigen Vertrag [references/tool-contract.md](references/tool-contract.md) lesen.
5. `getMortgageOffersRefinancing` genau einmal mit allen geklärten Varianten aufrufen. Keine eigenen Zinssätze oder Angebote erfinden.
6. Angebote knapp auf Deutsch vergleichen. Effektivzins, Monatsrate, Restschuld und Zinsbindung nennen; Tilgung und gezahlte Zinsen bei Relevanz ergänzen.
7. Bei null Ergebnissen dies eindeutig sagen. Keine Verfügbarkeit oder Konditionen ergänzen, die das Tool nicht geliefert hat.

## Gesprächsregeln

- Bereits genannte Werte nicht erneut erfragen.
- Begriffe wie `Anschlussfinanzierung`, `Zinsbindung läuft aus`, `Prolongation` oder `Forward-Darlehen` diesem Tool zuordnen.
- Ein deutsches Datum nur dann in `YYYY-MM-DD` umwandeln, wenn Tag, Monat und Jahr eindeutig sind; sonst nachfragen.
- Eurobeträge als Zahlen ohne Währungssymbol übergeben; Prozentwerte als Prozentzahlen übergeben, beispielsweise `2.5` für 2,5 %.
- Bei unklaren Pflichtangaben nachfragen, statt Werte zu raten.
- Eine gewünschte Monatsrate als `monthlyPayment` übergeben. Ohne explizite Tilgungssätze berechnet das Tool dann nur monatsratenbasierte Varianten.
- Ergebnisse als unverbindliche Finanzierungsvorschläge darstellen und nicht als Kreditzusage oder individuelle Finanzberatung.

## Fehlerfälle

- Vor dem Aufruf sicherstellen, dass Immobilienwert und Restschuld positive ganze Eurobeträge sind.
- Das Ablaufdatum nur im ISO-Format `YYYY-MM-DD` übergeben.
- Bei einem Tool- oder Upstream-Fehler den Fehler knapp benennen. Keine Ersatzberechnung mit erfundenen Konditionen durchführen.
