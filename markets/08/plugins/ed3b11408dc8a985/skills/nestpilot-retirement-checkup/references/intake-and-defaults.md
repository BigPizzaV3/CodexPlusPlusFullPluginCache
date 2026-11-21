# Intake And Defaults

Use this reference before calling `start_retirement_checkup`.

## Core Inputs

Collect and validate all of these values:

| Input | Valid value | Handling |
|---|---|---|
| Current age | Integer 18-100 | Do not request an exact birth date. |
| Intended retirement age | Integer 50-80 and not below current age | Ask for a corrected age when invalid. |
| Filing status | `single` or `married` | Use the tool's exact enum. |
| Total retirement savings | Dollars, zero or greater | If itemized accounts are provided, use their confirmed sum and explain that the account list supersedes the total. |
| Current annual income | Dollars, zero or greater | Use primary income only. Keep spouse income separate. |
| Intended annual retirement spending | Dollars, greater than zero | Use annual spending, not monthly spending. |
| Spouse age | Integer 18-100 | Required when filing status is married. |
| Spouse retirement age | Integer 50-80 and not below spouse age | Required when filing status is married. |

Ask for all missing core values together in one compact intake turn. Do not
open the checkup until every applicable core value is known and valid.

## Focused Analysis Facts

The plan facts are current age, planned retirement age, filing status, the
primary person's income, annual spending, and savings; when married, also the
spouse's age, planned retirement age, and income, with 0 only when the user
said so; for a claiming question, also the benefit estimates at full
retirement age. A focused claiming analysis needs the user's own benefit
estimate above 0, or the question uses the explorer instead; a focused
retirement-age analysis needs someone still earning, or explain that no
retirement age is left to compare.

A focused review keeps its button disabled until every plan fact is given. A
value of 0 counts as given; an omitted value does not. Pass the spouse's income
as `spouseSalary`, and `0` only when the user said the spouse has none.

## Optional High-Impact Inputs

Invite these once before launching the review. Let the user skip them.

| Input | Valid value | Default or omission effect |
|---|---|---|
| Primary Social Security benefit at full retirement age | Monthly dollars, zero or greater | `$0`; the baseline is incomplete until the user supplies an SSA estimate. |
| Primary claiming age | Integer 62-70 | `67`. |
| Spouse Social Security benefit | Monthly dollars, zero or greater | `$0`. |
| Spouse claiming age | Integer 62-70 | `67`. |
| Primary or spouse pension | Annual dollars, zero or greater | Omitted. |
| State | Two-letter US abbreviation | State income tax is not modeled. Ask only when state-tax modeling is material; do not infer it from other information. |
| Itemized accounts | Traditional, Roth, or taxable balances and owner | All savings use one traditional pre-tax bucket. Cash, checking, ordinary savings, money-market, and brokerage balances map to taxable. |
| Primary or spouse life expectancy | Integer 60-110 | Planning horizon age `95`. |
| Expected real return | Decimal -0.10 to 0.15 | `0.02`, or 2% real. |
| Inflation | Decimal 0 to 0.15 | `0.03`, or 3%. |
| Spouse salary | Annual dollars, zero or greater | Omitted. Do not combine it with primary income. |
| Supplemental income | Monthly rental, annuity, or other income with optional start/end ages | None. Do not duplicate salary, Social Security, or pension here. |
| Roth conversion policy | `conservative`, `moderate`, `aggressive`, `optimized`, or `none` | `conservative`. Offer `optimized` when the user wants modeled ACA subsidy and Medicare IRMAA effects included in conversion sizing. |

When passing percentages to a tool, convert them to decimals. For example,
pass 2% as `0.02`.

## Material Omission Language

Use direct language for defaults that materially limit the result:

- No Social Security estimate: "No Social Security estimate was entered, so
  the forecast models a $0 monthly benefit. Add the estimate from your SSA
  statement to make the baseline more complete."
- No account mix: "The forecast treats all savings as one pre-tax account.
  Adding traditional, Roth, and taxable balances would improve withdrawal and
  Roth-conversion modeling."
- No state: "State income tax is not modeled."
- No life expectancy: "The planning horizon defaults to age 95."

Do not describe an omitted material input as if the user supplied it.

## Launcher Contract

Before calling `start_retirement_checkup`:

1. List the user-provided and directly derived values.
2. List defaults separately.
3. Include "Expected real return: 2%" when the user did not override it.
4. Explain any material omission using the language above.
5. If a Roth follow-up is relevant, show "Roth policy: conservative" unless
   the user selected another policy, and mention that `optimized` considers
   modeled ACA and Medicare effects.
6. Pass the supplied facts to the launcher. The persistent UI shows the review
   and requires the user to click **Run my checkup**, or, for a focused
   analysis, that analysis's button.

Do not silently infer financial values. Simple unit conversion or summing
itemized balances is allowed when shown to the user before launching.
