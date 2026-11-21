# Current prompting guidance

For a 6.2 target, use the [6.2 guide](https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra.md#prompting-best-practices), checked November 19, 2026. Ask for the result and evidence that establish completion; specify the desired voice only where it changes the outcome. For ambiguity, keep independent work moving without crossing an unresolved boundary. For visual work use a relevant reference and inspect the render. For architecture or style changes, inspect existing code first and limit the diff. Try one instruction change against actual failures before adding more. The October guidance below is retained for older [GPT-6 targets](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices); do not infer that any recipe was tested on the user's workload.

## Match the task before adding instructions

Keep the requested result clear, with enough context to preserve facts, constraints and the desired format. A short edit rarely needs an agent charter. Add examples only when they clarify a format or difficult distinction. Separate supplied evidence from instructions and ask for checkable conclusions, sources or calculations where useful; do not request hidden internal reasoning.

For ChatGPT, follow the current [prompting guide](https://learn.chatgpt.com/docs/prompting): describe the result in normal language, supply relevant sources and refine with follow-ups. Tool and plugin availability belongs to the active surface.

## Astra and the GPT-6 family

- Define completion so an action request finishes the authorized work. For a plan or review, completion is that plan or review. Do not turn every request into implementation.
- Carry forward existing authorization. Resolve routine details from context, then ask only for missing decisions that materially affect the result. Prepare an actionable review artifact before a remaining approval step.
- Preserve real boundaries, including protected systems and external actions. When a loaded workflow unexpectedly stops work, identify the relevant visible file and rule, explain its application and continue unaffected authorized work. Do not treat this as a requirement to pause.
- Specify the audience and useful level of detail. Use plain language and the format the user needs instead of generic formatting instructions for every response.
- Where the harness supports delegation, use separate scopes for independent work and reconcile the results. Do not invent agents or assume dispatch permission.
- Verify the changed behavior with proportionate checks. Repeat tests for a concrete failure, further change or unresolved concern, not because a template demands repeated broad testing.

These points summarize [GPT-6 prompting best practices](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra.md#prompting-best-practices). Evaluate a material prompt change on the actual model and workload. A static checklist does not show better answers or lower cost.

## Keep reusable guidance focused

A skill description should identify a specific task trigger. Put optional procedures and long references behind links. Retain meaningful domain exceptions and evidence requirements while removing obsolete repetition or contradictory instructions. Read project documents when they apply to the task rather than preloading everything for every change.

Source: [OpenAI's skills and prompts guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra).

## Handle older guides

Use the current model guide for model settings and behavior; use the general [API prompt-engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering) for roles, input structure and prompt versioning. Older o-series formatting tricks, GPT-4-era role recipes and broad testing demands are not automatic GPT-6 requirements. Preserve useful older examples as dated context, and check them against current source guidance before reuse.
