---
name: export
description: "Download or export saved Chalkie lessons, quizzes, worksheets and booklets as PowerPoint, Word or PDF, or transfer them to Google Slides or Google Docs through an available import connector."
---

# Export a saved teaching resource

Use the saved resource from the conversation, or resolve its name with `search_resources`. Ask which resource only when the target is ambiguous. Do not recreate content to export it. This workflow is for teaching materials, not Live student answers, scores or participant data.

## Choose the file format

| Resource | Requested destination | `export_resource` format |
| --- | --- | --- |
| Lesson or quiz (`resource_type: lesson`) | PowerPoint / PPTX | `powerpoint` |
| Lesson or quiz | Google Slides | `powerpoint`, then import with a Google connector |
| Worksheet or booklet (`resource_type: document`) | Word / DOCX | `word` |
| Worksheet or booklet | Google Docs | `word`, then import with a Google connector |
| Either resource type | PDF | `pdf` |

Generation and media must finish first. Teacher-notes-only and whole-series exports are not supported. For an incompatible resource/destination pair, explain the supported options instead of silently changing the resource or format.

## Start and follow the export

1. Call `export_resource` with the saved `resource_type`, `resource_id` and format. Keep the returned `export_id`.
2. While status is `processing`, wait at least `retry_after_seconds` before calling `get_export`. Never start another export merely to check progress. Stop checking on completion, failure, any error, or after five minutes. If still processing, retain the ID for a later check. Status entries expire after 24 hours; an expired entry needs a new export.
3. For a file download, show a Markdown link using the exact completed `download_url`, labelled with the file format. Do not claim the file is ready before a completed result. Use the host's file transfer/download capabilities when file bytes are needed; the tool returns a URL and metadata, not the file bytes.

The preview card's Export control checks its own exports. Do not poll tools on its behalf or promise that a text-requested export will update the card.

## Transfer to Google Slides or Google Docs

When the teacher requests a Google destination, complete the transfer if the connected tools support it. Chalkie produces the Office file; the Google connector imports and converts it. Google formats are not values accepted by `export_resource`.

1. Discover the available Google tools and read their import instructions. A connected Google account alone does not prove upload/conversion is available. Check that the host can also transfer the exported file to the connector.
2. Export PPTX for Slides or DOCX for Docs using the flow above. Download the returned file to the host's supported local file or uploaded-file handle. Preserve the Office file. Do not send a download URL to a parameter that requires a local file, or put binary/base64 file content in chat.
3. Import with native Google conversion enabled. For connectors exposing `import_presentation`, use the PPTX as `source_file` with `upload_mode: "native_google_slides"`. For `import_document`, use the DOCX with `upload_mode: "native_google_docs"`. Tool names and parameters vary by host: use the actual discovered schema and the teacher's requested destination.
4. Verify the result is a native Google presentation (`application/vnd.google-apps.presentation`) or document (`application/vnd.google-apps.document`), rather than an Office file merely stored in Drive. Read it back with the connector to check the content. Inspect rendered output when layout fidelity matters; do not promise identical formatting without checking it.
5. Return the verified Google file link. If import fails, provide the completed Office download and explain that the Google transfer did not finish. If the outcome is uncertain, check for the created file before retrying the import.

If the Google connector, native conversion, or file transfer capability is unavailable, explain the specific missing step and offer the PPTX/DOCX download for manual import or ask the teacher to connect a compatible tool. Do not claim that Google export is categorically unsupported, or that a Google file exists before the connector confirms it. A request for a normal PPTX, DOCX or PDF download does not request a Google upload.
