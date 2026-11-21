# Print Ready service menu

Version 0.7.45. This is the tool menu advertised by the running MCP server.

All tool calls use POST /mcp with JSON-RPC method tools/call and params.name plus params.arguments.
GET /tools returns the same descriptions, input schemas and annotations as MCP tools/list. GET /menu returns this readable reference.

OpenSCAD uses millimetres. +Z is up, front is viewed from -Y, and right from +X.
STL export happens automatically when create_model completes. get_model returns fresh STL, PNG and manifest download links. Set include_source=true to retrieve editable SCAD only when the user asks. Downloads last at most ten minutes; ask get_model for new links.

## Connection and render allowance

If the user did not select an App or environment, prefer a registered Print Ready App for the full workflow. Check get_capabilities for its sign-in state. The App and a direct MCP route can have different account states. Never copy OAuth tokens between tools or infer account identity from host metadata.

Preserve render_quota_token from the signed-in App or preparation. Pass it with preparation, creation and camera-view calls if the workflow uses another authorized route in the same environment. It carries the account allowance only. Refresh expired quota context through the existing connection. Guests receive 250 render and camera jobs per UTC day. Signed-in accounts receive 2,000, and the verified owner has no limit. Polling, viewer inspection and downloads do not count.

When the allowance is exhausted, preserve the source and model handles. Check the existing App for an authorized signed-in allowance before asking the user to sign in again. If a revision exists only locally, tell the user which version the hosted viewer shows.

## Renders and exports

create_model compiles complete source and returns a 640 x 640 PNG sheet. Upper left is isometric, upper right front, lower left top, lower right right.
render_view returns a 320 x 320 PNG for isometric, front, back, left, right, top, bottom, custom or bed_contact. It reuses the compiled STL and returns the same source/STL geometry in that view job.
Custom azimuth runs from -360 to 360 degrees and defaults to -45. Zero points from +X and positive angles turn toward +Y. Elevation runs from -90 to 90 and defaults to 35. Zero is level, +90 is top, -90 is bottom. Camera fitting is automatic.
bed_contact shows the footprint within 0.05 mm of the minimum Z of the source geometry. It does not alter the STL or prove adhesion.
The sheet is automatic at model creation, not a render_view choice. Resolution, lighting and material color are fixed. render_view supports orthographic zoom from 0.25 to 2, default 1. Larger values enlarge the model and may crop it. create_3mf packages ready STL models with named parts and materials. create_colored_relief combines PNG palette refinement, tracing, height bands and print files in one job. refine_artwork and trace_artwork expose the stages separately. For relief design, run host ImageGen first with the skill prompt and any reference image. Submit the generated print-face PNG. Submit a separate SCAD cutaway variant for a section plane.

## Modeling references

get_print_ready_skill, get_colored_reliefs_skill, get_openscad_cheatsheet, get_bosl2_cheatsheet and get_welcome_skill return the same authored skills packaged with the plugin. get_capabilities advertises them. These read-only tools do not open the welcome screen. Show the guide only on requested help.

## Tools

### get_capabilities

Get this connection's environment, release version, deployed SHA, endpoint, rendering limits, libraries, reference skill tools and signed-in state. When the user selects an App or environment, call this tool on that connection first. If it is unavailable or reports a different environment, tell the user and stop before rendering. Keep all model operations on the verified connection.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Print Ready capabilities","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| include_welcome | no | See the exact schema below. |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "include_welcome": {
      "type": "boolean"
    },
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    }
  },
  "additionalProperties": false
}
~~~

### get_print_ready_skill

Return the current Print Ready modeling workflow, print guidance and delivery instructions. Read-only reference; does not render a part or open the welcome screen.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Read Print Ready modeling skill","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### get_colored_reliefs_skill

Read the required ImageGen workflow and limited-palette prompt for signs, nameplates, birthday placards, logos, magnets, ornaments and other shallow artwork. Read this before starting a relief. Pass any supplied reference into ImageGen.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Colored reliefs skill","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### get_openscad_cheatsheet

Return the OpenSCAD language skill and the downloaded cheatsheet in Markdown with the original documentation links and attribution. Read-only reference; no render or welcome screen.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Read OpenSCAD cheatsheet","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### get_bosl2_cheatsheet

Return the BOSL2 skill and practical reference for the pinned library, including includes, anchors, attachments, threads and gears with upstream documentation links. Read-only reference; no render or welcome screen.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Read BOSL2 cheatsheet","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### get_welcome_skill

Return the optional welcome-guide instructions as text. Use show_welcome only when the user asks for help using Print Ready, examples or the guide. Reading this skill does not display that screen.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Read welcome skill","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### whoami

Return the stable opaque profile represented by the validated connection credentials. A signed-in account includes its verified email when available. A guest connection returns its persistent guest profile with the label Not signed in and no email; it has no private account access. Use get_capabilities to check sign-in state without prompting. No user ID or email argument is accepted.

Connection required; guest connections are supported.
Annotations: {"title":"Connected Print Ready account","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### prepare_model

Prepare a new model handle and retry key on the verified Print Ready connection. Preserve the returned access and erasure tokens privately with the handle. Preserve render_quota_token and pass it to queued modeling tools and render_view.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Prepare model","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    }
  },
  "additionalProperties": false
}
~~~

### create_model

