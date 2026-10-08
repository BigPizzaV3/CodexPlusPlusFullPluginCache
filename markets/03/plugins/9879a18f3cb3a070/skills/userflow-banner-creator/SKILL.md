---
name: userflow-banner-creator
description: Create an in-app banner in Userflow through a guided, conversational flow — gather context from a short summary, pasted content, attached file, public page, or linked document/ticket in a connected app; draft and refine short banner copy; add an optional CTA; configure placement and behavior; optionally target users; show a confirmation card; create an unpublished draft through Userflow MCP; return the Builder link; and offer to publish. Use whenever a user with Userflow MCP connected asks to create or add an in-app banner, announce maintenance, a promotion, or an update in a page-top or page-bottom bar, or turn a note, ticket, or document into a Userflow banner. Requires the Userflow MCP connector.
---

# Userflow Banner Creator

Guide the user from a rough idea (or a linked doc/ticket) to a finished, ready-to-publish Userflow
**banner** — a bar embedded directly into their app's page. This is a **conversational, step-by-step**
skill: move through the phases in order and **pause at each ✋ checkpoint**. Never create or publish
without an explicit yes.

The core habit, same as any content-creation flow: **create is not publish**. `create_flow` saves an
unpublished draft and returns a Builder link; nothing is live until the user confirms and you call
`set_flow_publication`.

## How banners differ from announcements

Banners embed **directly into the page DOM**, so — unlike announcements — there is **no notification
level** (silent/badge/boosted) and **no Resource Center dependency**. The banner-specific choices are
**placement** (where it sits) and **behavior** (sticky / overlay / animate). Copy should be **short —
one line is ideal**.

## Before you start

1. Confirm the **Userflow MCP** is connected. If not, say so and stop.
2. Resolve the **environment** via `describe_session` (e.g. Production vs. Staging). One env → use it;
   several → ask which. The banner *draft* is account-level, but you'll need the env for the
   live-banner priority check and for publishing.

---

## Phase 1 — Gather the context

Ask for the source material, offering three ways:

> "What's the banner for? Give me a short summary, share a link to a doc or ticket with the context
> (Notion, Jira, a Google Doc, etc.), or paste the content in."

If they share a **link**, use the matching connected app for private content (for example Notion,
Atlassian for Jira/Confluence, or Google Drive), use browser or web access for a public page, and read
files attached to the current task directly. If the required app is unavailable or access fails, say
so and ask them to paste the relevant text. If they give a summary or pasted text, work from that.

Banners carry one short message and maybe one action — pull out the single thing users need to know
and any link/action they should take.

---

## Phase 2 — Draft and refine the copy

Write **short** banner copy — ideally one line. Lead with the point; cut everything else. If a
bundled Userflow brand-copy skill is available, follow its voice rules; otherwise use concise,
direct, friendly product copy and preserve any tone requirements the user provides.

✋ Show the draft (plain, readable — not JSON) and ask:

> "Here's the banner text. Good? Want changes to tone, length, or wording? And should it have a
> **button** — e.g. 'Learn more' linking somewhere, or a 'Dismiss' button?"

If they want a CTA, capture the button text and its action — most commonly **navigate** to a URL, but
also **start a flow**, **dismiss** the banner, track an event, or set an attribute. See
`references/mcp-reference.md` → *Buttons*. Iterate until the copy and button are right.

---

## Phase 3 — Placement and behavior

Banners always need a placement. **Always ask** (offer it as a dropdown of choices):

- **Top of page** → `embed_mode: "body_first"`
- **Bottom of page** → `embed_mode: "body_last"`
- **Anchor to a specific element** → hand off to the Builder (see below)

**Element-anchored placement is finished in the Builder, not here.** The MCP can't click to pick an
element on a live page, so if the user chooses element-anchored, create the draft with the copy and
settings you have and tell them to open the Builder link to position it against the element. Don't ask
for CSS selectors. Top/Bottom of page need no selector and work fully via MCP.

Then a couple of quick behavior questions (offer sensible defaults):

- **Sticky?** Stick to the top/bottom of the viewport while scrolling, or scroll away with the page
  (`sticky`, default false).
- **Overlay or push?** Float over app content, or push the app's content down (`overlay`, default
  false = push).
- Optional: animate on appear (`animate`, default true); allow users to dismiss with an X.

---

## Phase 4 — Audience targeting

> "Should this show to **everyone**, or only a **specific set of users**?"

If targeted, ask them to describe the audience in plain language, then build a `filter_condition` from
the predicate DSL — **resolve real attribute FQNs / event names first via `list_attribute_definitions`
/ `list_event_definitions`; never invent them** — and **echo the interpreted audience back in plain
English** for a ✋ nod. See `references/mcp-reference.md` → *Targeting*. If everyone, leave
`filter_condition` unset.

**Priority — only if other live banners exist.** Check `list_flows` (`types: "banner"`,
`state: "published"`, the chosen `env_id`). Only if that returns one or more, raise priority: at any
moment a user sees just one banner, and the highest-priority eligible one wins. Ask whether this banner
should take precedence over the existing one(s), set `priority` (1–5) accordingly, and note the final
ordering is visible in the Builder. If there are no other live banners, don't bring priority up at all.

---

## Phase 5 — Confirmation card

✋ Show a **readable confirmation card** (never raw predicate/draft JSON) and get a clear go-ahead.
Use an interactive confirmation card if that capability is available; otherwise use a clean text
table. Include:

- **Copy** and the **button** (label + what it does), if any
- **Placement** in plain words ("Top of page", or "Anchored — finish in Builder")
- **Behavior** — sticky / overlay / animate as on or off
- **Audience** — plain-English ("Everyone" or "Active EU companies")
- **Priority**, only if it came up
- **Environment**

Then: "Ready for me to create this banner as a draft?" — wait for the yes.

---

## Phase 6 — Create the draft

On confirmation, call `create_flow` with `type: "banner"` and the `draft.banner` payload (content as a
**rich2** document, buttons, `embed_mode`, `sticky`, `overlay`, `animate`, layout), plus
`filter_condition` if targeted and `priority` if it came up. See `references/mcp-reference.md` →
*Creating the banner* for the exact shape.

`create_flow` returns a **Builder URL**. Give it to the user:

> "Done — here's your banner draft: [link]. Saved, not live yet."

If placement was element-anchored, remind them to set the anchor position in the Builder before
publishing.

---

## Phase 7 — Offer to publish

✋ Never auto-publish.

> "Want me to publish it now, or review in the Builder first?"

If publish, call `set_flow_publication` (`action: "publish"`) — a **two-step confirm**: first call
without `confirm`, then again with `confirm: true`, passing the chosen `env_id`. See
`references/mcp-reference.md` → *Publishing*.

---

## Guardrails

- **Never publish without an explicit yes.** Create (draft) and publish (live) are separate confirmed
  steps.
- **Never invent** attribute FQNs, event names, or values — look them up and echo the audience back.
- **Keep copy short.** A banner is one line, not a paragraph. Push back gently on wall-of-text copy.
- **Element-anchored → Builder.** Don't fabricate CSS selectors; hand off placement.
- **No raw JSON in the confirmation** — a readable card is what catches mistakes.
- Keep it conversational — a helpful teammate, not a form.
