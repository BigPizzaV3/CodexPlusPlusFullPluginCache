# Resumable Endelir business interviews

<!-- ChatGPT Codex — CODEX-V2-004. Working V2 source, not a publication record. -->

Use this only when the three business-draft tools are available. Conversation and
questions stay in ChatGPT. The tools store a private interview in the connected
owner's Endelir workspace; they do not create checkout products or activate AI.

## Resume and collect

1. Identify the connected business with get_profile. If it is the wrong business,
   ask the owner to connect the intended login; no argument may select an account.
2. Call get_business_draft before starting or resuming. Keep its current revision,
   facts, sources, offering keys and approved snapshot. Read get_current_setup to
   distinguish the saved draft from knowledge actually applied to the AI.
3. Ask the next relevant unanswered questions. The returned nextQuestions are
   suggestions, not a requirement that every industry answer the same form.
   Group at most three related questions per message. Do not repeat answered ones.
4. Research available website pages and owner-supplied documents with the host's
   supported tools. Say what could not be read. These draft tools neither crawl
   URLs nor upload/OCR PDFs themselves. When the business-source tools are available,
   follow business-sources.md for actual persisted import and OCR before interviewing.
   A manually entered source reference alone is not proof it was fetched.
5. Record each source with a stable id, kind, title and reference. Include the
   page/section and reading date in the reference. Website URLs must be HTTPS
   and must not contain login credentials. Never store passwords, tokens,
   customer records, bank/card details or verification codes.
6. Record facts as confirmed only after the owner confirms them. Extracted claims
   start unconfirmed. Record conflicts in the fact note and ask the owner which
   value applies. Unknown means unknown; do not manufacture an answer.
7. Keep each course, location variant, travel package and add-on as a separate
   offering with a stable key. A parentKey links related offerings; it never means
   the package is included. Do not carry Andamans-specific terms into another place.
8. For prices, collect currency, amount/range, unit, taxes and validity where
   relevant. Record them as exact confirmed text; these tools do not calculate
   totals, convert currencies, check stock or verify live availability. Keep
   eligibility, certification and safety requirements unresolved until confirmed.
9. Mark every internal selling floor, negotiation rule or private note internal.
   The reserved keys minimum_price, lowest_price, price_floor, discount_floor and
   private_notes require internal audience. Internal facts never enter the handbook.

## Save progress

Call save_business_draft with expectedRevision and the complete merged content.
This replaces the private draft: include everything that must be retained. It is
bounded to 48 KB and eight offerings. If it does not fit, explain the limit; never
silently truncate facts or remove previous offerings. Do not claim this is an
unlimited product-inventory system. A stale revision requires a fresh read and
merge, not an automatic overwrite. Report a saved draft only from a successful
tool result. A failed call or local chat text is not persistent progress.

## Review and approve a private revision

Call review_business_draft with the current expectedRevision and omit confirm.
Show the business identity, the full proposed facts and relationships, the exact
generated handbook, and the excluded internal/unconfirmed/unknown facts. Names
are part of the draft being approved. Explain what is still missing and that
absent facts will require confirmation rather than guesses.

Only after the owner approves that review, call the same tool with confirm true,
the same expectedRevision and its previewId. The review expires after 30 minutes;
edits or a new review invalidate the earlier one. If refused, read, review and
obtain approval again. Never use approval of one company or revision for another.

Approval stores a private structured snapshot. It does not apply knowledge,
send messages, publish a brochure/page, create checkout inventory or switch on AI.
Subsequent draft edits preserve the last approved snapshot. Explain when the
current draft has unapproved changes. This slice keeps the latest approved
snapshot, not a complete revision history or automatic restoration system.

## Apply approved knowledge separately

The approved result contains an exact dossier.handbooks payload. If the owner
wants it in the AI, read get_current_setup, then call save_dossier with that
payload and without confirm. Show its actual changes and business identity.
Explain that applying knowledge can affect answers immediately if the owner
already has AI replies enabled; this workflow does not toggle that switch.

Wait for separate approval of this application preview before calling
save_dossier with exactly that dossier, confirm true and its previewId. Report
actual saved/failed results and use a fresh get_current_setup to verify the saved
handbook text. Do not apply the latest unapproved draft instead of the approved
snapshot. Keep all unrelated instructions, offers, knowledge and answers intact.

Internal facts, source notes and unconfirmed claims are intentionally absent
from the generated handbook. Keep private information out of any public file,
page, message or brochure as well. This flow supplies text knowledge, not a PDF
or DOCX export and not a real AI answer/delivery test. Follow the separate live
test instructions before the business starts serving customers.
