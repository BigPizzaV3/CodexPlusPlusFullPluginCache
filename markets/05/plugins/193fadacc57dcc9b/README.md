# Cria.al

Last verified: 2026-10-06

An OpenAI plugin connecting travellers to CRIA's public car-rental search in Albania.
The package uses the portable Agent Plugins format: `plugin.json` holds the listing and
review scenarios, `mcp.json` connects to `https://cria.al/mcp`, and `assets/icon.png` holds
the CRIA icon.

The server provides the workflow instructions and four read-only tools: `list_locations`,
`search_cars`, `get_car` and `check_availability`. Searches require no sign-in. Travellers
complete reservation requests and payments on cria.al.

## Listing

The plugin is approved in the [OpenAI Platform Plugins](https://platform.openai.com/plugins)
directory under the verified Cria.al identity, with the domain verified by
`public/.well-known/openai-apps-challenge`. Review materials (five positive and three
negative scenarios, the walkthrough video, the commerce declaration and release notes) are
in `extensions.com.openai.review`; the portal reads the video URL only from the package.
Country availability is set in the dashboard. The listing's public ChatGPT link is
`ai.chatgpt_app_url` in `config/cria.php`; the `/ai` hub, the traveler page and the llms
files link it.

`name` (`cria-car-rental`) is the plugin's stable identity: never change it. The folder
name does not matter.

## Update

- **Tool changes** need no new package: OpenAI rescans `https://cria.al/mcp` daily, or on
  **MCPs → Issues → Rescan** after a deploy.
- **Listing, review or asset changes** need a new package: bump `version`, rebuild the ZIP,
  open the existing plugin, choose **Upload plugin to make changes**, resolve any findings
  and submit it for review. Publish the approved version.

## Rebuild the ZIP

Run from this directory; the ZIP is written to `plugins/dist/` (git-ignored). The archive
contains one plugin folder and only the four listed public package files.

```sh
python3 - <<'PY'
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path.cwd()
manifest = json.loads((root / "plugin.json").read_text())
output = root.parent / "dist" / f"{manifest['name']}-{manifest['version']}.zip"
output.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
    for name in ("plugin.json", "mcp.json", "assets/icon.png", "README.md"):
        archive.write(root / name, f"{manifest['name']}/{name}")
print(output)
PY
```

Update the manifest version when uploading a changed package. Keep credentials, local
configuration and application source out of the ZIP.

Format and submission references:
[Package your plugin](https://developers.openai.com/plugins/build/plugins) and
[Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission).
