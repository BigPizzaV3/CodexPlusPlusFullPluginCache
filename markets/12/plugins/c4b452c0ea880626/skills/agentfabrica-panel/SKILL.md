---
name: agentfabrica-panel
description: Use when the user asks about their AgentFabrica marketing panel, such as brands, the content calendar, items waiting for approval, ad pre-test results, lead or WhatsApp counts, plan quota, or wants a draft post added to a brand's approval queue.
---

# Working with the AgentFabrica panel

AgentFabrica is a marketing operations panel. The connected tools read the user's own account and can add a draft post to an approval queue. They never publish, approve or delete anything.

## Start with the brand

Most tools take a `brandId`. When the user names a brand, or the account may hold more than one, call `list_brands` first and use the id of the matching brand. If two brands could match the name, ask which one the user means before going further.

## Pick the tool that answers the question

| The user wants | Tool |
|---|---|
| Their brands, industry, website and tone of voice | `list_brands` |
| Upcoming or past posts and their status | `scheduled_posts` |
| Everything waiting for a person to decide | `pending_approvals` |
| How ads scored with the panel before launch | `ad_pretests` |
| How reliable the panel has been for this brand | `calibration_report` |
| Which hooks, angles and formats have worked for the brand | `learning_pool` |
| Lead counts by status and source | `lead_summary` |
| WhatsApp line status and conversation counts | `whatsapp_summary` |
| Plan usage and what remains | `quota_status` |
| Recently generated content | `generated_assets` |
| A new draft post in the approval queue | `submit_post_for_approval` |

## Report results accurately

- Approval items come with a `reviewUrl`. Give the user that link, and say that approving or rejecting happens in the panel.
- `lead_summary` and `whatsapp_summary` return counts only. If the user asks for names, phone numbers or message text, explain that the panel does not share them through this connection.
- An ad pre-test score is the panel's reaction to the ad. Do not present it as a forecast of reach or sales. When the ad later ran, the real result is included, so report both.
- When `calibration_report` or `learning_pool` says there is not enough data, pass that on instead of estimating a number.
- If a tool returns an error, tell the user what failed and what they can do next. Do not fill the gap with guessed figures.

## Adding a draft post

1. Confirm the brand, the platforms (facebook, instagram, linkedin) and the caption with the user before calling `submit_post_for_approval`.
2. Instagram needs at least one public `https://` image URL. If the user has none, offer Facebook or LinkedIn, or ask for an image link.
3. Without `scheduledAt`, the brand's best posting time is used. Say so in the reply.
4. After the call, tell the user the draft is waiting for approval and share the `reviewUrl`. Never describe the post as published or scheduled to go out on its own.
