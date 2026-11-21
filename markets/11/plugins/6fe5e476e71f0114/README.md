# PartyPass for ChatGPT and Codex

PartyPass hosts an invitation created in an AI conversation and returns a
shareable preview link plus a link for the host to claim the event. After
claiming, the host can manage delivery, RSVPs, QR passes, and reminders in
PartyPass.

The plugin connects to the public Streamable HTTP MCP endpoint:

```
https://mcp.partypass.mx/mcp
```

## Publisher and support

- Publisher: **DCM DEVS** (PartyPass is its trade name)
- Website: <https://www.partypass.mx>
- Support: <https://www.partypass.mx/soporte>
- Legal, billing, and privacy contact: [WhatsApp +52 639 175 0101](https://wa.me/526391750101)
- Privacy policy: <https://www.partypass.mx/privacy>
- Terms: <https://www.partypass.mx/terms>
- Legal notice: <https://www.partypass.mx/legal>

## Tool

`host_invitation` accepts either a self-contained HTML invitation or a JPG,
PNG, or WebP invitation, plus event metadata. It creates a new hosted draft;
it never sends messages, charges the user, or changes an existing event.

The user should receive both returned URLs:

- `previewUrl` — the invitation can be viewed and shared immediately.
- `claimUrl` — the host claims the event before publishing or sending it.

## Local package validation

```sh
node -e 'for (const f of ["plugin.json", "mcp.json"]) JSON.parse(require("fs").readFileSync(f, "utf8")); console.log("valid JSON")'
```

The MCP service implementation and its test suite are in [`../../mcp`](../../mcp).
