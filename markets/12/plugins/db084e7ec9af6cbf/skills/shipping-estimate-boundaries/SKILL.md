---
name: shipping-estimate-boundaries
description: Use for BoslogShip public US parcel rate estimates and explaining this connection's limits, including requests for international rates, label purchases, account access or tracking.
---

# BoslogShip shipping estimate boundaries

Apply these instructions only to the BoslogShip plugin workflow. This connection provides anonymous, read-only public estimates for up to five US domestic residential parcels through the connected `get_shipping_rates` tool. No BoslogShip account is needed for this estimate tool. It cannot purchase or reserve a label, charge an account, connect a private account, retrieve account-specific prices or track shipments.

## Identify unsupported requests before collecting information

- If the user explicitly requests an international route, label purchase, payment, private account access or tracking, explain that this BoslogShip connection cannot perform that operation.
- Describe the limitation as a limitation of **this connection**, not a claim that the BoslogShip business or website has no other services.
- Do not invoke the rate tool solely to fulfill an unsupported request. Do not invent a price, purchase, charge, account record or tracking result.
- For an unsupported international route, do not convert cities into arbitrary US ZIP codes, offer to obtain an international carrier quote through this connection, or continue an intake interview.
- Do not ask for full pickup or delivery street addresses, recipient names, email addresses, phone numbers, parcel contents, declared customs values or documents to continue an unsupported international workflow.
- Do not ask for account passwords, verification codes, payment information or credentials for an unsupported account, tracking or purchase workflow.
- Keep the response brief, use the user's language, and offer help with a supported US parcel estimate only if useful. Do not imply that providing additional personal details will unlock an unsupported operation.

Examples of an appropriate international-route response:

English: "This BoslogShip connection only provides public US domestic parcel estimates, so it cannot quote the Paris-to-Shanghai route. Please do not send full addresses or customs details here."

Chinese: "当前 BoslogShip 连接仅提供美国境内包裹的公开运价估算，无法查询巴黎到上海的国际运费。请勿在此发送完整地址或报关资料。"

US Spanish: "Esta conexión de BoslogShip solo ofrece estimaciones públicas para paquetes dentro de EE. UU.; no puede cotizar la ruta de París a Shanghái. No envíes aquí direcciones completas ni datos aduaneros."

## Keep supported quotes read-only and minimal

For a supported US route, ask only for missing five-digit origin and destination ZIP codes, package quantity, each package's weight and dimensions. Convert units explicitly to pounds and inches. An existing shipping amount is optional and is only for a savings comparison.

Use the connected `get_shipping_rates` tool and its actual returned data. Each returned price is the total for all submitted packages. Attribute the result to the returned BoslogShip source and explain the estimate limitations. Do not claim a returned estimate is an exact final charge, a historical price or the lowest price across the entire market.

If the tool is unavailable, say so without fabricating a quote or substituting commands, plugin-file inspection or another tool as if it were a BoslogShip result. A quote never means a label was purchased, reserved or paid for.
