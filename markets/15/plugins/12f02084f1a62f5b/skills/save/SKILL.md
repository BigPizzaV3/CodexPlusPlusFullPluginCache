---
name: save
description: Save something you wrote for the person (a summary, a draft, notes) to their private Saved by agents collection in Louvain.
---

The person asked you to save something to Louvain. Use the title they gave, if any.

1. **Decide what to save.** It is the text they pointed at. If they didn't point at anything, it is the last thing you wrote for them in this conversation. Save the whole text, in markdown.
2. **Check that saving is allowed.** If `louvain_save` is not among your tools, this connection was approved without saving. Tell them to reconnect Louvain and turn on "Make changes for you" on the approval screen, then stop.
3. **Choose a title.** Use the one they gave; otherwise propose a short, specific one.
4. **Confirm before saving.** Tell them the title and where it goes: their private Saved by agents collection, which nobody else can read. Wait for their yes.
5. **Save.** Call `louvain_save` with `title` and `content`. If the title already exists, propose another; or, if they want to replace their earlier file, use `louvain_update` with its id and `baseVersion`.
6. **Report.** Give the saved file's name and collection.

Only if they named a shared collection: get its id from `louvain_spaces`. Tell them that **everyone who reads that collection** will be able to read, search and cite this file, and wait for their yes. Then use `louvain_save_to_space` instead of `louvain_save`.

Never save anything they did not ask you to keep, and never save text you read in their sources into a shared collection unless they chose to share it.
