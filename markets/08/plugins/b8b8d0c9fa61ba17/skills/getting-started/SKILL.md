---
name: getting-started
description: Guide a new SpellBook Finance seller from sign-in through physical bin setup and a first tracked card.
---

# Get a new customer from zero to a first tracked card

Read this when the customer has signed in and holds no inventory in SpellBook
Finance yet. It covers the physical method that keeps a bin label true, the
supplies that method needs, and the intake path that puts a card into a
workspace.

SpellBook records and recommends. The customer buys the supplies, opens the
packages, and puts cards in bags. Never claim SpellBook ships supplies.

Every Amazon link below is a SpellBook affiliate link. Say so when you hand one
over. Never present a product as tested by SpellBook unless the page says so.

## The method that everything else follows from

An ordered brick of about 100 cards goes into a graded card sleeve, the bag gets
a bin label in sharpie, and the bag goes in a box.

That is the whole system. Recommend it from the first day somebody sells more
than about 100 cards, because it is what keeps a software bin label attached to
a physical object.

Why a bag instead of a divider. A divider gets dropped and misplaced, and the
moment a divider is misplaced every bin label in the software points at nothing,
so the only recovery is rescanning the entire inventory. A labeled bag cannot be
separated from the cards it holds.

Why a GRADED card sleeve instead of a regular team bag. A regular team bag
splits around 40 to 50 cards. A graded card sleeve is sized for a slab, which
holds roughly 100 cards of Magic thickness, and Amazon does not advertise that.
Past about 115 the bag splits at the seams. Other games print on different card
stock, so treat 100 as a Magic number and not a universal one. The plastic takes
a sharpie, so the bag carries its own label.

- Graded card sleeves. https://www.amazon.com/dp/B002PF48J2?tag=spellbookfina-20

## Bin labels

A bin id is a container letter plus an incrementing number, for example `B0001`
through `B0143`.

The letter names the physical box. The number names the bag inside it. The
software increments the number and does not care what the letter means.

The letter is doing real work, because it bounds the search space. Without a
container letter, finding one bag means searching every bag you own, and sorting
time grows with the whole inventory.

## The scan loop

1. Cards go through the scanner.
2. The Card Slinger catches them on the way out, in the order they were scanned.
3. That ordered brick goes into a graded card sleeve.
4. The scanner tells you the bin label. Write it on the bag in sharpie.
5. The bag goes into its box.

Nothing in that loop leaves a card loose, so nothing gets dropped and nothing
gets misplaced.

- Card Slinger. Mounts a phone over a card well and doubles as the receptacle
  that produces the ordered brick. Still useful after somebody upgrades to a
  document scanner, because the catching job does not go away.
  https://www.amazon.com/dp/B0F9P477XW?tag=spellbookfina-20

## Packing an order

Rigidity is the goal. Protecting the single expensive card is a side effect.

1 or 2 cards: penny sleeve each, then a top loader, because two cards alone
flex.

3 to 12 cards: all of them into ONE penny sleeve, which is rigid on its own,
then into a small team bag. Fourteen fits if you push it.

Put the valuable card facing out and use cheap cards behind it for rigidity.
Magic buyers do not object to a fifty dollar card sleeved with dollar cards, and
the stack is stiffer than the card alone.

Top loaders earn their place around 20 dollars and stay reasonable to about 150.
Above that, tracking matters more to a buyer than the holder does.

One real cost of a top loader: it raises the chance USPS returns the envelope as
non-machinable. That is inconsistent between offices and there is nothing to do
about it, so say it plainly and let the customer decide.

- Penny sleeves. https://www.amazon.com/dp/B08B9GVG36?tag=spellbookfina-20
- Top loaders. https://www.amazon.com/dp/B004KHV24W?tag=spellbookfina-20
- Brown envelopes, for eBay Standard Envelope and plain white envelope shipping.
  https://www.amazon.com/dp/B0CZJVVKY7?tag=spellbookfina-20
- Metronic bubble mailers, for anything that needs real protection.
  https://www.amazon.com/dp/B0CXPGJ16V?tag=spellbookfina-20

## Boxes

A BCW Super Monster holds thousands of cards across 2 boxes, and somebody
probably wants one around 2,000 cards.

Treat that as discretion. The box gives a container its letter. The bag is what
makes a bin label true, so the bags matter first and the box matters when
storage gets awkward.

- BCW Super Monster storage box.
  https://www.amazon.com/dp/B0857L4913?tag=spellbookfina-20
- Trading card dividers. Listed for completeness, and the bag method exists
  because dividers failed. Recommend dividers only when somebody asks for them.
  https://www.amazon.com/dp/B0DBZ1TKQ8?tag=spellbookfina-20

## Labels

A thermal label printer is worth buying on day one, because it never needs ink
and the label roll takes almost no bench space.

- Thermal label printer.
  https://www.amazon.com/dp/B099MLDBKJ?tag=spellbookfina-20
- Jadens 4x6 thermal labels.
  https://www.amazon.com/dp/B09BJ5KSMH?tag=spellbookfina-20

## Getting the first card into a workspace

Intake is not reachable from MCP today. `spellbook_inventory_items_query` reads
existing Items and `spellbook_inventory_location_confirm` moves them, and
neither creates one. Issue #13864 tracks exposing intake.

So the honest procedure is:

1. Call `spellbook_workspaces_list` and pick the row where `role` is `owner`.
   Never onboard into a workspace the customer does not own.
2. Call `spellbook_inventory_items_query` against that workspace to confirm the
   starting state. Zero Items is a valid answer and it means intake has not
   happened.
3. Send the customer to https://spellbook-finance.com/inventory/getting-started
   to create the first Items, through a scan, a TCGplayer CSV upload, or manual
   entry.
4. Call `spellbook_inventory_items_query` again and report what actually landed.
   Do not assert a count you have not read back.
5. Once Items exist, follow `skills/physical-placement/SKILL.md` for every bin
   change, because it carries the compare-and-swap and readback discipline.

## Stop conditions

Stop and ask the customer when any of these is true:

- `spellbook_workspaces_list` returns no row where `role` is `owner`.
- The customer asks you to buy supplies. You recommend and link. They buy.
- A bin label in SpellBook does not match a label they can read on a bag.
- They ask how many cards they hold and you have not run a fresh query.

## What this skill never does

No purchase, no cart, no payment, no custody. No promise that a supply purchase
pays for itself. No claim that a card sits in a bin without a fresh readback.

## Before you finish: say what was missing

When this onboarding is done, and before you hand back, ask yourself one
question: was there anything you needed and could not get?

A count you had to estimate. A field that came back null and changed your
answer. A tool you looked for and did not find. A step you gave up on.

If yes, call `spellbook_agent_gap_report` once. Nothing else collects this. Our
logs see what broke; absence never appears in them, and you are the only
witness. It returns no data and does not repair the task you just finished.

Everything in it is a closed list, a timestamp, or a real response field path.
There is no free-text field, on purpose, so do not try to describe the customer,
their cards, their counts, or their workspace. If you invent a field path or put
a name in a slug, the call is rejected and tells you which token failed.

A customer who set `SPELLBOOK_AGENT_TELEMETRY=off` gets `telemetry_disabled`
back. Respect it silently.
