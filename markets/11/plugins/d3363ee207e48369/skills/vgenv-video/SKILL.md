---
name: vgenv-video
description: Quote, create and manage paid asynchronous vgenv videos with browser OAuth and explicit user cost confirmation.
---

# vgenv

使用已连接的 vgenv 远程 MCP。用户先通过浏览器登录并选择 Project 和授权范围；不要要求用户在聊天中粘贴 API Key、支付密钥或 OAuth Token。

1. 收集模型、档位、提示词、时长、分辨率、比例及素材。创建复用 V2；明确选择 `prompt_optimization.mode` 为 `enhance` 或 `raw`。
2. 调用 `quote_video`，展示实际规格、币种和总价（微单位除以 1,000,000）。取得用户对本次费用的明确同意，不自行制定预算。
3. 调用 `create_video`，提交相同视频参数、报价的 `currency` 与 `price_catalog_version`、用户确认的 `max_amount_micros` 和稳定的 `idempotency_key`。该调用直接创建收费任务，不再跳转网站逐次批准。金额或价表不匹配时重新报价并确认；不得擅自提高费用上限。
4. 返回 Video ID 后立即告知用户。用 `get_video` / `list_videos` 查看进度；`preparing`、`queued` 可用 `cancel_video` 取消；成功后 `get_result` 返回短期下载链接，过期后重新查询。
5. `get_balance` 只显示项目可用与冻结余额。余额或权益不足时如实说明当前请求不可用，不提供充值、购买、升级或直接交易链接，不收集支付信息。

一次逻辑请求始终使用同一个幂等键，包括网络超时、错误和并发重试；不要因未收到响应而生成新键。`MCP_BUSY` 表示本次工具未开始或 OAuth 事务已回滚，但相同请求可能仍在另一调用中进行。按返回间隔重试原请求；其他错误也不能据此认定未扣费。

OAuth 的 `video:create` 权限允许受信任客户端直接创建收费任务；服务端只校验授权范围和费用上限，不能验证聊天中的人工确认。不得把 OAuth 授权解释为用户同意任意后续收费。用户可在vgenv网站 `/mcp/connections` 撤销授权，已接受任务继续执行。
