---
name: giftroam
description: Send a real gift — gift baskets, flowers, chocolates and treats — to someone in 190+ countries. Use when the user wants to send, find or track a physical gift for a person in another city or country. Final prices include delivery; checkout happens on GiftRoam's secure page.
---

# GiftRoam
Send real gifts abroad — user-confirmed checkout, recipient details never in chat.

## Instructions
GiftRoam sells physical gifts only: curated gift baskets, fresh flowers, chocolates, gourmet food and plush gifts, assembled and delivered by a local partner in the destination country. 193 destination countries.

- Every price is **final and includes delivery**; taxes, if any, are shown at payment.
- The recipient's name, address and phone, and the payment, are entered **only** on GiftRoam's secure checkout page (checkout.giftroam.com, Stripe). Never in chat.
- After payment the buyer receives a private **order token** (`GR-XXXXX-XXXXX-XXXXX-XXXXX-XXXXXX`) by email for tracking.

## Tool selection
| The user wants… | Call |
|---|---|
| Gift ideas for a destination | `search_gifts` (country = ISO-3166 alpha-2 code) — renders the gift cards |
| More about one gift (contents, arrival window) | `get_gift_details` with the `gift_id` from `search_gifts` |
| "Can it arrive by …?" | `check_delivery` (country, `date_needed`, optionally `gift_id` and city) |
| To actually send it | `create_checkout` → show summary → user approves → share the link |
| Where is my order? | `get_order_status` (needs the order token) |
| All my orders | `list_my_orders` (signed-in connection only) |

## The confirm gate — REQUIRED before sharing a checkout link
1. `create_checkout` returns a summary (gift, destination, final price, delivery estimate, card message) and a single-purpose link that **expires in 30 minutes**. Nothing is charged by the tool.
2. Show the summary and get the user's **explicit OK**.
3. Only then share the link. If the call must be retried, reuse the same `idempotency_key` — it returns the same link.

## Arguments that must be exact
- **Country:** always the ISO-3166 alpha-2 code — `FR`, not "France"; `US`, not "USA". A city ("Paris") tells you the country; it does not replace it.
- **Dates:** `YYYY-MM-DD`. Resolve "next Friday" or "for her birthday on the 12th" to a calendar date yourself before calling.
- **Budget:** `budget_min` / `budget_max` are in **cents** — "under $100" is `budget_max: 10000`.
- **Query:** product keywords only, 1–4 words ("red roses", "chocolate basket"). Put the occasion in `occasion` and the destination in `country`, not in the query.
- **Occasion slugs:** birthday, anniversary, thank-you, congratulations, get-well, sympathy, new-baby, housewarming, corporate, just-because, valentines-day, mothers-day, fathers-day, rosh-hashanah, hanukkah, christmas, new-year.
- **Language:** pass `locale` with the conversation's language (e.g. `he-IL`, `fr-FR`) so gift names, descriptions and messages come back in it.

## Presentation rules
- Use the `gift_id` from the results for details and checkout. Do not search again just to find a gift the user picked from the cards.
- Ask only for what is missing before searching: the destination country is required; occasion, budget and deadline help.
- When the user has a deadline, call `check_delivery` and say that dates are **estimates**, not guarantees.
- Offer to write the card message (max 180 characters), in the recipient's language if the user wants.
- Quote prices, availability and dates from this conversation's tool results only.

## Do not
- Do not ask for or accept the recipient's address, phone or email, or any payment details in chat — the checkout page collects them.
- Do not promise a delivery date the tools did not confirm.
- Do not share a checkout link before the user explicitly approves the summary.
- Do not guess or enumerate order tokens; use only the token the user provides.
- Do not sell digital gift cards, vouchers or experiences — GiftRoam delivers physical gifts only.
- Do not invent products, prices, coverage or order states — always use the tools.

## Notes
- Alcohol-containing gifts are not offered through AI assistants.
- `list_my_orders` needs the signed-in GiftRoam connection; on a guest connection it returns `auth_required` — everything else works without an account.
- Site: https://giftroam.com · MCP endpoint: https://mcp.giftroam.com/mcp
