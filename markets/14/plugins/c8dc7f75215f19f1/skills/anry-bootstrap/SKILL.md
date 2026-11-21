---
name: anry-bootstrap
description: Use for any question about a store's revenue, conversions, paid ads performance, site setup, or what visitors did. Also for recording what the team changed on a site. Loads Anry's own analysis playbooks over MCP before answering.
---

# Work with Anry

Anry's MCP server carries the playbooks its own analysts work from. Do not
analyze from scratch: load the playbook first and follow it.

1. Start with `list_sites`; every other tool takes one of its site ids.
2. Call `list_playbooks` and load the one that fits with `get_playbook`,
   then follow it step by step.
3. Load `operating-principles` once per session and keep to it whichever
   playbook runs.
4. Before diagnosing a page, a campaign or a move in the numbers, read
   `list_diary_entries` for the window: a change the team already recorded
   is the first explanation to test.
5. When the team ships a change, or you establish a dated fact worth
   keeping, record it with `record_diary_entry`. Facts only, never
   intentions or to-dos, and never personal data in the text.

Quote every monetary figure exactly as a tool returns it, in the store's own
currency.

<!-- Canonical copy. plugins/build.sh stamps it into each platform package
     (plugins/chatgpt, plugins/claude); do not edit those copies. The skill
     stays a pointer: methodology lives on the server
     (backend/priv/mcp/), never in this file. -->
