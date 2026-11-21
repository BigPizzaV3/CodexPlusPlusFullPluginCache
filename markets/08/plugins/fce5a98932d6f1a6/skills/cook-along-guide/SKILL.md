---
name: cook-along-guide
description: >-
  Turn a supplied recipe, meal-prep plan, or food goal into a sequenced cook-along checklist and invoke display-guide. Use for step-by-step cooking instructions, mise en place, serving-size adaptations, coordinated dishes, observable doneness checks, and safe serving or storage guidance. Do not use for restaurant or grocery recommendations, nutrition or medical-diet advice, suspected food-poisoning assessment, recipe discovery without an actionable cooking guide, or improvised home-canning and fermentation protocols.
---

# Cook-Along Guide

Create a practical guide that a cook can follow without repeatedly rereading the source. Prefer a simple, safe sequence over culinary exposition, then present it with `display-guide`.

## Build the cooking plan

1. Establish the source and constraints.
   - Treat a supplied recipe as the source of truth unless the user requests an adaptation.
   - For a food goal, choose a straightforward preparation that fits the stated meal, time, ingredients, and skill level. Distinguish user-provided facts from assumptions.
   - Determine the target servings, dietary restrictions or allergies, available equipment, and any timing constraint that materially changes the plan.
   - Ask one concise question when a missing answer affects safety or feasibility. Otherwise, use a conservative, clearly stated assumption.
2. Normalize quantities and equipment.
   - Set one target yield and apply the same scaling factor to every scalable ingredient.
   - Keep one authoritative total quantity for each ingredient. Mark it as divided when separate steps use portions, and specify each portion at its point of use.
   - Use consistent units and practical precision. Do not round amounts in ways that materially change baking ratios, seasoning concentration, or food safety.
   - Do not scale oven temperature, cooking time, pan size, or appliance capacity mechanically. Adjust them only when the changed batch requires it, and state the adjustment.
   - Check that vessels and appliances can hold the batch safely; split batches when crowding would undermine cooking or exceed capacity.
3. Design the sequence.
   - Move washing, measuring, chopping, marinating, thawing, preheating, and equipment setup into preparation when they should happen before active cooking.
   - Order instructions by dependency. Start long passive tasks first and use their waiting periods for independent prep.
   - For multiple dishes, work backward from the serving time and place each action in one integrated sequence.
   - Make each instruction atomic and imperative. Include the vessel or tool, heat level or setting, approximate duration, and an observable endpoint when relevant.
   - Pair time estimates with sensory or measured cues; never rely on "cook until done" alone.

## Apply safety guardrails

- Treat an allergy as a safety constraint, not a preference. Clarify an ambiguous allergen before proceeding.
- Never claim that a dish, substitution, packaged ingredient, or kitchen is allergen-free. Tell the user to verify every label and account for shared tools, surfaces, oil, and other cross-contact risks.
- Preserve relevant handwashing, raw-versus-ready-to-eat separation, clean-tool, thawing, and storage steps. Do not recommend tasting mixtures that may be unsafe while raw.
- Use a food thermometer when safe doneness depends on internal temperature, and give both the measurement location and a non-temperature quality cue when useful.
- Verify exact safety-critical temperatures, holding limits, cooling times, and storage windows against current guidance from an authoritative government food-safety or public-health source. Prefer the user's jurisdiction when known. Do not guess when verification is unavailable.
- If a supplied recipe conflicts with current authoritative safety guidance, do not silently repeat the unsafe direction. Use the safer requirement and explain the change briefly.
- Do not improvise hazardous preservation processes or advise on whether symptoms after eating require treatment. Direct those cases to the appropriate validated process or health authority.

## Map the plan to `display-guide`

Use only the supported fields and omit empty optional sections:

- `requirements`: List ingredients with exact total quantities, noting divided uses, followed by essential equipment. Keep the target yield consistent with these amounts.
- `preparation`: List mise en place, safe setup, preheating, and advance prep in the order needed.
- `instructions`: Provide at least one dependency-ordered cooking action. Keep required safety actions here rather than hiding them in tips.
- `wrapUp`: Include finishing, resting, serving, prompt cooling or storage, and task-specific cleanup when relevant.
- `tips`: Add only optional substitutions, coordination advice, or troubleshooting that is not required for success or safety.
- `notes`: State the yield, material assumptions or adaptations, and concise allergy or safety caveats that apply to the whole guide.
- `reason`: Briefly state that the tool is presenting a cook-along guide.

Do not add titles, timing objects, citations, nested steps, or other unsupported fields. Put source citations in the surrounding response when external verification was needed.

## Check and present

Before calling the tool, verify that:

- Every ingredient used in an instruction appears in `requirements`, and every listed ingredient is used or intentionally reserved for serving.
- Quantities, servings, pan capacity, temperatures, and units agree throughout.
- Preparation completes the mise en place needed before each time-sensitive step.
- Instructions have no dependency inversions, unexplained simultaneous actions, vague endpoints, or duplicated work.
- Required allergy and food-safety controls are explicit, current, and not relegated to optional tips.
- `instructions` is non-empty and every checklist item is a concise, standalone action.

Invoke `display-guide` once with the completed guide. Keep the accompanying prose brief and use it only for necessary source attribution or a limitation that does not fit the guide.
