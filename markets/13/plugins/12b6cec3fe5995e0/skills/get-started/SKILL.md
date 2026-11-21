---
name: get-started
description: How to use isGenAI to check text, links, images, saved prompts and C2PA Content Credentials for evidence of AI use, and how to read the results.
---

# Getting started with isGenAI

isGenAI reads the evidence of AI use that files and pages carry. Use it when someone asks whether an image, page, text or code was made with AI, what prompt was saved in an AI image, or what a file's Content Credentials say.

- **check_image**: an image by public URL or base64 (up to 20 MiB). Reads C2PA Content Credentials, IPTC AI labels, saved generation settings and metadata.
- **check_url**: a public page or file URL. Reads AI labels, AI-use statements, Content Credentials and saved records found there.
- **check_text**: pasted text or code. Finds statements of AI use and named AI tools and quotes the exact sentence.
- **extract_saved_prompt**: the prompt and settings saved by AUTOMATIC1111, ComfyUI, InvokeAI or NovelAI. It never reconstructs a prompt.
- **read_content_credentials**: the C2PA manifest, recorded actions and digital source type, with signature validation and signer trust reported separately.

## Reading results

Each result says what was found and where it came from. A missing AI signal does not prove a person made the content: screenshots and re-uploads often strip records, so ask for the original file when it matters. isGenAI does not give a verdict from how pixels look. When a public report URL is returned, share it so others can check the evidence.
