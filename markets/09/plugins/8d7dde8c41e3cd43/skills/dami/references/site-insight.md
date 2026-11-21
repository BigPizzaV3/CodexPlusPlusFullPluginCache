# 统计数据

总后台保存 GA Lite 账号连接，GA4/GSC/Bing 凭据留在统计服务。站点使用总后台 project_id；统计项目使用稳定 statistics_project_key，不能用域名、名称或 G-XXXX 代替。

## 连接与已有项目

`get_analytics_connection` 为 active 时复用；connection_required/reauth_required 时 `connect_analytics`，把短时授权链接交给用户完成，再重读状态。打开链接不等于连接成功。

`list_analytics_projects` 可按已有 project_id、新站 site_name 或 query 查询候选。名称/域名匹配只用于推荐，即使唯一也要确认用户选择。用选定 integration_id + statistics_project_key 调用 `bind_analytics_project`；`unbind_analytics_project` 只解除站点关联，不删除远端项目。

## 新建统计项目

1. 先创建站点取得 project_id，并设置真实主域名。服务端固定使用站点名称和主域名，不猜 URL。
2. `list_analytics_data_sources` 取得 account_ref；缺 provider 账号时交给用户完成 connect_urls 对应授权。
3. GA4 是创建必选项；GSC/Bing 仅在用户要求时启用，选定实际账号。
4. `create_analytics_project` 先不传 confirmed=true，取得 preview；展示目标、账号、动作、DNS 材料和影响。
5. 用户确认后用同一业务参数、confirmation_token 与稳定 idempotency_key 执行。参数变化重新 preview，同一次重试保持原 key。
6. 成功时服务端绑定统计项目并推送 GA4 配置；config_push=failed 只恢复推送，不重复创建或再次 bind。

## 搜索验证与数据

1. `get_analytics_project` 读取已有项目和 pending 材料；缺 GSC/Bing 时继续使用原统计项目，不能重新创建 GA4。
2. `list_analytics_data_sources` 选定 account_ref。GSC 的 can_read/can_manage_sites/can_verify_site 和 missing_scopes 来自 Google 实际授予的 scope；capability_source=granted_scopes 不证明 API 已启用或调用成功。缺权限时使用受控 authorization_url 升级并重读账号。
3. 首次 prepare 失败、已有项目缺 provider、完成扩展授权或启用 Google API 后，用 `prepare_analytics_setup` 预览并按已授权意图确认执行。同一项目/账号的 pending 返回原记录，已有资源返回 attached，不能把预览成功当作 Google 调用成功。
4. attached 无需再验证；verification_required 时配置返回的完整 DNS type/name/value，确认公网可查询后再 `complete_analytics_setup`。仍须 preview → 同参数/token/key 确认执行；integration_prepare_required 表示必须先 prepare，不能重复 complete。
5. 查询项目确认挂载 active，再 `refresh_analytics_link`。GA4/Bing 已成功时只恢复缺失 provider，统计项目标识和其他资源保持不变。

超时或结果未知时用 `get_analytics_operation`，传原连接的 integration_id 和 operation_id 查询最新账本；该工具需要账号管理员权限。running/unknown 不能换 key 盲目重试；unknown 还需核实 Google 远端状态，账本查询本身不代表远端已核实。相同 key 只回放原结果。已明确 failed 且修复 scope/API/DNS 后，新的 prepare 或 complete 尝试须重新预览并使用新的操作 key；这与未知结果重试不同。

配置验证记录先 `list_site_domains → list_site_domain_dns_records`，按已授权站点的 DNS 材料使用 `create_site_domain_dns_record`；只有实际已有记录需修改时才按 record_id 使用 `update_site_domain_dns_record`。保留已有 SPF、邮件及其他验证记录，不因缺注册商库存而阻断。

GSC active 只表示接入完成，不表示 Sitemap 已提交或页面已收录。Sitemap 用正式工具，不通过只读 raw proxy 写入，也不自动切换浏览器执行。

