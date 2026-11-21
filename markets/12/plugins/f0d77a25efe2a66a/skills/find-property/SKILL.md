---
name: find-property
description: Find verified HataHub listings and HataHub Aggregator listings in Ukraine, or read details for a supplied listing link. Use for monthly rent and sale comparisons; no account or transaction actions.
---

# Find a property on HataHub

Use `search_listings` to search the public catalog and `get_listing` to read a public listing. Ask only for missing search preferences that materially change the result. The tools do not need a HataHub account.

## Choose a public catalog

Use the public catalog reference matching the user's chosen transaction, property type, and city. Supported route shapes:

- Monthly rent: `https://www.hatahub.com.ua/orenda/kvartyry/kyiv`
- Sale: `https://www.hatahub.com.ua/prodazh/budynky/ukraina`

Use `kvartyry` for apartments, `budynky` for houses, `kimnaty` for rooms, `harazhi` for garages, and `zemlia` for land. Common catalog city slugs include `kyiv`, `lviv`, `odesa`, and `dnipro`; `ukraina` covers the country. Do not substitute a personal address, coordinates, private account page, or arbitrary external URL. If a catalog reference is rejected, clarify the location or use a known supported catalog with the user's agreement.

Pass price bounds in the chosen currency (`uah`, `usd`, or `eur`). Default currency is UAH for rent and USD for sale. Prices apply per month for rent and to the total for a sale. Room values are `studio`, `1`, `2`, `3`, and `4`; `4` means four or more. Send only these search preferences and the public catalog URL, without conversation text or personal identity data.

## Present the actual results

Present only facts returned by the tools, with listing links. Preserve the exact currency and price period. In hosts with plugin UI, search results offer a horizontal card carousel, in-chat details, a load-more action, and an expandable 3D map with price pins, 2D/3D controls, and a matching card carousel. Use the returned mapLocation only; its precision can be approximate, and a missing position is not permission to invent a pin. The map shows the returned results, not every listing in the marketplace. Do not duplicate its photos as Markdown image embeds. In a host without the gallery, provide clickable photo links when requested. The tools expose structured details; do not invent seller descriptions, missing characteristics, addresses, or contacts.

Search returns at most six listings per page. Use the returned `nextPage` with the same filters when the user asks to continue. Fresh checks can remove stale indexed rows, so a page may contain fewer than six results. An empty page is not proof that the entire marketplace has no matching property. If `nextPage` exists, offer to continue; otherwise include the returned `searchUrl` for browsing.

Search includes verified HataHub listings and active HataHub Aggregator listings. Keep the returned inventory and verification labels visible when presenting either type of result.

For details, pass the user's public `/hata/` or `/a/` URL or an exact listing URL returned by search to `get_listing`. If a listing is unavailable, report that result. If it is archived, say so and do not present it as an active option. A claimed aggregator link can resolve to the owner's current public HataHub listing; use the returned URL and status.

Explain verification using the returned label, identity status, and scope. For `inventory=aggregated`, show `Агрегатор` and state that identity and ownership are unverified. Do not apply HataHub's identity, ownership, or live-media verification claims to aggregator inventory. `media=live` indicates HataHub's live-media verification; `uploaded` does not. `ownershipScope=land` means the land is verified while the building is unregistered; `unverified` makes no ownership claim. Report these as HataHub's checks, without claiming an independent legal assessment. Active publication is not confirmation of booking dates, vacancy, or transaction readiness.

Explain the supported boundary when asked to contact an owner, reserve a property, pay, access an account, or retrieve government identity/registry records. Do not invoke these read-only tools as a substitute for an unsupported action or claim that the action happened. Use the user's language; Ukrainian is the default when no language preference is apparent.
