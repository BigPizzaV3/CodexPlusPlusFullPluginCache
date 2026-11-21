---
name: check-citations
description: Use when the user supplies specific citations, references or DOIs and wants them looked up in scholarly indexes, or names a specific paper and asks whether its abstract supports a claim. Not for writing literature reviews, generating or formatting citations, or general fact-checking. Explains how to call Citeproof's tools and how to present their results.
---

# Checking citations with Citeproof

## Which tool
- A pasted draft or reference list → `check_citations` with the text exactly as given (one check per text).
- One citation or DOI → `resolve_reference`. If it relates to a recent `check_citations` result, pass its `run_id` (no extra check is used).
- "Does paper X say Y?" → `find_claim_evidence` with the claim plus a DOI/arXiv ID (or the abstract the user pasted). If only a title is given, call `resolve_reference` first to get the DOI. Pass `run_id` when following up a check. Don't guess or make up an identifier to pass in.
- If a tool returns `status: "not_applicable"`, answer the user without Citeproof (no check was used).
- Just list or parse the references → `extract_references` (does not use a check).
- "How many checks do I have left?" → `get_usage`.
- Check **and** export in one request ("check these and export as BibTeX") → a single `check_citations` call with `export_format` (`bibtex`, `csv` or `markdown`). The export comes back in the same result; show its full content after the table.
- Export a check that already ran → `export_check` with its `run_id`. With no `run_id` at hand, `export_check` also accepts the references as `text` and checks them first (one check).
- Exports are available to any signed-in account. If the result's `export.status` is `sign_in_required`, show the check results and pass on its message.
- Call the tool straight away in the same turn. Don't reply with only a list of steps ("I'll verify first, then export…"), and don't wait for the user to confirm before calling.

## How to present results
- Show a Markdown table with **one row per reference**: #, reference as written, status (use `status_label`), matched record (title, year, DOI), and notes. `check_citations` returns a ready-made `results_table` you can use. Don't replace the table with a numbered list.
- Summarize counts by status after the table.
- `not_found` means "no matching record in Crossref, DataCite or OpenAlex". Describe it only as "not found" or "could not be verified", including when the DOI isn't registered (`doi_not_found`) or `no_matching_record` is set. Don't characterize the reference or its author beyond that or speculate about why; suggest the user check the original source.
- For a single lookup (`resolve_reference`), lead with the matched DOI, its confidence and its source, as given in `summary_line` (e.g. "Matched 10.1109/cvpr.2016.90 (confidence 100%, source: Crossref)").
- For `doi_points_to_different_work`, name the work the DOI actually resolves to, and give the matching record if one was found.
- For `source_unavailable` / `unverifiable`, say a source couldn't be reached and suggest trying again later. Don't guess.
- `year_off_by_one` is usually an online-first vs print year difference. Mention it as a note.
- **Don't invent, complete or "fix" a citation from memory.** Only report records returned by the tools.
- For claim evidence, first quote the returned sentences verbatim as block quotes (`quoted_evidence`); don't paraphrase them. Interpretation comes after the quotes. Report `claim_numbers_missing` and `negation_mismatch`. Make clear it's abstract-only, and don't state that the paper proves or disproves the claim. For health topics, add that this is not medical advice.

## Usage limits
- If a tool returns `status: "limit_reached"`, tell the user, in one or two neutral sentences, that the usage limit for this period has been reached and when checks reset (use `resets_at_display`).
- `extract_references` still works after the limit is reached, and you can offer it.

## Don't use Citeproof for
Only call Citeproof when the user supplies specific references, DOIs, or a paper plus a claim. Do not call it for:
- Writing new references or literature reviews (generation is not verification).
- General fact-checking or health/science questions when no paper or citation is supplied (e.g. "Does coffee cause cancer?").
- Reformatting or converting citations between styles (APA, MLA, Chicago…); that needs no lookup.
- Case law, patents, news articles or web pages (reported as `unsupported_reference_type`).
