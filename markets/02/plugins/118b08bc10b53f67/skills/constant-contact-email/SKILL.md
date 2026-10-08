---
name: constant-contact-email
description: Create, preview, revise, score, and prepare Constant Contact email campaigns using this plugin's MCP tools. Use whenever the user asks to create an email, newsletter, or email campaign in Constant Contact. Also use for campaign previews, edits, subject-line scoring, and schedule-readiness checks. Do not use for social posts, contact management, or general email writing outside Constant Contact.
---

# Email Campaign Management

Quick reference for email campaign creation, preview, scheduling, and management operations.

## Email Preview Widget

The **Email Preview Widget** (`ui://public-api/email-preview.html`) is an interactive MCP UI component that displays the email campaign visually. It is automatically triggered by the MCP client whenever a tool returns an `EmailPreviewResponse`.

**Which tools trigger the widget automatically:**
- `create_email_campaign` — widget fires after creation; if the widget renders, do NOT call `get_campaign_html_preview` again
- `get_campaign_html_preview` — widget fires on every preview fetch

**Which tools do NOT trigger the widget:**
- `update_email_campaign_activity` — no widget metadata; always follow an update with a call to `get_campaign_html_preview` so the user can see the changes

The widget renders the email HTML in a sandboxed iframe with Constant Contact image CDN support. Do not attempt to render raw HTML yourself — always rely on the widget via the tool response.

## Campaign Brief Requirement

**Before creating a campaign**, collect the minimum brief unless the user explicitly requests a placeholder, starter draft, mockup, or says "just make something":

- **Goal** — What is the business objective of this email?
- **Audience** — Who are the recipients?
- **CTA** — What action should readers take?

Frame this as improving performance, not as a blocker. If immediate creation is required without a brief (demo/placeholder/mockup request), use reasonable assumptions and label the output as a best-effort draft.

## Campaign Naming

Campaign names must be **unique** (max 80 chars). Always append a timestamp or short unique suffix to generated drafts to prevent name collisions:

```
"Summer Sale 2026-09-17 14:32"
"Welcome Email – draft-a3f2"
```

## Success Verification

After `create_email_campaign` completes, verify the response includes **both**:
- `campaign_id` — the parent campaign ID
- `campaign_activity_id` — the activity ID needed for preview, update, and scheduling

Do not report success to the user until both IDs are confirmed present.


## User-Provided Images

Images used in campaign HTML should first be uploaded to Constant Contact
MyLibrary. Use the returned `external_url` in the `<img>` element; never use a
local filepath or temporary attachment path in campaign HTML.

### Upload procedure

1. Attempt to upload the original image using
   `upload_my_library_file`.
2. If the upload returns HTTP 400 or rejects a large PNG:
   - preserve the original file;
   - create an email-optimized copy;
   - convert it to JPEG unless transparency or animation is required;
   - resize it to a maximum dimension of approximately 1000–1200 pixels;
   - remove unnecessary metadata;
   - use JPEG quality around 80–85;
   - retry the upload using a `.jpg` filename, `file_type: "JPG"`, and a
     `data:image/jpeg;base64,...` URL.
3. Use the returned public `external_url` in the campaign.
4. If automated upload still fails, use the interactive image-upload tool or
   explain that the image could not be hosted. Do not silently omit an image
   the user explicitly requested.
  
## Core Workflows

### 1. Create Email Campaign

Create a new email campaign with HTML content.

```json
{
  "name": "Summer Sale 2026-09-17 14:32",
  "email_campaign_activities": [{
    "format_type": 5,
    "subject": "Your Summer Sale Starts Now",
    "preheader": "Exclusive deals inside — don't miss out",
    "html_content": "<html>...[[trackingImage]]...</html>"
  }]
}
```

**Key Fields:**
- `name`: Unique campaign name (max 80 chars) — always include a timestamp or suffix
- `format_type`: **Must be `5`** for custom HTML emails (Custom Code format)
- `html_content`: Must include `[[trackingImage]]` for open/click tracking and reporting
- `subject`, `preheader`: Required for deliverability and inbox preview
- `physical_address_in_footer`: Required for CAN-SPAM; omit to use account defaults
- `from_name`, `from_email`, `reply_to_email`: Omit to use account defaults

