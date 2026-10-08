---
name: upload-document
description: Create or edit a Jotform form from an uploaded PDF, DOCX, or supported image by calling create_form or edit_form with document_file. Use whenever the user attaches a document or image that should become, update, or serve as the basis of a form.
---

# Upload Document

When the current user message includes a supported file for form creation or form editing, call the matching tool in that same turn. Include `document_file` so ChatGPT attaches the structured file payload through `openai/fileParams`.

Do not inspect, transcribe, summarize, or analyze the file with another tool first. Do not ask the user to restate information contained in the file.

## Create a form

Call `create_form` when there is no existing form to change.

- Put a short user-stated goal in `description`, or pass `null` when the upload alone defines the form.
- Default to `workspace_type: "personal"` and `team_id: ""` unless the user requests a team workspace.
- If the user names a team, call `get_teams` only to resolve its numeric ID, then call `create_form` with `workspace_type: "team"` and that ID.

If no file is attached, use the normal text-only `create_form` flow instead.

## Edit an existing form

Call `edit_form` when the user wants to change an existing form using the uploaded file. Include `form_id` and `document_file`.

- Put a short user-stated goal in `description`, or pass `null` when the upload alone defines the change.
- Do not call `create_form` for an existing form just because a file is attached.

If no file is attached, use the normal text-only `edit_form` flow instead.
