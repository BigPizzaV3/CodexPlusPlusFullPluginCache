# Publish to GitLab

Use the project editor's attachment control or the documented
[project Markdown uploads API](https://docs.gitlab.com/api/project_markdown_uploads/):
`POST /api/v4/projects/:id/uploads`, with the WebM in a multipart `file` field. Resolve
the numeric project ID or URL-encode its full path. Use the authenticated integration's
multipart support. Do not send the local filename as a JSON string and expect the server
to read it.

Keep the response's `markdown`, `url`, and `full_path`. Use the returned `markdown` in
the project's MR or comment, changing descriptive text as needed. If it is a plain link,
use the returned `url` with image syntax to request a video player. Relative upload
paths belong to that project. Do not reuse them in another project without resolving the
URL and checking access. An upload does not create or update an MR or comment; do that
separately if requested.

[GitLab Markdown](https://docs.gitlab.com/user/markdown/#videos) turns image syntax
pointing to `.webm` into a player:

```markdown
![Changing the theme updates the application](/uploads/RETURNED_PATH/demo.webm)
```

Use the returned path in place of the placeholder. Check playback and file access on the
target GitLab instance.
