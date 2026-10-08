---
name: saleseq-docs
description: Answer questions about how the SalesEQ product works — recording and the desktop app, sharing and permissions, groups, auto-share rules, public links, insights and reporting, calendar/email/HubSpot integrations, members and roles, billing, two-factor, and connecting SalesEQ to an AI assistant. Fetches the official docs rather than answering from memory. Use when someone asks how to do something in SalesEQ, why SalesEQ behaved a certain way, what a SalesEQ term means, or how a SalesEQ feature is configured. Do NOT use this to look up meeting content — the SalesEQ MCP tools handle searching meetings, reading transcripts, and pulling summaries.
---

# SalesEQ product documentation

Answers questions about **how SalesEQ works as a product**. This is not for querying meeting
data — the MCP tools (`search_meetings`, `get_transcript`, `get_meeting_summary`,
`list_meetings`, `get_meeting_frame`, `get_org_context`) own that, and they describe their own
usage. Use this skill for product behavior, configuration, terminology, and troubleshooting.

## Fetch the docs; do not answer from memory

SalesEQ ships fast and the product changes. Model recall of SalesEQ specifics is unreliable and
will invent settings that do not exist. Always fetch before answering anything beyond the
vocabulary below.

The docs site publishes agent-readable endpoints:

| URL | What it is |
| --- | --- |
| `https://saleseq.ai/docs/llms.txt` | Index of every page with a one-line description (~5 KB). **Start here.** |
| `https://saleseq.ai/docs/<path>.md` | Any page as clean Markdown — append `.md` to the page URL |
| `https://saleseq.ai/docs/llms-full.txt` | Every page concatenated (~110 KB). Only when a question genuinely spans the whole product. |

### Workflow

1. Fetch `https://saleseq.ai/docs/llms.txt` and pick the page(s) whose description matches the
   question.
2. Fetch those pages as `.md`. Fetch two or three in parallel when a question straddles sections
   — sharing questions often need both `sharing/share-a-meeting.md` and `sharing/groups.md`.
3. Answer from what you fetched, and link the human-readable page (the URL without `.md`).
4. If the docs do not cover it, say so and point to `https://www.saleseq.ai/docs`. Do not guess
   at menu paths, setting names, or plan limits.

## Vocabulary

Enough to route a question correctly without a fetch. Anything beyond this, fetch.

- **Meeting** — the central object: recording, transcript, participants, and everything generated
  on top. Arrives three ways: recorded by the desktop app, uploaded by hand, or pulled in by an
  integration. Some meetings are audio-only or transcript-only.
- **Organization** — the company account. Owns members, groups, settings, and meetings. Every
  meeting belongs to exactly one.
- **Member / Admin** — the two roles. Lowercase "member" means anyone in the org; capitalized
  **Member** is the non-Admin role. Admins manage members, invites, groups, and org-wide sharing.
- **Group** — a named set of people (Sales, Leadership). Share with a group and later joiners get
  access too.
- **Owner** — the person who recorded or uploaded a meeting. Ownership does not transfer.
- **Viewer / Editor** — the two grant roles. Viewer watches and reads; Editor also edits and
  shares onward. Sharing is additive: the highest applicable role wins.
- **Auto-share rule** — shares a meeting the moment it finishes, without manual action.
- **Public link** — shares a meeting with someone outside the organization.

Recording happens on the user's own machine via the desktop app. **No bot joins the call** and no
extra participant appears — this is a frequent point of confusion when comparing SalesEQ to
bot-based notetakers.

## Section map

Route to the right part of `llms.txt` fast:

- **getting-started** — create/join an org, first recording, download, concepts
- **capturing-meetings** — desktop app, automatic recording, upload, Live AI, recording notice,
  what gets captured
- **your-meetings** — viewing, Ask AI, search, delete and discard
- **sharing** — share a meeting, groups, auto-share rules, public links
- **insights** — meeting insights, reporting
- **integrations** — calendar, email and follow-up drafts, HubSpot
- **ai-assistants** — overview, connect Claude, connect ChatGPT, connect a custom MCP client,
  the tool list, troubleshooting
- **account** — members and roles, billing, two-factor, onboarding flow

## Connection and auth questions

Questions about connecting SalesEQ to Claude, ChatGPT, or another MCP client, or about why the
tools return nothing, live under `ai-assistants`. `ai-assistants/troubleshooting.md` is the right
first fetch for "the connector isn't returning my meetings."

Empty tool results are usually **access**, not failure: the tools return only meetings the account
owns, meetings shared with it directly, and meetings shared with a group it belongs to. Check that
before treating an empty result as a bug.
