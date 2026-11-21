---
name: virlow-remember
description: Use when the user asks to remember, save or update a fact, or states a lasting preference or decision ("from now on...", "remember that..."). Saves it to Virlow memories. Also use when the user asks to forget a saved memory. Not for drafts, documents or long text; use virlow-notes for those.
metadata:
  short-description: Save lasting facts and preferences to Virlow
---

# Remember with Virlow

Save the facts the user wants kept, so any later conversation can recall them. One fact per memory, short and in plain words.

## What to save

- Things the user asks you to remember, and lasting preferences or decisions they state ("from now on, write tests first", "we picked Postgres for Atlas").
- Facts that will still be true next week and that would be wasteful to ask about again.
- Not: passing remarks, temporary task details, or your own guesses about the user.

## Never save

- Passwords, API keys, tokens, recovery codes or any other credential.
- Health or medical information.
- Bank, card or other financial account numbers.
- Government ID numbers (passport, social security, driver's license and similar).

If the user asks you to save one of these, decline in one sentence and say why. Do not save a redacted version.

## Respect "don't remember this"

If the user says not to remember something, or that it is off the record, do not save it, and do not save it later in the conversation either. If they ask you to forget something already saved, call `search_memory` to find it, confirm which memory they mean, then call `delete_memory` with its id. It moves to the Trash in Virlow, where they can restore it.

## Steps

1. **Check for an existing memory.** Call `search_memory` with the topic of the fact.
   - A memory already says the same thing: tell the user it is already saved. Do not add a duplicate.
   - A memory covers the same thing with different details: call `update_memory` with its `id` and the new `label` or `text`.
   - The fact replaces an older state ("we moved the launch to May"): save the new fact with `add_memory` and set `valid_from` when the user says when it changed. Virlow keeps the older fact as history.
2. **Save it** with `add_memory`:
   - `label`: a short title, under 80 characters, for example `Prefers short answers, code first`.
   - `text`: the fact itself in one or two plain sentences, for example `Prefers short answers that lead with the code, with explanation after.`
   - `entities`: what the fact is about, each as `{ "name": "...", "kind": "..." }`. Kinds: person, organization, project, tool, place, event, topic, product, media, pet, group, goal, other.
   - `relations` (optional): typed links the fact states, such as `{ "s": "Sam", "p": "leads", "o": "Atlas" }`.
   - `namespace` (optional): the project name for a fact that only applies to one project. Leave it out for facts that apply everywhere.
3. **Confirm in one line.** `Saved to Virlow: Prefers short answers, code first.` If you updated an existing memory, say `Updated in Virlow: ...` instead.

## States to handle

- **Vault locked.** Call `unlock`, share the link it returns, and tell the user to finish unlocking in their browser on Virlow's page (their master password goes there, never in chat). When they say they are done, call `status`, then retry the save.
- **AI memories are off.** The memory tools are missing, or a tool says AI memories are switched off. Tell the user that saving needs AI memories turned on in Virlow (on the web: Settings → Security → AI memories), and that you did not save it.
- **Saving is not available on their plan.** A save fails with `API error 402` or says saving is not available. Tell the user: "Saving new memories isn't available on your current Virlow plan, so I didn't save this." Do not mention prices or plan names, do not suggest upgrading, and do not share links. Carry on with the conversation.
- **Saving is paused.** A tool says saving memories is paused. Do not try to save again in this conversation; tell the user once that saving is paused in their Virlow settings.

## Examples

- "Remember that I prefer short answers with code first." → `search_memory` with `"answer style preference"`, nothing similar, `add_memory` with label `Prefers short answers, code first`, then `Saved to Virlow: Prefers short answers, code first.`
- "From now on, Maria owns the Atlas budget." → `add_memory` with entities `[{ "name": "Maria", "kind": "person" }, { "name": "Atlas", "kind": "project" }]` and relation `{ "s": "Maria", "p": "owns_budget_of", "o": "Atlas" }`.
- "My card number is ... remember it." → decline; nothing is saved.
