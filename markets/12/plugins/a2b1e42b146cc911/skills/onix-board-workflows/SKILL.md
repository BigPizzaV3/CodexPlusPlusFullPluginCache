---
name: onix-board-workflows
description: Use when working with authorized Onix Board businesses, contacts, catalog records, tickets, tasks, sales, or content through the Onix Board MCP tools.
---

# Onix Board workflows

Use the connected Onix Board tools for information and actions supported by their current schemas. Tool discovery describes capabilities; it does not authorize every action.

## Select the business

If the user may belong to multiple businesses and no business is selected, use `board_businesses_list` to discover the available businesses. Resolve an ambiguous choice with the user. Carry the selected `business_key` on subsequent business-specific calls. Use only keys returned by tools or explicitly supplied by the user, and verify records belong to the selected business. A change of business never expands OAuth access.

## Read and summarize

Use filters and pagination supplied by the current tool schema. Explain empty results and access errors accurately. Distinguish returned facts from your interpretation. For cross-business sales, use `board_sales_summary` with `all_businesses=true` or an authorized explicit subset. Keep amounts separated by currency unless the user requests conversion and a stated conversion source is available. Include the applied period and relevant business context.

## Make requested changes

Read the current record before updating it. Stay within the user's requested scope and the tool's current contract. For `board_tickets_create`, generate one stable `operation_key` for each intended creation and reuse that same key with identical arguments on retries. Apply the same rule to other tools whose schemas require `operation_key`, including `create_social_post_draft`. Use the key format and length required by the current schema. Preserve the original request key; a returned operation reference is not a replacement for it. Do not retry non-idempotent creation blindly after an uncertain outcome.

Distinguish drafts, saved content, scheduled work, queued messages and completed delivery. `create_social_post_draft` creates a suggestion and does not publish it. Campaign review tools never grant human approval; respect the approval step in Board before an authorized send. A notification or delivery queued for later is not proof of delivery. Use the returned status to describe what actually happened.

## Respect access and limits

If a tool returns an OAuth challenge, request authorization for the required scopes before retrying. Never request passwords, access tokens or client secrets in chat. Permissions, modules and OAuth scopes all limit access. Do not work around denied access by switching business or guessing identifiers.

For an unsupported Board view or action, use `board_app_links_get` to obtain the relevant audited Board URL when that navigation would help the user. Present the link and explain which step remains in Board. Do not invent routes or claim to have opened a page or completed an action unless that actually happened. For requests wholly outside Onix Board capabilities, explain the limitation without unrelated tool calls.

## Processing and available capabilities

Processing may consume an existing quota even when the user supplies finished text or an image generated elsewhere. Follow the current tool description and response: article processing uses the existing article generation category, image processing uses the existing image generation category, and `create_social_post_draft` uses one existing monthly community-manager slot. Do not invent categories, prices, balances or charges for reads or references to existing files. Native generation already accounts for its quota; do not perform an extra processing operation merely to charge it again. Report insufficient quota and failed or partial results accurately.

The media library requires storage; optional AI recovery or generation capabilities depend on their own enabled modules and permissions. Use the capabilities actually returned for the selected business. Missing AI capabilities do not imply that ordinary storage is unavailable. Respect the prerequisites of every other tool; storage is not a universal substitute for them.

If an AI summary provides only category, percentage and resets_at, report those fields without reconstructing exact credits, tokens, limits or remaining units. For partial image operations, use their returned status and the supported resume operation when appropriate to finish the same request; do not start another generation merely to retrieve an existing result.

Use returned public resource keys and supported file-delivery URLs. Never reconstruct storage paths or internal identifiers. Private or pending files are not public downloads; preserve their access and readiness restrictions, and do not claim an attachment is viewable without a usable returned delivery mechanism.
