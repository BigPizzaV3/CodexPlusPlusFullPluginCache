# Award letters

An award letter is the most useful thing a family can bring: real prices beat school averages. It's also where loans get dressed up as aid. This file covers getting the numbers, classifying each line, and passing the results to the checks.

## Getting the numbers

Ask for a few figures from each letter, not the whole document. Adapt the wording; don't read it out:

> "To use your actual offer instead of averages, I need a few numbers from each letter: the total cost of attendance (or tuition, housing and other costs listed), every grant and scholarship, each loan with its name (Direct Subsidized, Direct Unsubsidized, Parent PLUS, private), and any work-study. Are the amounts per year or per semester?"

Ask only for what's missing when the user has already given some numbers.

If the user pastes the whole letter as text:
1. Don't ask them to re-enter it.
2. Extract each line with its amount.
3. Show what you extracted and how you classified it, and ask whether it looks right.
4. Once confirmed, call `review_award_letter`.

If there's no letter yet, run the checks on the school's figures (the defaults are marked `assumed`) and say that the numbers will change once the letter arrives.

## Classifying each line

`review_award_letter` takes each line as `{label, amount, kind}`. Classify from the label; ask when it's ambiguous.

| What the letter says | `kind` |
|---|---|
| Total cost of attendance, "estimated cost", "budget" | `cost_of_attendance` |
| Tuition and fees | `tuition_fees` |
| Housing, room and board, food, meal plan | `housing_food` |
| Books, transport, personal, other listed costs | `other_cost` |
| Pell Grant, SEOG, state grant (Cal Grant, MAP and so on), institutional or need-based grant | `grant` |
| Merit scholarship, named scholarship, outside scholarship | `scholarship` |
| Tuition waiver or remission | `tuition_waiver` |
| Federal Direct Subsidized Loan | `federal_subsidized` |
| Federal Direct Unsubsidized Loan | `federal_unsubsidized` |
| Parent PLUS, "parent loan" | `parent_plus` |
| Alternative or private loan | `private_loan` |
| A loan from the school itself | `institutional_loan` |
| Federal or state work-study | `work_study` |
| Anything else | `other` |

Rules that matter:
- **Grants, scholarships and waivers are aid. Loans and work-study are not.** Net price is cost minus grants, scholarships and waivers, never minus loans.
- **Don't double-count costs.** If the letter gives a total cost of attendance and also its parts, pass the total and leave out the parts, or pass the parts and leave out the total.
- **Semester and quarter amounts:** set `amounts_period` to `semester` or `quarter`; the tool annualizes. If the numbers look like half a year's costs and the letter doesn't say, ask.
- **`year_in_school`** matters for the federal limits ($5,500 in year one rising to $7,500, or $9,500 to $12,500 when parents can't get Parent PLUS).

## What the review returns

- **`annualized`**: cost of attendance, gift aid, net price, federal loans, Parent PLUS, private loans and work-study, per year.
- **`flags`**, each with a message. Explain them in plain words:
  - `loan_shown_as_aid`: a loan sits among the aid, or the letter's "aid" total includes loans. Loans have to be repaid.
  - `parent_plus_in_package`: the package assumes the parents borrow. That's the parents' debt, capped at $20,000 a year and $65,000 per student for loans made after July 1, 2026, with no income-driven plan. Show what it costs with `parent_check`.
  - `work_study_not_guaranteed`: work-study is paid as the student works; it isn't a discount on the bill.
  - `federal_over_annual_limit`: the federal loans listed exceed the limit for that year. Ask whether the student was already borrowing before July 1, 2026 (older limits may apply through 2028–29) or whether the letter is wrong.
  - `plus_over_annual_cap`: the Parent PLUS listed is above $20,000 a year. Same question about older loans; otherwise the rest needs another source.
  - `no_cost_listed`: no cost line, so no net price. Ask for the cost of attendance.
  - `annualized_from_semester`: amounts were doubled (or tripled for quarters); confirm.
  - `grant_renewal_unknown`: ask the aid office whether each grant renews every year and on what conditions (GPA, credits, income).
- **`suggested_inputs`**: the values to pass to the checks.

## Passing the results to the checks

**Use `suggested_inputs`, not the letter's raw loan figures.**
- `student_check.borrow_per_year` is the cash the student receives. Letters list loan amounts, which already include the origination fee. The review converts them; passing a letter's loan amount straight to `student_check` would add the fee twice.
- `parent_check.plus_per_year` is the Parent PLUS loan amount, which is what the letter lists. The review passes it through.

Then:
1. Run `student_check` for the school (and field) with the suggested borrowing.
2. If Parent PLUS appears, run `parent_check` with the household income (ask for it) and the suggested PLUS amount.
3. Lead with what the letter really asks of the family: the net price per year, how much of it is loans, and what those loans cost to repay.

## Questions worth taking to the aid office

Offer the ones that fit:
- Does each grant renew every year, and on what conditions?
- Does the package assume Parent PLUS? What happens if the parents are denied or won't borrow?
- Is there room to appeal, given another school's offer or a change in income?
- What does the cost of attendance include, and how is it likely to change after year one?

## Comparing letters

Run `review_award_letter` once per letter, then `student_check` (and `parent_check`) per school with each letter's own suggested inputs. Here, unlike `compare_schools`, the inputs differ by school on purpose because each offer is different; say so in the answer. Follow `comparisons.md` for framing.
