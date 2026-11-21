# Endelir export

How to turn the dossier (dossier-format.md) into the files for an assistant that runs on Endelir —
the WhatsApp AI agent — with Endelir's exact fields, limits and a worked example. Every limit here is
one Endelir enforces; text over a limit is cut off without warning.

## How Endelir's AI uses each part

| Part | Where it goes in Endelir | Limit | Why the limit matters |
|---|---|---|---|
| A. AI instructions | AI Brain → AI Settings → System Prompt | 3,800 characters | Endelir keeps the first 1,000 tokens and cuts the rest. The cancellation policy at the end is what gets lost first. |
| B. Service answers | AI Brain → Service answers (5 fields) | 300 characters each | Shown to the AI on every customer-service reply; the screen stops at 300. |
| C. Handbook | AI Brain → AI Settings → upload `handbook.txt` | 50,000 characters per document (Endelir cuts the rest); aim for 45,000 | The AI searches it for each question. One document where it fits: search does not connect facts across documents. |
| D. Sales agent (internal) | AI Brain → Sales agent (offers, questions, gives) | Products typed in one by one | The AI sells only what is listed and never goes below the lowest price. The ONLY place lowest prices go. |
| E. Quick answers | QnA (one per keyword, match type Contains) | Up to eight | With the AI on, they answer only messages of three words or fewer. |

