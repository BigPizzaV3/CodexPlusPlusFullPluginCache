---
name: read-results
description: Read CreceRank visibility, per-prompt results, history, and cited sources. Use when the user asks for the score, a summary, which prompts mention the brand, whether visibility improved, or which sites AI answers cite.
---

Use this skill to read scan results. Do not start a scan unless they also asked for a new analysis.

If the user gives a different instruction, follow that instruction.

1. Call `crecerank_whoami`. If no scan has completed, say so and stop.
2. If they name a brand, call `crecerank_list_brands` and `crecerank_set_active_brand` when it is not active.
3. Call `crecerank_get_panel` with `compact` true. Omit `scan_id` for the latest scan. Pass a `scan_id` from `crecerank_list_scans` when they name an older analysis.
4. For a paragraph, call `crecerank_get_simple_summary` with `lang` `es` or `en`. Pass `regenerate` true only when they ask for a new summary.
5. For question-level results, call `crecerank_get_prompts` with `compact` true. For one prompt's citations, call `crecerank_get_prompt_extras` with that prompt's id.
6. For one prompt's trend, call `crecerank_get_prompt_visibility_history` with its id. For the brand trend, call `crecerank_get_evolution`.
7. For cited domains and pages, call `crecerank_get_sources` with `compact` true. If they ask whether the same domains keep appearing, call `crecerank_get_domain_relevance_history`.
8. Call `crecerank_save_visibility_note` only when they ask to save a note, and pass the `scan_id` plus their text.

Report only figures and citations the tools returned. Say when the brand's own site is absent from sources. Do not treat sources as a backlink report.
