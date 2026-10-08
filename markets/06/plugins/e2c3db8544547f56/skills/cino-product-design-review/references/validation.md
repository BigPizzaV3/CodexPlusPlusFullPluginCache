# Skill validation protocol

Use this only to evaluate or revise Cino Product Design Review itself.

## Blind first pass

1. Choose a real target with known routes, states, and required widths.
2. Keep previous audits, expected findings, and answer keys out of context.
3. Run a read-only audit using the skill and preserve the raw output.
4. Only after completion, compare it with the established findings and source evidence.

This order prevents the skill from merely restating a supplied answer key.

## Score the result

Evaluate:

- recall of known P0 and P1 issues;
- unsupported P0 count, which should be zero;
- evidence completeness for every P0 and P1;
- correct separation of systemic and page-specific causes;
- repair instructions that another implementer can act on;
- preservation of settled product and business rules;
- explicit treatment of missing access and untested states; and
- whether the skill stayed read-only.

Do not reward a large number of findings. Reward correct prioritization, reproducibility, and useful repair direction.

## Correct and retest

Trace failures to the smallest instruction or reference gap. Revise the skill, then rerun on a fresh or reset target. Avoid adding target-specific facts to the general skill.

After the first product passes, test an unrelated product type and brand—such as a marketing site after a dense application—to detect domain overfitting. A skill is not proven by one familiar interface.

## Acceptance criteria

- Known serious visual and responsive failures are found.
- No P0 is unsupported.
- Every serious finding is tied to an exact route, state, width, component, evidence, repair, and verification method.
- System problems are distinguished from page problems.
- Recommendations preserve established product constraints unless evidence justifies challenging them.
- Missing evidence is disclosed.
- No product or code changes occur without separate authorization.
- The audit adapts to the target's brand, stakes, and user journey.
