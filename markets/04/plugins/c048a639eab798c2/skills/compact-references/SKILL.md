---
name: compact-references
description: Produce a compact, numbered reference list from AllNutrition results. Use when the user asks for "the references", "the sources", "a bibliography", or a copy-pasteable/shareable citation list — either for an answer AllNutrition already gave in this conversation or for a fresh topic.
---

# Compact reference list

Turn AllNutrition source lists into a short, numbered, plain-text bibliography
that fits in a tight character budget without losing any links.

## Input

One of:

- A prior `ask_nutrition` or `search_references` result in this conversation
  whose `sources` the user now wants listed.
- A fresh topic ("give me references on magnesium and sleep") with no prior
  result — call `search_references` with the topic first (default
  `max_results`, add `published_after` only if the user asked for recent work).

## Procedure

1. Collect the sources. Use only the `sources` array returned by AllNutrition
   tools. Never add sources from memory or the open internet, and never invent,
   guess, or "fix" a URL — reproduce each URL exactly as returned.
2. Deduplicate by URL, keeping the first occurrence. If the list annotates an
   existing answer's citations, keep the numbering the answer used so the
   numbers still match; otherwise number from 1 in the returned order.
3. Render one line per source in exactly this shape:

   ```
   References:
   1. Title https://example.org/...
   2. Title https://example.org/...
   ```

4. Fit the whole block into the character budget: 4,900 characters total
   unless the user gives a different limit. Shorten only the titles, never the
   URLs. Truncate every title at the same maximum length and append `...` to
   any title you cut; pick the largest uniform title length that keeps the
   whole block under budget. With a typical list of 10 sources, full titles
   usually fit — only shorten when they don't.

## Output

Only the `References:` block, ready to copy. No commentary, no verbatim
excerpts or quotes from the sources, no markdown link syntax (bare URLs are
the point — they survive copy-paste into plain-text contexts).

## Boundaries

- If there are no sources to list (the tool returned none, or the prior answer
  had none), say so — do not fill the gap with sources of your own.
- If the user asks for full abstracts or verbatim passages, explain that
  AllNutrition returns AI-written summaries, not verbatim source text, and
  offer the source links instead.
