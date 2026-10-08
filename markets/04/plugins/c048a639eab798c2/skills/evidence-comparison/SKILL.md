---
name: evidence-comparison
description: Compare two or more nutrition claims, diets, supplements, or interventions using AllNutrition's cited evidence. Use for "X vs Y" questions, "which is better for…", or whenever the user wants competing claims evaluated side by side rather than a single answer.
---

# Evidence comparison

Put competing nutrition claims side by side with the evidence behind each one,
so the user sees not just which option looks better but how sure the science
actually is.

## Input

Two or more named options and the outcome they should be compared on — e.g.
"creatine vs beta-alanine for strength", "Mediterranean vs low-carb for
longevity". If the outcome is missing, ask for it before calling any tool: a
comparison without an outcome is not answerable.

## Procedure

1. Call `ask_nutrition` once per option, phrasing each question identically
   except for the option ("Does X improve <outcome>?"). Identical phrasing
   keeps the answers comparable. Use `deep_research: true` only when the user
   explicitly asks for a deep or comprehensive review — it takes minutes per
   call, so mention the wait before starting.
2. Read each answer's `evidence_strength` (strong | moderate | limited |
   insufficient) and `consensus_level` (high | moderate | mixed | low). These
   labels are the comparison's backbone — never omit or soften them.
3. Compare only what the returned evidence supports. If the evidence for the
   two options was studied in different populations or doses, say so instead
   of forcing a winner.

## Output

1. A one-or-two-sentence verdict up front, hedged to match the weaker side's
   evidence labels.
2. A table with one row per option: what the evidence shows, `evidence
   strength`, `consensus`.
3. A single combined reference list for all options, deduplicated by URL, in
   the compact numbered format (`n. Title URL`) — cite only sources the tools
   returned.
4. A closing note naming the biggest gap or caveat (e.g. "no head-to-head
   trials; both compared to placebo separately").

## Boundaries

- Never declare a winner when both sides are `limited`/`insufficient` or
  consensus is `mixed`/`low` — say the evidence cannot separate them.
- Describe what the research shows for populations, not what this user should
  personally do; nutrition evidence is not a personal prescription.
- If the user adds their own claimed study ("I read that X cures Y"), check it
  against `search_references` results rather than accepting or contradicting
  it from memory.
