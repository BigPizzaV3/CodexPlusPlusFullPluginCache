# Monitor Hub OpenAI Plugin Package (v1.1.0)

This package registers the production Monitor Hub remote Model Context Protocol (MCP) server for ChatGPT and OpenAI Codex. It conforms to the `agent-plugins.org` v1.0.0 open specification and the OpenAI Plugins / Apps directory guidelines.

## Included MCP Tool Surface (24 Tools)

The connected MCP server at `https://mcp.monitorhubs.com/mcp` provides both comprehensive telemetry queries and operational management:

### Telemetry & Diagnostics (Read-Only)
- `read_monitor_status`: High-level summary of active monitors and system operational status.
- `list_monitors`: Filter and list monitors by status, type, tag, or keyword.
- `get_monitor_details`: Detailed configuration, SSL status, and last check telemetry.
- `get_monitor_history`: Historical check log and latency measurements.
- `search_monitors`: Search monitors by name or URL target.
- `read_server_status`: List connected Linux & Windows server telemetry agents.
- `get_server_metrics`: CPU, RAM, disk, and network utilization over time.
- `read_incidents`: Active and resolved outage incidents.
- `get_incident_details`: Incident root cause analysis (RCA), timeline, and response times.
- `list_recent_outages`: Chronological log of recent service disruptions.
- `read_uptime_stats`: SLA uptime percentages and average response times.
- `read_alerts`: Outage notifications dispatched across integrated channels.
- `list_notification_channels`: Configured channels (Slack, Discord, Telegram, Email, Webhooks).
- `list_status_pages`: Configured public status pages and CNAME domains.

### Management & Remediation (Read & Write)
- `create_monitor`: Deploy a new HTTP, HTTPS, TCP, or Ping synthetic check.
- `update_monitor`: Update monitor interval, target URL, timeout, or name.
- `pause_monitor`: Temporarily halt checks during maintenance.
- `resume_monitor`: Resume monitoring for paused endpoints.
- `delete_monitor`: Permanently decommission a monitor.
- `test_endpoint`: Probe an external URL and verify response code, latency, and headers.
- `resolve_server_warning`: Acknowledge and resolve warning state on server agents.
- `acknowledge_incident`: Mark an active outage as acknowledged by the on-call engineer.
- `resolve_incident`: Resolve an active incident and log remediation notes.
- `trigger_test_alert`: Test notification channel delivery.
- `update_status_page`: Update public incident banners and maintenance announcements.

---

## Authentication & Security Invariants

- **Authentication Protocol**: RFC 7591 dynamic client registration + RFC 8414 OAuth 2.1 authorization server with PKCE (`S256`).
- **Transport**: Remote Streamable HTTP MCP at `https://mcp.monitorhubs.com/mcp` and Server-Sent Events (SSE) at `https://mcp.monitorhubs.com/sse`.
- **Declarative Scopes**:
  - `mcp:read`, `monitor:read`, `server:read`, `alerts:read`, `incidents:read`, `status:read`
  - `mcp:write`, `monitor:write`, `server:write`, `incidents:write`, `status:write`
- **Tenant Isolation**: All operations are strictly bounded to the authenticated user's workspace.

---

## Packaging & Review Submission Checklist

1. **Rebuild the ZIP archive**:
   Run `python package-plugin.py` to create `monitor-hub-plugin-1.1.0.zip`.
2. **OpenAI Portal Upload**:
   - In the OpenAI Platform / ChatGPT Plugins portal, select **"Create Plugin"** -> **"With MCP"**.
   - Upload `monitor-hub-plugin-1.1.0.zip`.
3. **Domain Verification**:
   - Verify domain ownership for `https://mcp.monitorhubs.com` and `https://monitorhubs.com`.
4. **Tool Scan**:
   - Click **"Scan Tools"** and verify that all tools are discovered with their input schemas.
5. **Reviewer Credentials (Private Form Only)**:
   - Provide a dedicated test account (e.g. `openai-reviewer@monitorhubs.com`) with sample data and MFA disabled.
   - Include the walkthrough demo video link (`https://youtu.be/0XKRl2g-hsw`).
