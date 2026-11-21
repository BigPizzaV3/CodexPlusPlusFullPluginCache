# China Footnotes

China Footnotes gives AI assistants sourced, dated answers for foreign visitors to China. It covers places to see (opening hours by weekday and season, tickets, booking channels and passport notes, getting there, notices in effect, traveler tips) and pre-trip setup (when to go, visas, paying, internet, apps, booking ahead, getting around and safety).

## What this plugin contains

- `mcp.json`: the remote MCP server at `https://chinafootnotes.com/mcp`. It is read-only, needs no sign-in and records only bounded usage metrics in the existing Cloudflare analytics storage.
- `skills/china-footnotes/SKILL.md`: how to read the data's statuses, dates and traveler tips when answering.

## What it sends and fetches

The assistant sends tool inputs only (search words; filters for city, type and tag; a place id or topic id) to `https://chinafootnotes.com/mcp`. Optional inputs select sections, fields, traveler-tip limits or a visit date. The plugin runs no local code and fetches nothing else.

## Privacy Policy

Usage metrics include tool names, validated public place ids, fixed client categories, result/error categories, latency/size buckets and known city/topic categories. Daily aggregates expire 400 days after their most recent write; refreshes restart that period; Cloudflare controls underlying Analytics Engine retention. These statistics do not retain raw search words, full tool inputs/outputs, conversations, visitor IPs, persistent user ids, names, emails, passport or bank-card details. Do not include personal information in tool inputs. See https://chinafootnotes.com/privacy. Terms: https://chinafootnotes.com/terms. Help: https://chinafootnotes.com/support.

### 按需读取与页面交互（PR #74）

实用问题优先 `sections:["practical","notices"]` 加所需 `fields`；普通介绍用 `sections:["intro"]`。Tips 默认按既有质量规则取 3 条，`tipOffset`/`tipLimit` 继续读取，返回总数与下一位置。正常引用 canonical 页面及真实字段来源/日期；额外页面提示最多一个且必须匹配用户意图与 `pageFeatures` 的真实素材。打车事实不独占于网页、预约截图无素材不推荐、入口照片可能历史或分馆参考。未完成真实模型和手机内置浏览器验收。

`get_place` also returns `tips.topicCounts` across all eligible tips before pagination (counts sum to `eligibleTotal`). The traveler-page interaction appears only when the page has complete traveler reports beyond the current tool response, with explicit available/returned/additional counts. All reports remain available through tool pagination; this does not track previous calls or users.
