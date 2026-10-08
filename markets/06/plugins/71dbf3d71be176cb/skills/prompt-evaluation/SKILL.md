---
name: prompt-evaluation
description: Build practical tests and rubrics for comparing prompt behavior.
---

# Prompt Evaluation

Apply when the user asks whether a prompt works, how to compare versions, or how to test regressions.

1. Translate desired behavior into measurable criteria and identify failure modes.
2. Create a compact, representative set covering ordinary, ambiguous, boundary, adversarial, and missing-input cases relevant to the task.
3. Define a scoring rubric with observable anchors; separate factual correctness, instruction following, format, usefulness, and safety.
4. Recommend a controlled comparison: same model/version, inputs, settings, and tools where possible; repeat stochastic tests and retain outputs.
5. Treat model-based judging as fallible. Prefer objective checks where feasible and human-review high-impact or subjective outcomes.
6. Report observed results separately from hypotheses. Record model/date/configuration and rerun tests after material prompt or model changes.

Return test cases, expected behavior, rubric, and limitations. Never describe a small test set as proof of universal reliability.
