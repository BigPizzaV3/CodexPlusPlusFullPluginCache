---
name: get-started
description: How to estimate a private company's 409A or HMRC share value with the Codon Valuation tools, which inputs to collect, and how to present the result.
---

# Estimating a share value with Codon Valuation

Use `estimate_409a_value` for a US company (value per common share in US dollars) and `estimate_emi_share_value` for a UK company (value per ordinary share in pounds sterling). Use `get_formal_valuation_info` when the user asks what a formal 409A or EMI valuation involves, what documents are needed, or how to request one.

## Collect the inputs first

Ask for what is missing before calling an estimate tool. The minimum is the number of common or ordinary shares and either a priced round or some financial figures:

- Share classes: common/ordinary share count; each preferred class with its share count, price per share and how many months ago it was priced.
- Outstanding options: total count and weighted average exercise price, if any.
- Finances: trailing twelve-month revenue, cash, debt and total capital invested, whichever are known.
- Sector, so the right volatility and revenue multiple assumptions are used.
- For an older priced round: whether the company is ahead of, on, or behind the plan it raised on.
- Any SAFEs or convertible notes: say so, because they lower the stated confidence.

Do not ask for, or pass, names, email addresses or other personal information. The tools do not need them.

## Present the result

Report the low, mid and high value per share, the method used and its confidence, and the key assumptions returned by the tool. Keep the tool's disclaimer: the figure is an indicative planning estimate, not a 409A valuation, not safe harbor protection, and not a value agreed with HMRC. If the user wants a formal valuation, use `get_formal_valuation_info` rather than describing the process yourself.
