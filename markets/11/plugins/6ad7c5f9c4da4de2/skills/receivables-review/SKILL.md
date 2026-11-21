---
name: receivables-review
description: Review unpaid or overdue customer Finance invoices and outstanding balances from HoreX. Use for receivables, customer debt and collection priorities, not supplier payables.
---

## State capability limits precisely

The plugin cannot edit, post, settle or mark Finance/Catering invoices paid, rewrite P&L, correct stock or recipes, send customer messages, make purchases or book travel. This remains true even when the user has evidence and native permissions. Offer analysis or the authorized native HoreX workflow, never promise that this plugin can perform those changes. Unsupported mutation requests require no business-data call. Supported Team tasks and advertising settings use only their dedicated proposal and native approval flows; they do not grant general editing or payment capabilities.

## Execute HoreX calls sequentially

For one connected HoreX account, wait for each call to finish before starting the next. Keep the result, source and billing status of each call separately. A busy/concurrency error applies only to the rejected call; it does not invalidate another successful result. Reuse successful results. Retry only the failed read once after the active call finishes, within the user's remaining successful-read budget. If no budget remains, report the partial result and ask before another charged read. Never broaden access or repeat a proposal/provider write to recover a read error.

First identify the source. get_receivables covers Finance invoices only; it does not summarize Catering debt. For Catering invoices or quotations use the catering-review workflow, list_catering_documents and get_catering_document. For an unspecified customer invoice search check both Finance and Catering before reporting no match. For combined customer debt state the Finance-only summary boundary and do not label it the complete HoreX balance.

For ambiguous customer documents, load get_horex_workflow with workflow catering-review: it contains the shared business map of Finance, Catering, supplier bills, B2B orders and POS-backed invoices. The user's explicit module choice and later corrections take priority over the conversation's previous source. Do not infer a module from food lines, customer name, invoice number or paid status alone. Read the free catalog's document_sources: denied or unavailable sources are not verified empty sources. Customer debt, invoice issued value, received cash, recognized revenue and conducted-event cost are different metrics.

Use get_receivables with scope unpaid for outstanding Finance balances or overdue for balances past the due date. Omit dates for the all-date visible balance. When dates are supplied, they filter invoice date; due date determines overdue status. Do not silently substitute a recent period for an all-time debt question.

Read summary.outstanding_value and matching_documents for the whole matching visible population. The records list is limited to 100; coverage.truncated and returned_rows state its completeness. It is ordered by invoice date, so the first records are not automatically the largest or most urgent debts. Owner-only visibility and permitted branches can constrain the summary; describe the returned coverage accurately.

Finance invoices are customer billing documents. Their issued value, recorded payments and outstanding amount differ from recognized revenue. Quotations are proposals, and supplier purchase invoices are payables; neither belongs in this receivables balance. Do not derive an all-time total from list_finance_invoices, which returns only recent matching documents.

Use get_finance_invoice to inspect a particular visible invoice when the user needs line detail. Preserve invoice number, customer/company, dates, total, paid and outstanding amounts. Do not invent contact details, bank information or payment links. Do not calculate full aging-bucket totals or per-customer rankings from a truncated list.

Present the visible balance and overdue coverage, then individual exceptions supported by the returned rows. Recommendations to follow up with customers are suggestions; the plugin does not send collection messages, alter payments, cancel invoices or mark debts settled.

Native output: widget view is paused. Combine returned facts into one normal answer using text and tables; keep requested comparison periods, coverage and exact source_links. Reading already returned facts is free. Reading another document, page or fresh analysis costs 1 AI Credit; reuse existing results when explaining them. The free open_restaurant_workspace tool returns workspace facts without opening a panel. For daily subscription setup load daily-review guidance.
