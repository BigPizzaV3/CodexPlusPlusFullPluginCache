# 注册商域名与 DNS

当前服务端支持 Spaceship 与 Dynadot，调用前仍用 `list_integration_service_types` / `list_integrations` 读取实际类型和已配置集成。不索取供应商 API Key；缺集成由用户在后台设置。

## 购买

1. `search_registrar_domains` 查询实际可注册性，最多 20 个域名；国际化域名使用 Punycode。
2. estimate.indicative=true 是参考价，不是最终报价或金额上限。普通域名与 premium 分开；当前购买工具不购买 premium。有严格预算时在注册商确认最终价格再下单。
3. `list_registrar_contacts` 选择已有 contact_id；Spaceship 必填，Dynadot 可用账号默认联系人。没有联系人时交由用户配置，不编造个人资料。
4. 用户授权须覆盖域名、注册商、年限、价格性质和续费策略。Spaceship 请求关闭自动续费；Dynadot 沿用注册商默认策略，不能根据本地初始字段推断已关闭。
5. `purchase_registrar_domain` 必须带 confirm=true 与 accept_price_variation=true。已有明确授权不重复询问。
6. 用 `get_domain_purchase_status` 核实到 registered。响应丢失先 `list_registrar_domains` 查记录；pending/unknown 不重购。无订单号时核对注册商或同步真实库存，错误文案不证明没有扣款。
7. 卡住且已核实未注册、原订单不会继续执行时，才按用户清理授权调用 `delete_unfinished_domain_purchase_record`。此操作删除后台记录并释放占位，不撤销外部订单、不退款。删除后重新查询价格与可用性，不自动连带重购。

## 已有域名与接入

已有域名从 `sync_registrar_domains` 开始，不能再次购买。同步更新注册商事实，保留已有 CF/站点关联；软删记录恢复时需重新核对绑定。

选择目标节点对应的 Cloudflare 集成，调用 `connect_registrar_domain_to_cloudflare`。它会创建/关联 Zone、修改注册商 NS 和 SSL/AI 爬虫设置，先核对影响。返回 ns_synced/ns_error/provision 可能部分成功，不能把接入当成已激活。

`bind_registrar_domain_to_site` 返回站点 domain_id；再 `refresh_domain_status → bind_domain_worker`，主域名用 `set_site_main_domain` 按授权单独设置。registrar_domain_id 与 domain_id 不可混用。

## DNS 与能力边界

已有站点域名的 DNS 使用 [site.md](site.md) 的 project_id + domain_id 工具，不要求注册商库存；不要为操作站点 DNS 额外同步、注册域名或重新接入 CF。

`list_domain_dns_records` 先读取现状，`upsert_domain_dns_record` / `delete_domain_dns_record` 只处理用户指定记录。不能批量清空其他服务的解析。

这三个旧入口只接受真实 registrar_domain_id。旧 upsert 不传 record_id 时可能覆盖同 type+name 的首条记录；有同名 TXT 时不能用它新增验证值，优先使用站点 DNS 的明确新增入口。

续费、自动续费、联系人写入是否可执行，以当前宿主发现的实际工具为准。缺工具时报告具体缺项并由用户使用后台/注册商界面，不自动回退命令行，也不编造工具。

Dynadot 请求串行处理；provider 差异交给服务端，不在 Skill 中重建供应商 API。
