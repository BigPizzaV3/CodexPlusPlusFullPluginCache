# Current Gluon ERP tool routing

Reviewed against 46 tool descriptors exposed to this ChatGPT connection on 29 October 2026. Descriptors and schemas at invocation time take precedence over this inventory. This is metadata review, not evidence that calls passed. Six reporting tools were exposed; save_report_definition was absent in this connection at review time, although the implementation and publisher-provided scan describe it. Do not claim saving is available until the runtime exposes it.

## Routing rules

- Customer resolution: search_customers; use returned ledger detailAccountId where required. resolve_sales_filter handles other supported named sales filters.
- High-level sales: get_sales_summary. Invoice rows: get_customer_invoices/get_customer_sales_details; one invoice: get_customer_invoice_details. Trend/ranking/product analysis: use the corresponding specialized tools rather than collecting all detail rows unnecessarily.
- Customer balances: get_customer_account_summary or get_account_balance. Open receivable documents: get_customer_receivables. Aging with supported default buckets: get_customer_receivable_aging. list_receivable_aging_templates is needed for requested/custom templates or when the chosen endpoint requires selection, not for every balance question. get_outstanding_receivables retains its configured-template workflow.
- Collections/recovery: get_customer_collections. Statements: get_customer_statement. Activity: distinguish current Active/Inactive flags from purchase recency and historical latest dates in each descriptor.
- Orders/deliveries: select master list, detail, or fulfillment tool as appropriate. Current delivery/payment measures are not necessarily as-of values. Avoid double-counting invoice values repeated across linked deliveries.
- Inventory: get_inventory_summary for direct questions; use only discovered reporting adapters for saved inventory widgets.
- Saved reports and financial writes: follow SKILL.md's separate workflows. Read-only discovery/validation/preview never authorizes a financial write.

## Exposed tool descriptions

The following descriptions are taken from the connected tool catalog. Consult each runtime schema for exact fields, wrappers, enum values, and required arguments; do not infer support from another tool's schema.

### compare_customers

Compares two or more customers (detailAccountIds, at most 20) across business metrics for a period. Use it for questions like compare ABC with XYZ, which customer purchased more, or compare their sales and outstanding. Optional fromDate/toDate (inclusive; toDate is also the reference date for Overdue and DaysSinceLastPurchase, default today) and metrics (default NetSales, OrderCount, AverageOrderValue, Collections, Outstanding, Overdue, Returns). Metrics: NetSales (CurrencyRate x Quantity plus tax), GrossSales (Quantity x CurrencyTradePrice), Quantity, InvoiceCount (invoices), OrderCount (sales orders), AverageOrderValue (NetSales / OrderCount), CollectionAmount (receipts allocated to the invoices of the period), Outstanding (invoice net of the period minus those receipts), Overdue (overdue amount from the account summary as of toDate), ReturnAmount (sales returns incl. tax), ReturnPercent (ReturnAmount / NetSales x 100), GrossProfit (batch quantity x (CurrencyRate minus CostPrice)), DaysSinceLastPurchase (days since the latest approved purchase invoice booked against the account as vendor). Returns customers (in the order requested), each with customerId, detailAccountId, customerName and one camelCase field per requested metric (netSales, orderCount, averageOrderValue, collectionAmount, outstanding, overdue, returnAmount ...). Describe measurable differences rather than declaring a better customer.

### create_customer_receipt

Creates a customer receipt (money received from a customer) with its cash/bank receipt voucher (CRV/BRV) and, when the Receipt approval process is on for the tenant, an approval request, exactly as the Receipt screen does. TWO STEPS: (1) call with confirm=false (default) to get a preview (receipt number, voucher number, whether approval is needed) - nothing is saved; (2) show the preview to the user and, only after they explicitly confirm, call again with the SAME arguments and confirm=true. Always send a requestKey (a new GUID per receipt) so a retry never creates a duplicate. Required: companyId, currencyId (tenant base currency only), customerDetailAccountId, stationId, amount (>0), paymentType (Cash, Transfer or Draft; PDC unsupported), depositAccountId (a Cash account for Cash, a Bank account for Transfer/Draft). Optional: remarks, manualReceiptNo, costCenterId, instrumentNo (cheque/transfer/draft number, must be new), instrumentDate, lineComment, depositComment, bankNameId, employeeId and invoiceId (a pending invoice to settle; the amount may not exceed its remaining amount). Discount and tax are not supported yet. PDC is not a receipt: use create_pdc. The receipt date is today. Get ids from get_receipt_form_options and search_customers.

### create_expense

