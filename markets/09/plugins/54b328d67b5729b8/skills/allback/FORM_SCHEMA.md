# AllBack form schema

The agent sends this JSON to create a form. The MCP tools `create_request` and `create_form` take it as `form`.
Source of truth: `src/shared/schema.ts`. The server rejects a form with a clear error when a reference or value is wrong.

## Minimal form

```json
{
  "title": "Speaker details",
  "blocks": [
    { "id": "full_name", "type": "short_text", "label": "Full name", "required": true },
    { "id": "headshot", "type": "file", "label": "Headshot", "accept": ["image/*"] }
  ]
}
```

`blocks` is a shortcut for one page. Use `pages` for steps and paths.

## Style: "make it like …"

| The user says | Set |
|---|---|
| "like Tally", "simple", "like a doc" | `theme.preset: "paper"` (layout `classic`) |
| "like Typeform", "one question at a time", "conversational" | `theme.preset: "focus"` (layout `conversational`) |
| "dark", "sleek" | `midnight` |
| "warm", "friendly" | `sunrise` (conversational, serif) |
| "calm", "green", "nature" | `forest` |
| "brutalist", "techy", "monospace" | `mono` |
| "playful", "soft", "purple" | `lavender` (conversational, centered) |
| "corporate", "blue", "trustworthy" | `ocean` |

Override any token after the preset: `background`, `surface`, `text`, `muted`, `accent`, `accentText`, `border`, `error` (hex colors), `font` and `headingFont` (`system`, `inter`, `grotesk`, `serif`, `rounded`, `mono`), `radius` (`none` … `full`), `surfaceStyle` (`card`, `plain`), `align` (`left`, `center`), and `logo`, `cover`, `backgroundImage` (https URLs, or paths on our site like `/demo/venue-cabin.svg`).
Set `layout` to force `classic` or `conversational` with any preset.

## Field types

| Type | Answer value | Options |
|---|---|---|
| `short_text`, `long_text` | string | `minLength`, `maxLength`, `placeholder` |
| `email`, `phone`, `url` | string | validated format |
| `number` | number | `min`, `max`, `step`, `unit` |
| `choice` | option id, or list of ids | `options` (strings or `{id, label, image}`), `multiple`, `minSelect`, `maxSelect`, `allowOther`, `display` (`auto`, `list`, `dropdown`, `cards`), `shuffle` |
| `yes_no` | boolean | `yesLabel`, `noLabel` |
| `rating` | 1…max | `max` (3–10), `icon` (`star`, `heart`, `thumb`, `bolt`) |
| `scale` | min…max | `min` (0 or 1), `max` (≤10), `minLabel`, `maxLabel`. NPS = 0–10. |
| `ranking` | list of option ids | `options` |
| `matrix` | `{rowId: columnId}` | `rows`, `columns` |
| `date`, `time` | `YYYY-MM-DD`, `HH:MM` | `min`, `max` (date) |
| `file` | list of file ids | `multiple`, `maxFiles`, `accept` (`image/*`, `application/pdf`, …), `maxSizeMb` (≤25) |
| `signature` | list with one file id | — |
| `consent` | `true` | `text` (markdown links allowed) |
| `hidden` | string | value comes only from prefill; never shown |

All fields take `id` (lowercase, `_`), `label`, `description`, `required`, `showIf`.
Content blocks: `heading`, `text` (markdown: `**bold**`, `*italic*`, `[link](https://…)`), `divider`, `image` (`src`), `document`.

### Document (read and confirm)

```json
{ "type": "document", "id": "doc_policy", "title": "Travel policy 2026", "body": "# Booking\n- Book 14 days ahead", "required": true }
{ "type": "document", "id": "doc_handbook", "title": "Handbook", "src": "https://example.com/handbook.pdf", "required": true }
```

- Give `body` (markdown with `#` headings, `-` and `1.` lists, paragraphs) or `src` (an https link or a same-site path). A PDF link shows inside the form, with an "Open in a new tab" link.
- `id` is optional. Without it, the id comes from the title (`doc_travel_policy`).
- `required: true`: a text document counts as read when the person scrolls to the end. A linked document counts when it stayed on screen for 3 seconds or the person opened the link. The server checks this again on submit.
- Pattern: a required document, then a required `consent`, then an optional `signature`. `get_status` lists who read each document.

