---
name: eonik
description: >-
  Do a brand's creative work with eonik, in the eonik app on the person's
  computer: the adapts a media plan asks for, exact changes to a creative's
  pieces, reels and animated banners, versions in another language or with
  another person, new ads and ads recreated with the brand's own, the client's
  notes, checks, approval and delivery, a project's changed facts, copy
  against the brand's limits, a brand's handover files, and what competitors
  run. Use when eonik is connected and the person asks for any of these, or
  asks where their eonik work stands.
---

# eonik

eonik does the work on the person's own computer, in the eonik app. You are how they ask for it. **eonik prepares; the person decides.**

## Where the work runs

The work on creatives runs in the eonik app on the person's computer, signed in to the same eonik account as this connection, where their files and fonts are. When it is not open as that account, the tool says so in plain words and names the account: tell the person exactly that. The brand and research tools need no app open; they report what eonik has recorded.

## Every time

1. Pass the person's words exactly in `their_words`. eonik keeps them with the change they made.
2. Look before you change: `get_creative` shows each size's pieces and a picture of every size. Judge a size beside its master, from its picture.
3. The person decides. Making the sizes, keeping a change, approving, sending and spending are theirs: they press them in eonik's panel, in a form your host shows, or in eonik itself. Say what is waiting for them; do not say it is done.
4. Say what eonik says, as it says it: when eonik is not open, is signed in as another account, may not spend, or needs a line confirmed.
5. Every price is the person's to confirm, before anything that costs is made.
6. A change is a new state of the creative: `undo_change` puts it back, and the state it had is saved first.

## Their words

