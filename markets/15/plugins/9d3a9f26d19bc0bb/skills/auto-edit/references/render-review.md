# Review rendered evidence

`render preview` uses the same compiler as the final render, with reduced scale/frame rate by default. `--start` and `--end` select output-timeline seconds. Subtitles are rebased to that range. Use a full-quality final check when a defect depends on pixels or frame rate.

`review` returns actual extracted images, stream metadata, black-frame/silence measurements and a JSON report. Open those image files with the host image tool. Sample more densely around cut boundaries, source actions, caption changes and fast motion. Technical reports leave visual review pending; the director records observations and decisions in director state.

`project validate` includes `quality.findings`, estimated source enlargement, and a review plan. `review` samples up to 24 frames using scene coverage, recorded actions/results, cuts, captions and text settling; `--limit` controls the budget. It also produces `smallScreenFrames` at the configured viewing width. A long film may require additional range previews; 24 frames do not exhaustively prove quality.

New renders save their timeline, director plan, asset metadata, relevant action evidence and preview range in an immutable render context. A later edit does not change the context of an earlier render's review. `reviewPlan.atSeconds` and explicit `--times` are local output-video times; `reviewPlan.timelineSeconds` and quality finding ranges are full-film times. For a partial preview, subtract its `renderRange.start` before choosing `--times`. An unregistered `--input` gets media measurements and generic frames, without attributing findings to the current timeline.

Use `quality.findings` to prioritize inspection. `measurements.nearStatic` identifies nearly unchanged frames, `silence` identifies quiet intervals, and loudness/true-peak values describe audio levels. These measurements do not detect semantic success or guarantee smooth motion. Static specimens, title holds and silent reading time can be intentional.

For a defect, inspect a short sequence around its time, make a concrete change, render that range again and compare actual output. For an intentional choice, record why it serves the brief and which frames/ranges were checked. Do not replace the visual check with an automatically assigned score or an effects quota.

Check source visibility, chronological causality, crop and zoom, protected regions, caption fit and real Chinese glyphs, motion continuity, transitions, and the opening/result/ending. Listen to uncertain audio ranges. Segment-level ASR times are approximate, so inspect synchronization rather than treating timestamps alone as proof.

Intentional black frames or silence are not automatically errors. Diagnose against the brief and actual media. After a correction, inspect the relevant new render and record what changed. Deliver a usable MP4 and applicable subtitle files; retain project JSON and referenced assets for revision.

## Visual upgrades and reused footage (0.5.0)

When the user asks for a visual/backend improvement, inspect the old render context and source frames first. Preserve that `.render.json` as the baseline, then add a scoped request to `director-state.json`:

```json
{
  "revisionRequest": {
    "kind": "visual-upgrade",
    "baselineRenderContext": "outputs/r3-final-EXISTING.render.json",
    "sceneIds": ["the-scene-being-redesigned"],
    "expectedBackends": {"the-scene-being-redesigned":"anatomy"}
  }
}
```

Use an existing project-relative snapshot path, actual scene IDs, and backend expectations only where the brief requires them. `project validate` reports unchanged visual fingerprints and wrong native backends; render blocks these explicit upgrade failures. Ordinary repeat exports remain allowed and report unchanged shots as information.

Change geometry, camera/composition, animation or selected source content to meet the requested result. Changing a filename, project title, narration, encoding or plugin version does not establish a visual upgrade. Inspect the new output frames at matched moments and record the visible difference. Compare `sourceUsage` asset hashes and `spatialRuntime.observed` per scene; a pre-rendered video layer is reported as 2D footage even if its content looks three-dimensional. Clear/archive the completed revision request only after the intended differences are reviewed, not to bypass a failing check.

The report freezes the render revision, source hashes/provenance and observed engine. If a requested backend is absent, runtime/model loading fails or capture evidence is missing, fix the cause and rerender. Do not replace the plugin's failed render with an ad-hoc external script and describe that as plugin capability.
