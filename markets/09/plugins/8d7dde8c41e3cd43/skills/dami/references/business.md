# 模板业务配置

## 语义边界

- 用户只说“查看配置 / 修改配置”时，默认仍是站点配置：用 `get_site` / `get_site_schema` / `update_site`。
- 用户问“当前站点有什么可配置”时，先读取当前 `project_id` 的能力清单；清单包含站点配置分类和模板声明的业务能力。
- 用户明确点名业务后，必须先读取该业务的实时合同，再按合同执行读写。
- 反馈、推广、页面、定价等有独立命令面的领域，不转入模板业务合同。

## 不可破坏的不变量

1. 业务合同只对返回它的 `project_id + contract_template_id` 有效。切换项目后必须重新读取能力与合同。
2. 同名 business/action 在不同模板可以指向完全不同实现；禁止复用另一项目的说明、字段、路径或结果假设。
3. Agent 只能提交 `business + action + input`。内部 path/method 由总后台从当前模板实时合同解析，不得自行拼 HTTP。
4. 先读合同，再只提交合同允许且用户明确要求的字段；删除等破坏动作按合同标记向用户确认。
5. 业务名称、动作名称、状态值、字段限制和副作用说明全部以当前模板合同为准；不得在 Skill 中预设任何模板业务。

合同输入只使用轻量字段类型 `string/integer/number/boolean/array/object`；可声明 `required/nullable/enum/default/min/max/min_length/max_length/min_items/max_items/items/properties/description`。服务端拒绝合同外字段。

## MCP 工作流

```text
询问有什么可配置
  list_projects
  → list_configurable_features(project_id)

明确业务读写
  get_business_contract(project_id, business)
  → read_business_config(project_id, business, action, input)
  或 write_business_config(project_id, business, action, input)
```

`list_configurable_features` 不是每次站点配置修改的前置条件；未指定业务时继续走站点配置工具。

## 合同驱动的执行纪律

- 先使用能力清单定位当前项目实际声明的 business，再读取完整合同。
- 读取合同中的 business/action 描述、notes、字段 description、enum、default、destructive 和 confirmation；这些内容是当前模板的操作规则。
- 多步操作只能使用当前合同声明的 action，并按合同说明传递上一步结果；合同没有声明的动作不得自行推断。
- 写入前确认用户意图与合同输入一致；写入后只依据接口返回结果报告，不用其它模板的经验补全结果。
