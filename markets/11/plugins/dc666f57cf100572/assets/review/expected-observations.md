# Visual reference for the synthetic offer images

Reviewer reference only. This is an English translation of the independently
reviewed matrix in the repository at
`tests/fixtures/plugin-handwriting-20261009/expected-observations.md`. That
review used only the two finished images, without reading their generation
prompts. Do not give this matrix, its expected values, or the generation prompts
to the ChatGPT session being tested.

Both sheets display “TESTANGEBOT – FIKTIV” (fictional test offer) and
“Synthetisches Dokument – keine Bestellung” (synthetic document, not an order).

Sources: `angebot-a-handschrift.png` (A) and
`angebot-b-optionspreis-unleserlich.png` (B), each containing one fully visible
offer page. The image regions below identify the sources of the observations.
Amounts and dates retain the German formatting visible in the images.

## Visible information

| Feature / image region | Offer A | Offer B |
| --- | --- | --- |
| Header | Musterbetrieb A · Fenstermontage; A-017; 09.10.2026 | Musterbetrieb B · Fenstermontage; B-028; 09.10.2026 |
| Project / scope | Musterhaus · 12 windows; professional installation of 12 windows | Musterhaus · 12 windows; professional installation of 12 windows |
| Sealing, scope section | Interior and exterior sealing included | Interior sealing included; exterior sealing explicitly **NOT included** |
| Change / addition concerning exterior sealing | No visible change | Handwritten: exterior sealing optional, **+300,00 € net**, **not included in the total price** |
| Disposal of old windows, scope section | Printed “included” crossed out; handwritten arrow: **NOT included; optional +480,00 € net** | Included; no visible deletion or change |
| Site electricity, scope section | Provided by the client | Provided by the client |
| Net lump sum, price summary | Printed **9.600,00 €** crossed out; handwritten **9.240,00 €** | Printed **9.100,00 €** |
| VAT, price summary | Rate **19%**; printed **1.824,00 €** crossed out; handwritten **1.755,60 €** | Rate **19%**, amount **1.729,00 €** |
| Gross total, price summary | Printed **11.424,00 €** crossed out; handwritten **10.995,60 €** | Printed **10.829,00 €** |
| Payment, below the prices | Due within 14 days without deduction | **2% early-payment discount for payment within 7 days**, otherwise due within 14 days without deduction |
| Validity, below payment terms | Printed **31.10.2026** crossed out; handwritten **15.11.2026** | **10.11.2026** |
| Window sills, boxed note at the bottom | Handwritten: optional **720,00 € net**, **not included in the total price** | Handwritten: optional, **not included in the total price**; “Aufpreis: … € netto” (net surcharge), but the number is densely scribbled over and **cannot be read reliably** |

## Expected comparison treatment

- A: use the clearly identified handwritten replacement values. Do not also
  count the crossed-out values. Preserve the extended validity date and the
  change stating that disposal is not included.
- These are net lump sums for the stated scope. No unit price per window is
  given; do not multiply the lump sum by twelve again. Supply of the windows is
  not promised.
- Show options separately; none is automatically ordered.
- B: treat the window-sill surcharge as **unreadable / requires clarification**.
  Do not infer an amount from the scribbles, offer A, or an assumed price range.
  “Optional” and “not included in the total price” are clearly readable and must
  be retained even though the amount is unknown.
- B: the early-payment discount is conditional. Do not automatically deduct it
  without explicitly stating the payment assumption.
- The base prices cover different scopes. Any claim about the lower total for
  an equivalent scope must identify an explicit comparison scenario. A complete
  comparison including window sills cannot be established for B because its
  option price is unknown.

## Optional independent arithmetic checks — not additional source claims

The visible corrected totals for A and the printed totals for B are consistent
with 19% VAT.

| Explicit calculation scenario, before early-payment discount | A net / gross | B net / gross |
| --- | --- | --- |
| Visible base price | 9.240,00 € / 10.995,60 € | 9.100,00 € / 10.829,00 € |
| Installation with interior/exterior sealing and disposal, **excluding window sills**: A plus disposal; B plus exterior sealing | 9.720,00 € / 11.566,80 € | 9.400,00 € / 11.186,00 € |

The nominal base-price difference is 140,00 € net or 166,60 € gross. In the
explicitly calculated scenario, the difference is 320,00 € net or 380,80 € gross.
These scenarios do not establish any other technical equivalence and are
neither supplier quotations nor orders.

## Uncertainty

B's window-sill surcharge is unknown. The other numbers, corrections, and
negations transcribed above are clearly readable in these images. Differences
from the generation request were not checked because that request was
deliberately not read during the independent visual review. The images test
simulated handwriting; a successful model run does not establish general
reliability for real handwritten offers.
