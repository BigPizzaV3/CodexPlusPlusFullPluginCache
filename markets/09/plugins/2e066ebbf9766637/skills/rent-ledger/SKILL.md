---
name: rent-ledger
description: Rent ledger and prorated rent calculator for landlords. calculate_prorated_rent prorates move-in or move-out rent by actual days, 30-day month, and 365-day year. generate_rent_ledger builds a tenant ledger from lease terms and payments (typed or a CSV/Excel file) with prorated months, late fees by lease rule, oldest-first payment application, credits, a running balance, and PDF, Excel, and CSV downloads.
---

# LeaseLine Rent Ledger

Use `calculate_prorated_rent` when the user only needs a partial month's rent: "tenant moved in on the 17th, how much rent do they owe", prorated rent calculator, move-out proration.
- Pass `monthly_rent` and `move_in_date` and/or `move_out_date` as YYYY-MM-DD. If the user gives only a day ("the 17th"), use the current month and year and say so.
- Pass `method` only if the lease names one (`thirty_day`, `annual_365`); the result shows all three methods.

Use `generate_rent_ledger` for a rent ledger, tenant ledger, rent ledger template, proof of rent payments, a payment history, or "tenant paid 800 of 1200, what is the balance".
1. Required: `monthly_rent` and `lease_start` (move-in date, or the first month of the period the user wants). `as_of_date` is required: the date the user names, or today's date from the conversation.
2. Put each payment in `payments` (date + amount). A returned or bounced check is a negative amount on the day it bounced (e.g. -1450). If the user attached a CSV or Excel file of payments, pass it as `payments_file` instead of retyping it.
3. `late_fee` only from the user's lease terms. Grace: "5-day grace period" = `grace_days: 5` (fee on the 7th when due the 1st); "late after the 5th" = `grace_days: 4`. Do not invent a late fee the user did not state.
4. Other charges (utilities, pet rent, returned check fee) go in `other_charges` with a positive amount; concessions are negative. Do not add the security deposit as rent or a payment unless the user asks.
5. Use `payment_order: rent_first` if the lease or the user says payments go to rent before late fees.

Reply with the balance due (or credit) as of the date, total charged, paid, late fees, any unpaid months, each warning verbatim, and the PDF, Excel and CSV links (they expire in about an hour). Say once that late-fee limits vary by state and this is not legal advice.

Do not use these tools for legal questions (how much late fee a state allows, evictions), apartment searches, rent receipts for proof of address, or fake receipts. Do not ask for Social Security numbers or bank account numbers.
