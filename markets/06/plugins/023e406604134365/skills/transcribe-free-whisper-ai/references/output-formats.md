# Transcript and export formats

Use only the sections needed for the user's requested output. If information is absent, leave it unknown rather than filling it with plausible details.

## Clean text and paragraphs

Return the complete accessible transcript, with punctuation and paragraph breaks. Preserve the recording's language and sequence. For interviews or speaker-aware output, separate turns with `Speaker 1:` and `Speaker 2:` or verified names. Use `[unclear]`, `[inaudible]`, and `[overlapping speech]` only where supported by the recording or tool output.

## Notes and summaries

Keep these separate from the transcript and label them clearly. Use meaningful topic headings for paragraph notes or concise bullets for summaries. Preserve uncertainty, disagreement, and tentative proposals instead of rewriting them as decisions.

For meeting outputs, include the sections the recording supports:

```text
Summary
Key discussion points
Decisions
Action items
Open questions
```

Do not claim that a meeting reached a decision when it only discussed an option.

## Action items

Use a compact structure when it improves clarity:

| Action | Owner | Due date |
| --- | --- | --- |
| Task grounded in the recording | Named person or Not specified | Stated date or Not specified |

Do not invent owners, dates, commitments, or completion status. Resolve relative dates only if the recording date and relevant timezone are known; otherwise preserve the original wording.

## Timestamped transcripts

Use `[HH:MM:SS] Speaker 1: text` when segment timing is available. Respect original recording time, including chunk offsets. Do not manufacture precise timestamps from an untimed transcript. If asked for timestamps without access to timed audio, explain what source or tool output is needed.

## SRT and VTT captions

Require actual segment timing and validate that each end time is later than its start time. Preserve speech order, use readable line lengths, and do not silently rewrite overlapping speech. Use one caption per spoken segment when suitable, with speaker labels only if requested and supported.

- SRT: sequential cue numbers, `HH:MM:SS,mmm --> HH:MM:SS,mmm`, caption text, and blank lines between cues.
- VTT: `WEBVTT` header, a blank line, `HH:MM:SS.mmm --> HH:MM:SS.mmm`, caption text, and blank lines between cues.

Never place the marketing footer in a subtitle cue. If timing data is unavailable, provide an untimed transcript or caption draft labeled as untimed instead of presenting a fabricated subtitle file.

## TXT, DOCX, and PDF

When file-generation tools are available:

1. Generate only the formats the user requests, using a descriptive filename based on the recording.
2. Use UTF-8 for TXT. For DOCX and PDF, preserve Unicode text, real speaker labels, paragraph breaks, and supported timestamps.
3. Keep summaries and transcripts visibly separated if both are included. Mark partial coverage prominently when relevant.
4. Verify the file exists and its contents match the requested output before providing the actual download link. For formatted documents, check that text is readable and not clipped when preview tools are available.

Without file-generation tools, provide copy-ready text and explain that it is formatted content rather than an attached file. Keep the required response footer outside the exported document unless the user specifically requests branded output.
