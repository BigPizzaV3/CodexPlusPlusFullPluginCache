---
name: get-started
description: Use the Book Safari Tours plugin for Book Safari Tours — what each of its 14 tools does, when to use it, and which ones change data.
---
# Book Safari Tours

Connects you to **Book Safari Tours** (https://booksafaritours.com), a WordPress site. It works on that one site only.
14 tools: 14 read, 0 write.

## Getting started
1. Confirm the user is connected: call `wp_x_safari_browse` with a small limit.
2. Say in two sentences what you can do for Book Safari Tours: Browse safaris and see their full details; Link straight to the booking form for safaris; Browse reviews and see their full details.
3. Offer three starter tasks: Create a new blog post about our upcoming Serengeti safari tours. / List all the recent comments on our safari tour pages. / Update the site settings to change the site title.

## Rules
- Never guess an id. List or search first, then act on the id you found.
- Read tools are safe to call. Before any write tool, tell the user what will change.
- Tools marked "asks first" return a preview when called without `confirm`. Show the preview, and only call again with `"confirm": true` after the user agrees.
- Lists are paged: use `page` and `per_page` (at most 50) rather than asking for everything.
- Customer emails are masked in lists. Fetch a single record only when the task needs the full details.
- If a tool reports an error, tell the user what it said. Do not retry a write without asking.

## Tools
### Site_safari
- `wp_x_safari_browse` — **Browse safaris (customers)** (read). For customers: find published safaris on Book Safari Tours by keyword or filter. Filter by Countries (country), Destinations (destination), Safari types (safari_type), Travel styles (travel_style), Budget levels (budget_level) using term IDs. Each result has book_url: send the customer there to book or enquire on Book Safari Tours's own page.
- `wp_x_safari_view` — **View safari (customers)** (read). For customers: the full public details of one published safari on Book Safari Tours. Each result has book_url: send the customer there to book or enquire on Book Safari Tours's own page.
- `wp_x_tax_country` — **List countries** (read). List the countries on Book Safari Tours with their IDs, to filter safaris.
- `wp_x_tax_destination` — **List destinations** (read). List the destinations on Book Safari Tours with their IDs, to filter safaris.
- `wp_x_tax_safari_type` — **List safari types** (read). List the safari types on Book Safari Tours with their IDs, to filter safaris.
- `wp_x_tax_travel_style` — **List travel styles** (read). List the travel styles on Book Safari Tours with their IDs, to filter safaris.
- `wp_x_tax_budget_level` — **List budget levels** (read). List the budget levels on Book Safari Tours with their IDs, to filter safaris.

### Site_review
- `wp_x_review_browse` — **Browse reviews (customers)** (read). For customers: find published reviews on Book Safari Tours by keyword or filter. Each result has a link to its page on the site.
- `wp_x_review_view` — **View review (customers)** (read). For customers: the full public details of one published review on Book Safari Tours. Each result has a link to its page on the site.

### Site_extension
- `wp_x_extension_browse` — **Browse options & extensions (customers)** (read). For customers: find published options & extensions on Book Safari Tours by keyword or filter. Filter by Countries (country) using term IDs. Each result has book_url: send the customer there to book or enquire on Book Safari Tours's own page.
- `wp_x_extension_view` — **View extension (customers)** (read). For customers: the full public details of one published extension on Book Safari Tours. Each result has book_url: send the customer there to book or enquire on Book Safari Tours's own page.

### Site_api
- `wp_x_api_bst_v1_safaris` — **Search safaris** (read). For customers and staff: Book Safari Tours's own "safaris" search (/bst/v1/safaris). Items with a link get book_url for booking or enquiring on the site.

### Posts
- `wp_list_categories` — **List categories** (read). List post categories on Book Safari Tours.
- `wp_list_tags` — **List tags** (read). List post tags on Book Safari Tours.
