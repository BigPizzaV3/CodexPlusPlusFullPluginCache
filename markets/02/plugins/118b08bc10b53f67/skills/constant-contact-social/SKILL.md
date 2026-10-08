---
name: constant-contact-social
description: Create, preview, and manage Constant Contact social media post campaigns using this plugin's MCP tools. Use whenever the user asks to create a social post or update social campaigns. Do not use for email campaigns, contact management, or general social content outside Constant Contact.
---

# Social Post Campaign Management

Quick reference for creating, previewing, and updating social media post campaigns in Constant Contact.

## Social Preview Widget — CRITICAL REQUIREMENT

The **Social Preview Widget** (`ui://public-api/social-preview.html`) is an interactive MCP UI component that displays the social post visually before it goes live. It is automatically triggered by the MCP client whenever a tool returns a successful response.

**Which tools trigger the widget automatically:**
- `create_social_post` — widget fires after successful creation; wait for it to render before confirming
- `update_social_post` — widget fires after successful update; wait for it to render before confirming

The widget renders the post visually across multiple social platforms (Facebook, Instagram, LinkedIn, etc.) with proper formatting, images, and text. Do not attempt to describe the post manually — always rely on the widget.

### Scheduling via the Widget

**Posts are always created as `DRAFT`.** Scheduling is handled entirely through the social-preview widget UI, not through tool parameters.

Never pass `status="SCHEDULED"` or `scheduled_time` to the tools. Always create `DRAFT` and let the widget button handle the scheduling handoff.

## Campaign Creation Workflow

### 1. Create Social Post (DRAFT)

Create a new social media post in draft status (not yet published).

```json
{
  "profile_posts": [{
    "profiles": [],
    "text": "Check out our latest updates! 🎉",
    "images": [{"url": "https://imgur.com/abc123.jpg"}]
  }],
  "status": "DRAFT"
}
```

**Key Fields:**
- `profile_posts`: Required — list of post objects
  - `profiles`: List of `{profile_id: "..."}` objects — can be empty for DRAFT posts
  - `text`: Optional caption/text content (required for effective posts; use 2-3 sentences)
  - `images`: Optional list of image objects — **must use `[{"url": "..."}]` format, NOT flat strings or `media_urls`**
- `status`: Default `"DRAFT"` — post is not published
- `name`: Optional campaign name; auto-generated if omitted

**Image URLs:**
- Use fully qualified public URLs (e.g., `https://example.com/photo.jpg`)
- URL-encode each path component
- Supported: Social platform CDNs, imgur.com
- Not all CDN domains support CSP; if images don't load in preview, upload to Constant Contact or imgur

**Returns:** dict with `campaign_id`, `user_cta`, and widget metadata. **The social-preview widget renders automatically.** Wait for it to display before confirming creation.

### 2. Update Social Post

Modify an existing draft post.

```json
{
  "campaign_id": "camp_abc123",
  "profile_posts": [{
    "profiles": [],
    "text": "Updated post text goes here",
    "images": [{"url": "https://imgur.com/new_image.jpg"}]
  }]
}
```

**Fields:**
- `campaign_id`: Required — the ID from the creation response
- `profile_posts`: Optional — update post content and profiles
- `name`: Optional — rename the campaign

**All fields except `campaign_id` are optional.** Only specify fields to change.

**Returns:** dict with updated campaign data. **The social-preview widget renders automatically.** Verify the changes appear in the preview.

## Core Workflows

### Full Workflow: Create → Preview → Schedule

1. **Create** with `create_social_post` (always `DRAFT`)
2. **Wait for social-preview widget to render** — do not report completion until it appears
3. User reviews the preview — request edits if needed
4. When satisfied, user clicks the **Send button** in the widget to open the Constant Contact UI and schedule or publish

### Quick Edit: Modify a Draft

1. **Update** with new text, images, or profiles via `update_social_post`
2. **Wait for social-preview widget to render** — verify the changes
3. User clicks the **Send button** in the widget to proceed to scheduling

## Image Handling

### Best Practices

- **Prefer Constant Contact or imgur**. Images from these sources always render in preview.
- **For user-uploaded images**: For a chat-uploaded image, use a data URL with upload_my_library_file when available. If the image cannot be passed to the tool, call user_image_upload and let the user upload through the widget. Never pass a local filepath as the URL.
- **Test in preview**: The social-preview widget shows exactly how the post will appear on each platform (Facebook, Instagram, LinkedIn, etc.). If an image fails to load in preview, it will fail when published.

If the upload returns HTTP 400 or rejects a large PNG:
  - preserve the original file;
  - create an email-optimized copy;
  - convert it to JPEG unless transparency or animation is required;
  - resize it to a maximum dimension of approximately 1000–1200 pixels;
  - remove unnecessary metadata;
  - use JPEG quality around 80–85;
  - retry the upload using a `.jpg` filename, `file_type: "JPG"`, and a
     `data:image/jpeg;base64,...` URL.

### Format

Images **must** use the `images` array format with `url` objects:

```json
"images": [
  {"url": "https://imgur.com/photo1.jpg"},
  {"url": "https://imgur.com/photo2.jpg"}
]
```

**Incorrect formats** (these will cause errors):
```json
"images": ["https://imgur.com/photo1.jpg"]  // ❌ flat array
"media_urls": ["..."]  // ❌ wrong field name
```

## Response Format

Both `create_social_post` and `update_social_post` return a `dict` containing:

- `campaign_id`: Unique identifier for the campaign — **verify this is present before confirming success**
- `status`: Always `DRAFT` when created via this skill
- `profile_posts`: Current post content and profiles
- `user_cta`: `"send"` (authenticated — widget shows Send button) or `"signUp"` (unauthenticated — widget shows sign-up CTA)
- `name`: Campaign name
- Widget metadata (automatically triggers social-preview rendering)

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **Preview widget doesn't appear** | Network delay or widget not registered | Creation and update tools should return the social-preview UI resource. Do not create a second textual preview. If the response reports success, confirm creation and state that the preview should appear. If the tool returns no UI resource or reports an error, explain that the campaign may exist but its preview could not be displayed. |
| **Image fails to load in preview** | Unsupported CDN or CSP blocked | Use imgur or Constant Contact instead; upload via `upload_my_library_file` if needed |
| **"Campaign not found"** | Wrong `campaign_id` in update | Verify the ID from the creation response and use exact match |
| **Image upload returns HTTP 400** | Image may be too large or inefficiently encoded | Resize it, strip metadata, convert a non-transparent image to JPEG at roughly 80–85 quality, and retry once |

## Best Practices

### Effective Post Content

Before generating a substantive social post, ask for or infer:

* Goal
* Audience
* Desired action
* Target network/profile
* Brand tone
* Image or visual direction

## Error Handling — Widget Not Rendering

If the social-preview widget does not render after calling `create_social_post` or `update_social_post`:

1. **Do not report success** — the preview must be visible to confirm the post
2. Check the response for errors in the JSON-RPC result
3. If the response contains `campaign_id`, the campaign was created but the preview widget failed to render — try refreshing the client
4. If the response contains an error code (e.g., `400`, `401`, `404`), address the root cause:
   - `400 Bad Request`: Invalid `profile_posts` format or missing required field
   - `401 Unauthorized`: Authentication failed; user must sign in
   - `404 Not Found`: Campaign ID not found (for updates)
   - `-32603 Internal Error`: Transient server error; retry once with the same parameters

**Never skip the preview widget verification.** It is the user's visual confirmation that the post is ready for publication.
