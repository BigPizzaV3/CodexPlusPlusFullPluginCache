---
name: lift-result-review
description: Review an incrementality or lift result someone else produced, such as a Meta or Google lift study report, a vendor's geo test, an agency deck, or an internal claim that a channel is or is not incremental. Checks design, statistics and interpretation, and says how much weight the result can carry. Use when the user shares a lift result, a test report or a screenshot and asks whether to trust it.
---

# Lift result review

Gives an independent read on a lift or incrementality result: what it shows, what it does not, and whether it can support the decision being made.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Steps

1. Identify what was run: platform lift study, geo experiment, switchback, pre/post, MMM output, or attribution presented as incrementality. Use `references/method-ladder.md` to place it on the ladder.
2. Extract the facts stated in the material: KPI, source, treated and control groups, dates, sample sizes, effect, interval or p-value, spend. Mark what is missing. Never fill gaps with assumptions presented as facts.
3. Check it against the list below.
4. If the user has the underlying data, offer to recompute it with the `geo-test-readout` or `quick-incrementality` skills.
5. Give the verdict.

## Checklist

Design:

- Was there a control group, and was assignment random (users or geos) or chosen?
- Was the plan, including the KPI and the decision rule, set before the data came in?
- Was the test long enough for the channel's carryover, with a cooldown for video and upper funnel?
- Platform lift: which conversions were counted? Pixel-only events miss offline and cross-device outcomes; was CAPI or offline upload used?

Statistics:

- Is there an interval, and does it include zero?
- What effect could the test detect (MDE or power)? A non-significant result from an underpowered test says little.
- Was the result picked from several metrics, segments or windows? If so, discount it.
- Geo tests: how many geos, how good was the pre-period fit, were placebos run?

Interpretation:

- Is "incremental conversions" being compared with attributed conversions to produce an incrementality factor? Is that factor applied to other campaigns or periods where it may not hold?
- Is a go-dark result being used to justify a budget increase (a different question)?
- Are lift results from different platforms being added together?
- Is "lift" relative to the treated group's baseline, or to all conversions? Percentages on different bases are not comparable.

## Verdict format

- One line: how much weight the result can carry (decision-grade, directional, or not usable), and why.
- What the result supports, and what it does not.
- Missing information that would change the verdict.
- The smallest next step that would make it decision-grade.

## References

- `references/platform-lift.md` for what Google and Meta lift studies measure and their thresholds.
- `references/literature.md` for methods and published evidence.
- `references/reading-results.md` for how results should be stated.

## Rules

- Be specific and fair: name the issue and its likely direction (overstates, understates, unknown).
- Do not dismiss platform lift studies as biased by default. A randomized user-level holdout is a strong design; its limits are scope (one platform, its own conversion data), not randomization.
- Do not invent numbers that are not in the material.
