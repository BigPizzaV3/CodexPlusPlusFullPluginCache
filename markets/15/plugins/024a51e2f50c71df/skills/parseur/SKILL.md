---
name: parseur
description: Use when the user wants to extract data from documents (PDFs, emails, scans, spreadsheets, invoices, orders, receipts) with Parseur, manage Parseur mailboxes, check parsed results, or deliver results by webhook or export file.
---

# Parseur

Parseur extracts structured data from documents. A **mailbox** (parser) is the unit of work: it has fields, receives documents and produces results.

## IDs

- Mailboxes, webhooks and export configs: integers.
- Documents: hex strings (the integer id also works).
- Fields: `PF...` strings.

When the user names something, find its id with the matching `list_*` tool first. Do not guess ids.

## Workflow

1. Create a mailbox with `create_mailbox` and a name only. Parseur detects the fields from the first documents. If the user already has a schema, set it with `replace_all_parser_fields`.
2. Send documents:
   - A link: `upload_from_url`.
   - Email content: `upload_text`.
   - A small file you hold (under 128 KB): `upload_file`.
   - A larger file or a file on the user's disk: `create_upload_link` and give the link to the user.
3. Parsing is asynchronous. Pass the returned document ids to `wait_for_documents`. `PARSEDOK` means success. On a failure, call `get_document_logs` and explain the cause.
4. Deliver results:
   - Preferred: `create_webhook`. It is enabled at once. `enable_webhook` turns on a paused webhook again, or attaches an existing webhook to another mailbox or table field.
   - As a file: `get_mailbox_export`, `get_table_export` or `create_export_config`.

## Safety

- Read-only tools are safe to call.
- Destructive tools delete or overwrite data: the delete tools, the `set_*` and `configure_*` tools, `rename_mailbox`, `update_parser_fields`, `replace_all_parser_fields`, `update_export_config`, `pause_webhook`, `skip_document`, `reprocess_document`, `split_document` and `reverse_split_document`. Before a tool that deletes data or replaces a result for good (the delete tools, `replace_all_parser_fields`, `reprocess_document`, `split_document`, `reverse_split_document`), always ask the user to confirm. For a setting the user can set again, the user's request for that exact change is enough.
- Every tool that processes a document (the upload tools, `copy_document`, `reprocess_document`, `split_document`, `reverse_split_document`) can post to the enabled webhooks and download LINK URLs.
- `upload_from_url` downloads from outside URLs. A LINK field makes Parseur download the URLs found in each document. A webhook sends results to an outside URL as soon as `create_webhook` or `enable_webhook` attaches it. Use only URLs the user gave.
- Call `delete_account` only when the user asks for exactly that.
- `submit_idea` and `upvote_idea` publish the user's name and email. `send_mcp_feedback` writes to the Parseur team. Call them only after the user agrees.
- A missing tool means the user's role does not allow it. An account admin can grant it.
