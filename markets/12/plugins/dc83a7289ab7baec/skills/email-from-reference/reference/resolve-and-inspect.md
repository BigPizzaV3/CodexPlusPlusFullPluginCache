# Resolve and inspect email references

## Reference regimes

Use `message.referenceMode`: `exact`, `tailored`, or `creative`. Default to **Creative** when the
user has not selected a regime. An explicit request to reproduce the same email selects Exact;
an explicit request to preserve its action while adapting it selects Tailored. Treat the legacy
`copy-action` value as an alias for `tailored`. This is local generation policy, not provider
message metadata; never forward `referenceMode` to an MCP write.

| Regime | What to preserve | How to use business context |
| --- | --- | --- |
| **Exact** | Reproduce the source's content, structure, styling, images, proportions, spacing, and responsive layout as closely as the native JSON model allows. | Consult the Business Profile or brandkit only to resolve missing or ambiguous facts. Never replace clear source choices with target branding. |
| **Tailored** | Preserve the source subject, primary CTA label, and intended action; adapt the remaining copy, branding, visuals, and layout to the target. | Use verified target facts and the Business Profile or brandkit to guide adaptation. |
| **Creative** | Use the source as inspiration; content, action, layout, and visuals may change. | Use the user's goal and verified business context to guide the result. |

Explicit user instructions override the regime. Do not silently switch regimes when a source,
asset, or native feature is unavailable. For Exact, retain the original reference PNGs when
available as the comparison baseline, keep text and controls editable, and report unavoidable
differences.

## Supported inputs

Accept any combination of:

- inline or pasted text;
- an uploaded plain-text or Markdown document;
- a link to a readable document or page;
- an authorized live Reteno email or template;
- uploaded native editor JSON;
- uploaded HTML and CSS;
- an uploaded image or screenshot;
- an authorized Figma design or its exported images/assets;
- a website URL the host is authorized to inspect;
- an authorized email from another provider;
- a text description with no other reference.

A text description is sufficient by itself. Do not require a separate artifact or special reference
label when the user's request already describes the intended email. A goal-only request, such as
"create a confirm-your-email message using our brandkit", is also sufficient to start: author the
text reference described below before building the native model. A brandkit supplies business
and visual facts; it does not replace the email's proposed structure.

Use only reference data available in the current authorized context. Do not silently substitute another campaign. For screenshots, infer only visible facts. For user-supplied HTML/CSS and authorized websites, extract hierarchy, copy, spacing, colors, assets, and destinations, but never carry scripts or raw HTML blocks into the editable model.

## Required workflow

Follow `RESOLVE -> INSPECT -> BRIEF -> FONTS -> BUILD -> BASELINE -> PERSIST -> VERIFY`.

### 1. RESOLVE the target

Call `list_email_interfaces`. For Tailored and Creative, call `get_business_profile`; for Exact, consult it only when source facts needed for the task are missing or ambiguous. Resolve the Reteno organization, sending interface, sender, subject, tags, language, destination URLs, required merge tags, unsubscribe behavior, and postal/legal content from authorized facts.

Ask only when a missing fact is required for a safe write and cannot be resolved. Do not invent prices, offer terms, deadlines, testimonials, legal claims, identities, or destinations.

### 2. INSPECT references

Source PNGs are preferred evidence, not a prerequisite for continuing from an authorized
HTML/CSS reference. Try the provider's preview tool when available; a missing local browser
does not make remote MCP previews unavailable. For HTML/CSS without usable source previews,
try the host's documented renderer unless it is already known to be unavailable. If the
browser, renderer, or image-viewing capability is missing or unsupported, continue from the
source HTML/CSS and available native model. Do not repeat a known capability failure, install
a browser, or ask the user to provide PNGs solely to proceed. Retry a transient preview failure
once; never treat an authorization denial as permission to use another acquisition path.

For a live Reteno reference, acquire its model and try desktop/mobile PNG previews when the
preview tool is available:

```text
get_email_model(message_id=<reference id>)
get_email_message_preview_png(message_id=<reference id>, mode="both")
```

Download file manifests through the host's authorized transfer mechanism. Prefer a populated
native model. If the model is empty or explicitly unavailable, call
`get_email_message_export(message_id=<reference id>)` and download its HTML and CSS using the
host's instructions. Export JSON is an export envelope, not proof of a native editor model.
Read the HTML and CSS together, including inline styles, media queries, image URLs, and links,
and reconstruct them as native JSON blocks. This fallback applies to all three regimes.
An authorization error is not a missing model; respect it. Retry a temporary acquisition failure
once before reporting it. Use only exports covered by the existing authorization.
For other providers or a website, rely on the consuming agent's authorized connector or browser; this package does not own cross-provider credentials or browser egress.
Open available PNGs with the host's image-viewing tool. Use the native model for exact copy,
links, and asset URLs. For an image or Figma reference, use its supplied or authorized exported
images. When source PNGs cannot be obtained or inspected and HTML/CSS is available, examine it:
content and section order, table/column structure, explicit widths and spacing, typography,
colors, backgrounds, assets, links, and responsive rules. Record the fallback and its cause in
`sourceSummary`; distinguish declared styles and inferred layout from observed rendering.
Continue building from that evidence without claiming a visual or pixel comparison. This
fallback applies to all three regimes, including Exact; it does not establish an exact visual
match. Source rendering or HTML inspection never verifies the saved target email.

