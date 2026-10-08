# Tool-Vertrag: getMortgageOffersPurchaseOrBuild

## Eingabe

| Feld | Typ | Regel |
|---|---|---|
| `financingPurpose` | `KAUF \| NEUBAU` | Pflichtfeld |
| `purchasePrice` | positive ganze Zahl | Pflichtfeld, Euro |
| `equity` | nichtnegative ganze Zahl | Vor Aufruf erfragen; muss kleiner als `purchasePrice` sein |
| `renovationCosts` | nichtnegative ganze Zahl | Optional, Standard 0 Euro |
| `loanAmount` | positive ganze Zahl | Optional; muss kleiner als `purchasePrice` sein. Sonst berechnet das Tool den Betrag aus Preis, Renovierung, Nebenkosten und Eigenkapital. |
| `brokerCommissionPct` | nichtnegative Zahl | Optional; nur für `KAUF`, sonst ignoriert. Ohne Wert aus dem Bundesland abgeleitet. |
| `postalCode` | String mit genau 5 Ziffern | Optional; Standard `23588`. Dient regionaler Preisfindung und der Ermittlung des Bundeslands. |
| `fixedInterestTerms` | Array ganzer Zahlen | Optional; erlaubt: 5, 8, 10, 12, 15, 20, 25, 30. Standard `[10]`. |
| `repaymentRates` | Array positiver Zahlen | Optional, Prozent. Standard `[2]`, aber nur wenn auch `monthlyPayment` fehlt. |
| `monthlyPayment` | positive Zahl | Optional, Euro. Ohne `repaymentRates` nur monatsratenbasierte Angebote; mit `repaymentRates` zusätzlich zu deren Kombinationen. |

Mehrere Zinsbindungen und Tilgungssätze erzeugen das kartesische Produkt aller Kombinationen.

## Ausgabe

- `offerResults[]`: enthält `offer` und `repaymentInfo`.
- `offer`: `repaymentRate`, `fixedInterestTerm`, `monthlyPayment`, `nominalInterestRate`, `effectiveInterestRate`, `remainingDebt`, `applicationUrl`.
- `repaymentInfo`: `principalRepaid` und `interestPaid`.
- `closingCosts`: Grunderwerbsteuer, Grundbuchkosten, Notarkosten, Maklerprovision und Summe. Für `NEUBAU` setzt die aktuelle Berechnung diese Positionen auf 0.
- `warnings`: optionale Hinweise, insbesondere zu zu wenig Eigenkapital oder Eigenkapital unterhalb der Nebenkosten.

Zusätzliche Textausgaben erklären verwendete Standardwerte und das ermittelte Bundesland.
