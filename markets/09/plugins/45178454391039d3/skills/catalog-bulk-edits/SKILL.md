---
name: catalog-bulk-edits
description: Change many Zid products at once. Use for price increases or decreases by percent or from a list, folding payment fees into prices, sale prices, publishing or hiding, categories, names, descriptions and SEO, images, market prices, duplicating or deleting products, or importing a product spreadsheet.
---

# Catalog bulk edits

Selects the products, shows every change before it happens, applies it with the
right tool for its size, and checks the result.

## Ground rules

- The merchant's explicit instructions take precedence over this skill.
- Show the full change list (product, field, current → new) and apply it after
  the merchant agrees. When a manage tool answers `confirmation_required`,
  compare its plan with what the merchant approved: if they match, repeat the
  call with its `plan_id`; if not, show the plan and ask again.
- Change only the fields the merchant asked about. Rounding, products with
  variants, and items already on sale are the merchant's call: ask once, then
  apply the answer to every row.

## 1. Select the products

`zid_products.list_products` with `pageSize` 100, every page. Filters: `search`
(name, SKU or barcode), `categoryIds`, `priceMin` and `priceMax`, `isPublished`,
`inStock`, `hasDiscount`, `productClass`, `updatedFrom`. Details of one product:
`zid_products.get_product`. Variants of a product: `zid_catalog.list_variants`.
A product id that returns 404 was deleted: list again rather than retrying it.

Done when the merchant agrees with the list (count, plus a sample for long lists).

## 2. Work out the changes

- **Percent change**: new price = price × (1 + percent), rounded the way the
  merchant chose. A sale price stays below the price; recalculate it or flag the row.
- **Folding a payment fee into prices**: new price = price ÷ (1 − r), where r is
  the fee percentage as a fraction (2.5% → 0.025) from `zid_payments.get_fee_plan`
  or the merchant. Ask whether a fixed fee or VAT on the fee should be included.
- **From a list**: match rows to products by SKU, then barcode; list unmatched rows.
- **Text and SEO**: draft per product in the store's languages, keep facts from
  the current description, and state only specifications the product data or the merchant gives.

## 3. Apply

| Change | Tool |
| --- | --- |
| Name, price, quantity for many products | `zid_products_manage.bulk_update_products` with `products` (`id` and `sku` required, plus `name`, `price`, `quantity`, `isInfinite`) |
| Sale price, cost, description, SEO, keywords, barcode, weight, one product at a time | `zid_products_manage.update_product` with `productId` and only the changed fields |
| Publish or hide, VAT, shipping required (store owner only, up to 100 products per call) | `zid_catalog_manage.bulk_update_products` with `productIds` and `published`, `taxable` or `requiresShipping` |
| Move between categories (store owner only, up to 100 products per call) | `zid_catalog_manage.bulk_move_categories` with `productIds`, `oldCategoryId`, `newCategoryIds` |
| Add one product to several categories | `zid_products_manage.bulk_add_categories_to_product` with `productId` and `categoryIds` |
| Prices per market (stores selling in several markets) | `zid_settings.list_markets`, `zid_catalog.list_prices`, then `zid_catalog_manage.update_prices` with `priceUpdates` (up to 100 per call; `salePrice` null removes the sale) |
| Images | `zid_products_manage.add_product_image` (`productId`, `imageUrl` reachable from the internet, `altText`); order with `zid_products_manage.sort_product_images` |
| Duplicate, delete, restore | `zid_catalog_manage.bulk_duplicate_products`, `zid_catalog_manage.bulk_delete_products` (to the trash for 60 days), `zid_catalog_manage.restore_products` (returns hidden with zero stock) |

Large batches go in groups of 100, one group at a time.

## 4. Spreadsheet edits

For hundreds of rows or many fields at once:

1. `zid_catalog_manage.export_products` emails the merchant the catalog.
2. The merchant edits it and puts it at a public URL ending in `.csv` or `.xlsx`.
3. `zid_catalog_manage.import_products` with `fileUrl` and `importMode`:
   `update_all_fields` updates products matched by SKU with every column (blank
   cells are ignored unless `deleteEmptyFields` is true); `import_new` adds the
   rows as new products. `delete_old` deletes every current product first: use
   it only when the merchant asks for exactly that.
4. `zid_catalog.get_import_status` until it finishes; report the rows it rejected.

## 5. Verify

Read the changed products again (`zid_products.get_product`, or the list with
the same filters) and report changed, unchanged and failed rows with the reason.

Done when every product in the approved change list is reported as changed,
unchanged or failed.

## Output

The change table before approval; afterwards, counts of changed, skipped and
failed products and the failures with their reasons.
