---
name: lead-performance-report
description: Use when the broker asks how their leads are going: number of enquiries, response time, conversion, sources/portals, lost reasons or most enquired boats.
---

1. Pick the period the broker asks for: 30, 90 or 365 days (default 30).
2. Call `get-lead-stats` with `days`.
3. Summarise: leads received compared with the previous period, median first response time and % answered within 24 h, won leads and conversion, the top sources, the main lost reasons and the most enquired boats.
4. Point out one or two concrete actions, for example slow responses or a portal that brings no leads. Use `search-leads` if the broker wants to see the leads behind a figure.
