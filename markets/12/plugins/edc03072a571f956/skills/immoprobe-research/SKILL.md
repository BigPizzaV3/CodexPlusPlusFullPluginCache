---
name: immoprobe-research
description: Analyse German residential investment listings (Kapitalanlage-Immobilien) with the Immoprobe MCP tools. Map an exposé, a portal page or pasted text to the calculator input, look up the land value (Bodenrichtwert), calculate cashflow, yields and tax effect, write an assessment note with questions for the Makler, and save the object to the user's Immoprobe list; sweep a saved portal search for new listings; review and compare what is saved. Use when the user shares a listing URL, an exposé PDF or text, a portal search, or asks about their saved properties.
---

# Immoprobe research

Immoprobe is the user's system of record for German residential investment
properties and a deterministic calculator. It runs no model of its own: you
read the listing, Immoprobe does the maths, keeps the objects and answers the
geodata from public sources. You work with the `immoprobe` MCP server; if it is not
connected, tell the user how: claude.ai → Settings → Connectors → add
`https://api.immoprobe.de/mcp`; Claude Code →
`claude mcp add --transport http immoprobe https://api.immoprobe.de/mcp`.

## The tools

| Tool | Use it to |
|---|---|
| `get_guide` | the field mapping and how to read every layer — read it once per conversation |
| `calculate_property` | run the calculation for one input; free, but like every tool it needs the user's free account |
| `lookup_address` | find where a listing is and the Bodenrichtwert at the point |
| `save_object` | keep a listing with its input, address, note and lists |
| `find_objects` | list saved objects as compact rows, by status, list, source or text |
| `get_object` | one object in full: input, assumptions, notes, links, attachments, land value |
| `clone_object` | save a copy with other financing or a negotiated price, to compare the variants |
| `add_note` | append a note to a saved object |
| `add_link` | attach a further page of the flat: another portal, the developer, a plan |
| `add_attachments_from_urls` | fetch the listing's photos, Grundriss and a linked PDF into the object by URL |
| `set_object_status` | into the trash (discarded) or back to the list (active) |
| `set_object_lists` | file an object under list names |
| `check_known_listings` | which listing ids are already saved — the sweep cursor |
| `compare_objects` | two to five objects side by side, best value marked |
| `get_account` | who is connected, plan, what is left of the quotas |

Every answer that concerns an object carries a `url` into the web app — show
it. `calculate_property` carries `shareUrl` with charts — show it too.

## Reading a listing

Call `get_guide` once per conversation before the first calculation (or read
`immoprobe://guide`): it carries the field mapping from a listing to the
calculator — Kaufpreis, Wohnfläche, Kaltmiete, Hausgeld, Provision, Baujahr,
the state from the postcode, financing, KfW, a new build's Bauphase, the plot
for the Kaufpreisaufteilung — with units and defaults, and how to read every
layer `lookup_address` answers. The server serves the guide, so it is always
the current contract; this skill is the procedure around it.

