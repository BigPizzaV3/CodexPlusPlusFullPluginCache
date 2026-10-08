# ChatGPT Work 等云端环境的独立授权

此流程创建新的云端授权，不复制本机已有凭据。CLI 1.2.1 只有 loopback 回调，
所以用户必须在自己的电脑运行一次 Python 3 授权助手；不能只在本机打开云端的
127.0.0.1 链接。若用户无法运行助手，明确报告此限制，不声称安装插件即已授权。

## 发起

先运行 `sh "<skill-root>/scripts/browser.sh" auth status` 和 `doctor`。
已有凭据且 doctor 就绪时直接继续；仅缺少凭据时创建请求：

```sh
python3 "<skill-root>/scripts/remote_auth.py" begin \
  --output-dir "<task-deliverable-dir>" \
  --private-root "<task-private-dir>/.lexmount-auth" \
  --client-name "ChatGPT Work"
```

使用当前任务真实、获准写入的绝对目录，不猜测路径。私有目录必须位于交付目录
之外；不能把整个任务工作区打包交付。只交付返回的 `helper_file`，记住本任务
的 `state_dir` 和 `credentials_file`。PKCE verifier 只保留在云端私有状态中。

告诉用户：“下载授权助手，在自己的电脑运行 `python3 "<实际助手文件名>"`
（Windows 可用 `py`），在浏览器中确认 LexMount 授权。再把助手旁边生成的
`lexmount-authorization-result-*.json` 文件上传回本任务，无需填写 API Key。”
给出助手的实际下载链接。助手不是已经在用户电脑上运行，不替用户点击授权同意。
返回文件只包含一次性授权码和请求关联字段，不包含 API Key；不要展示文件内容。

请求 30 分钟过期；用户确认后的授权码 10 分钟过期。等待附件，不轮询登录。
不得自动上传本机凭据、助手结果或扩大既有授权范围。

## 完成

用户上传后，从当前附件元信息获取真实文件路径，执行：

```sh
python3 "<skill-root>/scripts/remote_auth.py" finish \
  --state-dir "<returned-state-dir>" --callback-file "<actual-upload-path>"
LEXMOUNT_BROWSER_CREDENTIALS_FILE="<returned-credentials-file>" \
  sh "<skill-root>/scripts/browser.sh" doctor
```

每条后续 CLI 命令都使用同一 `LEXMOUNT_BROWSER_CREDENTIALS_FILE`。
不要 cat、打印或把凭据和回调文件内容放进提示词。兑换校验 state、PKCE、回调
地址和有效期；成功后消耗请求，并将凭据以 0600 权限保存在 0700 私有目录内。
只有 `data.ready_for_browser_actions == true` 才恢复原网页任务。

恢复任务时先运行 `remote_auth.py status --state-dir ...`。过期则生成新请求，
状态丢失则说明无法恢复；不要搜索其他任务的凭据。此包不保证云平台跨任务或
沙箱回收后保留文件；没有平台持久化保证时，只承诺当前任务内复用。

安装失败、授权缺失、授权兑换失败、服务连通失败和网页失败必须分别报告。
本包没有 MCP 连接器，不能让用户去插件设置寻找不存在的 CLI OAuth 按钮。
