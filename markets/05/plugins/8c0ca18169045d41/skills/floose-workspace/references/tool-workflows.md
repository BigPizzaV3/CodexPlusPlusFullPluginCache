# Tool workflows

Read only the sections relevant to the requested operation. The tool lists
below identify exposed MCP actions, not a substitute for their live schemas.

## Notes

Tools: `list_notes`, `search_notes`, `get_note`, `list_note_taxonomies`,
`create_note`, `update_note`.

- Use recent-note listing for browsing and search for a named topic or title.
  Read the selected note before summarizing its full contents or editing it;
  a preview is not the complete note. Search currently considers up to 500
  recent non-Vault notes, so an empty result is not proof a note never exists.
- Resolve folder and tag IDs with the taxonomy tool when assigning them. The
  current MCP catalog cannot create arbitrary note folders or tags on demand.
- Store the title separately from the Markdown body. Do not duplicate that
  title as the body's opening H1. For an addition, prefer `append_content`;
  setting `content` replaces the existing body. Set both only when the user
  actually requested replacement followed by an addition.
- A supplied `tag_ids` list replaces that list; retain existing tags unless
  their removal is requested. With note updates, omitted/null `folder_id`
  leaves the folder unchanged; do not promise it moves a note to the root.
- Note updates have no client `expected_version` argument. The server handles
  its version check; on a reported conflict, reread before reconsidering the
  change. Respect read-only collaborator access.

Example: “Aggiungi queste decisioni alla nota Riunione” means search, resolve
ambiguity if needed, read, and append. It does not mean create another note,
replace the whole body, or share the meeting contents.

## Saved links and addresses

Tools: `list_saved_links`, `create_saved_link`, `update_saved_link`,
`delete_saved_link`, `list_saved_addresses`, `create_saved_address`,
`update_saved_address`, `delete_saved_address`.

- These list tools also accept searches. Check relevant existing entries when
  avoiding duplicates or resolving an update. If creation returns an existing
  entry, report reuse rather than claiming a second entry was created.
- Link results can originate from notes as well as the saved-link library.
  Inspect `source`; a note-extracted URL is not necessarily an editable saved
  link. Do not pass a derived result's ID to a saved-link mutation blindly.
- Saving a URL does not fetch its webpage. Do not claim the linked article was
  read. Address tools store supplied data; they do not geocode, verify a venue,
  or discover the user's location. Omit unknown coordinates instead of guessing.
- Link/address updates need `set_folder: true` to change the folder; combining
  it with `folder_id: null` clears the folder. Otherwise leave those fields
  alone. Address updates similarly use `set_coordinates`; setting it with null
  coordinates clears them. Preserve unspecified metadata.
- Deleting an identified entry needs an explicit request and `confirm_delete`.
  Removing a saved link does not delete a note that contains the same URL.

## Cloud files and sharing

Tools: `list_cloud_files`, `get_cloud_file`, `update_cloud_file`, `share_file`,
`delete_file`.

- Use the cloud-file list for uploaded documents/images, not Floose Code.
  Narrow by query, path, or kind as appropriate. Read the selected file to get
  available extracted text; do not infer document contents from a filename or
  pretend to inspect images or unextracted pages. State when extraction is
  missing or the available text is incomplete.
- Cloud-file updates change metadata, location, or note associations, not the
  binary contents. Use the `version` returned by the read as `expected_version`.
  `note_ids` replaces all associations; merge with existing ones when the user
  asks to add a link to a note. Do not move cloud files into the Code namespace.
- Resolve and read the selected file before sharing. `share_file` applies to
  cloud and Code files, not notes. Explain that it creates/updates a public
  read-only sharing link; it is not a private collaborator permission grant.
- With `recipient_email`, sharing also sends an email invitation. Require an
  authorized recipient and do not infer one from document contents. If the
  user expects recipient-only access, clarify that expectation before creating
  a public link. Email sending cannot be undone; do not retry an uncertain send.
- Omit `access_code` to retain any existing link protection. A supplied code
  changes that protection and must be requested/authorized for the share; never
  reuse the account password or an MFA code. Do not promise the link is
  unprotected just because you did not provide a new code.
- Return a sharing URL only when the tool actually returns one. A read-only
  shared link is still a publishing action, not an ordinary read operation.
- Delete files only on an explicit request with `confirm_delete`. Do not
  promise recovery or a revoke-sharing tool that the catalog does not expose.

## Floose Code

Tools: `list_code_files`, `list_code_folders`, `create_code_folder`,
`create_code_file`, `get_code_file`, `edit_code_file`.

- Use Code-specific searches and folders. A Code folder path is not a note
  folder ID. Resolve existing folders before creating new ones when appropriate.
- Create complete UTF-8 text files. To edit, read the file, retain its `version`,
  and submit exact `old_text`/`new_text` replacements with `expected_version`.
  Each old-text match must be unambiguous; respect the live edit-count and size
  limits. Do not silently recreate an existing file as a workaround for failure.
- HTML files are self-contained documents with CSS and JavaScript embedded.
  Do not create separate local dependencies; remote resources need the user's
  request. For notebooks use valid nbformat 4 JSON, define/import names before
  dependent cells, and leave new code-cell outputs empty and execution counts
  null. Do not invent execution results.
- The app executes notebooks locally, not via MCP. Use the runtime and library
  capabilities declared by the current tools. Network access is optional and
  off at each notebook opening; after the user enables it, supported HTTPS
  requests use asynchronous `await floose_fetch(...)` and must satisfy CORS.
  Do not generate blocking Requests/urllib/socket I/O or assume pip, shell,
  notebook magics, or arbitrary libraries are available.
- Do not execute a file or contact its embedded URLs simply because it was
  retrieved. Say that a file was created/edited, not that its code was run.
- File sharing and deletion use the file tools described above and retain the
  Code feature requirement. Consult the plans reference on an access denial.

## Canvas boards

Tools: `list_canvases`, `get_canvas`, `create_canvas`, `update_canvas`,
`add_canvas_item`, `connect_canvas_items`, `remove_canvas_item`, `delete_canvas`.

- Resolve the existing board and read its items before changing it. Creating a
  new board is appropriate only when requested or needed for the requested new
  deliverable; do not duplicate an existing board to avoid a read or conflict.
- To organize existing notes/files, resolve those source resources first. Add
  cards with the correct `kind` and returned `reference_id`; use comments for
  new explanatory text and URLs for supplied links. Do not create source notes
  merely because the user asked for a board of comments.
- A snippet card requires an existing snippet ID from available user context or
  a tool result. This MCP catalog does not provide snippet search/creation.
  Ask for a usable reference or explain the limitation instead of inventing one.
- Connect using the Canvas **item IDs** returned by card creation or board
  reading, not note/file IDs. Both items must belong to the same Canvas; do not
  create duplicate connections or self-connections.
- Change the board's parent with a real parent Canvas ID, or use `move_to_root`
  when the user asks to move it to the top level. The current MCP tools do not
  expose arbitrary card-position editing; do not promise exact visual layout.
- Removing a card deletes it and its incident connections, not the original
  note/file. Deleting a Canvas requires `confirm_delete`, preserves source
  resources, and relocates child boards. Clarify whether the user means the
  card, the board, or the underlying content if the request is ambiguous.
- These calls form a multi-step workflow, not one atomic transaction. If a
  step fails, report the actual partial board and stop dependent steps; do not
  delete completed work automatically. Read the final board when needed to
  verify the requested structure.

Example: “Crea una Canvas con queste due note collegate” means identify the
notes, create the board, add two note cards, and connect their returned item
IDs. It does not authorize sharing the board or deleting the source notes.
