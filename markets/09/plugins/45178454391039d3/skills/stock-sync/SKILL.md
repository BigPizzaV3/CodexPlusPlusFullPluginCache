---
name: stock-sync
description: Keep a Zid store's stock in line with an ERP, POS, warehouse system or spreadsheet such as Rewaa, Foodics, Odoo, Zoho Inventory, Qoyod, Daftra or Business Central. Use to compare quantities by SKU and location, apply a stock file or physical count to Zid, record received or damaged stock, or check why two systems disagree.
---

# Stock sync

Compares the stock in another system with Zid's, product by product and location
by location, then brings Zid in line with whichever system the merchant names as
the source of truth.

## Ground rules

- The merchant's explicit instructions take precedence over this skill.
- One system owns each quantity. Before writing, find out whether a connector
  already pushes stock into Zid (step 1). Writing beside a connector makes the
  two overwrite each other, so with one in place this skill reports and leaves
  the fixing to the owning system.
- Show the full change list and apply it after the merchant agrees. When a
  manage tool answers `confirmation_required`, compare its plan with what the
  merchant approved: if they match, repeat the call with its `plan_id`; if not,
  show the plan and ask again.
- Other systems' credentials (API keys, passwords, tokens) stay in that system or
  in the merchant's automation tool. Work from the files the merchant shares.

## 1. Find the source and the owner

1. Ask which system holds the true stock, or read it from the file the merchant shares.
2. `zid_account.list_installed_apps` shows whether that system's connector is
   installed. Look the system up in [references/systems.md](references/systems.md)
   for which way its connector moves stock and how to export its stock.
3. Locations: `zid_inventory.list_locations`. Agree which source warehouse or
   branch maps to which Zid location; one source location can feed only one Zid location.

Done when you can name the owner of the quantities and the location mapping.

## 2. Read both sides

- **Source**: the merchant's export. Find the SKU, barcode, quantity and location
  columns by matching values against Zid's SKUs, not by header names. Read
  identifiers as text so leading zeros survive. Note whether the quantity is an
  ending balance or a movement (+/-); the references say which for each system.
- **Zid**: `zid_products.list_products` with `pageSize` 100 and every page (or
  `search` for one SKU or barcode; `locationIds` limits it to the mapped
  locations). For each product in scope, `zid_products.list_stock` with
  `productId` gives its quantity at each location; for a product with variants,
  `zid_catalog.list_variants` with `productId` and `locationIds` gives each
  variant's stock. For catalogs of more than a few hundred products,
  `zid_catalog_manage.export_products` with `locationIds` emails the merchant the
  dashboard's product export; ask them to share it and compare the two files.

## 3. Match and compare

Match each source row to a Zid product or variant by SKU, then by barcode. Map
each variant to its own row. Convert cartons or
packs to the unit Zid sells before comparing.

Put each row in one class:

- equal;
- differs: show Zid quantity, source quantity and the difference;
- unlimited in Zid: the product does not track stock; changing it is a separate decision;
- bundle: its stock comes from its products, so leave it out;
- only in source / only in Zid: list them, with likely matches when a SKU differs only by spacing or case;
- invalid: negative, blank or non-numeric quantity.

Done when every source row and every tracked Zid product at the mapped locations
sits in one class and the counts add up.

## 4. Apply

Pick the path that matches what the numbers mean:

| The numbers are | Use | Notes |
| --- | --- | --- |
| A physical count | `zid_inventory_manage.create_stock_count` with `locationId`, `name` and `start` true counts every tracked product at the location. For some products only, create it with `isPartial` true, add them with `zid_inventory_manage.update_stock_count` (`stockCountId`, `productIds`), then start it with `countStatus` `in_progress`. Enter counts with `zid_inventory_manage.record_counted_quantities` (`stockCountId`, `counts` of `productId` and `count`, up to 500 per call) and apply with `zid_inventory_manage.complete_stock_count` | Applies counted minus expected, so sales made during the count are kept. Completing cannot be undone. |
| Exact balances from the source | `zid_inventory_manage.update_location_stock` with `locationId` and `products` (`productId`, `availableQuantity`, `isInfinite`) | Replaces the quantities. Orders placed between reading the source and writing are overwritten, so run it right after the export. |
| One product across locations | `zid_products_manage.bulk_update_stock` with `productId` and `stocks` (`location`, `availableQuantity`, `isInfinite`) | |
| Movements: stock received, damaged, returned | `zid_products_manage.adjust_stock` with `productId`, `locationId`, `quantityChange` (signed, not 0) and `adjustmentReason` | Refuses to go below 0 and refuses unlimited stock. |

## 5. Verify

Read `zid_products.list_stock` with `productId` again for the changed products and report the counts
per class before and after. `zid_inventory.list_stock_history` (last 60 days, by
`locationId` or `productId`) shows who or what changed a quantity, which explains
most "the numbers keep drifting" questions.

## Output

A table of SKU, product, location, Zid quantity, source quantity, difference and
class, followed by counts per class, the changes applied, and the rows that need
the merchant (unmatched SKUs, bundles, unlimited stock, invalid quantities).

To repeat the sync on a schedule, use the `zid-ops` skill.
