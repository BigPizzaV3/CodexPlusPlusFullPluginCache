# The Financial GPS framework and the federal loan rules since July 1, 2026

**Rules last checked:** September 26, 2026, against P.L. 119-21, the Department of Education's final rule (91 FR 23768), 34 CFR 685 and studentaid.gov. If today is past a date in "Dates that change things" below, call `get_loan_rules` and trust its result over this file.

Rates, fees, the poverty guideline and its year change every year. They are not in this file on purpose: read them from `get_loan_rules` or from the check results, and name the year.

---

## The idea

Defaults are a cash-flow problem that hits when repayment starts, not an earnings problem. So the framework measures **slack**: what's left of a graduate's pay after basic living costs and the loan payment. Slack decides whether someone can make payments, save and absorb a bad month.

The framework rejects:
- gross or median earnings with no living costs;
- school-wide affordability claims (the program drives slack, not the school);
- debt alone or earnings alone;
- "the median debt is manageable, so it's manageable for you".

It centers:
- programs, not schools;
- income above a basic allowance, not raw pay;
- the first years of repayment;
- family debt: Parent PLUS counts alongside the student's loans.

---

## One yardstick for every loan

Affordability is judged on **the payment that clears the debt in ten years** at the current federal rate. It's a yardstick, not a repayment plan.

- New borrowers aren't on a "standard 10-year plan": the new standard plan's term depends on the balance (below).
- One yardstick keeps schools, programs, student loans and Parent PLUS comparable.
- Billing plans (the tiered standard plan, RAP) come in only when someone is choosing a plan. Version 1 of the tools calculates one bill: the standard plan's for Parent PLUS, in `parent_check` and `family_check`. It doesn't calculate RAP or a standard-plan bill for a student's own loans.

Two details the tools handle, worth knowing when explaining results:
- A school's **median debt** is a sum of loan amounts, which already include the origination fee, so it's amortized as is.
- When the tools model **borrowing year by year**, they turn cash needed into a loan (`loan = need ÷ (1 − fee)`), apply the federal annual limits, treat anything above them as private borrowing, and add interest from each disbursement until repayment starts six months after graduating.

## The allowance (basic living costs)

```
Students: share = (10-year payment × 12) ÷ (earnings − 150% of the poverty guideline for one person)
Parents:  share = (10-year payment × 12) ÷ (household income − 200% of the guideline for a household of three)
```

- The tools return the allowance and **its year**. Name the year whenever a share appears.
- The allowance is a national figure. It doesn't know that rent in San Francisco is triple Indianapolis's; say so when it matters.
- It's the framework's own baseline, not the line federal plans use for new loans (RAP takes a share of total income).

## Tiers

The share is classified **as displayed**, rounded to one decimal place, so a "12.0%" is never labeled Good.

