import {
  createWriteStream,
  lstatSync,
  readFileSync,
  readdirSync,
  realpathSync,
  statSync,
} from "node:fs";
import {
  basename,
  delimiter,
  dirname,
  isAbsolute,
  join,
  resolve,
} from "node:path";
import { spawn } from "node:child_process";
import { createHash } from "node:crypto";
import { StringDecoder } from "node:string_decoder";
import { Transform } from "node:stream";
import { fileURLToPath } from "node:url";
import { TextDecoder } from "node:util";

const scriptRoot = dirname(fileURLToPath(import.meta.url));
const script = join(scriptRoot, "meetings_mcp_entrypoint.py");
const isWindows = process.platform === "win32";
const pythonNames = isWindows
  ? ["python.exe", "python3.exe"]
  : ["python3", "python"];
// Match the MCP environment without running its entrypoint or touching client
// stdin. Disable ambient oaipkg missing-import repair in both processes.
const pythonEnvironment = { ...process.env, OAIPKG_DISABLE_META_MISSING: "1" };
const pythonProbe = [
  "import sys",
  "sys.exit(1) if sys.version_info < (3, 10) else None",
  "import ctypes, hashlib, ssl, urllib.request, xml.parsers.expat",
].join("; ");
const pythonProbeTimeoutMs = 2000;
// Admit candidates for three seconds, then let the last probe finish its full
// two-second window. With reaping, selection takes at most 5.1 seconds, leaving
// the MCP's 12-second deadline and two seven-second cleanup periods inside the
// host's 35-second startup budget.
const pythonSelectionAdmissionMs = 3000;
const pythonProbeCleanupMs = 100;
const cacheVersion = /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/u;
const maximumIdentityFileBytes = 64 * 1024;
const maximumRuntimeConfigBytes = 16 * 1024;
const runtimeConfigKeys = [
  "schemaVersion",
  "flavor",
  "distribution",
  "pluginName",
  "marketplaceName",
  "developmentUpdatePolicy",
  "serverName",
  "defaultMcpProfile",
  "appName",
  "bundleIdentifier",
  "appSupportDirectory",
  "controlTarget",
  "teamIdentifier",
  "toolNames",
  "frameworkSymlinks",
  "officialCachePublishers",
];
const runtimeComponent = /^[A-Za-z0-9][A-Za-z0-9._() -]{0,127}$/u;
const runtimeToolName = /^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$/u;
const distributionMarketplaces = Object.freeze({
  internal: "openai-internal-testing",
  external: "openai-curated-remote",
});
const trustedPublishers = Object.values(distributionMarketplaces);
const semanticVersion =
  /^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$/u;

function samePath(first, second) {
  return isWindows
    ? first.toLowerCase() === second.toLowerCase()
    : first === second;
}

function sameDirectoryIdentity(first, second) {
  if (!second.isDirectory() || second.isSymbolicLink()) return false;
  // Some Windows filesystems do not expose stable inode identifiers. A
  // disappearing cache entry remains observable without trusting zeroes.
  return first.ino === 0 || second.ino === 0
    ? first.dev === second.dev
    : first.dev === second.dev && first.ino === second.ino;
}

function scanJSONObjects(source, visit) {
  const objects = [];
  for (let index = 0; index < source.length; index += 1) {
    const character = source[index];
    if (character === "{") {
      objects.push(new Set());
    } else if (character === "}") {
      objects.pop();
    } else if (character === '"') {
      const start = index;
      for (index += 1; source[index] !== '"'; index += 1) {
        if (source[index] === "\\") index += 1;
      }
      let next = index + 1;
      while (/\s/u.test(source[next] ?? "")) next += 1;
      if (source[next] === ":") {
        const key = JSON.parse(source.slice(start, index + 1));
        const keys = objects.at(-1);
        if (
          !keys ||
          visit(keys, key, source, next + 1, objects.length) === false
        )
          return false;
      }
    }
  }
  return true;
}

function parseUniqueJSONObject(bytes) {
  const source = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  const value = JSON.parse(source);
  if (!value || typeof value !== "object" || Array.isArray(value)) return null;

  // JSON.parse discards duplicate keys, while the Python runtime rejects
  // them. Scan parsed JSON strings so escaped spellings compare identically.
  if (
    !scanJSONObjects(source, (keys, key) => {
      if (keys.has(key)) return false;
      keys.add(key);
      return true;
    })
  ) {
    return null;
  }
  return value;
}

function safeRuntimePath(value) {
  return (
    typeof value === "string" &&
    value.length > 0 &&
    !value.includes("\\") &&
    !value.includes("\0") &&
    value
      .split("/")
      .every((part) => part !== "" && part !== "." && part !== "..")
  );
}

