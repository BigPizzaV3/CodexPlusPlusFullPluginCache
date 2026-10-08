#!/usr/bin/env node
import { createHash, randomUUID } from "node:crypto";
import {
  constants,
  copyFileSync,
  cpSync,
  lstatSync,
  readFileSync,
  readdirSync,
  realpathSync,
  renameSync,
  rmSync,
} from "node:fs";
import { homedir } from "node:os";
import { dirname, isAbsolute, join, relative, resolve } from "node:path";
import process from "node:process";
import { fileURLToPath, pathToFileURL } from "node:url";

const EXECUTABLE_NAME = "ChatGPT Meetings.exe";
const OFFICIAL_WINDOWS_PUBLISHERS = Object.freeze([
  "openai-internal-testing",
  "openai-curated-remote",
]);
const SHA256 = /^[a-f0-9]{64}$/u;

export function windowsPlatform(
  environment = process.env,
  architecture = process.arch,
) {
  const machine = (
    environment.PROCESSOR_ARCHITEW6432 ||
    environment.PROCESSOR_ARCHITECTURE ||
    architecture
  )
    .trim()
    .toLowerCase();
  if (["amd64", "x86_64", "x64"].includes(machine)) return "windows-x64";
  if (["arm64", "aarch64"].includes(machine)) return "windows-arm64";
  throw new Error(`unsupported Windows architecture: ${machine || "unknown"}`);
}

function regularFile(path, label) {
  const metadata = lstatSync(path);
  if (!metadata.isFile() || metadata.isSymbolicLink()) {
    throw new Error(`${label} is not a regular file`);
  }
  return metadata;
}

function sha256(path) {
  return createHash("sha256").update(readFileSync(path)).digest("hex");
}

function readWindowsLicenses(directory) {
  const actual = Object.create(null);
  function visit(current, prefix = "") {
    const metadata = lstatSync(current);
    if (
      !metadata.isDirectory() ||
      metadata.isSymbolicLink() ||
      realpathSync(current) !== current
    ) {
      throw new Error("Windows license directory is unsafe");
    }
    for (const name of readdirSync(current)) {
      const path = join(current, name);
      const relativePath = prefix ? `${prefix}/${name}` : name;
      const child = lstatSync(path);
      if (child.isSymbolicLink())
        throw new Error("Windows license file is unsafe");
      if (child.isDirectory()) visit(path, relativePath);
      else {
        regularFile(path, "Windows license");
        actual[relativePath] = sha256(path);
      }
    }
  }
  visit(directory);
  return actual;
}

function windowsLicensesMatch(actual, expected) {
  return (
    Object.keys(actual).length === Object.keys(expected).length &&
    Object.entries(expected).every(([path, digest]) => actual[path] === digest)
  );
}

function verifyWindowsLicenses(directory, expected) {
  if (!windowsLicensesMatch(readWindowsLicenses(directory), expected)) {
    throw new Error("Windows licenses failed digest verification");
  }
}

function existingWindowsLicenses(directory) {
  try {
    lstatSync(directory);
  } catch (error) {
    if (error?.code === "ENOENT") return undefined;
    throw error;
  }
  return readWindowsLicenses(directory);
}

class WindowsLicensePublicationError extends Error {}

