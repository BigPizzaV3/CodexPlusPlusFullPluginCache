# 本土化与发布

站点、页面、定价源稿由 Agent 按合同 config_lang 书写；Dami MCP 使用 Agent 身份，不能依赖后台替它直译。博客使用独立 revision/locale 流程，见 [blog.md](blog.md)。

## 固定流程

1. 修改前查 `get_publish_readiness`，再读取详情、合同并保存本次源稿。
2. `get_translation_status` 确认 scope：site、pricing 或 page:<id>。
3. `export_translation` 获取冻结源稿、逐语言增量清单与发布锁；保留 task ID，源稿冻结后不继续修改。
4. 只对 `incremental[lang].pending` 中的新增、改动或缺失字段做本土化。按目标市场调研当地表达，用 `get_keyword_ideas` 核对搜索词；不能把逐字翻译当最终稿。宿主缺少外部检索能力时如实说明依据限制，不捏造调研。
5. 只遍历 `target_langs` 逐语言 `import_translation`，`config` 可仅包含本语言 pending 路径的译文；缺失或空白译文会被拒绝，不以源文填空。未改字段由服务端保留，Agent 不重新改写。
6. 站点发布须检查 site + pricing 联合 readiness；页面查 page:<id> 状态及发布锁。ready=true 且无阻断后，按已有授权发布并查询任务终态。

已有语言层是否新鲜以 ready、needs_translation、required_langs 和当前任务为准，不使用旧 fresh 语义。纯复用语言由服务端自动收口，不会列入 `target_langs`；数组为空时不调用 import，直接核对 readiness。只有用户明确要求全量重译时才使用 export 的 force，它跳过旧译文复用；这不授权覆盖他人的锁。

## 增量导入合同

`incremental[lang]` 包含 `pending` 与 `reused_count`。pending 每项的 `path` 是字符串/数字组成的路径数组，`source` 是本次待译源文；`reused_count` 是服务端复用的字段数量。完整 `source` 只提供冻结上下文，`existing` 只供参考，不能把它们当作全量重写清单。

按 pending 路径构造稀疏 `config`，数组使用冻结 source 中的原索引，前面的未提交元素用 `null` 占位。例如路径 `["hero", "items", 2, "title"]` 对应：

```json
{"hero":{"items":[null,null,{"title":"目标语言标题"}]}}
```

不要压缩数组或自行移动路径。提交完整结构也不会改写未变字段；服务端忽略这些字段的提交，合并旧译文与本轮译文，并保留源稿中的数字、布尔、ID 和最终形状。

本次 pending 字段若是品牌名、产品名、型号或目标语言中拼写相同的单词（如德语 Video），确需与源文完全相同时，将完整路径（如 `hero.items[2].title`）列入 `keep_source_paths`。未声明的 pending 同文会被拒绝；不要把本应翻译的文案声明为保留。合法的旧未改字段 keep 声明没有效果，无需重复提交。

## 内容边界

翻译范围以 export 的逐语言 pending 为准，结合 source 与 hints 理解上下文；不自行读取敏感配置后过滤。所有语言准备完成后才统一提交目标层和源快照，单个语言 import 成功不代表整次翻译或发布完成。

保留产品事实，按当地表达调整标题、卖点和正文，避免关键词堆砌。标题建议 60 字以内、描述 160 字以内，合同中的实际限制优先。站点真实市场优先于语言到国家的默认映射。

平台葡语只支持 `pt-pt`（葡萄牙葡语），使用葡萄牙的拼写和用词；历史 `pt` 仅是输入别名，正式输出、文件名和导入参数统一写 `pt-pt`。不创建或导入 `pt-br` 及其他葡语变体，也不能把巴葡译文改名当作 `pt-pt`。只处理 export 的 `target_langs`，不得因为目标市场是巴西而自行新增语种；发现历史葡语配置与本规则冲突时，先报告并修正语言配置，再重新 export。

## 排查历史译文

先调用 `inspect_translations`，用 `scope=all` 看站点、当前定价策略及各页面的语种统计，再指定 scope、langs 查看明细。只返回当前 schema 的可译字段；单次最多 500 行，`truncated=true` 时使用 path_prefix 分段，数组路径形如 `hero.items[0].title`。

`ok` 表示原文未变且有译文；`missing` 表示缺译文；`stale` 表示原文改过；`same_as_source` 仅提示同文，品牌等可合法保留。语义是否准确需要结合站点事实和当地表达判断，不能仅凭状态判断翻译质量。

历史 CLI 脚本对应 `dami i18n inspect --scope site --lang ja,fr --path hero --issues`；AI 运营仍优先 MCP。

## 定点修正

1. inspect 确认当前 path、source 和目标语种内容，保留原文精确值。
2. 调用 `patch_translation`，一次只传一个目标语种及需要改动的 items（path/source/text）。同文品牌等必须列入 keep_source_paths；stale 字段走正常 export/import，不用 patch 覆盖。
3. `publish_required=true` 只表示已保存。站点/定价查联合 readiness；页面先读页面详情，确认是否还有草稿或语种待发布标记，并告知用户发布会把页面草稿一起上线。
4. 按当前已有授权调用 publish_site / publish_page，并查询原任务终态。未改源文的修正会在后续增量翻译中复用；不使用 force，不重写其他语种。

历史 CLI 脚本对应 `dami i18n patch --scope site --lang ja --items items.json --keep hero.brand`，items.json 根节点为数组。没有返回成功时先重读 inspect，不盲目重放写入。

## 语种变更

保存语言配置后读取 `language_change`：added/removed 是公开语种差异，pages_queued 是已入队页数，pages_need_manual_publish 列出首页和有草稿的页面，并返回 reason。只有无草稿的已发布普通页面会自动补译/重推，且仅推该页面，不推送站点或定价草稿。自动任务只补登记的新增语种；源快照变化或旧语种需要重翻时保留标记，转为手动处理。首页依赖整站配置，须按已有发布授权手动发布。删除的目标语言层会被移除，以后再添加会重新翻译。

配置语言切换使用完整译层互换，不清空翻译。目标语种须已存在且所有 scope 译文齐全，源稿及目标译文先发布；有未发布可译改动会拒绝。返回 inactive_pricing_strategy_ids 的非启用策略仍保留原语言，启用前需人工处理。博客不在此流程内。

## 异常处理

- import 冲突或源稿变化：读取状态并重新 export，不拿旧任务继续覆盖。
- blocked=true / publish_operation.can_continue=false：等待锁持有者完成，不重复保存、发布或换身份。
- 语言只完成一部分：不能发布，报告剩余 required_langs / pending_langs。
- 发布已受理但响应丢失：查原项目/页面状态，不能再次发起同一操作。
