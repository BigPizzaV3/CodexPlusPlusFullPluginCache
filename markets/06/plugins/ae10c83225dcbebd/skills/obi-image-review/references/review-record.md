# Review report

For every finding record an ID; lens; severity (`critical`, `medium`, `minor`, or `encouragement`); deduction; confidence; evidence label; visible observation; expected requirement; supporting artifact, claim, source, or Scripture reference; image region; likely origin; root-cause artifact; minimum correction; recommended next capability; disposition; and whether a human or consultant decision is needed.

Recommended next capability values are `research_context`, `find_sources`, `define_entities`, `character_continuity`, `revise_composition`, `build_prompt`, `generate_draft`, or `human_decision`.

Disposition values are `resolved`, `needs_sources`, `needs_research`, `needs_entity_revision`, `needs_composition_revision`, `needs_prompt_revision`, `needs_generation`, or `needs_human_decision`.

When a review was triggered by user, collaborator, consultant, external reviewer, or prior AI feedback, record `feedback_id` or other source linkage and preserve the original comment. When follow-up capabilities run, append their run IDs and resulting artifact revisions without replacing the original finding.

Record the starting score, deductions, final score, pass/fail/preliminary result, review confidence, consultant recommendation and exact question, overall recommendation (`human_review`, `revise`, or `unusable`), blocking findings, positive elements worth preserving, non-deducted research notes, localized edit prompt, and any unresolved handoff questions.

`human_review` means only that no known blocker prevents a person from considering acceptance. It is not approval.
