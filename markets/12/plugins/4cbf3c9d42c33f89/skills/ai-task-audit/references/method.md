# How to interpret the WCS rubric

Method version 1.0.0. Product documentation checked 18 October 2026.

## Origin

The public [Teach Them to Drive framework](https://wecallshotgun.com/teachthem) puts human judgment, source context and evaluation at the center of AI adoption: Frame, Prompt, Evaluate, Iterate. The [WCS adoption framework](https://wecallshotgun.com/blog/enterprise-ai-adoption-4-phase-framework) starts from real workflows, then training, embedding and measured expansion.

The task audit turns those principles into a newly designed rubric. Its weights, thresholds, minimum sample and evidence freshness are design choices for this plugin. They are not empirical success probabilities, a certification or a formula claimed to appear in the book.

## Four separate dimensions

Each factor has five anchors, rated 0 to 4. Read the live methodology tool for exact anchors. The score is 100 times the weighted sum of rating divided by 4. Unknown factors make the dimension unknown.

| Dimension | Factors and weights | Direction |
| --- | --- | --- |
| Relevance | Repetition 35%, AI contribution 35%, workflow friction 30% | Higher means stronger potential fit |
| Complexity | Process variation 35%, integration effort 35%, exception burden 30% | Higher means more implementation effort |
| Capability | Input readiness 35%, output verification 35%, approved tool access 30% | Higher means more of the requirements are in place |
| Risk | Error consequences 30%, data sensitivity 25%, hallucination exposure 25%, action impact 20% | Higher means greater exposure |

There is no blended score that can hide a serious risk. Data disapproval, high-impact decisions, maximum error/sensitivity/action factors and risk scores of 75 or above take priority. Scores do not authorize actions. Reassess bounded preparation separately from the final consequential decision.

## Accuracy above 95%

Every AI task starts unverified. The user must supply actual complete-task evaluation counts, a success criterion, date and confirmations about the sample and configuration. A task passes this rubric's evidence gate only when:

- At least 100 representative cases were independently checked on the same configuration within 90 days, with no critical failure.
- The two-sided 95% Wilson confidence interval's lower bound is strictly above 95%.

The [NIST reference](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm) supports the statistical method. The 100-case and 90-day rules are plugin design choices. The calculation assumes the sample supports a binomial interpretation; repeated near-duplicates and biased examples do not establish real-world reliability. The plugin cannot independently verify supplied counts or representativeness.

For illustration, 95 passes in 100 is not evidence of accuracy above 95%. Neither are 20 perfect examples. A qualifying supplied test still does not guarantee a future result. Separate critical errors, omissions and unsupported assertions from an average pass rate. Recheck after changing the model, prompt, skill, source set, tool or task distribution.

Creative outputs may need a human rubric rather than factual accuracy. Say when the 95% factual accuracy question is not meaningful; keep the plugin's unverified AI flag and assess task acceptance instead. A pure rules-only route receives no LLM accuracy claim.

## Time and implementation

Weekly net minutes saved = runs per week times (manual baseline minus AI handling minus review minus rework), minus weekly maintenance. Use high overhead for the low saving estimate and low overhead for the high estimate. Keep setup effort and payback separate. Negative savings mean a task may take longer with AI.

Follow [WCS automation guidance](https://wecallshotgun.com/blog/start-ai-automation): identify repeated work, triggers, outputs, review and exception handling. Follow the [agentic workflow guidance](https://wecallshotgun.com/blog/building-production-ready-agentic-workflows) for bounded scope, monitored steps, human escalation, cost limits and recovery. Repeated effective methods can become [reusable skills](https://wecallshotgun.com/blog/stopped-prompting-built-50-claude-skills).

Time estimates require evidence labels. A hypothesis is an input to a pilot. It is not a result from a customer. Never claim adoption, reduced headcount, saved cash, production readiness or a running automation from an audit alone.
