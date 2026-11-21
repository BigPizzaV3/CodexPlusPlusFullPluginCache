---
name: lei-lookup
description: Read public LEI status, renewal dates, company-name candidates and accounting parents, with dated XLSX and CSV downloads.
---
Use `verify_leis` for an LEI lookup, lei check or to verify lei numbers (1–100 LEIs). Supply `today` as YYYY-MM-DD when a renewal check date is given; otherwise the tool uses the current UTC date. Invalid and duplicate inputs remain separate report rows.

Use `find_leis_by_name` to find LEI by company name (1–25 registered names, optional two-letter legal-address country). Show the ranked candidates and match notes. Select a result only when the tool returns `single match` and a selected LEI; the user chooses between multiple candidates.

Use `get_lei_parents` for the direct and ultimate reported accounting-consolidation parent of 1–10 LEIs. Preserve reporting-exception reasons. These are not a full ownership chart.

Include summary counts, publication and retrieval times, per-item errors and both download links. Links expire in about an hour. Data is the golden copy at the shown publication time; later changes can wait for another publication. Legal forms are ELF codes. Treat this as a data check, not legal or regulatory advice. Do not request credentials or private account data.
