---
name: obi-prompt-generator
description: Compile an Open Bible Images brief, research, entities, composition, and character references into a model-neutral image direction and provider-ready prompt package. Use when preparing or revising an image-generation prompt without changing project facts, including private working drafts and feedback-driven revisions.
---

# OBI Prompt Generator

Prompts are disposable delivery formats. The approved composition and character records remain authoritative. Read [references/prompt-package.md](references/prompt-package.md).

When a canonical project JSON file is supplied, preserve all other sections, update only `prompt_packages`, increment its artifact revision and the project revision, and append a history/capability-run entry. If revision was triggered by feedback or review, link the prompt revision back to the upstream artifact/finding that required it. If no project file is supplied, label the result `unpersisted`.

## Workflow

1. Load the latest relevant artifacts and determine whether this is a private working draft or formal approved use.
2. Identify the target provider, model, aspect ratio, generation mode, and reference-image capabilities. If no provider is named, default the user-facing prompt to Nano Banana Pro while retaining a model-neutral master direction.
3. Check whether the requested change is actually a prompt problem. If research, entity, character, or composition data is wrong or unresolved, return the earliest required capability instead of hiding the problem in prompt wording.
4. Build a model-neutral master direction faithful to the current composition and character records.
5. Translate it into concise provider-ready instructions, normally 150–400 words and ordered by visual importance. Apply the Research & Create prompt standards: observational documentary realism, natural light, ordinary regionally plausible people, material and environmental realism, practical wear, believable scale, and natural spatial relationships.
6. Map each reference image to its intended control and prevent unintended transfer of style, clothing, pose, or identity.
7. Include historically important exclusions and known model failure risks without overwhelming the positive direction.
8. For feedback-driven revisions, change only prompt instructions affected by the approved upstream revision and preserve unrelated successful instructions.
9. For a private draft, a working or draft composition may produce a `working_private_draft` prompt with provisional choices preserved. For formal OBI use or costly batch generation, require an approved composition and return an `approved_provider_prompt`. List only material blockers.
10. If the user explicitly requested an image revision and the prompt is ready, return disposition `needs_generation`; otherwise stop with the updated prompt.

## Boundaries

- Do not introduce new biblical, historical, entity, or composition facts.
- Do not convert uncertainty into certainty.
- Do not promise exact compliance from a generative model.
- Do not use fake inscriptions, halos, fantasy conventions, or anachronisms unless explicitly approved.
- Do not generate or accept an image unless requested.
- Do not substitute cinematic spectacle, glamour, uniform beige dirtiness, or a long generic negative list for specific historical direction.
- Do not patch an upstream factual problem with downstream prompt tricks.

Completion means the prompt is traceable to its project artifacts and clearly labeled either `working_private_draft` or `approved_provider_prompt`.

## User-facing response

Return the usable prompt first. Add only essential settings, reference instructions, and up to three risks or decisions. If an upstream issue blocks a trustworthy prompt, state the single earliest action needed, such as **Research this**, **Update character**, or **Revise composition**. Do not repeat the entire project brief or explain every translation choice.
