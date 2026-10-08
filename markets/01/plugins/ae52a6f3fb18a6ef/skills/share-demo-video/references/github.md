# Publish to GitHub

GitHub accepts `.webm` attachments. Check the
[attachment limits](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)
for the repository's plan and your access.

When the installed CLI supports it, use the documented
[`--attach` flow](https://docs.github.com/en/github-cli/github-cli/attaching-files-with-github-cli).
GitHub requires push access to the repository for attachments. For example, check that
`gh pr comment --help` lists the flag before running:

```sh
gh pr comment PR_URL --body-file "/absolute/path/evidence.md" --attach "/absolute/path/demo.webm"
```

For a standalone player, put `![](/absolute/path/demo.webm)` in its own paragraph.
For two related videos, put Markdown links in a two-column table instead:

```markdown
| Before | After |
| --- | --- |
| Completed issues still count as open. | Completing an issue reduces the open count. |
| [Watch before](/absolute/path/before.webm) | [Watch after](/absolute/path/after.webm) |
```

Pass both files with `--attach`. The CLI replaces local paths with durable attachment
URLs. GitHub can render those linked attachments as players inside table cells. For
already uploaded videos, use their existing URLs directly; do not upload them again or
add duplicate players below the table. Use platform or workflow names as column labels
when the videos are not a Before / After comparison.

Check the published layout. A table and two players somewhere on the page are not enough:
both players must be inside separate cells of the same row. Inspect the page or the
GitHub-rendered `body_html` from the PR or comment API; in HTML, each `<video>` should
be inside its own `<td>` in that row. Markup inspection confirms placement, not browser
playback. This CLI flow does not support video alt text, so describe each video in its
column.

If that flow is unavailable, use the attachment control in the intended PR or comment
editor, or use an existing supported integration. An upload in the editor happens
immediately. Save the returned attachment URL and publish only the requested description
or comment. Do not invent a public attachment REST endpoint or depend on an undocumented
session-authenticated upload service.

For videos hosted elsewhere, a link is a fallback. Raw HTML video elements can be
stripped or rendered differently. Use them only after checking that the destination
produces a playable video. Do not commit the video to the source repository just to get
a URL.
