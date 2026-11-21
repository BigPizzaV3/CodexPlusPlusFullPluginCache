# Captino plugin for ChatGPT and Codex

An [Agent Plugins](https://agent-plugins.org) package that connects Codex and
ChatGPT to the Captino MCP server at `https://api.captino.io/mcp` and adds
skills for working with funnels, pages and leads.

## Install

Add this repository as a marketplace, then install the plugin:

```bash
codex plugin marketplace add Grumsen-Development-ApS/captino-openai-plugin
```

Then open `/plugins` in Codex (or the Plugins directory in the ChatGPT desktop
app) and install **Captino**. For a local checkout, add the repo root as a local
marketplace instead:

```bash
codex plugin marketplace add /path/to/captino-openai-plugin
```

The marketplace file is `.agents/plugins/marketplace.json` at the repo root.

## Authentication

The server uses OAuth, so there is nothing to configure: Codex and ChatGPT
discover the Captino sign-in from the server and register themselves.
`mcp.json` declares only the server's type and URL.

On connect, the user signs in on captino.io and ticks the resources the app may
use on a consent screen: Funnel, Contact and Form (read or write), Performance
and Subscription (read). Grant Funnel write, Contact write, Form write,
Performance read and Subscription read to use every skill. The connection acts
as the user who approved it, in that user's Captino account.

**Codex** asks to sign in when the plugin is installed. To sign in later, or
again:

```bash
codex mcp login captino
```

**ChatGPT** asks to connect Captino when the plugin is installed and opens the
same sign-in.

Tokens refresh on their own. Connected apps are listed in Captino under
**Settings → MCP** (`/app/mcp-settings`), where they can be revoked. To change
permissions, connect again and tick different boxes (Codex:
`codex mcp logout captino`, then `codex mcp login captino`).

## Skills

| Skill | What it does | Needs |
| :-- | :-- | :-- |
| `funnel-performance` | Visits, opt-ins and opt-in rate for a period, change vs previous period, funnel ranking, head-to-head | Funnel read, Performance read |
| `funnel-dropoff` | Per-step conversion, biggest drop, per-question form abandonment | Funnel read, Performance read |
| `leads` | New leads, contact search, lead activity and source funnel, pipeline counts | Contact read |
| `lead-followup` | Qualify a lead, move it through the pipeline, set deal value, add a note, schedule a meeting | Contact write |
| `pipeline-report` | Weekly or monthly account overview: pipeline, funnels, subscription usage | Contact, Funnel, Performance, Subscription read |
| `page-builder` | Build, edit and publish funnel step pages (landing, opt-in, thank-you, popups) from a brief | Funnel write |
| `form-builder` | Build, edit and publish multi-question forms (lead, qualification, survey) and add them to a funnel as a form step | Form write, Funnel write |
| `captino-setup` | Connect and sign in from Codex or ChatGPT, change permissions, troubleshoot 401/403/missing tools | none |

Skills are picked up from natural questions such as "how did Spring Campaign do
last week", "any new leads today", "build me a landing page for the webinar"
or "create an application form for the coaching funnel".

## MCP tools

The server exposes only the tools the granted permissions allow. Each group
below is one resource on the consent screen, with the OAuth scopes
`<resource>:read` and `<resource>:write` (`funnel:read`, `contact:write`, ...);
Performance and Subscription are read only. Write implies read.

- **Funnel**: `list_funnels`, `get_funnel`, `list_funnel_steps`, `create_funnel`,
  `update_funnel`, `set_funnel_active`, `create_funnel_step` (site step, or form
  step with `formId`), `set_funnel_step_visibility`, `set_funnel_step_form`,
  `set_form_step_completion`, `delete_funnel`
- **Page builder** (Funnel permission): `get_page_builder_reference`,
  `get_page_project`, `validate_page_project`, `save_page_project`, `publish_page`
- **Contact**: `list_contacts`, `list_leads`, `get_contact`, `get_contact_activity`,
  `list_contact_opt_ins`, `get_contact_pipeline_stats`, `get_contact_options`,
  `update_contact`, `create_contact_meeting`
- **Performance**: `list_funnel_performance`, `get_funnel_performance`,
  `compare_funnel_performance_with_previous_period`, `get_funnel_step_performance`,
  `get_funnel_conversion_stats`, `get_form_step_performance`, `compare_funnels`
- **Subscription**: `get_subscription`, `get_subscription_usage`
- **Form**: `list_forms`, `get_form`, `create_form`, `update_form`, `publish_form`,
  `delete_form`, `list_form_responses`, `get_form_performance`

Ids are GUIDs, dates are ISO 8601 with offset, lists are paged with `page`
and `itemsPerPage` (max 100).

## Development

The seven analysis, page-building and form-building skills are shared with the
Claude Code plugin in
[captino-claude-plugin](https://github.com/Grumsen-Development-ApS/captino-claude-plugin)
and their `SKILL.md` must be kept identical by hand; there is no sync step.
`captino-setup` is client-specific and maintained separately in each plugin.

Keep `mcp.json` to `type` and `url`. Agent Plugins 1.0.0 has no auth fields in
`mcp.json` and Codex rejects unknown keys in a server entry, so an
`extensions["com.openai"].auth` block would drop the server. Codex and ChatGPT
find Captino's OAuth through the server's discovery metadata instead.

Each skill also has `agents/openai.yaml` with an `interface` block (display
name, short description and default prompt shown in the ChatGPT skills picker)
and the Captino MCP dependency. Add it for any new skill, keep the dependency
entry the same across skills, and update the short description when a skill's
scope changes.

The ChatGPT directory listing comes from `extensions.com.openai.interface` in
`plugin.json`. Review rejects it unless the subtitle (`shortDescription`) is 30
characters or fewer, there are at most three `defaultPrompt` entries, and the
privacy policy, terms of service and support URLs all load publicly. The icon
is `assets/logo.png` (256×256), rendered from `assets/logo.svg`.

The review test cases (exactly five positive and three negative) are in
`extensions.com.openai.review.test_cases` in `plugin.json`. The dashboard shows
them read-only, so change them here and upload a new ZIP. The demo video and
release notes are kept in the dashboard, and reviewer credentials go only in
its review form, never in the ZIP. The positive cases expect the demo data in
the review account, such as the Free Marketing Webinar funnel and its leads.

When MCP tools change in the API (`API/MCP/Tools/`), update the tool list above
and the skills that use them, in both plugins. Bump `version` in `plugin.json`
and in the Claude Code plugin together. Every push to `master` that touches
`plugins/` zips this directory and publishes it to a GitHub Release tagged
`v<version>` (`.github/workflows/release.yml`).
