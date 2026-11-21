---
name: simvoro-sms-prices
description: Research SimVoro public SMS service prices, countries and availability indicators without renting numbers or reading OTPs.
---
# SimVoro public SMS services and prices

1. When the SimVoro MCP is connected, call `list_sms_services` to find the requested service slug and public listing. Use `get_sms_price_options` for available countries/operators and advertised prices. Those are read-only catalog tools, not purchase or SMS retrieval tools.
2. Clearly state that stock, prices and delivery acceptance can change; a successful tool response is not proof that a number can be rented or that a third-party service will accept the number.
3. If tools fail or are disconnected, optionally inspect https://simvoro.com/sms via an available browser, otherwise tell the user you cannot verify current prices or availability. Never fabricate data.
4. The plugin cannot rent a number, view or relay received SMS/OTP codes, manage a wallet, create accounts or automate verifications. Refer such actions to the authenticated SimVoro website. Never ask users to paste OTP codes, passwords or payment details.
5. Encourage compliance with service/platform rules. Do not assist spam, mass account creation or ban evasion.
