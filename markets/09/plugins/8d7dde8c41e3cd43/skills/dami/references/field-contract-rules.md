# 字段合同

字段和类型的权威源是当前项目返回的 `get_site_schema` / `get_page_schema`，以及模板业务的 `get_business_contract`。本文件只解释如何消费合同，不复制模板类型表。

## 取值规则

- 使用字段实际 name、type、required、nullable、enum、min/max、长度、数组数量与 value_schema。
- 复杂对象依据 properties、required、additionalProperties 等规则；不从字段名猜结构。
- 没有 value_schema 时用 `get_page_type_doc` 获取该类型说明。仍无法确定时停止该字段写入，不套用其他模板结构。
- example_content 仅帮助理解，不能当成生产事实；default 也不能用来覆盖已有值。
- ai_editable 缺省 true，显式 false 禁止 Agent 修改/清空。sensitive 字段不回显明文，不回填掩码。
- 配置的录入语言来自 content_language_contract.source_language / config_lang；可翻译与不可翻译字段分开。

## 结构与补丁

站点 app_config_patch 对象递归合并、数组整体替换。清空顶层字段使用 clear_fields；以实际工具合同为准，不把 null 普遍解释成删除。

页面 content_blocks 使用页面合同的 editor_patch 匹配键与语义。编辑前读取完整原值；修改单块不覆盖其他块。类型改变、删除、排序都必须有本次用户意图。

导航、引用和动态选择字段先查询其真实目标。primary_category 是分类页 slug，不能恢复已经退役的 group_id 关系；动态 options/枚举以当前合同为准。

## 模型与功能枚举

AI 输入区块的模型枚举由当前模板 catalog 注入。合法写值来自 value_schema 中的 enum，available_models 提供展示名称；不同模板 ID 即使名称相同也不可互换。

选择模型后继续读取该模型可用分辨率、时长、数量、功能和默认值。不能因展示名类似就继承另一模型参数。

## 校验与输出

MCP 写工具会复用后台校验。保存前按合同构造最小合法输入，遇错误定位到具体字段，不通过换接口跳过校验。保存后回读验证用户要求的变化，并区分已保存与已发布。