function validRuntimeConfig(value) {
  if (
    !value ||
    runtimeConfigKeys.some(
      (key) => !Object.prototype.hasOwnProperty.call(value, key),
    ) ||
    value.schemaVersion !== 1 ||
    [
      "flavor",
      "serverName",
      "defaultMcpProfile",
      "appName",
      "appSupportDirectory",
      "controlTarget",
    ].some(
      (key) =>
        typeof value[key] !== "string" || !runtimeComponent.test(value[key]),
    ) ||
    typeof value.bundleIdentifier !== "string" ||
    !/^[A-Za-z0-9][A-Za-z0-9.-]{0,127}$/u.test(value.bundleIdentifier ?? "") ||
    typeof value.teamIdentifier !== "string" ||
    !/^[A-Z0-9]{10}$/u.test(value.teamIdentifier ?? "") ||
    !value.appName.endsWith(".app")
  ) {
    return false;
  }

  if (
    typeof value.distribution !== "string" ||
    !Object.prototype.hasOwnProperty.call(
      distributionMarketplaces,
      value.distribution,
    ) ||
    value.pluginName !== "chatgpt-meetings" ||
    value.marketplaceName !== distributionMarketplaces[value.distribution] ||
    !["production", "development"].includes(value.flavor) ||
    !["disabled", "local-to-internal"].includes(
      value.developmentUpdatePolicy,
    ) ||
    (value.developmentUpdatePolicy === "local-to-internal" &&
      (value.flavor !== "development" || value.distribution !== "internal")) ||
    (value.flavor === "development" && value.distribution !== "internal")
  ) {
    return false;
  }

  const tools = value.toolNames;
  if (
    !Array.isArray(tools) ||
    tools.length < 1 ||
    tools.length > 32 ||
    new Set(tools).size !== tools.length ||
    tools.some(
      (tool) => typeof tool !== "string" || !runtimeToolName.test(tool),
    )
  ) {
    return false;
  }

  const links = value.frameworkSymlinks;
  if (!Array.isArray(links) || links.length > 16) return false;
  const paths = new Set();
  for (const link of links) {
    if (
      !link ||
      typeof link !== "object" ||
      Array.isArray(link) ||
      Object.keys(link).length !== 2 ||
      !Object.prototype.hasOwnProperty.call(link, "path") ||
      !Object.prototype.hasOwnProperty.call(link, "target") ||
      !safeRuntimePath(link.path) ||
      !safeRuntimePath(link.target) ||
      !link.path.startsWith("Contents/Frameworks/Sentry.framework/") ||
      paths.has(link.path)
    ) {
      return false;
    }
    paths.add(link.path);
  }

  const publishers = value.officialCachePublishers;
  return (
    Array.isArray(publishers) &&
    publishers.length ===
      (value.flavor === "production" ? trustedPublishers.length : 0) &&
    new Set(publishers).size === publishers.length &&
    publishers.every((publisher) => trustedPublishers.includes(publisher))
  );
}

function readIdentity(path, { runtimeConfig = false } = {}) {
  try {
    const metadata = lstatSync(path);
    if (
      !metadata.isFile() ||
      metadata.isSymbolicLink() ||
      metadata.size <= 0 ||
      metadata.size >
        (runtimeConfig
          ? maximumRuntimeConfigBytes
          : maximumIdentityFileBytes) ||
      (!isWindows && (metadata.mode & 0o022) !== 0) ||
      (typeof process.getuid === "function" &&
        metadata.uid !== process.getuid())
    ) {
      return null;
    }
    const bytes = readFileSync(path);
    if (bytes.length !== metadata.size) return null;
    const value = parseUniqueJSONObject(bytes);
    if (!value || (runtimeConfig && !validRuntimeConfig(value))) return null;
    return runtimeConfig
      ? Object.fromEntries(runtimeConfigKeys.map((key) => [key, value[key]]))
      : value;
  } catch {
    return null;
  }
}

function newerPluginVersion(current, candidate) {
  const previous = semanticVersion.exec(current);
  const next = semanticVersion.exec(candidate);
  if (
    !previous ||
    !next ||
    [previous[4], next[4]].some(
      (prerelease) =>
        prerelease &&
        prerelease
          .split(".")
          .some(
            (identifier) =>
              /^[0-9]+$/u.test(identifier) &&
              identifier.length > 1 &&
              identifier.startsWith("0"),
          ),
    )
  ) {
    return false;
  }
  for (let index = 1; index <= 3; index += 1) {
    const before = BigInt(previous[index]);
    const after = BigInt(next[index]);
    if (before !== after) return after > before;
  }

  if (!previous[4] || !next[4]) return Boolean(previous[4]) && !next[4];
  const before = previous[4].split(".");
  const after = next[4].split(".");
  for (
    let index = 0;
    index < Math.max(before.length, after.length);
    index += 1
  ) {
    if (before[index] === undefined) return true;
    if (after[index] === undefined) return false;
    if (before[index] === after[index]) continue;
    const previousNumeric = /^[0-9]+$/u.test(before[index]);
    const nextNumeric = /^[0-9]+$/u.test(after[index]);
    if (previousNumeric !== nextNumeric) return previousNumeric;
    return previousNumeric
      ? BigInt(after[index]) > BigInt(before[index])
      : after[index] > before[index];
  }
  return false;
}

