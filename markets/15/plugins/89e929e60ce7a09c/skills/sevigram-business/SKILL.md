---
name: sevigram-business
description: Use when the user asks about or wants to change their Sevigram business records, such as sales and reports, orders and bookings, invoices and quotes, customers, services and products, expenses, assets or deliverables. Covers choosing the business, reading accurately, confirming changes, and explaining Sevigram review links.
---

# Working with a Sevigram business

The Sevigram Business tools read and change the records of businesses the user runs on Sevigram. Explicit user instructions take priority over this guidance.

## 1. Choose the business first

- Call `list_businesses` before any other business tool. Every other tool needs its `business_id`.
- If there is one business, use it. If there are several and the request doesn't name one, ask which business to use. Never guess.
- If the user only connected some of their businesses, say so when they ask about one that isn't listed. They can change this by reconnecting.
- Call `get_business_capabilities` when you need the business's currency, time zone or what the user may do there.

## 2. Read accurately

- Report only what the tools return. Never invent, estimate or round figures, names, dates or statuses.
- Always give amounts with their currency. A business can have records in more than one currency, so keep them separate.
- Use the business's time zone for dates such as "today" or "last month". `expenses_get_context` gives the business date for expenses.
- Lists are paged. If a result says there are more items, say how many you've shown, or fetch further pages before giving a total. Prefer report and summary tools such as `analytics_get_sales_report`, `analytics_get_dashboard` and `expenses_get_overview` for totals.
- For invoices, "unpaid" means an issued invoice whose payment state is not fully paid. Check the `balance`.

## 3. Making changes

There are two kinds of change, and the tool descriptions say which kind each tool is.

**Changes that run once confirmed** (for example adding a customer, recording an expense, drafting a quote or invoice, updating a product):
1. Gather every required detail. If one is missing or unclear, ask. Don't fill it in yourself.
2. Show the user exactly what will be created or changed and ask them to confirm.
3. Call the tool only after they confirm, then report the result the tool returned.

**Changes reviewed in Sevigram** (anything that contacts a customer, records or reverses a payment, issues or voids a document, deletes or archives a record, or imports data in bulk):
1. Gather and confirm the details as above, then call the tool.
2. The tool returns a review link. Give the user the link and say plainly that nothing has happened yet: the change only happens after they approve it in Sevigram.
3. Never say an email was sent, a payment was recorded or a document was issued until `get_action` reports the action succeeded.
4. When the user says they approved it, call `get_action` to check and report the actual outcome. If its state is `outcome_unknown`, tell them to check the record in Sevigram and not to repeat the request.

If a change fails because the record changed since it was prepared, fetch the record again and ask the user before trying again.

## 4. Money

- Sevigram tools never move money. `invoices_record_payment`, `orders_mark_manual_paid` and the refund tools only record money the business already received or paid back outside Sevigram.
- If the user asks you to pay, transfer or charge someone, say you can't move money. Offer to record a payment or expense that already happened instead, if that fits.

## 5. Files and imports

- To import customers, expenses, assets or deliverables, first get the CSV template with the matching `*_download_import_template` tool. Then use `prepare_file_upload` to give the user an upload link, check the file with the matching `*_preview_import` tool and show the result, and only then import it.
- Uploaded and generated files are kept for one hour.

## 6. Stop and ask

Stop and ask the user instead of acting when:
- the business, customer, record or amount is ambiguous or missing;
- a search returns more than one plausible match;
- the request would affect many records at once, such as "delete all customers". There is no bulk delete, so explain what is possible instead;
- the user asks for something the tools can't do. Say so plainly, and don't work around it with other tools.
