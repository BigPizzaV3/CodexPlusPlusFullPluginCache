# Local file upload

For a host that can read the files the user named and make HTTPS PUT requests.

Before prepare:

- resolve only the exact paths the user gave and check they are regular files;
- read each file's exact byte count and content type.

Describe each file as `kind: upload` with its filename, content type and byte
count. Prepare answers with the size limits of the user's account when a file
is too large.

For each returned upload plan:

- match its `slot` to the original file;
- PUT the exact bytes once, with the plan's method, signed URL, headers and
  content length;
- never follow redirects or turn on verbose HTTP tracing, which would print
  the signed URL;
- pass each `upload_handle` in `upload_completions`.

Signed URLs are credentials: never print, log or store them, and send bytes
only to the Viggle URL a plan returned. Do not make a private file public or
move it through a third-party file-sharing service.

To save a finished Mix, download `result.video_url` to the location the user
chose, and ask before overwriting an existing file. If the URL has expired,
`viggle_get_mix` returns a fresh one.
