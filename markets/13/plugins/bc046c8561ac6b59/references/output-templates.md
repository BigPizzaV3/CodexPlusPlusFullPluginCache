# WizPrompt Output Templates

Use these templates for consistent ChatGPT output. The host may generate text first, then call save tools only after the user asks to save or the workflow clearly includes saving.

## Single Song

```markdown
**Title:** [Original title]

**Style:** [Focused music-generation prompt with a few coherent musical priorities. Start with genre and mood. Include tempo, key, vocal description or instrumental direction, production palette, mix texture, and constraints. Do not include artist names, song titles, lyrics, or conversational instructions.]

**Exclusions:** [Array of short unwanted genre, vocal, instrument, or production bleed terms. Keep this separate from the style prompt.]

**Settings:** [Model named by the user, vocal/instrumental mode, tempo/key preferences, or other Suno UI settings the user supplied. Do not invent current platform limits.]

**Lyrics:**
[Intro]
[Lyric lines]

[Verse 1]
[Lyric lines]

[Pre-Chorus]
[Lyric lines]

[Chorus]
[Lyric lines]

[Verse 2]
[Lyric lines]

[Bridge]
[Lyric lines]

[Final Chorus]
[Lyric lines]

[Outro]
[Lyric lines]
[End]

**Studio Notes:** [Optional concise notes about structure, motif, or Suno transfer tips.]
```

For instrumental songs, replace `Lyrics` with:

```markdown
**Instrumental Direction:**
[Intro texture]
[Main motif entrance]
[Build]
[Breakdown or contrast]
[Climax]
[Outro]
```

## Refinement

```markdown
**Preserved Strengths:** [What stays from the prior prompt or Suno result.]

**Targeted Fix:** [What changes and why, using user-described feedback only unless a tool provided audio analysis.]

**Revised Package:** [Title, Style, Lyrics or Instrumental Direction, Exclusions, Settings, Studio Notes.]

**Faithful Variant:** [Closest version that protects the original direction.]

**Adventurous Variant:** [Bolder version that explores a different arrangement, energy, or texture without overwriting the original.]
```

## Artist Persona

```markdown
## [Persona Name]

**Sonic Role:** [One sentence describing the character's sound without naming a real artist.]

**Vocal DNA:** [Range, texture, delivery, resonance, articulation, emotional posture, processing.]

**Production World:** [Core instruments, rhythm language, harmonic palette, room/space, signature effect.]

**Lyric Lens:** [Narrative themes, point of view, imagery rules, vocabulary.]

**Prompt Anchor:** [Reusable prompt fragment for future songs.]
```

## Album Or EP Plan

```markdown
# [Project Title]

**Concept:** [One paragraph describing the world, conflict, and emotional destination.]

**Sonic Signature:** [Three recurring production or vocal anchors.]

**Track Map:**

1. **[Track Title]** - [Role in the arc]. [Energy]. [Arrangement job]. [Neighbor relationship]. [Tempo/key if useful]. [One-line style direction.]
2. **[Track Title]** - [Role in the arc]. [Energy]. [Arrangement job]. [Neighbor relationship]. [Tempo/key if useful]. [One-line style direction.]

**Continuity Rules:** [Voice, motif, sonic palette, lyrical boundaries.]
```

## Save Confirmation

Only use this after a save/create/update tool returns success.

```markdown
Saved to WizPrompt.

**Record:** [Name]
**Type:** [Project, persona, prompt, or album track]
**ID:** `[stable ID from tool result]`
```

## Feedback Confirmation

Only use this after `record_prompt_feedback` returns success.

```markdown
Feedback saved to WizPrompt.

**Prompt:** [Name or stable ID]
**Result:** [Rating, linked Suno result, or outcome note]
```

## Save Failure

Use this when a save/create/update tool fails or is unavailable.

```markdown
I created the draft, but it is not saved in WizPrompt yet.

Reason: [Brief recoverable reason from the tool result or missing tool availability.]
Next step: [Retry, link account, choose a project, or keep the draft in this chat.]
```

## Prepared song panel and editorial review

Call `begin_song`, draft, review all seven returned editorial criteria and call `prepare_song` with that review. Use `completed` only when all criteria were assessed with text evidence. Do not present a formatting pass as a musical quality score.

Use the returned Style, Lyrics (or instrumental direction stored in `lyrics`) and Exclusions fields separately. Never put studio notes, labels, review comments or settings into copied lyrics. Keep settings and editorial findings outside them. Show unresolved warnings even when the package is structurally valid.

A successful `prepare_song` result confirms prepared fields and validation, not whether the host displayed its widget. The assistant cannot infer rendering or clipboard success from tool content, structured data or widget metadata. Do not claim that the widget rendered, failed to render or is missing without an explicit host rendering error or the user's report. Normally say “Song fields prepared” and present the returned fields and findings without diagnosing the UI. If the user reports that the panel is absent or an explicit host error confirms it, provide separate fenced text blocks containing the exact prepared fields. When visibility is unknown, phrase optional help conditionally: “If you don't see the copy panel, I can provide the fields as plain text.” Do not rerun preparation or save a duplicate merely to check visibility.

For troubleshooting, first state the preserved elements, one or two targeted field changes, and the recommended Suno operation. Distinguish user-confirmed controls from dated documentation and unknown availability. Provide a plain new-generation fallback when an edit operation is unavailable.
