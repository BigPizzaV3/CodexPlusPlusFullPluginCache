---
name: think
description: Answer deeper questions that span many pages of the user's Albo brain with think or synthesize, which return a cited answer across pages and point out conflicts and gaps. Use for "why", "how has X changed", "what's the pattern", "compare", "what are we missing" and strategy questions about the user's own projects, people and decisions. Not for simple lookups, which search, get_page and recall answer faster.
metadata:
  triggers:
    - '"why did we …", "how has … changed over time", "what''s the pattern in …"'
    - '"compare … with …", "what are we missing", "what do we really know about …"'
    - strategy or review questions that need evidence from several pages
---

# Think across the Albo brain

Most questions are lookups: use `search`, `query`, `get_page` or `recall`
(the `brain` skill). Reach for `think` or `synthesize` only when the answer
needs evidence pulled together from many pages.

Brain tools appear only for people in an Albo team. If neither `think` nor
`synthesize` is connected, answer with search and reading as in the `brain`
skill.

## Which tool

- **`synthesize`** gives a cited answer to a broad question across pages. Pass
  `question`, and `since` / `until` to limit the period.
- **`think`** goes further: multi-hop reasoning across pages, takes and the link
  graph, with conflict and gap analysis. Pass `question`, optional `anchor` (a
  slug to centre on), `rounds` for more hops, `since` / `until`, and
  `reference_date` for "as of" questions. `think` isn't on the default tool list;
  it's still callable. If your app needs its schema first, call `request_tools`
  with `{"tools": ["think"]}`.

Both are slow and make paid AI calls, so use them once per question rather than
in a loop. Don't use them for questions a single page answers.

## Steps

1. Do a quick `search` or `query` first. If one or two pages answer it, read
   them and stop.
2. Otherwise call `synthesize`, or `think` for multi-step "why" and "what's
   missing" questions. Phrase the `question` fully, with names and the period.
3. Check the key claims. Open the cited pages with `get_page` for anything you
   state as a date, status or decision.
4. Answer with the slugs you relied on. Keep the conflicts and gaps it found in
   the answer: say which pages disagree and what the brain doesn't cover.
5. If the answer is a lasting conclusion the user agrees with, save it with the
   `remember` skill.

## Notes

- If the brain has no AI key set up, `think` returns the gathered evidence with
  a `synthesis_keyless` notice and no written answer. Write the answer yourself
  from that evidence and cite it.
- Don't present a synthesis as more certain than its sources. Flag thin or
  one-source evidence.