Create a printable part from complete OpenSCAD source, a required detailed English brief and required design decisions. Compiles a binary STL in source orientation and a 640 x 640 sheet of real isometric/front/top/right previews. Returns a queued job handle; poll get_model for status, intent, images and STL/PNG/manifest downloads; request SCAD only when the user asks. Reuse identical source, brief, decisions and tokens for retries. A new revision uses a new preparation. Link revisions with previous_model and other parts in this conversation with context_model. To package ready STL models with material colors, call create_3mf.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Render model","readOnlyHint":false,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |
| context_model | no | An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context. |
| previous_model | no | For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access. |
| imagegen_used | no | Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown. |
| name | yes | Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly. |
| source | yes | Complete OpenSCAD source in millimetres, at most 180000 UTF-8 bytes. BOSL2 is available. Model in the intended print orientation with the bed face at Z=0. |
| brief | yes | Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages. |
| decisions | yes | Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant. |
| idempotency_key | yes | Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key. |
| access_token | yes | Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle. |
| erasure_token | yes | Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    },
    "context_model": {
      "description": "An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "previous_model": {
      "description": "For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "imagegen_used": {
      "description": "Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown.",
      "type": "boolean"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100,
      "description": "Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly."
    },
    "source": {
      "type": "string",
      "minLength": 1,
      "maxLength": 180000,
      "description": "Complete OpenSCAD source in millimetres, at most 180000 UTF-8 bytes. BOSL2 is available. Model in the intended print orientation with the bed face at Z=0."
    },
    "brief": {
      "type": "string",
      "minLength": 40,
      "maxLength": 10000,
      "description": "Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages."
    },
    "decisions": {
      "minItems": 1,
      "maxItems": 30,
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "maxLength": 2000
      },
      "description": "Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant."
    },
    "idempotency_key": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9_-]{16,100}$",
      "description": "Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key."
    },
    "access_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle."
    },
    "erasure_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately."
    }
  },
  "required": [
    "name",
    "source",
    "brief",
    "decisions",
    "idempotency_key",
    "access_token",
    "erasure_token"
  ],
  "additionalProperties": false
}
~~~

### refine_artwork

Flatten printable PNG artwork to the supplied or selected palette. For loaded filament colors, pass palette. Use color_map only for deliberate substitutions. Inspect the flattened PNG from get_model before building when the print colors differ from the source. Call prepare_model first and pass the ready handle as artwork to trace_artwork or create_colored_relief.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Refine artwork","readOnlyHint":false,"destructiveHint":false,"openWorldHint":true}

| Parameter | Required | Description |
| --- | --- | --- |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |
| context_model | no | An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context. |
| previous_model | no | For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access. |
| imagegen_used | no | Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown. |
| name | yes | Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly. |
| brief | yes | Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages. |
| decisions | yes | Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant. |
| idempotency_key | yes | Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key. |
| access_token | yes | Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle. |
| erasure_token | yes | Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately. |
| file | no | Host file parameter for a printable PNG. For the relief design workflow, use the ImageGen output. |
| image_url | no | Reachable HTTPS URL or PNG data URL for the printable artwork. Send only the art to be traced. |
| artwork | no | Handle from refine_artwork or trace_artwork, with guest access token if needed. |
| palette | no | Ordered #RRGGBB filament colors. First is the base. Use the loaded colors when specified. Unmatched regions require an intentional color_map. Omit to select colors from the image. |
| color_map | no | Intentional source-to-filament substitutions. Each source is a distinct #RRGGBB from the artwork. Each target is in palette. Omit to preserve the artwork colors. |
| colors | no | Maximum number of automatically selected colors, including the base. Default 4. |
| footprint | no | Rectangle fills transparent pixels with the base color. Silhouette keeps transparent areas open. |
| cleanup | no | Clean small color artifacts when selecting colors automatically. Defaults to true for new images. |
| resolution_px | no | Longest edge of the tracing grid in pixels. Defaults to 480. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    },
    "context_model": {
      "description": "An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "previous_model": {
      "description": "For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "imagegen_used": {
      "description": "Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown.",
      "type": "boolean"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100,
      "description": "Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly."
    },
    "brief": {
      "type": "string",
      "minLength": 40,
      "maxLength": 10000,
      "description": "Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages."
    },
    "decisions": {
      "minItems": 1,
      "maxItems": 30,
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "maxLength": 2000
      },
      "description": "Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant."
    },
    "idempotency_key": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9_-]{16,100}$",
      "description": "Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key."
    },
    "access_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle."
    },
    "erasure_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately."
    },
    "file": {
      "type": "object",
      "properties": {
        "download_url": {
          "type": "string",
          "maxLength": 8000,
          "format": "uri"
        },
        "file_id": {
          "type": "string",
          "maxLength": 512
        },
        "mime_type": {
          "type": "string",
          "maxLength": 128
        },
        "file_name": {
          "type": "string",
          "maxLength": 512
        }
      },
      "required": [
        "download_url",
        "file_id"
      ],
      "additionalProperties": false,
      "description": "Host file parameter for a printable PNG. For the relief design workflow, use the ImageGen output."
    },
    "image_url": {
      "description": "Reachable HTTPS URL or PNG data URL for the printable artwork. Send only the art to be traced.",
      "type": "string",
      "maxLength": 5700000
    },
    "artwork": {
      "description": "Handle from refine_artwork or trace_artwork, with guest access token if needed.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
          "description": "Model or view job UUID returned by the service."
        },
        "access_token": {
          "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "palette": {
      "description": "Ordered #RRGGBB filament colors. First is the base. Use the loaded colors when specified. Unmatched regions require an intentional color_map. Omit to select colors from the image.",
      "minItems": 1,
      "maxItems": 16,
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^#[0-9a-fA-F]{6}$"
      }
    },
    "color_map": {
      "description": "Intentional source-to-filament substitutions. Each source is a distinct #RRGGBB from the artwork. Each target is in palette. Omit to preserve the artwork colors.",
      "minItems": 1,
      "maxItems": 16,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source": {
            "type": "string",
            "pattern": "^#[0-9a-fA-F]{6}$"
          },
          "target": {
            "type": "string",
            "pattern": "^#[0-9a-fA-F]{6}$"
          }
        },
        "required": [
          "source",
          "target"
        ],
        "additionalProperties": false
      }
    },
    "colors": {
      "description": "Maximum number of automatically selected colors, including the base. Default 4.",
      "type": "integer",
      "minimum": 1,
      "maximum": 16
    },
    "footprint": {
      "description": "Rectangle fills transparent pixels with the base color. Silhouette keeps transparent areas open.",
      "type": "string",
      "enum": [
        "rectangle",
        "silhouette"
      ]
    },
    "cleanup": {
      "description": "Clean small color artifacts when selecting colors automatically. Defaults to true for new images.",
      "type": "boolean"
    },
    "resolution_px": {
      "description": "Longest edge of the tracing grid in pixels. Defaults to 480.",
      "type": "integer",
      "minimum": 64,
      "maximum": 720
    }
  },
  "required": [
    "name",
    "brief",
    "decisions",
    "idempotency_key",
    "access_token",
    "erasure_token"
  ],
  "additionalProperties": false
}
~~~

### trace_artwork

