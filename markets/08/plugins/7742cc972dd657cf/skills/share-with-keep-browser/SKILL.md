---
name: share-with-keep-browser
description: Prepare selected public links as a Keep Browser tab tree. Use for requests to share links, candidates, or research with Keep Browser, or to prepare that handoff.
---

# Share with Keep Browser

The connected `create_tab_tree_link` tool creates a new public-by-link tab tree. It does not research candidates, read existing device tabs, or confirm device import. Anyone with the share link or summary URL can read the shared names and descriptions and access the included links.

## Selected content and tree structure

- Build the input from the user's selected content using the current tool schema. Preserve exact public HTTP(S) URLs, available page names, hierarchy, and order.
- Research and recommendations use the host's available research tools. Identify unresolved URLs instead of guessing, replacing, or dropping candidates. Private or authentication links and unrelated conversation details do not belong in a share.
- Keep valid user-supplied group names. Use concise, descriptive names for unnamed groups in the requested or conversation language.
- The summary is the first tab of the root group. Supply `summary.locale` and the relevant overview or per-page descriptions from the selection. Count the summary within the node limit without discarding selected pages.

## Creation identity and results

`operation_id` identifies a creation intent. Repeated calls for that intent require the same ID and identical input, including names, notes, and summary. A timeout, missing response, or pending summary does not establish non-creation. A new ID loses duplicate protection. Idempotency records may be purged after 48 hours; retries do not extend retention, and repeating an unresolved request after that period can create a duplicate.

A successful result supplies the exact `share_url`. Present it as an opening link and as a single URL line in a fenced code block for copying. Use the returned import facts to explain how to open the tree in Keep Browser. A known share URL is sufficient to show an existing result again.

Link creation does not establish that the app is installed or that import completed. `summary_status=pending` means the share exists but its summary is not ready. Report that distinction.

For errors, explain the actual outcome and returned `wait_reason`, `retry_action`, and retry-time fields in the user's language. A retry time is the earliest retry time, not a recovery guarantee; null time fields provide no countdown. The service does not provide scheduled creation or background notifications. Keep internal identifiers out of routine user-facing explanations unless needed to answer the user's question.
