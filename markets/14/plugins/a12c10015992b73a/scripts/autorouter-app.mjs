#!/usr/bin/env node
/**
 * Installs and opens the AutoRouter Mac app for the plugin's setup skill.
 * The app's own onboarding then signs the person in and connects Codex; this
 * script never waits for it or touches the Codex config.
 *
 * Codex's default sandbox hides Launch Services, so a sandboxed `install`
 * can't open the app. It then returns `action: "open-link"` with a link the
 * person clicks in the chat, which Codex opens outside the sandbox. The link
 * is `auto://open` (the app's URL scheme), or `AUTOROUTER_LAUNCH_URL` when a
 * dev slot supplies a launcher that opens its own build.
 *
 * Local development: `AUTOROUTER_APP` names a local build (a dev slot's
 * companion) to open in place of the downloaded app. The launch forwards
 * `CODEX_HOME`, `CLAUDE_CONFIG_DIR` and every `AUTO_*` variable, so that build
 * connects the slot's Codex.
 *
 *   node autorouter-app.mjs status
 *   node autorouter-app.mjs install [--applications DIR] [--force]
 *
 * Every command prints one JSON object on its last line.
 */

import { execFileSync, spawnSync } from "node:child_process";
import { existsSync, mkdtempSync, readFileSync, readdirSync } from "node:fs";
import { homedir, tmpdir } from "node:os";
import { join } from "node:path";
import { parseArgs } from "node:util";

// Read while the entry point runs, so they precede it.
const APP_NAME = "AutoRouter.app";
const DMG_URL = "https://autorouter.com/AutoRouter.dmg";
const DOWNLOAD_PAGE = "https://autorouter.com";
// The Mac app writes this block once its onboarding has connected Codex.
const PROVIDER_MARKER = "# BEGIN AUTO MANAGED PROVIDER";
const LAUNCH_URL = "auto://open";

// -----------------------------------------------------------------------------
// Entry point
// -----------------------------------------------------------------------------

const { positionals, values } = parseArgs({
  allowPositionals: true,
  options: {
    applications: { type: "string", default: "/Applications" },
    force: { type: "boolean", default: false },
  },
});

switch (positionals[0]) {
  case "status":
    print(status(appPath(values.applications)));
    break;
  case "install":
    print(install(values));
    break;
  default:
    console.error("Usage: autorouter-app.mjs status | install");
    process.exit(2);
}

// -----------------------------------------------------------------------------
// Helpers
// -----------------------------------------------------------------------------

/**
 * Whether this computer can run AutoRouter, what is installed, and whether
 * the app has already connected this Codex.
 */
function status(app) {
  const supported = process.platform === "darwin";
  return {
    platform: process.platform,
    supported,
    installed: supported && existsSync(app),
    app,
    version: supported && existsSync(app) ? bundleVersion(app) : null,
    routing: codexRouted(),
    download: DOWNLOAD_PAGE,
  };
}

/**
 * Downloads the signed disk image, checks its signature, copies the app into
 * place, and opens it so its onboarding window appears.
 */
