---
name: convert-to-markdown
description: Convert PDFs, images, or Office files to Markdown with Veryfi. Use when a user wants document text extracted, structure preserved, or page layout details returned.
---

# Convert documents to Markdown

Use the Veryfi MCP server to convert supported PDF, image, and Office files into Markdown.

## Workflow

1. Ask for the document or an accessible document URL if it was not provided.
2. Use the conversion tool with the uploaded document data or public file URL. For multiple public documents, use the batch URL input when supported.
3. Set a filename when known so the service can detect the format. Pass an optional document type only when it is clear from the user's request.
4. Request page details only when the user needs layout, page, or bounding-box information; otherwise return the Markdown text.
5. Present the returned Markdown directly or save it in the format and location the user requested. Preserve headings, lists, and tables from the conversion result.

Never claim that a document was converted until the tool returns a result. Do not expose credentials or ask the user to paste API secrets into chat; complete Veryfi sign-in through the host's authorization flow.
