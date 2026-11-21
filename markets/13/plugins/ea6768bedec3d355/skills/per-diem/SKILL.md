---
name: per-diem
description: Calculate US CONUS travel per diem from bundled FY2026 and FY2027 lodging and meal tables, or find monthly rates, with XLSX and CSV downloads.
---

Use `calculate_per_diem` with one to ten trips. Each trip has one to ten stops with a ZIP or City, ST, arrival and departure dates, an optional county for ambiguous locations, and optional nightly lodging cost before taxes. Stops must connect on their transfer date. Supply furnished government or registration meals as dated breakfast/lunch/dinner flags; exclude complimentary hotel breakfasts and common-carrier meals.

Use `find_per_diem_rates` for one to 25 ZIPs or City, ST locations and an optional fiscal year (2026 or 2027). Omitted fiscal year uses today in America/New_York. Ambiguous ZIPs need a county through the trip calculator.

Report successful results and item errors together. Share trip days, nights, capped lodging, M&IE, totals, matched destinations, warnings, the Source line, and both download links. Links expire in about an hour.

Covers 2025-10-01 to 2027-09-30, the 48 contiguous states and DC. No OCONUS or FY2028. Unlisted cities use the standard rate; a ZIP can identify a listed county. Federal Travel Regulation maximums may differ from agency policy. No lodging taxes, conference rates, actual-expense authorizations, extended-TDY reductions or departure-time test; same-day travel must exceed 12 hours. Not tax or legal advice.