function prepareWindowsLicensesOnce(root, platform, entry, backups) {
  const expected = entry.thirdPartyLicenses;
  if (expected === undefined) return; // Historical bundles predate native notices.
  if (
    expected === null ||
    typeof expected !== "object" ||
    Array.isArray(expected) ||
    Object.keys(expected).length === 0 ||
    Object.values(expected).some(
      (digest) => typeof digest !== "string" || !SHA256.test(digest),
    )
  ) {
    throw new Error("Windows license manifest is malformed");
  }
  const source = join(root, "native", platform, "THIRD_PARTY_LICENSES");
  const target = join(root, "THIRD_PARTY_LICENSES_WINDOWS");
  verifyWindowsLicenses(source, expected);
  const current = existingWindowsLicenses(target);
  if (current !== undefined && windowsLicensesMatch(current, expected)) return;
  const temporary = join(
    root,
    `.THIRD_PARTY_LICENSES_WINDOWS.${randomUUID()}.tmp`,
  );
  const backup = `${temporary}.previous`;
  let backedUp = false;
  let installed = false;
  let published = false;
  let publishing = false;
  let stagedIdentity;
  try {
    cpSync(source, temporary, {
      recursive: true,
      errorOnExist: true,
      force: false,
      dereference: false,
    });
    verifyWindowsLicenses(temporary, expected);
    stagedIdentity = lstatSync(temporary);
    publishing = true;
    // Recheck after staging: another launcher may already have published it.
    const previous = existingWindowsLicenses(target);
    if (previous !== undefined && windowsLicensesMatch(previous, expected))
      return;
    if (previous !== undefined) {
      renameSync(target, backup);
      backedUp = true;
      backups.add(backup);
      const displaced = readWindowsLicenses(backup);
      if (
        !windowsLicensesMatch(displaced, previous) &&
        !windowsLicensesMatch(displaced, expected)
      ) {
        throw new Error("Windows licenses changed before replacement");
      }
    }
    try {
      renameSync(temporary, target);
      installed = true;
    } catch (error) {
      try {
        verifyWindowsLicenses(target, expected);
      } catch {
        throw error;
      }
    }
    verifyWindowsLicenses(target, expected);
    published = true;
  } catch (error) {
    if (backedUp) {
      // Restore only our staged directory or an absent destination. Never
      // overwrite a different directory published by a concurrent launcher.
      let restorePrevious = !installed;
      if (installed) {
        let targetIdentity;
        try {
          targetIdentity = lstatSync(target);
        } catch (identityError) {
          if (identityError?.code !== "ENOENT") throw identityError;
        }
        if (
          targetIdentity?.isDirectory() &&
          !targetIdentity.isSymbolicLink() &&
          realpathSync(target) === target &&
          targetIdentity.dev === stagedIdentity.dev &&
          targetIdentity.ino === stagedIdentity.ino
        ) {
          renameSync(target, temporary);
          restorePrevious = true;
        }
      }
      // A missing directory after successful publication means another
      // launcher moved it. Retry the verified source instead of restoring old bytes.
      if (restorePrevious && existingWindowsLicenses(target) === undefined) {
        renameSync(backup, target);
        backedUp = false;
        backups.delete(backup);
      }
    }
    if (publishing)
      throw new WindowsLicensePublicationError(
        "Windows license publication failed",
        { cause: error },
      );
    throw error;
  } finally {
    rmSync(temporary, { recursive: true, force: true });
    if (published && backedUp) {
      rmSync(backup, { recursive: true, force: true });
      backups.delete(backup);
    }
  }
}

function prepareWindowsLicenses(root, platform, entry) {
  const backups = new Set();
  for (let attempt = 0; attempt < 3; attempt += 1) {
    try {
      prepareWindowsLicensesOnce(root, platform, entry, backups);
      for (const backup of backups)
        rmSync(backup, { recursive: true, force: true });
      return;
    } catch (error) {
      if (!(error instanceof WindowsLicensePublicationError)) throw error;
      if (attempt === 2) throw error.cause;
      // Windows cannot replace a populated directory in one rename. Give a
      // concurrent publisher time to finish, then revalidate source and target.
      Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 10);
    }
  }
}

function usesProductionWindowsBundle(root, environment) {
  try {
    const configuredCodexHome = environment.CODEX_HOME;
    const codexHome =
      typeof configuredCodexHome === "string" && configuredCodexHome.length > 0
        ? configuredCodexHome
        : join(homedir(), ".codex");
    if (!isAbsolute(codexHome)) return false;
    const cacheRoot = realpathSync(join(codexHome, "plugins", "cache"));
    const [publisher, plugin, version, ...extra] = relative(
      cacheRoot,
      root,
    ).split(/[\\/]/u);
    const config = JSON.parse(
      readFileSync(join(root, "scripts", "runtime-config.json"), "utf8"),
    );
    return (
      config.flavor === "production" &&
      config.serverName === "chatgpt-meetings" &&
      config.pluginName === "chatgpt-meetings" &&
      config.marketplaceName === publisher &&
      config.developmentUpdatePolicy === "disabled" &&
      ((config.distribution === "internal" &&
        publisher === "openai-internal-testing") ||
        (config.distribution === "external" &&
          publisher === "openai-curated-remote")) &&
      OFFICIAL_WINDOWS_PUBLISHERS.includes(publisher) &&
      plugin === "chatgpt-meetings" &&
      typeof version === "string" &&
      version.length > 0 &&
      extra.length === 0 &&
      Array.isArray(config.officialCachePublishers) &&
      config.officialCachePublishers.length ===
        OFFICIAL_WINDOWS_PUBLISHERS.length &&
      OFFICIAL_WINDOWS_PUBLISHERS.every((officialPublisher) =>
        config.officialCachePublishers.includes(officialPublisher),
      )
    );
  } catch {
    return false;
  }
}

