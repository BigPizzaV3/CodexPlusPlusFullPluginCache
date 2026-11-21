# Draft from Bob's plan

Turn an existing Bob content-plan item into finished content using its actual brief, sources, format, and profile voice. Bob is Postiv's content planner. This playbook fulfills selected items; it does not change the user's strategy or configure Bob. Follow the parent skill's workspace/profile selection and shared rules.

Example requests:
- “Write Thursday's Bob item.”
- “Turn this week's planned ideas into drafts.”

## Select and read the item

Use `list_content_plans` for the requested profile/week unless an exact item ID is already available. Show a concise selection when the user has not specified an item or authorized you to choose. If they requested all eligible items, proceed within that scope. Note existing draft links, completed status, and passed target days so you do not create duplicate content or assume an old date is still a publishing instruction.

Call `get_content_plan_item` for every selected item before drafting. A plan-list summary is not the drafting brief. The returned package supplies the actual topic, angle, goal, format, profile, voice, source materials, research, and `createPostInput` where applicable. Confirm its profile matches the requested target; resolve any mismatch before saving.

Use the package's supplied sources and voice directly. Do not re-search the knowledge base when `sourceMaterials` already covers the brief; search only if that material is empty as instructed by the Tool Definition. Fetch missing style only if needed. If a key claim remains unsupported, ask for that fact or narrow the claim. Do not invent research to complete the brief.

## Develop the planned idea

Make the intended audience question and the item's answer clear. Use the item's actual evidence and angle rather than producing a generic post about the topic. Preserve the requested format; if the material would work better another way, propose the change instead of silently replacing the plan.

For text posts, use the returned `createPostInput` as the basis for `create_post`, filling in the developed copy while preserving profile and plan attribution. For carousels or infographics, use the appropriate available creation tool and its own current schema, retaining `planItemId` and `integrationId`; do not pass a text-post input object into a visual tool. Apply the parent's carousel/infographic workflow when relevant. Do not create both formats unless requested.

If the item already has a draft, read that draft and revise it when the request calls for revision. Treat published or locked content according to the current tools; do not work around restrictions by silently making a duplicate.

## Close the loop

Present the full copy or use `show_post` for an editable review card. For visual review, prepare exports with `render_carousel` if needed, then use `show_carousel` and its returned Postiv links. Follow the parent's presentation rules; do not open a card after every intermediate operation. For multiple items, make it clear which draft belongs to which plan item. Report any gaps or failed items individually rather than claiming the entire plan was completed.

The creation tools manage plan attribution; do not invent an additional plan-update tool. A request to draft planned content does not authorize scheduling it, changing pillars, changing cadence, or enabling recurring work. If scheduling was explicitly requested, establish a current valid time and use the parent's scheduling rules, preserving existing approval gates.
