# Changelog

## 0.1.8 (2026-11-04)

- Review re-submission after the 2026-11-04 rejection ("appears to enable
  or facilitate commerce for disallowed offerings"). The skill no longer
  links the pricing page or mentions credits or purchases: a feature that
  is not on the user's plan is stated plainly, with no links. The two commerce-shaped negative review cases (API key,
  API credits) are replaced by out-of-scope cases (password change, account
  deletion). A file-upload case was dropped: run in ChatGPT, the model
  offered an upload that no tool provides. release notes trimmed to the facts; commerce_description says what the tools carry (no checkout,
  payment or API key functions, no plan or upgrade links in results).
- mcp.json declares only auth type oauth; client and endpoints come from
  discovery, which restores the default OIDC scopes (openid, email,
  offline_access). Declaring endpoints had reduced the request to email.
- plugin.json name is isms-copilot: a new OpenAI plugin under the verified
  business identity, because a plugin's first connection keeps its OAuth
  client for good.
- Versions mirrored in the Claude and Cursor manifests. No tool or
  listing-metadata change; mcp.json gains the auth declaration only; the
  OpenAI package description is unchanged.

## Claude Code 0.1.7 (2026-10-19)

- README is now the public listing text (the Claude Code plugin directory
  shows it as the description): the approved Claude connector listing
  text, what the plugin contains and sends, install for Claude Code,
  Gemini CLI and other clients, maintainer notes.
- .claude-plugin/plugin.json: version 0.1.7, description matches the
  Claude directory listing, homepage carries ref=claude-code-plugins. Its
  extensions.com.openai block is unchanged. The ChatGPT and Codex package
  (root plugin.json, mcp.json) stays at 0.1.6.
- .cursor-plugin/plugin.json (new): Cursor manifest for cursor.directory,
  description ends "from Cursor.", homepage carries ref=cursor-directory.

## Gemini CLI 0.1.0 and Claude Code install (2026-10-14)

- New files only; the OpenAI package files (plugin.json,
  .claude-plugin/plugin.json, mcp.json, skills, assets) are unchanged and
  the package stays at 0.1.6.
- gemini-extension.json (extension 0.1.0, MCP server `ismscopilot` by
  httpUrl) and GEMINI.md context, so the repo installs with
  `gemini extensions install` and the Gemini CLI gallery can index it.
- .mcp.json (type http) and .claude-plugin/marketplace.json, so the repo
  installs as a Claude Code plugin with `claude plugin marketplace add`.
- README: Install section for both.

## 0.1.6

- Review: demo_recording_url added (video walkthrough of the review cases in
  ChatGPT, hosted on www.ismscopilot.com).

## 0.1.5

- Review case P4 prompt names both steps ("List my ISMS Copilot
  workspaces, then list the documents in My First Workspace."). In one
  of two ChatGPT runs the earlier wording led to a list_workspaces call
  only and a "no documents" answer. The matching starter prompt now names
  both steps too ("..., then list the documents in the first one.").

## 0.1.4

- Review cases P2 and P3: tools_triggered holds plain tool names
  (create_conversation, send_message). The conditional get_reply note
  stays in expected_behavior. Matches the documented format (tool names,
  comma separated).

## 0.1.3

ChatGPT test run on the reviewer account (2026-10-07):

- Review case P3 prompt names the app ("Ask ISMS Copilot to turn that
  into ..."). The bare follow-up was answered by ChatGPT itself without a
  tool call; the named prompt continues the same specialist conversation
  (send_message, verified: one thread, four messages).
- Negative case N2 expected behavior matches what ChatGPT does: declines
  without a tool call and says key creation is not available through
  this connection.

## 0.1.2

Pre-submission audit against the OpenAI plugin guidelines (2026-10-07):

- Subtitle "Compliance and GRC specialist" (states the purpose for the
  Security category; drops "your agent", which could read as a
  reference to another AI assistant).
- Long description: restricted-data line (no health records, card data
  or government IDs), not-legal-advice line, credit-purchase wording
  removed from the listing (commerce stays declared false).
- Support URL points to the public contact-support page.
- composerIcon added (required in the Codex-format manifest the portal
  derives).
- Review case P1 now reads the company profile (get_company_context)
  instead of the plan, so no plan, upgrade link or account identifier
  appears in review output. P2 and P3 name get_reply as conditional.
- Onboarding skill: writes only on user request; sensitive data and
  not-legal-advice guidance.

## 0.1.1

Category corrected to Security (the ChatGPT plugins directory category list
confirmed from the live directory: Security is the category for information
security compliance work; Productivity could not be confirmed by the portal
check). Version bump to 0.1.1. No other listing text change.

## 0.1.0

Initial plugin package for the ChatGPT and Codex plugins directory,
"With MCP" type. Connects the ISMS Copilot account MCP server
(https://account.ismscopilot.com/v1/account/mcp, Streamable HTTP, OAuth
2.1). Listing metadata under extensions.com.openai in both the root
Agent Plugins manifest and .claude-plugin/plugin.json: displayName and
subtitle within the 30-character limits, no pricing in the description,
no references to other AI assistants, four listing URLs, starter
prompts, five positive and three negative review cases, and the get
started onboarding skill. API key and credit purchases are not part of
the connected tool set, and commerce is declared false.
