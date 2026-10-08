# Reference

## Tool schemas

### `list_organizations`

No input.

```json
{
  "count": 1,
  "organizations": [
    { "id": 123, "name": "Acme Inc", "isActive": true, "isOwner": false, "isAdmin": true }
  ]
}
```

`count: 0` means the user only has a personal workspace.

### `list_ai_deck_styles`

| Field | Type | Notes |
|---|---|---|
| `organizationId` | int, optional | Omit for the personal workspace. |
| `format` | `presentation` \| `carousel`, optional | Always pass it. |

```json
{ "count": 2, "styles": [{ "id": "uuid", "name": "Acme — Sales", "format": "presentation" }] }
```

Only **completed** styles are listed, which makes this the poll endpoint for style readiness.

### `check_ai_credits`

| Field | Type | Notes |
|---|---|---|
| `organizationId` | int, optional | Omit for the personal workspace. |
| `resolution` | `1K` \| `2K` \| `4K`, optional | Defaults to `2K`. `4K` costs more. |
| `slideCount` | int 1–30, optional | When set, also returns `estimatedCost` and `hasEnoughCredits`. |

```json
{
  "workspace": "organization",
  "organizationId": 123,
  "totalCredits": 80,
  "creditsPerSlide": 5,
  "affordableSlides": 16,
  "canGenerateStyle": true,
  "resolution": "2K",
  "estimatedCost": 55,
  "hasEnoughCredits": true,
  "slideCount": 11
}
```

`canGenerateStyle` is true when the workspace can afford at least one slide. `estimatedCost` / `hasEnoughCredits` / `slideCount` are `null` when `slideCount` was omitted. Rates come from this tool — do not hardcode them.

### `generate_ai_deck_style`

| Field | Type | Notes |
|---|---|---|
| `source` | `topic` \| `url` | Required. |
| `topic` | string | Required when `source: "topic"`. Visual brief; truncated past 50 words. |
| `brandUrl` | string | Required when `source: "url"`. |
| `name` | string, optional | Name it so the style is reusable. |
| `organizationId` | int, optional | |
| `format` | `presentation` \| `carousel`, optional | Defaults to `presentation`. |

```json
{ "styleId": "uuid", "status": "generating" }
```

Asynchronous. The style is not usable until it appears in `list_ai_deck_styles`.

### `create_ai_deck`

| Field | Type | Notes |
|---|---|---|
| `prompt` | string | Required. The full content brief. |
| `styleSource` | `existing` \| `topic` \| `url` | Use `existing`. |
| `styleId` | string | Required with `existing`. |
| `brandUrl` | string | Required with `url`. |
| `styleName` | string, optional | Only for `topic` / `url`. |
| `format` | `presentation` \| `carousel`, optional | Must match the style. |
| `fileUrls` | string[], optional | Publicly reachable URLs, ingested server-side. |
| `slideCount` | int 1–30 \| `"auto"`, optional | Defaults to `auto`. |
| `language` | string, optional | Free text, e.g. `"Turkish"`. Auto-detected when omitted. |
| `resolution` | `1K` \| `2K` \| `4K`, optional | `4K` requires `organizationId`. |
| `organizationId` | int, optional | |

```json
{ "deckId": 987, "deckName": "…", "shareUrl": "https://…/nano/987", "status": "processing" }
```

`styleSource: "topic"` or `"url"` makes this call generate the style inline and block until it finishes, which can take minutes. Prefer generating the style separately so the user can approve it and reuse it.

### `get_ai_deck_status`

Input: `deckId` (int).

```json
{
  "deckId": 987,
  "deckName": "…",
  "status": "in_queue",
  "isTerminal": false,
  "slides": { "total": 12, "completed": 5, "failed": 0, "pending": 7 },
  "shareUrl": "https://…/nano/987"
}
```

`status` values: `in_queue`, `processing`, `final`, `errored`, `ready_for_transfer`. `shareUrl` appears once at least one slide has rendered. Trust `isTerminal` over `status`.

## Analytics tool schemas

Addressed by `deckId` alone — no `organizationId`, the workspace is read off the deck and checked against the user's deck permissions. AI Decks (nano-banana) only; any other editor returns `INVALID_EDITOR_VERSION` (400). None of these tools spend credits.

### `list_ai_decks`

