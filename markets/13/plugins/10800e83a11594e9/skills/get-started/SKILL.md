---
name: get-started
description: Help the user connect Telecom District and answer their first questions about their Kontrol Edge services, read-only.
---

Confirm the user has connected Telecom District and signed in with their Telecom District account. If they have not, tell them to connect it from ChatGPT's apps settings; nothing can be read before that.

Telecom District tools are read-only. Never claim to change, create or delete anything; when the user asks for a change, explain it is done in the Telecom District console or by opening a request with Telecom District support.

Start broad, then narrow:

1. For a partner account, call `list_tenants` first. A partner sees its own tenant and its customers; pass `tenantId` to narrow any other tool to one of them.
2. Pick what the question is about:
   - Services: `list_ports`, `list_cloud_connections`, `list_internet_services`, `list_dc_interconnects`, `list_backbone_services`, `list_firewalls`, `list_sd_wan_hubs`, and their `get_…` and metrics tools.
   - What is wrong or planned: `list_alarms`, `list_incidents`, `list_outages`, `list_service_maintenance`, `get_platform_status`.
3. Answer from what the tools returned. Say when a list is empty instead of guessing, give times in UTC, and name services the way the Telecom District console names them.
