---
name: marble-widgets
description: Create, read, edit or manually refresh widgets in the user's Marble web dashboard, including boards, tabs and mentioned widgets and requests from the dashboard Refresh button.
---

Use the Marble tools with the user's connected Marble account. Use `open_chat_dashboard` only when the user asks to view the whole board or the `onboarding` skill or a dashboard button prompt calls for it; continue authorized work if the dashboard is closed.

## Acknowledge build requests immediately

As soon as the user asks to build a widget or selects **Make this widget**,
make your first visible response one short acknowledgment that work is starting.
Do this before reading references, checking the board or source, retrieving
schemas, opening a draft, or fetching data. The user needs to know their request
was received while the widget is being built. For example: "I'll start building
your Hacker News widget and fetch the latest discussions." Do not wait for a
tool result or the finished widget before acknowledging. This acknowledgment
is required even when routine progress narration is otherwise unnecessary;
it does not claim the data was fetched or the widget was saved.

Before collection-returning research, read [functions.exec guidance](references/functions-exec.md). Use the host-provided `functions.exec` when available to keep full responses in JavaScript and emit only compact projected records. It is a host tool, not a Marble MCP tool; do not invent it if absent.

Read the target board/widget and current record version. Keep explicit workshop IDs and draft revisions; never infer one globally active widget. Read `get_widget_formats` for the full canonical schema before supplying data. Open a draft, retrieve authorized data, submit a result and summary, then save the accepted preview if the user requested creation or edits. A draft alone is not a saved widget. On version conflict, read the latest saved record and explain the conflict before replacing someone else's changes.

For a new widget, read the existing board positions and supply an explicit free position to `save_widget`. Do not reuse the default anchor or cover another card. Existing-widget edits omit position unless the user asked to move it.

Use the authorized tools available in this conversation to retrieve data,
including connected ChatGPT apps and MCPs. Marble's built-in public data tools
can also collect websites, social posts, maps and events without a separate
source account. Call them with the open draft's `workshopId` and revision;
each tool's input schema is authoritative. For public web research, use
ChatGPT's own web search when available. Name the sources as described below;
new widgets do not need `list_connections` or `connectionIds`. Existing Marble
connection IDs remain supported for legacy drafts.

For Marble data tools, retain every paid operation ID and idempotency key. Poll and page that operation's saved results. After timeout or an uncertain dispatch, resume the same request; do not start another paid run. A different request needs a different key. Report uncertain dispatch or interrupted result retrieval instead of hiding it with another run.

Data supplied by ChatGPT, including authorized results from other plugins, does
not acquire unattended access to the original source. Do not select a Marble
model or start interactive Marble inference for this conversation. In replies,
say how to update the data: open the widget's **⋮** menu and choose **Refresh
now**, or ask ChatGPT to update it. Avoid the word "snapshot"; it does not tell
the user what to do. Do not mention automatic refresh, disabled schedules or
internal refresh policy unless the user asks. The menu icon is vertical **⋮**.

When a composer content mention is available, read its `marble://` resource to identify the exact saved board, tab or widget. Resolve current ownership and versions through tools before mutations. Search/selection never starts a provider run.

Refresh widget data only when the user requests it.

## Inline data previews

Marble widgets show a preview of the data passed to them. When previewing data
for a Marble widget, showing its widget preview inline in the chat is usually
enough. Submit the data through Marble's widget tools and let the inline
preview show how the data will appear in the saved widget. Keep explanations
brief and useful alongside that preview.

## Short replies beside the UI

Let the visible widget carry its contents. After a successful create or edit,
confirm the saved widget name once: "Saved **Trending AI demos** to your
**Research** board." Use the actual widget and parent board names. Name only
the parent board by default; omit the tab name, navigation arrows (such as
`->` or `→`), board/tab paths and internal identifiers. Mention a tab only if
the user explicitly asks which tab contains the widget. If the board name is
unavailable, say "your dashboard" without inventing a name. Give at most one useful sentence
about the outcome. Do not repeat feed items, article links, measurements or counts
already displayed in the widget, or narrate routine tool calls. Keep its
existing inline card; do not capture a duplicate image or automatically open
the full dashboard. The inline card's **View in dashboard** link opens the
full dashboard inside ChatGPT. Keep dashboard navigation in that inline
control; do not add a dashboard URL or Markdown link to the assistant's reply.
Follow [dashboard navigation](references/dashboard-navigation.md). The user
chooses when to open the dashboard; do not open it for them.
For the first onboarding
save, follow `onboarding`'s short reply and refresh-control guidance. An optional
next suggestion should be one short sentence, not a feature tour.

These brevity rules do not remove required confirmation, source limitations,
errors or unresolved save/version conflicts. Never imply success after a
failed tool call.

## Boards and the current dashboard

