---
name: financial-review
description: Review a week, month or explicit period of Fina spending and received income, explain changes and highlight relevant pending items. Use for financial check-ins or period comparisons; answer a single balance lookup directly with Fina tools without launching a full review.
---

# Financial review

Read [Fina's shared workflow](references/fina-core.md) and [financial facts](references/financial-facts.md). Check or reuse setup first and resume prerequisites if needed. Lead with what changed and why it matters, not a dump of account data.

1. Reuse the requested dates, currency basis and account scope. Otherwise use this calendar month to date in the saved timezone and state the period. Use equal comparable windows for comparisons; do not compare a partial current month against a full previous month without saying so.
2. Read `summarize_spending` for spending and, when relevant, received income with the same inclusive `from` and exclusive `to`. For original-currency groups use `basis=original` without `currency`. For today/yesterday use `days_ago` without explicit dates. Categories must come from that same report, not a budget or another period.
3. Retrieve only useful supporting transactions with `search_transactions(detail=summary)` and bounded filters. A page or `page_totals` is not the full-period aggregate. Follow cursors only as needed; preserve uncategorized purchases and distinct equal-amount transactions.
4. For an account overview use `list_accounts(detail=summary)`. If the user also wants next steps about spending, debt or saving, read `get_financial_context(detail=summary)` for the decision horizon before giving an affordability judgment. Use `list_commitments` and dated card obligations when relevant rather than assuming every repeated purchase is a subscription.
5. Explain the largest supported changes, distinguish received versus expected income, and surface relevant pending review items with their effect on totals. Do not call a pattern unusual without a comparison basis. Do not mark gaps as zero or resolve candidates without consent.

Keep the answer small: result, two or three supported observations, and a useful next action if one follows from the data. Use the user's chosen format; create a file only if requested or helpful and supported by the host. A review request does not authorize imports, recurring tasks, saving goals or changing financial records.

If the user asks for a recurring review, read [refresh and scheduling](references/refresh-and-scheduling.md), create the real host schedule after settling cadence/timezone/destination, and report its actual status. On future runs resolve relative dates afresh. Never promise delivery through WhatsApp. For an updating dashboard use financial-dashboard so the same artifact is preserved.
