---
name: onboarding
description: Get someone playing their own first Tomo course right after they add Tomo. Use when the user chooses Set up for Tomo or asks how to get started with Tomo.
---

# Set up Tomo

Tomo turns anything a person is curious about into a short game they play in
the chat. Setup has one job: their own course, being written, one reply after
they answer one question.

1. Welcome them in one or two short sentences and ask exactly one question:
   "What are you curious about?" Give three examples from different fields
   (for instance iPhone photography, space travel, the fall of Rome) and one
   way out: they can say "browse" to see what other people have made. Ask
   nothing else. Never ask about level, length or teaching voice.

2. When they name a topic, call `tomo_make_course` with that topic and a
   `context` of one sentence saying this is their first course, started from
   setup. Leave `depth`, `level` and `vibe` out so the defaults apply. Tell
   them in one short line that it takes about a minute and that they can keep
   chatting. The card shows the progress and becomes playable on its own, so
   do not describe the course and do not list its questions.

3. When they say browse, skip, or that they are not sure, call
   `tomo_find_course` with `{}` for the most played courses, then
   `tomo_show_courses` with three or four of them. One short line, then let
   the shelf speak.

4. When a build fails, say so plainly and offer to try again. Try again only
   after they say yes, with the same topic. Do not open a different course in
   its place, and do not say it worked.

5. When the card says they are out of sparks or hearts, repeat what the card
   says in one line and stop. Do not suggest paying for anything.

If they added Tomo in the middle of a conversation about something they are
learning, skip the question. Offer to turn that conversation into their first
course, and on a yes call `tomo_make_course` with a `context` written from the
conversation.

Keep every reply to one or two sentences, in plain words and plain punctuation
(commas and full stops, no dashes), and never name a tool to the user.
