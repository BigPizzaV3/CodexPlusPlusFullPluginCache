# Product-design audit criteria

Apply the criteria that matter to the product and user journey. This is a diagnostic lens, not a checklist that forces a finding in every category.

## Task and decision clarity

- Can the intended user identify the page purpose and next action without reconstructing the interface?
- Does hierarchy follow the user's decision sequence rather than the implementation structure?
- Are primary, secondary, destructive, and reversible actions visually and verbally distinct?
- Are consequences, dependencies, and blocked states explained at the point of action?
- Do confirmations and success states communicate what changed and what happens next?

## Information hierarchy and content

- Do headings, summaries, labels, values, and help text have distinct jobs?
- Is important information visible before decorative or low-priority content?
- Are terminology, units, formats, dates, currencies, and statuses consistent?
- Does copy name the user's object and action precisely, avoiding generic filler?
- Do tables, charts, and cards support comparison rather than fragmenting related facts?

## Visual system

- Check type scale, weight, line length, line height, contrast, spacing rhythm, alignment, density, color roles, icon use, borders, elevation, and component states.
- Distinguish deliberate exceptions from drift. A system should create coherence without making every screen identical.
- Flag tokens or components only when their rendered use creates inconsistency, confusion, accessibility problems, or unnecessary maintenance risk.
- Evaluate whether the visual language fits the product's audience, stakes, and brand. Do not treat a fashionable style as a universal standard.

## Layout and responsiveness

- Does the layout preserve reading order, task priority, and access to actions as space changes?
- Do grids, sidebars, sticky regions, dialogs, tables, and charts behave within the actual available container?
- Are truncation, wrapping, overflow, hidden content, and unexpected horizontal scrolling controlled?
- Does increased text size or zoom reveal content loss or blocked interaction?
- Use [responsive-testing.md](responsive-testing.md) for the evidence matrix.

## Interaction and states

- Inspect default, hover, focus, active, selected, disabled, loading, empty, validation, error, success, expanded, and destructive states when relevant.
- Confirm that visual feedback is timely and attached to the action that caused it.
- Check that disabled controls explain prerequisites when the reason is not obvious.
- Check whether asynchronous changes preserve context and prevent duplicate or contradictory actions.
- Judge motion by comprehension, continuity, and comfort—not novelty. Respect reduced-motion preferences.

## Accessibility

- Inspect semantic structure, accessible names, keyboard reachability, focus order and visibility, contrast, target size, error identification, status announcements, and alternatives to color or motion.
- Test the required journey with keyboard interaction where access allows.
- Treat serious accessibility barriers according to user impact, not as a separate cosmetic category.
- Record the standard or method used when making a compliance claim. If not tested, say so.

## Data-dense and consequential interfaces

- Make labels, totals, units, assumptions, statuses, deltas, and data freshness unambiguous.
- Preserve alignment and comparison across rows and columns.
- Keep warnings and destructive actions close to the affected object.
- Do not claim the numbers are correct from appearance alone. Report only presentation, interpretability, and interaction risks unless underlying logic was separately tested.

## “Generic” or “AI-made” appearance

Do not diagnose generic design from a single visual trope. Look for accumulated evidence such as:

- interchangeable brand language and imagery;
- hierarchy created mainly by oversized type or repeated cards rather than the task;
- excessive containers, badges, gradients, glows, or decorative copy without informational purpose;
- inconsistent spacing, icons, radii, or component behaviors suggesting ungoverned generation;
- plausible-looking controls or content that do not support a real state or action; and
- polished hero sections paired with neglected dense, error, or mobile states.

Translate any such diagnosis into product-specific evidence and a repair direction. “Looks AI-generated” by itself is not a finding.

## System versus page findings

A system finding has a shared root cause and appears across components or routes. Cite representative instances and recommend a system-level repair. A page finding is confined to a particular journey or composition. Do not recommend a design-system change for an isolated local exception unless the evidence supports reuse.
