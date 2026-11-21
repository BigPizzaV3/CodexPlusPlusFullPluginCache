---
name: album-planning
description: Plan cohesive albums, EPs, mixtapes, and multi-track worlds with optional track-level saves to WizPrompt projects.
---

Use this skill when the user asks for an album, EP, mixtape, playlist concept, tracklist, album world, or multiple connected songs.

Follow the Album Or EP Plan template in `../../references/output-templates.md`.

Workflow:

1. Call `get_studio_guidance` with `workflow: "album"` when the tool is available.
2. If continuing a saved album or project, call `get_creative_context` before planning so approved persona, track history, and album direction carry into the new chat.
3. Infer a cohesive concept if the user gives only a mood, title, genre, or seed idea.
4. Choose a track count from the user request. If absent, use a compact album-sized plan for "album" and a compact EP-sized plan for "EP".
5. Define one sonic signature that recurs across the whole project.
6. Keep vocal identity, lyrical point of view, and central imagery consistent across tracks unless the user asks for a compilation-style project.
7. Provide a track map with each track's role in the arc, energy, arrangement job, and relationship to neighboring tracks. Add tempo/key guidance when it improves continuity.
8. Call `review_album_continuity` for a saved project before adding a track, supplying `song` and `intended_track_role` when known. Review text findings, retain intentional artistic repetition, and disclose missing context. Save an approved `track_arc` through `save_creative_brief` when saving is requested. If the user wants complete songs for the project, generate each track using the `music-prompt-lyrics` workflow and call `prepare_song` before any track save.
9. If save tools are available and the user asks to save, create or fetch the target project first, explicitly passing the requested `type` (`Album`, `EP` or `Single`) when creating it; ask if unspecified, then call the appropriate project or prompt save tool for each finished track. Include an `idempotency_key` for create/save retries. Confirm saved only for tracks whose tool calls succeed.

Quality checks:

- The project has a clear emotional arc.
- Each track has a distinct job in the sequence.
- Track roles explain how each song affects its neighbors.
- The recurring sonic signature appears in track directions.
- Save status is tracked per project or per track; never imply all tracks saved if only some tool calls succeeded.
