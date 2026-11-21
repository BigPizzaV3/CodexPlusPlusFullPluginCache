---
name: digital-product-passports
description: Get a product's EU digital product passport (DPP) ready in Veribl: see what each rule still needs, fill it from the brand's documents, battery passports, units and batches, substances, environmental data, supplier answers and EU registry status. Use for any DPP, ESPR, battery regulation or passport-readiness question.
---

# Digital product passports

1. `list_products`, then `get_passport_checklist` for the product: it lists every rule that applies (ESPR, batteries, textiles…) and what each still needs.
2. Fill only what a document states (manual, datasheet, declaration, supplier file): `update_passport_data`, `update_product` (materials, recycling, lifetime), `update_environmental_data`, `add_substance`. Never guess a value; if nothing states it, say what's missing and who usually has it (often the supplier).
3. Batteries: `get_battery_passport` / `update_battery_passport`.
4. Serial-level passports: `list_units`, `get_unit`, `add_unit_event` (repairs, refurbishment, change of owner). Lots: `list_batches`, `create_batch`.
5. Supplier data: `list_supplier_answers`, and `decide_supplier_answer` to accept or reject what a supplier sent, only when the user decides.
6. `get_registry_status` for the product's EU registry state.
7. If a value changed by mistake, `get_product_history` and `restore_product_history`.

Never publish a passport: that stays the brand's decision in Veribl. End with what's now complete, what's still missing and who should provide it.
