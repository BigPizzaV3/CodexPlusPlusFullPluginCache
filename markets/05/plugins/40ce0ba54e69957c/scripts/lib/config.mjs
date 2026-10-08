import { randomUUID } from "node:crypto";
import {
  chmod,
  mkdir,
  readFile,
  rename,
  writeFile,
} from "node:fs/promises";
import { isAbsolute, join, resolve } from "node:path";

import {
  SUPPORTED_REASONING_EFFORTS,
  validateModelProfile,
} from "./model-catalog.mjs";

const defaultsUrl = new URL("../../config/defaults.json", import.meta.url);
const rootKeys = ["provider", "routes", "routing", "schemaVersion", "telemetry"];
const routeNames = ["deep", "economy", "standard"];
const routingKeys = [
  "decisionMaxAgeMs",
  "denyNestedAutomaticDelegation",
  "escalationReasoningEffort",
  "maxAutomaticAgents",
  "structuralScoreEconomyMax",
  "structuralScoreStandardMax",
  "dynamicAgents",
  "smartClassifier",
  "taskProfiles",
];
const taskProfileKeys = [
  "analysis",
  "architecture",
  "complex_implementation",
  "file_edit",
  "implementation",
  "read",
  "retry",
];
const dynamicAgentKeys = [
  "enabled",
  "maxAssignmentsPerDecision",
  "profiles",
];
const dynamicAgentProfileKeys = [
  "fileEditor",
  "implementer",
  "repoReader",
  "repoReviewer",
  "testRunner",
];
const dynamicAgentProfileMaximums = Object.freeze({
  fileEditor: "economy",
  implementer: "standard",
  repoReader: "economy",
  repoReviewer: "standard",
  testRunner: "economy",
});
const routeRanks = Object.freeze({ economy: 0, standard: 1, deep: 2 });
const smartClassifierKeys = [
  "enabled",
  "model",
  "reasoningEffort",
  "timeoutMs",
];
const policyEnvironmentPattern =
  /^TOKENX_(?:PROVIDER|.*(?:MODEL|EFFORT|REASONING))$/i;

function isPlainObject(value) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    return false;
  }
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

function requireObject(value, label) {
  if (!isPlainObject(value)) {
    throw new TypeError(`${label} must be an object`);
  }
}

function requireExactKeys(value, expected, label) {
  requireObject(value, label);
  const actual = Object.keys(value).sort();
  const wanted = [...expected].sort();
  const unknown = actual.filter((key) => !wanted.includes(key));
  if (unknown.length > 0) {
    throw new RangeError(`${label} has unknown key: ${unknown[0]}`);
  }
  const missing = wanted.filter((key) => !actual.includes(key));
  if (missing.length > 0) {
    throw new RangeError(`${label} is missing key: ${missing[0]}`);
  }
}

function requirePositiveInteger(value, label) {
  if (!Number.isInteger(value) || value <= 0) {
    throw new RangeError(`${label} must be a positive integer`);
  }
}

function clone(value) {
  return structuredClone(value);
}

const parsedDefaults = JSON.parse(await readFile(defaultsUrl, "utf8"));

