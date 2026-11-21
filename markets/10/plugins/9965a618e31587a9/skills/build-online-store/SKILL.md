---
name: build-online-store
description: Build or extend a website that sells products online (an e-commerce or WooCommerce store) in UiChemy, with the standard shop pages: shop, product category, single product, search results, cart, checkout, my account, order details and order tracking. Use when the user wants an online store, an e-commerce site, a product shop, or shop pages added to an existing project.
---

Use this skill when the site sells products online. A service business that is only called a shop (barber shop, coffee shop, repair shop, salon) is not a store unless the user asks for online sales.

Steps:
1. For a new store, build the core site first with the `build-site-from-brief` skill (home, about, contact and any other pages the user wants). For an existing project, identify it with `uichemy_list_projects`.
2. Say that the shop pages will be added to that project, then call `uichemy_add_shop_pages`. It adds the nine standard shop pages under the names WooCommerce expects and leaves existing pages alone.
3. The new pages start with empty copy. Read each one with `uichemy_get_page` and write copy from the brief with `uichemy_set_text` (or `uichemy_batch` for many edits).
4. Run `uichemy_validate` and `uichemy_check_responsive`, fix what they report, then `uichemy_open_preview`.
5. To sell on WordPress, continue with `choose-where-to-publish`. The WordPress export sets up the store pages for WooCommerce.

Rules:
- Do not invent products, prices, stock, shipping terms or reviews. Use what the user gave, or neutral copy.
- Do not rename the shop pages; the cart, checkout and account area expect these names.
- This plugin does not take payments or set up a payment provider. Say so if asked.
