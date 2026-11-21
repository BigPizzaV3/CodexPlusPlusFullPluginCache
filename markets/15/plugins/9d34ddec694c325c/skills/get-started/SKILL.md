---
name: get-started
description: Use when someone first connects MetricRaven or asks what it can do with their website analytics, traffic, revenue, goals or funnels.
---

# Get started with MetricRaven

MetricRaven is web analytics with revenue attribution. Every report is about websites the person approved when they connected.

1. Call `list_websites` to see which websites this connection can read. If there is only one, use it without asking.
2. For "show", "chart" or "visualize" requests about traffic or revenue over time, call `show_traffic_chart`. For ranked comparisons (channels, referrers, campaigns, pages, countries, devices), call `show_breakdown_chart`.
3. For numbers without a chart, use `get_traffic`, `get_breakdown`, `get_revenue`, `get_conversions` (goals and funnels; pass `funnel_id` for a saved funnel) or `get_realtime`. For revenue per goal property value (plan, experiment, placement…), use `get_goal`; `list_event_properties` lists the property names and values to filter by. For traffic from AI assistants, `get_ai_crawlers` with `view: "companies"` shows pages crawled, visits, paying customers and revenue per AI company. Whether slow pages cost sales: `get_page_speed` (needs Page speed on in the website's settings); `get_breakdown` with `include: "speed"` adds LCP and INP per page. Which pages buyers pass through before paying: `get_paths`. With Visitor details: who took a path (`get_path_visitors`), who dropped off a funnel step (`get_funnel_people`), revenue per customer trait (`get_visitor_traits`), one visitor's journey with session recording details (`get_visitor`), and raw rows (`list_events`, `list_payments`). For JavaScript errors that may block checkout, `get_errors` groups them by message with how many of those visitors didn't pay (by page with `path`, or at a funnel step with `drop_step`; `get_breakdown` with `include: "errors"` adds them per page).
4. Periods default to the last 30 days. Use `period` (`today`, `7d`, `30d`, `90d`, `1y`, `mtd`, `all`…) or `from` and `to` dates, and pass `timezone` when the person mentions one.
5. Revenue is credited to the visit that first brought each customer. Say so when comparing channels by revenue.

Tools that change things need the write permission: adding websites, chart notes and alerts, changing goal labels, and creating or updating funnels, segments and page or link goals (`list_goal_definitions` and `preview_goal_definition` show and test goals first). Explain the change and ask before calling them; an update replaces the saved definition. This connection can't delete anything or change the team, alert or bot settings: for that, send the person to the MetricRaven dashboard. Without Visitor details, `update_segment` needs both name and filters. If a tool reports a missing permission, tell the person to reconnect MetricRaven and allow it.

Suggested first questions:

- "Chart my visitors and revenue for the last 30 days."
- "Which channels brought the most revenue this month?"
- "Show my signup funnel and where visitors drop off."
- "Create a funnel from the pricing page to payment and show where buyers drop off."
- "Which customer role brings the most revenue?"
