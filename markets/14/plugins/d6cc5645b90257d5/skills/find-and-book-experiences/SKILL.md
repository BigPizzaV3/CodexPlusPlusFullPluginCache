---
name: find-and-book-experiences
description: Use when the user wants to find, compare, or book tours, activities, day trips, or local experiences anywhere. Searches the Tixxly supplier network and hands booking off to the operator's storefront.
---

# Find and book experiences with Tixxly

Tixxly connects travelers to tours and activities from independent operators. This plugin searches every supplier on the network. It does not book inside the chat. Booking, passenger details, and payment happen on the operator's storefront.

## Workflow

1. **Search.** Call `experiences_search`.
   - For a country or city, pass `location` alone (for example `location: "Greece"`).
   - Use `query` only for specific activity keywords such as "castle", "food tour", or "hiking".
   - Do not combine a generic query like "things to do" with a location. It over-constrains results.
   - `query` does not match company names. For a specific operator, call `get_vendor_products` with its slug.
2. **Details.** When the user picks a result, call `experiences_detail` with its `experienceId`. Call it once per product.
3. **Availability (optional).** If the user gives a date, call `experiences_availability` with `experienceId`, `startDate`, and `endDate` in `YYYY-MM-DD`. This is read-only and does not hold a spot.
4. **Hand off.** When the user wants to book, give them the `product_url` from the search or detail result. It opens the operator's storefront at `https://stores.tixxly.ai/en/v/{operator}/details?productId={id}`. The widget's "Book on {operator}" button does the same.

## Rules

- An interactive widget shows search results, details, and availability. Do not repeat its contents unless the user asks a question.
- Never ask for or collect names, email addresses, phone numbers, passenger details, or payment information.
- Never say you can reserve, hold, or charge for a booking inside the chat.
- If the user asks to book in chat, explain that booking finishes on the operator's site and share `product_url`.
- If a search returns nothing, say so plainly and suggest a broader location or a different activity.
