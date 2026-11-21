# Fuzzbucket MCP Tool Map

Each tool performs one action. Read-only tools are annotated `readOnlyHint`.
Tools that can overwrite, replace, remove or stop existing work (updating a
node draft, disconnecting an input, generating from a node, cancelling a run,
sending or approving a chat brief, answering a brand onboarding question) are
annotated `destructiveHint`; creating workspaces and nodes, connecting inputs
and uploading are not. Brand onboarding and the workspace orchestrator can read
public web pages, so those tools are annotated `openWorldHint`.
`tools/list` only shows tools the connection's permissions allow, and execution
checks permissions again.

| Area | Read-only tools | Tools that change data |
| --- | --- | --- |
| Brands | `fuzz_list_brands`, `fuzz_get_brand`, `fuzz_get_brand_quota`, `fuzz_preview_brand_logos` | `fuzz_create_brand`, `fuzz_answer_brand_question` |
| Workspaces | `fuzz_list_workspaces`, `fuzz_get_workspace`, `fuzz_list_workspace_contents` | `fuzz_create_workspace` |
| Canvas nodes | `fuzz_get_node` | `fuzz_create_node`, `fuzz_update_node_input`, `fuzz_connect_node_input`, `fuzz_disconnect_node_input` |
| Chat | `fuzz_read_chat` | `fuzz_send_chat_message`, `fuzz_respond_to_chat_approval` |
| Generation runs | `fuzz_get_run` | `fuzz_generate_node`, `fuzz_cancel_run` |
| Assets | `fuzz_get_asset`, `fuzz_preview_assets`, `fuzz_download_asset`, `fuzz_export_node`, `fuzz_export_nodes` | `fuzz_prepare_upload`, `fuzz_complete_upload` |
| Models | `fuzz_list_models` | — |

`fuzz_get_run`, `fuzz_preview_assets` and `fuzz_preview_brand_logos` also
render an interactive results view (MCP Apps) in clients that support it.
`fuzz_preview_assets` returns small thumbnails (a frame for videos) and
`fuzz_preview_brand_logos` returns the brand's logos, both as image content the
client can display directly. No tool returns storage links; originals come
from `fuzz_download_asset` as a short-lived Fuzzbucket link.

A tool absent from discovery is not granted. Sanitized help and live tool
schemas are served from the configured API's `/docs/mcp.md` and
`/docs/mcp/tools.md`.

Tools that change data require an operationId; node edits and generation require
the saved node revision. Saving drafts and connecting inputs do not generate.
Chat and generation return a run ID. Transfers return short-lived URLs and
private request headers; the account credential never appears in a URL.
