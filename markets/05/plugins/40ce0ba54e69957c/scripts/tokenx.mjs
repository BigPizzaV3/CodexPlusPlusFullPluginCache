import { readFile, stat } from "node:fs/promises";
import { fileURLToPath } from "node:url";

import { classifyPrompt } from "./lib/classify.mjs";
import { buildAssignmentPrompt } from "./lib/assignment-prompts.mjs";
import { loadConfig } from "./lib/config.mjs";
import { resolveAssignmentProfile } from "./lib/delegation-plan.mjs";
import {
  resetConfiguration,
  setConfiguration,
  showConfiguration,
} from "./configure.mjs";
import { runDoctor } from "./doctor.mjs";
import {
  updatePluginFromMarketplace,
} from "./lib/plugin-update.mjs";
import { requirePluginData } from "./lib/plugin-data.mjs";
import { removeSessionState } from "./lib/state.mjs";

const pluginRoot = fileURLToPath(new URL("../", import.meta.url));

function printJson(value) {
  process.stdout.write(`${JSON.stringify(value, null, 2)}\n`);
}

function requireArgs(actual, expected, usage) {
  if (
    actual.length !== expected.length ||
    actual.some((value, index) => value !== expected[index])
  ) {
    throw new RangeError(`invalid arguments; usage: ${usage}`);
  }
}

async function readMode600TextFile(path, label) {
  const metadata = await stat(path);
  if (!metadata.isFile()) {
    throw new TypeError(`${label} must be a regular file`);
  }
  if (process.platform !== "win32" && (metadata.mode & 0o777) !== 0o600) {
    throw new RangeError(`${label} mode must be 0600`);
  }
  if (metadata.size > 1024 * 1024) {
    throw new RangeError(`${label} must not exceed 1 MiB`);
  }
  return readFile(path, "utf8");
}

async function explain(args, pluginData) {
  if (args.length !== 2 || args[0] !== "--prompt-file") {
    throw new RangeError(
      "invalid arguments; usage: explain --prompt-file <path>",
    );
  }
  const promptPath = args[1];
  const prompt = await readMode600TextFile(promptPath, "prompt file");
  const config = await loadConfig({ pluginData, env: process.env });
  const decision = classifyPrompt(prompt, config, {
    sessionId: "tokenx-explain",
    turnId: null,
    nowMs: Date.now(),
  });
  printJson({
    route: decision.route,
    model: decision.model,
    reasoningEffort: decision.reasoningEffort,
    method: decision.method,
    reasonCodes: decision.reasonCodes,
    explicit: decision.explicit,
  });
}

function parseAssignmentArgs(args) {
  const options = {
    role: null,
    parentRoute: null,
    taskFile: null,
    files: null,
    contextFile: null,
    evidence: null,
    verify: [],
    json: false,
  };
  const valueOptions = Object.freeze({
    "--role": "role",
    "--parent-route": "parentRoute",
    "--task-file": "taskFile",
    "--files": "files",
    "--context-file": "contextFile",
    "--evidence": "evidence",
  });

  for (let index = 0; index < args.length; index += 1) {
    const argument = args[index];
    if (argument === "--json") {
      if (options.json) {
        throw new RangeError("--json may be specified only once");
      }
      options.json = true;
      continue;
    }
    if (argument === "--verify") {
      const command = args[index + 1];
      if (command === undefined) {
        throw new RangeError("--verify requires a command");
      }
      options.verify.push(command);
      if (options.verify.length > 8) {
        throw new RangeError("verify must contain at most 8 commands");
      }
      index += 1;
      continue;
    }
    const key = valueOptions[argument];
    if (key === undefined) {
      throw new RangeError(`unknown assignment argument: ${String(argument)}`);
    }
    if (options[key] !== null) {
      throw new RangeError(`${argument} may be specified only once`);
    }
    const value = args[index + 1];
    if (value === undefined) {
      throw new RangeError(`${argument} requires a value`);
    }
    options[key] = value;
    index += 1;
  }

  if (
    options.role === null ||
    options.parentRoute === null ||
    options.taskFile === null
  ) {
    throw new RangeError(
      "invalid arguments; usage: assignment --role <role> " +
        "--parent-route <route> --task-file <0600 path> " +
        "[--files a,b] [--verify <cmd>]... " +
        "[--context-file <0600 path>] [--evidence <line>] [--json]",
    );
  }
  return options;
}

