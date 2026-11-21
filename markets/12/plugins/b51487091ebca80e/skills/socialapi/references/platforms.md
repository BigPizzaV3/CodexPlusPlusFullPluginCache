# What each platform supports

A "no" is final: the tool returns `resource.not_supported` or the plain sentence "Operation not supported for this platform" (`account.platform_unsupported` for reviews, `automation.platform_unsupported` for Automations), and retrying never changes it. Tell the user which platform cannot do it and offer one that can.

## Platform values

| Platform | `platform` value | Notes |
|---|---|---|
| Instagram | `instagram` | Professional (Business or Creator) account |
| Facebook | `facebook` | Pages. One account can hold several Pages, see `list_account_pages` |
| Threads | `threads` | |
| TikTok | `tiktok` | |
| X | `twitter` | Calls run on the X developer app the user connected, so X rate, credit and permission errors come from that app's X plan |
| YouTube | `youtube` | One account per channel |
| LinkedIn | `linkedin`, `linkedin_page` | A member profile and an organization Page are separate account types. Organization Pages are not open to every account: connecting one may return `billing.platform_not_available` |
| Google Business Profile | `google` | One account per Business Profile |
| Pinterest | `pinterest` | Boards instead of Pages |
| WhatsApp | `whatsapp` | WhatsApp Business |
| Telegram | `telegram` | Bot |
| Zalo | `zalo` | Official Account |
| Bluesky | `bluesky` | |

## Comments, DMs, mentions

| Platform | Read comments | Reply | Hide | Delete | Like | Private reply | DMs | Mentions |
|---|---|---|---|---|---|---|---|---|
| Instagram | yes | yes | yes | yes | no [1] | yes | read and send | read and reply |
| Facebook | yes | yes | yes | yes | yes | yes | read and send [2] | read and reply |
| Threads | yes | yes | see [3] | own replies only | no | no | no | see [3] |
| TikTok | no | no | no | no | no | no | no | no |
| X | last 7 days | yes | yes | own replies only | usually refused [4] | no | read and send, text only | read only |
| YouTube | yes | yes | yes | yes | no | no | no | no |
| LinkedIn (member) | no | no | no | no | no | no | no | no |
| LinkedIn Page | yes | yes | no | yes | yes | no | no | no |
| Google Business Profile | no | no | no | no | no | no | no | no |
| Pinterest | no | no | no | no | no | no | no | no |
| WhatsApp | no | no | no | no | no | no | send [5] | no |
| Telegram | no | no | no | no | no | no | send [5] | no |
| Zalo | no | no | no | no | no | no | read and send | no |
| Bluesky | yes | yes | your threads only [6] | own replies only | no | no | read and send [6] | read and reply |

1. Liking comments and deleting or unpublishing a published post are not available for Instagram accounts connected with Instagram Login, the standard way Instagram accounts connect. A published Instagram post can be deleted in the Instagram app.
2. On Facebook, `quick_replies` and `buttons` are not shown (the text is sent alone) and `message_tag` is not applied, so a Facebook DM can only be sent within 24 hours of the person's last message. Private replies on Facebook do show their buttons.
3. Hiding comments and reading or replying to mentions are refused for most Threads accounts. Report the error rather than retrying.
4. X restricts liking through its API on most access plans, so `like_comment` on X usually fails.
5. WhatsApp and Telegram conversations appear only after the person has messaged the account, and `send_dm` answers inside them. WhatsApp accepts a free-form reply only within 24 hours of the customer's last message.
6. On Bluesky, hiding works on replies in threads the account started, and DMs need an app password that allows direct messages.

More rules:
- `moderate_comment` follows the Hide and Delete columns, except on a LinkedIn Page, where only `delete` works.
- Quick replies and buttons in `send_dm` display on Instagram. Other platforms send the text alone or refuse them.
- `message_tag` applies on Instagram only, and only `HUMAN_AGENT`.
- Private replies: Instagram and Facebook, once per comment, within 7 days of it.
- Stories (`list_instagram_stories`): Instagram only.
- Reviews (`list_review_accounts`, `get_reviews`, `reply_to_review`): Google Business Profile only. A reply may come back with `state: PENDING` while Google checks it. Replying again replaces the existing reply, and deleting one is not available.
- Automations: Instagram and Facebook only.

## Publishing and account tools

| Platform | Publish and schedule | Delete or unpublish | `get_account_limits` | Notes |
|---|---|---|---|---|
| Instagram | yes | no [1] | yes | `platform_data.instagram.content_type` is required: `feed` (one image), `carousel` (2 to 10 items), `reel` (video) or `stories`. Text alone cannot be published |
| Facebook | yes | yes | no | `page_id` per target picks the Page, otherwise the default Page posts |
| Threads | yes | yes | yes | Chaining several posts into one Threads thread is unavailable |
| TikTok | yes | no | no | Call `get_creator_info` first: `platform_data.tiktok.privacy_level` must be one it lists |
| X | yes | yes | empty result | `segments` chains a native thread |
| YouTube | yes | yes | yes | Set `title` |
| LinkedIn (member) | yes | yes | no | Only posts created through SocialAPI appear in `list_posts` |
| LinkedIn Page | yes | yes | no | `page_id` picks the organization Page |
| Google Business Profile | yes | yes | no | Local posts on the Business Profile |
| Pinterest | yes | yes | no | `board_id` is required on every target, `list_pinterest_boards` lists the boards |
| WhatsApp | no | no | yes | Messaging only |
| Telegram | no | no | no | Messaging only |
| Zalo | yes | yes | yes | Articles and videos |
| Bluesky | yes | yes | yes | |

`get_creator_info` works on TikTok only. `get_account_limits` reports the platform's own quotas (posts remaining, messaging tier), separate from plan credits, and returns `resource.not_supported` on the platforms marked no.
