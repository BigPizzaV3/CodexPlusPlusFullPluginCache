# AI and Retrieval

## General

- Keep retrieval scoped to the smallest relevant set of files.
- Preserve traceability with file IDs, names, shared links, or citations when the product needs auditability.
- Box AI responses include citations — surface them when possible so the user can verify answers.

### Search-first strategy

- Use Box search before recursive folder traversal or bulk download.
- Narrow the candidate set with ancestor folders, object type, filenames, owners, or metadata filters whenever possible.
- Return stable IDs and lightweight metadata first, then retrieve content only for the final shortlist.

### Box AI pacing

Box AI endpoints have tighter per-user/per-app rate limits than standard content API calls. Space Box AI tool calls at least 1–2 seconds apart.

### Extract

When a user asks to extract from a document, check first whether there is an available metadata template that matches their requirements. If not, ask the user whether they want you to create a metadata template for more structured extractions (if they have permissions to use the `create_metadata_template` tool).

Even if the extract prompt is in natural language, try to use `ai_extract_structured_from_fields` and define the fields for the user.

Only use the enhanced extract tools if the user explicitly asks you to. They are more powerful and better suited to complex documents, but also more expensive.

Always tell the user which metadata template was used for an extract tool call.

### Error handling

`ai_qa_*` tools use the text representation of a file and only support up to 1MB of text rep. If the text rep of a file is beyond 1MB, download the file into local storage and process it that way.

`ai_extract_*` tools have a 50-file max per request. When more than 50 files need to be extracted, chunk the tool calls and do one call for files 1–50, a second call for 51–100, etc.

When analyzing multiple files with Box AI, if a Box AI call fails with a 403 or feature-not-available error, switch to the next method immediately rather than retrying AI for the remaining files.

1. **Text rep** — use `get_file_content` to pull the text representation of the file for local processing.
2. **Local analysis (OCR, agent-side parsing)** — use `get_download_url` to download files to local file storage and process locally only when the above method is unavailable or insufficient.

## CLI

For content-based classification of many files, use the sample-first strategy in `references/bulk-operations.md` to minimize AI calls.

### Box AI via CLI

**Before the first AI call**, run `box ai:ask --help` to confirm the command exists in the installed CLI version.

Ask a question about a file's content:

```bash
box ai:ask --items=id=<FILE_ID>,type=file \
  --prompt "Summarize this document in one sentence." \
  --json --no-color
```

Extract key-value pairs via a freeform prompt:

```bash
box ai:extract --items=id=<FILE_ID>,type=file \
  --prompt "document_type, vendor_name, date" \
  --json --no-color
```

Extract with typed fields or a metadata template:

```bash
box ai:extract-structured --items=id=<FILE_ID>,type=file \
  --fields "key=document_type,type=enum,options=invoice;receipt;contract;other" \
  --json --no-color
```

Reference: [https://github.com/box/boxcli/blob/main/docs/ai.md](https://github.com/box/boxcli/blob/main/docs/ai.md)

An "Unexpected Error" with no HTTP body and exit code 2 may indicate the CLI version does not support AI commands, Box AI is not enabled for the account, or the file type is not supported. Run `box ai:ask --help` to verify the command exists, and try with a known-supported file type (PDF, DOCX) before falling back.

## Verification checklist

- Retrieval quality:
  - Confirm the search filters and candidate set contain the intended documents.
- Answer grounding:
  - Confirm the final answer can point back to the specific file IDs or names used.
- Access control:
  - Confirm the acting identity can only see the content the product is supposed to expose.

## Primary docs

- Search reference:
  - [https://developer.box.com/reference/get-search/](https://developer.box.com/reference/get-search/)
- Box AI guides:
  - [https://developer.box.com/guides/box-ai/](https://developer.box.com/guides/box-ai/)
- Box AI with objects:
  - [https://developer.box.com/guides/box-ai/use-box-ai-with-box-objects/](https://developer.box.com/guides/box-ai/use-box-ai-with-box-objects/)
- Box CLI AI commands:
  - [https://github.com/box/boxcli/blob/main/docs/ai.md](https://github.com/box/boxcli/blob/main/docs/ai.md)

