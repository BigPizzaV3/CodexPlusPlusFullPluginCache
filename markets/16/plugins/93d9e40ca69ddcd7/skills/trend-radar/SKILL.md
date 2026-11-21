---
name: trend-radar
description: Find, measure and grade consumer and category trends with Statista Consumer Insights, Market Insights and Statistics, separating established shifts from emerging ones, weak signals and hype. Use whenever someone asks what the trends are in a category, for a trend report or trend scan, whether something is a fad, what to bet on for innovation or content, or which consumer shifts matter for next year's plan.
---

# Trend Radar

A trend is a change over time; a single data point is not one. This skill turns a topic into a short list of candidate shifts, measures each one over time against its parent category, and grades how strongly the data supports it.

## Inputs

| Input | Default if missing |
|---|---|
| Topic or category | Required. Ask if absent. |
| Markets | The country or countries named in the request |
| Look-back window | The last 3–7 years of actual data |
| Candidate trends | Generated in step 2, plus any the user names |

## Workflow

1. **Frame the topic** as a category plus a consumer need, e.g. "food & drink × health". This keeps the candidates relevant.
2. **Generate 6–10 candidates**, each named as a shift ("from X to Y") with a one-line definition. Draw them from three sources:
   - **Market Insights segments.** Look for segments whose revenue grows faster than their parent category. `search-statistics` returns compact single-country versions of these series. Their descriptions already state the latest value, the forecast and the change in growth, so they save fetch calls.
   - **Consumer Insights.** Look for questions that track a behaviour or diet over years. Call `fetch-consumer-insights` once per year with `year` set. Then read the "Changes in wording and/or filtering" note in the description: a wording change breaks the series.
   - **Independent statistics.** Use national statistics offices, panels or industry bodies (found with `search-statistics`) for adoption, production or sales series.
3. **Measure each candidate.** For each one record:
   - its level (share of consumers or share of the parent category's revenue);
   - its momentum (pp change, or CAGR compared with the parent category's CAGR);
   - how many independent sources agree;
   - its commercial pull;
   - the number of years in the series;
   - the latest and average yearly change.

   When two or more markets are in scope, also count the markets moving the same way.
4. **Grade** each candidate with `references/evidence-grading.md`: assign Established, Emerging, Weak signal or Not supported, and a direction. Apply the thresholds exactly. A measure you did not take counts as missing, never as passing. Check every Not supported trend: these results often make the most useful headline.
5. **Set watch indicators.** For each Emerging trend and Weak signal, name the metric and the threshold that would upgrade or retire it.

Before grading, make sure every candidate has a level. A missing level cannot reach Established or Emerging, so a well-supported trend with no level recorded will be under-graded. If the trend's own share is unavailable, use a proxy level as described in the reference file.

## Output

1. **Summary:** three sentences. Say which shifts are real, which are early, and which popular claims the data does not support.
2. **Radar table**, sorted by grade (Established first):

   | Trend | Grade | Direction | Level | Momentum | Corroboration | Pull | Years |
   |---|---|---|---|---|---|---|---|

   Level reads "x% consumers" or "x% revenue" (mark proxies). Momentum reads "+x.x pp" or "CAGR x.x% vs category y.y%". Every metric carries its years, market and source.
3. **Implications:** one line per Established or Emerging trend, aimed at product, proposition or content.
4. **Not supported:** the expected or hyped trends the data does not support, and why.
5. **Watch list:** indicator, current value and trigger threshold.
6. **Sources:** statistic IDs, Market Insights dataset IDs and Consumer Insights question IDs, each with the years used.

## Quality bar

- Compare like with like. Use only the years after the latest wording break. Survey waves are fieldwork windows that can overlap.
- Statistics derived from Market Insights are the same source as Market Insights. They count once towards corroboration.
- Attitude without behaviour is a weak signal at most. Say when stated interest is not matched by spending.