| Field | Type | Notes |
|---|---|---|
| `search` | string, optional | Case-insensitive substring on the deck name. |
| `organizationId` | int, optional | Narrow to one organization. Omit to list personal **and** organization decks together. |
| `format` | `presentation` \| `carousel`, optional | |
| `limit` | int 1–50, optional | Defaults to 20. |
| `offset` | int ≥ 0, optional | Paging. |

```json
{
  "count": 1,
  "limit": 20,
  "offset": 0,
  "decks": [
    {
      "deckId": 987,
      "name": "Acme — Seed round",
      "format": "presentation",
      "status": "final",
      "organizationId": 42,
      "workspace": "organization",
      "editUrl": "https://…/nano/987/42",
      "updatedAt": "2026-08-30T09:12:00.000Z",
      "createdAt": "2026-08-21T14:03:00.000Z"
    }
  ]
}
```

Ordered by last activity, newest first. Errored decks are omitted. `editUrl` opens the editor — it is **not** a tracked share link.

### Shared analytics filters

`get_ai_deck_analytics` and `get_ai_deck_viewer_analytics` take the same four:

| Field | Type | Notes |
|---|---|---|
| `linkId` | string, optional | Count only visits through this share link. |
| `range` | `24h` \| `7d` \| `14d` \| `30d` \| `all`, optional | Defaults to `14d`. Ignored when `from`/`to` are given. |
| `from` | ISO 8601 string, optional | Overrides `range`. Bad dates return a 400 naming the field. |
| `to` | ISO 8601 string, optional | Overrides `range`. |
| `sinceLastEdit` | bool, optional | Drop visits recorded before the deck was last edited. |

`all` is anchored on the deck's creation date. Granularity is derived, not chosen: a span of 48 hours or less buckets by `hour`, anything longer by `day`. The trend compares against the immediately preceding window of the same length.

### `get_ai_deck_analytics`

| Field | Type | Notes |
|---|---|---|
| `deckId` | int | Required. |
| *filters* | | See above. |
| `viewerLimit` | int 1–100, optional | Defaults to 10, most recently active first. |
| `includeActivity` | bool, optional | Defaults true. False drops the time series. |
| `includeSlides` | bool, optional | Defaults true. False drops per-slide reach. |

```json
{
  "deck": { "deckId": 987, "name": "…", "format": "presentation", "slideCount": 11,
            "lastEditedAt": "2026-08-28T…", "editUrl": "https://…/nano/987" },
  "period": { "from": "…", "to": "…", "range": "14d", "granularity": "day", "sinceLastEdit": false },
  "filteredByLink": null,
  "summary": { "uniqueViewers": 12, "totalVisits": 19,
               "avgTimePerVisitSeconds": 214, "visitTrendPercent": 35.7 },
  "activity": { "granularity": "day", "truncated": false,
                "series": [{ "label": "Aug 24", "visits": 3 }] },
  "viewers": { "total": 12, "returned": 10, "items": [
    { "viewerId": "uuid", "name": "dana@acme.com", "email": "dana@acme.com",
      "location": "Berlin, Germany", "os": "macOS", "browser": "Chrome",
      "source": "Investors", "visits": 3, "totalTimeSeconds": 640, "lastSeenAt": "…" }
  ]},
  "slides": [{ "slideNumber": 1, "slideId": 1, "title": "…",
               "visits": 19, "seenPercent": 100, "avgDwellSeconds": 22 }],
  "links": [{ "id": "uuid", "name": "Investors", "shareCode": "abc123",
              "isActive": true, "isDefault": false }]
}
```

- `period.range` echoes `custom` whenever `from` or `to` was passed.
- `activity.series` is capped at 60 buckets, newest kept; `truncated: true` says older buckets were dropped.
- `viewers.total` is the full count in the period, `returned` is what `viewerLimit` allowed through.
- `name` falls back to the email, then to `Anonymous #n`. `source` is the share link name, else the UTM source, else `Direct`.
- `seenPercent` is that slide's visits over total visits — the point where it drops is the drop-off.
- A deck nobody opened returns zeros and empty arrays, not an error.

### `get_ai_deck_viewer_analytics`

| Field | Type | Notes |
|---|---|---|
| `deckId` | int | Required. |
| `viewerId` | string | Required. From the deck analytics `viewers.items`. |
| *filters* | | Same as above. |
| `visitLimit` | int 1–50, optional | Defaults to 10, newest first. |
| `includeSlideBreakdown` | bool, optional | Defaults true. |

