---
name: find-hackathon
description: Discover which Devpost hackathon is open to enter before starting the guided flow. Use when the user wants to find, search, or browse hackathons, asks for a recommendation ("recommend a hackathon", "which hackathon fits me/my project"), or asks what hackathons are open or upcoming. This is the pre-stepper discovery step; setup and registration happen in $start-hackathon.
---

# Find Hackathon

## Purpose

Show the participant what is open to enter through this app, then point them to `$start-hackathon`.

This skill is discovery only. It writes no state file, performs no registration, and makes exactly one MCP call. Dates, prizes, rules, and announcements belong to later steps — do not fetch them here.

This is pre-stepper discovery. Do not call `show_hackathon_stepper` in this skill — the journey stepper starts at `$start-hackathon`.

Chat is the primary participant interface.

## Required Data Source

Official event data comes from the `devpost` MCP server — follow **Devpost MCP Server** in `references/plugin-runtime.md` (call only what you need, never verify or set up the server, degrade in one line on failure).

This skill uses exactly one tool: `devpost.list_open_hackathons` — the catalog of open or upcoming hackathons available through this app. Do not call `get_hackathon_overview`, `list_hackathons`, or `search_hackathons` here.

## Required References

Read before responding:

- `references/plugin-runtime.md`
- `references/config/hackathon.json`

## Authentication

Every `devpost` tool call requires the participant to be signed in — there is no public tier. `list_open_hackathons` is this skill's auth gate: if it fails on auth, hard-stop per **On auth failure** in `references/plugin-runtime.md` (one-line notice, the sign-in recovery, and stop). Do not call `whoami` first — the required call is the gate.

## Flow

1. **If the user names a specific hackathon** (a Devpost slug like `my-event`, a clear event name, or a devpost.com URL), skip discovery entirely: tell them `$start-hackathon` sets it up, and per the affordance rule in `references/plugin-runtime.md`, treat any go-ahead ("start it", "yes", "let's do it") as that command and proceed on this turn.
2. Otherwise call `list_open_hackathons` once.
3. **One hackathon in the catalog (the current normal case):** show it — name, the devpost.com link, and a one-line description — and recommend `$start-hackathon`. Do not present a list of one.
4. **More than one:** present a short numbered list (name, one-line descriptor, URL) and recommend `$start-hackathon`, naming their pick in the recommendation. Selection is resolved and recorded by `$start-hackathon`, not here.
5. **Present the catalog honestly.** These are the hackathons live in this app right now — never claim they are the entire Devpost catalog, and never invent entries. Point anyone who wants the full picture at the Devpost browse page (`links.browse_hackathons` in `references/config/hackathon.json`). Do not use web search for discovery — ever.

## Fallback

If `list_open_hackathons` fails on availability (not auth — the gate above owns auth failures), degrade in one line per `references/plugin-runtime.md` and point the participant at the Devpost browse page (`links.browse_hackathons` in `references/config/hackathon.json`). If they already know their event, `$start-hackathon` accepts a pasted name, slug, or URL.

## Chat Output

Keep chat output minimal:

- the current hackathon (or the short list), with the devpost.com link and a one-line description
- nothing else — no dates, prizes, or registration details; those come in later steps

End with an enrollment callout as the final line, so the participant's advance is an acknowledged choice of hackathon — never a generic "next" detached from the event. The callouts below are templates: `[Event Name]` is a placeholder slot, NOT literal text. Interpolate the actual event name(s) from the `list_open_hackathons` response you just received on this turn; never output the bracketed placeholder itself, and never hardcode an event name into this skill.

One hackathon in the catalog:

```text
Ready to enroll in [Event Name]? Say "next" and I'll get you registered — or type `$start-hackathon`.
```

More than one:

```text
Which one looks right? Tell me your pick — or type `$start-hackathon` and I'll set you up.
```

Treat "next", a named pick, "start it", or any clear go-ahead as `$start-hackathon` per the affordance rule.
