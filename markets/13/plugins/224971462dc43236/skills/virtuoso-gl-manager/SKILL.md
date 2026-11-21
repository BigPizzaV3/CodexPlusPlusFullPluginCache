---
name: virtuoso-gl-manager
description: >
  Route financial reporting, AR aging, AP analytics, and lease management questions to Yardi
  Virtuoso GL and Lease Management MCP tools. Use this skill whenever someone asks about income
  statements, balance sheets, trial balances, cash flow, budget comparisons, budget vs actuals,
  AP analytics, expense distribution, AP aging, AR aging, tenant delinquency, collections,
  aging buckets, lease details, tenancy schedules, lease clauses, or rent rolls. Also trigger
  when the user mentions "P&L", "NOI", "financial statement", "budget", "aging report",
  "delinquency", "collections", "lease", "tenancy", or asks about revenue, expenses, or
  tenant balances. Even if the user doesn't use these exact terms — if they're asking about
  financial data, aging, or leases, use this skill. Do NOT use for KPIs (use AssetIQ),
  work orders (use Work Order Manager), or vendor lookups (use P2P Manager).
---

# Virtuoso GL Manager

This skill routes financial reporting, AR/AP analytics, and lease management questions to Yardi
Virtuoso's GL and Lease Management tools. These tools use **property HMY IDs** (integers like
`35`) — not property codes. Use `get_autocomplete` with `autoCompleteType: "property"` to
resolve property names to HMY IDs before calling any tool in this skill.

## Tool Catalog (8 tools)

### Entity Resolution

| Tool | When to use |
|------|------------|
| `vn_mcpframework_get_autocomplete` | **Call first for every query in this skill.** Resolves property, tenant, and account names to HMY IDs. Pass `autoCompleteType` (`"property"`, `"tenant"`, `"account"`) and `searchTerm`. The `id` field is the HMY ID. For example: `{"id": 35, "label": "resny02", "label2": "Empire Terrace, 2040 Rosedale Ave, Bronx, NY"}` — use `35` as the PropertyId. |

### Financial Reports

| Tool | When to use |
|------|------------|
| `gl_financialreportsmain_financial_report` | **Generates any standard financial report.** Set `ReportType` to: `"incomestatement"`, `"balancesheet"`, `"trialbalance"`, `"cashflowstatement"`, `"budgetcomp"`, or `"twelvemonthbudget"`. Required: `PropertyId` (int array from autocomplete), `BookId` ([1]=Accrual, [2]=Cash), `MonthFrom`, `MonthTo`. Set `type: "screen"` and boolean flags to `false`. |
| `gl_financialreports_budget_comparison` | Budget vs actuals comparison. Required: `PropertyId` (int array) or `PropCode` (string array), `BookId`, `MonthFrom`, `MonthTo`. Optional: `BudgetSource` (0=None, 1=GL, 2=AdvBudget, 3=Analysis), `TreeId`/`TreeCode` for account tree. |
| `gl_apanalytics_ap_analytics_report` | AP analytics. Set `ReportType` to `"ExpenseDistribution"` or `"Aging"`. Required: `PropertyId` (int array) or `PropertyCodes` (string array), `PeriodFrom`, `PeriodTo`. Aging reports also need `AgeAsOf`. |

**Critical date format for all financial tools:** `YYYY-MM-DDT00:00:00.000` (always 1st of month, e.g. `"2025-01-01T00:00:00.000"`).

### Accounts Receivable

| Tool | When to use |
|------|------------|
| `ar_aranalytics_get_aging_detail` | AR aging by tenant, charge code, property, owner, or invoice. Required: `propertyIds` (^-separated HMY IDs, e.g. `"3^35^36"`), `summarizeBy` (0=ByTenant, 1=ByChargeCode, 2=ByProperty, 3=ByOwner, 4=ByInvoice). Optional: `asOfDate` (YYYY-MM-DD), `agingbuckets` (1–12, default 5), `showUnits`, `dataFilter`, `columnsToInclude`/`columnsToExclude`. |

### Lease Management

| Tool | When to use |
|------|------------|
| `lm_leaseinfobyid_get_lease_info_by_id` | Full lease details for a specific tenant. Pass `id` (integer tenant/lease HMY ID from autocomplete). |
| `lm_tenancyschd_get_tenancy_schedule` | Tenancy schedule — who's leasing what, lease dates, rent amounts. Required: `PageNumber`, `PageSize`. Optional: `Property` (property code string), `Tenant` (tenant name), `AsOfDate`, and boolean flags: `ChargeSchedules`, `Amendments`, `Options`, `Proposals`, `PrimaryContact`, `Units`. |
| `lm_clauses_get_clauses` | Retrieve lease clauses. Pass `tenantId` for tenant-level clauses, or `amendmentId` + optional `libraryId` for amendment-specific clauses. |

## Routing Logic

**Step 0:** Always call `get_autocomplete` with `autoCompleteType: "property"` first to get HMY IDs. Never use `search_properties` — that's for AssetIQ only.

