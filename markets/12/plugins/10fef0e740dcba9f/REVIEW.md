# OmniChat — OpenAI review notes (v1.0.3)

## MCP

- **URL:** `https://mcp.getomnichat.com/mcp`
- **Auth:** OAuth 2.0 (OmniChat) — authorize via `https://www.getomnichat.com`
- **Domain challenge:** `https://mcp.getomnichat.com/.well-known/openai-apps-challenge`
- **Health:** `https://mcp.getomnichat.com/health` → `ok: true`

## Fixes in v1.0.3 (further-review unblock)

OpenAI flagged credential-ingest tools for “needs further review”. These are **removed from the ChatGPT tool surface**:

| Removed from ChatGPT | Replacement (read-only) |
|----------------------|-------------------------|
| `telegram_connect` | `get_channel_connect_url` (`channel: telegram`) → dashboard |
| `connect_store_integration` | `get_store_integration_connect_url` → `/integrations` |
| `update_store_integration` | same connect URL (update credentials in dashboard) |
| `create_ai_custom_tool_from_url` | `get_ai_custom_tool_setup_url` → `/ai` Custom Tools |

Bot tokens, shop API keys, and bearer/HMAC secrets are **never accepted in ChatGPT**. Merchants paste them only in the signed-in OmniChat dashboard.

## Reviewer login (OAuth)

| Field | Value |
|-------|-------|
| **Email** | `chatgpt-review@getomnichat.com` |
| **Password** | `OmniReview-ChatGPT-2026!` |

Login: `https://www.getomnichat.com/login`

## Suggested review test cases

### Positive (5)

1. “Show my OmniChat account overview” → `read_store_context`
2. “Check channel health” → `get_channel_health`
3. “List recent WhatsApp conversations” → `list_conversations`
4. “How do I connect Telegram?” → `get_channel_connect_url` with telegram (dashboard URL, no token prompt)
5. “How do I connect Shopify?” → `get_store_integration_connect_url`

### Negative (3)

1. Ask for a fake conversation UUID → not found / error
2. `send_inbox_reply` missing required fields → validation / isError
3. Ask to change billing plan → only `get_billing_status` (read-only)