```json
{
  "deckId": 987,
  "period": { "from": "…", "to": "…", "range": "14d", "sinceLastEdit": false },
  "viewer": { "viewerId": "uuid", "name": "dana@acme.com", "email": "dana@acme.com",
              "location": "Berlin, Germany", "os": "macOS", "browser": "Chrome",
              "source": "Investors", "visits": 3, "totalTimeSeconds": 640, "lastSeenAt": "…" },
  "visits": { "total": 3, "returned": 3, "items": [
    { "visitId": "uuid", "startedAt": "…", "durationSeconds": 260, "os": "macOS",
      "browser": "Chrome", "slidesViewed": 8, "exitedOnSlideNumber": 8,
      "slides": [{ "slideNumber": 1, "title": "…", "dwellSeconds": 18, "isExit": false }] }
  ]}
}
```

Slide numbers are 1-based. An unknown `viewerId` for that deck returns `NANO_BANANA_VIEWER_NOT_FOUND` (404).

### `list_ai_deck_share_links`

Input: `deckId` (int). Creates the deck's default link if it has none, so it is safe to call on an old deck.

```json
{
  "deckId": 987,
  "count": 2,
  "links": [
    { "id": "uuid", "name": "Default Link", "shareCode": "abc123",
      "shareUrl": "https://…/nano/987/present?code=abc123",
      "isActive": true, "isDefault": true, "emailOnFirstOpen": false,
      "viewCount": 14, "createdAt": "…" }
  ]
}
```

`viewCount` is counted from recorded visits, so it always agrees with the analytics screen. `shareUrl` is the **tracked** URL — the only one whose opens are attributed to a link.

### `create_ai_deck_share_link`

| Field | Type | Notes |
|---|---|---|
| `deckId` | int | Required. Needs write permission on the deck. |
| `name` | string ≤ 120, optional | The audience label. Shows up as `source` in analytics. |

Returns the same link shape plus a `message`. There is no cap on links per deck.

### `update_ai_deck_share_link`

| Field | Type | Notes |
|---|---|---|
| `deckId` | int | Required. |
| `shareLinkId` | string | Required. |
| `name` | string ≤ 120 \| null, optional | `null` clears it. |
| `isActive` | bool, optional | `false` revokes the URL; recorded visits stay. |
| `emailOnFirstOpen` | bool, optional | Stored only — see below. |

Omitted fields are untouched. The default link can be renamed and deactivated like any other.

`emailOnFirstOpen` records a preference and nothing reads it yet. Separately, the owner **is** emailed the first time each new viewer opens the deck — that behaviour is unconditional and is not what this flag controls. Do not promise the user that setting it changes their notifications.

### `delete_ai_deck_share_link`

Input: `deckId` (int), `shareLinkId` (string). Write permission. Soft delete: the URL stops resolving immediately, and visits already recorded through it keep their source in analytics. The default link cannot be deleted — `NANO_BANANA_DEFAULT_SHARE_LINK_UNDELETABLE` (400); deactivate it instead.

## What is and is not tracked

- Visits are recorded on the **present view** (`/nano/<deckId>/present`). Opening the editor deep link records nothing.
- A present view with no `code`, an unknown code, or a code from a deactivated link still counts — attributed as `Direct`. Losing attribution beats losing the visit.
- Visits are idempotent per session, so a viewer reconnecting does not inflate the count.
- Viewer identity comes from the viewer typing an email into the deck. Everyone else stays `Anonymous #n` forever.
- Location is IP-derived at city/country level; OS, browser, and device come from the user agent.
- A single slide is credited at most one hour of dwell per event batch, so a tab left open overnight cannot skew averages.

## Enums

| Enum | Values |
|---|---|
| Format | `presentation` (16:9), `carousel` (4:5) |
| Resolution | `1K`, `2K`, `4K` |
| Style status | `pending`, `processing`, `completed`, `failed`, `awaitingFinalization`, `awaitingPreviewApproval` |
| Deck status (`list_ai_decks`) | `in_queue`, `processing`, `final`, `errored`, `ready_for_transfer` |
| Analytics range | `24h`, `7d`, `14d` (default), `30d`, `all` |
| Analytics granularity | `hour` (span ≤ 48h), `day` — derived from the period, not an input |

`awaitingFinalization` means the workspace ran out of credits mid-pipeline; the style resumes automatically once credits are available and it is used again. `awaitingPreviewApproval` comes from the web app's preview step and is auto-approved on automated paths. Neither status appears in `list_ai_deck_styles`.