function officialPluginInstallation() {
  try {
    const configuredHome = (process.env.CODEX_HOME || "").trim();
    const userHome = process.env.USERPROFILE || process.env.HOME;
    const codexHome =
      configuredHome || (userHome ? join(userHome, ".codex") : "");
    if (!codexHome || !isAbsolute(codexHome) || codexHome.includes("\0"))
      return null;

    const root = realpathSync(dirname(scriptRoot));
    const family = dirname(root);
    const publisherRoot = dirname(family);
    const cache = dirname(publisherRoot);
    if (!samePath(cache, realpathSync(join(codexHome, "plugins", "cache"))))
      return null;

    const config = readIdentity(join(root, "scripts", "runtime-config.json"), {
      runtimeConfig: true,
    });
    const manifest = readIdentity(join(root, ".codex-plugin", "plugin.json"));
    const publisher = basename(publisherRoot);
    if (
      config?.schemaVersion !== 1 ||
      config.flavor !== "production" ||
      config.pluginName !== basename(family) ||
      config.marketplaceName !== publisher ||
      config.serverName !== basename(family) ||
      !Array.isArray(config.officialCachePublishers) ||
      !config.officialCachePublishers.includes(publisher) ||
      manifest?.name !== config.serverName ||
      manifest.version !== basename(root) ||
      !cacheVersion.test(basename(root))
    ) {
      return null;
    }

    const rootIdentity = lstatSync(root);
    const familyIdentity = lstatSync(family);
    if (
      [rootIdentity, familyIdentity].some(
        (value) => !value.isDirectory() || value.isSymbolicLink(),
      )
    ) {
      return null;
    }
    return { config, family, familyIdentity, publisher, root, rootIdentity };
  } catch {
    // Source checkouts, private publishers, and incomplete installations do
    // not have installer-owned update authority and must remain untouched.
    return null;
  }
}

function officialPluginWasReplaced(installation) {
  if (!installation) return false;
  try {
    if (
      !sameDirectoryIdentity(
        installation.familyIdentity,
        lstatSync(installation.family),
      ) ||
      !samePath(realpathSync(installation.family), installation.family)
    ) {
      return false;
    }

    try {
      const current = lstatSync(installation.root);
      if (sameDirectoryIdentity(installation.rootIdentity, current))
        return false;
      if (!current.isDirectory() || current.isSymbolicLink()) return false;
    } catch (error) {
      if (error?.code !== "ENOENT" && error?.code !== "ENOTDIR") return false;
    }

    const candidates = [];
    for (const entry of readdirSync(installation.family, {
      withFileTypes: true,
    })) {
      if (!cacheVersion.test(entry.name)) continue;
      if (entry.isSymbolicLink() || !entry.isDirectory()) return false;
      const candidate = join(installation.family, entry.name);
      const metadata = lstatSync(candidate, { bigint: true });
      if (!metadata.isDirectory() || metadata.isSymbolicLink()) return false;
      if (!samePath(dirname(realpathSync(candidate)), installation.family))
        return false;
      const empty = readdirSync(candidate).length === 0;
      if (empty) {
        const rechecked = lstatSync(candidate, { bigint: true });
        if (
          !rechecked.isDirectory() ||
          rechecked.isSymbolicLink() ||
          rechecked.dev !== metadata.dev ||
          rechecked.ino !== metadata.ino ||
          rechecked.ctimeNs !== metadata.ctimeNs ||
          rechecked.mtimeNs !== metadata.mtimeNs ||
          !samePath(dirname(realpathSync(candidate)), installation.family) ||
          readdirSync(candidate).length !== 0
        ) {
          return false;
        }
      }
      candidates.push({ path: candidate, metadata, empty });
    }
    // An old, unchanged empty cache tombstone is not an installed successor.
    // New empty contenders may still be staging and must remain fail-closed.
    const installed = candidates.filter((candidate) => !candidate.empty);
    if (installed.length !== 1) return false;
    const selected = installed[0];
    const selectedCreated =
      selected.metadata.birthtimeNs > 0n
        ? selected.metadata.birthtimeNs
        : selected.metadata.ctimeNs;
    if (
      candidates.some((candidate) => {
        if (!candidate.empty) return false;
        const created =
          candidate.metadata.birthtimeNs > 0n
            ? candidate.metadata.birthtimeNs
            : candidate.metadata.ctimeNs;
        return created >= selectedCreated;
      })
    ) {
      return false;
    }

    const successor = selected.path;
    const successorScripts = join(successor, "scripts");
    const successorPluginMetadata = join(successor, ".codex-plugin");
    for (const directory of [successorScripts, successorPluginMetadata]) {
      const metadata = lstatSync(directory);
      if (!metadata.isDirectory() || metadata.isSymbolicLink()) return false;
    }
    for (const name of [
      "start_meetings_mcp.mjs",
      "meetings_mcp_entrypoint.py",
      "meetings_mcp.py",
    ]) {
      const metadata = lstatSync(join(successorScripts, name));
      if (!metadata.isFile() || metadata.isSymbolicLink()) return false;
    }

    const manifest = readIdentity(join(successorPluginMetadata, "plugin.json"));
    const config = readIdentity(join(successorScripts, "runtime-config.json"), {
      runtimeConfig: true,
    });
    if (
      manifest?.name !== installation.config.serverName ||
      manifest.version !== basename(successor) ||
      !newerPluginVersion(basename(installation.root), manifest.version) ||
      !Array.isArray(config?.officialCachePublishers) ||
      !config.officialCachePublishers.includes(installation.publisher)
    ) {
      return false;
    }
    return [
      "schemaVersion",
      "flavor",
      "distribution",
      "pluginName",
      "marketplaceName",
      "developmentUpdatePolicy",
      "serverName",
      "defaultMcpProfile",
      "appName",
      "bundleIdentifier",
      "teamIdentifier",
      "appSupportDirectory",
      "controlTarget",
    ].every((key) => config[key] === installation.config[key]);
  } catch {
    return false;
  }
}

