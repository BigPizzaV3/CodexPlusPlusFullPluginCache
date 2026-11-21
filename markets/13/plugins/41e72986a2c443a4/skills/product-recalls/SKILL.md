---
name: product-recalls
description: Check inventory against live consumer-product recalls by UPC, model or product words, search recall records, read full recall details, and download XLSX and CSV screening files.
---

Use `check_inventory_for_recalls` for a stock list of 1–100 items. Pass each product name and any brand, model or UPC supplied. Use the user's announcement start year, or omit it for the last 15 calendar years. Keep duplicate items in input order.

Use `search_recalls` for product recalls, a recall list or consumer product recall search. Pass keywords, an optional field and inclusive YYYY-MM-DD dates. A date range can touch at most 15 calendar years from 2000 onward. Without dates, it searches the last 365 days through today UTC. The preview has up to 20 rows; XLSX and CSV files contain up to the newest 2,000 matches.

Use `get_recall_details` for one to ten recall numbers. Report missing numbers separately. Full records include hazard, remedy, consumer contact, retailers, units, UPCs and image URLs.

Report status counts, identifier or word-match reasons, failed-year warnings, the source retrieval time and download links. Files expire in about an hour. Word matches require verification against the recall page and product label. Models written with spaces and differently described products can be missed. A no-match result does not establish absence of a recall. Include the returned coverage statement. This is a screening aid, not legal advice; food, drug and vehicle recall databases are outside coverage.