**Students** (graduate's pay, four years after graduating):

| Share | Tier | What it means |
|---|---|---|
| under 8% | **Excellent** | Room for error; could pay it off faster than ten years |
| 8% to under 12% | **Good** | Manageable to pay off in ten years |
| 12% to 20% (20.0% included) | **Concerning** | On the edge: likely a longer term or an income-based plan |
| over 20%, or pay at or below the allowance ("no room") | **High risk** | Repayment likely stretches for decades |

**Parents** (household income, household of three):

| Share | Tier |
|---|---|
| under 6% | **Safe** |
| 6% to 10% (10.0% included) | **Caution** |
| over 10%, or no room | **High pressure** |

The parent scale is stricter because new Parent PLUS has no income-driven fallback, and payments often run into retirement.

Use these exact labels, in sentence case, and attribute them: "By College Azimuth's measure, that's Concerning."

## Earnings

- The figure is earnings **four years after graduating**: downside, typical and upside for the school.
- A field's typical figure is its median; its downside and upside are scaled from the school's spread, and the tools say so.
- These are medians, so half of graduates earn less. One-year program earnings aren't available.

---

## Federal loan rules for loans made on or after July 1, 2026

**Repayment plans for new loans:** the new standard plan or RAP. IBR, PAYE and SAVE aren't available for them.

**The new standard plan (tiered)** sets the term by the total principal when repayment starts:

| Owed when repayment starts | Term |
|---|---|
| under $25,000 | 10 years |
| under $50,000 | 15 years |
| under $100,000 | 20 years |
| $100,000 or more | 25 years |

The minimum payment is $50 a month. Payments on this plan don't count toward PSLF. It's the default for new loans.

**RAP (Repayment Assistance Plan):**
- The payment is a percentage of **total** AGI, set by $10,000 band and not marginal: 1% for $10,000–$20,000, rising one point per band to 10% above $100,000. AGI of $10,000 or less pays $10 a month.
- Subtract $50 a month per dependent. The minimum is $10 a month. Joint filers use combined AGI.
- On an on-time payment, unpaid interest is waived, and principal falls by at least the smaller of $50 and the payment.
- There's no cap: unlike IBR, a high earner's RAP payment can exceed the standard plan's.
- What's left is forgiven after 360 payments (30 years), and that forgiveness is taxable.
- Describe RAP as a trade-off: it can make payments manageable and stops the balance growing when payments are on time, but it can run 30 years and the forgiveness is taxed. Don't recommend it or rule it out for anyone.

**The switch:** a borrower whose loans were all made before July 1, 2026 can stay on the older plans. Any new Direct loan, including a consolidation or a Parent PLUS for a younger child, moves **all** of that borrower's loans onto the new plans once it enters repayment.

**Older loans:**
- IBR remains for borrowers with only pre-July-2026 loans (10% of income above 150% of the guideline, or 15% for some older borrowers, never more than the 10-year payment).
- SAVE ended by court judgment on March 10, 2026; its borrowers are being moved through about March 2027.
- PAYE and ICR end June 30, 2028.

**Parent PLUS made on or after July 1, 2026:**
- Limits: $20,000 a year and $65,000 per student, counting every parent who borrows for that student.
- The new standard plan only: no RAP, no income-driven plan and no PSLF.
- Interest deferred while the student is in school is added to the balance when the deferment ends, and that larger balance sets the term. For example, $24,000 borrowed becomes about $30,530 and bills over 15 years, not 10.
- Older Parent PLUS can reach an income-driven plan only through a consolidation disbursed before July 1, 2026 (then ICR, then IBR).

**Student loan limits:**
- Dependent undergraduates: $5,500 / $6,500 / $7,500 / $7,500 for years one to four.
- When parents can't get Parent PLUS: $9,500 / $10,500 / $12,500 / $12,500.
- Grad PLUS has ended for new borrowers.
- Students who were enrolled and borrowing before July 1, 2026 keep the old limits through 2028–29 at the latest.
- Anything above the limits is private borrowing, priced on credit and usually cosigned. Private rates are an assumption (14% working figure, 11.3–18% range) until there's lender data.

**Other changes:**
- **Deferment:** loans disbursed from July 1, 2027 get no unemployment or economic-hardship deferment, and forbearance is capped at 9 months in any 24.
- **Capitalization:** none when repayment starts. Interest capitalizes only after a deferment on unsubsidized loans, which includes Parent PLUS in-school deferment.
- **Forgiveness:** taxable as income from 2026, except PSLF and death or disability discharges.

## Dates that change things

| Date | What changes |
|---|---|
| October 21, 2026 (done) | The tools moved to the 2026 poverty guideline; payments didn't change, allowances and shares did |
| Mid-January 2027 | HHS publishes the 2027 guideline, which College Azimuth adopts in its next data release |
| ~March 2027 | SAVE transfers finish |
| May 2027 | 2027–28 federal rates are set; until the tools carry them, they say loan terms aren't available |
| July 1, 2027 | Deferment and forbearance limits apply to new disbursements |
| June 30, 2028 | PAYE and ICR end |
| After 2028–29 | Grandfathered loan limits end |

---

## Terms

| Concept | Say | Avoid |
|---|---|---|
| Money left after basics and the payment | **slack**, "money left each month" | buffer, cushion, margin |
| Income-driven plans as a group | **income-driven repayment** | "IBR" as an umbrella term |
| The plan for new loans | **RAP** (Repayment Assistance Plan) | calling it IBR or SAVE |
| The 10-year figure | **the 10-year payment** (a yardstick) | "standard 10-year plan" |
| The allowance | **150% of the {year} federal poverty guideline** (200% for a household of three, for parents) | "poverty line" with no year |
| What drives burden | **the program** | "the school's affordability" |
| Parent PLUS | **family debt** | folding it into the student's figure |

## Rewrites of claims that are now wrong

Users, counselors and older articles still repeat pre-July rules. Correct them plainly.

| Old claim | Current wording |
|---|---|
| "IBR caps payments at 10% of discretionary income" | "For new loans, RAP sets payments at 1% to 10% of total income, minus $50 a month per dependent. IBR's rule now applies only to borrowers whose loans all predate July 2026." |
| "Parent PLUS can use ICR" | "Parent PLUS made after July 1, 2026 has no income-driven plan and no PSLF: only the standard plan, with a term set by the balance." |
| "Parent PLUS has no borrowing cap" | "New Parent PLUS is capped at $20,000 a year and $65,000 per student, across every parent who borrows for that student." |
| "on a standard ten-year repayment plan" | "if repaid over ten years" (the 10-year payment is a yardstick; the new standard plan runs 10 to 25 years by balance) |
| "IBR forgives after 20–25 years" | "RAP forgives after 30 years of payments, and that forgiveness counts as taxable income except under PSLF." |
| "SAVE is in litigation" | "SAVE was ended by a court in 2026; PAYE and ICR close by July 2028." |

## The point of view behind the numbers

1. A framework for thinking, not a guarantee. The tiers describe typical outcomes, not any one person's.
2. Where you live changes the floor. The allowance is national.
3. Households differ. One person for students, three for parents; anyone supporting others needs more room.
4. Other debts compete for the same slack.
5. You're not the median. Half of graduates earn less.
6. Income-driven repayment is a trade-off, not a free pass.
7. Don't build a plan on forgiveness. It's taxed, and three plans closed or are closing between 2026 and 2028.
8. The program, not the school, sets your slack.
9. Parent PLUS is family debt, now with caps and no income-driven safety net.
