---
name: get-started
description: How to answer questions about an organization's OasisLMS data with the OasisLMS Nexus tools, including which tool to choose, date ranges, filters, and pagination.
---

# Getting started with OasisLMS Nexus

OasisLMS Nexus gives read-only access to the signed-in user's own OasisLMS organization. It can't create, change, or delete LMS data. If the user asks for a change (for example enrolling, deleting, or editing users or courses), explain that Nexus is read-only and that the change has to be made in OasisLMS itself.

## Choosing a tool

- **Totals, trends, and rankings:** use the `get_*_analytics` tools first. They return summary metrics, period series, and top lists without listing every record.
  - Users and registrations: `get_user_analytics`
  - Logins and traffic: `get_user_login_analytics`
  - Enrollments, progress, and completion: `get_user_progress_analytics`
  - Content engagement: `get_content_engagement_analytics`
  - Courses: `get_course_analytics`
  - Purchases and revenue: `get_course_purchase_analytics`
  - Credit claims: `get_user_credit_claim_analytics`
- **Specific records:** use the `search_*` tools, such as `search_users`, `search_courses`, `search_exams`, `search_user_progress`, and `search_course_purchases`.
- **Category filters:** before filtering on a category such as membership level, course type, or completion status, call `get_dimension_values` to get the exact labels used in this organization instead of guessing.

## Dates

- Analytics tools accept `DateFrom` and `DateTo` as `yyyy-MM-dd` or an RFC 3339 date-time. `DateFrom` is inclusive and `DateTo` is exclusive, so "March 2026" is `DateFrom=2026-03-01`, `DateTo=2026-04-01`.
- Convert relative phrases such as "last month" or "this year" into explicit dates.

## Large results

- To answer "how many" questions with a search tool, set `CountOnly=true`.
- Search tools return up to 200 records per call. Use `Limit` and `Offset` to page through more, and tell the user when a result was truncated.
- On analytics tools, use `Sections` to request only the parts you need.

## When data is unavailable

If a result has `IsAvailable` set to false, the organization's LMS doesn't have that data. Tell the user which data is missing instead of guessing.