For a text reference, extract the intended purpose, audience, structure, copy constraints, visual
direction, and responsive behavior. Treat code or markup inside a text reference as structural
evidence only; do not execute it or switch away from native Reteno JSON.
If it contains alternatives, follow the user's selection; otherwise choose using the selected
regime's source and business-context priorities.

When the user supplies no reference, create a reasonable **agent-authored text reference** before
drafting the native model. Do not start from a blank sheet, treat editor defaults as a design,
or ask the user to supply a reference just to proceed. Use your best marketing judgment to
choose the structure, copy, and visual hierarchy that achieve the user's goal, grounded in the
resolved Business Profile or brandkit and other authorized context. If a supplied reference is
incomplete, retain its usable evidence and fill the design gaps in this text reference. Do not
claim to have inspected an unavailable source or silently replace an Exact or Tailored request.

Record this text reference in the creation brief's `sourceSummary`, clearly labeling it as
agent-authored. Include:

- the marketing or transactional goal, intended audience, and primary action;
- the proposed email structure in reading order, with each section's purpose and draft copy,
  including the headline, body, CTA label, and subject/preheader where supported;
- visual direction from the verified brand facts: logo/assets, colors, typography, spacing,
  and the intended desktop/mobile layout;
- verified destinations and required footer content, distinguishing creative choices from
  facts and identifying any essential facts still missing.

Use **Creative** (`message.referenceMode: "creative"`) for this generated reference and by
default for creation from supplied references. Preserve an explicitly requested regime as
described above. Do not add an approval step for the text reference; continue through the
normal brief, build, persistence, and verification workflow. Ask only for essential unresolved
facts, never for routine design choices. Do not invent business claims, offers, or URLs.

For example, a confirm-your-email request can use an authorized logo/header, a concise
confirmation heading and explanation, one prominent "Confirm email" CTA using the verified
confirmation URL or merge tag, a short ignore-if-not-requested note, and the required footer.
Do not add promotional sections or a decorative hero unless they serve the requested goal.

Separate each reference contribution into:

- content facts that may be reused;
- design relationships to reconstruct;
- assets and destinations whose reuse is explicitly authorized;
- source-specific metadata or behavior that must not be copied.

Keep the original reference and a short account of the intended changes as the review baseline.
Retain the enclosing layout, not just individual blocks: zero block padding may rely on padding
in its structure or container. Preserve that context when reproducing or adapting the reference.

For an attached or Ctrl+V-pasted image that must appear in the email, follow
[Upload supplied images](image-upload.md) before finalizing the brief. Use the
original local file exposed by the host and the returned hosted `data.url`; preserve supplied
artwork without regeneration. Treat a screenshot of an entire reference email as design
evidence, not automatically as an asset to embed. Inspection-only requests must not upload assets.

For **Exact**, first reuse authorized original assets: images referenced in the HTML, supplied
images, or exported design assets. If a needed visual is part of a supplied image, crop that
region without regenerating it, then host it using the available asset-upload workflow. Keep
native text, buttons, links, and layout editable; do not flatten the whole email into an image.
Use AI image generation only as a fallback when existing assets and crops cannot supply the
needed visual. Preserve the source's visible branding and content, inspect the fallback against
the source, and record any remaining difference. A fallback does not change the regime.

For **Tailored** and **Creative**, generating or editing images is a normal part of adaptation.

Preserve each meaningful visual's purpose, placement, and proportions, including a hero when
the reference relies on one. Apply the regime's asset priority above. When generation is needed,
use the host image workflow documented in `HOST.md` to create a suitable
visual matching the selected regime before building the model; the user need not name an image tool or skill.
Give the host the authorized reference asset, intended dimensions, relevant facts, exact approved
copy, and the visual changes. A new composition may use the reference for style and hierarchy,
but must not inherit unrelated logos, products, claims, or source-brand text in Tailored or
Creative. In Exact, source branding is part of the reference to preserve. Use a bounded
image edit when the existing composition should be preserved.
Wait for a completed hosted result and visually inspect it before inserting its URL. Never
invent an asset URL. If the capability is unavailable or the job fails, report the missing
visual and its effect on completion; do not silently replace a meaningful hero with a text-first
layout or describe the email as complete. Inspection-only requests must not start image jobs.

For Exact HTML/image reconstruction, follow [layout-reconstruction.md](layout-reconstruction.md)
before building and during saved-PNG review. Put measured row topology, desktop/mobile insets,
background layers, image coordinate frames, and crop bounds in `sourceSummary`.