function usable(path) {
  if (!path) return null;
  try {
    const canonical = realpathSync(path);
    if (/(?:^|[\\/])WindowsApps(?:[\\/]|$)/i.test(canonical)) return null;
    return statSync(canonical).isFile() ? canonical : null;
  } catch {
    return null;
  }
}

function* commandPaths(command) {
  if (!command) return;
  if (/[\\/]/.test(command)) {
    yield command;
    return;
  }
  const extensions = isWindows ? ["", ".exe"] : [""];
  for (const directory of (process.env.PATH || "").split(delimiter)) {
    if (!directory) continue;
    for (const extension of extensions) {
      yield join(directory, `${command}${extension}`);
    }
  }
}

function dependencyCandidates(root) {
  return isWindows
    ? [
        join(root, "python", "python.exe"),
        join(root, "dependencies", "python", "python.exe"),
        join(root, "python.exe"),
      ]
    : [
        join(root, "python", "bin", "python3"),
        join(root, "dependencies", "python", "bin", "python3"),
        join(root, "bin", "python3"),
      ];
}

function* pythonCandidatePaths() {
  const roots = [
    process.env.CODEX_RUNTIME_DEPENDENCIES,
    process.env.CODEX_WORKSPACE_DEPENDENCIES,
    process.env.CODEX_DEPENDENCIES,
  ].filter(Boolean);
  const home = process.env.USERPROFILE || process.env.HOME;
  if (home)
    roots.push(
      join(
        home,
        ".cache",
        "codex-runtimes",
        "codex-primary-runtime",
        "dependencies",
      ),
    );
  for (const root of roots) {
    yield* dependencyCandidates(root);
  }
  for (const name of pythonNames) {
    yield* commandPaths(name);
  }
}

function* usableCandidates(paths) {
  for (const path of paths) {
    const candidate = usable(path);
    if (candidate) yield candidate;
  }
}

function probePython(candidate, timeoutMs, signal, cwd) {
  return new Promise((resolveProbe, rejectProbe) => {
    let probe;
    let timeout;
    let cleanup;
    let stopped = false;
    let finished = false;
    const finish = (failure) => {
      if (finished) return;
      finished = true;
      clearTimeout(timeout);
      clearTimeout(cleanup);
      signal.removeEventListener("abort", stop);
      resolveProbe(failure);
    };
    const stop = () => {
      if (finished || stopped) return;
      stopped = true;
      try {
        probe.kill("SIGKILL");
      } catch {
        // The owned probe can exit concurrently with cancellation or timeout.
      }
      cleanup = setTimeout(() => {
        if (finished) return;
        finished = true;
        clearTimeout(timeout);
        signal.removeEventListener("abort", stop);
        rejectProbe(new Error("Python runtime probe could not be stopped"));
      }, pythonProbeCleanupMs);
    };
    try {
      probe = spawn(candidate, ["-B", "-c", pythonProbe], {
        cwd,
        env: pythonEnvironment,
        stdio: "ignore",
        windowsHide: true,
      });
    } catch {
      finish("could not be started");
      return;
    }
    probe.once("error", () => {
      // A failed kill must still wait for exit or fail the bounded cleanup;
      // it cannot admit another probe while this child might remain alive.
      if (!stopped) finish("could not be started");
    });
    probe.once("exit", (code, exitSignal) => {
      finish(
        stopped
          ? "probe timed out"
          : exitSignal
            ? `signal ${exitSignal}`
            : code === 0
              ? null
              : `exit ${code}`,
      );
    });
    timeout = setTimeout(stop, timeoutMs);
    signal.addEventListener("abort", stop, { once: true });
    if (signal.aborted) stop();
  });
}

async function findPython(signal, cwd, candidatesAtLaunch) {
  signal.throwIfAborted();
  const override = (process.env.CHATGPT_MEETINGS_PYTHON || "").trim();
  const paths =
    candidatesAtLaunch ??
    (override ? commandPaths(override) : pythonCandidatePaths());
  const candidates = usableCandidates(paths);
  if (override) {
    const resolved = candidates.next().value;
    if (!resolved)
      throw new Error("CHATGPT_MEETINGS_PYTHON is not a usable Python runtime");
    // An explicit interpreter keeps the existing MCP startup allowance. Its
    // single startup remains fail-closed, with no automatic fallback or retry.
    return resolved;
  }

  const deadline = performance.now() + pythonSelectionAdmissionMs;
  const seen = new Set();
  while (performance.now() < deadline) {
    const { value: candidate, done } = candidates.next();
    if (done) break;
    const identity = isWindows ? candidate.toLowerCase() : candidate;
    if (seen.has(identity)) continue;
    seen.add(identity);
    signal.throwIfAborted();
    if (performance.now() >= deadline) break;
    const failure = await probePython(
      candidate,
      pythonProbeTimeoutMs,
      signal,
      cwd,
    );
    signal.throwIfAborted();
    if (!failure) return candidate;
    // A rejected binary can emit private paths or arbitrary diagnostics. Only
    // the process outcome is safe here; stdout remains exclusively MCP traffic.
    console.error(
      `ChatGPT Meetings skipped an unusable Python runtime (${failure})`,
    );
  }
  throw new Error("no usable Python runtime was found for ChatGPT Meetings");
}

