# Validator rules

A rejected `submit_applet_deployment` lists one `- code: message` line per broken rule — at most one per code, in
this order. `…` stands for the detail the validator fills in (a size, a tag, a version).

| # | Code | Message |
| --- | --- | --- |
| 1 | `too_large` | `The file is … KB; an applet must be 512 KB or smaller — remove embedded assets or inline data.` |
| 2 | `not_html` | `The file is not an HTML document; start with <!doctype html> and put your markup in <body>.` |
| 3 | `external_script` | `<script src="…"> is not allowed; inline every script inside the file.` |
| 4 | `external_resource` | `External resources are blocked by the sandbox (…); inline styles and use data: URIs for images.` |
| 5 | `nested_frame` | `Nested frames and plugins (…) are not allowed inside an applet.` |
| 6 | `form_action` | `Forms cannot submit anywhere; handle input with JavaScript instead of a form action.` |
| 7 | `meta_refresh` | `<meta http-equiv="refresh"> is not allowed; an applet never navigates.` |
| 8 | `missing_ready_call` | `The file never calls fxr.ready(); await it before reading context, or the applet will never receive data.` |
| 9 | `sdk_version_mismatch` | `This applet targets SDK "…", but the host provides SDK 1; write against the v1 reference.` |
