# Conversion and design options

## The `pdf` parameter differs by tool

| Tool | `pdf` value |
| --- | --- |
| `heyzine_convert_attached_pdf` | File object from the current conversation |
| `heyzine_convert_pdf` | Public document URL string |
| `heyzine_convert_pdf_async` | Public document URL string |

Attached-file object shape:

```json
{
  "pdf": {
    "download_url": "https://.../signed-temporary-url",
    "file_id": "file_abc123",
    "mime_type": "application/pdf",
    "file_name": "report.pdf"
  }
}
```

`download_url` and `file_id` are required; `mime_type` and `file_name` should be
included when known. Take `download_url` from the current attachment; never
fabricate or reuse a signed URL.

All three tools accept PDF, DOC, DOCX, PPT, PPTX, ODT, ODP, and RTF documents.

## Shared design options

Accepted by all three conversion tools and by
`heyzine_update_flipbook_design`. Every field is optional. Send only fields
being set; omitted fields keep their current value on an update and use the
template or account default on a conversion.

### Content

| Parameter | Type | Notes |
| --- | --- | --- |
| `title` | string | Public title |
| `subtitle` | string | Public subtitle |
| `description` | string | Public description |
| `private_note` | string | Internal management note |
| `tags` | string | Comma-separated tags |

### Branding

| Parameter | Type | Notes |
| --- | --- | --- |
| `template` | string | Existing flipbook id or URL whose design is copied |
| `logo` | string | Public logo image URL; requires Standard or above |
| `background_color` | string | Hex without `#`, such as `000000` |
| `show_info` | boolean | Show the information panel |

### Reading experience

| Parameter | Type | Notes |
| --- | --- | --- |
| `page_effect` | string | `magazine`, `book`, `album`, `notebook`, `fade`, `cards`, `coverflow`, `flip`, `slideshow`, or `onepage` |
| `right_to_left` | boolean | Right-to-left reading order |
| `prev_next` | boolean | Show previous and next controls |
| `full_screen` | boolean | Show the fullscreen control |

`slideshow` is an alias of `fade`; `onepage` is an alias of `flip`. Never send
an effect outside this list. Set `right_to_left` only when the user asks or the
document language is clearly right-to-left, and report that choice.

### Sharing and distribution

| Parameter | Type | Notes |
| --- | --- | --- |
| `share` | boolean | Show the share control |
| `download` | boolean | Allow source document downloads |
| `url_path` | string | Custom path; requires custom-URL support |
| `url_domain` | string | Account custom domain; requires custom-URL support |

Changing `url_path` or `url_domain` changes the public link and breaks links
already shared. Confirm with the user first.

## Async conversion states

`heyzine_convert_pdf_async` returns a `state` field:

| State | Meaning |
| --- | --- |
| `started` | Conversion is running; call again with the same `pdf` URL |
| `processed` | Conversion finished and the response contains the flipbook |

`heyzine_convert_attached_pdf` and `heyzine_convert_pdf` block until the
conversion finishes. Conversion failures are tool errors; report the error and
do not silently retry with changed inputs.