function windowsWorkingDirectory() {
  const candidates = [
    process.env.CODEX_HOME,
    process.env.LOCALAPPDATA,
    process.env.USERPROFILE,
    process.env.HOME,
    process.env.TEMP,
  ];
  for (const value of candidates) {
    if (typeof value !== "string" || value.length === 0 || value.length > 4096)
      continue;
    if (value.includes("\0") || !isAbsolute(value)) continue;
    try {
      const absolute = resolve(value);
      const canonical = realpathSync(absolute);
      // A junction/symlink anywhere in the candidate changes its real path.
      // Never chdir through one: the long-lived launcher and child must not
      // pin an attacker-controlled directory or a replaceable cache entry.
      if (canonical.toLowerCase() !== absolute.toLowerCase()) continue;
      const metadata = lstatSync(absolute);
      if (!metadata.isDirectory() || metadata.isSymbolicLink()) continue;
      if (/(?:^|[\\/])plugins[\\/]cache(?:[\\/]|$)/i.test(canonical)) continue;
      return canonical;
    } catch {
      continue;
    }
  }
  throw new Error(
    "no safe Windows working directory was found for ChatGPT Meetings",
  );
}

function redactPythonStderr(runtime) {
  const privatePath = Buffer.from(runtime);
  let pending = Buffer.alloc(0);
  return new Transform({
    transform(chunk, _encoding, done) {
      const output = Buffer.concat([pending, chunk]);
      let offset = 0;
      for (
        let match = output.indexOf(privatePath);
        match !== -1;
        match = output.indexOf(privatePath, offset)
      ) {
        this.push(output.subarray(offset, match));
        this.push("Python runtime could not be started");
        offset = match + privatePath.length;
      }
      const safeEnd = Math.max(offset, output.length - privatePath.length + 1);
      this.push(output.subarray(offset, safeEnd));
      pending = output.subarray(safeEnd);
      done();
    },
    flush(done) {
      this.push(pending);
      done();
    },
  });
}

let python;
let workingDirectory;
let installedPlugin;
const selectionAbort = new AbortController();
const cancelSelection = () => selectionAbort.abort();
for (const signal of ["SIGINT", "SIGTERM"]) process.on(signal, cancelSelection);
process.stdin.once("close", cancelSelection);
process.stdin.once("end", cancelSelection);
process.stdout.once("close", cancelSelection);
// Detect an empty, orderly EOF during selection without consuming protocol
// bytes. Nonempty input stays buffered until it can be piped to the MCP.
process.stdin.read(0);
try {
  let candidatesAtLaunch;
  if (isWindows) {
    // Resolve relative and drive-relative paths before changing either cwd.
    // Keep filesystem checks lazy so a healthy preferred runtime never waits
    // on an unused PATH directory, which can be an unavailable network share.
    const override = (process.env.CHATGPT_MEETINGS_PYTHON || "").trim();
    candidatesAtLaunch = Array.from(
      override ? commandPaths(override) : pythonCandidatePaths(),
      (path) => resolve(path),
    );
    workingDirectory = windowsWorkingDirectory();
    // .mcp.json initially starts Node in the installed plugin directory.
    // Releasing that cwd before the session becomes long lived lets Codex
    // atomically refresh its Windows plugin cache while the MCP is active.
    process.chdir(workingDirectory);
  }
  installedPlugin = officialPluginInstallation();
  python = await findPython(
    selectionAbort.signal,
    workingDirectory,
    candidatesAtLaunch,
  );
} catch (error) {
  if (selectionAbort.signal.aborted) process.exit(0);
  console.error(`ChatGPT Meetings MCP launch failed: ${error.message}`);
  process.exit(1);
} finally {
  for (const signal of ["SIGINT", "SIGTERM"])
    process.removeListener(signal, cancelSelection);
  process.stdin.removeListener("close", cancelSelection);
  process.stdin.removeListener("end", cancelSelection);
  process.stdout.removeListener("close", cancelSelection);
}

// Windows process.stdout/stderr use synchronous pipe writes. Keep host output
// off the event loop so an abandoned reader cannot block owned-child cleanup.
const hostStdout = isWindows
  ? createWriteStream(null, { fd: 1, autoClose: false })
  : process.stdout;
const hostStderr = isWindows
  ? createWriteStream(null, { fd: 2, autoClose: false })
  : process.stderr;
let launchFailed = false;

async function failLaunch() {
  launchFailed = true;
  process.exitCode = 1;
  // A failed spawn owns no Python process. Give a healthy diagnostic reader
  // its complete message, but bound a closed or permanently full host pipe.
  const deadline = setTimeout(() => forceLauncherExit(1), 1000);
  await new Promise((done) => {
    hostStderr.once("error", done);
    hostStderr.write(
      "ChatGPT Meetings MCP launch failed: Python runtime could not be started\n",
      done,
    );
  });
  clearTimeout(deadline);
  process.exit(1);
}

let child;
try {
  child = spawn(python, ["-u", script, ...process.argv.slice(2)], {
    cwd: workingDirectory,
    env: pythonEnvironment,
    stdio: ["pipe", "pipe", "pipe"],
    windowsHide: true,
  });
} catch {
  await failLaunch();
}

