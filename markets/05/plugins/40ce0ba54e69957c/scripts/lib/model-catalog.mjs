import { readFile } from "node:fs/promises";
import { homedir } from "node:os";
import { join } from "node:path";

export const SUPPORTED_REASONING_EFFORTS = Object.freeze([
  "low",
  "medium",
  "high",
  "xhigh",
  "max",
  "ultra",
]);

export const BUNDLED_MODEL_CATALOG = Object.freeze({
  "gpt-5.6-luna": SUPPORTED_REASONING_EFFORTS,
  "gpt-5.6-terra": SUPPORTED_REASONING_EFFORTS,
  "gpt-5.6-sol": SUPPORTED_REASONING_EFFORTS,
});

export function validateModelProfile(
  profile,
  catalog = BUNDLED_MODEL_CATALOG,
) {
  if (profile === null || typeof profile !== "object" || Array.isArray(profile)) {
    throw new TypeError("model profile must be an object");
  }

  const efforts = catalog[profile.model];
  if (!efforts) {
    throw new RangeError(`unsupported Codex model: ${String(profile.model)}`);
  }
  if (!efforts.includes(profile.reasoningEffort)) {
    throw new RangeError(
      `unsupported reasoningEffort for ${profile.model}: ${String(profile.reasoningEffort)}`,
    );
  }

  return {
    model: profile.model,
    reasoningEffort: profile.reasoningEffort,
  };
}

export async function readCodexModelCatalog({ homeDir = homedir() } = {}) {
  if (typeof homeDir !== "string" || homeDir.length === 0) {
    throw new TypeError("homeDir must be a non-empty string");
  }
  const path = join(homeDir, ".codex", "models_cache.json");
  let value;
  try {
    value = JSON.parse(await readFile(path, "utf8"));
  } catch (error) {
    // An absent cache means live availability cannot be verified. That is not
    // the same as a model being unavailable, so callers are told "unknown"
    // rather than "empty"; reporting empty would fail every configured profile
    // and disable routing outright.
    if (error?.code === "ENOENT") {
      return null;
    }
    if (error instanceof SyntaxError) {
      throw new SyntaxError(`invalid Codex model catalog JSON: ${error.message}`);
    }
    throw error;
  }
  if (!Array.isArray(value.models)) {
    throw new TypeError("Codex model catalog must contain a models array");
  }

  const catalog = {};
  for (const model of value.models) {
    if (
      model?.visibility !== "list" ||
      typeof model.slug !== "string" ||
      !Array.isArray(model.supported_reasoning_levels)
    ) {
      continue;
    }
    catalog[model.slug] = model.supported_reasoning_levels
      .map((level) => level?.effort)
      .filter((effort) => typeof effort === "string");
  }
  return catalog;
}

export function validateConfiguredModels(config, catalog) {
  const profiles = [
    ...Object.entries(config.routes).map(([route, profile]) => ({
      label: route,
      ...profile,
    })),
    {
      label: "deep escalation",
      model: config.routes.deep.model,
      reasoningEffort: config.routing.escalationReasoningEffort,
    },
    ...Object.entries(config.routing.taskProfiles).map(([taskProfile, profile]) => ({
      label: `task profile ${taskProfile}`,
      model: config.routes[profile.route].model,
      reasoningEffort: profile.reasoningEffort,
    })),
  ];
  if (config.routing.smartClassifier.enabled) {
    profiles.push({
      label: "smart classifier",
      model: config.routing.smartClassifier.model,
      reasoningEffort: config.routing.smartClassifier.reasoningEffort,
    });
  }
  if (config.routing.dynamicAgents?.enabled) {
    for (const [role, route] of Object.entries(
      config.routing.dynamicAgents.profiles,
    )) {
      profiles.push({
        label: `dynamic ${role}`,
        ...config.routes[route],
      });
    }
  }
  const unavailable = [];
  for (const profile of profiles) {
    const efforts = catalog[profile.model];
    if (!efforts) {
      unavailable.push(`${profile.label}: model ${profile.model}`);
    } else if (!efforts.includes(profile.reasoningEffort)) {
      unavailable.push(
        `${profile.label}: ${profile.model} ${profile.reasoningEffort}`,
      );
    }
  }
  if (unavailable.length > 0) {
    throw new RangeError(
      `configured Codex profiles unavailable: ${unavailable.join("; ")}`,
    );
  }
  return true;
}

export async function validateLiveConfiguredModels(
  config,
  { homeDir = homedir() } = {},
) {
  const catalog = await readCodexModelCatalog({ homeDir });
  // With no readable cache there is nothing to verify against, so fall back to
  // the bundled catalog. This is not a model substitution -- the configured
  // profiles are still required to be ones TokenX ships support for -- it only
  // skips a liveness check that cannot be performed. Verifying against an
  // absent cache would fail every hook and disable routing entirely.
  const effective = catalog ?? BUNDLED_MODEL_CATALOG;
  validateConfiguredModels(config, effective);
  return effective;
}