**Returns:** `EmailPreviewResponse` — the widget renders automatically. Confirm `campaign_id` and `campaign_activity_id` are present before reporting success.

### 2. Preview Email Campaign

Fetch an HTML preview manually. Use this only when:
- The widget did not render after `create_email_campaign`, or
- After calling `update_email_campaign_activity` (which does not auto-trigger the widget)


**Returns:** `EmailPreviewResponse` with `campaign_activity_id`, `campaign_id`, `from_email`, `from_name`, `reply_to_email`, `subject`, `preheader`, `preview_html_content` / `html_content`, `call_to_action`.

### 3. Update Email Campaign

Modify existing email campaign content and settings.

**All fields optional** — only specify fields to update. Note: `format_type` cannot be changed after creation.

**Important:** `update_email_campaign_activity` does not trigger the Email Preview Widget. Always call `get_campaign_html_preview` after updating so the user can see the result.

### 4. Check Schedule Readiness

Verify campaign status and get scheduling link.

**Returns:**
- `ready` (bool): `true` only when status is `DRAFT`
- `campaign_url`: Direct link to the schedule page in Constant Contact UI
- `current_status`: `DRAFT`, `SCHEDULED`, `EXECUTING`, `DONE`, `ERROR`, `UNKNOWN`
- `message`: Human-readable status explanation

**Status Meanings:**
| Status | Ready | Meaning |
|--------|-------|---------|
| DRAFT | ✓ Yes | Ready to schedule |
| SCHEDULED | ✗ No | Already scheduled |
| EXECUTING | ✗ No | Currently sending |
| DONE | ✗ No | Already sent (resend available) |
| ERROR | ✗ No | Fix before scheduling |

### 5. Analyze Subject Line

Score email subject line effectiveness.


**Returns:**
- `score`: 0–100 numeric score
- `feedback`: Descriptive analysis
- `marketing_results`: List of scoring factors with points
- `display_cta`: `true` if unauthenticated (shows sign-up CTA)

## HTML Content Requirements

### Tracking

Email HTML **must include** `[[trackingImage]]` for click tracking, open tracking, and reporting. Place it just before the closing `</body>` tag.

### format_type

Always pass `"format_type": 5` when providing custom HTML content. This selects the **Custom Code** format in Constant Contact. Omitting it may cause the API to reject the request.

### CAN-SPAM Compliance

`physical_address_in_footer` required fields:
- `address_line1`
- `country_code`
- `organization_name`

Omit the entire field to use the account's registered address.

### Field Defaults

If email fields are omitted, the tool automatically uses account defaults:
- `from_email` → account's default sender
- `from_name` → account's configured sender name
- `reply_to_email` → account's reply-to
- Physical address → account's registered address

## Common Patterns

### Full Workflow: Create → Preview → Schedule

1. Collect campaign brief (goal, audience, CTA) — skip only for demo/placeholder requests
2. **Create** with `create_email_campaign` using `format_type: 5` and a unique timestamped name
3. Confirm `campaign_id` and `campaign_activity_id` in the response
4. Widget renders automatically — do not call `get_campaign_html_preview` unless widget did not appear
5. **Check readiness** with `check_campaign_schedule_readiness` using the returned `campaign_activity_id`
6. If `ready=true`, present `campaign_url` so the user can schedule in Constant Contact UI

### Update After Preview

1. Widget shows an issue (typo, layout problem, wrong copy)
2. Update via `update_email_campaign_activity` with only the changed fields
3. Call `get_campaign_html_preview` to re-trigger the widget — user sees the corrected email


## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| `-32603` InternalError | Transient server error, often a name collision | **Retry once with a new unique name** (add/change timestamp suffix) before running broader diagnostics |
| `409 Conflict` | Campaign name already exists | Retry with a different unique name |
| `401 Unauthorized` | Missing or invalid token | Ask the user to authenticate |
| `404 Not Found` | Invalid `campaign_activity_id` | Verify the ID was captured from the creation response |
| `400 Bad Request` | Missing required fields | Ensure `format_type: 5`, `html_content` with `[[trackingImage]]`, and a valid `subject` are present |
| Timeout | Network or API delay | Retry once with exponential backoff |