Take what the listing states; leave out what it does not. Fields left out
take defaults and come back in `assumed` — show them to the user as
assumptions, never as facts. Pass a stated value even when it equals the
default (a Provision of 3.57 %, say): left out, it would come back as an
assumption although the listing says it. The answer's `summary` lines are the
calculation as facts, a `*` on every assumption: quote them instead of retyping
numbers. Pass `language` (de or en, the user's language) to every tool that
takes it; for any other language pass en and translate yourself. A value you
estimated yourself (a typical Hausgeld, a guessed rent) is an assumption as
well: put its name into `assumed` when you save.

## Locating the listing

Call `lookup_address` before calculating: with `lat` and `lng` when the page
shows the point (ImmoScout24 does on the exposé map — free and exact),
otherwise the address as the listing writes it. Several candidates: ask the
user which, then call again with its `candidateId` (free). `approximate: true`
means the house number was unknown — present the values as assumptions and
say why. A missing layer means no data there: say so, never guess a land
value. Pass `layers.brw.eurPerSqm` and `gfz` on to `calculate_property` as
`landValuePerSqm` and `floorAreaRatio`, with `plotArea`, `coOwnershipShare`
and `coOwnershipTotal` from the listing. Show `attribution` next to every
value — the licences oblige it. What each layer means and what to tell the
user about it is in the guide.

## Calculating and presenting

Call `calculate_property` with the extracted input. Present, in this order:
the `verdict` sentence, cashflow per month before and after tax, net yield,
price-to-rent factor, total investment and the loan, the land value, and the
assumptions as a list. Keep the projection to the milestone years the answer
carries; do not invent a forecast.

## Without tools

If the tools are not available to you, hand the user a link instead of a
calculation: `https://immoprobe.de/calculator?purchasePrice=…&livingArea=…&stateCode=…&coldRent=…`
with every field you read by its name, plus `lat`, `lng`, `address`,
`listingUrl`, `title`, `note` (your assessment), `model` (your name) and
`assumed` (the fields you guessed, comma-separated), URL-encoded. The web calculates, looks up the land
value after sign-in and saves the object with your note in one click. Do not
compute the cashflow yourself.

## The note

Draft a note of kind `analysis` from the text — what the numbers do not show.
Write in the language the user writes in. Cover what applies:

- Erbbaurecht, Sondernutzungsrechte, Teilungserklärung
- Instandhaltungsrücklage, Sanierungsstau, Sonderumlagen, WEG-Protokolle
- Denkmalschutz (a depreciation topic), Energieausweis and class
- Mietvertrag: current rent against the Mietspiegel, Leerstand, Staffel- or
  Indexmiete
- Lage as the listing describes it, and what you could verify
- **Fragen an den Makler** — a block of concrete questions

Do not copy the Makler's contact details into a note unless the user asks.
Notes are append-only: correcting one means writing another. Pass an
`idempotencyKey` so a retried call cannot duplicate it.

## Saving

Save with one `save_object` call: the input, the address with the point and
precision from the lookup, `source` and the portal's `externalId` (the number
in `/expose/<id>`), `listingUrl`, the note, and the lists the user names.

- Saving the same source and externalId again updates the object — it never
  duplicates. Nothing keeps the old price: when the listing's price differs from
  the last saved one, save it again and add a note with the old and the new
  price and the date.
- The object is in the user's list at once, marked as saved by you — so every
  guessed field must be in `assumed`. `discarded` is the trash: out of the
  lists, restorable for 90 days, and a sweep does not save the listing again.
- `possibleDuplicates` lists saved objects at the same address. Nothing is
  merged — tell the user and let them decide.
- Found the same flat elsewhere — Immowelt, Kleinanzeigen, the developer's page
  on neubaukompass? `add_link` it to the saved object instead of saving twice.
- After saving, `add_attachments_from_urls` with the file URLs the page shows:
  the photos, the Grundriss (`kind: floorplan`), a linked exposé PDF — the image
  or PDF URLs, not the page. Immoprobe fetches them itself; the same URL is
  never stored twice. What fails (login wall, bot check) comes back in
  `failed` — say so, do not retry in a loop.
- A file on the user's machine cannot come through a tool. Read the PDF, save
  what you read, then say: attach the file on the object's page (the `url` in
  the answer). From Claude Code, `curl -F kind=document -F file=@Exposé.pdf`
  with the token against `POST /v1/objects/{id}/attachments` works too.

## Sweeping a saved search

Open the results page sorted newest first, collect the listing ids, call
`check_known_listings` with them and the source portal, and open only the
unknown ones. Analyse and save each as above. A known one whose price on the
results page differs from the last saved (the answer carries it) is saved again
with the new price plus a note with the old and the new one. Stop when a
whole page is known. One or two pages is a run; finish with a table and what
is left of the quotas (`get_account`).

## The portfolio

`find_objects` for the rows, `compare_objects` for two to five side by side,
`get_object` for the notes. Say which deserve a
viewing and why, what is still unknown per object, and offer to set
statuses, file into lists or add a note of kind `viewing`.

## Conduct on portals

- Read only listings the user opened or asked you to open; work at a human
  pace, a page or two per run.
- Never bypass a captcha, a login wall or an automated-access protection.
  Stop and ask the user.
- Do not contact sellers or agents on the user's behalf.
- Automated access is against the terms of most portals; the user carries that
  responsibility. Keep the volume modest.

## Quotas

Only a call that actually geocodes counts against the monthly quota; lookups
by point, candidate picks and repeated addresses are free. Objects are counted
per plan. `get_account` and every lookup answer say what is left; a refusal
carries the numbers and the reset date.
