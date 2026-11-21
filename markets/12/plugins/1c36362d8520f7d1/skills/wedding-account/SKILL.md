---
name: wedding-account
description: 내 정보, 활동 배지, 티켓, 결혼 조사, 플랜, 웨딩 메시지 기록과 남은 메시지 사용량을 볼 때 사용한다. Use when the user asks who they are in WeddingFlow, their badges, tickets, marriage survey, plans, or saved planner messages. Do not use to send gifts or generate an in-app AI reply.
---

# WeddingFlow account

Answer in Korean. Profile and entitlement data come from the MCP server. Do not infer a wedding date, partner, or ticket balance that the tool did not return.

## Tools

| Intent | Tool |
| --- | --- |
| Signed-in profile | `get_api_v1_auth_me` |
| Activity badges | `get_api_v1_activity_badge` |
| Unseen badges | `get_api_v1_activity_badge_unseen` |
| Tickets | `get_api_v1_ticket`, `get_api_v1_ticket_by_ticket_id` |
| Received and sent ticket gifts | `get_api_v1_ticket_gift_received`, `get_api_v1_ticket_gift_send` |
| Marriage survey and stats | `get_api_v1_survey`, `get_api_v1_survey_statistic` |
| Plans | `get_api_v1_plan` |
| Saved planner messages | `get_api_v1_message` |
| Message usage | `get_api_v1_message_usage` |

Start account questions with `get_api_v1_auth_me` when the wedding, name, or permission is unclear. Keep list sizes at 20 or below.

When the user asks who the connected WeddingFlow account is, call `get_api_v1_auth_me` and answer with `email` and `name`. If `name` is empty, say the name is not set and still give the email. Do not mention a numeric user id. Do not send the user to My Page when the tool returned `email` or `name`.

## Limits

This connection cannot edit the profile, withdraw, invite a partner, send or issue a gift, or mark a badge as seen. Gift tools here are read-only lists.

`get_api_v1_message` is the saved WeddingFlow planner thread, not this ChatGPT conversation. `get_api_v1_message_usage` reports remaining usage. Do not call `post_api_v1_message` to store this chat, and do not claim an in-app AI reply was generated. That generation tool is not available. If the user explicitly asks to save one message into WeddingFlow, confirm the exact `content` first and explain that it only stores the message.

If OAuth is required, use the host flow. Never ask the user to paste a token. Hide password, token, and secret fields if any appear in a result.
