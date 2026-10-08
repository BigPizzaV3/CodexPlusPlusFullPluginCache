# Direct REST Fallback

These instructions apply only in Codex. ChatGPT uses Box MCP and must ignore this reference.

Use direct REST only when selected by the main skill and REST authentication is already configured.

## Source of truth

- Use Box API endpoint docs as the authority for endpoint coverage and operation details: https://developer.box.com/reference
- Use the Box OpenAPI spec as the authority for request and response shapes.
- OpenAPI repository: https://github.com/box/box-openapi
- Versioning note: Box introduced API versioning in 2025. `openapi.json` remains for compatibility, and versioned specs live under `openapi/` in the same repository.

When this file and current Box docs disagree, follow current Box docs and OpenAPI.

## Auth and base URLs

- API base URL: `https://api.box.com/2.0`
- Upload base URL: `https://upload.box.com/api/2.0`
- Required auth header: `Authorization: Bearer $BOX_ACCESS_TOKEN`
- Recommended default header: `Accept: application/json`

Confirm the token and actor without printing the token:

```bash
test -n "$BOX_ACCESS_TOKEN" &&
curl --fail-with-body -sS \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  -H "Accept: application/json" \
  "https://api.box.com/2.0/users/me"
```

If either check fails, use `references/auth-and-setup.md`. Never echo or log token values.

## Request templates

JSON request:

```bash
curl --fail-with-body -sS -X <METHOD> \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  "https://api.box.com/2.0/<PATH>" \
  --data '<JSON_BODY>'
```

Omit `Content-Type` and `--data` for requests without a body.

```bash
curl -sS -X PUT \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  "https://api.box.com/2.0/files/<FILE_ID>" \
  -d '{"parent":{"id":"<TARGET_FOLDER_ID>"}}'
```

## Request structure guidelines

- Request only fields you need (`fields=...`).
- In Box APIs, setting `fields` changes the default response projection: only mini fields plus the explicitly requested fields are returned.
- Use pagination (`limit`, `offset`) for list/search endpoints.
- Some list endpoints also support marker pagination. Check the endpoint schema in OpenAPI before choosing offset vs marker for large traversals.
- For writes, follow with a read-after-write call using the same actor.
- For uploads, use the upload base URL and multipart form-data with `attributes` + file content at `POST /files/content`.
- In multipart uploads, the `attributes` part must come before the `file` part, or Box can return `400 metadata_after_file_contents`.
- Sanitize filenames in multipart `Content-Disposition` headers (escape quotes and backslashes, strip CR/LF).

Upload example skeleton:

```bash
curl --fail-with-body -sS -X POST \
  -H "Authorization: Bearer $BOX_ACCESS_TOKEN" \
  -H "Accept: application/json" \
  -F 'attributes={"name":"<FILE_NAME>","parent":{"id":"<PARENT_ID>"}}' \
  -F "file=@<LOCAL_PATH>" \
  "https://upload.box.com/api/2.0/files/content"
```

## Box-specific request behavior

- Setting `fields` replaces the default response projection with mini fields plus the explicitly requested fields.
- Check the endpoint schema before choosing offset or marker pagination.
- In multipart uploads, `attributes` must precede `file` or Box can return `400 metadata_after_file_contents`.
- After a write, read the same object with the same actor. Use `references/content-workflows.md` for domain-specific endpoints.

## Retries and failures

Use `references/troubleshooting.md` for HTTP-error diagnosis, `429` handling, and timeout or transient-server-error retries.

## First-use confirmations

- If the user did not explicitly request REST, explain the fallback and confirm it before the first REST call. Do not reconfirm the path when the user already requested it.
- Before the first REST request in a session that overwrites, moves, deletes, changes file or folder properties, posts a collaborator-visible comment, or starts a Doc Gen batch, describe the exact target and change and wait for confirmation. Combine this with REST fallback approval when both are needed, then ask whether later REST actions of that type may proceed without confirmation for the rest of the session.
- Before first pasting Box file content retrieved through REST into the conversation, ask whether the user prefers a Box link or pasted content and whether that choice should apply for the rest of the session.