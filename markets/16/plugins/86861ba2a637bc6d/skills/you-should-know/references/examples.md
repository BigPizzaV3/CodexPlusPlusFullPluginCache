# Worked notes

Eight notes that pass the bar, then four cases where the right answer is no note. Each figure in a note was computed with the calculator or a script before the note was written. No note body has more than 45 words.

## Contents

- Notes: 1 underperformer · 2 concentration before a renewal · 3 join that repeats deals · 4 partial month · 5 mixed currency · 6 sign flip · 7 paid twice · 8 total that does not tie
- No note: A already known · B below materiality · C advice, not data · D normal noise

## Notes that pass

### 1. Underperformer (You should know)

Request: "Which reps hit quota in Q3?" Files: `q3_deals.csv`, `quotas.csv`, `deals_2026.csv`. The answer gave 9 of 14 reps and a table of the five who missed.

```
---
**You should know**
**Dana Lee has missed quota three quarters running**
Dana reached 72% of quota in Q1, 64% in Q2 and 58% in Q3. Her Q4 pipeline is $495K against a $450K quota: 1.1× coverage, against 3.2× for the rest of the team.
```

- **Passes because:** the question was about one quarter, not the trend, and a coaching or hiring decision depends on it.
- **Figures:** `calc "261/450" --kind pct` gives 58.0%; `calc "495/450" --kind multiple` gives 1.1×.

### 2. Concentration before a renewal (You should know)

Request: "How did ARR move in Q3?" File: `subscriptions.csv`. The answer gave ARR up $1.3M to $21.4M, with the walk.

```
---
**You should know**
**Northwind Retail is 18% of ARR and renews on Dec 31**
Northwind pays $3.85M a year, the largest contract by far. Its seats fell from 420 to 360 since June. If it does not renew, ARR falls back below where it started the quarter.
```

- **Passes because:** a dated renewal is in the data, and losing it would undo the quarter's growth.
- **Figures:** `calc "3.85/21.4" --kind pct` gives 18.0%; `calc "21.4-3.85"` gives 17.55, below the $20.1M start.

### 3. Join that repeats deals (Heads up)

Request: "Total Q3 bookings by region. Join deals.csv with line_items.csv for the product mix." The answer gave $7.84M.

```
---
**Heads up**
**The join counts 38 deals twice**
deals.csv has one row per deal; line_items.csv has one row per product. The join repeats a deal's amount for each product. Those 38 deals add $1.12M. Summed on deals.csv alone, Q3 bookings are $6.72M.
```

- **Passes because:** the reported total is $1.12M too high, and the person chose the join, so they must choose the number.
- **Figures:** 38 deal IDs have two or more rows after the join; `calc "7.84-6.72"` gives 1.12.

### 4. Partial month (Heads up)

Request: "What's our gross margin for September? It's in gl_export.csv." The answer gave 64.2%, up 2.4 pts on August.

```
---
**Heads up**
**September stops on Sep 21**
The ledger export ends on Sep 21, so September has 21 of its 30 days. In August, 78% of freight and card fees posted after the 21st. On the same 21 days, August margin was 64.6%; it ended at 61.8%.
```

- **Passes because:** the margin will fall when the month closes, so 64.2% is not September's margin.
- **Figures:** the last posting date; August's freight and card fees after Aug 21 divided by August's total; August margin for Aug 1–21 and for the full month.

### 5. Mixed currency (Heads up)

Request: "Total invoiced revenue for Q3 from invoices.csv." The answer summed the `amount` column.

```
---
**Heads up**
**112 invoices are in GBP, summed as dollars**
invoices.csv mixes USD and GBP in one amount column. The 112 GBP invoices total £1.36M. At the 1.27 rate in fx_rates.csv, the total understates Q3 revenue by $367K.
```

- **Passes because:** the error is above materiality, and the fix needs a rate that the person should confirm.
- **Figures:** count and sum where the currency is GBP; `calc "1360000*(1.27-1)" --kind money` gives $367K.

### 6. Sign flip (Heads up)

Request: "Flux review: what moved between tb_aug.csv and tb_sep.csv?" Revenue led the answer.

```
---
**Heads up**
**Revenue changes sign between the two files**
tb_aug.csv shows revenue as credits (−$4.87M); tb_sep.csv shows it as positive ($4.95M). Compared as they are, revenue moved $9.82M. On one sign convention, it rose $80K (1.6%).
```

- **Passes because:** the top line of the review is wrong by $9.74M, and every revenue account is affected.
- **Figures:** `calc "4950+4870"` gives 9,820; `calc "4950-4870"` gives 80; `calc "(4950-4870)/4870" --kind pct` gives 1.6%.

### 7. Paid twice (You should know)

Request: "What did we spend with each freight vendor in August?" File: `payments.csv`. The answer gave spend by vendor.

```
---
**You should know**
**Three Coastal Freight invoices were paid twice in August**
INV-2231, INV-2240 and INV-2246 each appear twice in payments.csv, with the same amount and different payment dates. The duplicate payments total $41,200. A refund request would recover it.
```

- **Passes because:** money was paid twice and can be recovered, and the question was about spend, not about payment errors.
- **Figures:** group by vendor, invoice number and amount; `calc "18400+12950+9850" --kind money --unit 1` gives $41,200.

### 8. Total that does not tie (Heads up)

Request: "Summarise opex from pnl_export.xlsx for the board pack." The answer built $2,259K from the 14 opex lines.

```
---
**Heads up**
**The file's Opex Total is $45K more than its lines**
pnl_export.xlsx shows Opex Total as $2,304K. Its 14 visible lines sum to $2,259K. Hidden row 31, "Intercompany recharge", holds the $45K. The answer used the visible lines.
```

- **Passes because:** the board pack and the source file would differ by $45K, at materiality, and the person must decide whether the recharge belongs in opex.
- **Figures:** the sum of the lines from the script; `calc "2304-2259"` gives 45.

## No note

- **A. Already known.** Earlier, the person wrote "Dana is on a performance plan, leave her out." A later quota answer shows Dana's third miss. The finding is not new.
- **B. Below materiality.** A reconciliation leaves $3,000 unexplained on a $412,000 balance (0.73%), and materiality is $25K and 10%. If the question was about the reconciliation, mention the difference in the answer itself. It is not a note.
- **C. Advice, not data.** The data is clean and the answer is complete. "Consider a rolling forecast" is not about this data and changes no number.
- **D. Normal noise.** August marketing spend is 4% above its 12-month average, and monthly spend moves by up to 9% either way. There is nothing to act on.
