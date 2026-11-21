---
name: wedding-magazine
description: 매거진, 결혼 정보 글, 추천 글, 매거진 댓글, 유튜브 영상을 찾을 때 사용한다. Use when recommending or reading WeddingFlow magazines and YouTube videos, or writing a magazine comment. Do not use for community posts or notices.
---

# WeddingFlow magazine

Answer in Korean. Recommend articles that the WeddingFlow MCP server actually returned. Do not invent titles, authors, or links.

## Tools

| Intent | Tool |
| --- | --- |
| Search or list | `get_api_v1_magazine` |
| Recommendations for the user's wedding date | `get_api_v1_magazine_recommended` |
| Categories | `get_api_v1_magazine_category` |
| One article | `get_api_v1_magazine_by_magazine_id` |
| Comments | `get_api_v1_magazine_comment` |
| Write a comment | `post_api_v1_magazine_comment` |
| YouTube settings | `get_api_v1_youtube_settings` |
| YouTube videos | `get_api_v1_youtube_videos` |

Pass arguments only in the `query`, `path_params`, or `body` sections that tool declares. Keep `page_size` and `limit` at 20 or below.

Magazine list query fields: `search` for a simple title search, `q` for broader search, `category`, `liked_by_me`, `commented_by_me`. Ordering values include `-created_at`, `-popularity`, `-view`, `-like_count`, and `-comment_count`.

For "what should I read now", call the recommended endpoint first. It uses the account wedding date when one is saved. If there is no wedding date, say the recommendation is not date-based.

## Comments

Show the article title, then confirm the comment text. `post_api_v1_magazine_comment` body needs `magazine` (the article id) and `content`. Do not retry a failed POST. This connection cannot edit or delete a comment, and it cannot like an article.

Summarize the retrieved article. Distinguish that summary from text that was not in the tool result.
