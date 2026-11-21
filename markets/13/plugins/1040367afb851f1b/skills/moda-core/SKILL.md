---
name: moda-core
description: >-
  Moda meta, setup, and routing — the contract every moda skill assumes. Use
  for: connecting Moda to this client, account/team/workspace questions, "what
  can Moda do?", which moda skill handles X, troubleshooting a failed Moda
  tool call (typed errors), and any Moda ask no other moda skill clearly owns.
  Never for creating or editing an artifact — a matching format skill always
  wins.
---

# moda-core

Moda's operating contract: what Moda is, session setup, the write contract, recovery, and which
moda skill owns what. Load once per session; every other moda skill assumes it.

## What Moda is

One platform where several tools normally sit, driven through this connector's tools — you author
by writing markup, and a design is a document you rewrite, not a render you regenerate:

- **Design canvas** (Figma/Canva-class vectors): decks that export native PPTX with real shapes and text layers;
  documents and print pieces that export selectable-text PDF; social graphics and carousels; anchored-connector
  diagrams; data charts; UI mockups at real viewport sizes.
- **Motion + video**: keyframes, easing, staggers (After Effects' core), a timeline for cutting clips, mp4/gif export
  — plus image generation models for imagery inside editable designs, picked live from `load_skill("omni-and-media")`.
- **Websites**: real multi-page sites at public `*.moda.page` URLs. Reads are live here; building and
  publishing happen in the Moda app — moda-website routes there and never fakes a publish.
- **Workspace**: brand kits that bind to everything; team templates; a drive of files Moda reads for you
  (PDF/DOCX/PPTX/XLSX/CSV); stock photos and icons. PowerPoint import runs in the Moda app —
  moda-deck-pptx routes there.

Everything lands on a live URL that stays editable — by you, by the user in the Moda app, and by Moda's own agent.
**Free vs metered:** ALL canvas authoring, edits, screenshots, exports (png/jpeg/pdf/pptx/mp4/gif), brand kits,
templates, drive, and `ask_expert` are FREE. Only generated media meters — prices ride the model cards, and
`moda_bootstrap` reports the balance. Full inventory: references/capability-map.md.

## Step 0 — every session

1. `moda_bootstrap` — call it once, first. It returns identity, plan, teams, entitlements and the
   working discipline the other tools assume, and it doubles as proof that Moda is connected.
   Nothing here ever needs updating: tools and skills are served by Moda and are always current.
2. `brand_list` — one cheap call, never skipped. Every NEW design → ASK which brand kit, then
   wait, even with one kit or none: their kits (name + logo), a NEW one (load moda-brand), or no
   kit. A team default or a sole kit is not their answer; a kit they named (here, in project
   instructions, or in memory) is — `canvas_create` refuses a new design until you pass
   `brand_kit_id=…` or `skip_brand_kit=true`. BIND the chosen kit at create time.
   No kit means you INVENT an identity for the piece — never neutral, plain, or a default
   template look; the format skill's no-brand design reference carries the method.
3. No vision in this harness? Follow the degraded verify loop in references/contract.md.
4. Unsure, or a call failed? `ask_expert` — free and fast. Ask early, never guess.
5. You are the designer here. Moda's own agent is a separate ACTOR you can hand the whole job
   to — `task_delegate` (metered) — and only when the user's words name Moda's agent, make
   Moda the doer, set it against you, or name the hand-off: "have the Moda agent make this",
   "Moda should make this", "let Moda take over", "start a Moda design task". Moda attached by
   a preposition — "use Moda to make a deck", "a one-pager using Moda", "have this designed on
   Moda" — names it as the INSTRUMENT: YOU build it, which is the default. Torn? Build it.
   Handing off does NOT hand over your files: pass whatever the work is based on in
   `attachments` (file_… refs from `upload`, or public URLs), or the agent builds without it.

Bootstrap names your teams, and team decides whose workspace and billing the work lands in. Pass
`team` on the tools that take it, and never switch teams on your own initiative.

## The write contract (non-negotiable)

- Every write carries `expected_revision` from your last read. The connector already retries
  `canvas_edit`, markup append and `canvas_import_pages` once for you on `stale_revision`; on any
  other stale write, re-read and retry once — it heals. Persistent = a human is editing live.
- One canvas, serial writes. They serialize server-side anyway; a parallel batch can get `canvas_busy`.
- Success + `requires_repair` = committed but imperfect: read the result, repair, re-verify.
- Screenshot what you shipped (`canvas_screenshot`) — the only way to know how it renders.
- Send the canvas link the MOMENT it exists — before authoring, so the user watches it build.
- Same typed error twice → stop and open references/recovery.md; never spin on a third try.

**Match the ceremony to the job.** Tiny edit: make the edit, glance, done. Single artifact (a post, a page): a bar of
3 criteria or fewer, then one targeted fix pass at most. Multi-unit build (deck, doc, carousel, variants, whole-page
rebuild): three phases — freeze ONE spec, declare acceptance criteria before the first mutation, build every unit
without pausing to polish, verify in exactly ONE bounded round. Full ceremony: the multi-unit-workflow reference.

## Connection and account

- Nothing to install and nothing to update: Moda is connected by your host and served always
  current. `moda_bootstrap` shows identity, teams, plan and remaining credits.
- Ground truth for a call: the tool's own description and schema. Deeper guides are one free load
  away by name — the catalog with routing triggers rides that tool's description.
- Every failure comes back as a typed error with a hint on the result; follow the hint before you
  retry, and never re-run a failed write just to see its error again.

## Ask an expert — the universal recovery move

`ask_expert(question=…)` is a live Moda product expert: free, fast, grounded in Moda's own guides,
with citations. There is no dumb question and no cost — asking beats guessing every time.

- Stuck twice on the same error → `ask_expert(question=…, context="<the full error>")`
- Unsure whether Moda can do something → ask BEFORE telling the user no. Answers name the skills to read — load
  what they point at; follow-ups keep the thread (`session_id`). If `ask_expert` is absent from your tool list
  it is not enabled for this workspace: lean on the skill guides and the typed-error hints instead.



## Routing — which skill wins

Precedence, top rung first; the first rung that applies decides:

1. A canvas + a change/export verb → moda-edit, with two carve-outs this rung states itself because
   it decides before the rungs below it can: MOTION is moda-video's whatever the canvas ("make it
   move", "animate this", an mp4/gif of it), and a `*.moda.page` site is moda-website's. The ref does
   not have to be pasted: one built earlier in this session is already the referent, so a bare
   follow-up on it — "add California", "make it 14pt", "continue" — is moda-edit's, not a second build.
2. mp4/gif/video/animated anywhere in the ask → the moda-video family, whatever else it says.
3. Platform named (Instagram/LinkedIn/TikTok/YouTube) → that moda-social child, even for "poster",
   "flyer", "banner" wording; an AD noun outranks it → moda-social-ads, platform-native included.
4. Print/PDF words → moda-document; poster/flyer/menu/resume → moda-document-print.
5. Live/hosted → moda-website; a picture of an interface → moda-mockup.
6. Data chart → moda-chart; boxes-and-arrows → moda-diagram (a chart inside an artifact you are building stays there).
7. "Continue where you left off" with NOTHING in this session (rung 1 owns it once there is) →
   moda-library (newest canvases; screenshot to confirm), then moda-edit.
8. Nothing fits → this skill answers, honestly.

## References

- references/capability-map.md — "can Moda do X?": the full inventory with free/metered marks.
- references/basics.md — install, auth, update detail, account and credit verbs, conventions.
- references/contract.md — ids, revisions, idempotency, visibility, the no-vision verify loop.
- references/recovery.md — any typed error, export warnings, when and how to ask an expert.
- references/skills-index.md — every moda skill and its description on one screen (generated).
