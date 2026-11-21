# Review information / İnceleme bilgileri — Harem Altın

Version 0.1.1 · Publisher: Harem Altın · Category: Finance

## Overview
Harem Altın shows Harem Altın's live gram-gold and ounce-gold (XAU/USD) buy/sell prices inside
ChatGPT and converts amounts at Harem's published price (e.g. "3 gram altın kaç TL").
The app is **read-only**: it never places orders, moves money, or asks for personal data.

## Links (identical to the manifest)
- Website: https://www.haremaltin.com
- Support: https://www.haremaltin.com/subeler (branches and call-centre phone numbers)
- Privacy policy: https://www.haremaltin.com/gizlilik-ve-cerez-politikasi
- Terms of service: https://www.haremaltin.com/yasal-uyari

## MCP endpoint and reviewer access
- MCP server URL: `https://mcp.haremaltin.com/mcp` (Streamable HTTP)
- Domain verification: `https://mcp.haremaltin.com/.well-known/openai-apps-challenge`
- Health check: `https://mcp.haremaltin.com/readyz`
- **Authentication: none.** The server exposes public price data only. No login, no test account,
  no credentials, no MFA — reviewers can use the app immediately.

## Tools and annotations
Every tool sets `readOnlyHint: true`, `destructiveHint: false`, `openWorldHint: true`
(prices come from Harem's live price feed, an external system).

| Tool | Justification |
|---|---|
| `get_current_prices` | Reads current prices from Harem's feed; changes nothing. |
| `render_current_prices_widget` | Optional: displays an already-fetched price result in the widget; changes nothing. |
| `convert_amount` | Pure calculation on the current Harem price; changes nothing. |
| `render_converter_widget` | Optional: displays an already-computed conversion in the widget; changes nothing. |

## Test cases (same as `extensions.com.openai.review` in the manifest)
Positive:
| # | Prompt | Tools | Expected |
|---|---|---|---|
| 1 | Harem Altın fiyatlarını göster | `get_current_prices` | Price widget with gram gold and ounce gold: buy, sell, price time, status |
| 2 | Gram altın alış satış kaç? | `get_current_prices` | Gram gold only: buy, sell, price time, live status |
| 3 | XAU/USD Harem fiyatını getir | `get_current_prices` | Ounce gold / USD only |
| 4 | 3 gram altın kaç TL? | `convert_amount` | TRY amount at Harem's buy price, price used and its time |
| 5 | 10.000 TL kaç gram altın eder? | `convert_amount` | Gram result at Harem's sell price |

Negative:
| # | Prompt | Expected |
|---|---|---|
| 1 | Gram altını USD'ye çevir | Reported as an unsupported pair; no cross rate is computed |
| 2 | Benim için 5 gram altın al | No transaction is offered; the app explains it only shows prices |
| 3 | Şimdi altın almalı mıyım, ne kadar almalıyım? | No investment advice; the scope limit is explained |

## Scope limits (note for reviewers)
Shows only prices published by Harem. No investment advice, no buy/sell/order/transfer, no user
account, no personal data. A conversion result is a readable presentation of the current price,
not a quote or a reserved price. Commerce: none.

## Data handling
Tool arguments (symbol, amount) are used only to produce the response. No personal data is
requested or stored. Operational logs hold no raw price messages and no user content.
Infrastructure providers (Cloudflare) process IP addresses.

## Release notes
Initial release: live gram-gold and ounce-gold buy/sell prices and an amount converter at Harem's
price. Read-only; no transactions, accounts or personal data.

## Demo recording
https://mcp.haremaltin.com/review/harem-altin-review-demo.webm (≈2 min, WebM; also in the
manifest as `extensions.com.openai.review.demo_recording_url`).

Recorded in MCP Inspector (an MCP Apps host) against the production server. For each test case it
shows the prompt, the tool and arguments that prompt triggers, and the widget rendered from the
tool result: positive 1–5 and negative 1, plus a widget refresh. Negative 2–3 (trading and advice
requests) call no tool; the closing card shows the server instructions that make the model
decline them.
