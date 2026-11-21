# 站点、模板、节点与域名

## 项目列表与归档

用户说“项目列表”“有哪些站点”“查找某个站点”，默认只调用 `list_projects` 查询未归档站点。普通查询未命中时说明没有找到，不自动查询归档，也不把归档站点加入批量处理范围。

只有明确要求查看/查找归档站点，或恢复归档站点时才调用 `list_archived_projects`。恢复时用归档列表确认真实 `project_id`；有重名先澄清。仅查看不恢复；明确恢复请求后调用 `restore_site`，核对返回的 `archived_at=0`，再用普通列表确认目标重新出现。恢复需要后台管理员权限，只恢复列表可见性，不发布、部署或修改站点内容。

## 诊断与修复

先确认目标站点、症状和发生时机，用实际配置、发布、域名及内容状态定位问题。证据不足时标记尚未确认，避免同时修改多个无关配置。说明最小修复及影响，按已有授权执行；完成后重读状态，给出用户可以观察的验收结果。

## 建站与复制

1. 根据用户意图创建或复制；信息已明确时不重复询问。用 `list_site_templates` 或指定 ID 的 `get_site_template` 选择真实 `themes_id`。
2. 用 `list_integrations` 和 `list_integration_service_types` 核实所需集成。Cloudflare 用 `start_cloudflare_oauth` 返回的链接交给用户完成授权，再重读集成列表；不索取供应商凭证。
3. `verify_integration` 只用于类型目录声明 `verify_supported` 的集成，且会更新记录；未支持验证不等于已经验证成功。
4. 收集名称、语言、节点模式等当前工具要求的字段。共享节点用 `list_nodes` 取得真实 `node_uid` 并传 `independent:false`；独立节点按合同选择 Cloudflare/数据库集成。
5. 调用 `create_site`；复制先 `get_site_copy_context`，再 `copy_site`。复制若指定 config_lang，必须遵守源站语言合同。受理失败可能已创建项目，先查项目和节点状态，不能盲目重建。
6. 统计关联须来自用户选择的稳定统计项目标识，按 [site-insight.md](site-insight.md)；名称/域名相似和唯一候选都不替代选择。
7. 新站点取得真实 project_id 后才进行域名、内容和发布。源码/模板上传属于本地开发任务，不在此流程执行。

## 站点配置

`get_publish_readiness → get_site_schema + get_site → update_site → get_site`。

- schema 与当前详情是依据；只提交用户本次要求的 `app_config_patch`。其他发布任务持有锁时不保存。
- `ai_editable` 缺省为 true，显式 false 不可修改或清空；敏感字段只给 configured 状态，不能把掩码或空值写回。
- 对象递归合并，数组整体替换；改数组前读取完整现值，合并后提交完整数组。
- 清空顶层字段使用 `clear_fields`；不把 null、空字符串、掩码混作清空指令。
- 可翻译内容使用合同中的源语言 config_lang，不用用户对话语言或访客默认 now_lang 替代。保存后按 [translate-seo.md](translate-seo.md) 完成本土化与发布。
- 普通“修改配置”默认站点配置。用户明确点名模板业务才转 [business.md](business.md)。

## 友情链接

友情链接是站点配置中的 `friend_links`，不是推广资源。先读 schema 和原数组，按用户要求合并条目；保留其他链接。url/title 等字段以实时合同为准。

外链平台的 entry_url 是操作入口，indexed_url 才是外部成品地址；只有用户要求添加友链时才把成品地址写进站点配置。只登记外链建设不自动修改配置或发布。

## 域名与邮箱

已有站点域名：`list_site_domains → add_site_domain → add_domain_zone → get_domain_nameservers → refresh_domain_status → bind_domain_worker → set_site_main_domain`，按返回状态跳过已完成步骤。

需要注册商改 NS 时先让用户完成，或按 [registrar.md](registrar.md) 使用已支持的注册商工具。DNS 生效必须以刷新结果为准，不用等待时间推断成功。注册商域名 ID 与站点 domain_id 分开。

`enable_domain_email_routing` 配置收信路由，不证明发信服务就绪；反馈发送仍由服务端检查。

## 站点域名 DNS

已有站点域名优先走站点 DNS 工具：`list_site_domains` 取得真实 project_id + domain_id，确认已有 cf_zone_id 与 integration_id 后用 `list_site_domain_dns_records`。无需注册商库存，也不因为缺 registrar_domain_id 而重绑 CF、修改 NS 或索取新密钥。

- 查询每页 100 条；返回 has_more=true 时继续下一 page，不能把首页当作全部记录。name 只接受 @ 或本站域名下的完整名称。
- 用户要求新增解析或接入 GSC/Bing 时，按具体 DNS 材料执行 `create_site_domain_dns_record`；新增保留其他同名 TXT。验证记录使用 proxied=false。
- 修改先读取真实 record_id，再用 `update_site_domain_dns_record` 只传本次要改的字段；省略的 TTL、代理、priority、data、备注和标签保持原值。
- `delete_site_domain_dns_record` 只删除用户明确指定的已读取记录，不批量清空；写 DNS 要求 publish scope，既有 CF 授权仍由服务端检查。
- 新增/修改响应未知时先重查实际记录，再决定后续动作，不盲目重复提交。DNS 写入成功与外部站点验证成功分别核实。

CLI 脚本对应 `dami domain dns --domain-id <domain_id> --page 1`、`dami domain dns-create`、`dami domain dns-update`、`dami domain dns-delete`；当前项目通过全局 project_id 或已选择的项目注入。日常 AI 操作继续用 MCP。

## 程序升级与节点

`check_site_update` 会同步模板版本记录，需要 write 权限；`upgrade_site` 会触发节点升级。共享节点可能影响多个站点，先展示实际范围并遵守用户授权。

部署受理后用 `get_deployment_status` 查终态；配置推送继续走站点发布。不得以程序升级替代配置修改，也不在结果不明确时重复部署。
