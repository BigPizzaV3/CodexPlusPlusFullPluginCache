---
name: automotive-readonly
description: Use TalkToData Automotive to explore authorized transport, vehicle, fleet, workshop, appraisal, parts, road and public data in the user’s language.
---

# TalkToData Automotive

Use this skill whenever this plugin is invoked. Answer in the language of the user’s latest request; default to Hebrew only when no preference is apparent. The secure portal offers Hebrew and English.

1. Call listAutomotiveConnections first. Use only connection IDs returned for the signed-in user. If connectionRequired is true, show setupUrl immediately and keep this chat open. Keys, secrets, passwords and OTPs belong only in the secure portal, never in chat. Recheck connections after setup.
2. Call listAutomotiveProviders to identify products, aliases, capabilities and setup status. A keyword, directory entry or pending request does not prove an active connection. Offer the returned portal and support links when setup is needed. Never claim to have connected an account without verification.
3. Use only capabilities advertised by the selected connection. Request explicit dates for period reports and follow nextPage when completeness matters. Preserve identifiers, units and statuses; missing values are unknown, not zero.
4. Distinguish synthetic review_fixture data, authorized provider_api records and public_api data in every answer. Vehicle, customer, insurer, appraisal and claim records require the user’s authorized connection. Never search another customer’s private records.
5. WPS catalog query is an optional exact SKU. AutoWiz catalog query is a required exact OEM number returning alternative part numbers from the customer catalog. Neither is a vehicle-fitment guarantee; AutoWiz does not decode VINs.
6. For Israeli public data, list datasets and fields before querying. Use returned dataset IDs and exact field names. Keep source links and update dates. Public data is not business-account data or necessarily current. No result does not establish valid registration, roadworthiness or absence of recalls.
7. NHTSA VIN results may be partial and primarily cover the US market. Preserve ErrorCode/ErrorText; do not invent missing specifications, ownership or accident history.
8. TomTom traffic covers a road segment near a coordinate. HERE estimates routes; request actual dimensions and weights for truck or bus modes, preserve provider notices and label bus modes Beta. Do not present estimates as navigation instructions or claim coverage of hazardous cargo, axle loads or every special restriction.
9. TfL and MBTA return bus route catalogs for London and the Boston area respectively, not live arrival times. Preserve attribution, geography and pagination.
10. Keep damage estimates, approved claim amounts, labor, parts, invoices, settlements and payments separate. An estimate is not paid revenue or an insurer decision.

## Read-only and support

These tools read data. They cannot change appraisals, claims, work orders, appointments, vehicles, customers, stock, documents or payments; they cannot order parts or approve claims. For requested write permissions or actions, link the returned setupUrl/supportUrl or hello@navines.com to explore a separate integration based on the provider and desired actions. Do not claim write access has been enabled.

After website authorization, the user returns to the screen where authorization began. To start a new chat with the plugin, open the returned pluginUrl, choose Try in chat and send the prefilled question. For an existing chat, return to its original tab. Do not promise a direct return to an arbitrary chat or automatically send a message.

Product names and keywords identify relevant software families and services. They do not imply vendor sponsorship, endorsement or access to an unconnected account.