## Logic

**Show a field only when …** — `showIf` on any block:

```json
{ "id": "workshop_size", "type": "number", "label": "Seats", "showIf": { "field": "format", "op": "eq", "value": "Workshop" } }
```

**Paths** — `next` on a page. The first matching rule wins. No match goes to the next page.

```json
{ "id": "travel", "blocks": [...], "next": [{ "if": { "field": "needs_travel", "op": "eq", "value": false }, "to": "extras" }] }
```

`to` is a page id, `"end"`, or `"end:<ending id>"`.

**Conditions** nest: `{ "all": [...] }`, `{ "any": [...] }`, `{ "not": {...} }`.
Operators: `eq`, `neq`, `in`, `not_in`, `contains`, `not_contains`, `gt`, `gte`, `lt`, `lte`, `empty`, `not_empty`.
Choice values match by option id or label, without case. Use `recipient.name`, `recipient.first_name`, `recipient.email` as fields too.

**Endings** — a jump like `"end:regrets"` picks that ending. Otherwise: the first ending whose `showIf` matches, else the first ending without `showIf` that no jump points to:

```json
"endings": [
  { "id": "fan", "title": "You made our day!", "showIf": { "field": "nps", "op": "gte", "value": 9 } },
  { "id": "default", "title": "Thanks for your feedback." }
]
```

## Endings: what happens after people send

An ending needs only `title`. It can also have:

| Key | What it does |
|---|---|
| `text` | Markdown under the title. |
| `blocks` | Content under the text: `heading`, `text`, `divider`, and `image` blocks (no `showIf`). |
| `buttons` | Up to 3: `{ "label", "url", "style": "primary"\|"secondary", "kind": "link"\|"booking"\|"payment" }`. |
| `summary` | `true` shows the person their own answers. |
| `pdf` | `true` adds "Download PDF". The receipt email then has the PDF attached. |
| `redirect` | `{ "url", "after": 5 }`: go to the URL after 0 to 60 seconds. The page shows a countdown and "Stay here". |
| `email` | `{ "subject", "text" }`: send the person a copy of their answers with this text. See "After people answer". |
| `next` | `{ "request_id", "label" }`: the next request or form of a flow. Answers to fields with the same id go over as prefill. |
| `share` | `true` (forms only): the open link and a QR code, so people can pass the form on. |
| `ai` | `{ "prompt": "Give 3 next steps from their answers" }`: an AI text from the answers, under the ending text. Pro and Business plans. The text never has links or addresses. |
| `custom` | `{ "html", "css", "js" }`: a fully custom ending page. See "Custom design". |

Links (`buttons`, `redirect`) must be `https`. Piping works in the path and the query, never in the host: `"https://acme.com/welcome?plan={{plan}}"`.
Piped values are URL-encoded. `kind: "booking"` adds the person's name and email to Calendly and Cal.com links.
`kind: "payment"` adds the email to Stripe Payment Links, and the answer id as `client_reference_id`.

```json
"endings": [
  {
    "id": "yes", "showIf": { "field": "attend", "op": "eq", "value": "Yes" },
    "title": "See you there, {{full_name}}!", "text": "Doors open at 18:00.",
    "buttons": [
      { "label": "Book a 1:1 slot", "url": "https://cal.com/acme/intro", "kind": "booking" },
      { "label": "Event page", "url": "https://acme.com/event" }
    ],
    "summary": true, "pdf": true,
    "email": { "subject": "Your RSVP", "text": "Thanks {{full_name}}! Here is what you told us." }
  },
  { "id": "no", "title": "Sorry you cannot come", "redirect": { "url": "https://acme.com/recordings", "after": 5 } }
]
```

Safety: buttons, redirects, email texts, AI prompts, and custom endings get the same AI safety check as custom pages.
A high risk is refused when the form is saved. Until the check says low risk, a redirect waits for a click.
Before the claim, people see only the title, the text, and the content of an ending.

Each ending has its own preview link: `ending_previews` in `get_request` and `get_form`, or add `&ending=<id>` to the `preview_url`.

## After people answer

