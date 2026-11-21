# 页面管理

## 读取与最小修改

先确认 project_id，使用 `list_pages`、`get_page`、`get_page_schema` 获取实际页面类型、合同与现值。字段说明、枚举、必填、value_schema 以实时 schema 为准；不要读取仓库示例当业务合同。

创建与更新统一用 `save_page`，按工具合同提供新页面类型或现有页面 id。创建前检查 slug 冲突；更新先读取完整现值，只改变本次明确字段，再提交完整 page_config 和应保留的元数据。save_page 是覆盖保存，省略元数据可能应用默认值。服务端负责最终校验，不假设宿主存在本地 validate 命令。复杂字段说明用 `get_page_type_doc`，规则见 [field-contract-rules.md](field-contract-rules.md)。

修改前查 `get_publish_readiness`；他人冻结源稿时停止。保存、本土化和发布是不同阶段。

## 页面元数据与链接

- is_home 表示首页路由；is_index 表示允许搜索引擎收录；in_sitemap 表示进入 sitemap。三个字段不能混用，默认值读取当前合同。
- note 记录页面用途，不把本次变更说明塞进页面身份字段。
- 导航引用页面前先读取真实 slug；外部地址使用完整 URL。只有模板合同支持时才能使用 modal:feedback 等特殊值。
- 新增或设置首页会影响原首页，须在用户意图范围内。

## 语言与 SEO

可翻译字段用 content_language_contract.source_language / config_lang；now_lang 是访客默认语言。一个源字段不混写双语，中文对话不自动改变录入语言。

SEO 标题建议不超过 60 个 Unicode 字符，描述建议不超过 160；实际硬上限读取合同。中文视觉宽度较大，保持简短。正文中的产品能力、价格、数据均需有实际依据。

## 自由组合区块

先读取当前 content_blocks 与合同的 editor_patch。匹配键、合并/替换/删除语义使用合同声明，不猜按数组下标或固定 id 合并。保留用户未要求修改的区块、模型配置和嵌套字段。

模型 ID 只从当前项目的 value_schema enum / available_models 选择；同名模型在不同模板可能使用不同 ID。缺少字段结构时读取类型文档，仍不明确则停止该字段修改。

## 发布

保存源稿 → 按 [translate-seo.md](translate-seo.md) 对 page:<id> export/import → 检查对应翻译状态与发布锁 → 在授权范围内 `publish_page` → `get_page_publish_status`。

不能用站点发布冒充单页发布，也不能把保存成功或任务受理说成已上线。素材先按 [media-library.md](media-library.md) 上传并登记。
