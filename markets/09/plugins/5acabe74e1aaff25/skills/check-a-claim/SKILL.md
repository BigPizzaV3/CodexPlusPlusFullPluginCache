---
name: check-a-claim
description: Use when someone asks whether a statement about AI agents is true, where a claim comes from, or wants a source to cite for one. Searches the Greenlit Books claim ledger and returns sourced claims with citations and the limits of each source.
---

# Check a claim about AI agents

The Greenlit Books tools are read-only.

1. Call `check_claim` with the statement in the user's own words. A whole sentence works. Set `basis` to `external` only when the user wants a published result.
2. For each result, quote the claim and give its citation URL. Say what kind of statement it is (a published result, the book's argument, a method, or the author's own account) and follow the one-line quoting rule the result carries.
3. Read `doesNotEstablish` on every external source and tell the user what that source does not show. Do not lean on a source for more than it establishes.
4. If nothing comes back, say the ledger has no claim on that subject. That is an answer, not a failure. Do not cite the site loosely, and do not call the statement true or false just because nothing matched.

To get a finished citation, in prose or BibTeX, for a URL you are about to quote, call `cite_source` with that URL.

If the user's own instructions differ from these guidelines, follow the user's instructions.
