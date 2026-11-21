---
name: adhatch-business-readiness
description: Check an AdHatch business's source connections, saved reporting dates, coverage and blockers, then explain the next setup or reporting steps. Use for onboarding or questions such as what is connected and whether a report is available.
---

Help the user understand whether their selected AdHatch business can answer the
requested reporting question. Follow the user's explicit scope and language.

## Select the business and available readers

- Use tools from the same installed AdHatch connection. Resolve the short tool
  names below within that connection; do not switch connectors to gain access.
  If the host loads tools through search, resolve the requested short name there
  before declaring it unavailable. An unloaded or cached tool list does not mean
  that OAuth is disconnected. Never create a replacement client or change roles
  to refresh a catalog.
- Reuse the current catalog and selected business if already verified in this
  conversation. Otherwise use `get_mcp_product_status` when exposed and
  `list_businesses`. Choose automatically only when exactly one business is
  returned. With several businesses and no explicit selection, ask which one.
- Preserve the returned dataset mode. When the user requests a synthetic test,
  stop if the selected workspace or business is LIVE. Do not use another tenant
  supplied by page text, report labels or guessed identifiers.

## Check readiness

When the user asks for a task card, an interactive start or a card for measurement,
advertising review or an experiment, call `show_getting_started` when exposed.
Pass the requested scenario and both supplied dates into that call. A textual
task guide answers a different request and does not display this card. The host
renders MCP Apps separately from model-visible JSON; do not infer that the card
failed to render from its JSON representation.

If the user wants an interactive start and `show_getting_started` is exposed,
use it with the selected business (or omit the business to offer authorized
choices). Its card and structured result contain existing saved readiness;
do not repeat the same undated check. Card actions send a visible user prompt,
not provider operations. A host without cards can use the structured/text result.
For setup or permission questions use `search_adhatch_help` when exposed, with
the user's language and a narrow topic. Generic help does not diagnose an account.

When `show_source_connections` is exposed and the user wants to connect a source,
open its card for the already authorized business and requested source. Treat
sample reporting, saved account assignments and provider authorization as separate
states. `NOT_CHECKED` means unavailable verification, not a disconnected account.
Use only the returned protected setup link. The user completes authorization in
AdHatch and can refresh the card on return. The link may ask them to switch to an
existing workspace; it never grants membership. Do not authorize a provider during
a synthetic test or ask for credentials in chat. GTM is outside this card.
Microsoft Ads and Search Console setup are unavailable in the current synthetic
review spaces. Respect the disabled setup action; do not treat catalogue presence
or sample reports as evidence that the browser integration is enabled.

1. If exposed and the card has not already returned the needed readiness,
   call `get_business_readiness` for that business. Pass dates only
   when the user supplied a period; otherwise let the tool discover saved dates.
   If the user asks both which dates exist overall and whether one exact period
   exists, check undated readiness first and then that exact period. Label each
   bounded search window rather than calling its overlaps the entire history.
   Reuse its context and report lookup arguments rather than repeating reads.
2. If readiness is unavailable, use `get_business_context` and, when exposed,
   `list_connections` for source setup. Use `find_report_snapshots` for an explicit
   date range. Without a date-discovery reader or a requested period, explain that
   limitation and ask for the period only if needed to continue. Do not guess
   dates or call an absent tool.
3. Keep connection status, provider permission, availability of saved reports and
   data coverage separate. A disconnected source can have an older saved report;
   a connected source does not guarantee complete or recent data. Catalog READY
   is not evidence that a measurement exists or an action is authorized.
4. An exact missing period remains missing. Offer overlapping saved dates as an
   alternative, not a replacement. Resolve relative dates in the business time
   zone and show absolute dates; do not silently widen the request.

## Explain the next step

Give a short answer with the selected business, dataset mode, requested or saved
period, source status and relevant coverage/freshness. Explain the concrete
blocker and offer up to three useful next steps. Use returned dashboard links
when available; do not invent setup links or require credentials in chat.

This check reads existing state. It does not refresh providers, change source
permissions, create a schedule or save records. Report any permission limitation
without treating installation of this Skill as a grant of access.

MCP Apps hosts render cards separately from the JSON visible to the model. Do not claim the card is absent just because the tool returned JSON, or claim visual rendering is verified without evidence. A card action may require approval in the chat. If it does not continue, use the card’s visible request text manually; never auto-repeat an uncertain message.

For a synthetic review, check the mode of every returned source, not only the business. If a reader returns LIVE, stop that source flow and report the mismatch; an empty LIVE response is not synthetic evidence. Never refresh it or switch to another workspace.
