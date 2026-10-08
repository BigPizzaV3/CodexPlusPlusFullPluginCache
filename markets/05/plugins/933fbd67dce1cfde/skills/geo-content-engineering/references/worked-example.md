# Worked example: rebuilding a guide paragraph

A full before/after rebuild with a rule map. All numbers and program names below
are fictional illustrations of the structure, not real figures.

## Before: a typical guide paragraph

### Rebates

Basically there are various ways to get help paying for the purchase. These can
differ quite a lot depending on where you live and they change relatively often,
so it is worth checking regularly. As the chart below shows, the savings can be
substantial. It depends on many factors, such as where it is installed and which
provider you choose. In some cases the installation itself is also covered, which
makes the whole thing even more attractive.

### Why this fails

| Problem | Rule broken |
| --- | --- |
| "the purchase," "the whole thing" instead of the entity | Entity-first |
| Not a single number, program, or amount | Citation-worthiness zero |
| "as the chart below shows" with no text anchor | Block loses meaning on extraction |
| "it depends on many factors" with nothing named | Vague evasion |
| No date marker on a time-sensitive topic | Recency ignored |
| Heading "Rebates" instead of a question | Prompt language missed |
| Filler: "basically," "relatively," "quite a lot" | Language rules broken |

## After: rebuilt to the rules

### How much is the home EV charger rebate in 2026?

As of 07/2026: the home EV charger rebate is up to 600 dollars per charge point
for private installations under the federal program. State and local programs add
between 200 and 500 dollars on top, depending on where you live. The rebate
calculator shows that with combined federal and local support, the purchase cost
of an 11 kW charger drops by up to 45 percent.

### Which rebate fits which case?

The right path depends on installation site and ownership:

- Owned home with a private parking spot: federal program plus local top-up,
  combinable.
- Rented apartment with a garage spot: local program for renter installations;
  the federal program requires the owners' association to approve.
- Company parking lot: commercial program with its own rate of 900 dollars per
  charge point.

### What changed?

- 07/2026: local top-up in the example city raised from 300 to 500 dollars.
- 05/2026: installation cost added to the federal program.

## Rule map

| Element in the after text | Applied rule |
| --- | --- |
| "home EV charger rebate" instead of "the purchase" | Entity-first, `chunking.md` |
| Answer in the first sentence, details after | Inverted pyramid |
| "As of 07/2026" in the body text | Date marker, `recency.md` |
| Concrete amounts and percentages | `citation-worthiness.md` |
| "The rebate calculator shows ... 45 percent" | Text anchor for multimedia |
| Question-form H2 headings | Prompt language, `query-fan-out.md` |
| Case split by installation site | Condition block, `chunking.md` |
| "What changed" block | Update box, `../assets/update-box.md` |
| Each H2 block understandable alone | Self-containment |
