---
name: edit-a-session
description: Change music in an existing CookUp session, such as a melody, drums, sounds, tempo, arrangement or mix, or undo or redo a change. For example "make the hi-hats busier", "replace the counter melody", "make it 64 bars" or "undo that". Use when the user refers to a session or the CookUp panel already in the chat.
---

# Edit a CookUp session

Explicit user instructions always take priority over these guidelines.

## Steps
1. **Which session.** Use the session from the latest CookUp panel or tool result, or the one the user names. If none is clear, call `list_sessions` or ask. Never guess a code.
2. **Read first.** Call `get_edit_context` for exact track and clip IDs, the current notes and `expectedVersion`.
   - Use focused mode for the part being changed.
   - Before replacing a clip, fetch every page of its notes: notes you didn't fetch are not silence.
   - A selected clip is a reference, not permission to change locked tracks.
3. **Change only what was asked.** Keep everything else as it is.
   - For a small change, use the focused tool, such as `write_midi_notes`, `set_track_mix`, `assign_drum_sound` or `set_tempo`.
   - For several changes, send one `apply_session_edit` batch.
   - Leave the mix alone unless the user asks (the default is preserve mode).
4. **New sounds.** Follow the choose-sounds skill.
5. **Locks.** Respect session locks. Change them with `set_session_constraints` only when the user asks.
6. **Confirm.** Report the change only after the tool confirms it is applied. Note the returned `editId`.
7. **Undo or redo.** Call `get_edit_context` for the current version, then `restore_session_version`:
   - pass the real `editId`;
   - use `variant` `before` to undo, `after` to redo.
8. **Finish.** End with one `open_session` call.

## If something fails
- If an edit is refused because the session changed, read `get_edit_context` again, fix the commands and retry once.
- Otherwise, report the error plainly. Never say an edit was saved when it wasn't.

## Never
- Invent IDs, versions or edit IDs.
- Change parts the user did not mention.
- Claim you heard the change unless you listened to audio a tool returned.
