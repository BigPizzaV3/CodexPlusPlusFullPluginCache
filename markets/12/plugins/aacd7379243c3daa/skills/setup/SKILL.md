---
name: setup
description: Set up the Basecamp plugin after it's installed — confirm the connection and say what the person can ask Basecamp for. Use when the person chooses Set up for Basecamp or asks to set up Basecamp.
---

# Set up Basecamp

Confirm Basecamp is connected and tell the person what they can ask for.

1. Call `get_me` with `{}` and greet the person by name, naming the Basecamp
   account this connection works in. If it fails, say Basecamp isn't
   connected yet and stop.
2. Tell them, in a sentence each: they can ask for their tasks, what's due,
   and what's new for them at any time; and they can name a project in any
   request — when a request needs one and doesn't say which, you'll ask.

If they installed the plugin in the middle of a task, return to that task.
