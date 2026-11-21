# Trigger phrases — Mizar

Exact ChatGPT-style utterances that should activate this plugin. Keep `plugin.json` (`description`, `longDescription`, `defaultPrompt`) and `skills/invoice-from-notes/SKILL.md` (`description`) aligned with this list.

## Primary (listing / defaultPrompt)

1. create an invoice from these notes
2. turn this timesheet into an invoice with 19% VAT
3. generate an invoice PDF for this client

## Discovery / mid-chat recommendation

4. generate invoice PDF
5. make an invoice for this client
6. invoice from timesheet
7. draft an invoice with tax
8. freelance invoice generator
9. turn this into an invoice
10. invoice with line items and VAT
11. bill this client for last week's work
12. make a tax-ready invoice PDF
13. convert these hours into an invoice
14. invoice PDF with payment terms
15. I need to invoice Acme for 12 hours at €110
16. make a reverse charge invoice for my EU client
17. invoice template with my bank details
18. same invoice as last month but for October
19. create an invoice in German
20. Rechnung aus diesen Notizen erstellen
21. Rechnung mit 19 % MwSt als PDF

## Incomplete inputs (should activate, then ask)

- generate invoice PDF  ← no client/items/rates → ask in one checklist
- invoice from timesheet  ← timesheet has hours but no rate → ask for rate + tax

## Should NOT activate

- extract the line items from this invoice PDF into Excel (→ Vela)
- turn these receipts into an expense report (→ Alcor)
- send this invoice to the client for me
- charge the client's card / create a Stripe payment link
- what VAT rate should I charge? (tax advice)
- write a quote / proposal for this project
- chase this overdue invoice (collections email)
