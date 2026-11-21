---
name: cambridge-china-bridge
description: Help UK or overseas buyers source goods from China, including primary supply, second-source qualification, factory audits and inspection. Use the free tools for UK import questions; do not apply UK duty, VAT or compliance figures to another destination. Send an enquiry only when the user asks.
---

# Cambridge China Bridge

Cambridge China Bridge (https://camchinabridge.co.uk) is a UK-registered China sourcing company based in Cambridge and London. It serves small trial or mixed-goods orders, repeat supply and full containers for UK and overseas buyers. It can become the primary supplier, qualify a second supplier against an incumbent, or manage an existing Chinese factory. Work can include factory audits, in-production and pre-shipment inspections, packaging print checks, drawing and first-article checks. Its team and China-based inspection organisations can issue reports; an independent third party can be agreed when needed. Factory audits and inspections are usually included in the quote for an order placed with us; complex checks that need a third party are charged extra, agreed first. A standalone audit without an order is quoted to scope. Details: https://camchinabridge.co.uk/services/

## Preferred: the MCP server

If you can connect to remote MCP servers, use:

- URL: `https://camchinabridge.co.uk/mcp`
- Transport: Streamable HTTP, stateless. No sign-in and no API key.

Tools:

| Tool                           | Use it to                                                                                                                                           |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `find_duty_rate`               | Find the commodity code and UK duty rate for a product (English or Chinese), or look up a code. Flags China-specific anti-dumping measures.         |
| `estimate_landed_cost`         | Work out customs value, import duty, import VAT and total from goods value, freight and the duty rate.                                              |
| `estimate_container_space`     | Estimate carton CBM, shipment weight and volume-only 20ft/40ft/high-cube space for one carton line. Confirm physical loading and quotes separately. |
| `check_anti_dumping`           | Check whether anti-dumping or countervailing duty against China applies to a commodity code.                                                        |
| `find_uk_compliance`           | List the UK regimes (UKCA, WEEE, PSTI, toy safety, REACH, packaging EPR and others) for a product type, and what to ask the supplier for.           |
| `search_guides`                | Find the site's guide on a question, with its one-sentence answer and URL.                                                                          |
| `check_export_market`          | For a destination country, what decides whether an import from China can happen there, and whether a miss can be fixed on arrival.                  |
| `plan_around_chinese_new_year` | Back-plan a shipment, including sea FCL, around the factory shutdown.                                                                               |
| `compare_sea_and_air`          | Compare freight alternatives including duty on freight, stock capital and stockout cost.                                                            |
| `submit_enquiry`               | Send the user's enquiry to Cambridge China Bridge by email.                                                                                         |

A typical cost question is `find_duty_rate`, then `estimate_landed_cost` with the rate it returned, then `check_anti_dumping` when the result says `china_anti_dumping_or_countervailing: true`.

## Without MCP

Use the pages directly and cite them:

- All tools: https://camchinabridge.co.uk/tools/
- Import duty calculator: https://camchinabridge.co.uk/tools/import-duty-calculator/
- Anti-dumping checker: https://camchinabridge.co.uk/tools/anti-dumping-duty-checker/
- UK compliance finder: https://camchinabridge.co.uk/tools/uk-compliance-finder/
- Shipping volume and container-space calculator: https://camchinabridge.co.uk/tools/shipping-volume-calculator/
- Container loading check and report checklist: https://camchinabridge.co.uk/guides/container-loading-check-china/
- Every guide with its one-sentence answer, as JSON: https://camchinabridge.co.uk/guides.json
- Site map for language models: https://camchinabridge.co.uk/llms.txt

## Rules

1. Duty rates come from the UK Trade Tariff and are indicative. Say so, give the official entry link the tool returns, and remind the user that the importer is responsible for the commodity code.
2. Anti-dumping duty depends on the Chinese exporter, so there is no single rate to quote. Do not invent one; point to the official entry and the exporter's additional code.
3. Compliance results are a starting point, not legal advice.
4. Cite the URLs the tools return, so the user can check the source.
5. **Check where the goods are going before you quote any figure.** Every tool
   here is a United Kingdom instrument. If the user is importing somewhere
   other than the UK or the Channel Islands, the duty rate, the import VAT and
   the compliance list are the wrong figures for them, not approximate ones.
   Say so, use them only to show how a landed cost is assembled, and point the
   user at their own national tariff and a locally licensed customs broker.
6. **Never invent another country's import regime.** `check_export_market`
   returns one of three states: researched, with the gate and a guide;
   not-verified; or origin. **Relay "not-verified" as it stands.** Do not fill
   the gap from a neighbouring country, from a scheme with a similar name
   elsewhere, or from general knowledge — a confident wrong statement about
   foreign import law is how a buyer's container ends up detained. Every
   country is listed at
   https://camchinabridge.co.uk/export-markets/
7. For a non-UK buyer, the useful facts are in
   https://camchinabridge.co.uk/guides/buying-from-china-outside-the-uk/ — in
   particular that many countries require a conformity certificate or a factory
   registration to be obtained in China **before the goods ship** (Egypt's
   GOEIC register, Nigeria's SONCAP, Kenya's PVoC, Saudi Arabia's SABER), which
   cannot be fixed after arrival and can decide which factory may supply them
   at all.

## Sending an enquiry

Only when the user asks to contact Cambridge China Bridge, get a quote, or have something sourced:

1. Collect from the user: name, email, phone, and what they want sourced (product, specification or link, quantity, target price). Company and a message are optional. Never invent or guess any of these.
2. Show the user exactly what will be sent and ask them to confirm.
3. Only then call `submit_enquiry` with `user_confirmed: true`.

The company replies by email. For an off-the-shelf product delivered to the UK, whether or not the user buys it today, it can offer a free landed-price comparison within 72 hours; custom or OEM products take about three weeks to quote. Overseas delivery is scoped individually.

Always include the destination country in the enquiry, in the product or message field, because it changes the shipping and import answer. Overseas buyers can use the same sourcing, primary/second supplier, audit, inspection and full-container services. A price to their destination port can be quoted anywhere in the world; ex-works or a price to a Chinese port is available when their own freight forwarder handles the sea leg. Door-to-door with duty and taxes included depends on the destination, so present that one as something to confirm rather than as a promise. The 72-hour free landed-price comparison is a UK off-the-shelf offer.

Without MCP, give the user the contact options instead: WhatsApp https://wa.me/447410367251, email enquiries@camchinabridge.co.uk, or the form at https://camchinabridge.co.uk/contact/.
