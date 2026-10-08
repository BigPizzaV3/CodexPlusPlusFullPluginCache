---
name: rosey-document-review
description: Use Rosey to independently review a document against supporting materials. Apply when the user asks Rosey to check, verify, pressure-test, or quality-assure a Word document, slide deck, PDF, or spreadsheet. Prefer original file uploads when available; otherwise continue with the best representation supported by Rosey's existing MCP tools and disclose the limitation to the user.
---

# Rosey Document Review

Use Rosey as an independent review layer. The candidate is the deliverable being reviewed. Supporting materials are the sources Rosey should use to verify it.

## Preserve primary content when possible

Give Rosey the complete original file bytes whenever the client can access them and Rosey's existing MCP tools provide a direct file-transfer path. A semantic equivalent is not a bit-for-bit equivalent, so do not replace an accessible original file with extracted or model-written content.

For a direct transfer:

- Transfer the file itself without opening and re-saving it.
- Use an attachment or file handle as a lossless path only when the available tool documentation says it resolves to the stored file.
- Mechanical transport encoding or chunking is acceptable when it reconstructs the identical ordered bytes.
- Preserve the complete file rather than selected pages, passages, cells, or slides.

## Continue when direct upload is unavailable

Do not abandon a Rosey review solely because the client cannot provide a direct file upload. Use only the inputs and operations already exposed by the Rosey MCP; do not invent new arguments, metadata fields, labels, artifact types, or tool calls.

When Rosey accepts document content through an existing non-file input, provide the highest-fidelity representation the client can obtain, in this order:

1. An official provider export of a native cloud document.
2. Complete deterministic extraction that preserves all accessible text, values, formulas, tables, notes, and structure.
3. OCR or complete rendered content.
4. Partial extraction, retrieved passages, or a summary when nothing more complete is available.

Never choose a lower-fidelity representation when a higher-fidelity option is accessible. Avoid LLM rewriting or summarization when export, deterministic extraction, or OCR is available.

If Rosey's existing MCP accepts neither a file nor any usable representation, explain the limitation rather than fabricating an unsupported request. This is the only transfer-related condition that prevents the call.

## Review workflow

1. Identify the candidate and all intended supporting materials from the user's request and the inputs available to the client.
2. For each input, attempt the original-file path first. If it is unavailable, use the best fallback that Rosey's existing MCP schema already accepts.
3. Preserve each source separately when the MCP permits it. Do not merge multiple supporting files into a model-created document unless the existing Rosey interface requires one combined input.
4. Call Rosey using its documented parameters exactly. Do not add provenance or fidelity fields that the MCP does not define.
5. Present Rosey's results. In the assistant's user-facing response, state whether Rosey received original files or fallback representations and identify material limitations of any fallback.

## Accuracy of disclosure

Keep transfer-quality descriptions outside the Rosey tool call unless the existing MCP schema already has an appropriate field.

Do not claim "bit-for-bit," "lossless," or "original file" when content was exported, extracted, recreated, summarized, or not verifiably transferred as the original file. When a fallback was used, briefly explain what was submitted and what may have been lost, such as layout, formulas, embedded objects, omitted passages, or exact wording.
