# FORBIDDEN-GLOBAL — the project's own prohibition list

Phases 7 and 8 both build a negative block, and both of them open that block with the same thing:
every standing prohibition the project itself carries. Phase 7 calls it Tier 0 of the negative
taxonomy; Phase 8 makes it the first of the three sources of the negative list. Both name it
`forbidden_global`, and until this file existed neither of them said what it was, where it came
from, or who wrote it — so Tier 0 came out empty on every project, and came out empty *silently*,
which is the part that cost the work.

This file is the definition. It is short on purpose, for the same reason `ENGINE-CHECK.md` is short:
it is a thing to be filled per project, not a thing to be read twice.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. What it is](#1-what-it-is)
- [2. Where it lives, and who owns it](#2-where-it-lives-and-who-owns-it)
- [3. The block](#3-the-block)
- [4. Who adds to it, and how an entry is added](#4-who-adds-to-it-and-how-an-entry-is-added)
- [5. What happens when it does not exist yet](#5-what-happens-when-it-does-not-exist-yet)
- [6. What it is not](#6-what-it-is-not)
- [7. Where this file is referenced](#7-where-this-file-is-referenced)

<!-- /GENERATED:toc -->

## 1. What it is

**The list of things that must never appear anywhere in this piece, decided once for the whole
project rather than once per shot.**

It is a project-level fact, not a shot-level judgement. A wristwatch in a Nineveh frame is wrong in
every Nineveh frame, and asking a prompt writer to notice it forty separate times is asking them to
be right forty times in a row. So the decision is made once, written down once, and copied into the
top of every negative block after that.

**"Appear" includes what is heard.** The examples in this file are visual because most pieces have a
picture, but a prohibition is not a property of an image — it is a property of the piece, and it
governs whatever channels that piece has. On an audio-only piece there is no negative block to copy
it into, so the list is carried at the head of the script and the sound-design brief instead, and it
covers the same kinds of thing: a period boundary (an instrument that does not exist yet, a bell
cast centuries later, a bird that does not live there), and the owner's standing rules (no liturgical
chant on a heritage channel, no modern language in a reconstructed scene, no music under a named
victim's testimony). A piece with both channels writes one list and applies it to both — a symbol
that is forbidden in frame is forbidden in the narration that describes it.

Four kinds of entry live here and nothing else does:

- **What the canon forbids.** The period boundary, the reconstruction rules, an artefact that does
  not exist in this century, a costume element the research says is a later import. These come out
  of the world the piece is set in.
- **What the piece's own editorial rules forbid.** A channel that shows the ancient world as
  heritage and not as faith carries *no religious symbols*. A piece that must read as stateless
  carries *no flags*. A brand that will not be shown beside alcohol carries that. These come out of
  the owner's standing rules — for the heritage work, Part A of
  [`heritage-rules.md`](./phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md) —
  and out of whatever the commissioning brief promised.
- **What is factually unsafe or wrong to depict.** On a piece that tells people what to do — a public safety film, a health message, a first-aid sequence, anything instructional — the *content of the advice* is a prohibition too, and it is the one nobody thinks to write down. A heatwave film that shows salt tablets, an ice bath or an air-conditioned building as the answer has depicted three things that are wrong, or wrong for the place it is set, and every other check in this package will pass it: the frame is beautiful, the type is legible, the negative block is clean. **Name the specific wrong actions here, as prohibitions, before the first shot is written**, and take them from the guidance that actually governs the subject and the place — generic advice assumes a grid that works and water that is drinkable, and both assumptions fail in some of the places these films are made for.

- **A picture that would be read as something it is not.** The clearest case, and the one that
  catches careful people: **every object pictured in an ICOM Red List is a legitimately held,
  inventoried museum object.** The Red Lists show the *categories* at risk — they are explicitly not
  lists of stolen things — so putting one of those images under narration about looting tells the
  audience that a lawfully held object was stolen. The same trap runs through auction catalogues and
  dealer photographs, where the image is a sales asset and the claimed findspot is usually a dealer's
  assertion repeated: caption **who said it**, never the findspot itself. And on any piece about the
  trade, the profession's one hard media line is that **market value does not go on screen** — a
  televised price is the thing that demonstrably moves the market.

- **What would identify a person the piece is protecting.** Where a contributor was promised
  anonymity, the specific things that would undo it are project-level prohibitions and belong here
  by name, *before* the first shot is designed: the uniform, the insignia, the doorway, the view
  from the window, the street sign, the dialect word, the vehicle, the scar, the ringtone. They are
  not shot-level judgements — a guard's uniform is disqualifying in every frame, and asking a prompt
  writer to notice it forty times is asking them to be right forty times running, which is the
  argument this whole file is built on. **This entry kind was added in September 2026**, after a test
  run built a protected-identity film and found that the three kinds above had no room for the one
  constraint that governed the entire piece.

All four behave the same way downstream, which is why they share one list: they are the entries
that are not up for discussion in the shot, only in the project.

## 2. Where it lives, and who owns it

**It lives at the root of the project brief**, beside the engine record and the rest of the
project-level material, not inside any one phase's folder. Every phase can read it; no phase owns
it.

**It is owned jointly by the canon and by the piece's own editorial rules**, which is to say by the
two authorities that are allowed to decide something about the whole piece. **The agent writes it:**
Phase 1 fills it from the brief and the canon, and a later phase that finds a project-wide
prohibition adds it with the date and the reason, records it under `decisions`, and updates the
negative block of every prompt written before it.

**It is append-only.** Entries are added and are not quietly removed, because a prompt already
approved and rendered was approved against the list as it stood. Removing an entry is a recorded
choice, with the date and the reason written beside it, so that the shots rendered under the old list
can be found again. An entry the brief itself made is removed only by the brief.

## 3. The block

Copy this into the project brief and fill it. One list for the whole project, whatever the route is.

```
FORBIDDEN_GLOBAL
  project:        
  opened on:      YYYY-MM-DD
  decided by:     (the brief, the canon, or the agent's recorded choice)

  from the canon:
    - <entry>                       — why, in one clause; the canon rule it comes from
    - <entry>                       — …

  from the piece's editorial rules:
    - <entry>                       — why, in one clause; who decided it
    - <entry>                       — …

  factually unsafe or wrong to depict:      (instructional pieces; name the wrong action)
    - <entry>                       — the guidance it contradicts, and for which place
    - <entry>                       — …

  would identify a protected contributor:   (name the thing, not the person)
    - <entry>                       — which contributor it would identify, and how
    - <entry>                       — …

  removed, with the date and who decided it:
    - <entry>                       — removed YYYY-MM-DD by ______, because ______
```

**Write each entry as the thing, not as an instruction.** *no flags*, not *do not show flags* — the
entries are copied straight into a negative block, and a negative block that reads as a sentence
confuses the engines that parse it as a token list.

**Write the reason beside every entry.** An entry with no reason cannot be argued with later, and it
is the entries nobody can argue with that survive long past the project that needed them.

## 4. Who adds to it, and how an entry is added

- **The canon adds** when research settles a boundary: a period line, a reconstruction rule, an
  object that belongs to a later century than the piece.
- **The brief adds** when a standing rule applies to this piece: an editorial line about the channel,
  a promise made in a commissioning brief, a sensitivity that this particular audience carries.
- **A later phase adds.** A prompt writer in Phase 7 or Phase 8 who finds a prohibition that is
  obviously project-wide rather than shot-specific adds it with the date and the reason, records it
  under `decisions`, and carries it into every negative block from then on.
- **Phase 1 opens the block.** This is what [`PROJECT-STATE.md`](./PROJECT-STATE.md) means when it
  lists `forbidden_global` among Phase 1's writes. Phase 1 copies in the canon's entries and the
  brief's standing entries, adds what the piece itself plainly needs — a period boundary, a protected
  contributor's identifying detail — and where the brief states no standing rule it writes
  `none, per the project brief` beside that part (§5). Every entry it chose itself goes under
  `decisions`.

The distinction that matters: **project-wide or this shot?** If the answer is *this shot* it is not a
`forbidden_global` entry, it is Tier 1, 2 or 3 of the image negative block or the third source of
the video negative list, and it is budgeted like every other shot-level negative.

## 5. What happens when it does not exist yet

**The prompt is still written, in full.** Nothing is cut, no shot is redesigned, and nothing waits.
Phase 1 fills the list at once from the brief and the canon (§4), so a missing list is rare; where a
prompt is written before it exists — a supplied-stills route that starts at Phase 8 — the agent fills
it the same way on the spot. Only an entry that still needs the user's eye is marked, and the Tier 0
slot then carries the marker as a note:

```
[NEGATIVE]  Tier 0: pending_forbidden_global
            (Tier 1, 2, 3 as normal)
```

and the marker travels with the handoff, exactly as `pending_engine_check` does — a note for whoever
reviews the batch, never a stop.

**The block above is the prompt record, not the string sent to the engine.** The marker — and, on a
project that forbids nothing, `none, per the project brief` — is written on the prompt record and
on the handoff line, and it is left out of the negative string pasted into the engine, which would
otherwise receive it as a token. Until the list arrives the pasted Tier 0 is simply empty; the
record is what shows it.

**An empty Tier 0 must be visibly empty, never silently empty.** That is the entire point of the
marker. A Tier 0 that is simply absent looks identical to a Tier 0 on a project that genuinely
forbids nothing, and those two situations are not the same situation at all — one of them is a
finished decision and the other is a decision nobody has made. The marker is one minute of work to
close and it is the difference between a gap someone can see and a gap that reaches the render.

**Every marker closes two ways.** *Resolved* — the answer arrived — or *`unobtainable — why, and what was done instead`*, which is a finished answer and not an open one. [`ENGINE-CHECK.md`](./ENGINE-CHECK.md) carries the rule and a worked case for each marker. What is never acceptable is deleting a marker because it could not be resolved.

**A project that genuinely forbids nothing writes that down too.** The block from §3 is filled with
`from the canon: (none)` and `from the piece's editorial rules: (none)`, dated and signed, and Tier 0
then reads `none, per the project brief`. A stated nothing is a record. An unstated nothing is a
hole.

**The same rule as the engine record, for the same reason.** See
[`ENGINE-CHECK.md`](./ENGINE-CHECK.md) §3: a visible unfilled cell costs a minute, and a guessed or
assumed one costs a re-render. The package does not stop on a missing project input; it marks it and
keeps going.

## 6. What it is not

Three lists get confused with this one, and mixing them in wastes the attention a real prohibition
needs:

- **It is not the generic anachronism list.** *modern clothing, wristwatches, denim, asphalt* is
  Tier 2 of the image negative taxonomy, and it is taken from the project's own period boundary. It
  belongs here only when the canon has settled a specific boundary that the generic list does not
  express.
- **It is not the generation-artefact list.** *bad anatomy, extra fingers, watermark, split screen*
  are properties of the engines, not of the project. They live in the negative taxonomy where the
  engines are discussed, and they change when the engines change.
- **It is not a wishlist of things that would look worse.** An entry here is something the piece
  must not contain. A preference about what plays better is craft, it goes in the shot, and it is
  argued at tier 5 of [`PRECEDENCE.md`](./PRECEDENCE.md), not enforced as a standing prohibition.

One more, because it is the one that has actually bitten: **religious content is not a default
entry.** It is a per-project decision that reaches the negative block only through this list. Some
work forbids it — a heritage channel framing the ancient world as heritage rather than as faith —
and other work is built on it: a Christian children's song channel, a documentary about a
theological school where monks and a bishop are the subject. A blanket entry here would make those
pieces impossible to generate.

## 7. Where this file is referenced

- `phase-07-image-prompt-engineering/how-to-write-an-image-prompt.md` — the inputs table, and
  Tier 0 of the negative taxonomy
- `phase-08-video-prompt-engineering/how-to-write-a-video-prompt.md` — the inputs table, and the
  first source of the negative list

If a guide sends you here and the list for this project does not exist yet, fill §3 from the brief
and the canon now; §5 says how, without asking anyone.
