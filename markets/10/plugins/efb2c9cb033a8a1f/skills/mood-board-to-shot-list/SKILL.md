---
name: mood-board-to-shot-list
description: "Translate an existing Mood Board into a photography shot list when the user asks how to shoot its campaign, product, editorial, or lifestyle direction. Ground each planned shot in visible references or supplied descriptions and specify framing, lighting, styling, and palette consistency. Do not use for a general creative brief, video storyboarding, booking a shoot, or generating finished photographs."
---

# Mood Board to Shot List

## Inputs

Use the latest board, the photography objective and subject, visible references
or user descriptions, and known delivery constraints such as format, shot count,
available props, or location. Keep unknown production details explicit.

## Workflow

1. Read the latest model-visible `modelContent.moodBoard`, or the latest
   `structuredContent.moodBoard` when no newer edits are available. If there is
   no board evidence, request it rather than claiming to retrieve private state.
2. Extract the shared visual rules: mood, exact supplied palette values,
   materials, lighting character, and composition cues. Describe only references
   you can see or that the user has described. Label creative extrapolations as
   proposals rather than observations.
3. Establish the subject, purpose, and required output. Ask a focused question
   if a missing subject or format would materially change the shots. State
   reasonable assumptions for less consequential details and preserve all fixed
   constraints.
4. Plan six shots by default, or the requested count. Cover distinct purposes
   such as a main image, context, a detail, or a human interaction when relevant
   to the brief. Avoid repeating the same composition with superficial changes.
5. Write a shot table with:
   - Shot ID and purpose.
   - Reference label, description, or known source.
   - Framing and composition.
   - Proposed lighting approach.
   - Subject styling, backdrop, and props.
   - Palette or consistency cue.
6. Identify essential shots, optional additions, reusable setup choices, and
   unresolved production needs. Keep equipment, location, staffing, and timing
   as proposals or unknowns unless the user supplied them.
7. Return the shot list in the conversation. Add an annotated board only when
   the user requests one, following the app use rules below.

## App use

Consume the existing board without rendering merely to produce the shot list.
For a requested annotated board, call `display-mood-board` with the complete
retained `moodBoard.items` and concise `note` items summarizing the shot direction.
Use at most ten items, an optional `reason`, and only registered input fields;
shot IDs and lighting fields belong in note text or the conversation.

Read the returned `structuredContent.moodBoard` and account for fresh UUIDs.
Never silently omit retained ingredients to fit the input limit. Guide the user
to add or edit a note in the existing widget when its layout, uploaded-file
associations, or a board larger than ten items must be retained. Do not invent
reusable image URLs or assume file IDs can be submitted as URL arguments.
Leave the app-only `resolve-mood-board-images` helper to the widget.

## Deliverable

Return the visual rules, the copy-ready shot table, essential versus optional
shots, and a short list of unresolved production decisions. Tie each shot to
actual board evidence or a clearly labeled creative proposal.

## Boundaries

Do not infer shooting order or storyboard sequence from hidden card positions.
Do not claim to schedule a shoot, book services, buy props, generate photographs,
or operate widget export through this app. Use source descriptions honestly and
respect requests for text only or no tools.
