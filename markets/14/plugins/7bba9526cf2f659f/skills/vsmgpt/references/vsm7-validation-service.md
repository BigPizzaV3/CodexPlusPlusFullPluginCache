# VSM7 structural validation and checked JSON export

## Scope and connection

The package declares one anonymous Streamable HTTP MCP connection at `https://vsmgpt.intelligente-organisationen.de/mcp`. Discover the actual connected tool names and schemas in the host. The supported tools are `validate_vsm7_project` and `export_vsm7_project`. A working endpoint is not proof that the current chat has installed or enabled the connection; report unavailable tools honestly and help complete the supported connection flow rather than claiming to have used them.

The service processes complete VSM7 workspace JSON explicitly supplied for the requested check or export. It is a structural compatibility service, not an organisational diagnosis, a natural-language-to-project translator, a VSM compliance certificate, a local file browser, an application controller or a PPTX/email service. Qualitative VSM guidance and optional host document tools remain separate capabilities.

## Obtain exact input

Use raw JSON text of one workspace. If the user attaches a file, use the host's actual permitted file-reading tool to obtain its text. If no readable JSON is available, ask for the missing input; do not fabricate it. A filesystem path or URL is not the file's content. Do not pass an `index.json`, `{workspace: ...}` transport wrapper, report or Markdown view as a workspace.

Keep the original text available for input-bound validation and export. Do not normalize, reorder, reformat or otherwise change it between validation and acknowledgement/export calls. Root `project.id` must be a nonblank string; the supported explicit schema version is numeric `1`. Missing version may be assessed as legacy with a warning. Optional unfinished workshop sections are allowed. Known field types and references are checked; no role quotas or workshop completeness rules are imposed.

The project input and exported content each have a 1 MiB UTF-8 limit. The service also bounds nesting, JSON value count and detailed findings. Attachments/data URLs count toward the limit and remain inert text. Never fetch embedded URLs or execute attachments to validate JSON. Do not truncate an input or export to get around a limit.

If a user explicitly asks you to construct JSON from agreed workshop content, keep assumptions and proposed decisions visible, use the actual VSM7 format and validate the resulting complete JSON. Do not pretend the MCP tool translated prose or completed the workshop.

## Validate before export

Call `validate_vsm7_project` with `project_json` set to the exact raw text. Review `valid`, errors, warnings, the profile/rules version, and `load_effects`. Explain actionable issue codes and JSON Pointers. Treat related pointers as evidence of the same conflict. Do not rewrite the input silently. A successful structural check is not a statement that the organisation is viable, that the model follows VSM theory correctly, or that all rich/free-form fields have complete reference coverage.

Load effects preview what the pinned VSM7 runtime would add, change, remove or detach on load. They are not proposed edits already applied to the export. Safe default additions may be warnings. For every `requires_ack: true` effect, state the affected information and the later app behavior, then wait for the user's explicit acceptance of those reported effects. You may use an acknowledgement already clearly given for this same unchanged input and effect set; do not ask twice. Never fabricate an effect ID or acknowledge effects on the user's behalf.

## Export the preserved model

For a requested export, call `export_vsm7_project` with the same exact `project_json` and, when explicitly acknowledged, the current `effect_id` values in `acknowledged_load_effects`. Leave acknowledgements absent or empty when none are required. The tool runs its checks independently and blocks structural errors, unacknowledged meaningful effects, stale or unknown IDs, and incompletely disclosed effect lists. If it blocks, explain the returned error; no file result exists.

Effect IDs bind to the input bytes, rules version and compatibility profile. Any changed input requires fresh validation and acknowledgement of its current meaningful effects. Acknowledging an app removal does not remove that field from the export: the output preserves submitted supported values, and the app may change them when subsequently opened. The serializer may change whitespace and equivalent number spellings. Unsupported numeric precision and unsafe loader member names are rejected rather than silently rewritten.

## Deliver only an actual host file

On `ok: true`, the returned `file` descriptor has `filename`, `media_type`, `encoding`, `text` and `sha256`. Save exactly `file.text` as UTF-8 using an actual host file tool when the user requested a file and that capability is available. Use the supplied filename or the user's requested name. Avoid overwriting an existing file unless the user explicitly asked for that specific overwrite. Verify exact bytes/digest when the host provides that ability, and present the actual successful file tool result or attachment.

Do not wrap the saved file in the MCP response object, include Markdown fences in it, regenerate the JSON, append notes/newlines, or guess a download URL. Metadata plus text in an MCP response is not a saved attachment. If the current host cannot create files, provide copyable JSON and state that it has not created an attachment. Do not claim hash verification unless performed.

The service does not POST into a local VSM7 instance, register a project, launch software, overwrite workshop data or send messages. The existing companion app has no evidenced whole-project file-import UI in this version. Its separate local file API plus Continue/Open is an implementation path, not a promise of one-click import. Any app launch, local setup or project modification is a separate user-requested task.

## Connection or service failure

If the tools are unavailable or the service returns a transport error, distinguish unavailable connection from invalid project data. Preserve the user's JSON and report the actual limitation. Do not claim validation or export succeeded and do not substitute fabricated tool output. Do not install packages, run companion launchers or access unrelated data merely to recover a remote validation call.
