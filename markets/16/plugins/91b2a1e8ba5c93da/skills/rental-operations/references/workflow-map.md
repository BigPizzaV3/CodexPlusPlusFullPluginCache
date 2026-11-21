# Workflow map

| User task | Tool sequence |
| --- | --- |
| Find location stock | `get_account`, `list_products`, `get_product`, `get_product_bookings` |
| Maintain rental units | Product/variant tools, exact product-item tools, reversible trash/restore |
| Maintain consumables | Product/variant tools, `update_consumable_stock`; checkout fulfills quantity rows |
| Customer records | Customer tools, address tools, typed custom fields and comments |
| Rental order | Resolve customer and stock, `create_order`, lifecycle tools; inspect current state before each dependent action |
| Rental return | Read order items, record condition and any user-supplied deposit disposition, `return_order` or exact item transitions |
| Documents | `get_order`, `get_order_document`, `preview_order_document_pdf`; issue/share only when requested |
| Import inventory | `upload_chatgpt_file` (or bounded `upload_file`), `create_inventory_import`, `preview_inventory_import`, `confirm_inventory_import` |
| Webstore | `get_webstore`, slug/domain checks, create/update, existing-domain attachment and verification |
| Team/settings | Current account, admin team/role/location-access tools, location settings, custom-field definitions |
| Account security | `get_account_security`; open secure pages instead of collecting credentials |
| Existing billing | `get_billing` for current status and invoices. `open_billing_portal` links to the authenticated RentalBench billing overview for identity and payment settings. |

List tools support bounded pages where advertised. Follow `pagination.has_more` with the next offset until the requested scope is covered. Never describe a first page as the entire inventory. Preserve the location's currency and time zone when comparing schedules or totals.
