# Video QA Checklist

## Code and preview

- Formatting passes.
- Type checking passes.
- Linting passes.
- Representative frames render at the hook, each cut boundary, each overlay, the payoff, and the final frame.
- Text remains inside safe areas and does not cover key faces or action.
- Crop, scale, and background treatment work for both portrait and landscape sources.

## Full render

- Output duration matches the intended timeline.
- Resolution, frame rate, codecs, pixel format, and color tags match the delivery target.
- Audio exists, remains synchronized, and does not clip.
- Loudness is appropriate for the target platform.
- Black-frame detection finds no unintended gaps.
- Silence detection finds no unintended long gaps.
- The first and last frames are intentional.
- A final contact sheet shows no broken frames, blank overlays, or missing sources.

## Truth and usability

- Every factual overlay is supported by the supplied clips or user context.
- Low-confidence speech has not become asserted dialogue.
- Spelling, spacing, names, and Korean line breaks are checked.
- The final file opens in a standard player.
- File size is plausible and a hash can be produced for copied deliverables.
- Any Desktop or upload-location copy matches the project master by hash.
