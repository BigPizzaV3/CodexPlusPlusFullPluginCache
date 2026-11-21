---
name: create-mockup-template
description: Create a realistic scene of any blank product, turn it or a shared photo into a reusable Wrap mockup template, then let the user place their designs on it and export the mockup. Use when the user asks Wrap for a product scene or a mockup, wants an image turned into a mockup template, or asks to reopen a Wrap mockup.
---

# Create a Wrap mockup template

Explicit user instructions take priority over this default workflow. For
example, if the user requests conversion without opening a preview, use the
data tools and omit the preview tool.

Before you generate a scene image for a mockup, call `get_scene_prompt` with
the product and setting the user asked for. Generate the image with the prompt
it returns and follow its next steps.

Unless the user already asked you to convert it, do not convert a scene you
just generated or edited. End your reply by telling the user to keep asking
for changes until they are happy with it, and to reply "convert" when it is
ready. When they do, convert the latest scene.

Use the image the user refers to. Pass its host-provided file reference to
`create_mockup_template`; do not invent file IDs or download URLs. If the image
is not available as a file, ask the user to select or attach it.

Immediately call `open_mockup_preview` with the returned `template_id`, before
waiting for conversion. The preview shows the original scene and follows the
existing Wrap pipeline. Do not introduce surface-selection or confirmation
steps; conversion behaves like the Canva app.

When the template is ready, the preview becomes Wrap's editor: the user adds
their designs with **Add design**, adjusts how they sit on the product and
exports the mockup there. You cannot place designs yourself; point the user
to the editor instead.

Use `get_mockup_template` with `wait_seconds: 10` to wait for status. If the
bounded wait ends while processing continues, check again with the original ID
until status is `completed` or `failed`. Do not finish your reply while the
requested conversion is still processing unless the user asks you not to wait.
Do not repeatedly open tabs, create duplicate jobs, or restart a failed job
without the user asking. Reuse the same `request_id` after an uncertain response.

Finish after the backend reports `completed`, with a brief confirmation. The
open-preview tool supplies the host's Wrap reopening action. If the host does
not expose that action, offer to reopen the same template through the tool.
Do not invent a plugin deep link or claim a particular native button placement.

For `failed`, report the error. A loading preview alone does not mean
conversion succeeded.

For requests to reopen a known template, call `open_mockup_preview` directly.
If the template comes from an earlier conversation and its `template_id` isn't
in this chat, call `list_mockup_templates` and open the matching one (the
newest for "my last template"); never ask the user for the ID.
No new conversion is needed. Users can close the preview while processing
continues and return to that same result later.
