---
name: poolday
description: How to brief, follow and steer a Poolday video or media production task from the chat. Use whenever the user wants a video, clip, image, voiceover, captions or other media made or edited, or asks about a Poolday task.
---

# Working with Poolday

Poolday is an AI video editing platform. Its agent does the production work
in the user's Poolday workspace; you brief it and relay what comes back.
Everything happens in the one workspace the user connected, as that user.

## When to use it

- The user wants a video, clip, image, voiceover, music track, captions or
  a brand-kit application made or changed.
- The user refers to a Poolday task ("my video", "the clip from yesterday").

Do not use it for writing that is not media production, for Poolday billing
or plan changes, or for editing inside another application.

## Starting a task

Call `start_task` once with a brief written as for a skilled editor:

- goal and audience
- length, format and aspect ratio (for example 20 s, vertical 9:16)
- tone and pace
- must-haves: text on screen, captions, a call to action, a voice
- media to use: `asset:<id>` for files already in the Poolday library,
  pasted links (YouTube, TikTok, Instagram, web pages), or `attachments`
  for files the user gave you in the chat

A task runs for minutes in the background. Tell the user it has started and
stop. Do not call `get_task` in a loop; the panel follows the task itself.

Modes: `build` (default) goes straight to making it; `clarify` lets Poolday
ask questions first; `align` has it propose a plan and wait for approval.
Pick `clarify` or `align` when the brief is thin or the stakes are high.
Leave `tier` unset unless the user asks for a specific production tier.

The brief says what to make, nothing else. Never write answers to questions
Poolday has not asked yet into a brief, and never tell it how to behave when
it asks: wait for the question, then send the user's answer with
`answer_question`.

## Files on the user's computer

Call `add_files` before `start_task`. The panel takes drops and uploads;
once a file is in, reference it by the returned asset reference or by name.

## Following a task

Call `get_task` only when the user asks. Report the status in words:

- `working` or `preparing`: say so, no need to poll
- `needs_input`: relay `question` to the user, then send their reply with
  `answer_question` (or `skip: true` if they want Poolday to decide)
- `done`: list the outputs with their links
- `failed`: relay the reason and offer to start again with a clearer brief

`list_tasks` finds a task id when the user refers to earlier work.

## Changing a finished task

Send the change with `send_message` ("make it 15 seconds", "use the
second voice"). It works only while the task is not running; if Poolday
refuses because the task is still working or waiting on a question, say so
and do not start a second task for the same job.

## Credits

Starting and messaging a task uses the workspace's Poolday credits. If a
tool reports there are not enough, tell the user plainly and stop.
