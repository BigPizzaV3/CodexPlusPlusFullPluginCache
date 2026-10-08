# Tool-Vertrag: getMortgageOffersRefinancing

## Eingabe

| Feld | Typ | Regel |
|---|---|---|
| `maturityDate` | ISO-Datum `YYYY-MM-DD` | Pflichtfeld; Ablaufdatum der aktuellen Zinsbindung |
| `propertyValue` | positive ganze Zahl | Pflichtfeld, aktueller Immobilienwert in Euro |
| `remainingDebt` | positive ganze Zahl | Pflichtfeld, zu finanzierende Restschuld in Euro |
| `postalCode` | String mit genau 5 Ziffern | Optional; Standard `23588`. Dient regionaler Preisfindung. |
| `fixedInterestTerms` | Array ganzer Zahlen | Optional; erlaubt: 5, 8, 10, 12, 15, 20, 25, 30. Standard `[10]`. |
| `repaymentRates` | Array positiver Zahlen | Optional, Prozent. Standard `[2]`, aber nur wenn auch `monthlyPayment` fehlt. |
| `monthlyPayment` | positive Zahl | Optional, Euro. Ohne `repaymentRates` nur monatsratenbasierte Angebote; mit `repaymentRates` zusätzlich zu deren Kombinationen. |

Mehrere Zinsbindungen und Tilgungssätze erzeugen das kartesische Produkt aller Kombinationen. Bei einer Monatsrate wird pro Zinsbindung eine zusätzliche Variante berechnet.

## Ausgabe

- `offerResults[]`: enthält `offer` und `repaymentInfo`.
- `offer`: `repaymentRate`, `fixedInterestTerm`, `monthlyPayment`, `nominalInterestRate`, `effectiveInterestRate`, `remainingDebt`, `applicationUrl`.
- `repaymentInfo`: `principalRepaid` und `interestPaid`.
- `_meta.context.financingPurpose`: ist `FORWARD`.

Zusätzliche Textausgaben nennen die Anzahl der Angebote und erklären verwendete Standardwerte.
