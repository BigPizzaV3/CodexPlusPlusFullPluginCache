# First run

Run this package on a local computer with Node.js 22+ and npm. A cloud-only chat cannot run it. macOS arm64 is tested; Windows/Linux and physical phone installation are unverified. On Linux, Chromium also needs OS libraries, which setup does not install.

1. Resolve the plugin root containing `package.json` and `scripts/run.mjs`. All commands below run from that directory.
2. Check readiness without installing anything:

   ```sh
   node scripts/run.mjs preflight
   ```

   Exit 0 means locked dependencies import and matching Chromium launches and closes. Exit 1 gives the missing prerequisite and next step. If Node itself is missing, install a local Node.js 22+ runtime with npm before running this command. Setup cannot install its own runtime.

3. When npm/browser downloads are authorized by the task, run:

   ```sh
   node scripts/run.mjs setup
   ```

   Setup installs package dependencies with locked `npm ci --ignore-scripts` only when required packages are absent, have the wrong version or cannot import. It downloads pinned Chromium only when its executable is missing. Rerunning a ready package launches and closes Chromium again with no installation. It never uses `npx`, installs global packages, changes OS libraries or repairs an app project.

4. Review the already-built app's public shell files. Write their relative paths to an asset-list JSON file, including `index.html`, for example `["index.html", "app.js", "style.css"]`. Then use new output and evidence paths:

   ```sh
   node scripts/run.mjs prepare --dist /absolute/built --out /absolute/new-pwa --assets /absolute/public-assets.json --name "My App"
   node scripts/run.mjs preview --dir /absolute/new-pwa --qr /absolute/new-preview-qr.png
   ```

5. Use the printed loopback URL in another terminal:

   ```sh
   node scripts/run.mjs verify --url http://127.0.0.1:PORT/ --expect-text "Known visible app text" --report /absolute/new-check.json --screenshot /absolute/new-offline.png
   ```

   Stop the foreground preview with Ctrl+C and confirm its listener closes. Desktop offline-shell evidence does not prove iPhone Home Screen installation. A phone needs an explicitly approved LAN preview and reachable local address; ordinary LAN HTTP remains a preview.

Downloads use the configured npm cache and Playwright's normal versioned browser cache. An existing `PLAYWRIGHT_BROWSERS_PATH` is respected; use the same environment for setup and verification. Browser downloads disable Playwright's cache garbage collection (`PLAYWRIGHT_SKIP_BROWSER_GC=1`) so other cached browser versions remain. Caches are not included in the ZIP. Setup does not purge caches or download when preflight or a ready second setup is run. Downloads need network access and writable cache/package directories. A failed install is reported once, with no alternative installer or automatic retry.

Read `README.md` and `SKILL.md` for asset boundaries and full limitations. Browser/OS failures include the actual launch error. Resolve that prerequisite before preparing an app.
