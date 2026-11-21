---
name: rank-by-icp
description: "Prioritize target companies in a Compelling list using an explicit weighted customer-fit rubric and a 0-100 account score. Use for best-fit prospects, lead scoring or deciding which companies to approach first (Zielkunden bewerten, Vertriebsprioritäten). General sales advice or explanations of ICP do not require ranking a list."
---

# Prioritize target accounts in Compelling

Ranking scores every account 0-100 from an **explicit rubric over insight columns** — no
black box. Costs 1 credit per account.

## Workflow

1. **Discover the columns** with `compelling_list_insights(record_type='accounts')` — you need each column's `question_id` and answer type. Rankable columns must exist and be researched first (see `enrich-contacts` / `build-tam-list`).
2. **Build the rubric with the user.** For each column pick exactly ONE points spec, matching its type, points 0-10:
   - `value_points` — for `boolean`, single-choice, and `tamCriteriaMatch` columns: map each value to points (e.g. `{"true": 10, "false": 0}`).
   - `range_points` — for `integer` columns: numeric ranges to points (e.g. 50-200 employees → 10).
   - `choice_points` — for multiple-choice columns: points per selected option.
   Weight what actually predicts fit; 3-5 columns beat ten noisy ones.
3. **Offer a cost preview** with `compelling_estimate_credits(action='rank_list')` (1 credit x accounts in the list).
4. **Start scoring** with `compelling_rank_list(weights=[...])`. Asynchronous — pass `wait_seconds` or long-poll `compelling_ranking_status`.
5. **Explain the criteria and weights**, including which researched company values drive fit.
   Distinguish customer-fit scores from confirmed purchase intent; missing research is unknown.
6. **Read the ranked list**: `compelling_read_list(record_type='accounts', sort_by=<ranking question_id>, sort_dir='desc')` for top-N by fit. The ranking column's `question_id` is returned by `compelling_rank_list` / `compelling_ranking_status`.

## Pitfalls

- Accounts-only: contacts cannot be ranked.
- A column with unresearched values contributes nothing for those accounts — enrich first, rank second.
- Ranking columns themselves cannot be ingested or re-ranked; re-run `compelling_rank_list` with a new rubric to re-score.
- Present the rubric back to the user before starting — the scoring is only as good as the agreed weights.

## DACH examples

Customer criteria may include country, employee count, SAP usage or a researched certification.
Use the user's actual rubric; do not assume that a DACH location or any single signal means a
company is ready to buy. Present results in the user's language.
