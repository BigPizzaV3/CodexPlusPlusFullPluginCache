import { execFile } from "node:child_process";
import { readFile, stat } from "node:fs/promises";
import { extname, join } from "node:path";
import { performance } from "node:perf_hooks";

import { promptStats } from "./classify.mjs";

export const LANG_BUCKETS = Object.freeze([
  "js",
  "ts",
  "python",
  "go",
  "rust",
  "java",
  "c-cpp",
  "shell",
  "docs",
  "other",
]);

const manifestByteLimit = 64 * 1024;
const gitOutputLimit = 1 << 20;
const unknownRepo = Object.freeze({
  repoSizeBucket: "unknown",
  testCommandKnown: false,
  langBuckets: Object.freeze([]),
});
const zeroOutcomes = Object.freeze({
  retryEscalations: 0,
  assignmentDenials: 0,
  smartFallbacks: 0,
  lastRoute: null,
});
const extensionBuckets = Object.freeze({
  ".js": "js",
  ".mjs": "js",
  ".cjs": "js",
  ".jsx": "js",
  ".ts": "ts",
  ".tsx": "ts",
  ".mts": "ts",
  ".cts": "ts",
  ".py": "python",
  ".go": "go",
  ".rs": "rust",
  ".java": "java",
  ".c": "c-cpp",
  ".cc": "c-cpp",
  ".cpp": "c-cpp",
  ".h": "c-cpp",
  ".hpp": "c-cpp",
  ".sh": "shell",
  ".bash": "shell",
  ".zsh": "shell",
  ".md": "docs",
  ".rst": "docs",
  ".txt": "docs",
});

function remainingBudget(deadline, nowImpl) {
  const remaining = deadline - nowImpl();
  if (!Number.isFinite(remaining) || remaining <= 0) {
    throw new Error("signals digest deadline exhausted");
  }
  return remaining;
}

function deadlineTimeout(deadline, nowImpl) {
  return Math.max(1, Math.ceil(remainingBudget(deadline, nowImpl)));
}

async function completeBeforeDeadline({
  operation,
  deadline,
  nowImpl,
  timeoutMessage,
  onTimeout = null,
}) {
  const timeout = deadlineTimeout(deadline, nowImpl);
  let timer;
  try {
    const result = await Promise.race([
      Promise.resolve().then(operation),
      new Promise((_, reject) => {
        timer = setTimeout(() => {
          onTimeout?.();
          reject(new Error(timeoutMessage));
        }, timeout);
      }),
    ]);
    remainingBudget(deadline, nowImpl);
    return result;
  } finally {
    clearTimeout(timer);
  }
}

function runGitProbe({ cwd, deadline, execFileImpl, nowImpl }) {
  const timeout = deadlineTimeout(deadline, nowImpl);
  return new Promise((resolve, reject) => {
    let settled = false;
    const finish = (error, stdout) => {
      if (settled) {
        return;
      }
      settled = true;
      clearTimeout(timer);
      if (error) {
        reject(error);
      } else {
        resolve(stdout);
      }
    };
    const timer = setTimeout(
      () => finish(new Error("signals digest git probe timed out")),
      timeout,
    );
    try {
      execFileImpl(
        "git",
        ["-C", cwd, "ls-files", "-z"],
        {
          encoding: "buffer",
          maxBuffer: gitOutputLimit,
          timeout,
        },
        finish,
      );
    } catch (error) {
      finish(error);
    }
  });
}

function languageBucket(path) {
  return extensionBuckets[extname(path).toLowerCase()] ?? "other";
}