1. **Financial statement (P&L, balance sheet, trial balance, cash flow)?**
   - → `get_autocomplete` for property HMY IDs
   - → `financial_report` with `ReportType`, `PropertyId`, `BookId`, `MonthFrom`, `MonthTo`

2. **Budget vs actuals?**
   - → `get_autocomplete` for property HMY IDs
   - → `budget_comparison` with `PropertyId`, `BookId`, `MonthFrom`, `MonthTo`

3. **AP expense analysis or AP aging?**
   - → `get_autocomplete` for property HMY IDs
   - → `ap_analytics_report` with `ReportType` (`"ExpenseDistribution"` or `"Aging"`)

4. **Tenant delinquency or AR aging?**
   - → `get_autocomplete` for property HMY IDs
   - → `get_aging_detail` with `propertyIds` (^-separated HMY IDs) and `summarizeBy`

5. **Specific lease details?**
   - → `get_autocomplete` with `autoCompleteType: "tenant"` to get tenant HMY ID
   - → `get_lease_info_by_id` with the tenant HMY ID

6. **Tenancy schedule / rent roll?**
   - → `get_tenancy_schedule` with `PageNumber: 1`, `PageSize: 100`, and optional `Property` code

7. **Lease clauses?**
   - → `get_autocomplete` with `autoCompleteType: "tenant"` to get tenant HMY ID
   - → `get_clauses` with `tenantId`

## Workflow Recipes

### Financial Deep Dive
**Trigger**: "Show me the income statement for [property]" / "how are we tracking against budget?"
1. `get_autocomplete` with `autoCompleteType: "property"` and the property name → collect HMY IDs from the `id` field
2. For income statement: `financial_report` with `ReportType: "incomestatement"`, `PropertyId: [35, 36, ...]`, `BookId: [1]`, `MonthFrom`, `MonthTo`
3. For budget tracking: `budget_comparison` with same `PropertyId` array and date range
4. Present key line items: revenue, expenses, NOI, variance to budget

### Tenant Delinquency Review
**Trigger**: "Who owes us money?" / "show me the aging report for [property]"
1. `get_autocomplete` with `autoCompleteType: "property"` → get HMY IDs
2. `get_aging_detail` with `propertyIds` (^-separated HMY IDs, e.g. `"3^35"`), `summarizeBy: 0` (ByTenant)
3. Present aging buckets (current, 30, 60, 90, 120+ days) with totals
4. Flag tenants with balances over 60 days

### AP Expense Analysis
**Trigger**: "Where's our money going?" / "expense distribution for [property]"
1. `get_autocomplete` with `autoCompleteType: "property"` → get HMY IDs
2. `ap_analytics_report` with `ReportType: "ExpenseDistribution"`, `PropertyId: [<HMY_IDs>]`, `PeriodFrom`, `PeriodTo`
3. Present expense breakdown by account category

### Lease Expiry Review
**Trigger**: "What leases are coming up for renewal?" / "show me the tenancy schedule"
1. `get_tenancy_schedule` with `Property` (code), `PageNumber: 1`, `PageSize: 100`, `ChargeSchedules: true`
2. Filter/sort by lease end dates approaching
3. `get_lease_info_by_id` for detailed review of specific leases of interest
4. Highlight upcoming expirations and renewal options

## Common Pitfalls

- **Always use `get_autocomplete` for property HMY IDs, never `search_properties`.** `search_properties` returns property codes which financial tools cannot accept.
- **Date format for financial tools:** `YYYY-MM-DDT00:00:00.000` (always 1st of month). Missing the `T00:00:00.000` suffix causes errors.
- **AR aging date format is different:** `YYYY-MM-DD` (no time suffix).
- **AR aging `propertyIds` uses ^-separated strings** (e.g. `"3^35^36"`), not integer arrays.
- **`financial_report` has a massive schema but most fields should be ignored.** Use only: `ReportType`, `PropertyId`, `BookId`, `MonthFrom`, `MonthTo`, `type: "screen"`, and the boolean display flags (all `false`).
- **`budget_comparison` requires `BookId`** — [1]=Accrual, [2]=Cash. Omitting it causes errors.
- **AP analytics has two distinct report types:** `"ExpenseDistribution"` for spend breakdown, `"Aging"` for AP aging buckets (which additionally needs `AgeAsOf`).
- **Tenancy schedule pagination is required** — always pass `PageNumber` (start at 1) and `PageSize` (100 is a reasonable default).
- **`get_tenancy_schedule` uses a `Property` code string** (one of the few non-AssetIQ tools that does) — you can get this from autocomplete's `label` field.

## Presentation Guidelines

- **Lead with key metrics.** Revenue, NOI, net income for financial reports. Total delinquent balance for aging.
- **Show comparisons.** Budget vs actual variance, prior year comparison, aging bucket trends.
- **Flag red flags.** Budget overruns (>10% variance), high delinquency (60+ days), large AP aging balances.
- **Use accounting terminology naturally.** P&L, trial balance, accrual, cash basis, charge code, aging bucket, NOI.
- **Cite Yardi Virtuoso as the data source.**
