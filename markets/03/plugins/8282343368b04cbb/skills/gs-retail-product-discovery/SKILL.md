---
name: gs-retail-product-discovery
description: Search the GS Retail product catalog by product name, category, or promotion and guide users from service selection to product results. Use when a user wants to find products or promotions available through the supported GS Retail service channels. Do not use for store locations, product-detail lookup, orders, reservations, carts, or payments.
---

# GS Retail Product Discovery

Use the MCP tools to provide a short, widget-led product discovery flow.

## Choose the tool

- If the user names `GS25`, `GSTHEFRESH`, `WINE25`, or requests all services, call `list_products` with that service code.
- If the user wants a product or promotion but does not name a service channel, call `select_service` first.
- After the user selects a service, continue with `list_products` using the original product intent and the selected service code.
- Do not ask for a service in plain text when `select_service` can render the service-selection widget.

Map user-facing service names to the exact tool code when they clearly refer to a service channel:

| User expression | Service code |
| --- | --- |
| `GS25`, `편의점` | `GS25` |
| `GS더프레시`, `더프레시`, `슈퍼`, `수퍼` | `GSTHEFRESH` |
| `와인25+`, `와인25플러스`, `WINE25` | `WINE25` |
| `전체`, `모두`, `모든 서비스` | `ALL` |

## Prepare the query

- Keep the product name, category, and promotion terms needed by the catalog search.
- Remove conversational filler such as `찾아줘`, `보여줘`, `추천해줘`, `오늘`, and `지금` when it does not change the requested product intent.
- Preserve promotion expressions such as `1+1`, `2+1`, `3+1`, `덤증정`, `gspay`, `pop할인`, `다다익선`, `묶음할인`, and `콤보`.
- Normalize `GS Pay`, `GS페이`, and case variants to `gspay`; normalize `POP 할인` and `팝할인` to `pop할인`.
- Do not invent a service code or product constraint that the user did not request.

## Present results

- Prefer the message returned by the tool and keep any accompanying assistant text brief.
- When a widget is rendered, do not repeat product counts, service counts, or the complete results as a plain-text table.
- Do not refer to the widget with positional wording such as `아래`, `하단`, `above`, `below`, or `following`.
- If `searchKeywordStatus` indicates that a replacement or fallback keyword was used, preserve the tool's disclosure that a different keyword was searched.
- Treat an empty result and a temporary search failure differently; use the message returned by the tool for each case.

## Boundaries

- Do not claim that a product is in stock unless the tool explicitly returns stock information.
- Do not promise product details because no product-detail tool is available.
- Do not place orders, reserve products, add items to a cart, or initiate payment.
- Do not use this workflow for store-location requests or unrelated general questions.
- Do not call the product-search tools for account changes, payment data, delivery or pickup operations, inventory checks, medical claims, restricted-goods circumvention, competitor searches, internal company data, security bypasses, or requests involving another person's data.
- When evaluating an ambiguous or negative request, use [negative examples](references/negative-examples.md) to identify unsupported intent. Do not treat the examples as capabilities.

## Examples

```text
User: 우유 찾아줘
Tool: select_service({ "query": "우유" })
```

```text
User: GS25 1+1 음료 보여줘
Tool: list_products({ "query": "1+1 음료", "service": "GS25" })
```

```text
User: 모든 서비스에서 과자 찾아줘
Tool: list_products({ "query": "과자", "service": "ALL" })
```

```text
User: GS더프레시에서 계란 찾아줘
Tool: list_products({ "query": "계란", "service": "GSTHEFRESH" })
```

```text
User: 강남역 근처 GS25 찾아줘
Action: Do not call the product-search tools because this is a store-location request.
```
