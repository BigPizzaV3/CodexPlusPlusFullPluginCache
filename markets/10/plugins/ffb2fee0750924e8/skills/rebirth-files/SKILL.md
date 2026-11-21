---
name: rebirth-files
description: Use Rebirth file tools only when the user explicitly asks to save, search for, or retrieve a specific user-selected file or artifact through the authenticated Rebirth connection.
---

# Rebirth Files

Use this Skill only for a file operation the user explicitly requested. A file operation does not authorize access to any other attachment, recalled content, prompt, memory, Journal data, credential, secret, local path, provider object, or unrelated file.

## Find an existing artifact

If the user describes a stored file but does not provide an exact Rebirth artifact ID, call `rebirth_search_files` with the smallest useful query and appropriate artifact-kind filter. Use only the returned metadata to identify a candidate. Ask the user to disambiguate when several candidates plausibly match.

## Retrieve

Call `rebirth_get_file` only with an exact artifact ID returned by Rebirth or explicitly supplied by the user. Report success only after Rebirth returns `status: retrieved`. Let the Rebirth UI/file transport render or download the artifact. Never request or place base64, a data URI, image bytes, archive bytes, or a provider credential into model-visible content.

## Save

Call `rebirth_store_file` only when the user explicitly identifies a current-chat upload or generated file and asks to save it. Pass only the short-lived ChatGPT HTTPS attachment reference accepted by the typed schema. Do not invent URLs, attachment IDs, provider identifiers, credentials, or filesystem paths. Do not retrieve arbitrary URLs and do not convert the file to base64.

Use a clear semantic name and artifact kind when known. Do not infer file contents from a filename alone. Report success only after Rebirth returns a successful result, and retain the returned artifact ID for later exact retrieval.

## Boundary

Each invocation is limited to the specific file operation requested in the current conversation. File tools do not authorize memory disclosure, messaging, social actions, device control, account changes, or bulk transfer. When user intent is ambiguous, ask which exact file and operation they want before calling a write or retrieval tool.
