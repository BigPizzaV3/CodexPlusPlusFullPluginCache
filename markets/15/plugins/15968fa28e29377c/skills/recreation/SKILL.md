---
name: recreation
description: "Create a fresh lesson, quiz or activity-sheet family from saved prompt settings. Use when the teacher wants another generated version or an updated prompt while keeping the original."
---

# Recreate teaching resources

Resolve the source with `search_resources`. Use names and context to select the intended item; ask only when matches remain ambiguous. Never invent IDs or ask the teacher to find internal IDs.

Use `recreate_resource` for “make another version,” “edit the prompt,” or “generate this again with…” when the teacher wants a new AI result. It uses the owned source's saved prompt and generation settings, validates them against current permissions and plan limits, and creates new IDs without changing the original.

Supply only requested overrides in `changes`. `additional_instructions` replaces the full saved brief; call `get_generation_settings` with the resource type and ID first if you need to preserve its requirements while adding a change. New resources are created outside folders. New generation uses the normal quota and can produce different content and images.

For worksheets, `changes` also accepts `template`, `difficulty_levels` and `standard_ids`. Read `get_creation_context` for supported templates and difficulty levels, and use `search_curriculum_standards` to resolve requested alignment to real IDs from one curriculum. Each supplied field replaces the saved selection; omit it to keep the existing setting. Each requested difficulty creates a separate new worksheet, so changing to challenge only produces one challenge worksheet. Do not add extra versions or curriculum alignment unless requested. An empty `standard_ids` list clears alignment on topic-based worksheets; worksheets based on a lesson or series require a non-empty replacement because they otherwise inherit their source's standards.

For quizzes, use `resource_type: "lesson"`. Recreation preserves the quiz type, selected question types and saved source. Use `changes.question_count` or `changes.question_types` for quiz settings; the count excludes the cover. Do not use `slide_count` for quizzes.

Supported recreation is a quiz, a slide lesson (including a standalone version of a series lesson) or an activity-sheet difficulty family. Documents based on a lesson or series inherit their topic, grade, country and language from that source; use topic-based `create_documents` for a deliberately different audience or topic. Whole-series, workbook, legacy-worksheet and uploaded-file recreation are not supported by this tool. Explain that limit; do not silently drop attachments or change the resource type.

Treat recreation results like creation results: preserve every returned ID, never recreate an item that was already saved, and call `preview_resource` with the returned resource type and ID. Follow the creation skill for generation handling.

For a worksheet family, preview each requested difficulty using its ID in `versions`. A replacement brief describes one worksheet; Chalkie applies it separately to each difficulty. Never ask each worksheet to contain all difficulty versions.
