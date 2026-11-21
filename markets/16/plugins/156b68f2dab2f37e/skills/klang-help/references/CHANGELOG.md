# KLANG Knowledge Changelog

## v0.1 — 2026-10-08 — Baseline and indexing scaffold

- Adopted the uploaded `KLANG_Plugin_Knowledge` directory as the local source of truth for machine-facing Markdown knowledge.
- Preserved the nine source Markdown documents and `retrieval_manifest.json` byte-for-byte.
- Added `guide_index.md` with ReadMe URLs extracted from the existing corpus; **live availability and page titles are not yet independently verified**.
- Established workflow: ZIP local folder → submit to ChatGPT → inspect and revise → return full replacement ZIP → user versions locally → test private Plugin.

### Observations from initial private KLANG AI Help Plugin test (not yet fixed)

- **MIDI device semantics:** Plugin incorrectly suggested selecting `MU128` as a Synth type. The KLANG MIDI Device `Type` field is a role/category (`Generic`, `MidiCV Module`, `Synth`, `Controller`), not a model selector. Document `Device Type ≠ instrument model ≠ MIDI port`, with correct MU128 setup example. Verify exact meaning of `Generic` before writing definitive guidance.
- **Reference behaviour:** When guiding a specific UI step, offer the relevant verified ReadMe guide URL proactively; screenshots/video references where known. A user had to ask explicitly for a guide link.
- **Retrieval strategy:** All nine documents were packaged, but the Plugin reported incomplete reads/truncated retrieval for several large files. Consider compact foundational instructions plus selective retrieval rather than mandatory full-corpus reading.
- **Teaching flow:** First test successfully guided MU128 setup, checked observable success from MIDI TEST random notes, and advanced toward a first machine. Avoid requiring screenshots for every step.
- **Performance:** First response about 54 seconds; later observed response about 28 seconds. Measure again on independent account.
- **Isolation:** Compare Plugin responses on a fresh ChatGPT account to distinguish packaged knowledge from prior-account memory and conversation context.
- **Source availability:** Live ReadMe retrieval sometimes failed; packaged knowledge remained available. Keep live guide references separate from primary knowledge.

### Next update

- Verify guide URLs/titles from published ReadMe and enrich `guide_index.md` with topic, trigger, image and video mappings.
- Revise ontology and MIDI setup knowledge after reviewing exact KLANG UI behaviour.
- Refine Plugin teaching/bootstrap instructions and test retrieval/response speed.

### Source snapshot

The nine `.md` files and retrieval manifest are the untouched baseline imported from the user's ZIP on 2026-10-08. Keep this version in local history before future edits.