export function prepareWindowsCompanion(
  pluginRoot,
  platform,
  environment = process.env,
) {
  const root = realpathSync(pluginRoot);
  const productionBundle = usesProductionWindowsBundle(root, environment);
  const runtimeDescriptorPath = join(
    root,
    ".codex-plugin",
    "windows-runtime.json",
  );
  if (!productionBundle) {
    try {
      regularFile(
        runtimeDescriptorPath,
        "installed Windows runtime descriptor",
      );
      const runtime = JSON.parse(readFileSync(runtimeDescriptorPath, "utf8"));
      if (
        runtime.schemaVersion !== 1 ||
        runtime.platform !== platform ||
        runtime.artifactName !== EXECUTABLE_NAME ||
        !SHA256.test(runtime.executableSha256 ?? "") ||
        !["unsigned-test", "authenticode"].includes(runtime.signing?.kind)
      ) {
        throw new Error(`invalid installed ${platform} runtime descriptor`);
      }
      if (
        runtime.signing.kind === "unsigned-test" &&
        environment.CHATGPT_MEETINGS_NATIVE_ALLOW_UNSIGNED !== "1"
      ) {
        throw new Error(
          "unsigned Windows companion requires the explicit test gate",
        );
      }
      const installed = join(root, EXECUTABLE_NAME);
      regularFile(installed, "installed Windows companion");
      if (sha256(installed) !== runtime.executableSha256) {
        throw new Error(
          "installed Windows companion failed digest verification",
        );
      }
      return runtime;
    } catch (error) {
      if (error?.code !== "ENOENT") throw error;
    }
  }

  const descriptorPath = join(root, "native", "windows-production-bundle.json");
  regularFile(descriptorPath, "Windows bundle descriptor");
  const descriptor = JSON.parse(readFileSync(descriptorPath, "utf8"));
  const entry = descriptor.platforms?.[platform];
  const expectedRelative = `native/${platform}/${EXECUTABLE_NAME}`;
  if (
    descriptor.schemaVersion !== 1 ||
    descriptor.kind !== "chatgpt-meetings-windows-production-bundle" ||
    descriptor.release?.tag?.toLowerCase() === "latest" ||
    entry?.artifactName !== EXECUTABLE_NAME ||
    entry.executablePath !== expectedRelative ||
    !SHA256.test(entry.executableSha256 ?? "") ||
    !Number.isSafeInteger(entry.executableSizeBytes) ||
    entry.executableSizeBytes <= 0 ||
    !["unsigned-test", "authenticode"].includes(entry.signing?.kind)
  ) {
    throw new Error(`invalid bundled ${platform} companion descriptor`);
  }
  if (
    entry.signing.kind === "unsigned-test" &&
    !productionBundle &&
    environment.CHATGPT_MEETINGS_NATIVE_ALLOW_UNSIGNED !== "1"
  ) {
    throw new Error(
      "unsigned Windows companion requires the explicit test gate",
    );
  }
  const source = join(root, ...expectedRelative.split("/"));
  const sourceMetadata = regularFile(source, `bundled ${platform} companion`);
  if (
    sourceMetadata.size !== entry.executableSizeBytes ||
    sha256(source) !== entry.executableSha256
  ) {
    throw new Error(`bundled ${platform} companion failed digest verification`);
  }
  prepareWindowsLicenses(root, platform, entry);
  const target = join(root, EXECUTABLE_NAME);
  try {
    regularFile(target, "installed Windows companion");
    if (sha256(target) !== entry.executableSha256) {
      throw new Error(
        "installed Windows companion does not match the selected architecture",
      );
    }
    return entry;
  } catch (error) {
    if (error?.code !== "ENOENT") throw error;
  }
  const temporary = join(root, `.ChatGPT Meetings.${process.pid}.tmp`);
  let ownsTemporary = false;
  try {
    try {
      copyFileSync(source, temporary, constants.COPYFILE_EXCL);
      ownsTemporary = true;
    } catch (error) {
      // COPYFILE_EXCL never grants ownership of a pre-existing temporary.
      ownsTemporary = error?.code !== "EEXIST";
      throw error;
    }
    try {
      renameSync(temporary, target);
      ownsTemporary = false;
    } catch (error) {
      try {
        regularFile(target, "installed Windows companion");
        if (sha256(target) === entry.executableSha256) return entry;
      } catch {
        // Surface the original publication error below.
      }
      throw error;
    }
    return entry;
  } finally {
    if (ownsTemporary) {
      try {
        rmSync(temporary, { force: true });
      } catch {
        try {
          console.error(
            "ChatGPT Meetings could not clean up its temporary Windows companion.",
          );
        } catch {
          // A closed stderr must never mask the original publication outcome.
        }
      }
    }
  }
}

