---
name: visibility-change-explainer
description: Use when the user asks why their AI visibility went up or down, what changed this week or month, a sudden drop or spike, or whether a change is real.
---
# Visibility change explainer
1. list_workspaces. Then get_visibility_trend, with resolution=week or day for the period in question.
2. get_visibility_score for the current window and its comparison, which includes the per-model change.
3. For the models or questions that moved: get_prompt_performance on the affected questions, and get_ai_answers filtered by that model and period, to compare answers before and after.
Output:
- what moved, by how much and where (models, questions);
- whether the sample is large enough to trust;
- the evidence-based explanations you can see in the answers, such as new competitors named or different sources cited;
- what to watch next.
Separate observations from hypotheses. Correlation is not causation.

