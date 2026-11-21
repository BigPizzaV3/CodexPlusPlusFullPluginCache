# First-contact narrative — launch scope and later expansion

The cold @-mention should tell a newcomer why SigRank exists before asking them to choose a tool. The launch greeting lives in `skills/get-started/SKILL.md`; the plugin manifest points to it with `extensions.com.openai.onboardingSkill`. The host must still be tested with a fresh bare mention because manifest support alone does not prove the exact response ChatGPT will generate.

## What the opening should convey

SigRank | SignalAF is the **AI Operator Leaderboard**: performative stats and benchmarks for AI users, not models. Tokenpull measures → SigRank evaluates → SignalAF publishes. It makes observable token-flow structure legible so people can follow a field, compare approaches, and learn what a number means. Competition gives the board energy; education and connection give it lasting purpose. The analogy to sports or game stats is about shared baselines and discussion, not a claim that a score measures human talent, intelligence, productivity, or work quality.

The greeting is intentionally brief. It offers five routes: the live Active board; the metrics (including operating ratio and I/O/W/R); how measurements become rankings and where public data comes from; a public operator profile; and the homepage Four Degrees reference ladder. On a specific request, skip the greeting and answer the request. No live placement or field statistic belongs in a cold opening unless a live source is read.

## Deeper experiences to expand later

- A guided "read the board" journey could show the Active field first, then let a user inspect the token-flow drivers behind any row without presuming that rank alone tells the whole story.
- A "Four Degrees" explainer could distinguish the modeled AA baseline, Operator Center of Mass median, top-100 median, and top evaluation; label each cohort and date; and avoid treating those homepage references as the claimed-only Active board distribution.
- A methodology journey could trace I/O/W/R through operating ratio, Leverage, Velocity, Yield, Construction, and the current Build Archetype rules, with examples chosen from current data rather than a favored operator.
- Profile discovery could surface unusual patterns using neutral, repeatable comparisons. The system should not hard-code an account, assume a person/agent classification, or claim that a metric establishes ability.

These are product directions, not launch features or promises of measured improvement. Publication can proceed with the short greeting after fresh host testing; the deeper narrative can grow without changing the public MCP boundary.
