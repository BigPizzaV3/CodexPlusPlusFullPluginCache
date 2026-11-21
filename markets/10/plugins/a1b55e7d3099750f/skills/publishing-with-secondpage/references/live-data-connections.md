# Live data connections

A Connection keeps a Page current from an approved source. Refresh runs deterministic transforms and rendering; no model runs in that loop. Supported source names are google_sheets, csv, ga4, stripe, airtable, notion, and http_api. Availability depends on deployment and organization; a recognized type is not proof it is enabled.

## Human handoff and safe discovery

Use list_connections to find an existing Connection. New Connections must be created by a person in SecondPage's Connections settings; MCP cannot create them. For an existing pending Connection, get_connection_schema returns the handoff_url for the human to authenticate, select the resource, or upload CSV. Never ask for credentials in chat. get_connection_schema returns the current safe configuration, resource_locator, typed columns, bounded samples and readiness. Reuse returned locators and real field names; do not guess IDs. A redacted locator or configuration needs human source selection, not an attempt to reconstruct secrets.

## Save, wait, preview

1. Configure the validated FetchSpec using resource, transforms, output.table and version. The examples below illustrate each source. Copy its real locator from get_connection_schema; adapt transforms only to observed columns.
2. Keep revision_id from configuration_saved. Saving is not a completed refresh. Changed remote specs queue one refresh by default. Identical retries reuse the revision. trigger_sync:false defers remote refresh; trigger_sync:true requests a refresh subject to the existing debounce and plan limits.
3. Call get_connection_schema with expected_revision_id. ready:true proves snapshot_revision_id matches that revision. connected:true alone only proves prior readable data. Respect retry_after_seconds; do not loop rapidly. If superseded, read the active configuration and reconcile. Unknown or failed state is not ready; follow the returned recovery.
4. Call preview_connection_render with connection_id, expected_revision_id and the HTML with markers. Pending, unknown and superseded revisions cannot preview successfully. Fix any marker warnings.
5. Read/export the target Page and publish the complete bundle with update_page, its matching base_version_id, and the same markers. Markers survive in the stored files; the server substitutes values on export/refresh.

CSV is upload-driven. A changed CSV spec waits for a fresh human upload at the returned handoff_url for that Connection. The fresh raw rows are transformed once under the active spec and stamped with its revision. There is no remote CSV credential worker and no retained raw dataset to repeatedly transform.

## FetchSpec examples

The following are executable schema examples with fixture IDs. They do not authorize or fetch these resources. Replace connection_id and resource with values returned by discovery. HTTP URLs must be credential-free HTTPS destinations; human handoff stores authentication separately. Version 1 supports select, rename, filter, sort, limit, format and derive. Version 2 additionally supports filter_multi, group_aggregate and window. Transforms run in array order.

### google-sheets

<!-- example:configure-google-sheets -->
```json
{"tool":"configure_connection_data","args":{"connection_id":"44444444-4444-4444-8444-444444444444","spec":{"version":1,"resource":{"resourceId":"spreadsheet_fixture","range":"Sheet1!A1:C50"},"transforms":[{"op":"limit","count":20}],"output":{"table":"summary"}}}}
```

### csv

<!-- example:configure-csv -->
```json
{"tool":"configure_connection_data","args":{"connection_id":"44444444-4444-4444-8444-444444444444","spec":{"version":1,"resource":{"resourceId":"44444444-4444-4444-8444-444444444444"},"transforms":[{"op":"limit","count":20}],"output":{"table":"summary"}}}}
```

### ga4

<!-- example:configure-ga4 -->
```json
{"tool":"configure_connection_data","args":{"connection_id":"44444444-4444-4444-8444-444444444444","spec":{"version":1,"resource":{"resourceId":"123456789","query":{"metrics":"sessions","dimensions":"date","startDate":"28daysAgo","endDate":"today"}},"transforms":[{"op":"limit","count":20}],"output":{"table":"summary"}}}}
```

### stripe

<!-- example:configure-stripe -->
```json
{"tool":"configure_connection_data","args":{"connection_id":"44444444-4444-4444-8444-444444444444","spec":{"version":1,"resource":{"resourceId":"charges","query":{"limit":"100"}},"transforms":[{"op":"limit","count":20}],"output":{"table":"summary"}}}}
```

