---
name: fed-register
description: Search Federal Register documents by watches or look up document numbers, with agency grouping, comment and effective dates, and XLSX, calendar and CSV downloads.
---

# Zovo Federal Register Digest

Use `find_federal_register_documents` for federal register search, federal register this week, new federal regulations this week, proposed rules comment deadline, federal register notices by agency, or tracking proposed rules. Supply one to five watches combining terms, agency names or abbreviations, and CFR title/part. An empty watch searches the entire window. Default types are rules and proposed rules. Publication defaults to the last seven calendar days in America/New_York; comment-close and effective windows default to today through thirty days ahead. Publication windows cover at most ninety-three days; other windows at most three hundred sixty-six days. Published documents start in 1994.

Use `show_federal_register_documents` when the user supplies one to fifty document numbers. Pass the numbers as an array. Invalid and missing numbers are reported per item; successful documents still produce files.

Report the window, watch counts and truncation, type totals, nearest comment deadlines, per-item errors, source retrieval time, and the XLSX, ICS and CSV links. Links expire in about an hour. Each watch includes the newest five hundred matches, and a combined digest includes at most fifteen hundred unique documents. Downloads group by type and agency; the widget filters and sorts the retrieved rows without another request. Negative days mean the comment period is closed. The calendar omits past dates.

Dates reflect those published by the API; extensions and corrections can appear separately. This is a research aid, not legal advice. Do not use for state registers, unpublished guidance, or docket submissions.
