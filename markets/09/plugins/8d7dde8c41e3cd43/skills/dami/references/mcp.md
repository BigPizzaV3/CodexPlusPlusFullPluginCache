# MCP 连接与执行

## 宿主接入

同一个远程 MCP 服务面向桌面客户端、ChatGPT/Work 和内置 Agent。OAuth 由支持它的宿主处理；支持自定义认证头的客户端可由用户在连接设置中配置 Agent Key。内置 Agent 的凭据由后台服务端提供。Skill 和 UI 不保存凭据。

能力真相来自当前连接的 `tools/list`；该协议方法不一定作为模型工具暴露。宿主有工具搜索时按业务词和具体工具名搜索，接受宿主添加的命名空间。完成发现仍缺工具时报告当前会话缺失，按宿主规则刷新连接与缓存；不把未加载误判为后台未实现。

只通过已连接的 MCP 执行运营动作。Shell、任意 HTTP 请求或直接数据库操作不作为运营回退；需要本地开发时使用单独的开发套件。

## 项目、权限与错误

- 单站任务用 `list_projects` 从未归档站点中选择真实 `project_id`；普通查询不追加归档检索。明确查看/恢复归档时使用 `list_archived_projects`，恢复规则见 [site.md](site.md)。账号级关键词收藏、注册商库存和跨站反馈按各工具合同处理，不强行附加项目。
- 权限由账号、项目访问范围和 `dami:read/write/publish/audit` 共同约束。UI 与 AI 使用相同权限，Skill 无法授予访问权。
- 401/授权过期：使用宿主重新连接原账号。403/权限不足：报告所需范围，不能借另一身份绕过。
- 参数错误：重新读取工具输入合同或领域 schema；业务锁/版本冲突：重读状态并保留他人修改。
- 工具返回 `request_id` 时可提供给用户排查；不附带令牌、签名上传地址或第三方密钥。

## 长任务

站点发布用 `publish_site → get_publish_status`，页面用 `publish_page → get_page_publish_status`，节点用 `trigger_deployment → get_deployment_status`，博客用 `publish_blog_post → get_blog_push_status`。

受理后记录 task/project/resource ID，按返回状态轮询；无新日志不是失败。宿主有等待能力时逐步延长间隔，没有等待能力时交付真实的进行中状态和后续查询方式。不要为取得新输出再次触发发布。达到宿主执行上限时说明哪些已完成、哪些仍在运行。

## 翻译与发布闸门

当前入口是 `get_translation_status` 与联合 `get_publish_readiness`。旧连接的 `get_translation_coverage` 是兼容名称，不引导新任务使用它；旧 `fresh` 结果也不能证明新发布合同就绪。

站点发布应核对 site 与 pricing 的翻译状态及 `publish_operation`；页面核对 page:<id>。其他人持有锁、`blocked=true` 或 `can_continue=false` 时停止写入和发布。缺少联合 readiness 时先刷新工具定义；若连接确实只能逐 scope 查询，必须同时核对 site、pricing 和发布锁，不能只检查语言。

## UI 与文件

`open_dami_workbench` 提供可选工作台；无 MCP Apps 支持时仍使用数据工具。UI 的选中项是上下文，不能据此自动发布或发送。

远程 MCP 不能读取用户电脑上的路径。文件必须来自宿主可访问的真实字节、已授权的公网直链或已登记素材；具体上传及不明确结果的恢复见 [media-library.md](media-library.md)。
