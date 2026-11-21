# 站内博客（blog）

## 边界先行

站内博客拥有 `/blog` 与 `/blog/{slug}` 公开页面，中心真相是独立的 post + locale + revision，发布后才把完整快照推到节点。

- 博客 MCP 工具：站内博客，支持多语种、SEO、readiness、发布/下线。
- `save_bilingual_article`：双语 guest post 或软文素材，落素材库，不生成站内博客页。
- 动态页面：页面配置快照，不承载博客文章。

总后台的博客页负责列表、多语种预览以及上架、下架、删除，不提供新建、编辑、翻译或校验入口。后台状态操作与 Dami 共用 revision、readiness 和节点任务；文章内容生产与修改仍统一走 Dami 的受控合同。

用户只说“文章”时先根据交付目标判断；要站内 URL、博客列表或 SEO 即使用 blog，要交给外部渠道发布或素材预览即使用 article。不能在三者之间复制数据冒充完成。

## 固定工作流

顺序不能跳过：

```text
contract → upload assets → default locale → validate + preview
         → translation locales (if any) → validate → readiness → publish
```

1. 确认当前 `project_id`，读取 blog contract；模板未声明 `supported=true` 或版本不兼容就停止。
2. 正文图片和封面先上传到当前 `project_id` 的站点 CDN，再把返回的公开 `file_url` 写入 Markdown/front matter。不能直接引用外站图片、其他站点素材、Base64 或本地路径。
3. 新文章只创建 contract 的 `default_lang`，不得同时生成译稿，也不得用 `config_lang` 替代默认语种。每次写入都以最新 detail 的 `revision` 为乐观锁。
4. 默认语种保存后立即 `validate`，再用 `get` 或总后台预览逐项检查正文、SEO 标题、SEO 描述和封面。默认语种未通过校验时禁止调用 `save_blog_locale`。
5. 只遍历 contract 的 `translation_langs` 做母语化写作；数组为空表示站点只有默认语种，整个翻译阶段直接跳过。每份译稿绑定当时的 `source_revision`，源稿变化后旧译稿必须重做。
6. 校验所有稿件，再读取 readiness。任何缺失语种、过期译稿、SEO、Markdown、CDN 素材、路由或能力错误都必须解决。
7. 只有 readiness `ready=true` 且用户明确要求上线时才能发布。发布返回 durable task；未 `succeeded` 不能声称线上已生效。

博客译稿不使用通用 `i18n export/import`。每保存一个 locale 都会增加文章 revision，因此下一次写入前重新读取 detail。

封面采用“共享默认 + 语种覆盖”模型：源稿的 `cover_url` 是所有语种默认封面；译稿省略 `cover_url` 就继承，只有确有本地化需求时才传当前站点 CDN 的独立封面；传空字符串表示清除该语种覆盖并恢复继承。`cover_alt`、SEO 标题和 SEO 描述始终逐语种保存。

## MCP

云端先看实时 `tools/list`，不要把下列名字当静态白名单。完整链路的语义映射是：

- 合同/读取：`get_blog_contract`、`list_blog_posts`、`get_blog_post`
- 源稿/译稿：`create_blog_post`、`save_blog_source`、`save_blog_locale`
- 闸门：`validate_blog_post`、`get_blog_readiness`
- 上线状态：`publish_blog_post`、`unpublish_blog_post`、`delete_blog_post`、`get_blog_push_status`

写工具属于 `dami:write`，公开状态变更属于 `dami:publish`。完成发现仍缺工具时报告当前会话未取得该工具，不直接拼 HTTP 或写数据库。

素材上传按 [media-library.md](media-library.md) 使用真实直链/字节或具备传输能力的宿主；远程服务无法读取本地路径。缺素材能力时说明限制，不绕过 CDN 合同。

## Markdown 合同

Markdown 使用 GFM，不含原生 HTML、javascript:、data:、协议相对 URL 或本地路径。外链仅 HTTPS，站内绝对路径和锚点按合同允许。正文和封面图片必须是当前站点已登记 CDN 素材。标题、摘要、SEO 和正文分别按工具字段提交，不依赖本地文件 front matter 默认补全。

## Revision 与完成判定

- `revision`：任意共享字段、源稿、译稿或公开状态变化的并发闸门。
- `source_revision`：只在源内容变化时增加，是所有译稿的新鲜度基准。
- `published_revision`：节点确认成功的线上版本；保存成功不等于发布成功。
- slug 首次发布后不可修改；删除先下线，节点失败时中心稿件保持可恢复。
- 最终只在节点 task `succeeded` 且公开 URL 可访问时报告成功；缺失语种返回 404 是正确行为，不能用源稿回退掩盖问题。
