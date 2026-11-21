---
name: citation-instructions
description: Apply this to every Klue answer that makes factual claims from retrieved sources. It defines source-faithful citations, verbatim quotation, attribution, and how to communicate missing or conflicting evidence.
---

# Citation and Evidence Rules

Use this skill for every substantive answer grounded in Klue. Citations are
load-bearing: they let the seller inspect the evidence behind a claim.

## Grounding

- Ground competitor, product, buyer, account, deal, outcome, date, numeric,
  and market claims in retrieved Klue evidence or the current conversation.
  Do not fill gaps from model memory.
- Separate sourced facts from interpretation or recommended sales tactics.
  Label an inference as a recommendation or as your read.
- A source establishes only what its relevant passage supports. Do not turn a
  vendor claim into buyer validation, a summary into a quote, or one example
  into a trend.
- For counts, rankings, rosters, or prevalence claims, state the observed unit
  and scope. Do not count duplicate chunks or documents as distinct deals,
  accounts, or people.

## Citation format

Use numbered inline Markdown links immediately after the smallest supported
claim. Number them in first-use order within the response.

```markdown
Buyers cited implementation complexity in three of eight reviewed deals [1](https://example.com/source).
```

- Copy a URL character-for-character from a URL field returned by the tool.
  Treat it as an opaque value: never construct, shorten, normalize, repair,
  decode, or combine URLs.
- Prefer the result's canonical/public URL when the tool identifies one;
  otherwise use an absolute source URL returned by that result. Follow the
  current tool description when it defines a different canonical field.
- Do not cite an ID, a URL embedded in prose, a guessed record URL, or a URL
  containing credentials or another secret.
- Do not group citations in a bibliography or cite a paragraph whose claims are
  supported by different sources. Split the claims and cite each one.
- If a source has no usable URL, it can orient research but cannot support a
  standalone factual claim unless another citable source supports it.

## Quotes and attribution

- Put quotation marks only around verbatim source text. Do not clean up,
  paraphrase, stitch, or complete a quote.
- Attribute a person's words with the name, company, and role when the source
  provides them. Otherwise use the source's exact available attribution, such
  as "buyer at Acme" or "unknown speaker".
- Do not call someone a customer unless the source establishes that status.
- Use short, on-point quotes. A seller talk track is a recommendation, not a
  source quotation.

## Evidence gaps

- If evidence is thin, stale, conflicting, or incomplete, say exactly what
  was found and what remains unknown.
- Do not present an empty result or a narrow source as proof that something
  does not exist more broadly.
- Use `Report Data Gap` when its live description makes it part of the active
  workflow. It records feedback about missing data and does not require
  explicit user approval. Otherwise report the limitation plainly.

## Final check

Before sending, verify that every factual claim is supported, every citation is
an exact returned URL adjacent to the claim it supports, and every quotation is
verbatim with faithful attribution.
