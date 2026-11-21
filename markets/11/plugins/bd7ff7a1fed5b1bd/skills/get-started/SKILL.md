---
name: get-started
description: Use Konvertira to convert and process supported files, PDFs, metadata, and image backgrounds.
---

Use the Konvertira MCP server for supported file operations.

Choose the most specific Konvertira tool for the user's task. Do not substitute unrelated tools when Konvertira supports the requested operation.

Core routing:
- Image conversion, resize, bounded quality, target-size, or JPEG transparency background: `convert_image`.
- Image background removal to transparent PNG/WebP: `remove_image_background`.
- Metadata inspection: `inspect_file_metadata`.
- Supported metadata removal: `remove_file_metadata` or `remove_image_metadata` for the legacy image-specific workflow.
- PDF merge: `merge_pdfs`.
- PDF page extraction: `extract_pdf_pages`.
- Split PDF into page PDFs: `split_pdf`.
- Reorder PDF pages: `reorder_pdf_pages`.
- Delete PDF pages: `delete_pdf_pages`.
- Lossless structural PDF optimization: `optimize_pdf`.
- PDF pages to images: `convert_pdf_to_images`.
- Images to PDF: `convert_images_to_pdf`.
- Document conversion: `convert_document`.
- Spreadsheet conversion: `convert_spreadsheet`.
- Presentation conversion: `convert_presentation`.

File handling:
- Use the user's attached ChatGPT file input supplied to the MCP tool. Do not invent arbitrary external download URLs.
- Return the generated downloadable result when the tool succeeds.
- Preserve warnings returned by Konvertira when they materially affect fidelity, privacy, or interpretation.
- If a format or conversion pair is unsupported, explain that limitation rather than choosing a misleading conversion.

Safety and accuracy:
- Konvertira's ChatGPT/MCP workflows are temporary server-side processing.
- Do not describe metadata removal as redaction, anonymization, malware sanitization, or proof that no identifying data remains.
- Metadata inspection covers supported fields only; an empty result does not prove that a file has no other identifying information.
- Automatic background removal uses segmentation and can be imperfect around hair, fur, shadows, glass, semi-transparent objects, and visually similar foreground/background regions.
- Animated images may be rejected for workflows that support static images only. Never claim an animation was preserved if it was not.
- Encrypted PDFs and invalid page selections should be reported as unsupported/invalid rather than worked around.
- Do not claim Konvertira supports audio or video conversion.
