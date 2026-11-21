# Reteno AI Plugin

This repository contains installable releases of the Reteno plugin.

Reteno 0.4.1 packages the same skills and compiled SDKs for Codex and Claude Code. It uses the
host's authenticated Reteno MCP connection; local helpers do not need agent tokens, private
repositories, publisher proxies or control-plane sessions.

## Changes in 0.4.1

- Correct system-option values, organization-local activity date boundaries and cross-channel
  activity validation in dynamic segments and audience counts.
- Bundle stable email SDK 0.2.22 with intentional inline CSS edits and saved-style verification.
- Resolve saved modules by visible UID while using the matched numeric ID for placement.
- Use workflow-level analytics for workflow totals and label open rates derived from counts.
- Apply single relative Timer changes with focused instructions, guarded saves and graph checks.

## Features

| Skill | Capabilities |
| --- | --- |
| `reteno-email-editor` | HTML edits/localization with token and responsive-markup protection; all-language cloning, sender/Reply-To preservation, saved modules and 17 Fiteno templates |
| `email-model-editor` | Native structure/style/content and preheader edits, base/target merging and saved desktop/mobile verification |
| `email-from-reference` | Native email creation and explicit rebuilds from authorized references, supplied images and Reteno image jobs |
| `email-deliverability` | DKIM/CNAME, enforced DMARC, envelope-domain SPF and mandatory custom link-domain checks; missing evidence stays unavailable |
| `reteno-analytics` | Messaging/events, export date sharding with partial results, and audience analytics; exact active-workflow count remains limited |
| `segment-designer` | Validated dynamic segments and unsaved audience counts using live account definitions |
| `workflow-designer` | SDK edits and inactive workflow creation/cloning with hash preconditions and verified saves |
| `business-profile` | Existing profile reads and scoped updates from supplied information/files/account emails; no website extraction |
| `web-funnel-analyzer` | Existing Playwright onboarding-funnel capture, stopping at email collection |

Reteno only. Viber and Telegram channels are excluded. The plugin does not send, schedule or
activate campaigns as part of authoring. Supplied-image hosting does not trigger paid generation.

## Install

Claude Code:

```text
/plugin marketplace add reteno-com/ai-plugin
/plugin install reteno@reteno-plugins
```

Skills use `/reteno:<skill-name>`. Complete OAuth in `/mcp` for `reteno`.

Codex: add this repository as a plugin marketplace and install `reteno@reteno-plugins`. The
repository includes `.agents/plugins/marketplace.json` and the `.codex-plugin/plugin.json`
manifest. Complete Reteno OAuth on installation or first use.

Requirements: Python 3.11+, Node.js 20.18.1+. Install `requirements.txt` in the Python
environment used by the host's helper commands for trusted HTTPS transfers and deliverability.
Funnel capture additionally uses `requirements-funnel.txt`
and a Playwright Chromium installation. Run `python3 scripts/doctor.py` to inspect prerequisites.
Compiled SDKs and editor validation rules ship in `packages/`; no npm install is required.

## Data and external services

Reteno requires an authorized account connection at `https://mcp.reteno.com`. The skills request
only the records, content and operations needed for the user's task. They can read customer and
campaign data and save authorized changes to Reteno. They do not require full conversation history.

Some helpers also make network requests outside the declared MCP connection:

- **Authorized file transfers:** helpers download exports, models, previews and images and upload
  prepared files using the HTTPS URLs returned by Reteno or explicitly supplied for the task.
- **Deliverability checks:** the audit helper queries public DNS and checks TLS on the relevant
  sending or tracking domains. These requests disclose the queried domain and normal connection
  metadata to the contacted resolver or host.
- **Funnel analysis:** Playwright opens the user-selected website and walks its quiz with synthetic
  default answers, stopping at email collection. The website receives normal browser requests and
  the answers submitted during that navigation. Screenshots and visible DOM text are saved locally.
  Text embedded in images or canvases is not transcribed. The helper does not upload screenshots
  to a transcription service or use an API key from the user's environment.

The bundle also runs packaged Python and Node.js helpers locally in the host environment. Local
exports, screenshots and working files remain in that workspace until its owner or host removes them.
Reteno-held customer data follows the applicable customer agreement, DPA and documented instructions;
retention can exceed 30 days. External providers and the AI client apply their own service terms and
settings to their copies.

See the [Reteno privacy policy](https://reteno.com/privacy-policy),
[Data Processing Agreement](https://reteno.com/dpa), and
[OpenAI privacy information](https://openai.com/policies/privacy-policy/).

