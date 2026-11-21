---
name: family-tree
description: Make printable family tree charts (all relatives, descendants, pedigree/ancestors, hourglass, fan) with PDF poster, SVG and GEDCOM downloads using generate_family_tree, and name how two relatives are related (cousins, removed, half, great-aunt, in-laws, step) with find_relationship.
---

# Zovo Family Tree

Use `generate_family_tree` when the user wants a family tree, genealogy chart, pedigree chart, fan chart or family tree poster/template. Use `find_relationship` when they ask how two relatives are related.

1. Turn the description into `people`: one entry per person with a short `id` (p1, p2 ...), the `name` as it should print, `born`/`died` (1950, 1950-03-12, or c. 1890), `sex`, `parents` (ids, at most 2) and `spouses` (ids, optional `married` year, `divorced: true`). Listing a marriage on one side is enough; parents who share a child are linked automatically.
2. Only include people and dates the user gave. Use "Unknown" for an unnamed person who is needed to link others (for example an unnamed mother). Do not invent dates. Leave `died` out for living people.
3. Mark `adopted: true` on adopted children and `twin: true` on twins without full birth dates.
4. Chart: leave `chart` out (all relatives) unless the user asks for descendants (`root` = the top person), an ancestor/pedigree chart or fan chart (`root` = the person whose ancestors are shown), or an hourglass. Pass `title` if the user names the poster and `paper` if they name a print size (letter, a4, a2, 18x24, 24x36).
5. After the tool returns, give the title and subtitle, any warnings verbatim, the recommended paper, and the PDF, SVG and GEDCOM links. The widget lets the user switch chart type and paper size.
6. For "how are we related?" call `find_relationship` with the same people list and the two people; report the relationship both ways and the common ancestors. Do not compute kinship terms yourself.

Do not use this skill for researching ancestors or records, DNA match estimates, company org charts, or flowcharts.
