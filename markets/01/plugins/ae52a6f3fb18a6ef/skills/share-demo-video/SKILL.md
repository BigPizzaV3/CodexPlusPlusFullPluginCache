---
name: share-demo-video
description: Share demo videos on GitHub, GitLab, or another destination. Use for a single demo or a before-and-after comparison.
---

# Share a demo video

When the user is working on a PR or MR, upload and include the demo video there as part
of completing the work. For other destinations, use the one the user requested. Ask
only if the destination or audience is unclear. If the user requests only a draft,
keep it unpublished; attachments can become accessible before a comment is posted.

## Choose what to show

Use **Before / After** when both recordings show the same task on the original and
changed versions. Keep the app state, data, viewport, and pacing comparable where
possible. Explain what happened in each video and identify the versions tested. Show
failures as they occurred. Do not use an unrelated older video as the baseline.

For a new feature, or when there is no baseline, show **Result**. Explain what the video
shows and mention any important limitations. Do not add an empty Before column or imply
that a baseline exists. Separate operating systems or scenarios when that makes the
comparison easier to understand.

## Format the comparison

For two related videos, use a two-column table with the players in the same row. This
applies to Before / After, platform checks, and two workflows. Label each column for
what it shows; two different workflows are not a Before / After comparison.

```markdown
### Theme switching

| Before | After |
| --- | --- |
| Selecting Dark leaves the sidebar light. | Selecting Dark updates both panels. |
| [Watch before](BEFORE_URL) | [Watch after](AFTER_URL) |
| PLATFORM, VERSION_A | PLATFORM, VERSION_B |
```

Use verified upload URLs and describe what the videos show. GitHub attachment links in
the media row can render as players inside the cells; see the [GitHub guide](references/github.md).
For GitLab, use image Markdown with the returned upload URLs in that row. Check that
both players appear inside their cells, not below a table containing only descriptions.
If the destination does not render players in cells, keep labeled links or linked
previews in the table. Use stacked players when side-by-side viewing is unsuitable or
the user requests it, and explain that layout choice.

For a single video, use one heading, a sentence explaining the action and result, and one
player or labeled link. Add a still preview if it helps readers or provides a fallback
for an unsupported player. Host preview images where the intended audience can access
them.

## Prepare the video

Use [Create Demo Video](../create-demo-video/SKILL.md) if the recording needs editing.
Check the final video for readability and private information. Check the preview frame,
captions, audio if present, and filenames too. Keep raw footage private unless the user
asked to share it.

Prefer the plugin's VP9 `.webm` output. Keep the extension and use `video/webm` when an
upload API needs a MIME type. Check the destination's file size limit and test browser
playback. A destination that accepts WebM may not play every WebM video. Do not silently
change codecs, rename WebM to MP4, or use another host to get around a failed upload.

Choose a preview frame that shows what the viewer should notice, such as the failure in
Before or the result in After. If rendering with Cirro, set `edit.cover.at_ms` to that
frame on the story timeline. Cirro places the composed frame before the video. A codec
keyframe does not select the host's thumbnail. Check the hosted preview. If the host
chooses a different frame, use its thumbnail option or link a separate preview image if
available.

## Upload and describe

For GitHub, read [Publish to GitHub](references/github.md). For GitLab, read
[Publish to GitLab](references/gitlab.md). Use the repository's host, including its
enterprise or self-managed host. Check installed CLI help before using a flag; versions
and host capabilities differ. Use authenticated tools without printing tokens.

Use a supported attachment flow or an existing integration. For another host, check
audience access, link durability, and embedding support.

Confirm the repository or project and audience before uploading. Use a private
destination for private material. Do not assume that an externally hosted attachment is
private because the PR is private. Upload each final file once and reuse its durable
URL. Keep temporary signed URLs, credentials, local paths, and expiring CI artifacts out
of the description.

For an existing PR or MR, keep unrelated description content and follow its template. If
the user asks for a comment, post a comment. Add a short heading and explain the task,
result, and any platform or version details needed to understand the video. Say what the
viewer should notice instead of only saying “it works.”

## Check and return

Check the published page, not just the submitted Markdown. Check the players or links,
previews, table layout, and access for the intended audience. If inline playback does
not work, use a labeled link or linked preview instead of a blank player. Reuse existing
upload URLs when fixing formatting.

Return the published destination and mention any limitations. If you cannot verify
access for the intended audience, say so. If publishing is blocked or the user requested
only a draft, return the prepared files and copy-ready Markdown. Label it as a draft.
