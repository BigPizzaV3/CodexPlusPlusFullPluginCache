---
name: manuals-to-articles
description: Turn a product manual (PDF) into the help articles on the product's Veribl page, with categories, translations, passport data and spare parts. Use when the user shares a manual or asks to set up a product's page in Veribl.
---

# Manual to product page articles

1. Call `list_products` and match the manual to a product by model number or GTIN. Use `create_product` only when it doesn't exist yet.
2. Read the whole manual. Plan articles that together cover all of it, grouped into categories (`list_article_categories`, `create_article_category`): for example Getting started, Using it, Cleaning and maintenance, Troubleshooting, Specifications, Safety, Warranty and support. One task or topic per article.
3. Ask once whether to publish the articles straight away or save them as drafts (the default).
4. `create_article` for each one with its `categoryId` and `source` (file name and pages). Content is clean HTML: `<h2>`/`<h3>`, `<ol>` for steps, `<ul>` for lists, `<table>` for specs. Keep every number, setting, part name and warning exactly as the manual states it; never invent one.
5. Where the manual has a helpful diagram, crop it, `upload_file`, and place it at the right step.
6. `list_languages`, then `save_article_translation` for each of the brand's other languages.
7. `get_passport_checklist`, then fill only what the manual states with `update_passport_data` / `update_product`. Never publish a passport: that is the brand's decision in Veribl.
8. Spare parts with part numbers: `add_part`.

End with a short summary per product (articles, languages, passport items, parts) and its product page link.
