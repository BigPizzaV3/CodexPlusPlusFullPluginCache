---
name: get-started
description: Set up 3DMockups after installing it. Checks the connected account and shows what you can make.
---

1. Call `get_account`. Tell the user which 3DMockups account is connected, whether it has 3DMockups Premium and the URL of their store. If the account has no store username yet, say they can set it on the 3DMockups website or app before publishing.
2. Call `list_garments` and show, in one short line each, the garments with `agent_supported = true`. Point out the ones with `free = true`: they work without 3DMockups Premium.
3. Explain in two or three sentences what you can do together: create print-ready designs with AI (uses the AI credits of their plan), show them on real 3D garments, save them in My designs to edit later on the web or iPhone app, and publish them as products in their store.
4. Ask what they would like to make first and offer one concrete example, such as "a retro coffee club tee in 3D".

Before calling `create_product`, always confirm the title, price and whether it should be visible in the store or a hidden draft. Never publish without that confirmation.
