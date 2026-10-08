# OBI Image Project record

The canonical prototype artifact is one UTF-8 JSON file named `obi-image-project-<slug>.json`. A local Codex workflow may store it at `obi-image-projects/<slug>/project.json`. In ChatGPT, preserve the same file as a durable user-facing artifact when available; otherwise return it for the user to retain and attach later.

Top-level fields:

- `schema_version`
- `project_id`
- `slug`
- `title`
- `project_revision`
- `created_at`
- `updated_at`
- `workflow_mode`
- `brief`
- `sources`
- `research`
- `entities`
- `composition`
- `characters`
- `prompt_packages`
- `generations`
- `reviews`
- `feedback`
- `capability_runs`
- `decisions`
- `history`

Use `workflow_mode` values `quick_create`, `guided_create`, or `full_obi_project`.

Each artifact section includes its own `status`, `revision`, and provenance. Every specialist preserves sections it does not own, changes only its declared output section, increments `project_revision`, and appends a history entry containing the stage or capability, action, actor or skill, timestamp when available, and changed artifact revision.

Maintain artifacts independently so one stage can be revised without overwriting the others.

| Artifact | Minimum content |
| --- | --- |
| Brief | Request, Scripture scope, narrative moment, audience, format, style direction |
| Sources | Candidate and approved sources, provenance, reliability, licensing, supported claim IDs |
| Research | `full_brief` (1,000–2,000 words), `public_summary` (about 200 words), claims, evidence level, source IDs, visual implications, uncertainties, avoidances |
| Entities | People, places, objects, groups, proposed or existing OBI IDs |
| Composition | Subjects, actions, spatial relationships, setting, camera, light, narrative focus |
| Characters | Entity, portrayal, variant, time-specific appearance, references, continuity notes |
| Prompt package | Model-neutral direction, provider prompt, exclusions, reference mapping |
| Generation | Provider, model, settings, prompt snapshot, references, private outputs, and working or approved-use label |
| Review | Findings, severity, evidence, affected region, root-cause artifact, recommended capability, proposed correction |
| Feedback | Human or AI feedback, target, source, status, root cause, next capability, linked runs, resolution |
| Capability run | Requested capability, trigger, specialist skill, input targets, output artifact revisions, originating feedback/finding, disposition |
| Decisions | Person, decision, artifact version, reason, timestamp when available |

## Feedback records

Every material feedback item should have a stable `feedback_id` and preserve the original statement. Record:

- `source_type`: `user`, `creator`, `consultant`, `external_reviewer`, `image_review`, or `other`
- `source_name` when supplied
- `target_type` and `target_id` when available
- `image_region` when relevant
- `comment`
- `status`: `open`, `investigating`, `resolved`, `dismissed`, or `needs_human_decision`
- `root_cause_artifact`
- `next_capability`
- `capability_run_ids`
- `resulting_artifact_revisions`
- `resolution_note`

Feedback is not automatically factual. Preserve disagreement and the evidence used to resolve or retain it.

## Capability-run records

Record enough lineage to explain why work happened:

- `run_id`
- `capability`
- `trigger_type`: `automatic`, `manual`, `feedback`, or `follow_up`
- `trigger_text`
- `specialist_skill`
- `input_artifact_revisions`
- `parent_feedback_id` or `parent_review_finding_id` when applicable
- `output_artifact_revisions`
- `disposition`: `resolved`, `needs_sources`, `needs_research`, `needs_entity_revision`, `needs_composition_revision`, `needs_prompt_revision`, `needs_generation`, or `needs_human_decision`

This creates a traceable chain such as external comment → review finding → research → new sources → research revision → composition revision → prompt revision → generation → review.

Use `missing`, `working`, `draft`, `needs_decision`, `approved`, `rejected`, or `superseded` for artifact status. `working` permits private exploration but never implies approval. Never infer approval from the existence of content.

Preserve links between claims and sources, entities and character references, feedback and capability runs, and every generation and the exact prompt/settings that produced it. Validate JSON before handing it to another stage.
