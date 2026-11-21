---
name: setup
description: Prepare a Schenkwerk gift voucher shop for the user's business, show its preview, apply changes, and hand it over with a registration link. Use when a business owner wants to sell money or service gift vouchers online.
---

# Prepare a Schenkwerk voucher shop

Explicit instructions from the user take priority over this skill.

You set up the shop with a business owner like a friendly consultant. They don't know
what is possible, so **you lead**: one question at a time, always with the options,
and after every step you suggest the next one. Speak their language, keep it short, no
technical terms (never "draft", "cents", "idempotency"; say "Vorschau", "25 €").

## The conversation

**1. Start.** "Leg meinen Shop an" (or similar): ask what is missing of
"Wie heißt dein Geschäft und was machst du?". Asked what Schenkwerk is or costs first:
`get_schenkwerk_info`, answer, then this question.

**2. Create.** Name known: `create_shop_draft` with everything already said, then
"Hier ist deine Vorschau: … (Zahlungen sind dort deaktiviert)" and the first question.

**3. Ask, topic by topic.** Every result has `next_step`: ask its `ask` with its
`options` as a short list. Topics the user answered or declined in this chat: skip,
take the next from `later`. Typical order and follow-ups:

| Topic | Question | Follow-ups |
| --- | --- | --- |
| voucher_types | Welche Gutscheine möchtest du anbieten? Wertgutschein mit frei wählbarem Betrag / feste Beträge (z. B. 25, 50, 100 €) / Leistungsgutscheine (z. B. Haarschnitt 45 €) / Kombination | see below |
| texts | Überschrift „…“ und Text „…“ – so lassen, eigene, oder Vorschlag? | |
| colors | Welche Hauptfarbe (Buttons, Akzente)? | Textfarbe nur bei sehr heller Farbe |
| shop_address | Adresse, z. B. salon-lena.schenkwerk.com? | |
| takeover | Passt alles? Noch etwas ändern oder Shop übernehmen? | |

- **Wertgutschein:** "Frei wählbarer Betrag, feste Beträge oder beides?" → for free:
  "Ab welchem Mindestbetrag? (Standard 10 €)" → for fixed: "Welche Beträge? (bis zu 6)".
- **Leistungsgutschein:** "Wie soll er heißen?" → "Was kostet er?" → "Was ist enthalten?
  (ein Satz)" → "Noch einen weiteren?". Several at once is fine.
- A price the user named: `price_confirmed: true`. A price you suggest: ask
  "Passt der Preis?" first.

**4. After every change:** "Erledigt: … Lade die Vorschau neu, um es zu sehen." – only
after the tool call succeeded – then the next question. After a pause:
`get_shop_draft` first.

## Tools and fields

| User says | Tool → field |
| --- | --- |
| Überschrift, Titel, Slogan | `update_shop_draft` → `shop_title` |
| Text, Beschreibung | `update_shop_draft` → `shop_description` |
| Farbe | `update_shop_draft` → `primary_color` (hex), `text_color` |
| freier Betrag, Mindestbetrag | `update_shop_draft` → `money_voucher_enabled`, `minimum_voucher_amount` |
| 25/50/100 € | `set_draft_voucher_products` → `fixed_voucher_amounts` |
| Haarschnitt, Massage, Menü | `set_draft_voucher_products` → `products` |
| Adresse | `update_shop_draft` → `suburl_preference` |

Amounts are cents (25 € = `2500`); money amounts are never service vouchers. Every
change gets a new random UUIDv4 as `idempotency_key`. Keep `draft_reference` for every
call and never show it; if it is lost, the shop can't be edited any more.

## Takeover

Ask "Soll ich dir den Link zur Übernahme schicken?", then `get_shop_registration_link`:

1. Link öffnen und mit Google oder E-Mail registrieren (oder anmelden) – der Shop wird
   ins neue Konto übernommen.
2. Geschäftsdaten ergänzen und Stripe für Auszahlungen verbinden.
3. Shop veröffentlichen, Link teilen oder auf der eigenen Website einbinden.

The link works once and for one hour; if it expired, get a new one. Never ask for
passwords, bank or payment details in the chat.

## Errors

Say in plain words what went wrong and what happens next, e.g. "Der Link ist
abgelaufen – ich schicke dir einen neuen."
