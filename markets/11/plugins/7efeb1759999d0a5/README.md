# Cutaway

<img src="assets/icon.svg" width="80" height="80" alt="Cutaway icon">

/anatomy, adapted for ChatGPT.

Cutaway is a ChatGPT plugin for learning how machines work. Look inside the GE9X jet engine, follow water through an espresso machine, compare wing designs, or study the pistons and crankshaft in a boxer engine.

Open a finished model, select a component, and move its controls. The plugin returns explanations, source links, and HTML or SVG downloads of the selected view. You can also attach a photo or name a model to create a cutaway using the image, search, file, and code tools in your ChatGPT session. Neither path needs a separate API key.

The drawing toolkit and illustration guidance come from [Ryan's (@wheresryan22) Anatomy](https://github.com/wheresryan22/anatomy). Cutaway adapts that work for ChatGPT and adds the plugin, demos, and file delivery instructions.

## Use in ChatGPT

[Install Cutaway in ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6acd34e6e95c81919f7fcf2864d55591). Once installed, select **Cutaway** using `@` in a new conversation and describe the machine you want to understand.

Workspace admins can build the [marketplace package](#packaging) and follow the [workspace import instructions](https://learn.chatgpt.com/docs/enterprise/plugin-management). For local development, see the [plugin setup guide](https://developers.openai.com/plugins/build/plugins).

Imported packages that declare servers in `mcp.json` are marked **Desktop only**, even when the server uses HTTPS. For private web testing, import `dist/cutaway-photo-web-test-<version>.zip`. It includes the drawing skill without the MCP declaration. Public submission uses `dist/cutaway-<version>.zip` through the **With MCP** flow. The private-import badge doesn't establish the public listing's availability. See the [import restrictions](https://learn.chatgpt.com/docs/enterprise/plugin-management#desktop-only-plugins) and [submission guide](https://developers.openai.com/plugins/deploy/submission).

Try “Show the GE9X compressor,” “Extend the wing flaps to 25 degrees,” or “Open the espresso machine while brewing.” The model opens inside compatible ChatGPT clients, with links to open it in a browser or download the selected view. Custom cutaways use the bundled drawing skill.

### From a photo

Attach a photo or give a model number. Cutaway identifies the likely machine, researches its internals using available search tools or supplied manuals, and draws what the references support. Try:

```text
Show me how my espresso machine works. Identify the model from this photo,
find references for its internals, and build an interactive isometric cutaway
of the water path. Ask for the model label if you need it. Include sources
and explain which details are illustrative or unknown.
```

A photo alone doesn't reveal the internals. When references establish the operating principle but not the exact layout, Cutaway builds a simplified mechanism cutaway and labels the uncertain details. It asks for more information when that uncertainty changes what the drawing would teach, or when you request an exact internal layout. Drawings are created in the ChatGPT session; the photo isn't sent to Cutaway's hosted service.

Custom drawings use a [shared template](skills/cutaway/custom/guide.md) for shaded materials, playback, part selection, sources, and downloads. The build creates a standalone page and a preview fragment with the same drawing and controls. The skill supplies the machine-specific geometry and motion. To work on one locally:

```sh
bun skills/cutaway/scripts/create-project.mjs tmp/my-cutaway --example custom
bun tmp/my-cutaway/build.mjs
bun tmp/my-cutaway/custom/validate.mjs tmp/my-cutaway/cutaway.html tmp/my-cutaway/cutaway.svg
```

Replace the starter mechanism and research record before delivering a drawing. The validator checks the generated files; browser and ChatGPT checks are separate.

The 0.3.1 source adds **Download video** to custom cutaways. This update has not yet been submitted to the public listing. It runs one full cycle and prepares a silent, square H.264 MP4 with the drawing, stage captions, and scope note. Keep the tab open while it records; Cancel restores the previous view. Everything runs locally, without sending the drawing or source photo to a server.

Video export requires browser support for H.264 recording. If the ChatGPT preview cannot export it, download the HTML and open it in a current Chrome or Safari browser. **Save MP4** lets you retry a completed download. The hosted examples still offer HTML and SVG. Manual testing has confirmed MP4 playback, export from a ChatGPT preview, and upload to X.

`bun run check:video` exercises the real browser encoder from both the standalone HTML and a sandboxed preview fragment, then verifies playable, silent MP4s. It uses the same `CUTAWAY_PLAYWRIGHT` and `CUTAWAY_BROWSER` overrides as the existing browser checker. The ordinary test suite checks export controls and failure handling with browser API substitutes; it does not verify encoding. The sandbox check does not establish compatibility with ChatGPT's actual preview policies.

## Demos and prompts

These previews show the finished hardware demos. Each demo runs offline and includes controls, sources, and an explanation of its simplifications. Animations start paused.

[Build the demos locally](#development), or use the prompts below to create your own cutaways in ChatGPT.

### GE9X jet engine

![GE9X cutaway showing the fan, compressor, combustor, turbines, and separate core and bypass airflow](assets/examples/jet-engine.svg)

```text
Build a GE9X cutaway using GE Aerospace's published references: the 16-blade fan,
3-stage booster, 11-stage compressor, 2 high-pressure and 6 low-pressure turbine
stages, and concentric shafts. Separate core and bypass airflow, and let me select
parts and pause the flow. Explain the simplifications and include sources.
```

### Wing designs

![Aircraft wing cutaway showing spars, ribs, a leading-edge slat, and a trailing-edge flap](assets/examples/wing.svg)

```text
Build a wing cutaway with spars, ribs, flaps, and slats. Let me compare rectangular,
tapered, and swept wings. Explain what changes when the high-lift devices extend.
```

### Espresso machine

![Espresso machine cutaway showing the reservoir, pump, boiler, group head, and water path into the cup](assets/examples/espresso.svg)

```text
Build a cutaway espresso machine with a reservoir, pump, boiler, brew valve,
group head, and portafilter. Trace the water into the cup and let me step through
heating and brewing.
```

### Boxer engine

![4-cylinder boxer cutaway showing horizontally opposed pistons, connecting rods, and separate crankpins](assets/examples/boxer.svg)

```text
Build a 4-cylinder boxer cutaway with horizontally opposed pistons and separate
crankpins. Let me turn the crankshaft and follow an opposing piston pair.
Explain why the opposing pistons move together.
```

## Optional glow

Cutaway includes 2D SVG lighting and palettes from [April Zhu's iso-glow](https://isoglow.dev/), based on Tolga Cohce's iso-figure. Ask for glow to highlight active parts or flow paths in dark mode. For an espresso machine, add:

```text
Use 2D glow in dark mode. Light up the water path while pumping and the heater
while heating. Include technical/glow and light/dark controls.
```

The [glow guide](skills/cutaway/glow/guide.md) covers palettes, filters, and how to use them in editable drawings.

## Development

Use Bun and Node.js 22 or newer. Packaging also needs the system `zip` and `unzip` commands.

```sh
bun install --frozen-lockfile --ignore-scripts
bun run check
bun run test
bun run build:site
bun run preview:site
```

Open `http://127.0.0.1:4322`. The preview serves the website and MCP endpoint at `/mcp`. The website is in `site/`, the ChatGPT bridge in `app/`, and the server in `server/`. `build:site` also rebuilds the release archives.

The output includes a Cloudflare Pages worker. Static hosting serves the demos; the MCP endpoint and selected-view exports need a runtime. Deployment configuration stays local.

To build only the hardware demos:

```sh
bun run hardware
```

Open `dist/hardware/index.html`. Each demo has a self-contained HTML file and a standalone SVG, with source in `site/hardware/`.

After building, run `bun run check:site`, `bun run check:hardware`, and `bun run check:mcp`. These check links, controls, MCP requests, view exports, and the host bridge. Check layout and motion in a browser after changing drawings or controls. Local checks don’t establish that ChatGPT or Cloudflare has run the build.

## MCP service

The service exposes `list_cutaways`, `open_ge9x`, `open_wing`, `open_espresso`, and `open_boxer`. Each open tool accepts settings for its model and returns a view, an explanation, limitations, sources, and HTML/SVG export links. It provides public educational content without authentication, accounts, saved sessions, or an external model API.

The UI uses the MCP Apps bridge. Controls run locally; “Discuss this view” sends the current settings to the conversation. Downloads preserve the selected state and the applicable license notices. All animation starts paused.

For a development connection, use a reachable HTTPS endpoint ending in `/mcp` and no authentication. See OpenAI’s [connection instructions](https://developers.openai.com/plugins/build/app-quickstart). For normal use, [install Cutaway from the public directory](https://chatgpt.com/plugins/plugin_asdk_app_6acd34e6e95c81919f7fcf2864d55591).

## Packaging

```sh
bun run package
```

Every package build creates both ZIPs, using the version in [plugin.json](plugin.json):

| File | Use |
| --- | --- |
| `dist/cutaway-<version>.zip` | Public submission, including the drawing skill and hosted MCP tools. |
| `dist/cutaway-photo-web-test-<version>.zip` | Private import into ChatGPT on web, with the same drawing skill and templates. Hosted example tools are omitted. |

The private copy appears as **Cutaway Photo Web Test**, so it can be installed alongside Cutaway. Import it into ChatGPT, start a new chat, select it with `@`, and attach a photo. This tests photo generation; the complete plugin's hosted tools need their own connection test.

To refresh only the private ZIP while a submission is under review:

```sh
bun run package:web-test
```

This leaves the submission ZIP and workspace marketplace unchanged. The full build also creates `dist/workspace-marketplace/` with the submission package. The server deploys with the website; the offline demos ship separately.

For workspace import, copy the contents of `dist/workspace-marketplace/` into a GitHub repository, preserving the hidden `.agents` directory. Reimport or reinstall the package after rebuilding to use the changes.

Run `bun run release` to build `dist/releases/<version>/`. It contains plugin, source, marketplace, hardware, and software-example archives, plus `SHA256SUMS`. Release and website builds also generate both ZIPs in `dist/`; the private test ZIP stays out of the public downloads. Copy exported source outside `dist/` before editing it; builds replace generated files.

## Credits and license

Cutaway's original code, demos, and website use the [MIT license](LICENSE), copyright © 2026 Abhay Kumar. Bundled Anatomy and iso-glow code keeps its original copyright and MIT notices.

See [THIRD_PARTY.md](THIRD_PARTY.md) for upstream sources, local changes, and license details.
