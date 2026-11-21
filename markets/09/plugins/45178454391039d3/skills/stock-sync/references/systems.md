# Stock systems

How each system's Zid connector moves stock, where to export its stock by hand,
and what its quantity column means. When a connector owns the quantities, fix
them in that system and use Zid only to check.

| System | Zid connector and direction | Stock export by hand | Quantity means |
| --- | --- | --- | --- |
| Rewaa | Rewaa's Zid app. Rewaa owns quantities: its changes reach Zid, and quantity edits made in Zid do not flow back. Products match by SKU. Name, description, price and category changes do not sync after linking. | Products and Inventory → Products → Export (a `products_export` archive with simple, variable and composite products). For a count: Inventory Count → Create → location → Export Products → XLSX. | Current balance. Negative Rewaa stock shows as 0 in the store. |
| Foodics | Foodics Integration app: products and stock flow Foodics → Zid; orders and customers flow Zid → Foodics. | Inventory → Inventory Count for counted stock; Reports → Inventory Levels shows stock by branch on screen. Product CSVs (Menu → Products → Export) carry `SKU` and `barcode` but no quantity. | Counted balance per branch. Menu products consume recipe ingredients; match stock products only. |
| Odoo | Through connector apps such as Tecfy and Takamul, which send Odoo stock to Zid; check the connector's warehouse-to-location mapping. | Inventory → Reporting → Stock, filtered by warehouse, then Action → Export. | `On Hand` includes reserved stock; `Free to Use` excludes it. Each variant has its own stock and barcode. |
| Zoho Inventory | No Zid connector documented. | Items → Export Items (CSV) carries opening stock only; current stock per location comes from its API or an Inventory Adjustments file. | Adjustments are deltas. |
| Qoyod | Qoyod's Zid app sends Zid orders to Qoyod as sales invoices and reduces Qoyod stock; no stock flow back to Zid is documented. | Reports → Product Locations Report (Excel, one column per location). | Ending balance per location. Color and size sub-products have their own SKUs. |
| Daftra | Daftra's Zid app syncs products and quantities both ways for the chosen warehouse. | Reports → Store Reports → Stocktaking Sheet → Warehouse → Export (CSV or Excel). | `Stock Quantity` in imports is the ending balance; API stock transactions are movements. |
| Business Central | No Zid connector documented. | Items → Share → Open in Excel; Items by Location shows the per-location matrix on screen. | `Quantity on Hand` is posted stock; projected balance adds incoming and subtracts demand. |
| Google Sheets, Excel | Not a connector. | The sheet itself. | Whatever the merchant's columns say: confirm whether it is a balance or a change. |

## Matching pitfalls

- Spreadsheets drop leading zeros and round long numbers: keep SKUs and barcodes as text.
- One product can have several barcodes; a barcode is an alias, not a second stock row.
- Cartons, packs and weights need the conversion to the selling unit.
- Bundles and kits: assembled stock is a product of its own; a kit's stock is its components'.
- Reserved stock: decide with the merchant whether Zid should show on-hand or available-to-sell, and use the same column every run.

## Building an automated sync

For a script or workflow that repeats this, each system's API documentation is
the reference: Rewaa `https://doc.api.rewaatech.com`, Foodics
`https://apidocs.foodics.com`, Zoho Inventory
`https://www.zoho.com/inventory/api/v1/introduction`, Qoyod `https://apidoc.qoyod.com`,
Daftra `https://docs.daftara.dev`, Odoo the instance's own `/doc` page. Keep keys in the automation tool's secret store. Pass
quantities to Zid in batches and keep one writer per location (see the
`zid-ops` skill).
