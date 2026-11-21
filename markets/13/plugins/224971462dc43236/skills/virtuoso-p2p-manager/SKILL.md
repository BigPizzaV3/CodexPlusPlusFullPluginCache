---
name: virtuoso-p2p-manager
description: >
  Route vendor and payables questions to Yardi Virtuoso Procure-to-Pay MCP tools.
  Use this skill whenever someone asks about vendors, vendor lists, vendor status, vendor
  categories, invoices, payables, bills, accounts payable, payment status, purchase orders,
  vendor spend, expense tracking by vendor, or any procure-to-pay data. Also trigger when
  the user mentions "vendor", "payable", "invoice", "bill", "AP", "accounts payable",
  "payment", "supplier", or asks about who they're paying or how much they owe. Even if
  the user doesn't use these exact terms — if they're asking about vendor management or
  invoice/payment tracking, use this skill. Do NOT use for financial reports (use GL Manager),
  work orders (use Work Order Manager), or KPIs (use AssetIQ).
---

# Virtuoso P2P Manager

This skill routes vendor management and payables questions to Yardi Virtuoso's Procure-to-Pay
tools. Payables tools use **HMY IDs** (integers) for property and vendor filters. Use
`get_autocomplete` to resolve names to HMY IDs before filtering.

## Tool Catalog (4 tools)

| Tool | When to use |
|------|------------|
| `p2p_vendormcp_get_vendors` | List or search vendors. Optional filters: `status` (`"active"`, `"inactive"`, `"all"`), `category`, `expenseType`, `vendorCode`, `maxResults` (default 1000), `includeTransactionInfo` (shows last transaction date/amount). |
| `p2p_payable_get_payables` | List payables/invoices. Required: `DateFrom`, `DateTo`. Optional: `PropertyIds` (int array), `VendorIds` (int array), `Status`, `BatchIds`, `PayableIds`, `PostMonthFrom`/`PostMonthTo`, `ItemsPerPage`, `StartIndex` for pagination. |
| `vn_mcpframework_get_autocomplete` | **Call first to resolve property/vendor names to HMY IDs.** Pass `autoCompleteType` (`"property"` or `"vendor"`) and `searchTerm`. The `id` field in results is the HMY ID. |
| `vn_mcpframework_list_autocomplete_types` | Discover available entity types for autocomplete. |

## Routing Logic

1. **User asks about a vendor list or vendor lookup?**
   - → `get_vendors` with optional filters (`status`, `category`, `expenseType`)
   - For a specific vendor by code → `get_vendors` with `vendorCode`

2. **User asks about invoices, payables, or bills?**
   - → `get_autocomplete` with `autoCompleteType: "property"` and/or `"vendor"` to get HMY IDs
   - → `get_payables` with `DateFrom`/`DateTo` and optional `PropertyIds`/`VendorIds`

3. **User asks about vendor spend or payment history?**
   - → `get_vendors` with `includeTransactionInfo: true` for last transaction overview
   - → `get_payables` filtered by `VendorIds` for detailed transaction list

## Workflow Recipes

### Vendor Directory
**Trigger**: "Show me our active vendors" / "list all vendors"
1. `get_vendors` with `status: "active"`, `includeTransactionInfo: true`
2. Present: vendor name, code, category, last transaction date/amount
3. Highlight vendors with no recent activity if relevant

### Vendor Spend Detail
**Trigger**: "How much are we paying [vendor]?" / "show me invoices from [vendor]"
1. `get_autocomplete` with `autoCompleteType: "vendor"` and vendor name → get HMY ID
2. `get_payables` with `VendorIds: [<HMY_ID>]`, `DateFrom`/`DateTo` for the period
3. Present: total spend, invoice count, individual invoice details

### Property Payables Review
**Trigger**: "Show me all payables for [property]" / "what invoices are pending?"
1. `get_autocomplete` with `autoCompleteType: "property"` and property name → get HMY ID
2. `get_payables` with `PropertyIds: [<HMY_ID>]`, `DateFrom`/`DateTo`
3. Present: total payable amount, vendor breakdown, status summary

### Vendor Category Analysis
**Trigger**: "Show me all our landscaping vendors" / "vendors by category"
1. `get_vendors` with `category` filter and `includeTransactionInfo: true`
2. Present: vendor list with spend data, sorted by category

## Common Pitfalls

- **`get_payables` requires `DateFrom` and `DateTo`** — always specify a date range.
- **`PropertyIds` and `VendorIds` in `get_payables` are integer arrays** (e.g. `[3, 35]`), not strings. Use `get_autocomplete` to get these HMY IDs.
- **Never use `search_properties` for P2P tools** — it returns property codes, not HMY IDs. Always use `get_autocomplete`.
- **`get_vendors` returns up to 1000 results by default.** Adjust `maxResults` for larger datasets.
- **`includeTransactionInfo: true` adds the last transaction date and amount** to vendor results — useful for spend overviews without pulling full payables.

## Presentation Guidelines

- **Lead with totals.** Total spend, total invoices, total vendors — then break down.
- **Group payables by vendor or property** depending on the question.
- **Flag large invoices or unusual amounts** proactively.
- **Use AP terminology naturally.** Invoice, payable, batch, post month, vendor code.
- **Cite Yardi Virtuoso as the data source.**
