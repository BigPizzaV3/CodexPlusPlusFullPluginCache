---
name: annotations-extensibility
description: Explain or integrate the Browser Annotation API to customize annotation mode for a website in the ChatGPT browser. Use when choosing selectable content, attaching context to comments, adding custom controls, or supporting objects in canvas and 3D views.
---

# Annotations Extensibility

Customize website annotations with HTML attributes and `document.oai.annotation`. The browser owns selection, comment editing, and submission. Add customization for a concrete feedback task, using existing application state and rendering.

Read the [public documentation](https://learn.chatgpt.com/docs/annotations-extensibility) for availability, API contracts, schemas, limits, and examples before implementing. Do not invent missing contracts.

## Choose the extensibility features

- **Selection targets:** use HTML attributes to make a whole card, row, or other logical element selectable instead of its nested decorations. Keep selection containers narrow.
- **Text selection:** enable drag-to-select text in articles or documents so people can comment on specific passages. Text-selection containers do not clip the selected range.
- **Selection metadata:** attach context that helps ChatGPT understand or act on feedback, such as a hidden record ID or source revision. Omit context already available from the page or included identifiers.
- **Annotation entry points:** use `request()` to open a comment for an element or native text range from a site button or menu. Optionally suggest a comment the user can edit before sending.
- **Annotation mode:** `toggle()` enables or disables annotation mode without opening a comment. Use the mode getter and events to keep the site's button in sync with the browser.
- **Editor default mode:** use an HTML meta tag to show advanced annotation controls immediately for browser-initiated annotations. Site-initiated requests can choose their editor mode separately.
- **Custom controls:** use `registerControls()` to add choices to the annotation editor. Preview reversible changes to design tokens or component properties, or collect preferences such as email tone without changing the page.
- **Canvas objects:** use `registerSurface()` to make individual objects in a chart, canvas, or 3D scene selectable when they have no separate DOM elements. The site's renderer supplies picking, object identity, and bounds.

## Integration rules

- Add optional names, roles, metadata, and headings only for missing context. DOM details, screenshots when captured, and surface hit IDs already reach the model. Preserve necessary hidden identity or revision context; omit visible, inferable, duplicated, or retrievable information unless capture needs it. Exclude secrets and behavioral instructions.
- `request()` and `toggle()` need live user activation. Acceptance does not confirm editor opening or submission. Preserve the intended feedback target and omit suggested comments for open-ended feedback. Native text-range requests use the default editor without metadata; preserve DOM and browser Selection.
- Follow [starting-value guidance](https://learn.chatgpt.com/docs/annotations-extensibility#configure-controls-and-starting-values): `currentValue` reflects valid ordinary drafts, including unsaved edits, not previews or unfinished input. Use `defaultValue` for intentional proposals; omit `currentValue` for choices without an existing value. If an update or request fails or is rejected, discard the attempted proposal and restore the prior controls and proposal state. Accepted requests may queue before capture, so acceptance must not clear proposals.
- Follow [preview/reset behavior](https://learn.chatgpt.com/docs/annotations-extensibility#handle-previews-and-resets): previews never commit changes. Comparison and reset use supplied captured values, even off-step originals. Preserve ordinary Save behavior, unfinished input, and previews through unrelated edits. Editing the same setting replaces its preview; Show/Hide must fulfill the visible button's promise.
- Future controls follow ordinary edits and target changes; existing annotations retain captured baselines and callback routing. Save, preview events, and hover must not redefine controls. Route events to their owning DOM target or captured graphics object, not the current selection.
- Use stable graphics IDs, renderer picking, and viewport CSS bounds. Invalidate changed geometry/content and discard stale work. Empty picks and lookup failures differ: preserve documented DOM fallback on failure.
- Reuse owned registrations and batch identical controls. Handle unavailable or revoked capabilities without breaking ordinary editing; Space temporarily restores page interaction during annotation mode. Cleanup must restore ordinary rendering and release owned resources.

## Verification

Run the relevant [integration checks](https://learn.chatgpt.com/docs/annotations-extensibility#test-your-integration). Report unavailable browser verification; ordinary page rendering does not validate host integration.
