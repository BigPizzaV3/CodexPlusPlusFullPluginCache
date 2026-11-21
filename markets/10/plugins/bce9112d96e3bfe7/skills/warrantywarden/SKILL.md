---
name: warrantywarden
description: "Use when the person asks about WarrantyWarden: Track your product warranties"
---

# WarrantyWarden

Track your product warranties

## Tools that read

- `get_subscription_plans`: Get Subscription Plans. Get all active subscription plans with regional pricing. Region priority: 1) Explicit param, 2) User's country, 3) IP detection, 4) USD default.
- `get_credit_history`: Get Credit History. Get user's credit purchase and usage history.
- `get_inventory_categories`: Get Inventory Categories. Get categories with item counts from user's inventory.
- `get_inventory_summary`: Get inventory summary. Returns an overview of the user's WarrantyWarden inventory: how many products they track and how many have confirmed details, plus the products that need attention (warranties ending in the next 30 days, and products whose details aren't confirmed yet). Use it first for questions about their products as a whole.
- `get_item_detail`: Get product details. Returns what WarrantyWarden knows about one of the user's products: name, brand, model, category, warranty information, and links to its manual, support page and receipt where available. Get item_id from the `id` of items returned by list_user_items.
- `get_item_warranty`: Get warranty status. Returns whether one of the user's products is still under warranty: its status, the warranty terms, purchase date, start and end dates and days remaining. Use it to answer "is my <product> still under warranty?". Get item_id from the `id` of items returned by list_user_items.
- `get_support_history`: Get Support History. Get user's support request history.
- `get_upcoming_alerts`: Get upcoming warranty reminders. Returns the warranty reminders WarrantyWarden will send the user within the given number of days (for example, a warranty ending in 30 days, or one that has expired), each with its date and product.
- `get_upcoming_warranty_expiries`: Get warranties ending soon. Returns the user's products whose warranty ends within the given number of days, with each product's id, name, warranty end date and days remaining.
- `get_user_subscription`: Get subscription. Returns the user's WarrantyWarden plan: its name and status, when it expires, how many products they track and the plan's product limit. A product_limit of -1 means unlimited.
- `list_agent_tasks`: List Agent Tasks. List AI agent tasks for the current user. Returns active tasks (pending, in_progress, awaiting_user) by default. Set include_completed=true to also include recently completed tasks. Paginated: use limit to fetch further results when a page may be incomplete.
- `list_digital_archive`: List Digital Archive. Unified view of all user items: Physical Products + Travel/Bookings. Returns sorted, filtered, and paginated list. Paginated: use skip and limit to fetch further results when a page may be incomplete.
- `list_user_items`: List User Items. List authenticated user's items with their linked products and brands. Paginated: use skip and limit to fetch further results when a page may be incomplete.
- `list_user_products`: List User Products. List products owned by the authenticated user (via UserItem link). Paginated: use skip and limit to fetch further results when a page may be incomplete.
- `search_inventory`: Search inventory. Finds products in the user's WarrantyWarden inventory by name, brand or model, optionally within one category. Returns each product's id, name, brand, model, category, purchase date and warranty status and end date. Use it to list products or to find a product's id for the other tools. Paginated: use limit to fetch further results when a page may be incomplete.

## Example requests

- Is my iPhone 15 Pro Max still under warranty, and until when?
- Which of my warranties expire in the next 30 days?
- Which WarrantyWarden plan am I on?
