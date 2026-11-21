---
name: packing-checklist
description: Organize supplied packing items into a checkable list with unit totals, printable PDF, and CSV exports.
---

Call `generate_packing_checklist` for explicit supplied item names, quantities and optional categories, packed status, title, and paper size. Do not invent packing recommendations or provide travel or health advice. Same-name same-category duplicates merge case-insensitively and quantities sum. Mixed packed states reset the merged line to unchecked; a checked line means all units are packed. Checks remain in the widget session. Export current progress regenerates files with those checks. Explain PDF font substitutions and CSV formula protection when relevant. Split large lists to satisfy the 2,800-byte payload limit.
