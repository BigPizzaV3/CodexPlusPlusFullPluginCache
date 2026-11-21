# Pattern 16: Cost Ledger (imported from the accounting system)

The Gather API carries no cost data. The **value** side of a CVR comes from records priced at
Pattern 14 rates; the **cost** side comes from the user's accounting/cost system (COINS, Eque2,
Sage, or a cost spreadsheet). `$cost-import` parses a ledger export and writes a
normalised local cache that `$cvr` (and any future cost-shaped skill) consumes.

**File convention:** `commercial/cost-ledger.md` in the working directory. Created and updated
ONLY by `$cost-import`. Contains: provenance (source system, filename, ledger period
end / data date, currency, whether figures are period or cumulative, whether commitments and
accruals are included), a cost table by **user-confirmed CVR head** (labour, plant, materials,
subcontract, prelims/staff, other) with period and cumulative columns where the export carries
them, and the **user-confirmed mapping** between the ledger's cost codes and those CVR heads.

**Rules for consuming skills:**
1. Costs are **as stated in the ledger — never invented, scaled, or interpolated**. A cost head
   the export doesn't carry is "not in the imported ledger", not an estimate. Cite figures as
   "per the imported cost ledger ([source system], period to [date])".
2. **Column semantics are user-confirmed at import** — period vs cumulative vs committed is
   confirmed by the user, never guessed by a consumer. Guessing is the classic double-count.
3. Accruals, subcontract liabilities, and provisions are **user-supplied adjustments**,
   presented as distinctly-labelled lines — never derived from the ledger or the records.
4. Absent file → cost-shaped outputs degrade to value-side-only, with the cost column reading
   "no cost ledger imported — run $cost-import". Never block the value side on it.
5. Only `$cost-import` writes the file. A ledger whose `project` does not match the
   project being analysed is ignored (say so).
6. The file is commercially sensitive — same handling as Pattern 14 rule 5: keep it out of
   shared repositories, and outputs destined for the other party never include the cost side
   (a CVR is an internal management document).
