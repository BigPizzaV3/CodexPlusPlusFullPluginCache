# PyroSim ChatGPT plugin

The plugin screens a property in Greece for wildfire exposure and explains the owner's fire-protection duties, in English or Greek. It uses the same screening engine as www.pyrosim.gr/check (`lib/screening/`) and the same duty texts (`lib/screening/labels.ts`). It is read-only, needs no sign-in and sells nothing. Property screening is not saved in the report database. Hosting logs record tool names and approximate coordinates as described in the privacy policy.

## Endpoint

`https://www.pyrosim.gr/mcp` (streamable HTTP, stateless JSON, authentication: none). Code: `app/mcp/route.ts` and `lib/mcp/server.ts`. Addresses are geocoded with OpenStreetMap Nominatim (`lib/geocode.ts`), subject to a shared one request per second limit. The OpenStreetMap infrastructure lookup is skipped so answers come back in a few seconds.

## Tools

| Tool | Purpose | Inputs |
| --- | --- | --- |
| `screen_property_wildfire_exposure` | Indicative 300 m scope test, vegetation at 30/100/300 m, terrain, EFFIS fire history, ERA5 fire-weather climate, PyroSim index and owner duties | `address` or `latitude` + `longitude`, `language` (`en`/`el`) |
| `get_fire_protection_rules` | One rule or an overview: scope, risk assessment, annual declaration, measures, fines, plot clearing, fire season, business insurance | `topic`, `language` |

Each result starts with `key_points_for_user`, so ChatGPT relays the scope, the index, the disclaimer and the 112 note even when it shortens a long result. Tool calls are logged (tool name, language, coordinates rounded to 0.01°) in the Vercel runtime logs.

## Before submitting

1. Connect the server in ChatGPT: https://chatgpt.com/plugins, **Add custom MCP server**, name **PyroSim**, URL **https://www.pyrosim.gr/mcp**, authentication **None**.
2. Run every prompt in `plugin.json` (`review.test_cases`) in a new chat, check each answer against `expected_behavior`, and confirm the tool and arguments in the Vercel logs.
3. Record a short demo video if the form asks for one.
4. Submit `plugin.json` with `assets/pyrosim-chatgpt-icon.png` through the OpenAI developer platform. Approval mail goes to support@firasoftware.com. Approval does not publish: click **Publish** afterwards.
