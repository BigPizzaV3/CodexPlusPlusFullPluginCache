# Comparing schools

A comparison is only fair when every school gets the same assumptions. It's only useful when it shows what each choice trades away.

## Run it the same way for every school

- Use `compare_schools` with two to four slugs and **one** set of inputs: the same `borrow_per_year`, earnings scenario, private rate and Parent PLUS assumption.
- For a field, pass one `cip4`. If a school doesn't serve earnings for that field, the row falls back to all fields and the notes say so; repeat that note in the answer.
- With a household income, the comparison adds each school's estimated net price at that income and, with `plus_per_year`, the parent's share and tier.
- When the user has award letters, the inputs differ by school on purpose (see `award-letters.md`). Say that the schools are being compared on their own offers.

## Frame it conditionally

Never number the schools or name a winner. Tie each edge to what the user cares about:

- "If keeping the monthly squeeze low matters most, [school A] has the edge: the same borrowing leaves [money left] a month at typical pay, against [money left] at [school B]."
- "If the higher-paying field is the point, [school B]'s graduates in it earn more four years out, so the same borrowing takes [share] of pay above basic expenses instead of [share]."

The bracketed figures always come from the tool results; these are patterns, not numbers to reuse.

List schools in the order the user named them, not sorted by tier.

## Show the downside

The typical case flatters every school. When the gap between schools is small, or a result is Concerning or worse, rerun with `earnings_scenario: "downside"` and say what changes. A choice that only works at median pay is a different choice from one that works at the downside.

## Program over school

The field usually moves the result more than the school does. When a user compares schools with no field in mind, say that the comparison uses all fields and that a specific field could change the order of what matters. Offer to rerun with a field from `get_school`.

## Parent PLUS in comparisons

Put the student's and the parents' results side by side; don't add them into one tier. A school that looks affordable for the student can lean on Parent PLUS. When `parent_check` shows a plan above the caps, say how much has to come from somewhere else.

## Questions the tools can't settle

- **"Is the expensive school worth it?"** Version 1 has no value-added or break-even tool. Show what each school's numbers are, say what the price difference buys in debt and payment, and leave the judgment with the family. Don't compute break-even years by hand.
- **"Which school should I pick?"** That depends on things the data can't measure: fit, support, where they feel at home. What the tools can say is how much room for error each choice leaves.
- **Prestige, campus life, rankings:** outside the tools' data. Say so and bring it back to cost and earnings.

## Schools that look bad on the numbers

Some schools serve students with less financial cushion: they borrow more, and the payment math gets harder. That's a consequence of who the school serves and how it's funded, not a verdict on the school. When a school serving many Pell students or an HBCU shows a high share, name what the data measures and what it doesn't, without framing it as an indictment.
