# Editorial Source Map

The plugin skills are adapted from WizPrompt's local prompt fragments in `lib/prompts/fragments/`. The skills use the editorial ideas while removing unsupported outcome promises, unsupported platform-version claims, and any requirement to claim that output has been saved before a backend tool succeeds.

| Source fragment | Plugin use |
| --- | --- |
| `core-orchestrator.md` | Overall studio stance, direct generation, dense musical specificity. Removed chart-outcome promise language. |
| `provider-syntax.md` | Prompt ordering, style-field discipline, lyrics-vs-style separation, exclusion-field usage, and caution around model-specific claims. Removed fixed Suno-version assertions from skill-facing instructions. |
| `metatag-reference.md` | Section tags, pipe-stacked tags, transitions, and vocal tags. |
| `vocal-dna-library.md` | Persona dossier fields, vocal texture, delivery, resonance, processing, and consistency rules. |
| `artist-sonic-dna.md` | De-identified reference translation patterns. Skills prohibit real artist names in final generation prompts. |
| `production-mastery.md` | Studio language, mix texture, gear color, acoustic realism, and production troubleshooting. |
| `music-theory-standard.md` | Tempo/key/progression choices, genre formulas, and emotional arc mapping. |
| `songwriting-mastery.md` | Section roles, sensory lyric writing, central metaphor, and syllable discipline. |
| `album-mixtape-protocol.md` | Album/EP cohesion, track arcs, vocal lock, sonic signature, harmonic flow, and track-neighbor continuity. |
| `reverse-engineering-protocol.md` | Reference analysis and de-identification. |
| `generation-failsafe.md` | Output completeness checks and separation of style prompt from lyrics. |

When the MCP backend exposes DB-versioned prompt fragments, server responses can include active fragment versions for audit. Until then, this package uses local fragments only as editorial source material, not proof of the active production prompt state.

Runtime skills should call `get_studio_guidance` before drafting, `prepare_song` before saving or revising song packages, `get_creative_context` before continuing saved creative work in a fresh chat, `create_prompt_revision` for faithful or adventurous refinements, `record_prompt_feedback` for Suno outcome notes, and `get_prompt_history` for prior versions, favorites, ratings, and linked result history.