Convert PNG artwork or a ready refine_artwork handle into layered vector outlines. Call prepare_model first. Poll get_model for the flattened preview, SVG and contour JSON. Pass this job as artwork to create_colored_relief.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Trace artwork","readOnlyHint":false,"destructiveHint":false,"openWorldHint":true}

| Parameter | Required | Description |
| --- | --- | --- |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |
| context_model | no | An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context. |
| previous_model | no | For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access. |
| imagegen_used | no | Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown. |
| name | yes | Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly. |
| brief | yes | Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages. |
| decisions | yes | Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant. |
| idempotency_key | yes | Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key. |
| access_token | yes | Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle. |
| erasure_token | yes | Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately. |
| file | no | Host file parameter for a printable PNG. For the relief design workflow, use the ImageGen output. |
| image_url | no | Reachable HTTPS URL or PNG data URL for the printable artwork. Send only the art to be traced. |
| artwork | no | Handle from refine_artwork or trace_artwork, with guest access token if needed. |
| palette | no | Ordered #RRGGBB filament colors. First is the base. Use the loaded colors when specified. Unmatched regions require an intentional color_map. Omit to select colors from the image. |
| color_map | no | Intentional source-to-filament substitutions. Each source is a distinct #RRGGBB from the artwork. Each target is in palette. Omit to preserve the artwork colors. |
| colors | no | Maximum number of automatically selected colors, including the base. Default 4. |
| footprint | no | Rectangle fills transparent pixels with the base color. Silhouette keeps transparent areas open. |
| cleanup | no | Clean small color artifacts when selecting colors automatically. Defaults to true for new images. |
| resolution_px | no | Longest edge of the tracing grid in pixels. Defaults to 480. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    },
    "context_model": {
      "description": "An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "previous_model": {
      "description": "For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "imagegen_used": {
      "description": "Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown.",
      "type": "boolean"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100,
      "description": "Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly."
    },
    "brief": {
      "type": "string",
      "minLength": 40,
      "maxLength": 10000,
      "description": "Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages."
    },
    "decisions": {
      "minItems": 1,
      "maxItems": 30,
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "maxLength": 2000
      },
      "description": "Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant."
    },
    "idempotency_key": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9_-]{16,100}$",
      "description": "Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key."
    },
    "access_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle."
    },
    "erasure_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately."
    },
    "file": {
      "type": "object",
      "properties": {
        "download_url": {
          "type": "string",
          "maxLength": 8000,
          "format": "uri"
        },
        "file_id": {
          "type": "string",
          "maxLength": 512
        },
        "mime_type": {
          "type": "string",
          "maxLength": 128
        },
        "file_name": {
          "type": "string",
          "maxLength": 512
        }
      },
      "required": [
        "download_url",
        "file_id"
      ],
      "additionalProperties": false,
      "description": "Host file parameter for a printable PNG. For the relief design workflow, use the ImageGen output."
    },
    "image_url": {
      "description": "Reachable HTTPS URL or PNG data URL for the printable artwork. Send only the art to be traced.",
      "type": "string",
      "maxLength": 5700000
    },
    "artwork": {
      "description": "Handle from refine_artwork or trace_artwork, with guest access token if needed.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
          "description": "Model or view job UUID returned by the service."
        },
        "access_token": {
          "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "palette": {
      "description": "Ordered #RRGGBB filament colors. First is the base. Use the loaded colors when specified. Unmatched regions require an intentional color_map. Omit to select colors from the image.",
      "minItems": 1,
      "maxItems": 16,
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^#[0-9a-fA-F]{6}$"
      }
    },
    "color_map": {
      "description": "Intentional source-to-filament substitutions. Each source is a distinct #RRGGBB from the artwork. Each target is in palette. Omit to preserve the artwork colors.",
      "minItems": 1,
      "maxItems": 16,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source": {
            "type": "string",
            "pattern": "^#[0-9a-fA-F]{6}$"
          },
          "target": {
            "type": "string",
            "pattern": "^#[0-9a-fA-F]{6}$"
          }
        },
        "required": [
          "source",
          "target"
        ],
        "additionalProperties": false
      }
    },
    "colors": {
      "description": "Maximum number of automatically selected colors, including the base. Default 4.",
      "type": "integer",
      "minimum": 1,
      "maximum": 16
    },
    "footprint": {
      "description": "Rectangle fills transparent pixels with the base color. Silhouette keeps transparent areas open.",
      "type": "string",
      "enum": [
        "rectangle",
        "silhouette"
      ]
    },
    "cleanup": {
      "description": "Clean small color artifacts when selecting colors automatically. Defaults to true for new images.",
      "type": "boolean"
    },
    "resolution_px": {
      "description": "Longest edge of the tracing grid in pixels. Defaults to 480.",
      "type": "integer",
      "minimum": 64,
      "maximum": 720
    }
  },
  "required": [
    "name",
    "brief",
    "decisions",
    "idempotency_key",
    "access_token",
    "erasure_token"
  ],
  "additionalProperties": false
}
~~~

### create_colored_relief

Refine printable PNG artwork, trace it and build a colored relief in one job. For a user's relief design, read get_colored_reliefs_skill and run host ImageGen first. Pass any reference image to ImageGen and submit only the generated illustration or an artwork handle derived from it. Pass the ordered filament palette including the base. Call prepare_model first, poll get_model and compare the top preview with the artwork. Use show_model for the STL and 3MF downloads.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Create colored relief","readOnlyHint":false,"destructiveHint":false,"openWorldHint":true}

