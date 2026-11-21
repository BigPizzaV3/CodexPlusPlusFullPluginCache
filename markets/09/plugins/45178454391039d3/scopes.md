# OAuth scopes

Zid grants each ChatGPT connection permissions for one authenticated store and
Zid user. The server checks the granted scopes for every public tool call, and
every call is also limited to that Zid user's own dashboard permissions.

| Scope | Access |
| --- | --- |
| `profile:read` | Read the connected store's public name, stable profile ID, setup status and dashboard overview. |
| `orders:read` | List and inspect the connected store's orders, returns, draft orders, order tags and statuses, and abandoned carts (abandoned carts are read-only). |
| `orders:write` | Change order status, manage returns, draft orders, order tags and custom statuses. |
| `products:read` | Read products and their categories, attributes, images, vouchers, digital codes, badges, brands, custom fields, pre-order campaigns and back-in-stock alerts. |
| `products:write` | Manage products and their categories, attributes, images, vouchers, digital codes, badges, brands, custom fields and pre-order campaigns. Setting stock through products, variants, or a catalog import also needs `inventory:write`. |
| `inventory:read` | Read product stock, store locations, stock transfers, stock counts and stock history. |
| `inventory:write` | Change product stock, and manage store locations, their stock, stock transfers and stock counts. |
| `customers:read` | List and inspect the connected store's customers, customer groups and tags, wallet balances and support tickets. |
| `customers:write` | Manage customers, their addresses, notes, tags and customer groups, and export customers to the account's email. Crediting or debiting a wallet is not available in ChatGPT. |
| `marketing:read` | Read coupons, bundle offers, automatic and bank discounts, gifting, loyalty, cashback, campaigns, WhatsApp and notification templates, and affiliates. |
| `marketing:write` | Manage coupons, bundle offers, discounts, gifting, loyalty rules and points, cashback, campaigns, WhatsApp and notification templates, and affiliates' commission, discount and status. Adding an affiliate or changing their bank details is not available in ChatGPT. Sending a campaign is previewed first. Reading or adjusting one customer's points also needs `customers:read`. |
| `content:read` | Read product reviews, product questions, blog posts, blog categories and tags, store pages, FAQs, legal pages, SEO settings and product feeds. |
| `content:write` | Moderate and reply to reviews, answer questions, and manage blog content, store pages, FAQs, legal pages and SEO settings. |
| `design:read` | Read installed themes, theme settings, menus, landing pages and store identity (logo, colors, social links). |
| `design:write` | Edit installed themes, menus, landing pages and store identity. Installing a theme from the Zid theme market is not available in ChatGPT. |
| `shipping:read` | Read shipping methods, shipping zones and the store's countries and cities. |
| `shipping:write` | Manage shipping methods, zones and shipping settings. |
| `analytics:read` | Read store reports, and aggregate sales, order count, visits, and session conversion for a date range of up to 90 days. |
| `analytics:write` | Create, edit, pin, unpin and delete saved custom reports. Reports Zid provides are saved as a copy, never overwritten. |
| `payments:read` | Read payment methods, gateways, bank accounts for bank transfer, ZidPay deposits, transactions, refunds and disputes. |
| `payments:write` | Turn a payment gateway or bank transfer on or off, remove a bank account, and respond to a dispute. Refunds, payment links and payment status changes are not available in ChatGPT. |
| `settings:read` | Read store settings such as profile, opening hours, languages, currencies, taxes, e-invoicing, markets, domains and URL redirects. |
| `settings:write` | Change store settings such as profile, opening hours, languages, currencies, taxes, markets, domains and URL redirects, and open or close the store. |
| `account:read` | Read team members, roles and their locations, the action log, installed apps and their permissions, and support tickets. |
| `account:write` | Invite, update and remove team members, manage roles, and open and reply to support tickets. A Zid Cashier's login code, app integrations and security settings are not available in ChatGPT. |
| `pos:read` | Read point-of-sale settings, cashiers, payment methods, sales and reports. |
| `pos:write` | Manage point-of-sale settings, cashiers and payment methods. |
| `marketplaces:read` | Read connected sales channels and marketplaces, their products and price rules. |
| `marketplaces:write` | Manage sales channel and marketplace settings, listings, price rules and warehouses, and disconnect a marketplace. |

The analytics summary contains only those documented aggregate values and
localized currency labels. It does not expose the store's analytics token or
the upstream response body.

Zid plans, add-ons, purchases, the app market, the theme market, growth
services, phone verification codes, API keys, login codes, and entering or
changing bank details are not available in ChatGPT under any scope. Bank
accounts the store already saved are shown masked.