指标用 `get_analytics_metrics`，默认 overview / 7days；按需查询 timeseries、dimension、realtime、search/*。可传 metric、data_state、type、分页排序、自定义日期与 filters JSON。输出注明 provider、实际可用周期、抓取时间、缓存和分项错误；pending、partial、连接失效与数据缺失不能报告为真实零值。

## GSC 索引、Sitemap 与 SEO

- `inspect_analytics_urls`：同一绑定项目检查 1–10 个页面；检查失败单独报告，不能写成“未收录”。只查询 Google 已知索引版本，不执行实时测试或请求编入索引。
- `get_analytics_sitemaps`：列出提交；sitemap_index 列子项，sitemap_url 查详情。submitted 是提交数量，不是已索引数量。
- `submit_analytics_sitemap` / `delete_analytics_sitemap`：先预览；用户确认同一计划后，使用 confirmed=true、confirmation_token、稳定 idempotency_key 执行。移除 Sitemap 不移除已索引页面，提交也不保证收录。gsc_write_scope_required 时把 authorization_url 交给用户完成权限升级，不能把只读授权描述为写权限。
- `compare_analytics_periods`：当前绝对日期与可选 previous 日期；缺省等长前周期。排名正变化表示改善，零基数变化百分比为 null；样本缺行不证明关键词真实新增或流失。
- `get_analytics_content_opportunities`：高曝光、低 CTR、指定位置的 query/page 候选；潜在点击仅是假设目标 CTR 的估算。
- `get_analytics_cannibalization`：同词多页面候选，结合页面内容和搜索意图判断，不自动合并、加 canonical 或重定向。
- `get_analytics_seo_report`：指标与周期变化、下降词、趋势、内容机会、竞争候选。

项目含多个 GSC resource 时，使用返回的 resource_id 明确选择。分析 filters 使用原生 `{dimension,operator,expression}` 数组；max_rows 默认 25000、最多 100000。输出必须保留 coverage/truncated 和 freshness；API 头部样本不是网站全量，截断后不能称“全部关键词”。不接入 Service Account。

expression 的首尾空格与正则按原文传递。Sitemap 失败与失败回放都返回错误，保留 operation_id/state；idempotent_replay 只表示回放，不表示成功。remote_operation_in_progress 表示同一 key 正在执行，保留返回的操作编号，不更换 key 重复提交。overview 可返回部分数据与 errors，不能把分项错误描述为全部正常。

CLI 等价入口为 `dami analytics gsc <operation> --project-id ... --input JSON`，operation 为 inspect、sitemaps、sitemap-submit、sitemap-delete、compare、opportunities、cannibalization、report。Sitemap 写操作还需显式 --confirm、--confirmation-token、--idempotency-key；结果不明先核实远端状态，不更换 key 盲目重试。

## 错误

connection_required/reauth_required 处理原连接；provider_account_selection_required 展示账号候选；site_main_domain_required 先处理主域名；confirmation_required 重新 preview；idempotency_conflict 停止混用请求；远端项目缺失或服务不可达如实报告，不重复创建。

保留 request_id 用于排查，不把 token、confirmation token、API Key 写进日志或长期文档。

GSC 接入错误保留 provider、phase、step、api、reason、upstream_http_status、operation_id、retryable、next_action。gsc_api_disabled / SERVICE_DISABLED / accessNotConfigured 检查 Galite 实际 OAuth Client 所属 Google Cloud 项目的对应 API；gsc_scope_insufficient 根据 missing_scopes 重新授权；gsc_dns_verification_failed 核对 DNS；token_invalid/reauth_required 是 Google 账号凭据问题，不直接撤销总后台 Partner 连接。普通权限拒绝仍需根据安全 reason 定位，不能一律解释为缺 scope。

当前客户端未取得 prepare_analytics_setup 或 get_analytics_operation 时，明确报告工具尚未加载，等待服务端部署并按宿主方式刷新连接定义；更新 Skill 不会自动产生新工具，不切换私有 API/CLI 绕过缺口。