| Parameter | Required | Description |
| --- | --- | --- |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |
| context_model | no | An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context. |
| previous_model | no | For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access. |
| imagegen_used | no | Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown. |
| name | yes | Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly. |
| brief | yes | Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages. |
| decisions | yes | Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant. |
| idempotency_key | yes | Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key. |
| access_token | yes | Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle. |
| erasure_token | yes | Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately. |
| file | no | Host file parameter for a printable PNG. For the relief design workflow, use the ImageGen output. |
| image_url | no | Reachable HTTPS URL or PNG data URL for the printable artwork. Send only the art to be traced. |
| artwork | no | Handle from refine_artwork or trace_artwork, with guest access token if needed. |
| palette | no | Ordered #RRGGBB filament colors. First is the base. Use the loaded colors when specified. Unmatched regions require an intentional color_map. Omit to select colors from the image. |
| color_map | no | Intentional source-to-filament substitutions. Each source is a distinct #RRGGBB from the artwork. Each target is in palette. Omit to preserve the artwork colors. |
| colors | no | Maximum number of automatically selected colors, including the base. Default 4. |
| footprint | no | Rectangle fills transparent pixels with the base color. Silhouette keeps transparent areas open. |
| cleanup | no | Clean small color artifacts when selecting colors automatically. Defaults to true for new images. |
| resolution_px | no | Longest edge of the tracing grid in pixels. Defaults to 480. |
| format | yes | Bambu Studio filament assignments, or standard 3MF materials and build items. |
| bed_center_mm | no | Placement center for Bambu Studio, in mm. Defaults to [128,128]. |
| layer_height_mm | no | Layer height in millimetres. |
| first_layer_height_mm | no | Layer height in millimetres. |
| width_mm | yes | Finished width in millimetres. Height follows the source aspect ratio. |
| band_layers | no | Number of print layers per palette color. Default 8 base layers and 4 layers for each raised color. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    },
    "context_model": {
      "description": "An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "previous_model": {
      "description": "For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "imagegen_used": {
      "description": "Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown.",
      "type": "boolean"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100,
      "description": "Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly."
    },
    "brief": {
      "type": "string",
      "minLength": 40,
      "maxLength": 10000,
      "description": "Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages."
    },
    "decisions": {
      "minItems": 1,
      "maxItems": 30,
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "maxLength": 2000
      },
      "description": "Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant."
    },
    "idempotency_key": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9_-]{16,100}$",
      "description": "Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key."
    },
    "access_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle."
    },
    "erasure_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately."
    },
    "file": {
      "type": "object",
      "properties": {
        "download_url": {
          "type": "string",
          "maxLength": 8000,
          "format": "uri"
        },
        "file_id": {
          "type": "string",
          "maxLength": 512
        },
        "mime_type": {
          "type": "string",
          "maxLength": 128
        },
        "file_name": {
          "type": "string",
          "maxLength": 512
        }
      },
      "required": [
        "download_url",
        "file_id"
      ],
      "additionalProperties": false,
      "description": "Host file parameter for a printable PNG. For the relief design workflow, use the ImageGen output."
    },
    "image_url": {
      "description": "Reachable HTTPS URL or PNG data URL for the printable artwork. Send only the art to be traced.",
      "type": "string",
      "maxLength": 5700000
    },
    "artwork": {
      "description": "Handle from refine_artwork or trace_artwork, with guest access token if needed.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
          "description": "Model or view job UUID returned by the service."
        },
        "access_token": {
          "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "palette": {
      "description": "Ordered #RRGGBB filament colors. First is the base. Use the loaded colors when specified. Unmatched regions require an intentional color_map. Omit to select colors from the image.",
      "minItems": 1,
      "maxItems": 16,
      "type": "array",
      "items": {
        "type": "string",
        "pattern": "^#[0-9a-fA-F]{6}$"
      }
    },
    "color_map": {
      "description": "Intentional source-to-filament substitutions. Each source is a distinct #RRGGBB from the artwork. Each target is in palette. Omit to preserve the artwork colors.",
      "minItems": 1,
      "maxItems": 16,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source": {
            "type": "string",
            "pattern": "^#[0-9a-fA-F]{6}$"
          },
          "target": {
            "type": "string",
            "pattern": "^#[0-9a-fA-F]{6}$"
          }
        },
        "required": [
          "source",
          "target"
        ],
        "additionalProperties": false
      }
    },
    "colors": {
      "description": "Maximum number of automatically selected colors, including the base. Default 4.",
      "type": "integer",
      "minimum": 1,
      "maximum": 16
    },
    "footprint": {
      "description": "Rectangle fills transparent pixels with the base color. Silhouette keeps transparent areas open.",
      "type": "string",
      "enum": [
        "rectangle",
        "silhouette"
      ]
    },
    "cleanup": {
      "description": "Clean small color artifacts when selecting colors automatically. Defaults to true for new images.",
      "type": "boolean"
    },
    "resolution_px": {
      "description": "Longest edge of the tracing grid in pixels. Defaults to 480.",
      "type": "integer",
      "minimum": 64,
      "maximum": 720
    },
    "format": {
      "default": "bambu",
      "description": "Bambu Studio filament assignments, or standard 3MF materials and build items.",
      "type": "string",
      "enum": [
        "bambu",
        "standard"
      ]
    },
    "bed_center_mm": {
      "description": "Placement center for Bambu Studio, in mm. Defaults to [128,128].",
      "type": "array",
      "prefixItems": [
        {
          "type": "number",
          "minimum": -2000,
          "maximum": 2000
        },
        {
          "type": "number",
          "minimum": -2000,
          "maximum": 2000
        }
      ],
      "items": false,
      "minItems": 2,
      "maxItems": 2
    },
    "layer_height_mm": {
      "type": "number",
      "minimum": 0.05,
      "maximum": 1,
      "description": "Layer height in millimetres."
    },
    "first_layer_height_mm": {
      "type": "number",
      "minimum": 0.05,
      "maximum": 1,
      "description": "Layer height in millimetres."
    },
    "width_mm": {
      "type": "number",
      "minimum": 5,
      "maximum": 1500,
      "description": "Finished width in millimetres. Height follows the source aspect ratio."
    },
    "band_layers": {
      "description": "Number of print layers per palette color. Default 8 base layers and 4 layers for each raised color.",
      "maxItems": 16,
      "type": "array",
      "items": {
        "type": "integer",
        "minimum": 1,
        "maximum": 300
      }
    }
  },
  "required": [
    "name",
    "brief",
    "decisions",
    "idempotency_key",
    "access_token",
    "erasure_token",
    "format",
    "width_mm"
  ],
  "additionalProperties": false
}
~~~

### create_3mf

