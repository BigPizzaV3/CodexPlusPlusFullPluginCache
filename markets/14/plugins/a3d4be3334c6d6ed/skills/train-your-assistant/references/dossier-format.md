# The company dossier

The dossier is the master record of what a business's assistant may say. It is complete and
platform-free: platform limits shape the EXPORTS, never the dossier. The owner keeps it and brings
it back to update.

## Format of dossier.md

```
# <Business name> — assistant dossier
Prepared <date> · Last updated <date> · Assistant platform: <Endelir / other / not decided>

## 1. Identity
What the business is, in two sentences. City, area, address, landmark, how to reach.
Assistant name and tone (e.g. "Kavi — warm and brief, like a good barista").

## 2. Offerings and prices
One table per group. Every row carries its source.
| Item | Variant | Price | GST | Unit | Source | Read on | Status |

## 3. Buying, booking and payment
## 4. Delivery or service area
## 5. Timings
## 6. Policies — cancellation, returns and refunds, warranty, privacy
## 7. Customer questions — the top questions, the words customers use, and the answers
## 8. Objections and the honest answers
## 9. Sales guidance (INTERNAL — never shown to customers)
Lowest prices, gives to offer before any discount, negotiation rules, approved deals and upsells,
qualifying questions.
## 10. Never say or promise
## 11. Hand over to a person — when, and to whom
## 12. Languages customers write in
## 13. Not applicable — what the business does not do (e.g. "no home delivery")
## 14. When the assistant does not know — what it says, and who it hands to
## 15. Sources — every page and document read, with the date
```

Fact status is one of: **confirmed** (the owner said yes) · **from source, not confirmed** · **owner
to decide**. Nothing leaves the dossier for an export until it is confirmed, marked not applicable,
or covered by section 14.

## Conflicts

When sources disagree, record both values with their sources and ask the owner which is current.
A newer document does not automatically beat the website, nor the website a document.

## Interview checklist

Tick each item from the website or documents first; ask only for what is still missing.

1. Offerings and prices — every product or service, variants or sizes, price and unit, GST included or extra, seasonal or weekend prices, what is included.
2. Who buys — typical customers, groups, corporate or bulk buyers.
3. How to buy or book — chat, website, store visit; what the business needs to confirm (date, size, address, number of people).
4. Payment — UPI, cards, cash on delivery (limit, fee), advance or token amount, payment link.
5. Delivery or service area — cities or pincodes, charges, free above, time taken, same day.
6. Timings — opening hours, days closed, support hours, check-in and check-out.
7. Location — full address, landmark, how to reach (airport, station, ferry, parking), map link.
8. Cancellation and refunds — by notice period, peak dates, how refunds are paid and how fast.
9. Warranty or guarantee — what is covered, how to claim.
10. Top customer questions — the ten most asked, and the exact words customers use (including Hindi or regional phrasing).
11. Objections — "too expensive", "I'll think about it", competitors — and the honest answer.
12. Discounts — the lowest price per product, and non-cash gives to offer first (free delivery, a free add-on). INTERNAL.
13. Deals and upsells — bundles, group or corporate offers, first-order offers, add-ons.
14. Never — what the assistant must never promise or say (medical claims, delivery dates, availability without checking).
15. Hand over — when a person must take over (complaints, custom quotes, big orders) and who.
16. Languages — which languages customers write in.

## Large price lists — one rule

The dossier and the knowledge file always hold every price. A platform's instructions field may be
too small for all of them; then the instructions hold the prices customers ask about most, every
other price stays in the knowledge file, and the export says how many prices are in the knowledge
file only — the assistant can quote those only when its search finds them. Shorten wording before
dropping any price from the instructions.

## Export for any other platform (or not decided)

- **assistant-instructions.txt** — who the assistant is and its tone; how to qualify a customer;
  the price list; key facts (address, timings, delivery, payment); policies in short; never-say
  rules (section 10); when to hand over (section 11); what to do when it does not know (section
  14). Never internal sales guidance (section 9): a private instructions field does not guarantee
  the assistant keeps it to itself. Lowest prices go only into a setting the platform built for
  them; with none, they stay in the dossier.
- **knowledge.txt** — one document: sections with headings in CAPITALS, each followed by the
  customer's words in brackets, every price, policies in full, questions and answers.
- Ask whether the platform has limits on either; fit to them the way endelir-export.md does.

## A knowledge file that is too long

The knowledge file holds every price and policy. When it is longer than the platform accepts in
one document, split it into the fewest documents possible, by whole sections, each self-contained:
a section carries its own prices, conditions and exceptions, so no answer needs two documents
(search does not connect facts across documents). Never cut inside a section. Name the parts by
topic (knowledge-1-products.txt, knowledge-2-policies-and-faq.txt) and list them in the export.

If ONE section is longer than the limit by itself (a very large catalogue, a long price list),
split that section into parts by a natural sub-topic — a product category, a brand, a price band —
never in the middle of an item. Give each part the section's heading plus its sub-topic and "part
1 of 3", and repeat in every part the conditions that apply to all of it (GST, units, delivery
charges, validity dates), so each part answers on its own. Tell the owner the catalogue spans
several files.

## Two checks: the content rehearsal, then the live check

**Content rehearsal (you, before handing over files).** Answer these as the assistant would, using
ONLY the exported text, and show the owner. It finds missing or wrong content. It cannot test the
running assistant — its search, routing or price checks — so say so.

1. "How much is <their most popular item>?" — the exact price, with GST and unit.
2. A total for several items or people — the working shown.
3. "It's too expensive." — the honest answer, no invented discount.
4. "Can I cancel / get a refund?" — the policy, accurately.
5. "Where are you, how do I get there?" — the address and landmark.
6. A question the dossier cannot answer — the section 14 reply and handover, never a guess.
7. The same price question in Hindi (or the owner's customers' language) — the same price.
8. Something the business does not do — "not applicable" handled politely.

Fix the export for every wrong, missing or invented answer, then run the failed ones again.

**Live check (the owner, after setting the assistant up).** Give the owner these same questions to
send to the running assistant from a personal phone or test chat, before customers do. On Endelir:
switch on AI Brain → Sandbox & drafts (replies become drafts in the inbox, nothing reaches the
customer), message the business's WhatsApp number, and read the drafts. A wrong or missing answer
there, with correct content, means the platform did not find or use it: tell the owner to bring the
question back here or to their platform's support.
