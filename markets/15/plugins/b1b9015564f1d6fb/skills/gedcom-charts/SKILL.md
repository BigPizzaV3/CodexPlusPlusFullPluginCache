---
name: gedcom-charts
description: Make a printable pedigree (ancestor) chart PDF of 4 to 6 generations and an Excel workbook from a GEDCOM (.ged) family tree file with generate_pedigree_chart, or convert a GEDCOM file to Excel and list data errors with convert_gedcom_to_excel.
---

# Zovo Pedigree Charts

Use these tools only when the user has a GEDCOM file (attached .ged, a .zip with a .ged inside, or GEDCOM text pasted into the chat).

1. Pass an attached file as `file`. Pass pasted GEDCOM text as `gedcom_text`, unchanged (line breaks may be lost; the tool restores them).
2. `generate_pedigree_chart`: set `person` to the name the user gives (add the birth year if they mention it) or a GEDCOM ID such as `@I12@`. Leave `person` empty when the user does not say whose chart it is: the tool picks the person with the most known ancestors and says so. `generations` is 4 to 6 (default 5). `page_size` is `Letter` (default) or `A4`.
3. If the tool answers that several people match the name, show the list and ask the user which one; then call again with that ID. Do not guess.
4. `convert_gedcom_to_excel`: for "GEDCOM to Excel", "list everyone in my tree", or "check my GEDCOM for errors".
5. After a result, give the chart person, ancestors known (for example 13 of 30), the data checks in plain words, any line that goes further back (offer a new chart from that ancestor), and the download links. The links expire in about 1 hour.

Do not use these tools for a family tree described in words with no GEDCOM file, for researching ancestors or records, or for organisation charts. Never invent people, dates or places.