Package one or more ready Print Ready STL models as a new 3MF model. Call prepare_model first. Set named parts, material colors, grouping, scale and offsets as needed. Separate objects can be resized independently in the slicer. Shared object names keep parts registered. Choose Bambu Studio filament assignments or standard 3MF. Poll get_model and call show_model for the new result. This tool works with any ready Print Ready STL.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Create 3MF","readOnlyHint":false,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |
| context_model | no | An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context. |
| previous_model | no | For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access. |
| imagegen_used | no | Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown. |
| name | yes | Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly. |
| brief | yes | Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages. |
| decisions | yes | Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant. |
| idempotency_key | yes | Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key. |
| access_token | yes | Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle. |
| erasure_token | yes | Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately. |
| format | yes | Bambu Studio filament assignments, or standard 3MF materials and build items. |
| bed_center_mm | no | Placement center for Bambu Studio, in mm. Defaults to [128,128]. |
| parts | yes | Authorized ready models. Use common source coordinates for parts that must align. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    },
    "context_model": {
      "description": "An authorized model handle from this conversation, with its guest access token when needed. Pass it for another part, cutaway or test in the same conversation. This preserves session correlation when the host omits conversation metadata. It does not grant access to other models. For a revision, previous_model already carries this context.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "previous_model": {
      "description": "For a revision, reference the earlier model ID and its guest access token if needed. The service uses this link to count iterations. Each revision keeps its own files and access.",
      "type": "object",
      "properties": {
        "model_id": {
          "type": "string",
          "format": "uuid",
          "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
        },
        "access_token": {
          "type": "string",
          "maxLength": 256
        }
      },
      "required": [
        "model_id"
      ],
      "additionalProperties": false
    },
    "imagegen_used": {
      "description": "Report whether image generation has been used in this conversation. Supply true or false when known. Omit when unknown.",
      "type": "boolean"
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100,
      "description": "Part name and visible version, at most 100 characters. Name separate parts and cutaway/test variants distinctly."
    },
    "brief": {
      "type": "string",
      "minLength": 40,
      "maxLength": 10000,
      "description": "Required detailed English model intent, 40 to 10000 characters. Describe purpose, use, mating parts, dimensions, measured facts, fit requirements, known printer/material constraints and assumptions. Summarize the request rather than copying chat messages."
    },
    "decisions": {
      "minItems": 1,
      "maxItems": 30,
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "maxLength": 2000
      },
      "description": "Required design notes, 1 to 30 entries of at most 2000 characters each. Explain orientation, bed face, support/bridge choices, fit parameters, fasteners, assumptions and changes from the previous revision as relevant."
    },
    "idempotency_key": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9_-]{16,100}$",
      "description": "Use the key from prepare_model. Reuse it only for retries of identical source, brief and decisions. A new revision needs a new key."
    },
    "access_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Secret from prepare_model. Required for submission and guest retrieval. Preserve privately with the handle."
    },
    "erasure_token": {
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$",
      "description": "Separate secret from prepare_model for deletion, including after guest downloads expire. Preserve privately."
    },
    "format": {
      "default": "bambu",
      "description": "Bambu Studio filament assignments, or standard 3MF materials and build items.",
      "type": "string",
      "enum": [
        "bambu",
        "standard"
      ]
    },
    "bed_center_mm": {
      "description": "Placement center for Bambu Studio, in mm. Defaults to [128,128].",
      "type": "array",
      "prefixItems": [
        {
          "type": "number",
          "minimum": -2000,
          "maximum": 2000
        },
        {
          "type": "number",
          "minimum": -2000,
          "maximum": 2000
        }
      ],
      "items": false,
      "minItems": 2,
      "maxItems": 2
    },
    "parts": {
      "minItems": 1,
      "maxItems": 32,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": {
            "type": "string",
            "format": "uuid",
            "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
            "description": "Model or view job UUID returned by the service."
          },
          "access_token": {
            "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
            "type": "string",
            "maxLength": 256
          },
          "name": {
            "description": "Part name, or use the source model name.",
            "type": "string",
            "minLength": 1,
            "maxLength": 100
          },
          "object": {
            "description": "Parts with the same object name stay in one assembly. Omit to create an independently editable object.",
            "type": "string",
            "minLength": 1,
            "maxLength": 100
          },
          "color": {
            "description": "Filament/material color as #RRGGBB. The order of first use sets Bambu filament slots.",
            "type": "string",
            "pattern": "^#[0-9a-fA-F]{6}$"
          },
          "material": {
            "description": "Material name for this color, such as PLA or PETG. Distinct material names create separate slots even when their colors match.",
            "type": "string",
            "minLength": 1,
            "maxLength": 100
          },
          "scale": {
            "description": "Uniform scale around the source origin. Defaults to 1.",
            "type": "number",
            "minimum": 0.001,
            "maximum": 100
          },
          "offset_mm": {
            "description": "XYZ translation after scaling. Defaults to [0,0,0].",
            "type": "array",
            "prefixItems": [
              {
                "type": "number",
                "minimum": -2000,
                "maximum": 2000
              },
              {
                "type": "number",
                "minimum": -2000,
                "maximum": 2000
              },
              {
                "type": "number",
                "minimum": -2000,
                "maximum": 2000
              }
            ],
            "items": false,
            "minItems": 3,
            "maxItems": 3
          }
        },
        "required": [
          "model_id"
        ],
        "additionalProperties": false
      },
      "description": "Authorized ready models. Use common source coordinates for parts that must align."
    }
  },
  "required": [
    "name",
    "brief",
    "decisions",
    "idempotency_key",
    "access_token",
    "erasure_token",
    "format",
    "parts"
  ],
  "additionalProperties": false
}
~~~

### record_model_image

Report imagegen use for an authorized model and retain the generated image when available. Optional image_url accepts exported PNG, JPEG or WebP data or a public HTTPS image URL, up to 4 MiB. Stores originals until explicit model erasure. Omit image_url when the host cannot export the image. The service cannot see other imagegen tools or open sandbox/private host references. Do not invent URLs or image bytes. Only submit generated illustrations. Never upload user reference photos, screenshots or composites containing them; omit image_url for those.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Save generated image","readOnlyHint":false,"destructiveHint":false,"openWorldHint":true}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | yes | Authorized root model UUID for this generated image. |
| access_token | no | Original guest model access secret. Omit for an owned model. |
| image_url | no | Optional public HTTPS image download URL or a data:image/png, data:image/jpeg or data:image/webp base64 URL. Use real exported image data, up to 4 MiB. Omit to report imagegen use without an available export. |
| prompt | no | Image generation prompt when available, up to 10000 characters. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "Authorized root model UUID for this generated image."
    },
    "access_token": {
      "description": "Original guest model access secret. Omit for an owned model.",
      "type": "string",
      "maxLength": 256
    },
    "image_url": {
      "description": "Optional public HTTPS image download URL or a data:image/png, data:image/jpeg or data:image/webp base64 URL. Use real exported image data, up to 4 MiB. Omit to report imagegen use without an available export.",
      "type": "string",
      "maxLength": 6000000
    },
    "prompt": {
      "description": "Image generation prompt when available, up to 10000 characters.",
      "type": "string",
      "maxLength": 10000
    }
  },
  "required": [
    "model_id"
  ],
  "additionalProperties": false
}
~~~

