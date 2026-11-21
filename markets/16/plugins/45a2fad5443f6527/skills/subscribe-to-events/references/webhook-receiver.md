# Receiving monday webhooks (Path B)

ChatGPT and Codex plugins can't host an inbound URL. A board webhook needs an HTTPS endpoint the user controls:

- **No-code:** Zapier "Catch Hook", Make "Custom webhook", n8n "Webhook" node. Add a step that answers monday's challenge (below).
- **Own service:** any HTTPS endpoint.

## 1. Answer the challenge
When the webhook is created, monday POSTs:
```json
{"challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P"}
```
Return HTTP 200 with the same JSON body. Minimal example (Node/Express):
```js
app.post("/monday", (req, res) => {
  if (req.body.challenge) return res.json({ challenge: req.body.challenge });
  // handle req.body.event ...
  res.sendStatus(200);
});
```

## 2. Handle events
- Payloads arrive as `{"event": {...}}`. See `event-catalog.md` for fields.
- Retries happen once a minute for 30 minutes. De-duplicate on `event.triggerUuid`.
- Webhooks created with a user OAuth token (as this skill does) are **not JWT-signed**. JWT signing needs a webhook created with a monday app integration token. Don't trust payload contents blindly: re-fetch the item through the monday API before acting, and keep the URL unguessable.

Source: https://developer.monday.com/api-reference/reference/webhooks
