---
name: lapyme-supplier-cost-updates
description: Assess and apply supplier cost increases in La Pyme when product scope, margin impact, bulk adjustment, or downstream synchronization matters. Do not use for an unrelated single-product edit.
---

# La Pyme Supplier Cost Updates

Resolve the affected supplier and product scope, assess the commercial impact, and apply only the cost change the user requested.

Read `context://core-rules`, `context://reporting-rules`, and `reporting://catalog` when their money or report semantics affect the assessment.

## Resolve Scope And Impact

- Use `list_suppliers` to resolve the supplier by name, email, or a returned internal identifier.
- Use `list_products` for an explicit SKU, barcode, name, category, or product-type scope. It cannot enumerate a supplier's complete catalog.
- For a supplier-wide scope, use `run_report` with inventory dimensions `defaultSupplierName` and `product` to enumerate the products whose default supplier matches. Products bought from a supplier are not necessarily the same set.
- Ask for the supplier's file or exact product list when the affected scope cannot be identified safely from the request.
- Use reporting to estimate recent sales, margin, inventory exposure, and purchase impact. Keep cost impact separate from any selling-price recommendation.

Before a broad supplier-wide write, show the resolved scope unless the user already gave an exact product list and an explicit instruction to apply it.

## Apply The Update

- Use `bulk_adjust_products` with `target: cost` for confirmed cost changes.
- For a percentage increase across the resolved default-supplier scope, use the resolved `defaultSupplierId`, `operationType: increase`, `adjustmentType: percentage`, the requested percentage, and `allMatching: true`.
- Use explicit `productIds` instead of `allMatching` when the increase applies to a specific product or variant list.
- Do not update base selling prices unless the user separately requested that change.
- An exact apply instruction with resolved scope is sufficient authorization. Analysis alone does not authorize a write.

Read and report the result counts. `updated` is the adjusted variant count; `skipped` includes matched variants that were not changed, such as variants without a cost. Local commerce records and synchronization effects are written together, but provider execution can remain asynchronous. Do not claim that external channel prices or costs are already synchronized unless the returned state proves it.