function validateConfigVersion(value) {
  requireExactKeys(value, rootKeys, "configuration");

  if (value.schemaVersion !== 3) {
    throw new RangeError("configuration schemaVersion must be 3");
  }
  if (value.provider !== "codex") {
    throw new RangeError("configuration provider must be codex");
  }

  requireExactKeys(value.routes, routeNames, "configuration.routes");
  for (const routeName of routeNames) {
    requireExactKeys(
      value.routes[routeName],
      ["model", "reasoningEffort"],
      `configuration.routes.${routeName}`,
    );
    validateModelProfile(value.routes[routeName]);
  }

  requireExactKeys(
    value.routing,
    routingKeys,
    "configuration.routing",
  );
  const economyMax = value.routing.structuralScoreEconomyMax;
  const standardMax = value.routing.structuralScoreStandardMax;
  // Keep in sync with STRUCTURAL_SCORE_BASE in classify.mjs (minimum attainable
  // structural score with no bonuses). Below this, structural economy is dead.
  const minAttainableStructuralScore = 20;
  if (
    !Number.isInteger(economyMax) ||
    economyMax < minAttainableStructuralScore ||
    !Number.isInteger(standardMax) ||
    standardMax <= economyMax
  ) {
    throw new RangeError(
      "routing thresholds must be ordered integers with " +
        `structuralScoreEconomyMax >= ${minAttainableStructuralScore}`,
    );
  }
  requirePositiveInteger(
    value.routing.decisionMaxAgeMs,
    "routing.decisionMaxAgeMs",
  );
  if (
    !Number.isInteger(value.routing.maxAutomaticAgents) ||
    value.routing.maxAutomaticAgents < 1 ||
    value.routing.maxAutomaticAgents > 4
  ) {
    throw new RangeError(
      "routing.maxAutomaticAgents must be an integer from 1 to 4",
    );
  }
  if (
    !SUPPORTED_REASONING_EFFORTS.includes(
      value.routing.escalationReasoningEffort,
    )
  ) {
    throw new RangeError(
      "routing.escalationReasoningEffort is unsupported",
    );
  }
  if (value.routing.denyNestedAutomaticDelegation !== true) {
    throw new RangeError(
      "routing.denyNestedAutomaticDelegation must remain true",
    );
  }
  requireExactKeys(
    value.routing.dynamicAgents,
    dynamicAgentKeys,
    "configuration.routing.dynamicAgents",
  );
  if (typeof value.routing.dynamicAgents.enabled !== "boolean") {
    throw new TypeError(
      "routing.dynamicAgents.enabled must be a boolean",
    );
  }
  requireExactKeys(
    value.routing.taskProfiles,
    taskProfileKeys,
    "configuration.routing.taskProfiles",
  );
  for (const taskProfile of taskProfileKeys) {
    const profile = value.routing.taskProfiles[taskProfile];
    requireExactKeys(
      profile,
      ["reasoningEffort", "route"],
      `configuration.routing.taskProfiles.${taskProfile}`,
    );
    if (!(profile.route in routeRanks)) {
      throw new RangeError(
        `routing.taskProfiles.${taskProfile}.route must name a route`,
      );
    }
    validateModelProfile({
      model: value.routes[profile.route].model,
      reasoningEffort: profile.reasoningEffort,
    });
  }
  if (
    !Number.isInteger(value.routing.dynamicAgents.maxAssignmentsPerDecision) ||
    value.routing.dynamicAgents.maxAssignmentsPerDecision < 1 ||
    value.routing.dynamicAgents.maxAssignmentsPerDecision > 4
  ) {
    throw new RangeError(
      "routing.dynamicAgents.maxAssignmentsPerDecision must be an integer from 1 to 4",
    );
  }
  requireExactKeys(
    value.routing.dynamicAgents.profiles,
    dynamicAgentProfileKeys,
    "configuration.routing.dynamicAgents.profiles",
  );
  for (const profileKey of dynamicAgentProfileKeys) {
    const route = value.routing.dynamicAgents.profiles[profileKey];
    if (!(route in routeRanks)) {
      throw new RangeError(
        `routing.dynamicAgents.profiles.${profileKey} must name a route`,
      );
    }
    if (routeRanks[route] > routeRanks[dynamicAgentProfileMaximums[profileKey]]) {
      throw new RangeError(
        `routing.dynamicAgents.profiles.${profileKey} exceeds its role maximum`,
      );
    }
  }
  requireExactKeys(
    value.routing.smartClassifier,
    smartClassifierKeys,
    "configuration.routing.smartClassifier",
  );
  if (typeof value.routing.smartClassifier.enabled !== "boolean") {
    throw new TypeError(
      "routing.smartClassifier.enabled must be a boolean",
    );
  }
  validateModelProfile(value.routing.smartClassifier);
  if (
    !Number.isInteger(value.routing.smartClassifier.timeoutMs) ||
    value.routing.smartClassifier.timeoutMs < 1_000 ||
    value.routing.smartClassifier.timeoutMs > 25_000
  ) {
    throw new RangeError(
      "routing.smartClassifier.timeoutMs must be an integer from 1000 to 25000",
    );
  }

  requireExactKeys(value.telemetry, ["enabled"], "configuration.telemetry");
  if (value.telemetry.enabled !== false) {
    throw new RangeError("configuration telemetry.enabled must remain false");
  }

  return clone(value);
}

