---
name: naceneni-zakazky
description: Prepare and review a craft or construction quote using the connected Majster.ai account.
---

# Nacenění zakázky / Job quotation

## Česky

1. Přihlas uživatele k jeho účtu Majster.ai. Čti pouze jeho zakázky a údaje. Zjisti rozsah práce, rozměry, materiál, místo a měnu; chybějící podstatné údaje si vyžádej.
2. U existující nabídky nejprve zavolej `list_projects` a `get_quote` s přesným názvem, zákazníkem a verzí. Pro soukromé zobrazení použij `preview_quote`. Vlastní položky najdeš přes `get_price_list`, materiál nabídky přes `get_material_list`.
3. Před `create_quote` zjisti přes `get_credits` přesný dopad na stávající zůstatek. Shrň zadání a vyžádej si jasné potvrzení. Bez něj nic nevytvářej. Je-li výsledek ve zpracování, použij `poll_quote`, potom `list_projects` a `get_quote`.
4. Před `update_quote` přečti aktuální verzi a revizi. Ukaž přesně, co se změní, a požádej o potvrzení. Úprava vytvoří novou soukromou verzi. Při konfliktu načti nabídku znovu a vyžádej nové potvrzení.
5. Před `get_share_link` pojmenuj přesnou nabídku, zákazníka a verzi a vysvětli, že první volání zveřejní trvalý odkaz. Požádej o výslovné potvrzení. Odkaz neodesílá e-mail.
6. Položky s chybějící hodnotou nebo stavem `totals_status=incomplete` nejsou práce zdarma. Součet označ jako neúplný a neuváděj ho jako konečnou částku. Respektuj `needs_review` a `review_issues`.

## English

1. Connect the user's Majster.ai account. Read only their jobs and data. Confirm scope, dimensions, materials, location and currency; ask for missing essentials.
2. For an existing quote, call `list_projects` and `get_quote` with the exact title, customer and version. Use `preview_quote` for a private view. `get_price_list` reads the user's own catalogue; `get_material_list` reads quote materials.
3. Before `create_quote`, call `get_credits` to learn the exact effect on the existing balance. Summarize the brief and ask for explicit approval. Do not create before approval. If processing, use `poll_quote`, then `list_projects` and `get_quote`.
4. Before `update_quote`, read the current version and revision. State the exact proposed edits and ask for approval. The edit creates a new private version. On conflict, reload and reconfirm.
5. Before `get_share_link`, name the exact quote, customer and version. Explain that the first call publishes a durable client link and request explicit approval. The link does not send email.
6. Missing line values and `totals_status=incomplete` are not free work. Label the sum incomplete and never present it as final. Respect `needs_review` and `review_issues`.
