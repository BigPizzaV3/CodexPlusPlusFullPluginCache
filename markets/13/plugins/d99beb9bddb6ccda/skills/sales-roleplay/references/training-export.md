# Requested training exports

Read for an actual export or explicitly requested format/next-action choice, not merely to show the completed-feedback labels. Export is a quiet control over available completed evidence, never a buyer turn, automatic ending, reevaluation or company-side save.

## Select content and format

Support Training Report and Full Roleplay Record in DOCX, Markdown and TXT. Preserve identifiers TRAINING_REPORT_DOCX / TRAINING_REPORT_MARKDOWN / TRAINING_REPORT_TXT and FULL_ROLEPLAY_DOCX / FULL_ROLEPLAY_MARKDOWN / FULL_ROLEPLAY_TXT. Clear Japanese/English equivalents work. A direct content+format request bypasses menus; ask only for genuinely missing content, format or ambiguous attempt.

The explicit “Export Training Report” action selects the current unambiguous Training Report; when no format was chosen, offer DOCX (Word), TXT and Markdown in one brief question. Direct “Download Word Report (.docx)” / “Wordレポートをダウンロード” still selects Training Report DOCX immediately, and direct TXT/Markdown requests select those formats. Save Scenario is a different action handled by personal-scenarios.md. Do not export because an action group appeared.

An explicitly requested next-action menu retains legacy mappings: 1=Training Report, 2=Full Roleplay Record, 3=eligible Focused Retry, 4=New Practice, even when displayed retry-first. Format choices normally show Word / Markdown / Plain Text. Only if legacy numeric format compatibility is explicitly requested, retain 1=Markdown, 2=TXT, 3=DOCX. Consume that displayed menu once; pending Start/End choices take precedence and never accept numbers.

An unfinished current attempt has no completed report. Offer the existing End/Continue gate, without silently ending/exporting. After confirmed ending give feedback, then wait for a separate export selection; Continue discards the deferred export choice and restores the preceding state quietly. Already pending confirmation must be resolved before a current-attempt export. An explicitly named, genuinely available prior completed snapshot can be exported without changing the current lifecycle. Never invent a prior attempt.

## One immutable snapshot, all formats

Use available scenario/configuration and source classes, actual ordered buyer/seller speech, seller IDs, immutable **Feedback Content** only, coverage/outcome, UNKNOWNs and original/retry relationships. Never include the **Post-training Actions** menu or application controls in a report. No hidden/system/implementation instructions. A Training Report includes concise context, actual buyer and seller quotations and the whole original feedback. A Full Roleplay Record additionally includes the public six-field configuration, fact groups/meeting context and separately labeled available retry records within the requested scope.

Before rendering, account for: actual ordered dialogue; complete Feedback Content from heading to final coaching/limitations **excluding action labels**; reviewed/pending coverage and limitations; completion/commercial outcome; relevant fact/source/UNKNOWN boundaries; requested attempt and retry relationships. Each is available, explicitly not applicable or unavailable. No retry in an A1-only report is not a missing retry; a requested known-but-unavailable retry is a gap.

Copy the complete original **Feedback Content** as one ordered source block, including headings, status/coverage/outcome, every card/comparison, exact seller quotes, suggestions and limitations, **excluding separately displayed Save/Retry/Export UI actions**. Do not rebuild it from selected Feedback paragraphs, rename its source heading, paraphrase or truncate the feedback. Label an outer block Original Feedback — Verbatim / 元のフィードバック — 原文 without changing its source text.

Preserve quotations character-for-character, paragraph boundaries, internal line breaks, source language, speaker attribution, order and namespaces. Include actual buyer opener/responses/final spoken line; a summary or a quoted hypothetical cue cannot replace them. Suggested rewrites remain unperformed. Keep original and retry attempts separate, and do not invent historical offsets or evidence IDs.

Retain actual visible source assessment labels and their canonical meaning (positive/negative/neutral/missed_opportunity). Default output does not newly introduce internal codes absent from source feedback. Missing assessment stays unavailable; do not recompute or default to positive. Geography belongs only to the actor/source that actually established it: never infer seller country from Japanese language, buyer location, product origin or developer identity. No new price, guarantee, purchase, ability score or resolution of UNKNOWN during formatting.

COMPLETE requires all required source segments accounted for and every promised available segment actually delivered. Genuine missing source means PARTIAL, with covered/missing/pending scope, Partial / 一部の記録 in the title and `partial` in the filename. Do not fabricate missing text. A renderer dropping available text is a rendering failure: repair from the unchanged snapshot and recheck, not conceal it by relabeling partial. Multipart output remains undelivered until all promised parts arrive; wait for explicit continuation and distinguish output length from lost source.

## RC.10 DOCX semantic formatting and evidence checks

