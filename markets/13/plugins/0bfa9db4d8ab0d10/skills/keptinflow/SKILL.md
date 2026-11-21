---
name: keptinflow
description: Find and read what KeptInFlow saved on the user's PC (meeting transcripts, copied text and snips, notes, and text seen on screen), then use it to answer questions or draft follow-ups.
---

# KeptInFlow

KeptInFlow runs on the user's Windows PC and keeps what they do there. These
tools read what it already saved. They never change anything. Reach for them
when the user mentions something they said in a call, copied, snipped, wrote
down, or saw on screen, and it is not already in the conversation.

Every list or search result carries an id. Pass that id to the matching `get_`
tool to read the whole item.

## Find a meeting and read its transcript

1. Call `list_meetings` for recent calls, newest first. When the user names a
   topic or a person instead of a time, call `search_meetings` with those words.
2. Pick the meeting that matches what they said ("this morning's call", "the
   sync with Dana"). If two could fit, ask which one.
3. Call `get_meeting_transcript` with its id. Quote short lines with the
   speaker's name when you rely on them.

A meeting marked "not transcribed" has no text yet. Say so rather than
guessing what was said.

## Draft a follow-up email

Read the transcript first. Then write a short email: thank the attendees, sum
up what was decided, and list each action item with its owner and due date
when one was said out loud. Never invent an owner or a date. Leave a clear
placeholder instead.

## Find something the user copied or snipped

- "What did I just copy?": call `search_captures` with no query for the newest
  items.
- Otherwise call `search_captures` with the words they remember, then
  `get_capture` for the full text. Snips are searched by the text read out of
  the image; the image itself is never returned.

## Find something the user saw on screen

Call `search_screen_memory` with the words that were on screen. Add `app` or
`day` (YYYY-MM-DD) when the user gives them. Read a hit in full with
`get_screen_frame`. If Screen Memory is off on the PC, the tool says so; tell
the user where to turn it on rather than retrying.

## Find a note

Call `list_notes` (optionally with a query), then `get_note` for the whole
thing.

## Show the user their items

`list_recent_items` returns recent meetings, captures, and notes together,
newest first, and opens the KeptInFlow view. Pass `query` to search across all
of them, including Screen Memory, or `kind` to show one kind.

## When the PC is not reachable

If a tool answers that KeptInFlow isn't running on the PC, or that ChatGPT
access is turned off, pass that on in plain words and stop. Do not retry in a
loop.
