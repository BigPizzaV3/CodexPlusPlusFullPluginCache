---
name: visibility-status
description: Report how visible a brand currently is in AI assistants' answers, using 3RD. Use when the user asks how visible they are, what their AI visibility score is, or how it changed against the previous period.
---

Use this skill to answer "how visible are we?" from 3RD's measurements.

1. Call `list_brands` and take the `brandId`. If the account has several brands and the user did not name one, ask which brand they mean. Never guess a brand from a name or a URL.
2. Call `get_visibility_breakdown` with the `brandId`. It returns the overall visibility score and the scores per prompt type (must-win, core, foundation).
3. Call `get_highlights` with the same `brandId` for sentiment, citation share and the direction against the previous period.
4. Answer with:
   - the overall score, exactly as returned;
   - the must-win, core and foundation scores;
   - the direction against the previous period, only when `status` is up, down or neutral (when it is unknown, say there is nothing to compare with);
   - the period the numbers cover. Without dates both tools report the last 30 days; say so.

Do not average, round differently or recompute any score. A score of 0 with no measured prompts means "not measured yet", not "invisible". If the user names a period, pass it as `fromDate` and `toDate` (YYYY-MM-DD) to both tools.