function analyzeTrackedFiles(stdout) {
  const output = Buffer.isBuffer(stdout) ? stdout : Buffer.from(stdout);
  const frequencies = new Map(LANG_BUCKETS.map((bucket) => [bucket, 0]));
  let entryCount = 0;
  let entryStart = 0;

  for (let index = 0; index < output.length && entryCount < 5001; index += 1) {
    if (output[index] !== 0) {
      continue;
    }
    if (entryCount < 5000) {
      const path = output.subarray(entryStart, index).toString("utf8");
      const bucket = languageBucket(path);
      frequencies.set(bucket, frequencies.get(bucket) + 1);
    }
    entryCount += 1;
    entryStart = index + 1;
  }

  const repoSizeBucket = entryCount <= 200
    ? "small"
    : entryCount <= 5000
      ? "medium"
      : "large";
  const langBuckets = LANG_BUCKETS
    .filter((bucket) => frequencies.get(bucket) > 0)
    .sort((left, right) => frequencies.get(right) - frequencies.get(left))
    .slice(0, 4);
  return { repoSizeBucket, langBuckets };
}

async function readManifest({ cwd, deadline, readFileImpl, statImpl, nowImpl }) {
  const path = join(cwd, "package.json");
  const metadata = await completeBeforeDeadline({
    operation: () => statImpl(path),
    deadline,
    nowImpl,
    timeoutMessage: "signals digest manifest stat timed out",
  });
  if (
    !Number.isSafeInteger(metadata?.size) ||
    metadata.size < 0 ||
    metadata.size > manifestByteLimit
  ) {
    throw new RangeError("signals digest manifest is too large");
  }
  const controller = new AbortController();
  try {
    const manifest = await completeBeforeDeadline({
      operation: () => readFileImpl(path, { signal: controller.signal }),
      deadline,
      nowImpl,
      timeoutMessage: "signals digest manifest read timed out",
      onTimeout: () => controller.abort(),
    });
    const contents = Buffer.isBuffer(manifest)
      ? manifest
      : Buffer.from(manifest);
    if (contents.byteLength > manifestByteLimit) {
      throw new RangeError("signals digest manifest is too large");
    }
    remainingBudget(deadline, nowImpl);
    const parsed = JSON.parse(contents.toString("utf8"));
    remainingBudget(deadline, nowImpl);
    return parsed?.scripts !== null &&
      typeof parsed?.scripts === "object" &&
      !Array.isArray(parsed.scripts) &&
      typeof parsed.scripts.test === "string";
  } finally {
    controller.abort();
  }
}

function baseDigest({ prompt, deterministicDecision, outcomes }) {
  let stats = {
    wordCount: 0,
    byteLength: 0,
    pathCount: 0,
    structuralScore: 0,
  };
  let deterministicRoute = null;
  let deterministicMethod = null;
  let history = zeroOutcomes;
  try {
    stats = promptStats(prompt);
    deterministicRoute = deterministicDecision.route;
    deterministicMethod = deterministicDecision.method;
    history = outcomes ?? zeroOutcomes;
    return {
      ...stats,
      deterministicRoute,
      deterministicMethod,
      retryEscalations: history.retryEscalations,
      assignmentDenials: history.assignmentDenials,
      smartFallbacks: history.smartFallbacks,
      lastRoute: history.lastRoute,
    };
  } catch {
    return {
      ...stats,
      deterministicRoute,
      deterministicMethod,
      ...zeroOutcomes,
    };
  }
}

export async function buildSignalsDigest({
  prompt,
  deterministicDecision,
  outcomes,
  cwd,
  budgetMs = 100,
  execFileImpl = execFile,
  readFileImpl = readFile,
  statImpl = stat,
  nowImpl = performance.now,
}) {
  const base = baseDigest({ prompt, deterministicDecision, outcomes });
  try {
    const deadline = nowImpl() + budgetMs;
    const stdout = await runGitProbe({
      cwd,
      deadline,
      execFileImpl,
      nowImpl,
    });
    remainingBudget(deadline, nowImpl);
    const tracked = analyzeTrackedFiles(stdout);
    remainingBudget(deadline, nowImpl);
    const testCommandKnown = await readManifest({
      cwd,
      deadline,
      readFileImpl,
      statImpl,
      nowImpl,
    });
    return { ...base, ...tracked, testCommandKnown };
  } catch {
    return { ...base, ...unknownRepo, langBuckets: [] };
  }
}
