# Tax & compliance notes — Mizar

**Informational only, not tax or legal advice.** Mizar never decides a user's tax status or rate. When the user asks "which rate?" or "do I need to charge VAT?", say a tax advisor should confirm, and offer to build the invoice once they tell you.

## Germany (§14 UStG) — fields an invoice normally must show

1. Full name + address of seller and client
2. Seller's business tax number (Steuernummer) **or** business VAT number (USt-IdNr.) — not the personal Steuer-ID
3. Issue date
4. Unique sequential invoice number
5. Quantity and type of goods/services
6. Date/period of delivery or service
7. Net amount per tax rate, applicable tax rate, tax amount (or exemption reason)
8. Any agreed reductions (discounts) not already in the price

Small invoices (≤ €250 gross, "Kleinbetragsrechnung") have reduced requirements — only apply if the user says so.

Common notes (use **only when the user confirms** the case applies):
- Kleinunternehmer: "Gemäß § 19 UStG wird keine Umsatzsteuer berechnet." / EN: "No VAT charged under the small business scheme (§ 19 UStG)."
- Reverse charge (B2B services to EU business): "Steuerschuldnerschaft des Leistungsempfängers (Reverse Charge)" / EN: "Reverse charge — VAT to be accounted for by the recipient." Both business VAT numbers on the invoice.

From 2025 onward, German B2B invoices are moving to mandatory e-invoicing (XRechnung / ZUGFeRD) on a phased timeline. Mizar v1 renders a human-readable PDF only — **not** a structured e-invoice. Tell German B2B users to check whether their client/advisor requires an e-invoice format.

## EU (general)

VAT Directive Art. 226 sets similar mandatory fields. Rates differ by country; never assume a rate from the client's country.

## UK

VAT-registered sellers: VAT number, rate, VAT amount per rate, unique number, dates. Not registered → no VAT line.

## US

No federal VAT. Sales tax depends on state and product type; most services are untaxed in many states but not all. Only add a tax line with the rate the user gives.

## Rounding

Line amounts rounded half-up to 2 decimals; tax computed per rate group on the summed base (not per line) and rounded half-up. If the user's accounting tool rounds per line, follow the user's instruction and note it.
