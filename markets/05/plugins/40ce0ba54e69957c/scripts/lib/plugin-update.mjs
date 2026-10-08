import { execFile } from "node:child_process";
import { randomUUID } from "node:crypto";
import { readdir, rename, rm } from "node:fs/promises";
import { isAbsolute, join, resolve } from "node:path";
import { promisify } from "node:util";

import { refreshStoredConfig } from "./config.mjs";

const execFileAsync = promisify(execFile);
const marketplaceNamePattern = /^[a-z0-9][a-z0-9._-]{0,63}$/i;

function requirePluginData(pluginData) {
  if (typeof pluginData !== "string" || !isAbsolute(pluginData)) {
    throw new TypeError("pluginData must be an absolute path");
  }
  return resolve(pluginData);
}

function parseJson(stdout, label) {
  try {
    return JSON.parse(stdout);
  } catch (error) {
    throw new SyntaxError(`${label} returned invalid JSON: ${error.message}`);
  }
}

async function defaultRunCodex(args) {
  const { stdout } = await execFileAsync("codex", args, {
    encoding: "utf8",
    maxBuffer: 1024 * 1024,
    timeout: 60_000,
    windowsHide: true,
  });
  return stdout;
}

function selectInstalledTokenX(value, requestedMarketplace) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    throw new TypeError("Codex plugin list must return an object");
  }
  if (!Array.isArray(value.installed)) {
    throw new TypeError("Codex plugin list must contain installed plugins");
  }
  const candidates = value.installed.filter(
    (item) =>
      item?.name === "tokenx" &&
      item.installed === true &&
      (requestedMarketplace === null ||
        item.marketplaceName === requestedMarketplace),
  );
  if (candidates.length === 0) {
    const suffix =
      requestedMarketplace === null
        ? ""
        : ` in marketplace ${requestedMarketplace}`;
    throw new RangeError(`TokenX is not installed${suffix}`);
  }
  if (candidates.length > 1) {
    throw new RangeError(
      "multiple TokenX installations found; use update --marketplace <name>",
    );
  }
  const selected = candidates[0];
  if (
    typeof selected.marketplaceName !== "string" ||
    !marketplaceNamePattern.test(selected.marketplaceName)
  ) {
    throw new RangeError("installed TokenX marketplace name is invalid");
  }
  return selected;
}

async function removeRuntimeDirectory(dataRoot, name) {
  const path = join(dataRoot, name);
  let entries;
  try {
    entries = await readdir(path);
  } catch (error) {
    if (error?.code === "ENOENT") {
      return 0;
    }
    throw error;
  }
  const stalePath = join(dataRoot, `.${name}-${randomUUID()}.stale`);
  await rename(path, stalePath);
  await rm(stalePath, { recursive: true, force: false });
  return entries.length;
}

export async function refreshPluginData(pluginData) {
  const dataRoot = requirePluginData(pluginData);
  const configResult = await refreshStoredConfig({
    pluginData: dataRoot,
  });
  const [stateEntriesRemoved, smartRunsRemoved] = await Promise.all([
    removeRuntimeDirectory(dataRoot, "state"),
    removeRuntimeDirectory(dataRoot, "smart-classifier"),
  ]);
  return {
    ...configResult,
    stateEntriesRemoved,
    smartRunsRemoved,
  };
}

export async function updatePluginFromMarketplace({
  pluginData,
  marketplaceName = null,
  runCodex = defaultRunCodex,
}) {
  if (
    marketplaceName !== null &&
    (typeof marketplaceName !== "string" ||
      !marketplaceNamePattern.test(marketplaceName))
  ) {
    throw new RangeError("marketplace name is invalid");
  }
  if (typeof runCodex !== "function") {
    throw new TypeError("runCodex must be a function");
  }

  const listOutput = await runCodex(["plugin", "list", "--json"]);
  const installed = selectInstalledTokenX(
    parseJson(listOutput, "codex plugin list"),
    marketplaceName,
  );
  if (installed.marketplaceSource?.sourceType === "git") {
    await runCodex([
      "plugin",
      "marketplace",
      "upgrade",
      installed.marketplaceName,
      "--json",
    ]);
  }

  const selector = `tokenx@${installed.marketplaceName}`;
  const installOutput = await runCodex([
    "plugin",
    "add",
    selector,
    "--json",
  ]);
  const installResult = parseJson(installOutput, "codex plugin add");
  if (
    installResult?.pluginId !== selector ||
    installResult.name !== "tokenx" ||
    installResult.marketplaceName !== installed.marketplaceName ||
    typeof installResult.version !== "string" ||
    installResult.version.length === 0
  ) {
    throw new RangeError("Codex returned an invalid TokenX install result");
  }

  return {
    updated: true,
    marketplaceName: installed.marketplaceName,
    version: installResult.version,
    restartRequired: true,
    pluginData: await refreshPluginData(pluginData),
  };
}