const redactedStderr = redactPythonStderr(python);
child.stderr.pipe(redactedStderr).pipe(hostStderr, { end: false });

const maximumObservedRequestFrameBytes = 1 * 1024 * 1024;
const maximumObservedResponseFrameBytes = 32 * 1024 * 1024;
const maximumRPCIDBytes = 4 * 1024;
const maximumPendingRequests = 1024;
const startupTimeoutMs = boundedDuration(
  process.env.CHATGPT_MEETINGS_MCP_STARTUP_TIMEOUT_MS,
  // Leave both owned-child cleanup grace periods inside the host's 35-second
  // MCP startup deadline, even when it keeps an abandoned stdio session open.
  12 * 1000,
);
const requestTimeoutMs = boundedDuration(
  process.env.CHATGPT_MEETINGS_MCP_REQUEST_TIMEOUT_MS,
  4 * 60 * 1000,
);
const terminationGraceMs = boundedDuration(
  process.env.CHATGPT_MEETINGS_MCP_TERMINATION_GRACE_MS,
  // Cover the RPC drain, the auth manager's three-second worker join, and
  // its owned app-server's bounded TERM/KILL and reader cleanup budgets.
  7 * 1000,
);
const pendingRequests = new Map();
let terminating = false;
let terminationExitCode;
let pendingStdioDisconnect;
let pendingClientDisconnect;
let pendingTermination;
let pendingForcedTermination;
let pendingLauncherExit;
let pendingDiagnosticRelease;
let startupRequestID;
let startupResponseObserved = false;
let startupResponsePending = false;
let startupResponseDelivered = false;
let startupClientAcknowledged = false;
let startupComplete = false;

function boundedDuration(value, fallback) {
  if (value === undefined || value === "") return fallback;
  const parsed = Number(value);
  return Number.isSafeInteger(parsed) &&
    parsed >= 50 &&
    parsed <= 24 * 60 * 60 * 1000
    ? parsed
    : fallback;
}

function rpcID(value, frame) {
  if (typeof value === "string") {
    return Buffer.byteLength(value) <= maximumRPCIDBytes
      ? `string:${value}`
      : `long-string:${createHash("sha256").update(value).digest("hex")}`;
  }
  if (typeof value === "number" && Number.isFinite(value)) {
    if (!Number.isInteger(value)) return `number:${value}`;
    if (Number.isSafeInteger(value)) return `integer:${value}`;

    let exact = null;
    scanJSONObjects(frame, (_keys, key, source, start, depth) => {
      if (depth === 1 && key === "id") {
        exact =
          /^\s*(-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?)/u.exec(
            source.slice(start),
          )?.[1];
      }
      return true;
    });
    // Python compares integral floats and integers by their exact numeric
    // value. Preserve arbitrary integer spelling before JavaScript rounds it.
    return `integer:${BigInt(/^-?(?:0|[1-9][0-9]*)$/u.test(exact ?? "") ? exact : value)}`;
  }
  return null;
}

function observeFrames(stream, maximumFrameBytes, onFrame) {
  const decoder = new StringDecoder("utf8");
  let buffered = "";
  let bufferedBytes = 0;
  let droppingOversized = false;
  stream.on("data", (chunk) => {
    const decoded = decoder.write(chunk);
    buffered += decoded;
    bufferedBytes += Buffer.byteLength(decoded);
    while (true) {
      const newline = buffered.indexOf("\n");
      if (newline < 0) {
        if (bufferedBytes > maximumFrameBytes) {
          buffered = "";
          bufferedBytes = 0;
          droppingOversized = true;
        }
        return;
      }
      const line = buffered.slice(0, newline);
      buffered = buffered.slice(newline + 1);
      const lineBytes = Buffer.byteLength(line);
      bufferedBytes -= lineBytes + 1;
      if (droppingOversized) {
        droppingOversized = false;
        continue;
      }
      if (lineBytes > maximumFrameBytes) continue;
      try {
        onFrame(JSON.parse(line), line);
      } catch {
        // The Python server owns parse errors; the watchdog must remain a
        // transparent observer and never turn an invalid frame into a crash.
      }
    }
  });
}

// Start at MCP child launch, not receipt of initialize: an abandoned host can
// retain both stdio endpoints without ever sending its first protocol frame.
const startupDeadline = setTimeout(
  () => terminate("startup deadline"),
  startupTimeoutMs,
);
startupDeadline.unref();

function completeStartupHandshake() {
  if (
    terminating ||
    startupComplete ||
    !startupResponseDelivered ||
    !startupClientAcknowledged
  ) {
    return;
  }
  startupComplete = true;
  clearTimeout(startupDeadline);
}