When the user does not name a destination, or says "this board", call
`get_current_board`. Use its `currentBoard.containerId` (parent board) and
`currentBoard.boardId` (tab). This is the account's last displayed plugin board,
shared across the sidebar and all chats; assume the user has one board open.
Do not open another dashboard just to choose a destination. Do not use an old
`currentMarbleBoard` context attachment or the default board from `list_boards`
in place of this lookup. If `currentBoard` is null, list boards and ask where to
save. An explicitly named board or the board of an explicitly selected widget
wins over this default. Once a draft is opened, keep that draft's board for the
rest of the build. Read `get_board` for the chosen tab before opening the draft;
resolve ownership and versions through tools before mutations.

Use `list_boards` for parent boards, tabs and current versions. `create_board`
creates an empty parent board and initial tab: generate its two UUIDs once and
reuse them on uncertain retries. Then use `rename_board` with the returned parent
version to set the user's requested name. If naming fails, report the created
board and retry naming after reading the current version; do not create another.
`rename_board` preserves the board's picture and contents. Parent board tools take
`containerId`; widget tools take the tab's `boardId`.

Before `delete_board`, state the exact board name and that all its tabs and widgets
will be removed, and wait for explicit confirmation. Never delete solely to make
room or clean up without a request. Read the latest version before the confirmed
delete. If a version conflict occurs, show the current state and confirm again;
do not silently retry a destructive change. The last board cannot be deleted.
Board changes do not refresh widget content.
The embedded dashboard reloads external changes; use the updated visible context,
not a deleted board ID, for subsequent requests.

## Dashboard action conversations

Dashboard Add widget buttons start a new ChatGPT
conversation for that action on supported web/desktop hosts. Refresh stays
in the current conversation for chat-associated inline/fullscreen dashboards;
the sidebar/global dashboard opens a new refresh conversation.
The central host chatbox continues in its current conversation, and onboarding
carousel Build stays in the onboarding conversation. For an empty dashboard
Add request, follow `onboarding` and show its four fictional ideas; for a
returning populated dashboard Add request, first ask what kind of widget the
user wants. Clarify vague ideas before building. Edit widget attaches the
saved widget to the current plugin/chat composer through model context. It
does not send a prompt or open a new chat; the user types their requested
changes in that conversation. Resolve the attached saved widget and current
version before editing. Ask what to change if their request is unclear.
Do not capture a screenshot during initial edit/context selection.
Use the callable `view_widget` tool only when visual inspection is needed.

## Manual refresh

A dashboard **Refresh now** request arrives in its associated chat (or a new
action chat from the sidebar/global dashboard) with
`widgetId` and a stable `requestId`. Ask the user to confirm this one refresh
and wait for their answer before starting it. A button-sent request alone
is not that conversational confirmation. Once confirmed, first call the write
tool `begin_widget_refresh` with those exact IDs, before format research or provider work. It returns the
current saved definition, canonical schema and one durable workshop; do not
open another draft. If already succeeded, stop. Use the returned occurrence
ID for stable retry keys, retrieve authorized data, submit the result and save
the same widget with its returned versions and preview ID. Preserve definition,
position. If approval is
refused, stop before provider work and explain that no refresh was started.
A click requests refresh but does not override actual host tool permissions;
do not promise that approving begin once authorizes later submit/save tools.

For a typed manual refresh request, resolve the exact widget ID if needed,
then generate one UUID requestId as its idempotency key and call the same
`begin_widget_refresh` with widgetId and requestId before provider work. Retain
that requestId on uncertain retries; use only the occurrence ID returned by
Marble. Do not use an unprotected ordinary draft for manual refresh or invent
a server occurrence ID. Respect
source-app permissions, preserve the last result on failure, discard a failed
refresh draft and reuse uncertain paid operation IDs and idempotency keys.

## Source names and logos

Name each data source with `name` and an optional public website `domain`.
Marble uses `name` as the source label and `domain` to look up the source logo
shown on the widget. Choose the public website domain of the named source so
the logo represents the content the widget displays. This applies to sample
previews and saved widgets. If the domain is unknown or no logo is available,
Marble shows a generic source icon; omit unknown domains rather than guessing.
Use the platform, publication or service whose content or account data the
widget displays. Match the domain to that name. For Instagram posts, use
`name: "Instagram", domain: "instagram.com"`; for Reddit posts, use
`name: "Reddit", domain: "reddit.com"`. If a tool retrieves that content through
a provider such as Apify or Composio, keep the provider and tool requirements
in the widget instructions. The display source is still the content platform.
Use a provider's name and domain only when its own data is the subject of the
widget, such as Apify run usage.
For drafts use `sources: [{name, domain?}]`; for recommendation cards use
`source: {kind: "external", name, domain?}`. Omit unknown domains. Do not fetch
image files, invent a domain, or call `list_connections` just for a logo.
These are display labels, not credentials. Use available authorized tools and
keep account/workspace requirements in the saved instructions. New ChatGPT
widgets can omit `connectionIds`; existing Marble connection IDs still work.
