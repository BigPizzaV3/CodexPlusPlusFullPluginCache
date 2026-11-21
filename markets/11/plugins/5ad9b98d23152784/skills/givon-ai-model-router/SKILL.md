---
name: givon-ai-model-router
description: "Inspect the live Givon AI catalog, model schemas, parameters, capabilities and costs before generation. Task-specific selection guidance lives in model-selection-guidance."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Givon AI Model Router

Recommend one practical model path by default. Keep catalog detail hidden unless
the user asks for comparison.

## Route

1. Start with `givon_list_models`; filter by modality, status, tags, or query.
2. Short-list active models only unless the user asks about coming-soon or
   deprecated models.
3. For every candidate you might recommend, call `givon_get_model_schema`.
4. Compare the user's required fields with schema-supported fields, asset slots,
   variants, and cost metadata.
5. Recommend one model and the minimum valid `input` shape.

Before live catalog/schema inspection, name only the requested result and
compatibility needs. Do not declare an executable generation/edit mode:
reference-conditioned creation may be exposed as a still-generation input or
as an edit operation, and the selected schema owns that distinction.

## CLI Flow

When working through the CLI, use `givon model list --kind <image|video>` for
live catalog discovery and `givon model get <id>` for schema inspection. Choose
the model from these instructions and the live schema; do not rely on a separate
CLI heuristic.

Selection priorities come from the user's requested result and the relevant
specialist workflow. Availability, input compatibility, quality guidance,
defaults and cost come from the live catalog and schema.

## Answer Shape

- Give one recommendation first.
- Use a table only for explicit comparisons.
- Mention costs from model metadata or live responses.
- A separate creation intent starts generation; catalog questions end with the
  recommendation and supported input shape.
- A user-named model gets a full-catalog lookup when filtered search misses it.
- Classify by the requested result, required inputs and user priorities, not by
  tags alone.
- For asset/reference workflows, treat `x-assetSlots` as capability discovery
  plus a schema checklist. Media is passed only through fields present in the
  selected model's `input` schema; a schema without media fields is prompt-only.

Read [references/model-selection.md](references/model-selection.md) for the
schema checklist.