### airtable

<!-- example:configure-airtable -->
```json
{"tool":"configure_connection_data","args":{"connection_id":"44444444-4444-4444-8444-444444444444","spec":{"version":1,"resource":{"resourceId":"appFixture","path":"tblFixture"},"transforms":[{"op":"limit","count":20}],"output":{"table":"summary"}}}}
```

### notion

<!-- example:configure-notion -->
```json
{"tool":"configure_connection_data","args":{"connection_id":"44444444-4444-4444-8444-444444444444","spec":{"version":1,"resource":{"resourceId":"55555555-5555-4555-8555-555555555555"},"transforms":[{"op":"limit","count":20}],"output":{"table":"summary"}}}}
```

### http-api

<!-- example:configure-http-api -->
```json
{"tool":"configure_connection_data","args":{"connection_id":"44444444-4444-4444-8444-444444444444","spec":{"version":1,"resource":{"resourceId":"https://example.com/data.json","path":"items"},"transforms":[{"op":"limit","count":20}],"output":{"table":"summary"}}}}
```

<!-- example:read-ready-revision -->
```json
{"tool":"get_connection_schema","args":{"connection_id":"44444444-4444-4444-8444-444444444444","expected_revision_id":"66666666-6666-4666-8666-666666666666"}}
```

<!-- example:preview-ready-revision -->
```json
{"tool":"preview_connection_render","args":{"connection_id":"44444444-4444-4444-8444-444444444444","expected_revision_id":"66666666-6666-4666-8666-666666666666","html":"<ul data-sp-repeat=\"summary\"><li><span data-sp-bind=\"name\"></span></li></ul>"}}
```

## Marker vocabulary (frozen for v1)

The renderer is a dumb stencil. It substitutes values; it computes nothing. All
logic, such as sort, filter, limit, format, and derive, lives in the fetch spec
transforms, never in markers. Every bound value is HTML-escaped (spreadsheet
cells are untrusted input).

| Marker | Meaning |
|---|---|
| `data-sp-bind="table.field"` | Replace the element's text content with the field value (escaped). |
| `data-sp-attr="src:table.image_url,href:table.link"` | Set attribute(s) from fields. Values escaped; `href`/`src` are validated http(s) only. Comma-separated `attr:target` pairs. |
| `data-sp-class="table.row_class"` | Append spec-computed class token(s); validated `[a-z0-9_-]+`. |
| `data-sp-repeat="table"` | The element is a row template. It is cloned once per row. Descendants bind row-relative: bare `data-sp-bind="field"` resolves against the repeat's table. |
| `data-sp-empty="table"` | Shown only when the table has zero rows. Place it as a sibling of the repeat. |
| `data-sp-updated` | Optional placeholder for the freshness badge. If absent, the renderer injects a default badge unless the page setting disables it. |

Reserved and inert in v1 (write-back fast-follow): `data-sp-form`,
`data-sp-write`. Do not use them yet.

### Rules that keep the render predictable

- Inside a `data-sp-repeat`, use bare field names (`data-sp-bind="dish"`), not
  qualified ones. Outside a repeat, always qualify (`data-sp-bind="menu.title"`).
- Nested `data-sp-repeat` is unsupported in v1; the inner one is left inert.
- A marker that references a table or field the snapshot does not have is left
  inert and surfaces a warning in `preview_connection_render`, never an error.
  The render is total and never throws, so a malformed marker degrades quietly
  rather than breaking the page.
- Only safe attributes are settable via `data-sp-attr`; `href`/`src` must resolve
  to http(s). Unsafe attributes and URLs are dropped with a warning.

### Example: a menu repeat

```html
<ul data-sp-repeat="menu">
  <li>
    <span data-sp-bind="dish"></span>
    <span data-sp-bind="price"></span>
    <img data-sp-attr="src:photo_url" alt="" />
  </li>
</ul>
<p data-sp-empty="menu">The menu is being updated.</p>
```

Pair this with a fetch spec whose `output.table` is `menu` and whose transforms
format `price` (for example, `format` to currency) and sort the rows. Run
`preview_connection_render` and confirm `bound_tables` includes `menu` and there
are no `unknown_field` warnings before you publish.