observeFrames(
  process.stdin,
  maximumObservedRequestFrameBytes,
  (message, frame) => {
    if (!message || typeof message !== "object") return;
    const id = rpcID(message.id, frame);
    if (
      startupResponseObserved &&
      !startupComplete &&
      message.jsonrpc === "2.0" &&
      !Object.prototype.hasOwnProperty.call(message, "result") &&
      !Object.prototype.hasOwnProperty.call(message, "error") &&
      ((message.method === "notifications/initialized" &&
        !Object.prototype.hasOwnProperty.call(message, "id")) ||
        (typeof message.method === "string" &&
          message.method !== "initialize" &&
          !message.method.startsWith("notifications/") &&
          message.method !== "$/cancelRequest" &&
          id !== null))
    ) {
      // Codex sends initialized only after consuming the initialize reply.
      // Accept a later real request as the equivalent legacy-client proof.
      startupClientAcknowledged = true;
      completeStartupHandshake();
    }
    if (typeof message.method === "string" && id !== null) {
      if (
        !pendingRequests.has(id) &&
        pendingRequests.size >= maximumPendingRequests
      ) {
        terminate("request capacity");
        return;
      }
      // A duplicate in-flight id is invalid JSON-RPC, but it must not be able
      // to keep a wedged child alive by continually resetting its deadline.
      if (!pendingRequests.has(id)) pendingRequests.set(id, Date.now());
      if (message.method === "initialize" && startupRequestID === undefined) {
        startupRequestID = id;
      }
      return;
    }
    // A cancellation is advisory. Keep its original deadline until the child
    // actually responds so an ignored cancellation plus heartbeat traffic
    // cannot retain a wedged session indefinitely.
  },
);
process.stdin.pipe(child.stdin);
// Register the forwarding listener first so its real write is queued before
// the zero-byte delivery checkpoint in the response observer below.
child.stdout.pipe(hostStdout, { end: false });
observeFrames(
  child.stdout,
  maximumObservedResponseFrameBytes,
  (message, frame) => {
    if (
      !message ||
      typeof message !== "object" ||
      typeof message.method === "string"
    )
      return;
    const id = rpcID(message.id, frame);
    if (id === null) return;
    if (id === startupRequestID && !startupComplete) {
      if (
        terminating ||
        startupResponsePending ||
        message.jsonrpc !== "2.0" ||
        !Object.prototype.hasOwnProperty.call(message, "result") ||
        Object.prototype.hasOwnProperty.call(message, "error") ||
        typeof message.result !== "object" ||
        message.result === null ||
        Array.isArray(message.result)
      ) {
        return;
      }
      startupResponseObserved = true;
      startupResponsePending = true;
      hostStdout.write("", (error) => {
        startupResponsePending = false;
        if (terminating) return;
        if (error || hostStdout.destroyed || hostStdout.writableEnded) {
          terminate("stdio disconnect");
          return;
        }
        pendingRequests.delete(id);
        startupResponseDelivered = true;
        completeStartupHandshake();
      });
      return;
    }
    pendingRequests.delete(id);
  },
);
const observeClientDisconnect = () => {
  if (terminating || pendingClientDisconnect) return;
  clearTimeout(startupDeadline);
  // Once the host disconnects, outstanding requests can no longer outlive a
  // client. Their watchdog must not interrupt Python's owned-child cleanup.
  clearInterval(watchdog);
  // The ordinary pipe already forwards EOF to Python. Preserve its natural
  // exit and final response; intervene only if that owned session wedges.
  pendingClientDisconnect = setTimeout(
    () => terminate("client disconnect", { expected: true }),
    terminationGraceMs,
  );
  pendingClientDisconnect.unref();
};
process.stdin.once("end", observeClientDisconnect);
process.stdin.once("close", observeClientDisconnect);
child.stdin.once("error", (error) => {
  if (terminating) return;
  if (error.code !== "EPIPE") {
    terminate("stdio disconnect");
    return;
  }
  if (child.exitCode !== null || child.signalCode !== null) return;

  // A normally exiting child can close stdin before its final reply drains.
  pendingStdioDisconnect = setTimeout(
    () => {
      if (child.exitCode === null && child.signalCode === null) {
        terminate("stdio disconnect");
      }
    },
    Math.min(terminationGraceMs, 1000),
  );
  pendingStdioDisconnect.unref();
});

function signalChild(signal) {
  if (child.exitCode !== null || child.signalCode !== null) return;
  try {
    child.kill(signal);
  } catch {
    // Child exit can race its exact owned-process signal.
  }
}

function scheduleRetiredLauncherExit() {
  if (!terminating || pendingLauncherExit) return;
  // A full host pipe can prevent ChildProcess "close" indefinitely even after
  // the exact owned Python child exits. Never apply this bound to healthy
  // sessions: their final multi-megabyte replies must drain completely.
  pendingLauncherExit = setTimeout(
    () => forceLauncherExit(terminationExitCode),
    Math.min(terminationGraceMs, 1000),
  );
  pendingLauncherExit.unref();
}

function forceLauncherExit(code) {
  // Called only after Python exits or fails to spawn. A Windows async fd write
  // can block in the thread pool and prevent process.exit from finishing.
  if (isWindows) process.kill(process.pid, "SIGKILL");
  else process.exit(code);
}

function releaseStalledDiagnostics() {
  if (!terminating || !redactedStderr.isPaused() || pendingDiagnosticRelease)
    return;
  pendingDiagnosticRelease = setTimeout(
    () => {
      pendingDiagnosticRelease = undefined;
      if (!redactedStderr.isPaused()) return;
      // A retired session's blocked host must not stop Python from reaping its
      // helper. Keep the redactor flowing without retaining additional bytes.
      redactedStderr.unpipe(hostStderr);
      redactedStderr.resume();
    },
    Math.min(terminationGraceMs / 2, 1000),
  );
  pendingDiagnosticRelease.unref();
}
redactedStderr.on("pause", releaseStalledDiagnostics);
redactedStderr.on("resume", () => {
  clearTimeout(pendingDiagnosticRelease);
  pendingDiagnosticRelease = undefined;
});

