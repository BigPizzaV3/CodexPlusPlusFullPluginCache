# SistaniGPT source index

Status: local test draft, version 0.1.0. This index is navigation metadata, not a religious source.

The corpus contains the five PDFs supplied by the owner, totaling 848 physical PDF pages. English Islamic Laws 2023 is missing. A Code of Practice for Muslims in the West is a separate work, not a replacement edition of Islamic Laws.

## Books

| ID | Supplied book | PDF pages | Navigation |
|---|---|---|---|
| `hajj` | Hajj Rituals | 150 | [Index](books/hajj/index.md) |
| `women` | Women's Religious Rules in Simple Language | 46 | [Index](books/women/index.md) |
| `worship` | Summary of the Rules of Worship | 73 | [Index](books/worship/index.md) |
| `jme` | Jurisprudence Made Easy | 268 | [Index](books/jme/index.md) |
| `west` | A Code of Practice for Muslims in the West | 311 | [Index](books/west/index.md) |

## Topic routing

These are suggested starting points, not a hierarchy of authority. Search other relevant books and read full conditions before answering.

| Subject | Starting references |
|---|---|
| Prayer, wudu, ghusl, tayammum, fasting, zakat, khums | [Worship](books/worship/index.md), then [Jurisprudence Made Easy](books/jme/index.md) |
| Hajj, umrah, ihram, tawaf, sa'y, proxy pilgrimage | [Hajj Rituals](books/hajj/index.md), then [Worship](books/worship/index.md) |
| Menstruation, istihada, nifas, related worship | [Women's Religious Rules](books/women/index.md), [Worship](books/worship/index.md), [Jurisprudence Made Easy](books/jme/index.md) |
| Inheritance, wills, transactions, marriage, divorce | [Jurisprudence Made Easy](books/jme/index.md), then [Muslims in the West](books/west/index.md) where relevant |
| Food, clothing, work, and practical issues in non-Muslim countries | [Muslims in the West](books/west/index.md), then [Jurisprudence Made Easy](books/jme/index.md) |
| A specified source number | Identify the book first; only Hajj Rule and Worship Issue labels are indexed as numbered rulings |
| Book comparison or an apparent conflict | Read both exact passages and [reading notes](reading-notes.md); do not invent precedence |

## How to navigate

Each book has a topic index and a complete list of linked 12-page blocks. Every block identifies physical PDF pages and links to previous and next blocks. Do not load the whole corpus into context. Use targeted reads, then follow the complete relevant passage and its cross-references.

The [source registry](source-registry.json) holds filenames, original SHA-256 hashes, page ranges, edition notes, selected image locations, and extraction warnings. It is metadata, not a ruling source. Its `sections` are navigation labels, not authoritative numbered sections.

For exact citations, preserve the source's book title, Rule/Issue label where present, otherwise its actual heading or question, and the physical PDF page. This pack does not invent an online URL for every paragraph.

## Known limitations

The corpus is a mechanical extraction, not a fully reviewed transcription. Some Arabic, numeral order, source spacing, and image-only content need visual inspection. Selected source-page images are linked where available. Full original PDFs are in the outer developer kit, not in this installable skill. Read [reading notes](reading-notes.md) before interpreting a corrupted span or visual dependency.
