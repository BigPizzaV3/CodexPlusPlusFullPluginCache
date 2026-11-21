---
name: wedding-help
description: FAQ, 공지사항, 알림, 읽지 않은 알림, 1:1 문의, 오류 신고, 앱 피드백을 보거나 등록할 때 사용한다. Use for WeddingFlow notices, FAQs, notifications, support inquiries, and product feedback. Do not use for community posts or dress-rental inquiries.
---

# WeddingFlow help

Answer in Korean. Quote notices and FAQ answers from the tool result. Do not invent a support policy.

## Tools

| Intent | Tool |
| --- | --- |
| FAQ categories | `get_api_v1_faq_category`, `get_api_v1_faq_category_by_category_id` |
| FAQ list and detail | `get_api_v1_faq`, `get_api_v1_faq_by_faq_id` |
| Notices | `get_api_v1_notice`, `get_api_v1_notice_by_notice_id` |
| Notifications | `get_api_v1_notification` |
| Unread count | `get_api_v1_notification_unread_count` |
| My inquiries | `get_api_v1_inquiry`, `get_api_v1_inquiry_by_inquiry_id` |
| Create an inquiry | `post_api_v1_inquiry` |
| Send feedback | `post_api_v1_feedback` |

Keep `page_size` and `limit` at 20 or below. This connection cannot mark notifications as read.

## Inquiry

Search FAQ and notices before opening an inquiry. If the user still wants to contact support, confirm the question. `post_api_v1_inquiry` body:

- `question`: required, at most 4000 characters
- `type`: optional. One of `user_info`, `payment`, `ETC`, `error`, `chat`, `reply`, `post`, `comment`, `wedding_select`. Default is `ETC`.

Do not retry a failed POST. The user cannot send the answer; they can only read it later.

## Feedback

Use this for opinions about WeddingFlow itself, not for a rental or community report.

- `satisfaction`: `very_satisfied`, `satisfied`, `neutral`, `dissatisfied`, `very_dissatisfied`
- `opinion_category`: `feature_request`, `usability`, `bug`, `content`, `customer_experience`, `other`
- `opinion`, `burdensome_part`, `requested_feature`
- `phone_number` and `is_privacy_agreed` only if the user explicitly wants a gift and agrees to share the number

Confirm the text before saving. Never ask for a password or token. Authorization uses the host OAuth flow.
