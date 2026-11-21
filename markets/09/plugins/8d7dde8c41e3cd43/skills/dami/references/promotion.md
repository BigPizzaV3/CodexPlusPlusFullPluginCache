# 外链管理与站外推广 (`promotion`)

`#/backlink-manage` 管理可以建设外链的外部平台。使用已连接的大米 MCP，缺少能力时先完成宿主发现流程。

## 术语与字段边界

| 对象 | 含义 | 入口与字段 |
| --- | --- | --- |
| 外链资源 / 推广渠道 | 可发布产品介绍、文章或资料页的外部平台 | MCP 推广资源工具；`entry_url` 是操作入口，`note` 是资源公共备注 |
| 站点外链建设记录 | 某个产品站点在某条外链上的执行结果 | MCP 建设记录工具；`project_id + channel_id` 唯一，`note` 是该站点建设备注 |
| 发布所得外部链接 | 产品介绍发布后取得的外部成品页面 URL | 建设记录 `indexed_url`；字段沿用历史命名，不代表搜索引擎已经收录 |
| 友情链接 / 友链 / 页脚链接 | 本站展示、供搜索引擎发现的链接配置 | `site.md` 的站点 schema + 最小 patch，不属于推广资源 |

典型链路：**外链管理找平台 → 发布产品介绍 → 取得成品 URL → 标记该站点建设记录 → 用户明确要求时将成品 URL 放入站点友情链接**。

“收录某个外链”在外链管理语境中表示把外部平台收入资源库，不表示添加友情链接，也不表示向搜索引擎提交收录。上下文明确包含“收录渠道并放到友情链接”时，分别执行两个对象的操作；仅要求收录或标记建设记录时，不改站点配置。

## 操作前发现能力

- 使用宿主发现的工具输入合同；用 `list_projects` 确认目标项目。缺工具不通过其他通道绕过。
- 修改前读取对应详情，只提交本次修改字段。资源公共备注与站点建设备注不能混用。
- 写入超时或结果未知时先查现状，不盲目重复创建或标记；`mark` 没有请求回放键，并发重复调用也只保留一条站点/渠道记录。

## 合法值与写入语义

| 字段 | 合法值 |
| --- | --- |
| 资源状态 | `newly_collected`, `approved`, `expired` |
| 评级 | `high`, `medium`, `low`, `deprecated` |
| 验证码 | `none`, `cf_turnstile`, `recaptchav2`, `recaptchav3`, `hcaptcha` |
| 平台类型 | `post_product`, `post_article`, `profile_page`, `post_video`, `post_audio`, `post_image`, `post_package`, `post_slides`, `post_token`, `post_thread`, `post_comment`, `other` |
| 建设状态 | `pending`, `success`, `failed` |
| 操作模式 | `assist`, `auto` |
| 竞品状态 | `newly_collected`, `active`, `offline` |

建设状态与资源可用状态是两套独立枚举。一个资源对站点 A 可以成功，对站点 B 可以失败。

- `mark` 按站点 + 渠道创建或更新，不要求知道建设记录 ID；至少提供状态、备注、URL 等一个建设字段。
- `mark` / `update` 只修改明确传入字段：省略保持原值，`note: ""` / `indexed_url: ""` 明确清空。不带状态创建时默认 `pending`，不带模式创建时默认 `assist`。
- 备注最长 2000 字符，锚文本最长 500，URL 最长 1000；时间是非负 Unix 秒数。
- 删除资源级联删除关联建设记录；删除建设记录保留资源。
- 记录与渠道汇总同事务保存。`submit_count` 是现存建设记录数，`success_count` 是当前成功记录数，`last_submit_at` 是现存记录的最大时间；重复标记、成功改失败和删除不会累计错误计数。
- 查询及写入必须满足账号和站点权限；不支持通过传入其他站点 ID 跨范围操作。

## MCP 工作流

以下按意图示例说明，实际可用能力始终以当前 `tools/list` 为准。

| 意图 | 工作流 |
| --- | --- |
| 收录一个外部平台 | `check_promotion_resources` 查域名 → `list_promotion_resources` 核对具体入口 → `create_promotion_resource` |
| 查询 / 编辑 / 删除渠道 | `list_promotion_resources` / `get_promotion_resource` → `update_promotion_resource` / `delete_promotion_resource` |
| 标记某站点建设状态或备注 | `list_promotion_submissions` 按站点与渠道读取 → `mark_promotion_submission` |
| 按记录 ID 修改或删除 | `get_promotion_submission` → `update_promotion_submission` / `delete_promotion_submission` |
| 查找待建设平台 | `list_unsubmitted_promotion_resources`；按资源评级、价格和建设状态组合筛选用 `list_promotion_resources` |

标记示例（JSON 是工具参数，不是 HTTP payload）：

```json
{
  "project_id": "confirmed-project-id",
  "channel_id": 123,
  "status": "success",
  "indexed_url": "https://example.com/products/your-product",
  "note": "产品介绍已发布，等待审核"
}
```

只改站点建设备注时只传 `project_id`、`channel_id`、`note`，不要填写默认状态或空 URL。资源 `entry_url` 由适配层映射历史 `resource_url`，`channel_id` 映射历史 `resource_id`；调用方只使用公开字段。

## 友情链接接续

只有用户要求把已发布链接添加到本站友情链接时才继续：加载 `site.md`，读取站点详情与实时 schema，确认 `friend_links` 字段及已有列表，按合同把成品 URL 合并到最小 patch。不得把操作入口当成成品链接，不得覆盖已有友链，不自动发布站点。

## 人工发布边界

外部渠道由运营人工提交并核实，再用 `mark_promotion_submission` 标记；插件仅辅助生成和填写。已移除全自动批量发布、support_full_auto 和未建设渠道的自动模式筛选。DR 仅保留人工录入与导入，不再调用失效的 Ahrefs DR 同步接口。
