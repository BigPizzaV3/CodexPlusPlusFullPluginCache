---
name: august-weekly-digest
description: >
  Build a Slack-ready weekly digest of all August research — interviews and
  focus groups — run against a given org (or across all orgs) in the past 7
  days. Surfaces top themes with supporting quotes, standout twin verbatims,
  and unresolved questions to follow up on, so the team stays caught up on
  customer signal without skimming raw transcripts. This workflow can be
  scheduled to run every Monday morning. Triggers on: "weekly august digest", "august
  weekly recap", "summarize this week's research", "what did we learn from
  twins this week", "/august-weekly-digest".
---

# August Weekly Digest

Roll up every August interview transcript and focus-group result from the
past 7 days into a Slack-ready markdown digest, one section per org. All
tools live under the August MCP.

The output is **copy-paste-ready markdown**, not an auto-post. The user
pastes it into #research, #product, or their own channel.

---

## When to use

- User asks for a weekly recap of research / twin conversations.
- User is prepping for a Monday standup and wants the customer signal from
  the prior week.
- A scheduled run fires every Monday morning.

## When NOT to use

- User wants deep synthesis of a *single* interview → use `/august-interview`.
- User wants live feedback on a new artifact → use `/august-feedback`.
- User wants a single focus-group readout → use `/august-focus-group-report`.
- Time window is not "past 7 days" — for arbitrary windows, ask the user
  and pass the date range through instead of hardcoding.

---

## STEP 1 — Resolve the org(s)

The digest is org-scoped. Figure out which org(s) to summarize.

- If the user names a specific org ("weekly digest for GNC") → resolve via
  `list_organizations` and use that one.
- If the user says "all my orgs" / "across everything" → call
  `list_organizations` and iterate over every org they have access to.
- If ambiguous, default to **all orgs** rather than blocking — the digest is
  cheap to skim and easy to trim. Note at the top which orgs were included.

---

## STEP 2 — Pull the past 7 days of activity per org

For each org, in parallel where possible:

1. `list_conversations` with `org_id` and filter to conversations whose
   `created_at` (or equivalent timestamp) falls within the last 7 days.
2. `list_focus_groups` with `org_id` and filter to focus groups completed in
   the last 7 days.

If both lists are empty for an org, produce the **empty-week fallback**
(see STEP 5) — do NOT skip the org silently.

---

## STEP 3 — Fetch content for each item

For each conversation ID from step 2: call `get_interview_transcript`.
For each focus group ID from step 2: call `get_focus_group_results`.

Batch these calls in parallel where the tool signatures allow. If any
individual fetch fails, note the item as "unavailable" in the digest
rather than failing the whole run.

Keep track of:
- twin name / persona (for quote attribution)
- artifact or topic evaluated
- the raw response body

---

## STEP 4 — Synthesize the per-org digest

For each org, cluster across all items pulled and produce:

- **3–5 top themes** — recurring reactions, objections, or observations that
  showed up in more than one conversation. For each theme:
  - one-sentence description of the theme
  - one supporting verbatim quote (≤25 words), attributed to twin + org
- **3–5 standout quotes** — the punchiest single lines from the week that
  don't necessarily belong to a theme but are worth circulating. Attribute
  each.
- **Unresolved questions** — 2–4 things the research raised but didn't
  answer, worth following up on next week.

**Hard budget: ≤400 words per org.** If it runs long, cut themes down to 3
and standout quotes down to 3. Slack readers scan; density beats completeness.

---

## STEP 5 — Format output

Return one markdown block per org, in this shape:

```
*August weekly digest — {Org name} — {date range}*
_{N interviews, M focus groups} from the past 7 days_

*Top themes*
1. *{Theme name}* — {one-line description}
   > "{quote}" — {twin name}
2. …

*Standout quotes*
- > "{quote}" — {twin name}, on {topic}
- …

*Unresolved questions*
- {question 1}
- {question 2}

_Source: {N} interviews, {M} focus groups. Full transcripts in August._
```

If a run turned up nothing for an org, use the **empty-week fallback**:

```
*August weekly digest — {Org name} — {date range}*
No new interviews or focus groups this week. Consider spinning up a round
on {suggested topic based on prior weeks or open questions}.
```

At the top of the whole response, add a one-line summary: "Digest across N
orgs — copy-paste each block into Slack."

---

## Output rules

- **Do NOT auto-post to Slack.** This skill produces markdown; the user
  posts it.
- **Do NOT include the raw transcript.** Only synthesized themes + quotes.
- **Every quote must be attributable** to a real twin from the actual
  transcripts — never invent verbatims.
- **Keep it human.** Punchy quotes > paraphrases. If a twin said something
  striking, use their words, not yours.
- If the user later asks "expand theme 2" or "what did Sarah say in full,"
  re-fetch that specific transcript rather than reconstructing from memory.
