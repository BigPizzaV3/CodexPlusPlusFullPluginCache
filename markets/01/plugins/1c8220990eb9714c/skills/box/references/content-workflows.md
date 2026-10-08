# Content Workflows

Codex-only CLI and REST behavior, including initial confirmation gates, lives in `references/box-cli.md` and `references/rest-calls.md`.

## MCP

### Tool selection

Use the `upload_file` tool only when uploading small (< 50MB) text-based files. When uploading binary files or large (> 50MB) text files, use `get_upload_url` instead.

Use `get_file_content` before downloading raw bytes. Fall back to `get_download_url` when no usable text representation exists.

Use `upload_file_version` for a new text version of an existing file. For a binary version, pass `file_id` to `get_upload_url`.

### Upload and folder behavior

Use the destination the user specified. Resolve ambiguous folder matches before uploading; when no destination is given, the Box root folder is the default and offer to move the file to their folder of choice.

Subfolders inherit the sharing and collaborations of their parent. For changes that could widen exposure, follow `references/collaboration.md`.

### Error handling

`get_file_preview` only works on clients that support MCP Apps and MCP resources, which are extensions to the MCP protocol. If the tool call succeeds but the user claims there is no UI widget, this may be the cause.

`get_file_preview` only works on documents that are up to 3MB.

`get_file_content` pulls the text representation of a file. There is a max 50MB file size limit.

`get_upload_url` and `get_download_url` require the AI client to execute a curl command to hit a Box domain. This will not work in declarative agents that do not have a code sandbox. Some clients also block external network requests from their code client and require admins to allowlist Box domains. If this is the case (the AI client is able to get the signed URL but cannot hit the external network request to actually POST the bytes over HTTP), refer them to this documentation for how to whitelist domains: https://docs.box.com/en/box-mcp/tools#upload-and-download-url-tools

## Codex-only CLI / REST

Use Box CLI only when it is installed and authenticated. Read `references/box-cli.md` for commands and `references/rest-calls.md` for REST authentication, request templates, and initial confirmation gates. After a write, read the same object with the same actor.

### Content API index and Box-specific behavior

- **Upload:** [Upload a file](https://developer.box.com/reference/post-files-content/). Use chunked upload only when file size or resumability requires it; raw multipart details belong in `references/rest-calls.md`.
- **Folders:** [Create a folder](https://developer.box.com/reference/post-folders/) and [list folder items](https://developer.box.com/reference/get-folders-id-items/). Names must be unique within a parent, and listings must be paginated.
- **Download and preview:** [Download a file](https://developer.box.com/reference/get-files-id-content/) and [Box Preview](https://developer.box.com/guides/embed/ui-elements/preview/).
- **Move:** [Move a file](https://developer.box.com/reference/put-files-id/) or [move a folder](https://developer.box.com/reference/put-folders-id/) by updating `parent.id`. Moving a folder includes its descendants, and a same-name target conflict returns `409`. Use `references/bulk-operations.md` for bulk moves.
- **Metadata:** Use the [metadata guide](https://developer.box.com/guides/metadata/). Read the template or existing instance before writing and validate field keys and types against its schema.