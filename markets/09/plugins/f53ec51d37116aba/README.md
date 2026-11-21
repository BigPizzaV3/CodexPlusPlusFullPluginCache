# Capable Cap Table for ChatGPT

Connects ChatGPT to a company's cap table in [Capable](https://capable.so) through its remote MCP server at `https://capable.so/api/mcp` (OAuth 2.1 with dynamic client registration).

- Admins read the cap table, stakeholders, securities, vesting, 409A status and recent activity, and model a priced round or an exit.
- Employees, advisors and investors read their own equity.
- Changes are proposals only. An admin approves each one in Capable before anything changes.

Support: https://capable.so/support. Privacy: https://capable.so/privacy. Terms: https://capable.so/terms.

Build the ZIP from the repository root with `scripts/plugin/build.sh`. The server's tools are documented at https://capable.so/docs/mcp.
