# Skillsail authoring playbook

Use this reference to turn an outcome map into the right Skillsail components and to execute fragile media, translation, and lifecycle workflows. Tool schemas remain authoritative; inspect the current schema and returned values whenever a field is uncertain.

## Outcome-to-evidence blueprint

For each outcome, record:

- **Action:** what the learner must be able to do;
- **Context:** where, when, or with what constraints;
- **Instruction:** the minimum explanation, demonstration, or worked example needed;
- **Practice:** optional unscored rehearsal that resembles the real task;
- **Evidence:** a graded question only when success must affect score or reporting;
- **Feedback:** why the response works or fails and what to do next;
- **Accessibility:** text alternatives, labels, transcripts, and equivalent controls;
- **Transfer:** a recap, job aid, decision rule, or next action.

## Choose the content path

| Learner task | Use | Reporting |
| --- | --- | --- |
| Read, watch, inspect, compare, or understand | Native slide with `add_slide` | Presentation only |
| Explore, manipulate, decide, or rehearse | JSON Render activity with `add_interactive_activity` | Session-local and unscored |
| Demonstrate mastery that counts | Graded question with `add_question` | Score, completion, resume, and aggregate LMS reporting |

### Native slides

Use an ordinary slide for concise explanation, steps, or a worked example. The six native designs are:

- `statement`: one concise message;
- `note`: a semantic tip, warning, reminder, or callout;
- `quote`: attributed words with an optional source;
- `hero`: a section opener with a strong title and short support;
- `two-column`: a deliberate comparison or contrast;
- `image-overlay`: readable text over one managed image.

For `image-overlay`, create the text slide first, then call `generate_slide_image` with `placement: "replace"`; never invent an asset ID. Native designs use their constrained presentation layout, so do not combine them with arbitrary positioning.

An ordinary slide may use one to four images in `stacked`, `split-left`, `split-right`, or `gallery`. Use more than one only for a comparison, sequence, distinct examples, or visual recap that benefits from simultaneous viewing.

### Preferred unscored activities

Always read `skillsail://json-render/catalog` immediately before authoring or patching a specification. Use the catalog's exact component names, props, events, root policies, examples, and stable element IDs. Never copy an old props schema from memory.

Practice and decisions:

- `Scenario`, `MatchingPairs`, `SequenceBuilder`, `SortingTask`
- `MultipleChoicePractice`, `MultipleResponsePractice`, `FillInBlankPractice`
- `SpatialDragDrop`, `GuidedReflection`, `Checklist`

Exploration and explanation:

- `ProcessStepper`, `Timeline`, `Flashcards`
- `GuidedScreenshotSimulation`, `LabeledGraphic`, `BeforeAfterComparison`

Data and resources:

- `BarChart`, `PieChart`, `LineGraph`
- `NavigationButtonStack`, `AttachmentDownload`, `WebEmbed`

Use advanced roots—`Accordion`, `Card`, `Grid`, `ImageCarousel`, `QuoteCarousel`, `Stack`, and `Tabs`—only when their composition materially improves the learning task. Do not use a carousel for an ordinary gallery or a decorative sequence. Child-only and legacy playback components are not valid new roots.

These activities never affect score or LMS question reporting. Matching, multiple-choice, multiple-response, and fill-in-blank have graded equivalents. Sequence, sorting, and spatial drag-and-drop currently do not.

### Graded questions

The eight formats are `multiple-choice`, `pick-a-side`, `image-choice`, `multiple-response`, `fill-in-blank`, `cloze`, `matching`, and `hotspot`.

- Align the prompt and answer key to one observable outcome.
- Make distractors plausible but unambiguously wrong from the supplied instruction.
- For multiple response and hotspot, the correct array is the exact zero-based index set.
- For cloze, provide ordered blanks and exactly one more `textParts` item than blanks.
- For matching, keep pairs conceptually parallel and avoid accidental wording cues.
- Give correct and incorrect feedback that explains the principle, not merely “Correct” or “Try again.”

For `image-choice`, author `options`, one aligned `optionImageAlts` value per option, and the zero-based correct index. Preserve the server-returned `imageChoiceOptionIds`. Attach each option image with `set_question_image` using `slot: "option"` and its exact `optionId`. On later edits, use complete `imageChoiceOptions`, retain IDs for preserved or reordered options, omit an ID only for a new option, never provide `imageId`, and do not combine this identity-bearing patch with positional `options` or `correct`.

For `hotspot`, create one to ten rectangles with `x`, `y`, `width`, and `height` as percentages from 0 to 100, all within the image. Provide aligned `hotspotLabels`, localized `imageAlt`, and the exact correct index set. Then attach the verified image with `set_question_image` using `slot: "prompt"` and no `optionId`.

## Upload resources

Choose exactly one upload flow.

### Small in-call upload

1. Call `upload_resource` with `base64`, `contentType`, and `fileName`.
2. Treat the returned resource as already verified. Do **not** call `process_resource_upload`.

Use this only when the client can safely represent the bytes in a tool call. Never ask a client without byte access to paste base64.

### Signed upload

