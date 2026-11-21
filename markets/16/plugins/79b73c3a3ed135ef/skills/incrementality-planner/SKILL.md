---
name: incrementality-planner
description: Explain incrementality and choose how to measure whether an ad channel, campaign type or budget change drives incremental results, then plan the test. Use when someone asks what incrementality, iROAS, lift or a holdout means, if a channel is incremental, whether to pause or scale ads (brand search, PMax, Meta, TikTok, YouTube), how to run a holdout, lift study, geo test or incrementality test, or how much of their attributed conversions are real.
---

# Incrementality planner

Turns a question about ad effectiveness into a measurement plan: which method, which data, how long, what it costs, and what decision it will support.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## When the user asks what incrementality is

Answer in plain terms first, then offer to plan a test:

- Incrementality is the share of results that would not have happened without the ads. Attribution assigns credit for conversions that happened; incrementality asks which of them the ads caused.
- It is measured by comparing a group exposed to the ads with a comparable group that was not: users held out by the platform, regions switched off, or periods with ads off.
- iROAS is incremental revenue divided by the spend that caused it. iCPA is spend divided by incremental conversions.
- Give one example from `references/literature.md` if useful (eBay brand search: 99.5% of lost clicks came back through organic results).

## Workflow

1. **Understand the decision.** Ask only what is missing, in one message, using the decision questions in `references/method-ladder.md`. If the user already gave the answers, do not ask again.
2. **Pick the method** with the ladder in `references/method-ladder.md`:
   - If the platform offers a native lift study and the account is likely eligible, recommend it first and explain how to request it. Details in `references/platform-lift.md`.
   - If the question spans channels, or the channel is search, or the platform has no lift tool, recommend a geo experiment.
   - If geos are not possible, recommend a switchback; if nothing can be changed, a directional pre/post.
   - Always state the rung: causal, quasi-experimental or directional.
3. **Size it.**
   - With a geo panel: hand over to the `geo-test-design` skill, which runs the design script.
   - Without data: run `python scripts/geolift.py quick` with the user's daily KPI and a noise assumption, and show the MDE by test length. Say it is a rough sizing.
4. **Deliver the plan** using `assets/test-plan-template.md`, filled with what is known and marked placeholders for what is not.

## Output

- One-line recommendation: method, scope, duration, and why.
- What it will and will not answer.
- Data needed, with the source for each item (`references/data-format.md`).
- Cost in KPI or spend, with the assumption it rests on.
- The plan, or the next step to get the plan (usually: export the geo panel).

## Rules

- Do not invent volumes, costs, eligibility thresholds or dates. When a platform rule matters and may have changed, say so and point to where the user can confirm it in their account.
- Attribution reports, spend-KPI correlation and "we paused it and nothing happened" are not incrementality. Say so politely when offered as evidence, and propose the test that would settle it.
- Recommend the KPI from the business backend over platform-reported conversions.
- If the decision needs a precision the test cannot reach (the MDE is larger than the effect that matters), say so before the user spends money on it.
- Keep it short. A plan is a page, not an essay.

## Evidence

When the user doubts that testing is needed, or asks what to expect, cite findings from `references/literature.md`. Examples: the eBay brand search experiment, or the Facebook comparison of observational methods with experiments. Quote only figures that appear there.

## Scripts

`scripts/geolift.py` is bundled with this skill. See `references/script-reference.md`. If code execution is not available, give the user the exact command to run locally (`python geolift.py ...`; it needs numpy, pandas and scipy).
