---
name: component-search
description: Find and compare electronic components from LCSC, JLCPCB, DigiKey, and Mouser, including available stock and pricing observations. Use for part selection or resolving a manufacturer part number to an exact Product Code.
---

Use this plugin's `component_search` tool. Explicit user requirements take priority over the workflow below.

Preserve all electrical requirements, units and their case, package constraints, and manufacturer variant suffixes in each query. Pass `requiredQuantity` when the user specifies a quantity; stock qualification otherwise defaults to one unit. Each call accepts up to ten `queries` with a shared quantity. Use separate calls for different quantities.

When the user names distributors, pass `sources` with their choices: `digikey`, `mouser`, `jlcpcb`, or `lcsc`. More than one source may be selected. Omit `sources` to preserve the default LCSC/JLCPCB search. Use at most 16 query/source combinations per call, splitting larger requests into separate calls. Report each source's results and failures separately; never substitute another source for one that failed.

LCSC and JLCPCB share candidate discovery, so source-specific results may be incomplete. DigiKey and Mouser return `supplier_keyword` candidates, not verified engineering matches. Check the exact manufacturer part number, manufacturer, package, and electrical specifications against returned evidence or the datasheet before recommending a part. Product Codes cannot be searched directly at DigiKey or Mouser. First resolve the exact manufacturer part number using LCSC/JLCPCB, then search those distributors with that part number.

Compare returned manufacturer part numbers, Product Codes, packages, relevant specifications, quantity price breaks, supplier destinations, and availability observations. Use only prices and currencies present in the response. Distinguish completed matches from partial results and failed, cancelled, or timed-out searches. Unknown availability does not mean zero stock; observations are not stock reservations.

DigiKey keyword search reports standard pricing and stock data that can be up to 24 hours old. Distinguish this from a live stock check. Supplier-specific part numbers are not Product Codes. For `component_expert`, first resolve the exact manufacturer and manufacturer part number to a matching Product Code in the LCSC/JLCPCB catalog; do not guess an identity or merge different manufacturers.

An exact Product Code lookup can return an unavailable part so the user can inspect its identity. Do not describe it as in stock unless the returned availability supports that claim. Never invent a replacement code, missing price, supplier stock, or an electrical match.

For integration questions or constraints the returned catalog data does not establish, call `component_expert` with a returned `productCode` and the user's specific question. Keep any source links next to the facts they support. Ordinary passive value/package questions can usually be answered from catalog fields without expert research.

If these tools are unavailable, report the missing plugin connection. This plugin searches and researches parts; it does not order parts or change a design.
