# LQT Opener Generator MCP submission checklist

- Upload through **With MCP** as a new plugin, not the old skills-only entry.
- Use the real MCP endpoint in mcp.json.
- Confirm the exact category in the dashboard.
- Confirm the website, legal pages and support URL; the support URL currently uses the homepage, which should be replaced by a dedicated support page if required by reviewers.
- Add a reviewer-accessible demo recording URL to the dashboard review details; no recording URL has been invented or included.
- Review the 5 positive and 3 negative cases in plugin.json, run them in ChatGPT, and correct any mismatches before submission.
- Run the dashboard MCP tool scan and resolve findings.
- Verify the publisher identity and any required domain ownership.
- For production publication upgrade hosting to a reliable always-on instance and review server privacy/security and log retention.
- The skill contains the teaching workflow; the remote MCP server implements the two tools. The Python server itself is NOT in this package because the remote server remains deployed on Render.
