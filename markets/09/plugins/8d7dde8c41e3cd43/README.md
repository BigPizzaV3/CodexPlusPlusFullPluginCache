# 大米 2.4.1

这是唯一的 OpenAI 正式提交包，包含远程 MCP 配置、共同 Skill 和 UI 审阅副本。前往 https://platform.openai.com/plugins，在已有正式插件记录选择 Upload plugin to make changes 上传完整 ZIP，保留同一插件身份；首次提交才使用 Upload new or existing plugin。若此前只有 ChatGPT 个人开发连接，不能据此认定开发者平台已有正式记录，需先核对。完成 MCP 连接、域名验证、认证、扫描、审核和发布后，用户安装一个插件并授权使用。不要把本包直接导入 ChatGPT 个人页后宣称已支持网页；工作区导入直接 MCP 配置仍有 Desktop only 限制。本包替代 2.0.1 的私有应用引用产物，不包含 apps 或 .app.json，上传到现有记录才保持平台身份。保留旧 dami 连接，待正式插件可用后再清理重复的个人导入项；不要删除正式插件记录重建。元数据、隐私政策、支持入口和审核材料仍须按开发者平台检查结果补齐。

插件技术名称：`dami-workbench`；显示名称：大米。2.0.3 起使用此名称，绕过旧个人导入项 dami 的重名占用；第一次上传会创建新身份，不会覆盖或迁移旧记录。后续固定此名称并更新该记录。此改名不改变宿主的 Desktop only 判定。

MCP 地址：https://quick-deploy.com/mcp

UI 由 MCP resources/read 提供；仅 OpenAI 包附带 assets/workbench.html 同源审阅副本，不是独立登录网页。上传 ZIP 不会部署服务器；工具、UI 元数据变化须部署后台并按宿主要求刷新/扫描。内置 Agent 的 Skill 变化需重新构建部署。

本地客户端说“更新大米”即可由 CLI 同步 dami 与 dami-dev；ChatGPT 网页从 AI + 下载新版运营 Skill 后上传。项目列表默认未归档，只有明确查看或恢复归档站点时才查询归档列表。