function terminate(reason, { expected = false } = {}) {
  if (terminating || launchFailed) return;
  terminating = true;
  terminationExitCode = expected ? 0 : 1;
  // An errored host stream can let Node exit before either drain callback.
  process.exitCode = terminationExitCode;
  clearTimeout(startupDeadline);
  clearTimeout(pendingStdioDisconnect);
  clearTimeout(pendingClientDisconnect);
  hostStderr.write(`ChatGPT Meetings MCP session closed after ${reason}\n`);
  // Stop forwarding a live client's heartbeats into a child that is already
  // being reaped. In particular, a Windows pipe can otherwise keep the
  // launcher/child stdio pair alive across forceful process termination.
  process.stdin.unpipe(child.stdin);
  process.stdin.pause();
  // Retirement also covers expected shutdowns whose host stopped reading.
  // Release stdout so Python can finish a blocked write and reap
  // its auth helper. Ordinary EOF gets its final-response grace before here.
  child.stdout.unpipe(hostStdout);
  child.stdout.resume();
  // Preserve the redactor's tail and cleanup diagnostics while the host reads.
  // Release a persistently blocked destination inside the child cleanup grace.
  releaseStalledDiagnostics();
  // Every retirement reason must first give Python's independent stdin reader
  // an opportunity to reap its exact owned Codex app-server. Signals cannot
  // otherwise reach a detached POSIX grandchild or a Windows child tree.
  child.stdin.end();
  if (child.exitCode !== null || child.signalCode !== null) {
    scheduleRetiredLauncherExit();
    return;
  }
  pendingTermination = setTimeout(() => {
    signalChild("SIGTERM");
    pendingForcedTermination = setTimeout(
      () => signalChild("SIGKILL"),
      terminationGraceMs,
    );
    pendingForcedTermination.unref();
  }, terminationGraceMs);
  pendingTermination.unref();
}

const watchdog = setInterval(
  () => {
    const now = Date.now();
    let oldestRequest = now;
    for (const startedAt of pendingRequests.values()) {
      oldestRequest = Math.min(oldestRequest, startedAt);
    }
    if (pendingRequests.size > 0 && now - oldestRequest >= requestTimeoutMs) {
      terminate("request deadline");
    } else if (
      pendingRequests.size === 0 &&
      hostStdout.writableLength === 0 &&
      officialPluginWasReplaced(installedPlugin)
    ) {
      // A complete response can still be queued for a connected slow reader.
      // Updating the plugin does not authorize discarding that host output.
      // Retire this launcher and its own Python MCP child only. An active
      // native recorder belongs to the authenticated update/handoff flow and
      // must never be stopped by stale-session cleanup.
      terminate("plugin update", { expected: true });
    }
  },
  Math.min(1000, requestTimeoutMs),
).unref();
for (const signal of ["SIGINT", "SIGTERM"]) {
  process.on(signal, () => terminate("client shutdown", { expected: true }));
}
for (const output of [hostStdout, hostStderr]) {
  output.on("error", () => terminate("stdio disconnect"));
}
child.once("error", failLaunch);
child.once("exit", () => {
  scheduleRetiredLauncherExit();
  finishAfterChildExit();
});
child.stdout.once("end", finishAfterChildExit);
function finishAfterChildExit() {
  if (
    launchFailed ||
    (child.exitCode === null && child.signalCode === null) ||
    !child.stdout.readableEnded
  ) {
    return;
  }
  // ChildProcess close also waits for stderr. Finish once Python has exited
  // and stdout has ended, so blocked diagnostics cannot prevent this drain.
  clearTimeout(pendingStdioDisconnect);
  clearTimeout(pendingTermination);
  clearTimeout(pendingForcedTermination);
  clearInterval(watchdog);
  // Expected client/update shutdowns are not reconnect-worthy failures, while
  // deadline, capacity, and unhealthy-session watchdog exits remain visible.
  // Keep the EOF deadline until the host actually drains its final output.
  hostStdout.write("", (error) => {
    if (error) terminate("stdio disconnect");
    clearTimeout(pendingClientDisconnect);
    const exitCode = terminating ? terminationExitCode : child.exitCode ?? 1;
    // Stdout has drained and Python is gone. Preserve ordinary stderr, but do
    // not let an abandoned diagnostic pipe retain the launcher indefinitely.
    const stderrDeadline = setTimeout(
      () => forceLauncherExit(exitCode),
      Math.min(terminationGraceMs, 1000),
    );
    stderrDeadline.unref();
    const finishStderr = () => {
      hostStderr.write("", () => {
        clearTimeout(stderrDeadline);
        clearTimeout(pendingLauncherExit);
        process.exit(exitCode);
      });
    };
    // The child's diagnostic pipe can still contain bytes after its process
    // exits. Checkpoint only once the redactor has forwarded its final tail.
    if (redactedStderr.readableEnded) finishStderr();
    else redactedStderr.once("end", finishStderr);
  });
}
