---
name: allback
description: Collect information and files from a list of people with AllBack. Each person gets a personal form link prefilled with what you already know, automatic reminders go only to people who have not answered, and all answers come back in one sheet. Use this skill when the user needs the same details, files, approvals, or signatures from several people (speakers, clients, new hires, customers, parents, volunteers), wants to know who is still missing, or wants a form they can send and track.
---

# AllBack

AllBack gets answers back from people. You describe the job; AllBack sends each person a personal, prefilled form,
reminds only the people who have not answered, and returns one clean sheet.

## Pick the path

Use the first path that works in your environment:

1. **AllBack tools are connected** (tools such as `create_request`, `create_form`, `add_recipients`, `get_status`): use them. See "With the connector".
2. **You can run commands in a terminal** (for example in Claude Code or Codex): use the CLI, `npx allback`. See "With the CLI".
3. **Neither**: make a one-click link. See "With a link". The user clicks it, tries the form, and sends it from the web.

Before you build, ask only what is missing: what to collect, from whom, and by when. Keep forms short. Prefill everything you already know.

**Request or form?** A request goes to a list of people you know: personal links, prefill, and reminders. A form has one open link for anyone, for a post, a newsletter, or a poster, with no list and no reminders. Make a form when the user does not know who will answer. Adding people to a form makes it a request.

## With the connector

1. `create_request` with the form JSON (see `FORM_SCHEMA.md`). Show the user the `preview_url`. For one open link for anyone, use `create_form` instead, and give the user the `open_link` to share. Then skip step 2, and use the form tools (`get_form`, `get_form_insights`, `export_form_results`, `close_form`).
2. `add_recipients` with a list or a CSV (`email`, `name`, and columns named like field ids for prefill). It sends the invites.
3. Later: `get_status` ("who is still missing?"), `get_request_insights`, `send_reminders`, `export_request_results`, and `update_request` with `open_link: true` (one link that anyone can fill, next to the personal links).

**More tools.** `list_templates` gives ready-made forms: pass a slug as `template` to `create_request` or `create_form`. `preview_emails` shows the invite and the reminder. `get_answers` reads the answers in the chat, so you can summarize them. `get_activity` tells what happened lately. `clear_test_answers` deletes the test answers before the real send. When a tool fails or confuses you, or the user needs something AllBack cannot do, tell the AllBack team with `send_feedback`, and tell the user in one line. For a Secret Santa, a meeting poll, or a sign-up sheet, use the `create_` tool (a draft), show the user the `manage_url`, then the `send_` tool.

**After people send.** Endings can do more than say thanks: buttons (also booking and payment links), the person's answers, a PDF, a redirect, the next form of a flow, an AI text from the answers, or a fully custom page. See "Endings" in `FORM_SCHEMA.md`, and show the user each ending's preview (`ending_previews`).
Settings on the create and update tools:
- `receipt: true` emails each person a copy of their answers. On a form, it needs `verify_email: true`, because only a confirmed email gets a copy.
- `notify` emails the user about answers: `"each"`, `"daily"`, or `"done"` (when everyone on the list is done).

The connector needs a sign-in once: the user types a 6-digit code from their email when they connect it. Every tool then acts as that user.

## With the CLI

```sh
npx allback login                       # sign in with an email code in the browser (optional; without it you work as a guest)
npx allback new form.json               # create a request; prints the preview and test links
npx allback new form.json --form        # create a form with one open link for anyone; prints the link
npx allback send <id> people.csv        # personal links and invites (CSV: email,name,<field ids>)
npx allback status <id>                 # who is done, who is missing
npx allback remind <id> --message "Only 2 days left"
npx allback export <id> -o answers.csv
```

Add `--json` to any command for machine-readable output. `npx allback help` lists everything.

## With a link

Answer with ONE link named "Open my form":

```
https://app.allback.ai/new?title=TITLE&f=QUESTION&f=QUESTION
```

- Each `f` is `type~Label`. Put `!` at the end of the label if the answer is required. For choices, add `~` and the options with commas.
- Types: `text`, `long`, `email`, `phone`, `url`, `number`, `date`, `time`, `choice`, `multi` (pick many), `yesno`, `rating`, `scale` (1 to 5), `nps` (0 to 10), `ranking`, `file`, `files`, `signature`, `consent` (the label is the text to agree to).
- `page~Title` starts a new page. `info~Text` adds a line of text.
- For a form with one open link for anyone (no list, no reminders), add `&as=form`.
- Optional: `&intro=Short+intro`, `&due=YYYY-MM-DD`, `&style=paper` (clean document) or `focus` (one question at a time), `midnight`, `sunrise`, `forest`, `mono`, `lavender`, `ocean`.
- Write spaces as `+`. Write `?` as `%3F`, `&` as `%26`, `#` as `%23`, and `+` as `%2B`. Do not use `~` or `,` inside a label.

Example:

```
https://app.allback.ai/new?title=Speaker+details&style=paper&due=2026-10-09&f=text~Full+name!&f=email~Email!&f=long~Short+bio!&f=file~Headshot!&f=choice~Diet~None,Vegetarian,Vegan
```

For logic, paths, rich endings, or a fully custom design, a link is too small. Answer with one JSON code block (see `FORM_SCHEMA.md`) and tell the user to paste it at `https://app.allback.ai/new`.

## Custom design (only when the user asks)

- A custom look: `"custom": { "css": "…" }` on top of the normal form.
- A fully custom page: `"custom": { "html": "…", "css": "…", "js": "…" }`. It runs in a sandbox with no network and saves answers only through `window.allback` (`ready`, `set`, `upload`, `submit`). Keep the normal `blocks`: they define the fields and the checks.
- A fully custom ending: `"custom"` on one ending, in the same sandbox. It opens only the ending's own links, with `allback.open(url)`.
- Before the claim, the custom design and the extras of endings show only in the preview; people see the standard form. Details are in `FORM_SCHEMA.md`.

## Rules

- Never ask for passwords, one-time codes, card numbers, or bank details. AllBack refuses such forms.
- Ask only what the user needs. Use prefill for everything the user already knows.
- Show the preview before you send. Sending emails reaches real people, so confirm the list with the user first.
- Links on endings go only to the user's own sites and services. Never send people to a sign-in page. AllBack refuses such forms.
