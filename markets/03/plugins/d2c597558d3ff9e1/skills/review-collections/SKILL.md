---
name: review-collections
description: Review LeftLane deal finance accounts and aggregate collections, accounts-receivable, and delinquency reports. Use when a user asks about BHPH accounts, balances, days past due, promises, collections performance, AR snapshots, delinquency trends, or related filtering and pagination.
---

# Review Collections

Choose the narrowest read tool that answers the request:

- Use `DealFinanceAccounts` for account-level filtering, sorting, and pagination. State the page size, offset, and total count; continue paging only as needed.
- Use `CollectionsReport` for collected totals by balance type and effective date.
- Use `AccountsReceivableReport` for daily aggregate current-balance snapshots.
- Use `DelinquencyReport` for daily delinquent versus total open-account counts.

Use `yyyy-MM-ddT00:00:00` date values for report boundaries. Distinguish account facts from aggregate trends and call out incomplete pages. Treat results as decision support only: require a qualified human to review any credit, payment-plan, repossession, charge-off, or other adverse account decision. Never automate or present such a decision as made by the plugin.
