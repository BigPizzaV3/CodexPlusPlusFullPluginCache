# Correspondence Evidence: File Import and Microsoft 365

The plugin's biggest historical evidence gap is the paper trail: notification dates, PM
replies, and instructions live in email and document systems, not in Gather's site records.
This page covers the two supported routes to closing it — and the discipline both share.

## Route 1 (default): file-based import — no IT involvement

`$correspondence-import` parses exported correspondence (`.eml`, PDF, pasted text;
`.msg` is refused with export instructions) into the local **Pattern 17** register,
`correspondence/correspondence-register.md`. Classification (is this email *the* clause 61.3
notification?) and CE linkage are **user-confirmed, never inferred**, and proposed
`ce-register.md` updates are applied only on explicit confirmation.

This route works today for every customer: drag the relevant emails out of Outlook into a
folder, run the import, and the Red Team agent, `$adjudication-pack`,
`$nec-deadlines`, and `$final-account` start citing correspondence items instead
of relying on asserted dates.

## Route 2 (where IT has enabled it): Microsoft 365 connectors

the assistant supports Microsoft 365 access (Outlook mail and SharePoint/OneDrive) via connectors on
ChatGPT and MCP servers in ChatGPT Work. **The plugin does not require, request, or configure
this access** — it is a decision for the customer's IT (Graph API scopes, tenant admin
consent). Where a user's session already has such a connector, the skills above may use it
under these rules, which mirror Pattern 17:

1. **Scoped search only** — the project's mailbox/site, bounded by date range and search terms
   tied to the matter at hand. Never a bulk sweep, never "read everything".
2. **Same confirmation discipline** — an email found by search is a *candidate*; whether it
   constitutes a contractual notice is user-confirmed before it enters the register or a
   deadline computation, exactly as with file import.
3. **Cite, don't ingest** — outputs cite sender/date/subject and quote the load-bearing
   excerpt as recorded; whole mailboxes or document libraries are never copied into local
   files.
4. **Privilege gate** — in a live or contemplated dispute, correspondence may be legally
   privileged. Confirm with the party's legal advisers before searching or importing dispute
   correspondence through any tool. This is stated by `$correspondence-import` and
   applies with more force to connector search.
5. **Data governance** — mailboxes contain personal data and confidential material well beyond
   the project. The firm's RICS §3.1 assessment (see `docs/rics-ai-standard.md`) should cover
   connector use explicitly; the scoped-search rule above is the technical control that makes
   that assessment tractable.

## What this unlocks, either route

| Consumer | Before | After |
|---|---|---|
| Red Team agent | "we notified the PM on 14 Jan" → NO RECORDS | verified against [COR-NNN], or exposed as unevidenced |
| `$nec-deadlines` | clocks from typed-in dates | clocks from register-cited dates |
| `$adjudication-pack` | records-only chronologies | correspondence lines in the issue chronologies |
| `$final-account` | statuses asserted via `ce-register.md` | notified/reply dates evidence-cited in negotiation |

## What the plugin will not do

- Auto-classify an email as a contractual notice (Pattern 17 rule 2 — that judgement is the
  user's, or their lawyer's).
- Write to any mailbox or SharePoint site (everything here is read-only).
- Include register content in outputs destined for the other party.
- Ask a customer to grant tenant-wide access — if a customer wants deeper integration (e.g. a
  notices-mailbox watcher auto-populating the CE register), that is a scoped, IT-approved
  project to raise with Gather.