These are settings of the request or form, not part of the form JSON. Set them in `create_request`, `update_request`, `create_form`, `update_form`, or in the Settings tab.

- `receipt: true` emails each person a copy of their answers, with a link to change them. An ending with `email` sends one too, with its own text.
  - A request sends it to the email on the list.
  - A form sends it only to people who confirmed their email with a code. Turn on `verify_email` for that: people then type their email and confirm it before they answer.
- `notify` emails the owner: `"each"` (one email for each answer), `"daily"` (one summary a day), `"done"` (requests only: one email when everyone on the list is done), or `"off"`.

## Piping

Use `{{field_id}}` or `{{recipient.first_name}}` in titles, labels, descriptions, and endings: `"Thanks {{full_name}}!"`.

## Conversational extras

- `welcome: { "text": "...", "button": "Start" }` sets the first screen.
- A page with `"group": true` shows all its fields on one screen, not one per screen. Use it for related short fields (name + email).

## Settings

`settings.submitLabel` (default "Submit"), `settings.showProgress` (default true), `settings.highlightPrefill` (default true).

## Custom design (optional)

Only when the user asks for a fully custom look. Guests can build it, but before the claim only the preview shows it: people see the standard form until someone confirms their email.

**Level 1, custom CSS** on top of the normal form:

```json
"custom": { "css": ".ab-btn { border-radius: 0; background: #ff0080; }" }
```

Useful classes: `.ab-shell`, `.ab-main`, `.ab-sheet`, `.ab-h1`, `.ab-lead`, `.ab-q`, `.ab-input`, `.ab-btn`, `.ab-choice-row`, `.ab-error`.
For endings: `.ab-ending`, `.ab-ending-ai`, `.ab-ending-actions`, `.ab-ending-btn`, `.ab-ending-summary`, `.ab-ending-redirect`, `.ab-ending-share`.
`url()` works only with `data:image/…`. `@import` is not allowed. The CSS can load nothing from outside.

**Level 3, a fully custom page** in a sandbox:

```json
"custom": { "html": "<input id=nm><button id=go>Send</button>", "css": "…", "js": "go.onclick = async () => { await allback.set('full_name', nm.value); await allback.submit(); }" }
```

- Keep the normal `blocks`. They define the fields, the checks, the export, and the "Standard view" that people can always open.
- The page runs in a sandbox with no network: no `fetch`, no outside scripts or images, no links away, no cookies or storage.
- The only way to save answers is `window.allback`:
  - `await allback.ready()`: `{ form, fields, answers, recipient, dueAt, preview }`, with the prefill in `answers`.
  - `await allback.set(fieldId, value)`: `{ ok, error }`. Choice answers can be the option id or its label.
  - `await allback.upload(fieldId, file)`, `await allback.documentRead(docId)`, `allback.standardView()`.
  - `await allback.submit()`: `{ ok, errors, ending }`. The same server checks as for every form.
    `ending` has the parts of the ending: `title`, `text`, `buttons`, `summary`, `redirect`, `pdf`, `next`, `ai`.
  - `allback.open(url)`: after the submit, open one of the ending's own links (a button, the redirect, the next step, or the PDF). Other URLs do nothing.
- Images: use `data:` URIs.

**A fully custom ending** uses the same sandbox, also on a form without a custom page:

```json
{ "id": "done", "title": "Thanks", "buttons": [{ "label": "Visit", "url": "https://acme.com" }],
  "custom": { "html": "<h1 id=t></h1><button id=go>Visit</button>", "js": "allback.ready(({ ending }) => { t.textContent = ending.title; go.onclick = () => allback.open(ending.buttons[0].url); });" } }
```

- `await allback.ready()`: `{ ending, form, recipient, preview }`. `ending` is the same as in `submit()` above.
- `allback.open(url)` opens one of the ending's own links. `allback.edit()` goes back to the form.
- Pages that ask for passwords, codes, card numbers, or bank details are refused.
- An AI safety check runs on every change of the custom code or of the endings. The result decides what people see:
  - Low risk: the page shows with no bar. Free plans show the AllBack badge in the corner.
  - Medium risk: a warning banner above the page shows "Standard view" and "Report".
  - High risk: the code is not saved, and the error gives the reasons.

