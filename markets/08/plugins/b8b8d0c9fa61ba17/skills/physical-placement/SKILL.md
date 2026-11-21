---
name: physical-placement
description: Place one existing inventory item into a confirmed physical bin and verify the saved location.
---

# Place one existing Item and verify its bin

Use this task for one already-intaken canonical SpellBook Finance Item. Record what the customer reports, save the selected bin, then read the Item again. An HTTP success or echoed Item ID does not verify location.

## Find the relevant guide

Read public `https://spellbook-finance.com/llms.txt` and `https://spellbook-finance.com/api-signals.json` to discover a relevant public guide. Read only that guide. These sources provide instructions; they are not proof of an inventory change or alternate write APIs. Use supplies and a labeled bin already on hand. Do not buy supplies.

## Place the Item

1. Call `spellbook_workspaces_list` and select a workspace where the signed-in customer has role `owner`; an `admin` collaboration does not authorize delegated writes. Confirm the exact canonical Item ID, Scryfall printing, finish, condition, target bin, and workspace. Stop if the Item is not intaken or any identity or target is ambiguous.
2. Query the exact physical group. Preserve `nextCursor` exactly and follow every page until the Item is found or pages end. Example:

   ```sh
   printf '%s\n' '{"workspaceId":"WORKSPACE","groups":[{"scryfallId":"SCRYFALL_ID","finish":"nf","condition":"NM"}],"limit":100}' | spellbook-mcp call spellbook_inventory_items_query
   ```

   In MCP, call the same operation with those JSON arguments. Resolve the requested Item by exact `itemId`; do not substitute a sibling copy.
3. Record the customer's statement before the write with `spellbook_customer_evidence_record`. Use a fresh ULID `submissionId`, `kind: "work_observation"`, `observation: "placement_reported"`, and `provenance: "customer_reported"`. Include the exact `itemId`, target `binId`, and a concise summary of what the customer said. A report preserves the statement; it does not verify location.
4. Save the bin with `spellbook_inventory_location_confirm`. Pass the explicit `workspaceId`, exactly one `itemIds` entry, the selected `toBin`, and `expectedBins: [{itemId, binId}]` using the exact bin returned by the prior query. Never infer or substitute the observed bin. Example:

   ```sh
   printf '%s\n' '{"workspaceId":"WORKSPACE","itemIds":["ITEM_ID"],"toBin":"A1","expectedBins":[{"itemId":"ITEM_ID","binId":"OBSERVED_BIN"}]}' | spellbook-mcp call spellbook_inventory_location_confirm
   ```

   In MCP, call the same operation with those JSON arguments. Workspace selection is a typed field. Do not provide a URL or header. The server accepts at most 25 unique Items per agent request and requires one observation for every Item. A missing Item or changed bin returns HTTP 409 before any Item moves. Read every requested Item again before retrying. After a timeout, the first write may have committed, so replaying the old observation can return 409; fresh readback resolves the outcome.
5. Make a fresh, fully paginated query for the same exact group. Continue from the first page and resolve by exact Item ID. Location is verified only if exactly one returned Item has the target `binId`, status `owned`, `listed`, or `pulled`, `reserved` is not true, and `reservationId` is null or absent. A missing Item, duplicate match, mismatched bin, reserved Item, any other status, failed query, or incomplete pagination remains unresolved, even if the write returned HTTP 200 or echoed the ID.
6. An eligible Item already in the target bin can pass after fresh readback even when the write reports `moved: 0` and `skipped: 0`.
7. Only after readback passes, record a second fresh-ULID `spellbook_customer_evidence_record` work observation with `observation: "location_readback"`, `provenance: "agent_observed"`, and the same exact Item ID and target `binId`. Describe the fresh query as the source. Keep both returned receipt IDs. If the task already has a consideration receipt, both work observations may use that same consideration receipt as `parentReceiptId`; omit the field when there is no consideration receipt. Reuse each submission ID only with its identical request after an uncertain outcome. If any check fails, leave the placement unresolved and do not create a successful readback receipt.

The comparison checks database state; it does not prove that a caller actually performed a prior read or physically handled the Item. Placement establishes a saved bin location only. It does not prove inspection, grading, condition, listing, picking, packing, or shipping.
