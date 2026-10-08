# Codex++ Full Plugin Cache（私有归档）

此仓库保存从当前账号可取得的完整本地插件市场快照：**5,491 个实际插件包，分为 7 个市场目录**。仓库应保持私有；其中部分包没有公开再分发许可，不能当作公开镜像发布。

## 使用

先克隆仓库，然后把每个市场目录分别注册：

```sh
git clone https://github.com/BigPizzaV3/CodexPlusPlusFullPluginCache.git
codex plugin marketplace add ./CodexPlusPlusFullPluginCache/markets/01
codex plugin marketplace add ./CodexPlusPlusFullPluginCache/markets/02
codex plugin marketplace add ./CodexPlusPlusFullPluginCache/markets/03
codex plugin marketplace add ./CodexPlusPlusFullPluginCache/markets/04
codex plugin marketplace add ./CodexPlusPlusFullPluginCache/markets/05
codex plugin marketplace add ./CodexPlusPlusFullPluginCache/markets/06
codex plugin marketplace add ./CodexPlusPlusFullPluginCache/markets/07
```

注册市场只建立目录，不会自动安装全部插件。按需安装：

```sh
codex plugin add <插件名称>@codex-plus-full-local-01
```

完整目录、失败的 22 个条目、下载统计和 API Key 读取验证见 `directory.json`、`summary.json`、`api-read-validation.json`。

上传时刻意排除了一个插件包中的 `.env` 和 `.env.local`；它们含有凭据，完整列表见 `upload-exclusions.json`。本机缓存仍保留原文件。

## 范围与限制

此快照没有调用插件安装器，也没有执行插件包内代码。插件包可能包含需要单独账号、OAuth 或第三方服务授权的 MCP 连接器；API Key 模式下“包能安装”不等于远程服务一定能连接。

公开可再分发的子集另见 [CodexPlusPlusPluginCache](https://github.com/BigPizzaV3/CodexPlusPlusPluginCache)。
