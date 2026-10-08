# Privacy notice / 隐私说明

Effective date / 生效日期: 2026-09-10

Publisher / 发布者: ailuntz

Website: https://www.ailuntz.com

Codex Usage is a local plugin with a Python script. By default it reads JSONL
files in the selected Codex installation's `sessions` and `archived_sessions`
directories. It extracts structured usage metadata: percentages, window lengths,
reset times, plan labels, paid-credit balances, reset-card summaries when present,
and source file locations. Diagnostic results include the checked data directory,
reader version, and aggregate file/event counts. It does not return conversation contents, account IDs,
authentication tokens, or credential-file contents.

The publisher does not operate a backend for this plugin, collect analytics,
or receive your history. Results returned to your assistant become part of that
AI platform's conversation and are subject to its data practices. Source paths
can include a local username; omit them when sharing results publicly.

The `--live` mode runs the installed Codex CLI's app server and asks it
to read account rate limits using its existing authentication. Codex may contact
OpenAI and perform its normal credential refresh. The plugin does not open a
login flow, directly read credential files, or send credentials to its publisher.
Only allowlisted usage metadata is returned; arbitrary backend errors and
account identifiers are omitted.
The skill may try this once when local records cannot answer the usage query,
when requested reset-card details are missing, or when a live refresh is requested.

The script does not persist a report, modify history, consume reset cards, or
purchase credits. Your shell, Codex client, or AI platform may retain command
history or logs under their own policies. Installing the plugin and fetching
source code also involve OpenAI and GitHub. There is no publisher-side account
or user database to delete; uninstall the plugin to stop using it.

本插件默认在本地提取 Codex 用量记录，发布者不接收会话历史，也不提供托管查询服务。
查询结果进入你所使用的 AI 对话，适用该平台的数据政策。可选实时查询复用 Codex
已有认证，由 Codex 联系 OpenAI；插件不直接读取凭据文件，不兑换重置卡或购买积分。
结果中的本地路径可能包含用户名，公开分享前请删除。

Support: https://github.com/ailuntx/codex-usage/issues. Issues are public; do not
post raw history, credentials, account identifiers, or other private information.
