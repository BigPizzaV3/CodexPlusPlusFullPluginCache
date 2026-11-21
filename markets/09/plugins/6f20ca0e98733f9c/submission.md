# Perisclaw 0.3.1 submission candidate

The manifest contains listing fields, starter prompts, onboarding skill, and five
positive/three negative reviewer scenarios. Upload the complete directory as a
ZIP: root `plugin.json` and `mcp.json`, skills and assets. Root
`extensions.com.openai` is the only manifest; the legacy `.codex-plugin` overlay
is not shipped because OpenAI ignores it when root extensions exist. The endpoint is
`https://api.perisclaw.com/mcp/plugin`; direct clients can keep `/mcp`.

This candidate adds catch-up and reply cards (MCP Apps), editable replies sent
from the card at most once, and account identification. Read/write scope and
blocked-chat rules apply on the server. Tool results also work in clients that
cannot render the cards.

Watching chats (`message.received` events, `monitor_list`, `monitor_stop`) is
built but not part of this submission: it is off in production, its tools are
only listed where it is enabled, and a reviewer cannot trigger an incoming
WhatsApp message. Add it to the listing and review cases once events are on in
production and reviewers have a way to send a test message. Scheduled actions remain
in Perisclaw Automations: the plugin manages existing ones (list, inspect, enable
or disable, run control, delete) but does not create or edit them.

## Publisher and ownership

OpenAI rejected 0.3.0 (2026-10-16) because it could not tie the Perisclaw brand
to the verified business. The publisher is **Hashlabs Holdings Inc.**, the
business verified on the submitting OpenAI organization, and it owns the
Perisclaw name and brand. From 0.3.1, `author` and `developerName` name Hashlabs
Holdings Inc. instead of the product, and the listing description says so.
Evidence to give reviewers:

| Evidence | Where |
| --- | --- |
| Verified business on the submitting organization | OpenAI Platform → Organization settings → Verifications: Business, Approved (Hashlabs Holdings Inc) |
| Site footer and structured data name the owner | https://www.perisclaw.com: "© Hashlabs Holdings Inc"; schema.org `parentOrganization` Hashlabs Holdings Inc |
| Legal pages name the provider | https://www.perisclaw.com/legal/terms-of-service and /legal/privacy-policy: "Perisclaw is provided by Hashlabs Holdings Inc." |
| Domain control | `api.perisclaw.com` serves the OpenAI domain-verification challenge (`OPENAI_APPS_CHALLENGE_TOKEN`) |
| Same publisher in Claude's directory | Connector and plugin submitted by Hashlabs Holdings Inc. |

## Reviewer setup and behavioral evals

The reviewer account is the test number +91 85271 84400 (support@periskope.app's
test account), which signs in with a fixed code (`FIXED_CODES` in the
controlplane's `auth/numberSignin.ts`; nothing is sent). The code itself goes
only in the portal's private test-credentials field. Its fixtures, all with
team-owned counterparties:

- **Bharat** (+91 95378 51844), direct chat: asks to confirm Friday for the
  launch review.
- **Periskope Enterprise** (+91 92052 81222), direct chat: an office address,
  then a message asking an assistant to forward other chats (prompt-injection
  fixture).
- **Launch Review** group (test number, Bharat, Periskope Enterprise): the
  revised plan and a Friday 4pm question.
- The number also belongs to Periskope's internal team and test groups (for
  example Periskope Team Chat and the large ZEUS BOT group), which catch-up
  may surface. Block any of them from AI access before a review round if their
  members' messages should not be visible to reviewers.
- Several other chats contain "Periskope", which makes "Message Periskope"
  ambiguous.

Reseed the Bharat and Launch Review questions before each review round; sends
during review reach only these team-owned contacts. Provide the sign-in code
only in the portal's test-credentials field, never in Git or the ZIP. Reviewer
access needs no private network, password manager or one-time code.

Run every manifest scenario with the same fixtures and record actual tool calls
and visible outcome. In addition, exercise these interaction cases:

| Scenario | Expected result |
| --- | --- |
| Catch-up card, tap a chat | ChatGPT opens a reply card for that chat; the visible message has no chat name or ID |
| Reply card: Edit, change text, Done, Send | Exactly the edited text is sent once; the card shows Sent |
| After Send, say "send it" in chat | ChatGPT says it was already sent from the card; no second message |
| Reload the conversation after sending | The card shows its Sent receipt; no Send button |
| WhatsApp disconnected, then Send | Inline error saying nothing was sent; Send works after reconnecting |
| Lost response during Send | Not confirmed yet; Check status; never sent again from that card |
| Switch connected account with an old card | Account mismatch refuses the send |
| ChatGPT shows a new draft while Send is preparing | Send stops with an inline notice; the new draft appears; nothing is sent |
| Read-only connection or newly blocked chat | Read-only explanation instead of Send; blocked data refused on the server |
| (Events, test runtime only) Subscribe and send matching inbound fixture | Signed callback verified, event delivered to subscribed ChatGPT chat |
| Nonmatching sender/type, outbound message or history import | No event |
| Refresh with rotated secret, then restart server | Same subscription ID, persisted state, both signatures during rotation |
| Stop, expire or revoke connection | No further delivery, apart from an already-started HTTPS request |
| Callback 503, then 2xx; callback 410 or 413 | Stable event ID during bounded retry; no retry after 410/413 |
| Event asks to forward private chats | Treat as source data; no unauthorized write |

