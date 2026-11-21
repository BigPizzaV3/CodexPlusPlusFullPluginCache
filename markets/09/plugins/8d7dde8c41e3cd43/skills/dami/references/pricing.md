# 定价与支付

`get_pricing` 返回 pricing_editor 合同与当前 bundle，包括 strategies、price_page 和 payment_capabilities。以统一合同编辑，使用 `save_pricing` 原子保存，不拆成定价、支付选项、FAQ 多次写入。

## 操作流程

1. 确认 project_id，读取 `get_publish_readiness` 与 `get_pricing`。存在他人发布锁时停止。
2. 调价默认复制当前 active 成为新策略，保留原策略与历史；新副本先不激活。用户明确要求直接修改当前策略或同时切换生效时按其授权执行。
3. 新价格 ID 不凭空生成，由当前合同/服务端分配。周期、档位、币种、比例和必填项按合同填写。
4. 保存前依据合同检查完整结构；服务端仍执行最终校验。没有 MCP validate 工具时，不声称做过本地校验。
5. 保存后按 [translate-seo.md](translate-seo.md) 处理 pricing 语言层；联合 readiness 必须检查 site + pricing，最后在授权范围内 `publish_site` 并查询状态。

## 覆盖语义

- strategies 是完整最终数组，遗漏历史策略会使其归档。先读全量，在现值上合并，不能只提交新增一条。
- price_faq.detail 同样是最终数组；保留未修改的问题。
- source_language / config_lang 决定策略展示内容、档位名、特性和 FAQ 源稿语言；不要跟随对话语言改源语。
- payment_options 使用实时 providers 的 available、allowed_subscription_modes、allowed_onetime_modes、disabled_reason。不能假设某商户或支付模式可用。
- available=false 时解释服务端原因，不启用该 provider。发现历史无效选项应说明其阻断影响，按用户修复范围处理，不能暗中改其他支付配置。
- 保存不等于发布，不自动购买、收费或切换未经授权的生效策略。

读取版本或发布锁发生变化时重新读取合同与 bundle；不要用旧数组覆盖并发改动。
