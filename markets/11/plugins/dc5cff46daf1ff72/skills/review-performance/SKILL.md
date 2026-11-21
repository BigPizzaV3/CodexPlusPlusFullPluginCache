---
name: review-performance
description: Explain ProductByte sales and social performance for a requested reporting period and suggest next actions. Use for ProductByte analytics and performance reviews.
---

Use the ProductByte MCP tools from this plugin. Tool names below are the server names; use the corresponding names exposed by the host.

- Resolve the project with `workspace-get` when it has not been selected. Ask which project to use when several are available. Read only the selected project's figures.
- Translate the requested period into calendar dates and pass the customer's IANA timezone when known. For a review without a period, use the tool's current-month defaults and state the returned range.
- Use `insights-get` for sales and social figures. Call `insights-show` when the customer asks to see the performance card, and let it present the figures.
- Base conclusions on the returned reporting range and collection status. Missing metrics, absent days or an absent shop result mean figures are unavailable, not zero sales or poor performance.
- Treat gauge values as snapshots, not values to sum across days. Use returned range totals for daily metrics and shop sales. Preserve currency and identify ranges with no single currency.
- Compare equivalent periods and compatible metrics when the customer requests a comparison. Distinguish observed changes from possible explanations; do not claim that posts caused sales without supporting data.
- Give a concise assessment and practical next actions tied to the observed figures. A performance review does not itself authorize campaign changes or publishing.