Creates an expense (money paid out for an expense account) with its EX voucher and, when the Expense approval process is on for the tenant, an approval request, exactly as the Expense screen does. TWO STEPS: (1) call with confirm=false (default) to get a preview (expense number, voucher number, whether approval is needed) - nothing is saved; (2) show the preview to the user and, only after they explicitly confirm, call again with the SAME arguments and confirm=true. Always send a requestKey (a new GUID per expense) so a retry never creates a duplicate. Required: companyId, currencyId (tenant base currency only), expenseAccountId (an Expense account), stationId, amount (>0), paymentType (Cash or Bank), payFromAccountId (a Cash account for Cash, a Bank account for Bank). Optional: remarks, manualRefNo. The expense date is today. Get ids from get_expense_form_options.

### create_pdc

Creates a PDC (post-dated cheque received from a customer) and keeps it in a locker (PDC in hand), exactly as the PDC In Hand screen does. A PDC is NOT a receipt: no receipt or voucher is created, and no discount or tax is saved. TWO STEPS: (1) call with confirm=false (default) to get a preview (PDC number) - nothing is saved; (2) show the preview to the user and, only after they explicitly confirm, call again with the SAME arguments and confirm=true. Always send a requestKey (a new GUID per PDC) so a retry never creates a duplicate. Required: companyId, currencyId (tenant base currency only), customerDetailAccountId, stationId, bankNameId, lockerId, chequeType (CrossCheque, Guarentee, Open, Cash or Other), chequeNo (max 20 characters). Optional: chequeDate, amount, signatory (max 50), costCenterId, remarks. Get ids from get_pdc_form_options.

### discover_report_capabilities

Discover authorized sources and exact filters/fields/charts before authoring.

### execute_saved_report

Execute a saved report as the caller; recheck current data permissions and sharing. Routine UI refresh does not need this tool.

### get_account_balance

Returns the Gluon ERP balance of a customer, vendor, cash, bank or other detail account.

### get_current_tenant

Returns the currently authenticated Gluon ERP tenant context.

### get_current_user

Returns the currently authenticated Gluon ERP user context.

### get_customer_account_summary

Returns a customer's financial position from approved ledger vouchers, using the same sources and formulas as the Sale and Recovery report. Pass customerId/detailAccountId (or customerName) for one customer; pass no customer to get every customer of the tenant (totals plus a customers list with each customer's figures). Optional fromDate/toDate; balances are as of toDate (default today). Fields: openingBalance (balance before fromDate; 0 when fromDate is omitted), sales, salesQuantity, salesReturns, salesReturnQuantity, collections (= cashReceipt + bankReceipt), cashReceipt, bankReceipt, otherDebit, otherCredit, adjustments (= otherDebit - otherCredit), currentBalance (balance as of toDate). totalOutstanding is the receivable (currentBalance when positive, else 0). overdueAmount is the part of the outstanding balance, attributed to the newest invoices first, that is past its invoice due date, plus any older brought-forward balance; notDueAmount = totalOutstanding - overdueAmount. lastInvoice {date, quantity, amount} and lastCollection {date, amount} are the latest approved sale and receipt on or before toDate (null when none).

### get_customer_activity_status