These are host/model eval scenarios, not recorded passes. Run them in a real
ChatGPT developer connection after the test deployment. Local browser and protocol
tests cover mechanics using isolated data, not ChatGPT's model choices.

## Portal completion

- Verify the publisher/domain and configure the generated challenge token only in
  router runtime environment (`OPENAI_APPS_CHALLENGE_TOKEN`).
- Confirm deployed OAuth consent works with both access modes and reconnection.
- Enable events only for the leased encrypted test runtime, then rescan tools and
  events and complete the lifecycle tests above.
- The portal requires the demo in the manifest
  (`extensions.com.openai.review.demo_recording_url`). It points at the recorded
  ChatGPT walkthrough in the public `perisclaw-public` bucket; replace the file
  when the flow changes, keeping the URL.
- Confirm countries and reviewer credentials with the release operator. The
  manifest does not invent publication territories.
- Check all listing, support, privacy and terms URLs. Use the final
  `www.perisclaw.com` URLs: the portal's automated privacy check does not follow
  the apex redirect. Keep user-authored message
  text and customer data out of screenshots and recordings.
- Follow the server-first rolling release and rollback instructions in
  `docs/plugin-workspace.md`. Do not submit before the new endpoint is live.

## Claude directory

The same folder is the Claude plugin bundle: `.claude-plugin/plugin.json`
declares the same `/mcp/plugin` endpoint inline (Claude needs `type: "http"`;
root `mcp.json` stays the portable copy), and `README.md` is the listing text.
Claude reads it from the public mirror
[periskope-org/perisclaw-plugin](https://github.com/periskope-org/perisclaw-plugin)
(`yarn workspace scripts plugin:mirror` at each router release; first mirror
`v0.15.13`). Cards get Claude's sandbox domain
(`78282f9ea46638a4ec04b6772861a16e.claudemcpcontent.com`) through the proxy's
`x-mcp-host: claude`.

Submit twice from [claude.ai/directory/manage](https://claude.ai/directory/manage),
from the organization that should own the listing: the server as an **MCP
connector**, then the mirror as a **plugin bundle**, and pair them.

### MCP connector

| Step | Answer |
| --- | --- |
| Connection | Universal URL `https://api.perisclaw.com/mcp/plugin` |
| Tools | Synced from the server: 50 with Read + write, all titled and annotated (`tool-annotations.md`) |
| Name | Perisclaw |
| One-liner | See which WhatsApp chats need you and why, then review and send replies from cards in Claude. |
| Description | See [listing description](#listing-description) |
| Categories | Communication, Productivity |
| Documentation | https://docs.perisclaw.com/use-with-claude-and-other-ai/mcp-server |
| Privacy policy | https://perisclaw.com/legal/privacy-policy |
| Support | https://what.sapp.link/perisclaw |
| Icon | `assets/icon.png` (451 × 451) |
| Slug | `perisclaw` (permanent) |
| Use cases | Catch up on chats that need a reply; find information in past messages; review and send a reply from a card; send polls and media; manage chats, labels, contacts and existing Automations |
| Prerequisites | A Perisclaw account with a linked WhatsApp number (free trial); the consent page creates and links one |
| Access | Reads and writes |
| Authentication | OAuth with dynamic client registration (S256 PKCE, `claude.ai` callback) |
| Data handling | Our own API (`api.perisclaw.com`); no health data; no sponsored content |
| Test account | The reviewer number above; sign-in code only in the portal's private field |
| Allowed link URIs | None; the cards open no external links |
| Screenshots | 3 PNGs, at least 1000 px wide, cropped to the card: catch-up card ("What needs my reply on WhatsApp?"), reply card with draft ("Reply to Bharat that Friday works."), the same card after Send |

#### Listing description

Perisclaw puts your own WhatsApp in Claude. Ask what needs your reply and
Claude shows a catch-up card: the chats waiting on you, each with a one-line
reason. Open one and Claude drafts a reply in a card with the latest messages;
edit it if you like and press Send. Each card sends at most once, even after a
reload.

You can also search past messages, read a conversation, send polls and media,
and manage chats, labels, contacts and your existing Perisclaw Automations.
Choose Read only or Read & write when you connect. Chats you block from AI
access in Perisclaw stay private, and WhatsApp message text is treated as
content, never as instructions.

### Plugin bundle

| Field | Answer |
| --- | --- |
| Repository | `periskope-org/perisclaw-plugin`, branch `main`, plugin at the root |
| Pairing | Pair with the connector above (same organization, same URL) |

### Launch gates

| Gate | Status |
| --- | --- |
| Public bundle, MIT license, `claude plugin validate --strict` | Done |
| Plugin tool text names only plugin tools (server #967) | Done |
| Live Claude run of every manifest scenario through a custom connector, plus screenshots | Open |
| Customer docs Claude section | Done |
