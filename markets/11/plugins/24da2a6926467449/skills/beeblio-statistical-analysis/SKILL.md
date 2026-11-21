---
name: beeblio-statistical-analysis
description: Run and interpret statistical analyses on Beeblio project data using MCP analysis jobs. Use for hypothesis tests, regression, effect sizes, confidence intervals, or statistical reporting.
---

# Statistical analysis of Beeblio data

Use the `beeblio-data-analysis` workflow to inspect the saved source, execute code with `submit_analysis_job`, and verify the generated results in Beeblio. Choose a method that matches the research question, outcome scale, sampling design, and available covariates. State the estimand or comparison before fitting a model.

Inspect variable types, units, missingness, duplicates, ranges, and sample counts. Keep raw data unchanged. Record exclusions and transformations in the script; write derived data to a new `/workspace/2-Data/derived/` path. Set and record a random seed for stochastic methods. Check model assumptions and use an appropriate alternative or qualify the result when they fail. Validate important counts and one key statistic independently.

Report the model or test name, unit of analysis, analyzed sample size, missing-data treatment, estimate, uncertainty (preferably a 95% confidence interval), effect size, and any p-value with its threshold. Explain magnitude in the units of the data. A nonsignificant result is insufficient evidence for an effect, not proof of no effect. Do not equate a small p-value with practical importance. Discuss multiplicity and design limitations when relevant; use causal language only when the design supports it.

Save the executed script under `3-Analysis/` with `write_text_file`, using a new path. Save compact machine-readable results and a plain-language Markdown report from the analysis job, then verify each with `stat_file` or `read_text_file`. Use `upload_artifact` only for results created outside Beeblio. Include exact input and output project paths in the final answer.
