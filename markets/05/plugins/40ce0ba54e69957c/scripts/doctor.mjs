import { execFile } from "node:child_process";
import { randomUUID } from "node:crypto";
import {
  chmod,
  mkdir,
  readdir,
  readFile,
  unlink,
  writeFile,
} from "node:fs/promises";
import { homedir } from "node:os";
import { join } from "node:path";
import { promisify } from "node:util";

import { loadConfig } from "./lib/config.mjs";
import {
  readCodexModelCatalog,
  validateConfiguredModels,
} from "./lib/model-catalog.mjs";
import { SMART_CLASSIFIER_CONTRACT_VERSION } from "./lib/smart-classifier.mjs";

const execFileAsync = promisify(execFile);
const hookEvents = [
  "PreToolUse",
  "SessionEnd",
  "SessionStart",
  "UserPromptSubmit",
];

async function defaultRunVersion(command, args) {
  const { stdout } = await execFileAsync(command, args, {
    encoding: "utf8",
    timeout: 5_000,
    windowsHide: true,
  });
  return stdout.trim();
}

async function check(action) {
  try {
    return {
      ok: true,
      detail: await action(),
    };
  } catch (error) {
    return {
      ok: false,
      detail:
        error instanceof Error && error.message
          ? error.message
          : "unknown diagnostic error",
    };
  }
}

async function inspectHookContract(pluginRoot) {
  const hooks = JSON.parse(
    await readFile(join(pluginRoot, "hooks", "hooks.json"), "utf8"),
  );
  const actual = Object.keys(hooks.hooks ?? {}).sort();
  if (JSON.stringify(actual) !== JSON.stringify(hookEvents)) {
    throw new RangeError("hook contract does not contain the four expected events");
  }
  for (const groups of Object.values(hooks.hooks)) {
    for (const group of groups) {
      for (const hook of group.hooks) {
        const match = hook.command.match(
          /\$\{PLUGIN_ROOT\}\/scripts\/([^"]+\.mjs)/,
        );
        if (!match) {
          throw new RangeError("hook command does not resolve through PLUGIN_ROOT");
        }
        await readFile(join(pluginRoot, "scripts", match[1]), "utf8");
      }
    }
  }
  const sessionEnd = hooks.hooks.SessionEnd ?? [];
  const sessionEndMatchers = sessionEnd
    .map((group) => group.matcher)
    .filter((matcher) => typeof matcher === "string");
  if (
    sessionEndMatchers.length !== 1 ||
    sessionEndMatchers[0] !== "other"
  ) {
    throw new RangeError(
      "SessionEnd must remain matched to the probed host reason 'other'",
    );
  }
  return "four registered hook events and scripts; SessionEnd reason=other only";
}

async function inspectSessionState(pluginData) {
  const stateDir = join(pluginData, "state");
  let entries = [];
  try {
    entries = await readdir(stateDir);
  } catch (error) {
    if (error?.code === "ENOENT") {
      return (
        "no session state directory; no decisions, outcomes, or model pins " +
        "are stored"
      );
    }
    throw error;
  }
  const pinFiles = entries.filter((name) =>
    name.endsWith(".pin.json")
  ).length;
  const outcomeFiles = entries.filter((name) =>
    name.endsWith(".outcomes.json")
  ).length;
  const decisionFiles = entries.filter(
    (name) =>
      name.endsWith(".json") &&
      !name.endsWith(".pin.json") &&
      !name.endsWith(".outcomes.json"),
  ).length;
  const lockArtifacts = entries.filter(
    (name) => name.endsWith(".lock") || name.endsWith(".recovery"),
  ).length;
  return (
    `${decisionFiles} decision file(s), ${outcomeFiles} outcome file(s), ` +
    `${pinFiles} model pin file(s), ${lockArtifacts} lock/recovery ` +
    "artifact(s); SessionEnd clears decision/outcome state for reason=other; " +
    "model pins persist until explicit clear, exact-session cleanup, or update"
  );
}

async function inspectPluginData(pluginData) {
  await mkdir(pluginData, { recursive: true, mode: 0o700 });
  await chmod(pluginData, 0o700);
  const probePath = join(pluginData, `.doctor-${randomUUID()}.tmp`);
  await writeFile(probePath, "tokenx\n", {
    flag: "wx",
    mode: 0o600,
  });
  await unlink(probePath);
  return "writable with restrictive modes";
}

export async function runDoctor({
  pluginRoot,
  pluginData,
  homeDir = homedir(),
  runVersion = defaultRunVersion,
  nodeVersion = process.version,
  env = process.env,
}) {
  const checks = {
    node: {
      ok: /^v(?:2[0-9]|[3-9][0-9])\./.test(nodeVersion),
      detail: nodeVersion,
    },
  };
  const [git, codex, hookContract, pluginDataCheck, sessionState] =
    await Promise.all([
      check(() => runVersion("git", ["--version"])),
      check(() => runVersion("codex", ["--version"])),
      check(() => inspectHookContract(pluginRoot)),
      check(() => inspectPluginData(pluginData)),
      check(() => inspectSessionState(pluginData)),
    ]);
  checks.git = git;
  checks.codex = codex;
  checks.hookContract = hookContract;
  checks.pluginData = pluginDataCheck;
  checks.sessionState = sessionState;

  let config;
  checks.config = await check(async () => {
    config = await loadConfig({ pluginData, env });
    return "schema 3 Codex-only configuration";
  });
  checks.dynamicAgents = await check(async () => {
    if (!config) {
      throw new Error("configuration must be valid before dynamic-agent checks");
    }
    const dynamic = config.routing.dynamicAgents;
    const profiles = Object.entries(dynamic.profiles)
      .map(([role, route]) => `${role}=${route}`)
      .join(", ");
    return `enabled=${dynamic.enabled}; maxAssignments=${dynamic.maxAssignmentsPerDecision}; ${profiles}`;
  });
  checks.modelCatalog = await check(async () => {
    if (!config) {
      throw new Error("configuration must be valid before model catalog checks");
    }
    const catalog = await readCodexModelCatalog({ homeDir });
    // The hooks fall back to the bundled catalog when this file is absent so
    // routing keeps working. Diagnostics must still report it: the whole point
    // of doctor is to surface what degraded.
    if (catalog === null) {
      throw new Error(
        "Codex model catalog is unavailable at ~/.codex/models_cache.json; " +
          "routing falls back to the bundled catalog and cannot confirm live " +
          "model availability",
      );
    }
    validateConfiguredModels(config, catalog);
    return "all configured models and efforts are list-visible";
  });
  checks.nestingPolicy = {
    ok: true,
    detail:
      "assignment dispatch is guard-injected; live PreToolUse depth is not " +
      "exposed, so nesting is budget-capped rather than hard root-only denied",
  };

  return {
    ok: Object.values(checks).every((item) => item.ok),
    smartClassifierContract: SMART_CLASSIFIER_CONTRACT_VERSION,
    checks,
  };
}
