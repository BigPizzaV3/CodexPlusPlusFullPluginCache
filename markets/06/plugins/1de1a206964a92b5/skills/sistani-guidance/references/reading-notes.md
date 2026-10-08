# Reading and source-integrity notes

This is a local testing corpus, not a certified transcription or an official religious service. No external religious text was added. The full original PDF bytes are preserved in the developer kit's `source-pdfs/` directory, outside the installable plugin. They are not automatically accessible to a person who installs only the plugin.

## Text conversion

All 848 physical PDF pages have an extracted-text entry. Blank layout lines were removed. Source wording, source punctuation, ordering, printed headers, and footnote text were otherwise retained. Corrupt control characters or replacement glyphs were marked `[UNREADABLE GLYPH]`, not guessed. Retaining text is not the same as verifying extraction accuracy. Some text in these PDFs already has missing spaces, awkward wording, and inconsistent numeral extraction.

Do not silently fix a sentence, number, transliteration, apparent contradiction, or Arabic passage. Never quote a corrupt extraction as verified verbatim source text. When needed, use the original or a rendered page. If that is unavailable, explain the limitation and avoid a definite answer based on the corrupt span.

## Page boundaries and footnotes

Blocks use 12 physical pages for navigation, not semantic completeness. Complete the passage using neighboring blocks. Questions can end on one page with answers on the next. A footnote can materially qualify the main paragraph. For example, the Women's Religious Rules discussion on PDF p. 13 has a substantive footnote below the dialogue; it must not be dropped when relevant. Numbered items can also refer to definitions on other pages.

## Different kinds of source material

Hajj Rituals uses `Rule` identifiers. Summary of the Rules of Worship uses `Issue` identifiers. The other books contain many unnumbered sections and dialogues. Use actual locators, not invented ruling numbers.

Jurisprudence Made Easy's translator states in the foreword, PDF pp. 3 to 4, that the glossary is his contribution and that some parenthetical text is explanatory. Treat translator/editor commentary as such, not as a newly issued ruling. Approval of a source book is not approval of this assistant.

Navigation labels in the per-book indexes sometimes use simplified transliteration or descriptive labels to locate generic headings such as "Introduction". Verify the source's actual heading before quoting a section title.

## Editions and currentness

English Islamic Laws 2023 was named in the original prompt but was not supplied. A Code of Practice for Muslims in the West is a different book. The latter's prefatory material describes translation and amendments associated with an earlier Arabic edition. Jurisprudence Made Easy includes an English-edition preface dated 1997. These facts do not establish which of two differing rulings is applicable today. Dates are provenance, not an automatic precedence policy.

Keep apparently conflicting passages separately attributed. Do not consolidate several books into a single synthesized "ruling" database without qualified review.

## Visual and Arabic material

The plugin includes rendered source-page images for:

- A Code of Practice for Muslims in the West, PDF pp. 283 to 288: scanned answer specimens.
- The same book, PDF pp. 299 to 305: fish-name tables and illustrations.
- Summary of the Rules of Worship, PDF p. 36: Arabic and transliterated prayer-call text.

Those pages link to their images in the relevant text blocks. These are selected visual fallbacks, not a complete image representation of every PDF page. Other Arabic text or layout-sensitive content may need inspection of the original PDF by the developer. Whether a plugin host can open packaged images must be tested. Do not infer species identities or Arabic wording solely from an unreliable extracted text sequence.

## Search and source restrictions

The optional local helper only searches the installed text files. Keyword matching can miss synonyms, transliterations, multi-topic dependencies, and indirect references. Retry with alternate terms and read the appropriate section indexes before deciding the corpus is insufficient.

The official Q&A restriction in SKILL.md is workflow guidance. It is not network enforcement. Technical enforcement of source access requires an implementation that validates destinations and content, such as a controlled retrieval server. That still does not by itself guarantee the accuracy of an AI answer.