### render_view

Render one 320 x 320 preview from existing STL geometry. Choose isometric, front, back, left, right, top, bottom, custom or bed_contact. Custom azimuth/elevation are degrees; bed_contact shows the footprint within 0.05 mm of minimum Z. Does not alter print orientation, recompile source or accept section planes. Returns a queued view handle; retrieve it with get_model. Each new view consumes one render admission.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Render view","readOnlyHint":false,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| render_quota_token | no | Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota. |
| model_id | yes | Completed parent model or view job UUID. Reuses its existing STL; does not recompile or reorient the part. |
| access_token | no | Guest access secret for the parent model. Omit for an owned saved model. |
| idempotency_key | yes | New random key for this view; reuse on retry with exactly the same camera options. |
| view | yes | Single 320 x 320 view. bed_contact projects the footprint within 0.05 mm of minimum Z. The four-view sheet is generated by create_model. |
| zoom | yes | Orthographic zoom, 0.25 to 2, default 1. Larger values enlarge the model and may crop it. |
| azimuth | no | Custom camera azimuth in degrees, -360 to 360, default -45. Zero views from +X; positive rotates toward +Y. Use only with view=custom. |
| elevation | no | Custom camera elevation in degrees, -90 to 90, default 35. Zero is level, +90 is top, -90 is bottom. Use only with view=custom. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "render_quota_token": {
      "description": "Optional render quota capability returned by the existing signed-in Print Ready connection. Preserve and pass it across modeling tool routes to use that account allowance. Grants no profile, library or model access. Refresh through the existing connection if expired; do not sign in again or silently fall back to guest quota.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{43}$"
    },
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "Completed parent model or view job UUID. Reuses its existing STL; does not recompile or reorient the part."
    },
    "access_token": {
      "description": "Guest access secret for the parent model. Omit for an owned saved model.",
      "type": "string",
      "maxLength": 256
    },
    "idempotency_key": {
      "type": "string",
      "pattern": "^[a-zA-Z0-9_-]{16,100}$",
      "description": "New random key for this view; reuse on retry with exactly the same camera options."
    },
    "view": {
      "default": "isometric",
      "description": "Single 320 x 320 view. bed_contact projects the footprint within 0.05 mm of minimum Z. The four-view sheet is generated by create_model.",
      "type": "string",
      "enum": [
        "isometric",
        "front",
        "back",
        "left",
        "right",
        "top",
        "bottom",
        "custom",
        "bed_contact"
      ]
    },
    "zoom": {
      "default": 1,
      "description": "Orthographic zoom, 0.25 to 2, default 1. Larger values enlarge the model and may crop it.",
      "type": "number",
      "minimum": 0.25,
      "maximum": 2
    },
    "azimuth": {
      "description": "Custom camera azimuth in degrees, -360 to 360, default -45. Zero views from +X; positive rotates toward +Y. Use only with view=custom.",
      "type": "number",
      "minimum": -360,
      "maximum": 360
    },
    "elevation": {
      "description": "Custom camera elevation in degrees, -90 to 90, default 35. Zero is level, +90 is top, -90 is bottom. Use only with view=custom.",
      "type": "number",
      "minimum": -90,
      "maximum": 90
    }
  },
  "required": [
    "model_id",
    "idempotency_key",
    "view",
    "zoom"
  ],
  "additionalProperties": false
}
~~~

### get_model

Retrieve model or view job status, detailed English brief, design decisions, compiler error and mesh bounds. Ready jobs include a native PNG image block and explicit file links plus binary STL, PNG and manifest download links valid for at most ten minutes. Set include_source=true only when the user requests editable SCAD. The manifest includes intent, engine/library versions and compiler warnings. Repeating this read does not consume a render. Use the guest access secret or the authenticated owner. Older models may have no stored intent. Inspect the real preview yourself. When delivering show_model, use its interactive viewer without also displaying PNGs in chat. Display the PNG only when requested or when the host cannot show the viewer.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Get model","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | yes | Model or view job UUID returned by the service. |
| access_token | no | Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity. |
| include_preview | no | Include the real PNG for visual inspection. Use false when only refreshing viewer metadata or download links. |
| include_source | no | Include the editable SCAD download only when the user asks for source code. Defaults to false. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "Model or view job UUID returned by the service."
    },
    "access_token": {
      "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
      "type": "string",
      "maxLength": 256
    },
    "include_preview": {
      "description": "Include the real PNG for visual inspection. Use false when only refreshing viewer metadata or download links.",
      "type": "boolean"
    },
    "include_source": {
      "description": "Include the editable SCAD download only when the user asks for source code. Defaults to false.",
      "type": "boolean"
    }
  },
  "required": [
    "model_id"
  ],
  "additionalProperties": false
}
~~~

### download_models

Create a ZIP of the ordered STL files selected in the viewer. Set include_3mf to add the available 3MF print files and allow a single model. This action is available to the viewer.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Download print files","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| models | yes | The ordered model handles to download. Each guest model requires its own access token. |
| include_3mf | no | Include all available 3MF print files alongside STL files. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "models": {
      "minItems": 1,
      "maxItems": 20,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": {
            "type": "string",
            "format": "uuid",
            "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
            "description": "Model or view job UUID returned by the service."
          },
          "access_token": {
            "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
            "type": "string",
            "maxLength": 256
          }
        },
        "required": [
          "model_id"
        ],
        "additionalProperties": false
      },
      "description": "The ordered model handles to download. Each guest model requires its own access token."
    },
    "include_3mf": {
      "description": "Include all available 3MF print files alongside STL files.",
      "type": "boolean"
    }
  },
  "required": [
    "models"
  ],
  "additionalProperties": false
}
~~~

### create_share

