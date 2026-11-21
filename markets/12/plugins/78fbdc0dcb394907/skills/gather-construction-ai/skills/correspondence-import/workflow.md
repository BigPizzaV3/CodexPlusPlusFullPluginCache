---
name: correspondence-import
description: Import exported emails and notices (.eml, PDF, pasted text) into a local
  correspondence register — dates, parties, user-confirmed classification and CE links
  — so notification and reply claims cite evidence, not memory. Nothing applied silently.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Correspondence Import (Ref CO-NNN)

Notification dates, PM replies, and instructions live in email — not in the Gather API. This
skill parses exported correspondence and writes `correspondence/correspondence-register.md`,
the local register that the Red Team agent, `$adjudication-pack`,
`$final-account`, and `$nec-deadlines` cite instead of relying on user-asserted
dates. This skill is the **producer** of **Pattern 17 (Correspondence Register)** in
`../../shared/patterns/17-correspondence-register.md`; read it before starting —
it governs the register schema and the consuming rules. Also follow **Pattern 1** (project
resolution) and **Pattern 8** (report numbering).

**Scope note:** this skill imports and indexes correspondence **as recorded** — it never
decides whether an email legally constitutes a contractual notice (classification is proposed
and user-confirmed, per Pattern 17 rule 2), never summarises an excerpt into a stronger claim
than the words carry, and never edits `ce-register.md` without explicit confirmation.

**Before importing dispute correspondence:** correspondence in a live or contemplated dispute
may be **legally privileged**. Remind the user once, before parsing anything, to clear dispute
correspondence with their legal advisers before importing it into any tool (RICS §3.1 handling
— see `docs/rics-ai-standard.md`). Proceed on their confirmation; non-interactive runs state
the reminder and continue with the files given.

---

## Step 1: Locate the Files

Resolve the project (Pattern 1). Then find the correspondence:

- A file or folder the user names in `the user’s request`, or
- A scan of `correspondence/inbox/` (the drop-folder convention) for `.eml`, `.pdf`, `.txt`,
  and `.md` files — **confirm the list before parsing**, the same discipline as
  `programme-import` Step 1.

**Format handling:**
- `.eml` → parse directly: RFC 822 headers give Date, From, To, Cc, Subject; the body gives
  the excerpt.
- `.pdf` → read it; extract the header block (date, parties, subject/reference) from the
  visible text. A scanned PDF whose text cannot be read is listed as "not machine-readable —
  supply the date/parties manually or re-export", never guessed at.
- `.txt` / `.md` / pasted text → accepted; propose the header fields from the visible content.
- **`.msg` → refuse with export instructions** (Outlook: File → Save As → choose a location,
  or drag the email into a folder and use "Save As" → .eml via most mail clients; printing to
  PDF also works). `.msg` is a binary container — never parsed blind (the `.mpp` discipline).

---

## Step 2: Extract and Confirm the Header Fields

For each item, show the extraction back before it enters the register:

| Field | Source |
|---|---|
| Date sent/received | The email's own Date header / the document's date — **never the file's modified date, never today** |
| Direction | out (we sent) / in (we received) — proposed from the From address, confirmed |
| From → To | As the headers state |
| Subject | Verbatim |
| Key excerpt | The load-bearing sentence(s), quoted as recorded |

Non-interactive runs: state the extractions as assumptions and continue. An item with no
readable date is imported with "date not readable — supply manually", never a guessed date.

---

## Step 3: Classification (User-Confirmed — the Critical Discipline)

Propose a type per item from its subject and content (the Pattern 10 keyword families help:
"compensation event", "early warning", "instruction", "quotation"):

**CE notification / early warning notification / PM reply / instruction / quotation
submission / general**

The user confirms or corrects each proposal. **Whether an email legally constitutes a clause
61.3 notification (or a valid reply, or an instruction) is the user's call, not this skill's**
— the proposal is a filing suggestion, and the register records the *confirmed* type.

**Non-interactive runs: every item is imported as UNCLASSIFIED**, with the proposals listed
for later confirmation — never auto-classified as a contractual notice.

---

## Step 4: CE Linkage

Where `ce-register.md` exists (and its project matches), propose links: item ↔ CE ref, from
subject/content mentions. User-confirmed, exactly like the classification; unlinkable items
stay unlinked. Non-interactive: proposals listed, nothing linked.

Then, for confirmed links, **propose** (never apply unprompted) the `ce-register.md` updates
the correspondence evidences: a notified date from a confirmed CE-notification item, a PM
reply date from a confirmed reply. Show the exact before/after rows. Apply only on explicit
confirmation; **non-interactive runs list the proposals and do not touch `ce-register.md`**
(Pattern 17 rule 3).

---

## Step 5: Write the Register

Write `correspondence/correspondence-register.md` per the **Pattern 17** schema: provenance
header (project, import date, files parsed), then one row per item — `[COR-NNN]` numbering
continues from the highest existing entry (append discipline; the register is cumulative
across imports, never silently replaced). If the file exists, show its provenance and confirm
append (the default) vs replace.

Remind the user once (Pattern 17 rule 5): the register stays local (`correspondence/` is
gitignored in this repo's conventions), and its content is never included in outputs destined
for the other party.

---

## Step 6: Report

```
CORRESPONDENCE IMPORT
Ref: CO-[NNN]
Project: [name] | Files parsed: [n] | Register: correspondence/correspondence-register.md ([m] items total)

1. IMPORTED ITEMS
   | COR | Date | Dir | From → To | Subject | Type ([confirmed / UNCLASSIFIED — proposals listed]) | CE link |

2. PROPOSED ce-register.md UPDATES
   [exact before/after rows — applied only on confirmation / "listed, not applied (non-interactive)"]

3. NOT MACHINE-READABLE / DATE MISSING
   [list, or "none"]

4. WHAT THIS UNLOCKS
   - Red Team: "we notified on [date]" verified against [COR-NNN], not asserted
   - $adjudication-pack: correspondence lines in the issue chronologies
   - $nec-deadlines: clocks running from register-cited dates
   - $final-account: notified/reply dates cited, not typed

5. CAVEAT
   Classification records the user's confirmation, not a legal conclusion; excerpts are as
   recorded. Privilege reminder for dispute correspondence (see scope note).
```

---

## Hard Rules

1. **Classification is user-confirmed, never silent** — non-interactive imports are
   UNCLASSIFIED (Pattern 17 rule 2).
2. **`ce-register.md` is never updated without explicit confirmation**, and never on a
   non-interactive run (Pattern 17 rule 3).
3. **Excerpts as recorded** — quoted, never paraphrased into a stronger claim.
4. **`.msg` and unreadable scans are never parsed blind** — refuse with export instructions.
5. **Dates come from the correspondence itself** — never the file timestamp, never today.
6. State the **privilege reminder** before parsing dispute correspondence (Pattern 17 rule 5).
7. Only this skill writes `correspondence/correspondence-register.md` (Pattern 17 rule 6).
8. Early warnings are **notified**, never "raised". UK English throughout.

---

## Related Skills

- The Red Team agent — verifies a draft's procedural claims against this register
- `$adjudication-pack` — cites register items in its issue chronologies
- `$nec-deadlines` — runs its clocks from register-cited dates where confirmed
- `$final-account` — cites notified/reply dates from the register
- `$events` — finds the site-records side of what this register evidences on paper
