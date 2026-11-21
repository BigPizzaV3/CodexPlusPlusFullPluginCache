---
name: promises
description: Records promises with Zebra while the person works. Use when the person pastes a meeting transcript or a chat thread, or says they committed to something ("I told Ana I'd send it by Thursday", "Leo will review it tomorrow").
---

1. For a transcript or a thread, call the Zebra tool digest with the text and read only what it returns.
2. Call record with each promise: direction mine when the person committed, theirs when someone committed to them, who, what, due when a date was said, and the exact words as evidence.
3. Create the tasks from tasks_to_create in the person's task manager when they have one connected, then call link_task with each promise id and task id.
4. Answer with one line per promise recorded. Leave out anything nobody committed to.