function install({ applications, force }) {
  const target = appPath(applications);
  // AutoRouter is Mac only; report that instead of failing halfway through.
  if (process.platform !== "darwin")
    return { ...status(target), action: "unsupported" };
  // A local build stands in for the download, so there is nothing to copy.
  if (process.env.AUTOROUTER_APP) {
    if (!existsSync(target)) throw new Error(`No app at ${target}.`);
    return opened(target, "local-build");
  }
  if (existsSync(target) && !force) return opened(target, "already-installed");
  const work = mkdtempSync(join(tmpdir(), "autorouter-install-"));
  const image = join(work, "AutoRouter.dmg");
  const mount = join(work, "volume");
  step(`Downloading ${DMG_URL}`);
  execFileSync("curl", ["-fL", "--progress-bar", "-o", image, DMG_URL], {
    stdio: ["ignore", "inherit", "inherit"],
  });
  step("Mounting the disk image");
  execFileSync("hdiutil", [
    "attach",
    image,
    "-nobrowse",
    "-readonly",
    "-quiet",
    "-mountpoint",
    mount,
  ]);
  try {
    const bundle = readdirSync(mount).find((name) => name.endsWith(".app"));
    if (!bundle) throw new Error("The disk image has no app bundle.");
    const source = join(mount, bundle);
    // Refuse a bundle that isn't intact and signed by its developer; Gatekeeper
    // checks the notarization again when the app first opens.
    step("Checking the app's signature");
    execFileSync("codesign", ["--verify", "--deep", "--strict", source]);
    step(`Copying ${bundle} to ${applications}`);
    if (existsSync(target)) quit(target);
    execFileSync("ditto", [source, target]);
  } finally {
    // Detach even after a failure, so a retry can mount the image again.
    spawnSync("hdiutil", ["detach", mount, "-quiet", "-force"]);
  }
  return opened(target, "installed");
}

/**
 * Opens the app after `install` and reports how it went. When the sandbox
 * stops the launch, the result carries the link the person clicks instead,
 * with `installed` saying how the copy itself went.
 */
function opened(app, action) {
  if (launch(app)) return { ...status(app), action, opened: true };
  return {
    ...status(app),
    action: "open-link",
    installed: action,
    opened: false,
    link: process.env.AUTOROUTER_LAUNCH_URL ?? LAUNCH_URL,
  };
}

/** The app to open: a named local build, or the installed copy. */
function appPath(applications) {
  return process.env.AUTOROUTER_APP ?? join(applications, APP_NAME);
}

function codexRouted() {
  try {
    return readFileSync(configPath(), "utf8").includes(PROVIDER_MARKER);
  } catch {
    // No config yet means Codex has never been configured: not routed.
    return false;
  }
}

function configPath() {
  return join(
    process.env.CODEX_HOME ?? join(homedir(), ".codex"),
    "config.toml",
  );
}

function bundleVersion(app) {
  return bundleValue(app, "CFBundleShortVersionString");
}

function bundleValue(app, key) {
  const result = spawnSync("defaults", [
    "read",
    join(app, "Contents/Info"),
    key,
  ]);
  return result.status === 0 ? result.stdout.toString().trim() : null;
}

/**
 * Opens the app with this Codex's home and AutoRouter settings, so its
 * onboarding connects this Codex. `open -n` starts a new instance because
 * `open` drops `--env` when it only activates a running copy.
 */
function launch(app) {
  step("Opening AutoRouter");
  const forwarded = Object.entries(process.env)
    .filter(
      ([key]) =>
        ["CODEX_HOME", "CLAUDE_CONFIG_DIR"].includes(key) ||
        key.startsWith("AUTO_"),
    )
    .flatMap(([key, value]) => ["--env", `${key}=${value}`]);
  const executable = `${app}/Contents/MacOS/`;
  const wasRunning = spawnSync("pgrep", ["-f", executable]).status === 0;
  const result =
    forwarded.length > 0 && !wasRunning
      ? spawnSync("open", ["-n", ...forwarded, app])
      : spawnSync("open", [app]);
  // In the sandbox `open` fails at once (kLSNoExecutableErr); outside it,
  // confirm the process appears before reporting the window is up.
  if (result.status !== 0) {
    step("The sandbox blocked opening the app; the person opens it instead");
    return false;
  }
  for (let tries = 0; tries < 20; tries++) {
    if (spawnSync("pgrep", ["-f", executable]).status === 0) return true;
    spawnSync("sleep", ["0.5"]);
  }
  return false;
}

function quit(app) {
  const id = bundleValue(app, "CFBundleIdentifier");
  if (id) spawnSync("osascript", ["-e", `quit app id "${id}"`]);
}

function step(line) {
  console.error(`→ ${line}`);
}

function print(result) {
  console.log(JSON.stringify(result));
}
