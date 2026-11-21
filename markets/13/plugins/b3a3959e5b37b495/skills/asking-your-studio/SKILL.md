---
name: asking-your-studio
description: How to work in a creator's Agent Social account through the Agent Social connector — start with learn_agent_social for this session's instructions and the current guide (and read it again after a summary of the conversation and before the first change of each day), read and watch freely, ask the creator's studio for every change in one plain line, follow its turn to the end, look properly at the pictures and renders that come back, and take the next step. Use it whenever the creator asks for anything in Agent Social.
---

# Asking your studio

The creator's Agent Social studio makes every change to their films and posts. You read, watch, judge and ask.

1. **Start with the guide.** At the start of the session, before anything else, call `learn_agent_social`, and call it again after any summary of the conversation and before the first change of each day. It returns this account's instructions and the complete, current guide: films, clips, moments, place views, how to point the studio at exact pictures, how to work step by step, and everything the studio can do. Agent Social keeps it up to date, so follow what it returns over anything written here.
2. **Read and watch freely.** Your other tools read the creator's work: find it, read episodes, chapters and clips, and look at characters, places and posts. Reading and watching cost nothing, so do them without asking.
3. **Ask in one plain line.** Gather what you need first (which clip or picture, and what is wrong with it), then call `talk_to_agent` once, with the line the creator would type, in their own words and adding nothing they did not ask: "Generate chapter 1, clip 1." To point the studio at exact pictures (the place view that looks the right way, the moment to keep the people from), attach them as talk_to_agent pictures by kind and id, each with a note.
4. **Follow the turn.** After asking, tell the creator in one line what you asked, then stay with it: call `get_turn_result` with wait_seconds 45, and again with the since each answer returns, saying nothing in between, until the turn is done, failed or stopped. Then tell the creator what happened in one short report: what it made or changed, each problem, and the studio's question if it asks one. Where the app draws cards, the card shows the work and carries the chat's link, so do not repeat it. Elsewhere give the chat's link once and invite the creator to open it to watch (open it once yourself if you can open pages, never reload it).
   When the creator asks to see a film, chapter, clip, post or running task, call `open_in_app`: it draws it in the chat.
5. **Look at what came back.** Open every picture the result returns and compare it with what it was made from, and watch every render frame by frame with `watch_clip`. Frames have no sound: say you could not judge it.
6. **Take the next step.** If something is wrong, ask the studio to fix that one thing, saying what you saw. If it is right, tell the creator and move on to the next thing they asked for.

A studio turn can spend the creator's credits: ask only for what they asked, and never send a failed paid step again yourself.