Finds customers by account and purchase activity across many customers (or all customers of the tenant). Optional status: Active or Inactive (the customer account's Active flag); New (account created from fromDate, default the first day of the toDate month, to toDate); Reactivated (latest purchase followed a gap of at least inactivityDays); Dormant (no purchase for at least twice inactivityDays); NoRecentPurchase (no purchase for inactivityDays up to twice that); RecentPurchase (purchase within inactivityDays); NeverPurchased (no approved sale at all). Omit status to list every customer with both statuses. To find customers who have not purchased in N days, set inactivityDays to N and call NoRecentPurchase and Dormant (and NeverPurchased if wanted). Optional inactivityDays (default 60), toDate (as-of, default today), fromDate, salesPersonIds, areaIds, cityIds. Returns totalCount and customers with customerId (the customer record id), customerName, customerCode, salesPerson, lastPurchaseDate, daysSinceLastPurchase, salesLast90Days (approved sales invoice totals in the 90 days to toDate), activityStatus (account flag) and purchaseActivityStatus. Visit, route, region and channel data are not available.

### get_customer_activity_summary

Returns customer activity as of dateRange. All four latest dates search all history through that date, including activity older than 30 days. Only Last30Days totals use 30 calendar days ending on dateRange. Supply exactly one of detailAccountId/customerName. Invoice means purchase invoice, not sales invoice. Active/Inactive is the current account flag. Not a fully historical snapshot.

### get_customer_collections

Returns customer payment/recovery history: a summary (collectionCount, totalCollected, averageCollection) and the collections, newest first. Use it for questions like when a customer last paid, how much they paid this month, recovery history, or which invoices a collection settled. Pass detailAccountIds for specific customers; pass NO customer to get every customer of the tenant. Optional fromDate/toDate (inclusive) and paymentMethod (Cash, Bank or Other). A collection is an approved receipt (collectionType Receipt) or an approved cash/bank voucher that credits the customer and belongs to no receipt (collectionType Voucher). Each row has detailAccountId, customerName, collectionId, collectionNo, date, amount, paymentMethod, referenceNo, allocatedAmount, unallocatedAmount (the amount still available to adjust against invoices, as in the Invoice and Advance Adjustment screen) and allocatedInvoices (the invoices or vouchers a receipt settled directly: documentType, invoiceNo, allocatedAmount).

### get_customer_deliveries

Returns all matching delivery masters without pagination. Resolve names with search_customers and pass detailAccountIds (DetailAccounts.Id). Filters: DC date, orderIds, paymentStatus. Quantity is actual delivered quantity. amount, paidAmount and outstandingAmount are the full totals of distinct linked invoices, calculated as in get_customer_invoices. recoveredAmount is an alias for paidAmount. Shared invoice totals repeat on each linked delivery; do not sum delivery rows as unique receivables. Invoice links use DCDetailId. Missing order links do not prevent invoice valuation; missing invoice links return null amount/outstanding/status. A lone fromDate is an upper cutoff; dates filter deliveries, not payments.

### get_customer_delivery_status

Returns order fulfillment totals and pending delivery value. Resolve customer names with search_customers and pass detailAccountIds. No pagination. Cancelled orders are excluded. Closed orders retain actual quantities but have zero pending value. Delivery quantities use the reference order-status formula and may exceed ordered quantities. Date filters select order dates, not an as-of delivery snapshot. A lone fromDate is an upper cutoff.

### get_customer_invoice_details

Returns one invoice with items and collections for one invoiceId (SalesInfos.Id, as returned by get_customer_invoices) or exact invoiceNo. Both supplied must match; ambiguous invoiceNo requires invoiceId. invoice: gross (CurrencyTradePrice * Quantity), discount (gross minus amount), taxAmount, net (CurrencyRate * Quantity plus line taxes), paidAmount (sum of NewReceiptDetails.CurrencyGrossAmount by SaleInfoId), outstandingAmount, paymentStatus (Unpaid, Partially Paid, Paid). Same formulas as get_customer_invoices. items: one row per invoice line; lineTotal is gross for the invoiced quantity; orderedQuantity/deliveredQuantity/remainingQuantity belong to the linked sales-order line (null when the line has no order link) and are not limited to this invoice. collections: receipts allocated to this invoice, one row per receipt voucher. Missing invoice returns invoice=null, items=[], collections=[].

### get_customer_invoices

Returns summary and all matching invoices without pagination. Resolve customer names with search_customers and pass detailAccountIds (DetailAccounts.Id, never Customers.Id). Invoice amount is the previous sales net formula: CurrencyRate * Quantity plus line taxes. paidAmount sums NewReceiptDetails.CurrencyGrossAmount by SaleInfoId; outstandingAmount is amount minus paidAmount. Status is Unpaid, Partially Paid or Paid. Payments are current, not restricted to the invoice date range. A lone fromDate is an inclusive upper cutoff. overdueOnly requires outstanding > 0 and DueDate before the current SQL Server date.

### get_customer_order_details

Returns order and items for one orderId or exact orderNo. Both supplied must match; ambiguous orderNo requires orderId. Includes gross, line discount, net, ordered/delivered/remaining quantities. Missing order returns order=null and items=[]. Closed status does not imply full delivery.

### get_customer_order_status

Returns Gluon ERP customer sales order status including ordered, delivered, invoiced, returned and pending quantities.

### get_customer_orders

Returns summary and all customer order rows without pagination. Resolve customer names with search_customers and pass detailAccountIds (DetailAccounts.Id, never Customers.Id). Net amounts include detail taxes. Status is the master status with Close overriding IsClosed=true. Filters apply to OrderDate; delivery quantities are current, using the reference order-status formula. A lone fromDate is an upper cutoff.

### get_customer_product_sales

Returns totalSales and all matching products with quantity, net salesAmount, contribution percent, invoiceCount and lastPurchaseDate. Filters: account IDs, dates, product/category IDs; selectable sort. Net sales uses CurrencyRate * Quantity plus CurrencyTaxAmount. No pagination. Omitted filters include all matching tenant data. detailAccountIds are ledger IDs; never pass Customers.Id. A lone fromDate is an upper cutoff.

### get_customer_profile_details

Returns detailed Gluon ERP customer profile information.

### get_customer_rankings

Ranks the customers of the tenant by a business metric. Use it for top or bottom customers by sales, highest outstanding, most returns or highest collection. Required metric; optional fromDate/toDate (inclusive; toDate is also the reference date for Overdue and DaysSinceLastPurchase, default today), direction (Top or Bottom), cityIds, areaIds, productIds and limit (for example 10; omitted = every customer). productIds limits the sales, quantity, profit, order, invoice and return metrics to those products; it does not apply to Outstanding, Overdue or CollectionAmount. Metrics: NetSales (CurrencyRate x Quantity plus tax), GrossSales (Quantity x CurrencyTradePrice), Quantity, InvoiceCount (invoices), OrderCount (sales orders), AverageOrderValue (NetSales / OrderCount), CollectionAmount (receipts allocated to the invoices of the period), Outstanding (invoice net of the period minus those receipts), Overdue (overdue amount from the account summary as of toDate), ReturnAmount (sales returns incl. tax), ReturnPercent (ReturnAmount / NetSales x 100), GrossProfit (batch quantity x (CurrencyRate minus CostPrice)), DaysSinceLastPurchase (days since the latest approved purchase invoice booked against the account as vendor). Returns metric, total (the sum over all customers; overall average or percent for AverageOrderValue and ReturnPercent; null for DaysSinceLastPurchase) and rankings with rank, customerId (customer record id), detailAccountId, customerName, customerCode, value and contributionPercent (share of total; null for non-additive metrics).

### get_customer_receivable_aging

Returns outstanding receivables grouped into aging buckets plus totalOutstanding, using the same outstanding amounts as get_customer_receivables. Use it for questions like how old the receivables are or how much is overdue. Pass customerIds/customerId/customerName for specific customers; pass NO customer to get every customer of the tenant. Optional asOfDate (default today). Without agingTemplateId or agingTemplateName the default buckets are used: Current (not yet overdue, due today included), 1-30, 31-60, 61-90 and 90+ days overdue. With a template (see list_receivable_aging_templates) the buckets are that template's day ranges measured in days overdue, preceded by Current for documents not yet due; a bucket 'Outside template ranges' appears only if the template leaves a gap. Each bucket has label, fromDays, toDays (null when open ended) and amount; zero buckets are included. Bucket amounts add up to totalOutstanding unless template ranges overlap.

### get_customer_receivables

Returns the outstanding receivable documents (unpaid and partially paid invoices and customer debit vouchers) and their total, using the same rules as the Invoice Wise Receivables report. Use it for questions like what a customer still owes, which invoices are unpaid, or all outstanding documents. Pass customerIds/customerId/customerName for specific customers; pass NO customer to get every customer of the tenant (do not ask the user for a customer first). Optional asOfDate (default today). Each receivable has detailAccountId, customerName, documentType (Invoice or Voucher), invoiceNo, invoiceDate, dueDate, invoiceAmount, receivedAmount (receipts plus invoice adjustments and sales returns, never more than the invoice amount), outstandingAmount, daysOutstanding (asOfDate minus invoice date), daysOverdue (0 when not yet overdue) and status (Not Due, Due Today or Overdue). Only documents with more than 1 outstanding are listed. totalOutstanding is the sum of outstandingAmount.

### get_customer_sales_details

Returns totalCount, totalAmount and all matching invoice rows, including gross/net amounts and product/invoice/customer discounts. One row per invoice, not product line. Net amount is CurrencyRate * Quantity plus CurrencyTaxAmount. Filters: account IDs, dates, product/category IDs and exact documentNo. No pagination. Omitted filters include all matching tenant data. detailAccountIds are ledger IDs; never pass Customers.Id. A lone fromDate is an upper cutoff.

### get_customer_sales_returns

Returns summary and all matching sales returns without pagination. Resolve names with search_customers and pass detailAccountIds (DetailAccounts.Id). Filters: return date and productIds. Each return has returnId, returnNo, date, invoiceNo (original invoice(s) from the return lines' invoice links; comma-separated if several, null if unlinked), quantity and amount. Return amount is net: SalePrice * Quantity (or, when that is null or <= 0, Quantity * TradePrice minus DiscountAmount) plus line TaxAmount. productIds counts only matching return lines. summary: returnCount, returnQuantity, returnAmount (exactly the rows returned) and returnPercentOfSales = returnAmount / net sales * 100 over the same customers, dates and products, where net sales uses CurrencyRate * Quantity plus CurrencyTaxAmount as in get_customer_invoices; null when there are no sales. A lone fromDate is an upper cutoff.

### get_customer_sales_trend

Returns metric, groupBy, total, average, change percentages, trend points, highestPeriod and lowestPeriod. Filters: account IDs and dates. Metrics: NetSales, GrossSales, Quantity, InvoiceCount; groups: Day, Week, Month, Quarter, Year. Optional comparison to the preceding equal number of calendar days. No product/category filters. No pagination. Omitted filters include all matching tenant data. detailAccountIds are ledger IDs; never pass Customers.Id. A lone fromDate is an upper cutoff.

### get_customer_statement

Returns a ledger-style customer statement for a date range from approved ledger vouchers: customerName, openingBalance (before fromDate), totalDebit, totalCredit, closingBalance (opening + debit - credit) and all transactions in date order with date, documentNo, documentType, description, debit, credit and runningBalance. Pass customerId/detailAccountId (or customerName) for one customer; pass no customer to get every customer of the tenant (totals are summed, each transaction carries detailAccountId and customerName, runningBalance is per customer). fromDate defaults to 30 days before toDate and toDate to today. No pagination.

### get_customer_summary

Returns a compact Gluon ERP customer summary.

### get_expense_form_options

Lists the choices needed to create an expense: companies (companyId), currencies (currencyId) with baseCurrencyId, stations (stationId), expense accounts (accountId), Cash/Bank pay-from accounts (accountId, accountType) and payment types. Call it before create_expense to look up ids by name.

### get_inventory_summary

Returns compact Gluon ERP inventory totals and top products.

### get_outstanding_receivables

Returns Gluon ERP aging and outstanding receivable information.

### get_pdc_form_options

Lists the choices needed to create a PDC (post-dated cheque): companies (companyId), currencies (currencyId) with baseCurrencyId, stations (stationId), bank names (bankNameId), active lockers (lockerId), cost centers (costCenterId) and cheque types. Call it before create_pdc to look up ids by name. Use search_customers to find the customer detailAccountId.

### get_receipt_form_options

Lists the choices needed to create a customer receipt: companies (companyId), currencies (currencyId) with baseCurrencyId, stations (stationId), Cash/Bank deposit accounts (accountId, accountType) and payment types. Set includeBanks / includeEmployees / includeInvoices (invoices need companyId, currencyId, customerDetailAccountId) only when the user wants a bank, employee or invoice. Call it before create_customer_receipt to look up ids by name. Use search_customers to find the customer detailAccountId.

### get_recent_sales_invoices

Returns paged recent Gluon ERP sales invoices with PII minimization.

### get_sales_details

Returns paged Gluon ERP sales invoice and detail rows with optional filters, pagination and aggregate output.

### get_sales_summary

Returns compact Gluon ERP sales totals for a date range and optional sales filters.

### get_saved_report

Retrieve the authorized saved definition and its Angular viewer link.

### get_subscription_status

Returns the authenticated Gluon ERP tenant subscription status.

### list_receivable_aging_templates

Lists configured Gluon ERP receivable aging templates.

### list_saved_reports

List bounded metadata of caller-owned or shared reports.

### preview_report_definition

Preview at most 25 authorized rows for a ViewerDefinition; no save.

### resolve_sales_filter

Resolves Gluon ERP sales filter names such as customer, company, station, cost center, product, employee, manager or warehouse into tenant-safe IDs.

### search_customers

Primary customer resolution tool: use when the user provides a name/code without a verified ID. Supports title search, exact customer IDs/codes, salesperson IDs, city/area IDs or names and Active/InActive status. Filters combine with AND; list values with OR. Returns totalCount and all matching customers. Ask which customer when multiple matches exist. customerId means Customers.Id; use detailAccountId for ledger reports. Does not support region/territory/channel or salesperson-name filters.

### validate_report_definition

Validate a ViewerDefinition and current field permissions without querying rows or saving.

## Save tool awaiting exposure in this connection

save_report_definition creates a private report definition or updates an owned report with reportId and the latest concurrencyToken. It returns a viewer link. It requires reports.write and the AI Reports role permission. Because updates replace a saved definition, the server annotation must declare destructiveHint=true. Its presence and input type must be checked in the current runtime; this package cannot register a missing server tool or change its annotations.
