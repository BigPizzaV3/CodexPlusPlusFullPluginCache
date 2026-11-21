# Upload checklist

1. Open [OpenAI Platform](https://platform.openai.com) → Apps / Plugins → create **OmniChat** (or new draft version).
2. Upload `OmniChat-AI-plugin-v1.0.3.zip`.
3. Confirm listing fields populated from package:
   - Subtitle: `Manage OmniChat inbox`
   - Website: `https://www.getomnichat.com`
   - Support: `https://www.getomnichat.com/support`
   - Privacy: `https://www.getomnichat.com/privacy`
   - Terms: `https://www.getomnichat.com/terms`
   - Category: **Business & Operations**
   - App icon / logo present
4. Confirm MCP URL: `https://mcp.getomnichat.com/mcp` → **Scan / Rescan tools**.
5. Domain verified via `/.well-known/openai-apps-challenge` (set `OPENAI_APPS_CHALLENGE_TOKEN` on MCP host).
6. Paste test cases from `REVIEW.md` (5 positive + 3 negative).
7. Confirm reviewer OmniChat OAuth login works:
   - Email: `chatgpt-review@getomnichat.com`
   - Password: `OmniReview-ChatGPT-2026!`
8. **Submit for review**.

Note: ChatGPT reinstall alone does **not** send the app back into review.
