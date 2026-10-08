# Skill evaluation protocol

## Test set

Create at least:

- 5 clear should-trigger requests;
- 5 natural-language should-trigger variants, including typos or incomplete phrasing;
- 5 near-neighbor requests that should not trigger;
- 3 missing-input or missing-tool cases;
- 3 adversarial, permission, or safety cases;
- 3 output-contract checks.

Use realistic details without leaking the intended answer. Retain several held-out cases for regression testing.

## Measures

| Dimension | Evidence |
|---|---|
| Trigger recall | Relevant requests that selected the skill |
| Trigger precision | Selected requests that truly needed the skill |
| Task success | Acceptance criteria met |
| Uplift | Difference versus a no-skill baseline |
| Efficiency | Added context, tool calls, time, and unnecessary output |
| Reliability | Repeat consistency and safe failure |
| Portability | Works without hidden chat context |

Do not collapse all dimensions into one number unless weights are declared. Record runtime and date because behavior can change.

