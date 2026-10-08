---
name: flipbook-publishing
description: Publish and manage Heyzine flipbooks from attached documents or public URLs. Use when users ask to convert, list, inspect, brand, update, replace, or delete a flipbook.
---

# Publishing Heyzine flipbooks

Use this skill to turn supported documents into flipbooks and manage existing
flipbooks.

## Inputs and boundaries

- Accept an attached file object or a direct public document URL.
- Accept PDF, DOC, DOCX, PPT, PPTX, ODT, ODP, and RTF documents.
- Identify existing flipbooks by an id, public URL, short id, or an unambiguous
  title from `heyzine_list_flipbooks`.
- Never invent a file URL, attachment id, publication id, account plan, or
  conversion result.
- If the source is only a local path, ask the user to attach the file. If a
  title matches several flipbooks, show the candidates and ask which one.

## Convert a document

Choose the tool from the source:

- For a file attached or selected in the current conversation, call
  `heyzine_convert_attached_pdf`. Pass the current attachment object as `pdf`;
  it requires `download_url` and `file_id`, with `mime_type` and `file_name`
  when available. Do not reuse a signed URL from an earlier attachment. This
  call returns the finished flipbook and must not be polled.
- For a public URL, call `heyzine_convert_pdf_async`. While its state is
  `started`, call it again with the same URL at reasonable intervals. Stop when
  it returns `processed` or a tool error. Do not start another conversion with
  a changed URL as a polling workaround.
- Use blocking `heyzine_convert_pdf` only when the user needs one-call
  completion and the document is expected to finish within the client timeout.
  If it times out, check the same URL with `heyzine_convert_pdf_async`; do not
  assume the conversion failed.

Send only settings the user supplied or that the workflow resolved. When the
user asks to reuse branding, call `heyzine_list_flipbooks`, resolve the source
flipbook, and pass its id as `template`. Do not ask about a template when the
user did not request branding reuse.

Read [references/design-options.md](references/design-options.md) before setting
design or publication fields.

## Manage an existing flipbook

- Use `heyzine_list_flipbooks` with optional `offset` and `limit` to find
  candidates. Filter returned items only after retrieving them.
- Call `heyzine_flipbook_details` before an update when the current settings or
  URL matter.
- Call `heyzine_update_flipbook_design` with the target `id` and only the
  fields to change. Then call `heyzine_flipbook_details` to return the current
  URL and verify the result.
- Call `heyzine_replace_flipbook_pdf` only when the user explicitly asks to
  replace an existing source document. It requires a public document URL and
  is available only to eligible, support-enabled accounts. Preserve the target
  id; do not fall back to creating a separate flipbook without asking.
- `heyzine_delete_flipbook` is permanent. Before calling it, resolve and state
  the exact title and id, then obtain confirmation unless the user already
  confirmed that exact target. Never delete as an unrequested cleanup step.

Changing `url_path` or `url_domain` can break existing links. Confirm the exact
change before applying it when the flipbook may already be shared. If a paid
feature is rejected, report the server's plan message and stop; do not infer a
different subscription or silently remove the requested setting.

## Report the result

Lead with the live flipbook URL. Include the id and page count when returned,
plus any template or design choice applied. For a running async conversion,
report its id, URL, and current state without claiming it is finished.