Speak as the person does: a master (the designer's file), its adapts (its sizes), a set (the sizes one media plan wants, such as the launch set), a project (such as a tower launch) and its facts (each a label and the exact words a creative prints, such as its price or its registration number), and the pieces of a design: the headline, the price, the legal line, the logo, the photo.

## Jobs take minutes

Making, changing, checking, sending and delivering start a job in eonik. Where your host shows eonik's panel, the call answers at once and the panel follows the job. Otherwise the call follows the job for up to a few minutes, and eonik asks the person, as a form your host shows, whatever only they can decide. When the call comes back, say what it says: done, waiting for the person, or still being made.

## The work, piece by piece

Each is also served as a guide, `eonik://guide/<name>`, to a host without this skill.

### Where things stand (`eonik://guide/where-are-we`)

At the start of a session about the person's creatives, or when they ask what is waiting.

They say: "Where are we?" · "What came back from the client?" · "Is anything waiting for me?"

1. `get_adapts_status`: what needs them, what is being made, what the client sent back, and whether eonik is open on their computer.
2. For the client's words, `get_client_notes`.
3. Say what is waiting for them first.

- A job still running is not done: say it is being made, and check again when they ask, not in a loop.

### Adapts for a media plan (`eonik://guide/adapts`)

They want a creative's sizes for a set or a list of sizes.

They say: "Adapt the spring master to the launch set" · "These ten into GDN plus 640x800" · "Make the sizes of the file I attached"

1. `find_creatives` when you are not sure which creative they mean; name it by its name and folder.
2. `make_adapts` with the creatives, and with `sizes` only when they named sizes. Without sizes, eonik offers its own, last time's picked first, and the person picks. A file they attached goes in `attached`.
3. eonik opens its review of the sizes. Nothing is made until the person presses Make.
4. When it is done, `get_creative` shows each size; look at the pictures before you say how they came out.

- eonik makes the sizes: they carry the brand's fonts and rules, and the person reviews them in eonik before anything is made.
- A size eonik could not lay well is said by eonik; relay it as it is.

### An exact change to a creative (`eonik://guide/change`)

They said exactly what changes: words, a size, a place, a colour, a picture, or how a piece moves.

They say: "Logo bigger on 300x250" · "Use the evening photo everywhere" · "Headline in white on the GDN sizes" · "Hide the offer on the leaderboard"

1. `get_creative` first: each size's pieces, their words and places, and a picture of every size.
2. For another of the brand's pictures, `find_brand_pictures`, then its `ref` as the change's `picture`.
3. `change_creative` with each piece named by what it is for (`headline`, `logo`, `photo`, or `line` with the words it says), what changes, and the sizes. eonik makes it, reads it back size by size, and the person keeps it or puts it back.
4. `compare_versions` shows it beside the state before, as pictures.

- A change said as an outcome, such as "make it feel premium", is `revise_adapts`: eonik decides what to change.
- A figure no project fact supports is refused by eonik; ask the person for its source.
- Taken back later: `undo_change` with the state from `get_creative`'s history.

### A static made into a reel (`eonik://guide/reel`)

They want a creative to move: a reel, a moving version, an animated banner or a GIF.

They say: "Make this a reel" · "Headline rises in, then the price" · "An animated version for Google display"

1. `get_creative` first. A reel is usually 1080x1920: if the creative has no such size, `make_adapts` makes it.
2. `change_creative` with a `motion` on each piece that moves: how it enters (`rise`, `fade`, `pop`, …), its pace, when it appears (`starts_after`), and for words, line by line, word by word or letter by letter. `page_seconds` sets how long it plays.
3. The answer shows each moving size as frames across its length: look at them before you say how it moves.
4. `deliver_set`: a size that moves is written as MP4, or GIF on a Google display size; `formats` names another for a size when the person asks.

- A line on screen for the whole ad (a registration number, T&C) does not move; eonik says so.
- A picture brought to life by AI costs credits and is made in eonik itself.

### Versions of one creative (`eonik://guide/versions`)

They want versions that differ in one thing: who is shown, the setting, the language, or one line's words.

They say: "A Hindi version" · "The same ad with an older couple" · "The launch price instead"

1. `make_versions` with what varies and one value per version, in their words; for new words, `line` is the words the line says now.
2. A person or a setting is a paid edit of the photograph: the person confirms the price first. Words and languages are free.
3. Each version the person keeps becomes a page of the creative.

- A translation never changes a figure; eonik refuses one that does.

### A new ad (`eonik://guide/ads`)

They want a new ad from what it should say.

They say: "An ad for the summer sale" · "A 15-second ad for the new serum"

1. `make_ad` with what it should say, the product and the person, in their words.
2. eonik writes the script and shows it to the person with the price of making the ad. They approve it once, or change the words in eonik first.
3. Once approved, eonik draws the frames, makes the video or the page and puts it on its timeline. One ad per call; more of one ad come from `make_versions`.

- The product must be one of the brand's own: eonik asks which when the name fits several.

### An ad recreated with the brand's own (`eonik://guide/recreate`)

They want an existing ad remade with the brand's product, person or place.

They say: "Remake Lodha's café reel with our new serum" · "Recreate our Diwali ad in a café"

1. `recreate_ad` with the ad as they named it (a saved ad, one of the brand's own, or a link) and what goes in it.
2. eonik plans it: who becomes whom in which shots, what stays and what it cannot use, with the price. The person approves it once.
3. Another brand's footage is reused only when the person says they may.

- A real public figure is refused; offer the brand's own people instead.

### The client's notes (`eonik://guide/client-notes`)

The client sent a creative back with notes.

They say: "Put the client's notes in" · "What did the client say?" · "Fix the client's notes and send v3"

1. `get_client_notes`: each note, who wrote it, the size it is on, and each creative's `creative_file`.
2. For each note, pass its creative's `creative_file` as `creative` to `get_creative`, then to `change_creative`, making exactly what the note asks, on the size it was left on. The person keeps each change.
3. `send_for_approval` sends the new version, and `answer_client_note` answers each note the person kept a change for, saying what was done.

- A note that asks for an outcome, not a change, is `revise_adapts`.
- Answer a note only once its change is kept.

### Check, approve and deliver (`eonik://guide/package`)

The work is ready to go to the client or the media team.

They say: "Is it OK to send?" · "Send it to the client" · "Package the launch set for media"

1. `check_before_sending`: the brand's rules on every size, as facts, size by size.
2. `send_for_approval`: the brand's review room, and the link to give the client.
3. `deliver_set`: every size written as its plan says, zipped, then measured against each channel's limits; `zip_name` in their naming.

- Approval is the client's, in the review room: it is never yours to give.
- A finding the person sends past is their call, remembered by eonik.

### A finished package checked (`eonik://guide/check-package`)

They have a zip or a folder, theirs or an agency's, to check against a media plan.

They say: "Check the agency's zip against the media plan" · "Is this package ready for Google?"

1. `check_package` with the package and the sizes asked for: each file measured off its own bytes against its channel's limits.
2. Report it file by file: what is missing, over a limit, or in the wrong format.

### A product's facts changed (`eonik://guide/facts-change`)

A price, an offer, a registration number or an address a creative prints changed.

They say: "The tower project got its RERA number" · "The price is now 1.65 Cr from 1 Nov"

1. `update_project_facts` with each changed fact as a label and its exact words, and the date it takes effect. eonik keeps the earlier version as history.
2. eonik shows which of the project's creatives no longer say what its facts say. Their end blocks are rewritten only when the person presses Update all.

- Never invent a number, registration, price or date.

### Ad copy (`eonik://guide/copy`)

They want Meta or Google copy written or checked.

They say: "Write five Google headlines" · "Check this primary text"

1. Write it, then `check_copy` before you present it as ready.
2. Show each line with its count and its limit.

- A line eonik refuses is rewritten by you and checked again, never trimmed silently.
- A figure no project fact supports is named for the person to source.

### A brand's handover files (`eonik://guide/onboard`)

A brand's files arrive as a folder or a zip.

They say: "My brand files are at ~/brand-files, onboard this"

1. `onboard_brand` with the folder as they said it, or the zip they attached.
2. eonik reads every workbook, document and mark, and asks the person what only they can answer, through your host.
3. It ends with what reached the brand's library and what was not done.

- A part not measured is said as not measured, never as clean.

### The brand and what competitors run (`eonik://guide/brand-and-research`)

They ask about the brand's rules, what they told eonik, competitors, or their own ads.

They say: "What are our brand's rules?" · "Remember: never the old logo" · "What are competitors running?" · "Break that ad down" · "How did our ads do?"

1. The brand: `get_brand_overview`, `search_brand_memory`; a rule or a dated plan they state: `save_brand_note`, `save_dated_plan`, with their sentence exactly, read back.
2. Competitors: `list_watched_competitors`, `list_competitor_ads`, `get_competitor_activity`; a breakdown: `list_ad_breakdowns`, `get_ad_breakdown`, or `request_ad_breakdown` when it has none.
3. Their own ads: `list_my_ads`, `get_my_ad_performance`, `get_my_tested_history`. Any advertiser: `search_ad_library`.

- Say what an ad is and what was recorded about it, not whether it will work.

### What assistants did (`eonik://guide/activity`)

They ask what their assistant or their team did in eonik.

They say: "What did my assistant do this week?" · "Show me the team's activity"

1. `get_activity`: each request with when, who, from which assistant, what was asked, how it ended and whether it was checked. The whole team's needs an admin seat.

## Never

No predictions of how an ad will perform. No budget, launch or pause actions: there are none. No choices made for the person. No number, registration, price or date invented.

Tool details: [reference.md](../../reference.md).
