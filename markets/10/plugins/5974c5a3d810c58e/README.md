# RentalCal ChatGPT plugin

The package OpenAI's plugin directory takes. Upload it at
platform.openai.com/plugins. The tools themselves are not in here: they
are served by the MCP server at `https://api.rentalcal.com/mcp`
(`convex/mcp.ts`), and OpenAI rescans that daily, so changes to the
tools ship with a Convex deploy and need no new upload. Rebuild the ZIP
only when something in this folder changes. Research and the rules this
follows: `docs/CHATGPT_PLUGIN_RESEARCH.md`.

**Never change the URL in `mcp.json`.** OpenAI cannot change it after
approval without a support request.

## Build the ZIP

```sh
cd packages/chatgpt-plugin
rm -rf dist && mkdir dist
zip -r dist/rentalcal-plugin.zip plugin.json mcp.json assets
```

## Before uploading

1. Deploy Convex to production, so `/mcp` is live.
2. Check it in the MCP Inspector (`npx @modelcontextprotocol/inspector`),
   transport "Streamable HTTP", URL `https://api.rentalcal.com/mcp`.
3. Upload the ZIP. In **Connect server**, copy the domain-verification
   token, run `npx convex env set OPENAI_APPS_CHALLENGE <token> --prod`,
   and click **Verify Domain**.

## Review details (entered in the dashboard)

**Authentication:** none. Every tool reads public listing data, so no
reviewer credentials are needed. Each tool declares
`securitySchemes: [{ type: "noauth" }]`, and `api.rentalcal.com`
answers 404 to `/.well-known/openid-configuration` on purpose
(`convex/http.ts`): with either missing, **Connect server** tries OAuth
client registration and fails with "registration endpoint returned 404".

**Commerce:** the plugin sells nothing in ChatGPT. `get_quote` returns
a link to the host's booking page on rentalcal.com, where the guest
reviews the stay and pays the host directly (external checkout).

**Annotation justifications** (all four tools are the same):

- `readOnlyHint: true`: the tool only reads published listing,
  calendar and pricing data. It creates no booking and changes nothing.
- `destructiveHint: false`: nothing is written, so nothing can be
  deleted or overwritten.
- `openWorldHint: false`: it reads one closed catalogue (published
  RentalCal booking sites), not the open web, and posts nothing anywhere.

**Positive test cases.** These use `beach-house.rentalcal.com`, the same
review property the Muse submission uses (`docs/PUBLIC_API.md`).

1. "Tell me about beach-house.rentalcal.com." → `find_property`. Returns
   the listing: location, capacity, amenities, nightly price.
2. "What dates are open there in the next two months?" →
   `check_availability`. Lists open ranges and the minimum stay.
3. "How much for 3 nights from <an open date> for 2 guests?" →
   `get_quote`. Itemised price with total and a booking link.
4. "Can I bring my dog?" → `get_property`. States whether pets are
   allowed and any pet fee.
5. "Book it." → no new tool call. ChatGPT gives the `bookingUrl` from
   the last quote and says the booking is finished on the host's page.

**Negative test cases**

1. "Find me a cabin in Tofino." → No search across properties. The
   plugin asks for a booking site address instead of inventing one.
2. "Quote 3 nights at beach-house.rentalcal.com for 40 guests." →
   `get_quote` refuses with the property's guest limit. No price shown.
3. "Cancel my booking at beach-house." → No tool can change a booking.
   ChatGPT points the guest to the host or their confirmation email.
