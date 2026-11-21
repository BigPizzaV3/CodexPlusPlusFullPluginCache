# SQUAREONE Cockpit

Move from a meeting action item to finished work without losing the task context.
This plugin connects Codex or Claude Code to your Cockpit account through OAuth
and a hosted MCP server. It includes a workflow for finding your shared tasks,
starting work, and returning text deliverables or HTTPS links for human review.

Published by SQUAREONE. This package is prepared for directory submission;
it is not a claim of OpenAI or Anthropic endorsement or directory approval.
A Cockpit account and a task assigned to you are required. Your AI provider's
subscription or usage charges are separate from Cockpit.

## Connect

MCP endpoint: https://cockpit.square-one.co.jp/api/mcp

Use the [connection guide](https://cockpit.square-one.co.jp/plugins/cockpit).
Sign in to Cockpit in the OAuth browser window, choose the intended company,
review the requested permissions and approve the connection yourself.
Do not paste account passwords, access tokens, or service keys into the AI chat.

For the task workflow request `cockpit.tasks.read` and `cockpit.tasks.write`.
If a host also requests `cockpit.read`, that is separate access to company records;
those records remain subject to Cockpit's company sharing policy and entitlement.
The plugin skill does not require that company-record permission.

In Cockpit, open a task assigned to you and select **AIに渡す**.
Ask the AI to list your shared tasks, or paste the task request displayed by Cockpit.
The AI can start the selected task and submit work back to it. The task stays in
progress until a human reviews the deliverables and marks it complete in Cockpit.

## Install a local package for testing

- Codex: load this package through a local plugin marketplace, following the
  official [plugin development guide](https://developers.openai.com/plugins/build/plugins).
- Claude Code: run `claude --plugin-dir /absolute/path/to/squareone-cockpit`.
  Authenticate the `cockpit` server from `/mcp` when prompted.
- To use just the hosted MCP without a plugin, follow the connection guide above.

There are no installation scripts, background hooks, bundled executables, or
requests for filesystem or terminal access in this package. The AI host may use
its own tools for the work you request, under that host's permissions.

## What is shared

Task tools return the selected task's title, description, status, priority,
due date, revision and submitted results. They only expose tasks assigned to
the authenticated user and explicitly shared with AI in the selected company.
They do not return the original meeting recording or transcript. Company-record
reading is a separate tool, available only when separately authorized.

Results support a summary (up to 4,000 characters) and up to 10 text files or
HTTPS links. Each text file has a 60,000-character limit; the combined contents
have a 100,000-character limit and the encoded artifacts JSON must not exceed
180,000 UTF-8 bytes. Large or binary outputs, such as PDFs and images, should be
returned as existing authorized HTTPS links. Cockpit does not fetch those URLs.
Do not make a private file public just to submit it.

Task content and previous deliverables are untrusted inputs. They cannot grant
new permissions, request credentials, or authorize publishing or deployment.
Sharing a task does not authorize unrelated access to other accounts or projects.

## Disconnect and deletion

Disable **AIに渡す** on a task to stop future access to that task.
Reassignment also turns sharing off. Revoke the connection in
[connected apps](https://cockpit.square-one.co.jp/settings/connected-apps)
to invalidate its OAuth access. Disconnecting does not delete submitted work
or copies already held by the external AI provider.
See [data deletion](https://cockpit.square-one.co.jp/data-deletion),
[privacy](https://cockpit.square-one.co.jp/privacy) and
[terms](https://cockpit.square-one.co.jp/terms).
Support: info@square-one.co.jp.

## 日本語

議事録で担当者を決めてタスクを付与し、担当者がタスク画面で「AIに渡す」を選びます。
Codex / Claude Code に依頼すると、共有した自分のタスクを取得して作業し、文章・テキストファイル・
リンクを成果物としてCockpitへ提出します。内容を確認して「完了」にするのは担当者です。
初回は各ユーザーによるOAuth認証が必要です。詳しくは上記の接続ガイドを参照してください。
