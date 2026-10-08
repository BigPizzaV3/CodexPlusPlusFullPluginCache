import {
  DEFAULT_CONFIG,
  loadConfig,
  writeConfig,
} from "./lib/config.mjs";

const configurablePaths = new Set([
  "routes.economy.model",
  "routes.economy.reasoningEffort",
  "routes.standard.model",
  "routes.standard.reasoningEffort",
  "routes.deep.model",
  "routes.deep.reasoningEffort",
  "routing.structuralScoreEconomyMax",
  "routing.structuralScoreStandardMax",
  "routing.escalationReasoningEffort",
  "routing.decisionMaxAgeMs",
  "routing.maxAutomaticAgents",
  "routing.dynamicAgents.enabled",
  "routing.dynamicAgents.maxAssignmentsPerDecision",
  "routing.dynamicAgents.profiles.repoReader",
  "routing.dynamicAgents.profiles.repoReviewer",
  "routing.dynamicAgents.profiles.testRunner",
  "routing.dynamicAgents.profiles.fileEditor",
  "routing.dynamicAgents.profiles.implementer",
  "routing.smartClassifier.enabled",
  "routing.smartClassifier.model",
  "routing.smartClassifier.reasoningEffort",
  "routing.smartClassifier.timeoutMs",
]);

function getPath(value, path) {
  return path.split(".").reduce((current, key) => current[key], value);
}

function setPath(value, path, next) {
  const keys = path.split(".");
  let current = value;
  for (const key of keys.slice(0, -1)) {
    current = current[key];
  }
  current[keys.at(-1)] = next;
}

function parseValue(rawValue, currentValue) {
  if (typeof currentValue === "string") {
    return rawValue;
  }
  if (typeof currentValue === "number") {
    if (!/^-?\d+$/.test(rawValue)) {
      throw new TypeError("configuration value must be an integer");
    }
    return Number(rawValue);
  }
  if (typeof currentValue === "boolean") {
    if (rawValue !== "true" && rawValue !== "false") {
      throw new TypeError("configuration value must be true or false");
    }
    return rawValue === "true";
  }
  throw new TypeError("configuration value type is unsupported");
}

export async function showConfiguration({ pluginData, env = process.env }) {
  return loadConfig({ pluginData, env });
}

export async function setConfiguration({
  pluginData,
  path,
  rawValue,
  env = process.env,
}) {
  if (!configurablePaths.has(path)) {
    throw new RangeError(`configuration path is not documented: ${path}`);
  }
  const config = await loadConfig({ pluginData, env });
  const next = structuredClone(config);
  setPath(next, path, parseValue(rawValue, getPath(config, path)));
  return writeConfig({ pluginData, value: next });
}

export async function resetConfiguration({ pluginData }) {
  return writeConfig({
    pluginData,
    value: structuredClone(DEFAULT_CONFIG),
  });
}