1. Call `prepare_resource_upload` with `fileName`, `contentType`, and the exact `fileSize`.
2. PUT the raw bytes to the returned ten-minute `uploadUrl`, using the same Content-Type and no Authorization header.
3. Call `process_resource_upload` with the returned `resourceId` exactly once.
4. Continue only when `success: true`; report `parsed` or `rejected` when relevant.

Verification or parser rejection permanently deletes the invalid pending resource. `delete_resource` separately deletes the workspace resource and may report `cleanupPending`. `get_resource_download_url` returns a private two-hour link; it is not a package-local learner attachment.

## Attach and manage media

Author learner-facing accessibility copy first. Pass explicit `resourceId` or `assetId` values when known; omission on several set tools selects the actor's most recent upload and is safe only when that target is unambiguous.

### Learner attachments

1. In an activity spec, create an `AttachmentDownload` with stable `elementId`, `assetId: null`, and no `href`. Never invent or directly author an asset ID.
2. Upload and verify a PDF, DOCX, XLSX, or PPTX.
3. Call `set_activity_attachment` with the exact `componentId`, `elementId`, and `resourceId`.

The managed copy is available in preview and packaged HTML5, SCORM, xAPI, and cmi5 exports. `remove_activity_attachment` clears only the managed file across every language; it never removes an external HTTPS `href`.

### Activity images

Use `set_activity_image` with exact `componentId`, catalog `elementId`, verified JPEG/PNG `resourceId`, and this slot grammar:

- omit `slotId` for a fixed single-image slot;
- use the item ID for `ImageCarousel`;
- use `background` for `SpatialDragDrop`;
- use `before` or `after` for `BeforeAfterComparison`;
- use `background` or `character:<characterId>` for a dialogue-presentation `Scenario`.

`remove_activity_image` uses the identical target grammar. Both set and remove operations affect every language.

### Question images

Use `set_question_image` only after the question contains nonblank localized alt text in every configured language:

- `slot: "prompt"`, without `optionId`, for an optional question prompt or the required hotspot image;
- `slot: "option"`, with a stable returned `optionId`, for image-choice.

`remove_question_image` uses the same target and affects every language.

### Slide images

`generate_slide_image` consumes existing organization allowance and sends the prompt to the configured external image-generation service. Always set `placement` explicitly:

- `replace` resets the slide to one generated image and can supersede prior managed images;
- `append` preserves images and adds one, sequentially, up to four.

Choose a responsive layout preset and `contain` or `cover`; never supply HTML, CSS, coordinates, or arbitrary URLs. If the result reports `compositionConfirmed: false`, inspect the slide before another media change.

`edit_image` requires the exact organization-scoped, same-module image `assetId`, not an external URL. It sends a short-lived private copy and prompt to the configured external image-editing service, consumes allowance, and replaces the reference automatically when the source belongs to a slide; otherwise it stores a standalone derivative. Confirm the source and intended target when ambiguous.

### Slide video, logo, and voiceover

- `set_slide_video` accepts a verified MP4, MOV, or WebM and replaces the video across every language. Call it with `accessibilityPolicy: "preserve"` when existing captions and transcript still describe the replacement. Calling it with `accessibilityPolicy: "clear"` removes `videoCaptions`, `videoTranscript`, and `videoTranscriptLabel` in every language and requires fresh approval.
- `set_module_logo` accepts an exact verified image `resourceId`. Passing `null` removes the logo; after confirmation, also pass `confirm: true`.
- `generate_slide_voiceover` always targets every configured language and uses configured external narration and text-to-speech services. A `customScript` is valid only for a single-language module; omit it for multilingual modules. It consumes allowance and may partially succeed, so report `successLanguages`, `failedLanguages`, and `fallbackLanguages`.

## Translation-aware editing

Inspect the `translation` object returned by every creation or `update_component` call:

- `attempted: false` plus nonempty `synchronizedLanguages` means a structural design/layout change synchronized without a provider call or billing;
- `attempted: false` with no synchronized or failed languages means no target-language update was needed;
- `failedLanguages` retained prior content;
- `conflictedLanguages` means generated results were discarded after a concurrent source edit.

Retry a partial translation failure only by resending the same patch with `retranslate: true`. This reruns and bills every configured target language, not just failed languages, so obtain explicit approval.

`narrationSourceChangedLanguages` means existing narration predates changed slide text, not necessarily that it is wrong. Report the languages and offer regeneration; never call `generate_slide_voiceover` automatically because it re-records and bills all configured languages.

## Versions, deletion, and sharing

- Call `list_versions`, restate the exact module and returned version, and obtain fresh confirmation before `restore_version`. Restore replaces the current title, slug, structure, and every component, changes a live share immediately, and creates a new version for the restored state.
- Obtain fresh exact-target confirmation before `delete_component`, `delete_resource`, or `delete_module`. Do not promise recovery. Module deletion also removes the linked chat, messages, resources, components, sharing settings, and versions.
- Use only `set_module_sharing` and pass only requested fields. Private state clears template, password, and comments; template state forces public and clears password and comments. The tool accepts only `password: null`, never a new passphrase. Comments cannot be enabled on a private module or template.