function windowsWorkingDirectory(environment) {
  for (const value of [
    environment.CODEX_HOME,
    environment.LOCALAPPDATA,
    environment.USERPROFILE,
    environment.HOME,
    environment.TEMP,
  ]) {
    if (
      typeof value !== "string" ||
      value.length === 0 ||
      value.length > 4096 ||
      value.includes("\0") ||
      !isAbsolute(value)
    ) {
      continue;
    }
    try {
      const absolute = resolve(value);
      const canonical = realpathSync(absolute);
      const metadata = lstatSync(absolute);
      if (
        canonical.toLowerCase() !== absolute.toLowerCase() ||
        !metadata.isDirectory() ||
        metadata.isSymbolicLink() ||
        /(?:^|[\\/])plugins[\\/]cache(?:[\\/]|$)/i.test(canonical)
      ) {
        continue;
      }
      return canonical;
    } catch {
      continue;
    }
  }
  throw new Error(
    "no safe Windows working directory was found for ChatGPT Meetings",
  );
}

async function main() {
  const scriptRoot = dirname(fileURLToPath(import.meta.url));
  const pluginRoot = resolve(scriptRoot, "..");
  const runtime = join(scriptRoot, "start_meetings_mcp.mjs");
  const environment = process.env;
  const args = process.argv.slice(2);
  if (process.platform === "win32") {
    const duplicateScript =
      environment.CHATGPT_MEETINGS_MCP_DUPLICATE_SCRIPT === "1";
    delete environment.CHATGPT_MEETINGS_MCP_DUPLICATE_SCRIPT;
    if (duplicateScript) {
      const candidate = args.shift();
      try {
        if (
          typeof candidate !== "string" ||
          realpathSync(resolve(pluginRoot, candidate)).toLowerCase() !==
            realpathSync(fileURLToPath(import.meta.url)).toLowerCase()
        ) {
          throw new Error("invalid script identity");
        }
      } catch {
        throw new Error("invalid bundled MCP launcher path");
      }
    }
    process.chdir(windowsWorkingDirectory(environment));
    const platform = windowsPlatform(environment);
    prepareWindowsCompanion(pluginRoot, platform, environment);
    environment.CHATGPT_MEETINGS_NATIVE_PLATFORM = platform;
  }
  // The runtime owns stdio and shutdown; keep preparation in that same process.
  process.argv = [process.execPath, runtime, ...args];
  await import(pathToFileURL(runtime).href);
}

if (
  process.argv[1] &&
  resolve(process.argv[1]) === fileURLToPath(import.meta.url)
) {
  try {
    await main();
  } catch (error) {
    console.error(
      `ChatGPT Meetings bundled MCP launch failed: ${error.message}`,
    );
    process.exit(1);
  }
}
