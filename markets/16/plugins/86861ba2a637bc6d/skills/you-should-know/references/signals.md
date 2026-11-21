# Signals to check

Run through these signals after a data answer, in order. Stop at the first finding that passes the bar in SKILL.md. Prove each finding with code before writing about it.

| Signal | Check with code | Tag |
| --- | --- | --- |
| A person, customer, product or region far from the rest, or off for several periods in a row | Rank against the median. Compare the last three periods | You should know |
| One customer, vendor or SKU above about 15% of a total, with a date attached (a renewal, a contract end) | Share of the total, then the dates in the same file | You should know |
| A deadline in the data, such as a renewal or a covenant test | Dates in the next 90 days, joined to the amounts | You should know |
| A join that repeats rows | Count rows per key before and after the join | Heads up |
| A period that ends early or starts late | The first and last date against the period's calendar | Heads up |
| More than one currency or unit in one amount column | Distinct values of the currency column, and the symbols in the amounts | Heads up |
| The same account or line with opposite signs in two files | Compare the signs of the largest lines across the files | Heads up |
| The same invoice, payment or transaction twice | Group by number, party and amount | Heads up, or You should know when money was paid twice |
| A total row that differs from the sum of its lines, or a trial balance that does not balance | Recompute the total; sum debits minus credits | Heads up |
| An assumption in the answer that changes the figure, such as a rate, a cut-off date or an exclusion | Run the figure again without the assumption | Heads up |
