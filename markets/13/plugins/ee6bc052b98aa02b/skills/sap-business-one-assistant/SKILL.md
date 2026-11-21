---
name: sap-business-one-assistant
description: Connect to Sap Business One and work with authorized SAP Business One companies, business questions, reports, supported documents and actions. Use for onboarding or a user request involving their connected SAP company; not for unrelated general questions.
---

Use the bundled SOL MCP connection. An existing SOL account and organizational access are required. If authentication is missing, use the host connection flow. Never ask the user to put a password, API key or access token in the conversation.

## Connect and select a company

For onboarding, briefly explain the connection, call `sol_list_databases`, and help the user choose an authorized company. Use a returned `database_id` with `sol_start_conversation`; do not construct identifiers or choose an unrequested default. If the list is empty, relay SOL's notice and direct the user to their administrator or the [SOL support page](https://sol.inspiria.co.il/support). Installation does not grant company access.

Keep each returned `conversation_id` scoped to this host conversation, signed-in user and selected company. A company switch needs a conversation for that company. Do not reuse another user's or another host conversation's identifiers.

## Run a business request

Choose the matching operation from the tools already published by the SOL server. Each operation has a fixed purpose and execution boundary. SOL manages its shared training, query/action construction, permissions and validations. Do not generate SQL, Service Layer payloads, arbitrary endpoints or a hidden execution plan yourself. Send only the user's request for the selected operation, with a brief resolved business reference if needed; never forward the full host chat.

- Use `sol_query_erp` for authorized company data, reports and short follow-ups. It cannot change SAP, generate files, send messages or create schedules.
- Use `sol_answer_question` for SAP/product and approved company-training knowledge questions that do not require reading live company data.
- Use `sol_generate_file` with `format=pdf` or `format=xlsx` for a report file. Use `sol_export_sap_document` for the official PDF of an existing SAP document. Neither creates a new SAP document or sends a file.
- For SAP writes, select the published tool matching the exact entity and action. For example, `sol_create_sales_invoice`, `sol_create_sales_order`, `sol_create_purchase_order`, `sol_create_item`, `sol_update_business_partner`, `sol_update_exchange_rate` and `sol_cancel_sales_invoice` each allow only that named operation. Other supported entities and verbs are exposed upfront in the tool list. Do not substitute an unrelated tool for an unexposed operation.
- Use `sol_repair_missing_exchange_rates` only for an existing pending missing-rate repair in the selected company. Relay the user's manual/automatic choice and values. It can create/update and verify the missing rates using the shared SAP/Bank of Israel mechanism, but cannot resume an invoice or other original mutation. After confirmed repair, continue the original request through its own published operation and existing business reference; do not replace an uncertain creation with a fresh duplicate request.
- Use `sol_attach_sap_file` to attach an existing authorized file to an existing SAP document.
- Use `sol_send_email` for an explicitly authorized email with optional existing authorized artifacts. The system sender and connected personal sender remain subject to SOL's existing sender/recipient rules. Use `sol_create_calendar_event` for a requested calendar event, and `sol_write_integration_file` for saving an existing artifact to an authorized file integration. These are separate operations; they cannot generate files or change SAP.
- Use `sol_create_schedule`, `sol_update_schedule` or `sol_cancel_schedule` for the corresponding recurring-report task operation. Updating/cancelling requires the real `task_id`. These do not immediately send a report or schedule SAP mutations. Do not invent an ID when it is unavailable.
- Use `sol_generate_chart` only when a chart is requested. The configured external renderer receives the chart values; do not silently select this operation to satisfy a text-only question.

Split a compound request into visible calls: create an invoice with its entity-specific tool, export that confirmed invoice with `sol_export_sap_document`, then send its existing artifact through `sol_send_email` if requested. Use a distinct stable `message_id` for each operation call. Never bundle later steps into an earlier tool's free-text argument to bypass its boundary.

Keep the company, document identity, net/gross and VAT basis, requested currency and period when forwarding follow-ups such as “and in 2025?” or “and in euros?”. Preserve the user's language and stated form of address. A document number is an identifier, not a money value; do not add thousands separators.

Use one stable `message_id` for each submitted operation call. The ID is bound to the operation, its parameters and message. After a timeout or RUNNING result, check `sol_get_request` with that original ID. Do not change tools or parameters under an existing ID and do not create a new ID to replay an uncertain action. If its outcome remains unknown, explain that state instead of claiming completion or retrying a write.

SOL may ask a question, require confirmation, or return an access/license notice. Relay it accurately and send only the user's actual reply through the same operation in the same company conversation, using a new message ID for the new reply. Numeric choices remain replies to that operation and do not change language or form of address. A REPLIED transport status is not proof that the requested business action succeeded. Respect the user's existing authorization; never invent confirmations or switch delivery channels without it. A new step must have its own published tool and cannot inherit broader authority from an earlier workflow.

## Show generated files

When a verified reply supplies documents, relay the business result briefly, then call `sol_show_document` with the returned artifact identity. The card provides opening and downloading on supported clients. If the user reports a missing file, recover it with `sol_list_documents` and `sol_show_document` instead of repeating the export or SAP action.

An app card is not a native ChatGPT attachment. Do not invent URLs, local paths, host file IDs or claims about successful downloading, saving or delivery. A separate transfer is usable by other tools only when the host confirms a genuine file ID and the receiving tool supports it. Authorization to display a file is not authorization to email it.
