---
name: calculate-mortgage-purchase-or-build
description: Berechnet und erläutert mit dem MCP-Tool getMortgageOffersPurchaseOrBuild reale Baufinanzierungsangebote für den Kauf einer Bestandsimmobilie oder einen Neubau. Verwenden bei Fragen zu Immobilienkauf, Neubau, Baufinanzierung, Darlehensangeboten, Monatsraten, Zinsbindungen, Tilgungssätzen oder Kaufnebenkosten. Nicht für die Anschlussfinanzierung eines bestehenden Darlehens verwenden.
---

# Immobilienfinanzierung für Kauf oder Neubau

## Ablauf

1. Prüfen, ob es um `KAUF` oder `NEUBAU` geht. Für eine Anschlussfinanzierung stattdessen den Skill `calculate-mortgage-refinancing` verwenden.
2. Vor dem Tool-Aufruf auf Deutsch mindestens diese Angaben erfragen, sofern sie nicht bereits eindeutig vorliegen:
   - Vorhaben: Kauf oder Neubau
   - Kaufpreis in Euro
   - Eigenkapital in Euro
3. Optionale Angaben übernehmen, wenn der Nutzer sie nennt: Renovierungskosten, gewünschte Darlehenssumme, Maklerprovision, fünfstellige Postleitzahl, Zinsbindungen, Tilgungssätze und gewünschte Monatsrate.
4. Bei Vergleichen mehrere Werte als Arrays übergeben. Nur unterstützte Zinsbindungen verwenden. Für den vollständigen Vertrag [references/tool-contract.md](references/tool-contract.md) lesen.
5. `getMortgageOffersPurchaseOrBuild` genau einmal mit allen geklärten Varianten aufrufen. Keine eigenen Zinssätze oder Angebote erfinden.
6. Angebote knapp auf Deutsch vergleichen. Effektivzins, Monatsrate, Restschuld und Zinsbindung nennen; Tilgung und gezahlte Zinsen bei Relevanz ergänzen.
7. Kaufnebenkosten und Tool-Warnungen sichtbar erläutern. Bei null Ergebnissen die gelieferten Warnungen wiedergeben und keine Verfügbarkeit behaupten.

## Gesprächsregeln

- Bereits genannte Werte nicht erneut erfragen.
- `Kauf`, `Bestandsimmobilie` oder `Haus-/Wohnungskauf` auf `KAUF` abbilden.
- `Neubau`, `Haus bauen` oder `Bauvorhaben` auf `NEUBAU` abbilden.
- Eurobeträge als Zahlen ohne Währungssymbol übergeben; Prozentwerte als Prozentzahlen übergeben, beispielsweise `2.5` für 2,5 %.
- Bei unklaren Pflichtangaben nachfragen, statt Werte zu raten.
- Eine gewünschte Monatsrate als `monthlyPayment` übergeben. Ohne explizite Tilgungssätze berechnet das Tool dann nur monatsratenbasierte Varianten.
- Ergebnisse als unverbindliche Finanzierungsvorschläge darstellen und nicht als Kreditzusage oder individuelle Finanzberatung.

## Fehlerfälle

- Vor dem Aufruf sicherstellen, dass Kaufpreis positiv sowie Eigenkapital kleiner als der Kaufpreis ist.
- Eine angegebene Darlehenssumme nur verwenden, wenn sie positiv und kleiner als der Kaufpreis ist.
- Bei einem Tool- oder Upstream-Fehler den Fehler knapp benennen. Keine Ersatzberechnung mit erfundenen Konditionen durchführen.
