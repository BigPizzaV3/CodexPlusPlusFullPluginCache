# FileStation plugin

FileStation provides reusable file workflows for ChatGPT and Codex hosts that support skills and Python execution. This is a skills-only plugin, not a GPT or an MCP service.

## Included

- PDF merging, page extraction, selected-page rotation and selectable-text extraction.
- Image conversion to PNG, JPEG or WebP and aspect-preserving resizing.
- CSV to JSON and JSON formatting with data-loss guards.
- A dated guide to 50 FileStation website tools and their limitations.

The compatibility manifest is `.codex-plugin/plugin.json`; the skill is `skills/file-tools/SKILL.md`. Scripts and the tool guide are bundled inside that skill. The plugin contains no keys, account integration, analytics or outgoing network requests. Python dependencies may be installed from PyPI when permitted; the processing script itself makes no network requests.

Python 3.10+ is required. Install the skill's requirements into an isolated environment if the host does not provide them. Native ChatGPT file execution and skill support depend on the user's product and plan; the plugin cannot enable unavailable host capabilities.

Input limits: 50 MiB per file, 500 PDF pages, 25 megapixels per image. Encrypted PDFs and multi-frame images are unsupported. Outputs never overwrite existing paths. Document appearance, forms, links, signatures and metadata may change; preserve and review originals.

## Data handling

Files are processed in the execution environment of the host the user chooses, which may be cloud-hosted. This does not imply device-local processing, immediate deletion or a particular retention policy. Host settings and terms govern uploaded files and generated artifacts. The publisher receives no document contents through these bundled scripts. Website visits and optional website account operations are separate and follow FileStation's website notices. This version cannot save to FileStation accounts or synchronize drafts.

## Public availability

The package is built and locally tested. It is not yet submitted, approved or listed in the public directory. Public distribution requires verified publisher identity, accurate public notices and successful OpenAI review. The live FileStation website and the separately created private GPT are unchanged by this package.

Support: info@filestation.io. Do not email confidential documents merely to report a problem.
