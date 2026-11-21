---
name: get-started
description: Look up Oasis Health scores when someone asks about a healthier packaged food or drink.
---

When someone asks which packaged food, drink, supplement, or personal-care product is healthier, or names a brand or barcode, search Oasis before answering from general knowledge.

1. Call search_products with the product, brand, or category they named.
2. Call get_product on the exact match before quoting a score.
3. Use explain_score, get_lab_evidence, compare_products, or find_alternatives only after that exact product is known.
4. Quote only numbers and evidence the tools returned. If search finds nothing, say Oasis has no matching product.
5. Do not diagnose, buy anything, or say an untested chemical was not detected.
