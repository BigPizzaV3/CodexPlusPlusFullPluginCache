---
name: navigation
description: Find the exact published page or working Studio source, connect an open published page, and read it aloud with the sentence loop.
---

Start here before choosing a reading tool. This is a native reusable connector
guidance workflow, separate from Sesame custom Skills. Hosts may omit
initialization instructions, so reading and pairing tools also point here.

## Choose the source

- “Read this page aloud” or “the page I have open”: call
  `tabularia_pair_published_reading` FIRST with no URL, then follow its sentence
  loop. No source inventory is needed unless pairing cannot find the page.
- An exact published URL: pair with that URL. Never guess a handle, spelling,
  domain, or Chapter slug. A named URL must not attach to an unrelated open page.
- A named title: call `tabularia_list_reading_sources`. Its published and working
  entries are distinct even when they link to the same project. Match title and
  stable ID; use the returned URL. Follow `nextPublicationStart` to finish a
  bounded publication inventory before concluding a title is absent.
- An explicit published or working-draft preference wins. Use manuscript tools
  only for working text. If both sources match and the request does not choose,
  ask one question: “Published version or working draft?” Never silently read
  working wording when published was intended.
- For working sources, cloud reads use the saved Base checkpoint; local reads
  use the connected Studio composition. A cloud listing does not prove Studio
  is open. Call `tabularia_list_drafts` before choosing working Draft content.

## Connect and recover

Connect Tabularia's hosted MCP account in the assistant. Open the exact
published URL in a browser, sign into the same Tabularia account as the MCP
connection, and keep the page open. The verified path needs no manual pairing
code and no Listen modal. If discovery fails, check account match and open-page
presence; reconnect the MCP account when its grant is stale.

If no matching page is open, give the exact discovered URL and these setup
steps. Pairing with a known URL can read without highlighting; the reply says
which mode was obtained. If the URL is unknown, ask for it instead of guessing.
A missing and a restricted publication deliberately share one anonymous-reader
refusal. A revision mismatch means the requested revision does not match the
available cut; reload/restart without claiming a change was independently seen.
Stale saved Studio pagination does not by itself establish a connector defect.

## Read the paired page

1. From pairing, retain sessionId and the exact publication URL.
2. Call `tabularia_read_next_published_sentence` only when about to speak that
   exact sentence. Speak its text verbatim, finish it, and fetch the next one.
   Say no commentary, acknowledgments, or invented transitions between sentences.
3. Clicked-word seeks are picked up by the next call. The server crosses
   Chapters. Stop silently on empty text with done, end, or expiry.
4. When asked to stop, call `tabularia_end_published_reading`. Its explicit ended
   reply confirms closure. A voice hangup is not an established cleanup signal.

The sentence request advances highlighting immediately; this is assistant-paced
highlighting, not proof of audio-player events. Never fabricate playback progress.
Only a host with actual player callbacks uses
`tabularia_read_published_reading_session` and
`tabularia_report_published_reading_progress`. Session status exposes position,
seekVersion, and expiry as control data. Do not speak it.

For stateless text reads, use `tabularia_read_published_page` with the exact URL.
Its control header includes sentence IDs, offsets, nextFrom, expectedRevision,
and nextChapterUrl. Exhaust nextFrom before advancing Chapters; retain
expectedRevision throughout. Control metadata is never narration.

## Voice and author intent

`natural-voice` guides written prose. It is not a speech delivery controller.
Author mood notes are optional interpretive context, separate from manuscript
wording, never spoken. Pass relevant scene intent before reading a passage, and
keep its wording unchanged. Apply only controls the selected engine supports.
Do not claim precise Sesame pause, pitch, emphasis, or SSML controls: none are
established in this interface. Different takes do not prove a note caused the
change. Guaranteed silence gaps need audio segments and a player/editor that
can insert silence; MCP alone cannot control Sesame's player.
