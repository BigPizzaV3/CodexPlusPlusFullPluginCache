# Device It

Prepare a built static web app as a local PWA preview. Device It copies an explicit list of public assets into a new directory, adds a manifest and generic device icons, creates an exact static service-worker cache, generates a local QR code and tests the offline shell in Chromium.

This skills-only package runs on a local agent host. It has no MCP server, account integration, hosting service or device-management component. It does not install an app on a phone.

## Requirements

- Node.js 22 or newer and npm on a local computer with file and process access.
- An already-built static app with `index.html`, normal head/body tags, no base URL override, and no existing manifest or service worker.
- Installed, locked dependencies. Browser verification also needs the matching Playwright Chromium and its operating-system dependencies.
- Permission to read the selected build, write a fresh output, and start a local listener. Network access is needed for explicitly authorized npm/browser downloads only. Runtime preview and tests use local origins.

The Node commands use cross-platform APIs. The supplied `.sh` aliases need Bash. This candidate was executed on macOS arm64; Windows and Linux execution, physical phones and Home Screen installation have not been verified. No cloud-only ChatGPT runtime is claimed.

## Run locally

Start with [FIRST-RUN.md](FIRST-RUN.md). From this package's root, check readiness, then install missing dependencies/browser when downloads are authorized:

```sh
node scripts/run.mjs preflight
node scripts/run.mjs setup
```

`preflight` installs nothing. `setup` checks every locked package version, repairs missing/incomplete dependencies with pinned `npm ci`, and downloads the matching Chromium only if missing. Both launch and close Chromium to check readiness; `ok: true` and exit 0 mean the local tooling is ready. A second successful setup has an empty `actions` list and avoids installation. Standard npm/Playwright caches are reused without deletion. Runtime and OS library installation remains outside this command.

Create an asset-list JSON file in a working directory, for example:

```json
["index.html", "app.js", "style.css"]
```

Review those files as public static assets. Only listed files are copied; unlisted files stay in the original build. Include every script, stylesheet, font and image needed for offline rendering. Then use fresh output and evidence paths:

```sh
node scripts/run.mjs prepare --dist /path/built --out /path/new-pwa --assets /path/public-assets.json --name "My App"
node scripts/run.mjs preview --dir /path/new-pwa --qr /path/new-preview-qr.png
```

The foreground preview prints its selected port and `loopbackURL`. In another terminal:

```sh
node scripts/run.mjs verify --url http://127.0.0.1:PORT/ --expect-text "Known visible app text" --report /path/new-check.json --screenshot /path/new-offline.png
```

Stop the preview with Ctrl+C. Verification closes its own disposable browser even on failure. QR/report/screenshot files are not overwritten. No global packages or `npx` are used.

For an explicitly authorized LAN preview, add `--lan-address` with an IPv4 address belonging to this computer. This binds `0.0.0.0`, and the QR points at that LAN address. Other devices on the network may read the selected files. Ordinary LAN HTTP usually cannot activate service workers; the separate loopback URL supports desktop offline verification. No phone installation or phone test is implied.

## What is preserved and cached

The source build is never changed. The output must not exist and must be outside the input. Existing PWA files or registrations cause preparation to stop without replacing them. Rebuild into a new output for each revision.

Allowed assets use simple relative paths with supported HTML, JS, CSS, image, font or WASM extensions. Dot paths, symlinks, `api`, `private`, `secrets`, `node_modules`, JSON data, source maps and oversized files are refused. Limits: 1,000 selected files, 8 MiB per file, 64 MiB total. This is a file/path boundary, not a secret scanner; users must approve the selected content as public.

`device-it-build.json` lists the public file names, hashes and exact precache. The service worker fetches only that static list at installation, with credentials omitted. It refuses private/no-store, redirected or failed responses. It never adds network responses to the cache at runtime. Requests with query strings, Authorization headers, non-GET methods, off-origin destinations or paths outside the list bypass the cache. `/` maps to the cached `index.html`; other deep routes have no fallback. Only previous Device It caches for the same origin and scope are retired.

Offline verification proves the expected shell text survives reload and cache bytes match the prepared inventory. It does not prove every app feature works offline. APIs, login and external content are not cached. The preview's restrictive content-security policy blocks off-origin resources and inline scripts; apps requiring these need changes or a different preview workflow. The package does not relax that policy automatically.

Browser cache data exists in the chosen browser profile until its site data is cleared. The checker uses a disposable profile; a user's manual browser preview can retain site data. Generated output, QR, report and screenshot files remain until deleted. The generated icons are opaque generic placeholders in 192, 512, maskable 512 and Apple 180 pixel sizes.

## Review and packaging

```sh
npm run validate
npm test
npm run test:browser -- /absolute/new-fixture-evidence
python3 scripts/package.py /absolute/device-it-review.zip
```

Packaging uses `package-files.json`, an explicit file allowlist, and requires Python 3 only for ZIP creation. It never traverses or packages `local-state`, `node_modules`, old deployment/MDM helpers, old hosting references, credentials or device profiles. The source checkout may retain those legacy files for existing users; the new root/skill instructions and entrypoint do not invoke them.

Read `PRIVACY.md` and `ATTRIBUTION.md`. The [version-scoped public privacy policy](https://github.com/Christian-Katzmann/device-it/blob/main/docs/privacy-plugin-0.2.1.md) covers this local PWA plugin. Private support is available at christian@katzmann.dk. Original code carries the publisher-approved MIT grant and supplied listing artwork. Version 0.2.1 is prepared for review; OpenAI directory acceptance is not yet verified.