There is no mandatory Markdown intermediate file or external Pandoc/third-party converter.
Use the host's genuine DOCX generation ability, implementing the following semantic mapping when
Markdown notation is *formatting* rather than literal source content:

- `# heading` => native Word Heading 1; `##` => Heading 2; `###` => Heading 3.
- `**bold**` / `__bold__` => native bold runs; inline double stars NEVER mean Heading 2.
- `*italic*` / `_italic_` => native italic runs; `***text***` => bold and italic.
- `~~text~~` => strikethrough runs; inline backticks => code/monospace runs.
- `- item`, `* item`, `+ item` => actual bulleted lists; `1. item` => numbered lists.
- `> quote` => quote paragraph; `[label](URL)` => an actual hyperlink, after URL validation.
- `---` => a horizontal separator; Markdown tables => actual Word tables.
- Fenced code blocks and escaped Markdown punctuation remain literal/preformatted; do not parse their syntax.
- Blank lines separate paragraphs; preserve intentional source line breaks.

For actual performed buyer/seller utterances, preserve original *meaningful textual content*, spelling,
wording, punctuation, speaker, sequence and paragraph breaks. Presentation-only Markdown delimiters
may be rendered as native styling instead of leaking `**` into Word. However, if a salesperson
literally says the characters `**` as part of their actual speech, preserve them exactly; do not
strip arbitrary asterisks. Keep original raw dialogue evidence available separately for exact-fidelity checks.

Use the SINGLE same immutable attempt snapshot for Markdown, TXT and DOCX. Do not generate or
re-evaluate a new seller assessment during rendering. Before delivering the DOCX:
1. Compare transcript SELLER IDs and original recorded words against the immutable ledger.
2. Validate reviewed seller IDs and count against Feedback Content; never score a BUYER turn.
3. If previously finalized original feedback is inconsistent with recorded dialogue, DISCLOSE the
   discrepancy visibly, preserve original quoted feedback verbatim, and do NOT certify it corrected.
4. Ensure headings, lists, emphasis and links have native Word formatting; no unexpected Markdown decoration.
5. Confirm UI-only actions (Save Scenario, Export, Download, Load, Start/End) are absent from report body.
   Per-card Retry control labels should be separated into the Post-training Actions group during
   feedback generation; do not silently delete text from a pre-existing immutable feedback snapshot.
6. Validate all performed turns appear once in the transcript, original feedback is complete as
   actually finalized, UNKNOWN fields preserved and document opens without blank/truncated pages.
If available evidence cannot support these assertions, report a PARTIAL or explicit quality limitation;
do not invent evidence or claim DOCX verification from file existence alone.

## Language and delivery

EXPORT_LANGUAGE defaults to feedback_language. An explicit Japanese/English export explanation preference governs all newly authored export prose, including surrounding acknowledgments, headings, status, captions and closing lines; it does not change practice/feedback language. Preserve source quotations/whole feedback in their original languages. Any requested translation is a separate labeled aid. Begin directly with the requested artifact when content/format are clear; avoid redundant wrappers/menus.

- Markdown: clean headings/lists; preserve literal source blocks, using a longer fence than any embedded fence. Deliver all promised copyable text with an accurate suggested filename. Inline content alone is not a saved/downloaded file.
- TXT: readable plain text, speaker labels and paragraph separation; add no Markdown syntax. Literal source punctuation/Markdown characters remain unchanged.
- DOCX: use only genuine current-host file tools. Create a real Office Open XML document, verify its package, name, actual text and paragraph/line-break fidelity against the immutable snapshot, including every quote and all Feedback Content beginning-to-end while excluding UI actions. Render authored report headings/lists/bold as Word styles instead of exposing Markdown decoration as raw syntax. **Preserve the original meaningful text of performed speech. Translate presentation-only Markdown delimiters into native DOCX formatting, but keep delimiters that are truly literal spoken/source characters.** Keep original raw source strings for verification; never paraphrase or change the spoken claims. Preserve styling without adding new markup characters to source prose. Existence, ZIP validity or scattered matching phrases alone are insufficient. Expose only a real generated reference/attachment; actual download evidence is separate from generation. If generation, verification or delivery is unavailable, say which failed and offer separately requested MD/TXT. Never rename text as .docx, invent paths/links or silently substitute formats. Do not use an external server/other plugin fallback.

Use accurate names such as `b2b-sales-training-report-A1.docx` or `b2b-sales-roleplay-record-A1.md`; add `partial` / `part-01` where applicable. Do not invent dates or saved locations. Inspect the whole rendered output against the same snapshot before delivery. A source original table remains original even when new summaries use simple lists.

No automatic upload, history synchronization, Scenario Exchange JSON export or personal saving occurs through report export. Explicit redaction must be labeled redacted, with omissions identified; redacted text is not verbatim/full. Preserve the original evidence while available. User-requested personal definition saving is a separate create-only flow, never a report/history upload.
