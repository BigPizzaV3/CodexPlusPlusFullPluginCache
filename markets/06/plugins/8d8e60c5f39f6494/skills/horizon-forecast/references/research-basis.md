# Research basis and design decisions

Researched 2026-09-15. These sources inform the design; they do not validate Horizon Forge's accuracy. Entries distinguish empirical work, professional methodology, product documentation, and our own conventions. Links are to primary publishers or authors. Research abstracts and overview pages were used where noted; no claim is made to reproduce proprietary systems or every experiment.

## Forecasting and foresight

1. **Tetlock, Mellers, Rohrbaugh and Chen, Forecasting Tournaments (2014).** [APS article overview](https://www.psychologicalscience.org/journals/current-directions/0963721414534257/). Describes tournament practices including training, collaboration and aggregation. Design use: explicit probabilities, comparison classes, and accountable revisions. Limitation: human tournament findings do not establish that extra AI personas improve long-horizon industry forecasts.

2. **Halawi, Zhang, Yueh-Han and Steinhardt, Approaching Human-Level Forecasting with Language Models (2024).** [Paper](https://arxiv.org/abs/2402.18563), [full-text methods](https://arxiv.org/html/2402.18563v1). Evaluates a retrieval-based forecasting pipeline with aggregation on forecasting questions. Design use: gather external evidence, structure forecast questions, and compare estimates. Limitation: the paper's task, models, retrieval and evaluation differ from this plugin; its results cannot be inherited by copying prompts.

3. **Karger and colleagues, ForecastBench (2024; revised 2025).** [Research paper](https://arxiv.org/abs/2409.19839), [project documentation](https://www.forecastbench.org/docs/). Uses genuinely future questions to reduce outcome leakage. Design use: freeze prospective predictions, record resolution rules and compare consistent vintages. Limitation: historical replay can still be contaminated by model training. The article's historical performance results are not current model rankings.

4. **OECD, Strategic Foresight Toolkit for Resilient Public Policy (2025).** [Publisher overview and toolkit](https://www.oecd.org/en/publications/foresight-toolkit-for-resilient-public-policy_bcdd9304-en.html). Combines assumption challenges, alternative futures and strategy stress tests. Design use: explore coherent scenarios and cross-domain effects. Limitation: exploratory scenarios are possible futures, not automatically probability distributions.

5. **ODNI, Intelligence Community Directive 203, Analytic Standards.** [Primary directive](https://www.dni.gov/files/documents/ICD/ICD-203.pdf). Sets expectations for objectivity, uncertainty, alternatives and analytic quality. Design use: claim/source distinctions, confidence explanations, competing hypotheses and decision-relevant audit. This plugin is not an intelligence product and does not claim certification or compliance with the directive.

## Economic mechanisms and measurement

6. **US Bureau of Economic Analysis, gross output versus value added.** [Official explanation](https://www.bea.gov/help/faq/1197). Explains the relation between output, intermediate inputs and value added. Design use: choose one measure, avoid double counting and do not confuse sector sales with net addition to GDP. Global comparison also requires compatible country definitions.

7. **Brynjolfsson, Rock and Syverson, The Productivity J-Curve (2018 working paper; 2021 publication).** [NBER abstract and publication record](https://www.nber.org/papers/w25148). Describes complementary intangible investment and timing of measured productivity gains. Design use: examine organizational change and complementary investment before assuming immediate commercial benefits. The research does not supply a universal adoption-delay parameter for new fields.

8. **Farmer and Lafond, How predictable is technological progress? (2016).** [Authors' research paper](https://arxiv.org/abs/1502.05274). Studies historical technology-cost behavior and forecast error distributions. Design use: examine empirical cost trends and uncertainty. Limitation: a cost forecast does not establish adoption, revenue growth, or investment returns; the bundled tool does not implement or validate that paper's model.

## Prompting and multi-agent design

9. **OpenAI, Reasoning best practices.** [Official guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices). Supports clear objectives, structured inputs and explicit success criteria; reasoning models do not need instructions to reveal chain-of-thought. Design use: ask for checkable research artifacts and concise explanations rather than internal reasoning transcripts. Product guidance can change and should be rechecked when adapting the plugin.

10. **OpenAI, Subagents.** [Official documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents). Describes bounded delegated work, inherited settings and orchestration. Design use: real specialist assignments within host limits, concise handoffs and director-owned synthesis. Agent availability and settings come from the host; this package does not create a model backend.

11. **Huang and colleagues, Large Language Models Cannot Self-Correct Reasoning Yet (2023).** [Research abstract](https://arxiv.org/abs/2310.01798). Examines limitations of intrinsic self-correction without external feedback in the tested setting. Design use: require new evidence or explicit checks for review-driven changes. Limitation: this is not proof that every later model or every critique workflow fails.

12. **OpenAI, Plugin architecture.** [Official documentation](https://developers.openai.com/plugins/concepts/plugins). Describes packaging workflow skills with optional tools. Design use: a portable skills package using tools already exposed by the host, with a local arithmetic helper; no unnecessary external server or credentials.

## Original conventions in this plugin

The role roster, research-wave schedule, 5-/10-year defaults, candidate targets, report-length target, growth threshold, 0–5 anchors, rating weights/bands, confidence eligibility rule, perturbation factors and stopping convention are original design choices. They are inspectable and adjustable; they are not research-derived constants or validated predictors. Sources support broad principles, not every specific design choice.

## Practical techniques and their limits

| Technique | How it is used | Failure prevented or limit |
|---|---|---|
| Plan then execute | Named questions, owners, dependencies and evidence gates | Prevents omission; does not guarantee the plan is correct |
| Independent initial estimates | Neutral packets before preferred forecasts are shared | Reduces anchoring; shared models/sources still correlate |
| Source lineage | Track the original dataset behind repeated coverage | Avoids counting repetition as corroboration |
| Falsification search | Find the evidence that would reverse a thesis | Limits confirmation bias when the search is substantive |
| Reference classes | Compare adoption mechanisms and failures | Analogue selection itself can be biased |
| External verification | Reopen sources and reproduce arithmetic | More reliable than an unsupported request to rethink |
| Sensitivity analysis | Perturb weights and pivotal economic inputs | Reveals fragile conclusions; does not quantify all uncertainty |
| Prospective scoring | Freeze and later resolve predictions | Creates measurable feedback; requires time and enough outcomes |
| Progressive reference loading | Load detailed methods at the stage that needs them | Preserves useful context and avoids redundant prompt bulk |

No incantation, inflated expertise claim, forced delay, unlimited debate, or hidden reasoning request is included. Improvements in process quality can be tested immediately. Improvements in forecasting accuracy require prospective evidence over time.