**The price check.** Before a reply is sent, Endelir checks every rupee figure and percentage in
it against the business's own text. It accepts a figure found in: the AI instructions (A); the
service answers (B); the Sales agent settings (D's gives and advance); the handbook (C) and website
pages, but only the passages its search found for that question; the ad the customer tapped; and the
results of the AI's own lookups (product search, order status). A figure in none of them is blocked
and the chat goes to a person. So a price in A can always be quoted; a price only in C, only when
search finds it. Put every price in A that fits, written exactly as in C (the rule for long lists is
below). Totals worked out in the reply are allowed when the working is shown ("₹700 each, so ₹1,400
for two").

**Language.** The AI answers in the customer's language (English, Hindi, Gujarati, Tamil and so on)
and answers Hinglish in English. The files stay in English; put the words customers really use,
including Hindi or regional ones, in the handbook's brackets so search finds the right section.

## Format of each part

### A. AI instructions (System Prompt)

Plain paragraphs, in this order, under 3,800 characters (count with code):

1. One line: who the assistant is, for which business, where, and its tone.
2. How to qualify: what to ask before suggesting or quoting.
3. PRICE LIST: every price, grouped, written as in the handbook.
4. KEY FACTS: address and landmark, timings, delivery or service area, payment, codes or offers.
5. CANCELLATION / RETURNS: one short paragraph.
6. NEVER: the business's never-say and never-promise rules (dossier section 10), one line each.
7. WHEN UNSURE: what to say and when to hand over (dossier sections 11 and 14).

If it does not fit, follow the one rule in dossier-format.md ("Large price lists"): shorten
wording first; then keep the prices customers ask about most, leave the rest in the handbook, and
say in endelir-setup.txt how many prices are in the handbook only. Never put lowest prices,
margins or negotiation rules here; they belong in D only.

### B. Service answers

Five lines, each under 300 characters: Returns & refunds · Delivery · Warranty · Opening hours ·
Payment. For one that does not apply, say so plainly ("We do not deliver; visit us at …"), or
leave the field empty — never a placeholder.

### C. Handbook (`handbook.txt`)

- Title line: business name, what it is, city.
- Sections with headings in CAPITALS, each followed by the customer's words in brackets.
- Prices written exactly as in A. Policies in full. FAQs as plain question-and-answer pairs.
- No marketing copy, no customer names or numbers, no lowest prices.
- Over 45,000 characters: split by whole, self-contained sections into the fewest files
  (handbook-1-products.txt, handbook-2-policies-and-faq.txt), as in dossier-format.md ("A knowledge
  file that is too long"), and upload each. Never cut inside a section — a single section over the
  limit is split by sub-topic, conditions repeated in each part, as that rule describes. List the
  files in endelir-setup.txt.

### D. Sales agent (internal)

- **Offers:** one line each — name · price · lowest price · one-line description.
- **Qualifying questions:** three, one per line.
- **Gives:** non-cash, one per line, offered before any discount.

### E. Quick answers

`keyword — reply`, one per line, keywords a single word or two (location, timings, menu, cod).

## Worked example — Mosorb Coffee Co. (a demo business)

### A. AI instructions (excerpt; the real one is about 2,600 characters)

```
You are Kavi, the assistant for Mosorb Coffee Co., an online store selling fresh-roasted Indian specialty coffee from our roastery in Hauz Khas, New Delhi. We ship across India. Be warm and brief, like a good barista. Ask how they brew (espresso, moka pot, French press, South Indian filter, pour over, AeroPress, or no equipment) and how they take it (black or with milk), then suggest one coffee and a size.

COFFEE (250 g / 500 g / 1 kg): Attikan Estate, medium-dark, nutty, good with milk ₹700 / ₹1,300 / ₹2,380; Kerehaklu Estate, light, bright and citrusy, best black ₹850 / ₹1,580 / ₹2,890; ...
GIFTS: Little Box of Love ₹1,299; Big Box of Comfort ₹1,899. CORPORATE DIWALI GIFTING, 25 boxes or more: the Big Box of Comfort at ₹1,699 a box with your logo sleeve, shipped to each person's address; order by 25 Oct for delivery before Diwali.

KEY FACTS: we roast Monday to Friday and ship the next working day; weekday orders before 9 am ship the same day. Delivery 2 to 5 working days. Shipping free above ₹999, otherwise ₹79. Cash on delivery for orders up to ₹5,000, with a ₹49 fee. First order: code FIRST10 for 10% off. ...
RETURNS: not happy with a coffee? Tell us within 21 days of shipping for a replacement or a full refund, and send the pack back. 1 kg packs returned for taste get 50% back. Gear is refunded only if returned new and unused.
```

### B. Service answers

```
Returns & refunds: Within 21 days of shipping: a replacement or a full refund on any coffee (send the pack back). 1 kg packs returned for taste: 50%. Gear only if new and unused. Refunds start within 3 days.
Delivery: Roasted Monday to Friday, shipped the next working day; weekday orders before 9 am ship the same day. 2 to 5 working days across India. Free shipping above ₹999, otherwise ₹79.
Warranty: Brewing gear: warranty repairs at our Delhi roastery; we pay the delivery back to you.
Opening hours: Support 9 am to 6 pm, Monday to Saturday. The store takes orders any time.
Payment: UPI, cards, net banking, or cash on delivery up to ₹5,000 (₹49 fee).
```

### C. Handbook (excerpt)

```
MOSORB COFFEE CO. — COFFEES, GEAR, SHIPPING AND RETURNS. Fresh-roasted Indian specialty arabica, sold online from our roastery in Hauz Khas, New Delhi, shipped across India.

WHICH COFFEE (recommend, suggest, best for, strong, mild, milk, black, kaunsi coffee). Espresso or moka pot with milk: Attikan Estate or the House café blend. Strong and bold: Vienna Roast or French Roast. Black, pour over or AeroPress: Kerehaklu Estate. No equipment: Easy Pour sachets or cold brew.

SHIPPING AND PAYMENT (delivery, dispatch, COD, cash on delivery, shipping charge, delivery kab tak). Weekday orders placed before 9 am ship the same day. Delivery takes 2 to 5 working days. Free shipping above ₹999, otherwise ₹79. Cash on delivery for orders up to ₹5,000 with a ₹49 fee.
```

### D. Sales agent (internal)

```
Offers:
Attikan Estate coffee, 250 g · ₹700 · lowest ₹700 · Medium-dark, nutty and chocolatey.
Big Box of Comfort (gift) · ₹1,899 · lowest ₹1,699 · Easy Pour sachets, a mug and cookies.
Qualifying questions:
How do you brew your coffee?
Do you take it black or with milk?
Is it for you or a gift?
Gives:
Free shipping on this order
A free pack of 5 Easy Pour sachets
```

### E. Quick answers

```
cod — Yes — cash on delivery for orders up to ₹5,000, with a ₹49 fee.
shipping — Free shipping above ₹999, otherwise ₹79. Delivery takes 2–5 working days across India.
```

### open-items.txt (not an export)

```
[ ] Delivery time to the North-East — the website does not say. Until answered, the AI says the team will confirm.
[ ] Lowest price for the espresso machine — owner to decide in Sales agent.
```

## About Endelir (if the owner asks)

Endelir runs a business's WhatsApp: an AI agent that answers customers, quotes from the business's
own prices, takes bookings and orders, recovers abandoned carts, and hands the chat to the team when
needed. Sign in at dashboard.endelir.com. Part A goes in AI Brain → AI Settings → System Prompt, B in AI Brain →
Service answers, C is uploaded in AI Brain → AI Settings, D in AI Brain → Sales agent, E on
the QnA page.