Create a public snapshot of the ordered ready models in the current viewer and return its stable public URL. The page contains a rotatable STL viewer and an STL download and inline editable SCAD and geometry details. Each part includes its design brief and decisions. Account details, session data, conversation messages and captured images stay private. Available only to the app UI after the user clicks Share. Does not start a render. Existing active shares with the same ordered models are reused.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Share part","readOnlyHint":false,"destructiveHint":true,"openWorldHint":true}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | yes | The selected ready model. Its owner or original guest capability must authorize publication. |
| access_token | no | Original guest access capability when required. Never include this in the public URL. |
| models | no | Ordered models in the current viewer, each independently authorized. The first must match model_id. Omit for a single part. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "The selected ready model. Its owner or original guest capability must authorize publication."
    },
    "access_token": {
      "description": "Original guest access capability when required. Never include this in the public URL.",
      "type": "string",
      "maxLength": 256
    },
    "models": {
      "description": "Ordered models in the current viewer, each independently authorized. The first must match model_id. Omit for a single part.",
      "minItems": 1,
      "maxItems": 20,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": {
            "type": "string",
            "format": "uuid",
            "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
            "description": "Model or view job UUID returned by the service."
          },
          "access_token": {
            "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
            "type": "string",
            "maxLength": 256
          }
        },
        "required": [
          "model_id"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "model_id"
  ],
  "additionalProperties": false
}
~~~

### revoke_share

Revoke the selected part's public link and remove its public snapshot files. Private model files remain available. Available only to the user-operated app UI. A new Share action creates a different URL.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Stop sharing part","readOnlyHint":false,"destructiveHint":true,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | yes | The selected model whose public link should stop working. |
| access_token | no | Original guest access capability when required. |
| share_id | no | Public link identifier to revoke. Must belong to the authorized model. Omit to revoke all shares containing that model. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "The selected model whose public link should stop working."
    },
    "access_token": {
      "description": "Original guest access capability when required.",
      "type": "string",
      "maxLength": 256
    },
    "share_id": {
      "description": "Public link identifier to revoke. Must belong to the authorized model. Omit to revoke all shares containing that model.",
      "type": "string",
      "pattern": "^[A-Za-z0-9_-]{32}$"
    }
  },
  "required": [
    "model_id"
  ],
  "additionalProperties": false
}
~~~

### show_model

Open one model or an ordered collection of up to 20 models in the interactive in-chat STL viewer. First retrieve and inspect the real previews with get_model. Supply models in the order you want the numbered file list to appear; the first opens initially. Choose the models and their order to suit the task. Give diagnostic cutaways and printable parts distinct names. Users click numbered entries or arrows, or swipe the file strip on touch screens. The name, dimensions and STL download always refer to the selected file. Drag the viewport to rotate, scroll or pinch to zoom, and select preset cameras. Bed-contact faces at Z=0 appear darker without changing geometry. Camera movement and paging do not start render jobs. Guest capabilities and owned saved models are supported; a real PNG is shown if WebGL is unavailable. The client preloads the supplied STL files for paging. Use this viewer as the visual delivery without also posting PNG previews in chat. The Share button creates a public URL for the selected part, with this same rotatable viewer and an STL download and inline SCAD and model-details views. Sharing happens through the user-operated button. Stop sharing revokes the link. Always supply conversation_models with all available model handles from the current chat, including earlier revisions, separate parts and test variants, so My models can list them for guests. This gallery list does not change the selected files or their order. For models with a 3MF, the viewer offers Download 3MF and Download all files.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Show model","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | no | Single model or view UUID. Supply either model_id with its access_token, or the ordered models array. |
| access_token | no | Original guest secret for the single model_id. Omit for an owned saved model; use each array entry's token when supplying models. |
| models | no | Ordered list of 1 to 20 distinct model handles. Each entry has model_id and its original guest access_token when required. The first item opens initially; this exact order becomes the numbered file list. Each item has its own STL download. Choose useful ordering and clear model names, including for cutaways or fit tests. Do not also supply the top-level model_id or access_token. |
| conversation_models | no | All available model handles from this chat, up to 1000, each with model_id and its original guest access_token when required. Supply on every show_model call, even when showing one part. Used by My models separately from the numbered viewer files. Each handle is authorized individually. Do not invent handles or include handles from another chat. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "description": "Single model or view UUID. Supply either model_id with its access_token, or the ordered models array.",
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$"
    },
    "access_token": {
      "description": "Original guest secret for the single model_id. Omit for an owned saved model; use each array entry's token when supplying models.",
      "type": "string",
      "maxLength": 256
    },
    "models": {
      "description": "Ordered list of 1 to 20 distinct model handles. Each entry has model_id and its original guest access_token when required. The first item opens initially; this exact order becomes the numbered file list. Each item has its own STL download. Choose useful ordering and clear model names, including for cutaways or fit tests. Do not also supply the top-level model_id or access_token.",
      "minItems": 1,
      "maxItems": 20,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": {
            "type": "string",
            "format": "uuid",
            "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
            "description": "Model or view job UUID returned by the service."
          },
          "access_token": {
            "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
            "type": "string",
            "maxLength": 256
          }
        },
        "required": [
          "model_id"
        ],
        "additionalProperties": false
      }
    },
    "conversation_models": {
      "description": "All available model handles from this chat, up to 1000, each with model_id and its original guest access_token when required. Supply on every show_model call, even when showing one part. Used by My models separately from the numbered viewer files. Each handle is authorized individually. Do not invent handles or include handles from another chat.",
      "maxItems": 1000,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": {
            "type": "string",
            "format": "uuid",
            "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
            "description": "Model or view job UUID returned by the service."
          },
          "access_token": {
            "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
            "type": "string",
            "maxLength": 256
          }
        },
        "required": [
          "model_id"
        ],
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
~~~

### show_library

