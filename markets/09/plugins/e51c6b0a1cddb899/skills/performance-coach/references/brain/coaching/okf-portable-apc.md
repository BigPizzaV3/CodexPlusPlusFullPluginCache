---
key: okf-portable-apc
type: coaching
customer_visible: true
provenance: extension
source: "founder requirement 2026-08-08: cloud OKF link gives any RapportScore user the same APC; governance bake rules; coach-private-policy"
last_verified: "2026-08-08"
---

# Portable APC brain (cloud OKF)

The corner-coach brain is the **shared craft layer** for an agentic performance coach (APC) that works with RapportScore measurement. It must be **exportable**: Ron (or product) can hand another user a cloud OKF link and they get the **same coach operating system**, paired with **their** RapportScore data.

## What is shared vs personal

| Layer | Lives where | Ships in cloud OKF? |
|---|---|---|
| Measurements, dimensions, belts, drills, session types, credit rules, receipt→inner driver, curriculum map, safety | This vault (customer bake) | **Yes** |
| Research depth that is customer-safe | `research/` (bake rules apply) | **Yes** |
| Maintainer gaps, labs, changelogs under `_meta/` | `_meta/` | **No** (not customer bake) |
| Named-user dossiers, dial history, private ledgers | Hermes `coach-private/` or product user store | **Never** in the shared OKF |
| Live scores, transcripts, demos, team tape | RapportScore account via MCP/app | Per user at runtime |

Same brain. Different tape. Different private memory.

## Runtime contract for any user

1. Load **APC-SYSTEM-PROMPT.md** as the host **system / custom instructions** (not optional knowledge).
2. Load **portable OKF** (this brain bake) as knowledge / files.
3. Connect **that user's** RapportScore identity (OAuth / MCP).
4. Coach with receipts from **their** sessions only.
5. Store longitudinal memory in **their** private store, never inside the shared bundle.
6. Lesson credit always on RapportScore.ai ([[lesson-credit-and-practice]]).

If step 3 is missing, the coach may teach craft from the OKF but must not invent personal scores.

Host wiring cheat-sheets: root `CHATGPT.md`, `GROK.md`, `FOR-CLAUDE.md`, `FOR-AGENTS.md`.

## Authoring rules so export never leaks

When writing or editing bake-included notes:

- No named customers, employees, or founder-only dogfood as if it were universal truth.
- No emails, phone numbers, deal names, or internal project codenames required to understand the note.
- Examples stay generic ("John on the call", "your prospect") or clearly labeled as illustrative.
- Ron-only ops belongs in Hermes memory or `_meta/`, not in `coaching/` / `measurements/`.
- Before any cloud publish: banned-token scan, em-dash scan, wikilink integrity, and ship-clean check so private paths are absent.

## Cloud OKF link (product intent)

Target experience:

1. Publisher exports a **versioned bake** of this vault (customer-visible paths only).
2. Recipient opens a **link** (cloud OKF), agent loads that bundle as system craft.
3. Recipient connects RapportScore and gets Wendy-class APC behavior on their data.

Until the hosted link pipeline is fully productized, the source of truth for craft remains this vault; Hermes skill mirrors are deployment copies, not a second brain.

## Related

[[receipt-to-inner-driver]] · [[coaching-promises]] · [[lesson-credit-and-practice]] · [[getting-started]]
