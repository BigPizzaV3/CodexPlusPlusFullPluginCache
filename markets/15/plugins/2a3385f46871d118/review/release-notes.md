# KOOKone assistant 1.0.7

Text stored in `extensions.com.openai.publication.release_notes`:

Cart preparation and procurement for a connected KOOKone company. Search deliverable offers, set cart quantities and the delivery address, and read invoice spend and marketplace alternatives. Ordering and payment stay on the KOOKone website.

## What this version does

A connected KOOKone customer can:

- search the marketplace catalog and open a product sheet
- build and review the company cart, including delivery address, units of measure and supplier minimums
- open the cart on the KOOKone website to place and pay the order
- read procurement data the company plan allows: invoice spend, price trends and anomalies, off-network price rules, marketplace alternatives, food cost, recipes, menus, and HACCP work orders and lots

## Review dataset

The procurement cases and the demo use the demo invoices: 12 invoices from 8 September to 4 November 2026, three suppliers and 55 products. The largest spend is Caffè in grani 85% arabica 1 kg (`CAF-ARB85-1KG`), priced per kg. Two recipes are costed from those invoices, Caffè espresso and Cappuccino. Marketplace search uses the text aperol 1L bottiglia.

## What this version does not do

Checkout and marketplace orders are not tools of this connector. ChatGPT does not call `prepare_checkout`, `place_order`, `pay_order`, `list_orders`, `track_order` or the other order tools. The user finishes the order on https://www.kookone.com.

Order Hub, passive-invoice upload, reconciliation, external-order entry, the enterprise CRM, document OCR and image upload are not exposed.

## Publisher

CIGUALA s.r.l., info@kookone.com. Same name and email as the privacy policy and the terms of service.

## Known gap before public review

The linked privacy policy and terms of service describe the KOOKone website. They do not name the MCP connector, ChatGPT or OpenAI, and they do not describe the account, company, cart and procurement data sent through the connector. Update both iubenda documents before submission. The connector must not ship until that text is live.
