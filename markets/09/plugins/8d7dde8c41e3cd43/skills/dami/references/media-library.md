# 素材与双语创作

素材统一由 media_asset 保存，关联可跨站共享。ai_description 是素材实际内容描述，可为空；description 仍是创作说明/文章中文摘要，二者不能互相覆盖。

## 读取与上传

先 `get_site`，再按需 `list_media_assets` / `get_media_asset`，站内文章用博客工具读取。`get_content_writing_context` 聚合背景与最多 200 条最近素材摘要，不代表完整列表或正文。

- `upload_media_asset` 接收真实公网 HTTPS 直链 source_url，或真实字节 content_base64，二选一；filename 带正确扩展名。Base64 解码最多 2 MiB，不编造附件地址或字节。
- 直链必须公开可读、默认端口、无登录凭据、无重定向。后台不带 Agent Key 下载；类型与大小由当前工具/服务端合同限制。
- origin=reference 用于导入，ai_generated 用于创作；仅 status=registered 表示已登记可用。
- uploaded_not_registered / upload_unknown 时保留 recovery 原回执，用 `complete_media_asset_upload` 核实与登记，不重新上传。回执过期时先查素材是否已有记录。
- 宿主确有文件传输能力时才用 `prepare_media_asset_upload` → 按返回 mime 向 put_url 上传真实字节 → `complete_media_asset_upload`。拿到签名不等于已上传。没有这种能力时使用可读直链或已登记素材，不把本地路径交给远程服务。
- complete 使用原 upload_token、file_url、asset_type、mime、实际 size_bytes 与同一 project_id；签名回执不能作为公开分享链接。

`update_media_asset_description` 只改 ai_description，空字符串可清除。`save_media_asset_text` 保存已有 Markdown/链接，按合同传正文或 URL。描述为空时读取实际内容，不根据文件名臆测图片/视频。

## 创作

站内博客走 [blog.md](blog.md)；本节 article 是双语 guest post/软文素材，不创建站内博客 URL。

1. 读取真实站点、素材、历史内容与关键正文，不编造产品功能。
2. 分别完成目标语与中文对照 Markdown。帖子无标题；文章有两种语言的标题与正文，中文摘要单独填写。
3. 帖子用 `save_bilingual_post`；文章用 `save_bilingual_article`。新的首次保存使用稳定 idempotency_key，结果不明确先核实，不换键盲目重发。
4. 改文章先 `get_bilingual_article`，再 `update_bilingual_article`，同时提交两份对应正文；可选外链/语种等字段省略保留原值。
5. 素材 ID 与返回 preview_url 证明入库，不能把生成草稿等同保存成功。文章预览链接指向素材库，改稿后链接保持不变。

正文自然使用有依据的锚文本和外链，不提交明显 HTML 代替 Markdown。创作与保存不包含向外部平台发布的授权。

## 入库失败的交付

如工具不可用或入库未完成，明确写“未保存到素材库”，提供两个独立 Markdown 代码块：第一块仅目标语，第二块仅中文。文章每块包含本语 H1，帖子无标题；语种标签写在代码块外，不混排，不伪造 ID/链接。

上下文获取失败时仅使用用户已提供且可确认的事实。连接恢复后先核对是否已保存，再用原保存意图和幂等标识恢复。