Open available models in a zoomable, rotatable gallery in chat. Signed-in calls include the private saved library. For guests, pass up to 20 model handles from this conversation with their original access tokens. Each handle is authorized separately. Without sign-in or handles the collection is empty. Pass the cursor to page through saved models.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"My models","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| models | no | Up to 20 known model handles, each with model_id and its original guest access_token. Include the current part and earlier revisions available in this conversation. Omit access_token only for an owned saved model. Do not invent handles or user IDs. |
| cursor | no | Opaque saved-library cursor from the previous call. Omit for the first page. Requires sign-in. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "models": {
      "description": "Up to 20 known model handles, each with model_id and its original guest access_token. Include the current part and earlier revisions available in this conversation. Omit access_token only for an owned saved model. Do not invent handles or user IDs.",
      "maxItems": 20,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": {
            "type": "string",
            "format": "uuid",
            "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
            "description": "Model or view job UUID returned by the service."
          },
          "access_token": {
            "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
            "type": "string",
            "maxLength": 256
          }
        },
        "required": [
          "model_id"
        ],
        "additionalProperties": false
      }
    },
    "cursor": {
      "description": "Opaque saved-library cursor from the previous call. Omit for the first page. Requires sign-in.",
      "type": "string",
      "maxLength": 2000
    }
  },
  "additionalProperties": false
}
~~~

### show_welcome

Show the Print Ready welcome guide and example prompts only when the user asks for help using Print Ready, examples or the guide. Do not call after installation, for a greeting or before an ordinary modeling request. No sign-in required. Example buttons send a prompt into the conversation where supported, or let the user copy it.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Welcome guide","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### save_model

Save a completed guest model to your signed-in private library.

Sign-in required.
Annotations: {"title":"Save model","readOnlyHint":false,"destructiveHint":true,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | yes | Model or view job UUID returned by the service. |
| access_token | no | Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "Model or view job UUID returned by the service."
    },
    "access_token": {
      "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
      "type": "string",
      "maxLength": 256
    }
  },
  "required": [
    "model_id"
  ],
  "additionalProperties": false
}
~~~

### list_models

List available models, newest saved models first. Signed-in calls include the private saved library. For guests, pass up to 20 model handles from this conversation with their original access tokens. Each handle is authorized separately. Without sign-in or handles the collection is empty. Pass the cursor to page through saved models.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"List models","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| models | no | Up to 20 known model handles, each with model_id and its original guest access_token. Include the current part and earlier revisions available in this conversation. Omit access_token only for an owned saved model. Do not invent handles or user IDs. |
| cursor | no | Opaque saved-library cursor from the previous call. Omit for the first page. Requires sign-in. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "models": {
      "description": "Up to 20 known model handles, each with model_id and its original guest access_token. Include the current part and earlier revisions available in this conversation. Omit access_token only for an owned saved model. Do not invent handles or user IDs.",
      "maxItems": 20,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "model_id": {
            "type": "string",
            "format": "uuid",
            "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
            "description": "Model or view job UUID returned by the service."
          },
          "access_token": {
            "description": "Original guest access secret. Required for guest models; omitted for models owned by the signed-in identity.",
            "type": "string",
            "maxLength": 256
          }
        },
        "required": [
          "model_id"
        ],
        "additionalProperties": false
      }
    },
    "cursor": {
      "description": "Opaque saved-library cursor from the previous call. Omit for the first page. Requires sign-in.",
      "type": "string",
      "maxLength": 2000
    }
  },
  "additionalProperties": false
}
~~~

### rename_model

Rename a model in your private library.

Sign-in required.
Annotations: {"title":"Rename model","readOnlyHint":false,"destructiveHint":true,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | yes | Owned saved model UUID. |
| name | yes | New display name, 1 to 100 characters. Renaming does not change geometry. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "Owned saved model UUID."
    },
    "name": {
      "type": "string",
      "minLength": 1,
      "maxLength": 100,
      "description": "New display name, 1 to 100 characters. Renaming does not change geometry."
    }
  },
  "required": [
    "model_id",
    "name"
  ],
  "additionalProperties": false
}
~~~

### get_profile

Get your saved printer preferences.

Sign-in required.
Annotations: {"title":"Printer preferences","readOnlyHint":true,"destructiveHint":false,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| none | | No arguments. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
~~~

### save_preferences

Save only explicitly supplied printer and material preferences.

Sign-in required.
Annotations: {"title":"Save preferences","readOnlyHint":false,"destructiveHint":true,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| printer | no | Explicitly supplied printer name, at most 100 characters. |
| material | no | Explicitly supplied printing material, at most 100 characters. |
| build_volume_mm | no | Explicit build volume [X,Y,Z] in millimetres, each greater than zero and at most 2000. |
| nozzle_mm | no | Explicit nozzle diameter in millimetres, greater than zero and at most 5. Omitted fields keep their saved values. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "printer": {
      "description": "Explicitly supplied printer name, at most 100 characters.",
      "type": "string",
      "maxLength": 100
    },
    "material": {
      "description": "Explicitly supplied printing material, at most 100 characters.",
      "type": "string",
      "maxLength": 100
    },
    "build_volume_mm": {
      "description": "Explicit build volume [X,Y,Z] in millimetres, each greater than zero and at most 2000.",
      "type": "array",
      "prefixItems": [
        {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 2000
        },
        {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 2000
        },
        {
          "type": "number",
          "exclusiveMinimum": 0,
          "maximum": 2000
        }
      ],
      "items": false,
      "minItems": 3,
      "maxItems": 3
    },
    "nozzle_mm": {
      "description": "Explicit nozzle diameter in millimetres, greater than zero and at most 5. Omitted fields keep their saved values.",
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 5
    }
  },
  "additionalProperties": false
}
~~~

### delete_model

Delete the model files and retained task text. Guests must supply their erasure token, including after downloads expire.

Guest use is available; authenticated identity is used when supplied.
Annotations: {"title":"Delete model","readOnlyHint":false,"destructiveHint":true,"openWorldHint":false}

| Parameter | Required | Description |
| --- | --- | --- |
| model_id | yes | Model UUID to erase, including its views and retained task text. |
| erasure_token | no | Guest erasure secret from prepare_model; required for guest deletion, even after download expiry. Omit when deleting an owned saved model. |

Exact input schema:

~~~json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "model_id": {
      "type": "string",
      "format": "uuid",
      "pattern": "^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|ffffffff-ffff-ffff-ffff-ffffffffffff)$",
      "description": "Model UUID to erase, including its views and retained task text."
    },
    "erasure_token": {
      "description": "Guest erasure secret from prepare_model; required for guest deletion, even after download expiry. Omit when deleting an owned saved model.",
      "type": "string",
      "maxLength": 256
    }
  },
  "required": [
    "model_id"
  ],
  "additionalProperties": false
}
~~~