export function validateConfig(value) {
  return validateConfigVersion(value);
}

export const DEFAULT_CONFIG = Object.freeze(validateConfig(parsedDefaults));

export class StoredConfigError extends Error {
  constructor(message, options = {}) {
    super(message, options);
    this.name = "StoredConfigError";
  }
}

export function isStoredConfigError(error) {
  return error instanceof StoredConfigError;
}

function assertPluginData(pluginData) {
  if (typeof pluginData !== "string" || !isAbsolute(pluginData)) {
    throw new TypeError("pluginData must be an absolute path");
  }
  return resolve(pluginData);
}

function rejectPolicyEnvironmentOverrides(env) {
  for (const key of Object.keys(env)) {
    if (policyEnvironmentPattern.test(key)) {
      throw new RangeError(
        `environment policy override is not supported: ${key}`,
      );
    }
  }
}

function parseStoredConfig(source) {
  let value;
  try {
    value = JSON.parse(source);
  } catch (error) {
    throw new StoredConfigError(
      `invalid TokenX config JSON: ${error.message}`,
      { cause: error },
    );
  }
  try {
    return {
      config: validateConfig(value),
    };
  } catch (error) {
    const detail =
      error instanceof Error && error.message
        ? error.message
        : "stored configuration is invalid";
    throw new StoredConfigError(`invalid TokenX config: ${detail}`, {
      cause: error,
    });
  }
}

export async function loadConfig({ pluginData, env = process.env }) {
  const dataRoot = assertPluginData(pluginData);
  rejectPolicyEnvironmentOverrides(env);
  const configPath = join(dataRoot, "config.json");

  let source;
  try {
    source = await readFile(configPath, "utf8");
  } catch (error) {
    if (error?.code === "ENOENT") {
      return clone(DEFAULT_CONFIG);
    }
    throw error;
  }

  return parseStoredConfig(source).config;
}

export async function writeConfig({ pluginData, value }) {
  const dataRoot = assertPluginData(pluginData);
  const config = validateConfig(value);
  await mkdir(dataRoot, { recursive: true, mode: 0o700 });
  await chmod(dataRoot, 0o700);

  const configPath = join(dataRoot, "config.json");
  const temporaryPath = join(dataRoot, `.config-${randomUUID()}.tmp`);
  const serialized = `${JSON.stringify(config, null, 2)}\n`;
  await writeFile(temporaryPath, serialized, {
    encoding: "utf8",
    flag: "wx",
    mode: 0o600,
  });
  await rename(temporaryPath, configPath);
  await chmod(configPath, 0o600);
  return config;
}

export async function refreshStoredConfig({ pluginData }) {
  const dataRoot = assertPluginData(pluginData);
  const configPath = join(dataRoot, "config.json");
  let source;
  try {
    source = await readFile(configPath, "utf8");
  } catch (error) {
    if (error?.code === "ENOENT") {
      return {
        config: "default",
        configBackup: null,
      };
    }
    throw error;
  }

  try {
    const parsed = parseStoredConfig(source);
    await writeConfig({
      pluginData: dataRoot,
      value: parsed.config,
    });
    return {
      config: "preserved",
      configBackup: null,
    };
  } catch (error) {
    if (!isStoredConfigError(error)) {
      throw error;
    }
  }

  const configBackup = `config.invalid-${randomUUID()}.json`;
  const backupPath = join(dataRoot, configBackup);
  await rename(configPath, backupPath);
  try {
    await writeConfig({
      pluginData: dataRoot,
      value: DEFAULT_CONFIG,
    });
  } catch (error) {
    try {
      await rename(backupPath, configPath);
    } catch (restoreError) {
      error.restoreError = restoreError;
    }
    throw error;
  }
  return {
    config: "reset",
    configBackup,
  };
}