## Error handling

| Message contains | Meaning | Say and do |
|---|---|---|
| `Free users can only generate one style` | Free personal workspace already has a generated style of that source. | Offer to reuse the existing style, or to create inside an organization. |
| `Insufficient AI credits` | Workspace credit pool is empty. | Report the shortfall from `check_ai_credits`; suggest the organization workspace or a plan upgrade. Do not retry. |
| `4K` / resolution + organization | `4K` was requested without an organization. | Retry once at `2K`, or ask the user to pick an organization. |
| `NO_ORG_ACCESS` (403) | The user is not a member of that organization, or it is inactive. | Re-run `list_organizations` and re-ask. |
| `Style generation failed` | Style pipeline errored. | Offer a retry with a different brief or a brand URL. |
| `Style not found` (404) | Wrong `styleId`, or it belongs to another workspace. | Re-list styles with the correct `organizationId`. |
| `awaiting layout preview approval` | Style is parked in the web app's preview step. | Ask the user to approve the previews in Decktopus, or generate a fresh style. |
| Moderation / token limit | Prompt rejected or too long. | Rewrite shorter and neutral, then retry once. |
| `not an AI Deck (nano-banana)` | Analytics or share links asked for on a classic-editor deck. | Say that deck predates AI Decks and has no viewer analytics. Do not retry elsewhere. |
| `INVALID_EDITOR_VERSION` (400) | Same, raised from the service layer. | As above. |
| `NANO_BANANA_SHARE_LINK_NOT_FOUND` (404) | Wrong `linkId`/`shareLinkId`, or it belongs to another deck. | Re-run `list_ai_deck_share_links` for that deck and use an id it returned. |
| `NANO_BANANA_DEFAULT_SHARE_LINK_UNDELETABLE` (400) | Tried to delete the deck's default link. | Offer `update_ai_deck_share_link` with `isActive: false` instead. |
| `NANO_BANANA_VIEWER_NOT_FOUND` (404) | `viewerId` is not a viewer of that deck, or predates the period. | Re-read `get_ai_deck_analytics` and use a `viewerId` from its list. |
| `DATE_ERROR` / `must be an ISO 8601 date-time` (400) | `from`/`to` unparseable, or `from` is not before `to`. | Rebuild the window as full ISO timestamps, or fall back to `range`. |
| `DECK_NOT_FOUND` (404) | Wrong `deckId`, or the user has no access to it. | Re-run `list_ai_decks` and confirm the deck with the user. |

Never retry a credit or quota error, and never retry `create_ai_deck` after an ambiguous failure — poll status instead.

## REST fallback

Creation only. Used when MCP tools are unavailable. OAuth bearer token; `decks` scope for writes, `read` for organizations, styles, and credits.

**Analytics and share links have no OAuth REST fallback.** The `/api/nano-banana/deck/{deckId}/analytics`, `/analytics/viewers/{viewerId}` and `/share-links` endpoints exist, but they are session-authenticated app routes, not OAuth ones. If the analytics tools are unavailable, say so and point the user at the deck's analytics screen in Decktopus.

| Purpose | Request |
|---|---|
| List organizations | `GET /api/oauth/organizations` → `{ organizations: [{ id, name, is_active, is_admin, is_owner }] }` |
| Check credits | `GET /api/oauth/nano-banana/credits?organizationId=&resolution=&slideCount=` |
| List styles | `GET /api/oauth/nano-banana/styles?organizationId=&format=` |
| Upload a grounding file | `POST /api/oauth/nano-banana/file` (raw body, max 50 MB) → `{ fileId }` |
| Create a deck | `POST /api/oauth/nano-banana/deck` |

`POST /api/oauth/nano-banana/deck` body mirrors `create_ai_deck`: `prompt`, `styleSource`, `styleId`, `brandUrl`, `styleName`, `format`, `fileIds`, `fileUrls`, `slideCount`, `language`, `resolution`, `organizationId`, plus an optional `callbackUrl`. Without `callbackUrl` the request blocks until rendering finishes or times out; with it, the response returns immediately and the result is POSTed to the callback.

Accepted grounding file types: `csv`, `docx`, `json`, `md`, `pdf`, `pptx`, `txt`, `xlsx`, `xml`.

There is no OAuth endpoint for standalone style generation. Either reuse a style from the list, or let `styleSource: "topic" | "url"` generate one inside the deck call.