async function assignmentCommand(args, pluginData) {
  if (args.length === 1 && args[0] === "--help") {
    process.stdout.write(
      "usage: tokenx assignment --role <role> --parent-route <route> --task-file <0600 path> [--files a,b] [--verify <cmd>]... [--context-file <0600 path>] [--evidence <line>] [--json]\n\n" +
      "This stateless renderer does not authorize dispatch. Only the current persisted TokenX-advertised task_name authorizes a child; do not supply assignment_id.\n",
    );
    return;
  }
  const options = parseAssignmentArgs(args);
  const task = await readMode600TextFile(options.taskFile, "task file");
  const context = options.contextFile === null
    ? undefined
    : await readMode600TextFile(options.contextFile, "context file");
  const config = await loadConfig({ pluginData, env: process.env });
  const resolved = resolveAssignmentProfile(
    options.parentRoute,
    options.role,
    config,
  );
  const input = {
    role: options.role,
    task,
  };
  if (options.files !== null) {
    input.files = options.files.split(",");
  }
  if (options.verify.length > 0) {
    input.verify = options.verify;
  }
  if (context !== undefined) {
    input.context = context;
  }
  if (options.evidence !== null) {
    input.evidence = options.evidence;
  }
  const prompt = buildAssignmentPrompt(input);

  if (options.json) {
    printJson({
      prompt,
      role: options.role,
      parentRoute: options.parentRoute,
      profileKey: resolved.profileKey,
      reasoningEffort: resolved.reasoningEffort,
    });
    return;
  }
  process.stdout.write(prompt);
  process.stderr.write(
    `role=${options.role} profile=${resolved.profileKey} ` +
      `model=${config.routes[resolved.profileKey].model} ` +
      `effort=${resolved.reasoningEffort}\n`,
  );
}

async function configCommand(args, pluginData) {
  const [action, ...rest] = args;
  if (action === "show") {
    requireArgs(rest, [], "config show");
    printJson(
      await showConfiguration({
        pluginData,
        env: process.env,
      }),
    );
    return;
  }
  if (action === "set") {
    if (rest.length !== 2) {
      throw new RangeError(
        "invalid arguments; usage: config set <path> <value>",
      );
    }
    printJson(
      await setConfiguration({
        pluginData,
        path: rest[0],
        rawValue: rest[1],
        env: process.env,
      }),
    );
    return;
  }
  if (action === "reset") {
    requireArgs(rest, [], "config reset");
    printJson(await resetConfiguration({ pluginData }));
    return;
  }
  throw new RangeError(`unknown config command: ${String(action)}`);
}

async function updateCommand(args, pluginData) {
  if (args.length === 0) {
    printJson(await updatePluginFromMarketplace({ pluginData }));
    return;
  }
  if (
    args.length === 2 &&
    args[0] === "--marketplace" &&
    args[1].length > 0
  ) {
    printJson(
      await updatePluginFromMarketplace({
        pluginData,
        marketplaceName: args[1],
      }),
    );
    return;
  }
  throw new RangeError(
    "invalid arguments; usage: update [--marketplace <name>]",
  );
}

async function main(args) {
  const pluginData = requirePluginData(process.env);
  const [command, ...rest] = args;
  if (command === "explain") {
    await explain(rest, pluginData);
  } else if (command === "assignment") {
    await assignmentCommand(rest, pluginData);
  } else if (command === "config") {
    await configCommand(rest, pluginData);
  } else if (command === "doctor") {
    requireArgs(rest, ["--json"], "doctor --json");
    const report = await runDoctor({
      pluginRoot,
      pluginData,
    });
    printJson(report);
    if (!report.ok) {
      process.exitCode = 1;
    }
  } else if (command === "update") {
    await updateCommand(rest, pluginData);
  } else if (command === "cleanup") {
    if (rest.length !== 2 || rest[0] !== "--session") {
      throw new RangeError(
        "invalid arguments; usage: cleanup --session <opaque-id>",
      );
    }
    const sessionId = rest[1];
    if (sessionId.length === 0 || sessionId.length > 512) {
      throw new RangeError("session identifier length is invalid");
    }
    printJson({
      removed: await removeSessionState({
        pluginData,
        sessionId,
        includeOutcomes: true,
        includeModelPin: true,
      }),
      sessionId,
    });
  } else {
    throw new RangeError(`unknown command: ${String(command)}`);
  }
}

try {
  await main(process.argv.slice(2));
} catch (error) {
  const detail =
    error instanceof Error && error.message
      ? error.message.replaceAll(/\s+/g, " ").trim()
      : "unknown error";
  process.stderr.write(`TokenX CLI failed: ${detail.slice(0, 450)}\n`);
  process.exitCode = 1;
}
