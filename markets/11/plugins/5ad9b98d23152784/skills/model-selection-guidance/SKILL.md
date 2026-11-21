---
name: model-selection-guidance
description: "Compare generation models when the user asks for a comparison or the trade-offs. Not needed when a valid model choice and current guidance are already in context."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Comparing models

Compare only compatible options from the current catalog. The catalog owns availability,
inputs, parameters, limits and price; this skill owns the criteria for a recommendation.

## Pick the right action

Use `givon_list_models` (CLI: `givon model list`) for browsing and comparison. Choose from
current active models by the requested result, reference media and priorities. Read the exact
chosen model with `givon_get_model_schema` (CLI: `givon model get <id>`) before authoring
its input. Use the catalog's `promptAuthoring` and schema `x-promptAuthoring` metadata for
language and reference semantics, together with the relevant craft and model-family guide.
If a current choice and guidance already cover the same inputs and constraints, reuse them.
The caller writes the final prompt; there is no separate selection-advisor or prompt-preparation
tool on this surface. Finish through `givon-ai-create` when the user asked to generate; a
comparison or prompt-only request does not authorize a paid job. Treat an unknown capability
as unknown and a lack of a compatible model as a constraint, not a service outage.

For a model the user named, check its contract; do not start a new contest between models.
If a current choice and the skills you need are already in context, use them while the
requirements stay the same. A change of inputs, operation or significant constraints
requires rechecking the affected facts; editing the text alone does not require reading the
same catalog or skill again.

Tell a request to choose apart from a request to make. For «сгенерируй фотореалистичного
человека», choose a compatible model yourself and continue preparing the generation. Do not
add a separate reply that explains the choice or asks «какую модель предпочитаете?» when you
have enough data. Explain the choice when the user asks, or when a significant limit or
trade-off needs their decision. Preparation does not replace the price check or the user's
permission to launch.

## Comparison method

1. Define the required result and the required inputs: text, a start frame, a reference,
   a source video, text to be spoken or other material.
2. Pick out the criteria that matter to the user: quality, speed, cost, editing, exact text,
   identity, sound or another explicit priority.
3. Compare the candidates by purpose, inputs, limits, defaults and price.
4. Choose one exact id. In a consultation, name the significant trade-off; in a request to
   generate, continue the action if no further decision is needed.

## When there is no exact match

A required condition does not become a preference just because the catalog does not support
it. Offer one useful conditional option: what the user asked for, what a specific model
supports and which requirements would have to change. Name every significant concession, not
only the first conflict you found. A second option is needed only when it offers a different
useful trade-off given the user's priorities.

Use the fields of the current contract, not a closed list of parameters in this skill. Check
the combination of mode, inputs and settings: separate maximums do not prove that they are
available together. Limits on source material and limits on the result are different.
Missing information means the capability is unknown, not that it is proven absent.

Before preparing or proposing a generation, agree with the user on any change to required
conditions, a replacement of a model they explicitly chose, or dropping materials or required
content. Permission already given for such a trade-off still holds; do not ask again. Combine
related concessions into one concrete question. If the user has not settled a choice between
conflicting priorities, do not make it for them silently.

For a chain of steps, check the capabilities of each step and whether their inputs and outputs
are compatible. Separate the native result from post-processing; report losses, and do not
promise exact preservation of identity or continuity across a splice. If there is no confirmed
useful alternative, explain the obstacle and the smallest change that would let the work
continue. Do not reduce the answer to the word "impossible", and do not invent a workaround.

If the current context is enough, do not reread the catalog or a skill just to explain a
trade-off. You need new information only for facts that are missing or have changed.

If the current catalog names Givon's primary pick for the task, use that recommendation among
the compatible models. Do not answer with a list of equal names or with "it is impossible to
choose" when the request allows a useful primary option. When speed or price is the priority,
consider suitable low-cost models, even if they appeared less often in the user's history.
Cheaper does not mean "draft only"; do not forbid final use without a concrete limitation.

## Evidence and freshness

Distinguish technical compatibility, Givon's recommendation, a measured result, a provider's
claim and creators' practice. Comparisons, benchmarks, popularity and social media examples are
useful as dated evidence: take into account the exact version, the task and what exactly was
compared. Popularity can explain why a workflow is common, but it does not override
incompatible inputs or an important limitation.

Do not present a saved review as a continuously updated ranking or trend monitoring. An older
list of models does not override the current catalog. If the user asks for a fresh summary,
use the available verification tools and name the date; if there are none, separate saved
information from what is not verified right now. An ordinary choice does not require
researching the whole internet again: give a primary option based on the relevant evidence you
have. A reason belongs in a consultation, not in an obligatory extra reply before every
generation.

Check a model the user named against its current contract. Do not rank from memory, by provider
or by keywords, and do not invent a universal "best" option.
