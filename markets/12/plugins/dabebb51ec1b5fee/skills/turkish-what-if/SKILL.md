---
name: turkish-what-if
description: Calculate what a past Turkish lira amount in gold, dollars, euros, BIST 100, bonds or a deposit is worth today after inflation. Use for 'keşke … alsaydım' questions and real returns in Türkiye.
---

This skill covers "what if" questions about Turkish lira savings, which users usually ask in Turkish ("keşke 2015'te altın alsaydım", "2020'de 100 bin TL ile dolar alsaydım bugün ne olurdu", "2015'teki 10.000 TL bugün kaç TL"), and questions about how the six assets did over a period ("geçen ay hangi yatırım aracı ne kazandırdı"). The user's own instructions come first.

## Inputs

- **An amount in lira** (`amount_tl`), paid every month (plan monthly, the default) or once (plan once). "100 bin TL" is 100000.
- **A start month** (`start_month`, YYYY-MM): "since 2020" is 2020-01, "in 2018" is 2018-01. The data starts in January 1997; government bonds (DİBS) start in January 2005.
- Optional: an end month (`end_month`, the latest TÜİK month when absent), the assets (gold, usd, eur, bist100, bonds, deposit; all six when absent), `increase_with_inflation` for a monthly amount given in today's lira, and the language (tr for a user writing in Turkish, en otherwise).

## Flow

1. A what-if question goes to `calculate_what_if`. Its result gives each asset's value at the end month's average (`value_tl`), the gain or loss after inflation (`real_return_pct`, `real_gain_tl`), the same payments kept as TL cash, and the payments restated in end-month lira (`paid_in_today_tl`). That last figure also answers "what is an amount from a past year worth today".
2. A question about a period (last month, the last 12 months, a calendar year) goes to `show_real_returns`, with `start_month` and `end_month` or a year. With no dates it covers the last 12 published months.
3. Each result ends with a summary suitable to show the user, in the user's language, with the figures, the source (Kaynak: TÜİK) and the not-advice note. The card shows the chart; the user can change the amount and the months in it.

## Scope

- The figures are past, hypothetical results computed from TÜİK's monthly data. Each payment buys at its month's average level; deposits are gross, BIST 100 excludes dividends, and no fees or taxes are applied.
- Keşke gives no investment advice: no recommendations, no ranking of what to buy and no forecasts. Live prices and exchange rates are outside it.
- A result with a refusal (a month before the data, an end month before the start) carries a sentence for the user that says what happened.
