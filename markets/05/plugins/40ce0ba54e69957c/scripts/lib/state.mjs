import { createHash, randomUUID } from "node:crypto";
import {
  chmod,
  mkdir,
  open,
  readFile,
  rename,
  stat,
  unlink,
  writeFile,
} from "node:fs/promises";
import { isAbsolute, join, resolve } from "node:path";
import { setTimeout as delay } from "node:timers/promises";

import { validateRoutingDecision } from "./contracts.mjs";
import { validateModelPinProfile } from "./model-pin-controls.mjs";

const lockRetryDelayMs = 10;
const lockRetryLimit = 100;
const staleLockAgeMs = 5_000;
const outcomeKeys = [
  "assignmentDenials",
  "lastRoute",
  "retryEscalations",
  "smartFallbacks",
];
const outcomeCounterKeys = [
  "retryEscalations",
  "assignmentDenials",
  "smartFallbacks",
];
const routeNames = new Set(["economy", "standard", "deep"]);

function requirePluginData(pluginData) {
  if (typeof pluginData !== "string" || !isAbsolute(pluginData)) {
    throw new TypeError("pluginData must be an absolute path");
  }
  return resolve(pluginData);
}

function requireSessionId(sessionId) {
  if (typeof sessionId !== "string" || sessionId.length === 0) {
    throw new TypeError("sessionId must be a non-empty string");
  }
}

function requireOptionalDecisionId(value, label) {
  if (value !== null && value !== undefined) {
    if (typeof value !== "string" || value.length === 0) {
      throw new TypeError(`${label} must be a non-empty string when provided`);
    }
  }
}

function requireOptionalTurnId(value, label) {
  if (value !== null && value !== undefined) {
    if (typeof value !== "string" || value.length === 0) {
      throw new TypeError(`${label} must be a non-empty string when provided`);
    }
  }
}

function matchesExpectedTurn(decision, expectedTurnId) {
  return expectedTurnId === null || expectedTurnId === undefined ||
    decision.observedTurnId === expectedTurnId;
}

function sessionDigest(sessionId) {
  return createHash("sha256").update(sessionId).digest("hex");
}

function stateDirectory(pluginData) {
  return join(requirePluginData(pluginData), "state");
}

export function statePath({ pluginData, sessionId }) {
  const dataRoot = requirePluginData(pluginData);
  requireSessionId(sessionId);
  return join(dataRoot, "state", `${sessionDigest(sessionId)}.json`);
}

export function outcomesPath({ pluginData, sessionId }) {
  const dataRoot = requirePluginData(pluginData);
  requireSessionId(sessionId);
  return join(dataRoot, "state", `${sessionDigest(sessionId)}.outcomes.json`);
}

export function modelPinPath({ pluginData, sessionId }) {
  const dataRoot = requirePluginData(pluginData);
  requireSessionId(sessionId);
  return join(dataRoot, "state", `${sessionDigest(sessionId)}.pin.json`);
}

export function zeroOutcomes() {
  return {
    retryEscalations: 0,
    assignmentDenials: 0,
    smartFallbacks: 0,
    lastRoute: null,
  };
}

function requireOutcomeMaxAge(maxAgeMs) {
  if (!Number.isSafeInteger(maxAgeMs) || maxAgeMs <= 0) {
    throw new RangeError("maxAgeMs must be a positive safe integer");
  }
}

function requireOutcomeNow(nowMs) {
  if (!Number.isSafeInteger(nowMs) || nowMs < 0) {
    throw new TypeError("nowMs must be a non-negative safe integer");
  }
}

function validateOutcomes(value) {
  if (
    value === null ||
    typeof value !== "object" ||
    Array.isArray(value) ||
    Object.keys(value).sort().join(",") !== outcomeKeys.join(",")
  ) {
    throw new TypeError("routing outcomes have an invalid shape");
  }
  for (const key of outcomeCounterKeys) {
    if (!Number.isInteger(value[key]) || value[key] < 0 || value[key] > 99) {
      throw new RangeError(`routing outcomes ${key} must be from 0 to 99`);
    }
  }
  if (value.lastRoute !== null && !routeNames.has(value.lastRoute)) {
    throw new RangeError("routing outcomes lastRoute is invalid");
  }
  return { ...value };
}

function validateOutcomeRecord(value) {
  if (
    value === null ||
    typeof value !== "object" ||
    Array.isArray(value) ||
    Object.keys(value).sort().join(",") !== "outcomes,schemaVersion,updatedAtMs"
  ) {
    throw new TypeError("routing outcomes record has an invalid shape");
  }
  if (value.schemaVersion !== 2) {
    throw new RangeError("routing outcomes schemaVersion must be 2");
  }
  requireOutcomeNow(value.updatedAtMs);
  return {
    schemaVersion: 2,
    updatedAtMs: value.updatedAtMs,
    outcomes: validateOutcomes(value.outcomes),
  };
}

function validateModelPinRecord(value) {
  const keys =
    value !== null && typeof value === "object" && !Array.isArray(value)
      ? Object.keys(value).sort().join(",")
      : null;
  if (keys !== "profile,schemaVersion,updatedAtMs") {
    throw new TypeError("model pin record has an invalid shape");
  }
  if (value.schemaVersion !== 1) {
    throw new RangeError("model pin record schemaVersion must be 1");
  }
  requireOutcomeNow(value.updatedAtMs);
  return {
    schemaVersion: 1,
    updatedAtMs: value.updatedAtMs,
    profile: validateModelPinProfile(value.profile),
  };
}

async function ensureStateDirectory(pluginData) {
  const directory = stateDirectory(pluginData);
  await mkdir(directory, { recursive: true, mode: 0o700 });
  await chmod(directory, 0o700);
  return directory;
}

function validateRecord(value) {
  const keys =
    value !== null && typeof value === "object" && !Array.isArray(value)
      ? Object.keys(value).sort().join(",")
      : null;
  if (
    keys !== "claimedCalls,decision,schemaVersion" &&
    keys !== "claimedAssignmentIds,claimedCalls,decision,schemaVersion"
  ) {
    throw new TypeError("routing state record has an invalid shape");
  }
  if (value.schemaVersion !== 2) {
    throw new RangeError("routing state schemaVersion must be 2");
  }
  if (!Number.isInteger(value.claimedCalls) || value.claimedCalls < 0) {
    throw new RangeError(
      "routing state claimedCalls must be a non-negative integer",
    );
  }
  const claimedAssignmentIds = value.claimedAssignmentIds ?? [];
  if (
    !Array.isArray(claimedAssignmentIds) ||
    claimedAssignmentIds.some(
      (assignmentId) =>
        typeof assignmentId !== "string" || !/^a[1-9][0-9]*$/.test(assignmentId),
    ) ||
    new Set(claimedAssignmentIds).size !== claimedAssignmentIds.length
  ) {
    throw new RangeError(
      "routing state claimedAssignmentIds must be unique assignment IDs",
    );
  }
  return {
    schemaVersion: 2,
    decision: validateRoutingDecision(value.decision),
    claimedCalls: value.claimedCalls,
    claimedAssignmentIds: [...claimedAssignmentIds],
  };
}

async function writeRecord({ pluginData, sessionId, record }) {
  const path = statePath({ pluginData, sessionId });
  const directory = await ensureStateDirectory(pluginData);

  const temporaryPath = join(
    directory,
    `.${sessionDigest(sessionId)}-${randomUUID()}.tmp`,
  );
  try {
    await writeFile(temporaryPath, `${JSON.stringify(record)}\n`, {
      encoding: "utf8",
      flag: "wx",
      mode: 0o600,
    });
    await rename(temporaryPath, path);
    await chmod(path, 0o600);
  } catch (error) {
    try {
      await unlink(temporaryPath);
    } catch (cleanupError) {
      if (cleanupError?.code !== "ENOENT") {
        error.cleanupError = cleanupError;
      }
    }
    throw error;
  }
}

async function writeOutcomeRecord({ pluginData, sessionId, record }) {
  const path = outcomesPath({ pluginData, sessionId });
  const directory = await ensureStateDirectory(pluginData);
  const temporaryPath = join(
    directory,
    `.${sessionDigest(sessionId)}-${randomUUID()}.outcomes.tmp`,
  );
  try {
    await writeFile(temporaryPath, `${JSON.stringify(record)}\n`, {
      encoding: "utf8",
      flag: "wx",
      mode: 0o600,
    });
    await rename(temporaryPath, path);
    await chmod(path, 0o600);
  } catch (error) {
    try {
      await unlink(temporaryPath);
    } catch (cleanupError) {
      if (cleanupError?.code !== "ENOENT") {
        error.cleanupError = cleanupError;
      }
    }
    throw error;
  }
}

async function writeModelPinRecord({ pluginData, sessionId, record }) {
  const path = modelPinPath({ pluginData, sessionId });
  const directory = await ensureStateDirectory(pluginData);
  const temporaryPath = join(
    directory,
    `.${sessionDigest(sessionId)}-${randomUUID()}.pin.tmp`,
  );
  try {
    await writeFile(temporaryPath, `${JSON.stringify(record)}\n`, {
      encoding: "utf8",
      flag: "wx",
      mode: 0o600,
    });
    await chmod(temporaryPath, 0o600);
    await rename(temporaryPath, path);
  } catch (error) {
    try {
      await unlink(temporaryPath);
    } catch (cleanupError) {
      if (cleanupError?.code !== "ENOENT") {
        error.cleanupError = cleanupError;
      }
    }
    throw error;
  }
}

async function readRecord({ pluginData, sessionId }) {
  const path = statePath({ pluginData, sessionId });
  let serialized;
  try {
    serialized = await readFile(path, "utf8");
  } catch (error) {
    if (error?.code === "ENOENT") {
      return null;
    }
    throw error;
  }
  let value;
  try {
    value = JSON.parse(serialized);
  } catch (error) {
    throw new SyntaxError(`invalid routing state JSON: ${error.message}`);
  }
  const record = validateRecord(value);
  if (record.decision.sessionId !== sessionId) {
    throw new RangeError("routing state session does not match its path");
  }
  return record;
}

async function readOutcomeRecord({ pluginData, sessionId }) {
  const path = outcomesPath({ pluginData, sessionId });
  let serialized;
  try {
    serialized = await readFile(path, "utf8");
  } catch (error) {
    if (error?.code === "ENOENT") {
      return null;
    }
    throw error;
  }
  let value;
  try {
    value = JSON.parse(serialized);
  } catch (error) {
    throw new SyntaxError(`invalid routing outcomes JSON: ${error.message}`);
  }
  return validateOutcomeRecord(value);
}

export class StoredModelPinError extends Error {
  constructor(message, options = {}) {
    super(message, options);
    this.name = "StoredModelPinError";
  }
}

export function isStoredModelPinError(error) {
  return error instanceof StoredModelPinError;
}

async function readModelPinRecord({ pluginData, sessionId }) {
  const path = modelPinPath({ pluginData, sessionId });
  let serialized;
  try {
    serialized = await readFile(path, "utf8");
  } catch (error) {
    if (error?.code === "ENOENT") {
      return null;
    }
    throw error;
  }
  try {
    return validateModelPinRecord(JSON.parse(serialized));
  } catch (error) {
    throw new StoredModelPinError("stored model pin is invalid", {
      cause: error,
    });
  }
}

function requireFresh(record, nowMs) {
  if (!Number.isSafeInteger(nowMs) || nowMs < 0) {
    throw new TypeError("nowMs must be a non-negative safe integer");
  }
  if (nowMs >= record.decision.expiresAtMs) {
    throw new RangeError("routing decision expired");
  }
}

async function removeAgedPath(path) {
  let metadata;
  try {
    metadata = await stat(path);
  } catch (error) {
    if (error?.code === "ENOENT") {
      return false;
    }
    throw error;
  }
  if (Date.now() - metadata.mtimeMs < staleLockAgeMs) {
    return false;
  }
  let current;
  try {
    current = await stat(path);
  } catch (error) {
    if (error?.code === "ENOENT") {
      return false;
    }
    throw error;
  }
  if (
    current.dev !== metadata.dev ||
    current.ino !== metadata.ino ||
    current.mtimeMs !== metadata.mtimeMs
  ) {
    return false;
  }
  // Node does not expose conditional unlink. Rechecking the inode narrows the
  // replacement window; the recovery sentinel serializes competing recoverers.
  try {
    await unlink(path);
  } catch (error) {
    if (error?.code !== "ENOENT") {
      throw error;
    }
  }
  return true;
}

async function removeStaleLock(lockPath) {
  const recoveryPath = `${lockPath}.recovery`;
  // Age out orphaned recovery markers so a crashed recovery cannot permanently
  // block the session (removeStaleLock used to return false forever on EEXIST).
  await removeAgedPath(recoveryPath);

  let recoveryHandle;
  try {
    recoveryHandle = await open(recoveryPath, "wx", 0o600);
  } catch (error) {
    if (error?.code === "EEXIST") {
      return false;
    }
    throw error;
  }

  try {
    let metadata;
    try {
      metadata = await stat(lockPath);
    } catch (error) {
      if (error?.code === "ENOENT") {
        return true;
      }
      throw error;
    }
    if (Date.now() - metadata.mtimeMs < staleLockAgeMs) {
      return false;
    }
    const staleLockId = (await readFile(lockPath, "utf8")).trim();
    let currentMetadata;
    let currentLockId;
    try {
      currentMetadata = await stat(lockPath);
      currentLockId = (await readFile(lockPath, "utf8")).trim();
    } catch (error) {
      if (error?.code === "ENOENT") {
        return true;
      }
      throw error;
    }
    if (
      currentMetadata.dev !== metadata.dev ||
      currentMetadata.ino !== metadata.ino ||
      currentMetadata.mtimeMs !== metadata.mtimeMs ||
      currentLockId !== staleLockId
    ) {
      return false;
    }
    try {
      await unlink(lockPath);
    } catch (error) {
      if (error?.code !== "ENOENT") {
        throw error;
      }
    }
    return true;
  } finally {
    await recoveryHandle.close();
    try {
      await unlink(recoveryPath);
    } catch (error) {
      if (error?.code !== "ENOENT") {
        throw error;
      }
    }
  }
}

async function acquireStateLock(lockPath) {
  for (let attempt = 0; attempt < lockRetryLimit; attempt += 1) {
    const lockId = randomUUID();
    let handle;
    try {
      handle = await open(lockPath, "wx", 0o600);
      await handle.writeFile(`${lockId}\n`, "utf8");
      return { handle, lockId };
    } catch (error) {
      if (handle) {
        await handle.close();
        try {
          await unlink(lockPath);
        } catch (cleanupError) {
          if (cleanupError?.code !== "ENOENT") {
            error.cleanupError = cleanupError;
          }
        }
      }
      if (error?.code !== "EEXIST") {
        throw error;
      }
      if (await removeStaleLock(lockPath)) {
        continue;
      }
      if (attempt === lockRetryLimit - 1) {
        throw new Error("routing state is busy");
      }
      await delay(lockRetryDelayMs);
    }
  }
  throw new Error("routing state is busy");
}

async function releaseStateLock(lockPath, lock) {
  await lock.handle.close();
  let currentLockId;
  try {
    currentLockId = (await readFile(lockPath, "utf8")).trim();
  } catch (error) {
    if (error?.code === "ENOENT") {
      return;
    }
    throw error;
  }
  if (currentLockId === lock.lockId) {
    await unlink(lockPath);
  }
}

export async function readModelPin({ pluginData, sessionId }) {
  const record = await readModelPinRecord({ pluginData, sessionId });
  return record?.profile ?? null;
}

export async function writeModelPin({
  pluginData,
  sessionId,
  profile,
  nowMs = Date.now(),
}) {
  requireOutcomeNow(nowMs);
  const validated = validateModelPinProfile(profile);
  await ensureStateDirectory(pluginData);
  const path = modelPinPath({ pluginData, sessionId });
  const lockPath = `${path}.lock`;
  const lock = await acquireStateLock(lockPath);
  try {
    await writeModelPinRecord({
      pluginData,
      sessionId,
      record: {
        schemaVersion: 1,
        updatedAtMs: nowMs,
        profile: validated,
      },
    });
  } finally {
    await releaseStateLock(lockPath, lock);
  }
  return validated;
}

export async function removeModelPin({ pluginData, sessionId }) {
  await ensureStateDirectory(pluginData);
  const path = modelPinPath({ pluginData, sessionId });
  const lockPath = `${path}.lock`;
  const lock = await acquireStateLock(lockPath);
  try {
    try {
      await unlink(path);
      return true;
    } catch (error) {
      if (error?.code === "ENOENT") {
        return false;
      }
      throw error;
    }
  } finally {
    await releaseStateLock(lockPath, lock);
  }
}

export async function writeDecision({
  pluginData,
  decision,
  expectedDecisionId = null,
}) {
  const validated = validateRoutingDecision(decision);
  requireOptionalDecisionId(expectedDecisionId, "expectedDecisionId");
  await ensureStateDirectory(pluginData);
  const path = statePath({
    pluginData,
    sessionId: validated.sessionId,
  });
  const lockPath = `${path}.lock`;
  const lock = await acquireStateLock(lockPath);
  try {
    if (expectedDecisionId !== null) {
      const current = await readRecord({
        pluginData,
        sessionId: validated.sessionId,
      });
      if (current?.decision.decisionId !== expectedDecisionId) {
        throw new RangeError("routing decision changed before replacement");
      }
    }
    await writeRecord({
      pluginData,
      sessionId: validated.sessionId,
      record: {
        schemaVersion: 2,
        decision: validated,
        claimedCalls: 0,
        claimedAssignmentIds: [],
      },
    });
  } finally {
    await releaseStateLock(lockPath, lock);
  }
  return validated;
}

export async function readDecision({
  pluginData,
  sessionId,
  expectedTurnId = null,
  nowMs = Date.now(),
}) {
  requireOptionalTurnId(expectedTurnId, "expectedTurnId");
  const record = await readRecord({ pluginData, sessionId });
  if (!record) {
    return null;
  }
  requireFresh(record, nowMs);
  if (!matchesExpectedTurn(record.decision, expectedTurnId)) {
    throw new RangeError("routing decision turn changed");
  }
  return record.decision;
}

export async function readOutcomes({
  pluginData,
  sessionId,
  nowMs = Date.now(),
  maxAgeMs,
}) {
  requireOutcomeNow(nowMs);
  requireOutcomeMaxAge(maxAgeMs);
  const record = await readOutcomeRecord({ pluginData, sessionId });
  if (!record || nowMs - record.updatedAtMs >= maxAgeMs) {
    return null;
  }
  return record.outcomes;
}

export async function readOrResetOutcomesForPrompt({
  pluginData,
  sessionId,
  nowMs = Date.now(),
  maxAgeMs,
}) {
  requireOutcomeNow(nowMs);
  requireOutcomeMaxAge(maxAgeMs);
  const path = outcomesPath({ pluginData, sessionId });
  await ensureStateDirectory(pluginData);
  const lockPath = `${path}.lock`;
  const lock = await acquireStateLock(lockPath);
  try {
    try {
      const record = await readOutcomeRecord({ pluginData, sessionId });
      if (record === null || nowMs - record.updatedAtMs < maxAgeMs) {
        return record?.outcomes ?? zeroOutcomes();
      }
      const outcomes = zeroOutcomes();
      await writeOutcomeRecord({
        pluginData,
        sessionId,
        record: { schemaVersion: 2, updatedAtMs: nowMs, outcomes },
      });
      return outcomes;
    } catch (error) {
      if (!(error instanceof SyntaxError || error instanceof TypeError || error instanceof RangeError)) {
        throw error;
      }
      try {
        await unlink(path);
      } catch (unlinkError) {
        if (unlinkError?.code !== "ENOENT") throw unlinkError;
      }
      const outcomes = zeroOutcomes();
      await writeOutcomeRecord({
        pluginData,
        sessionId,
        record: { schemaVersion: 2, updatedAtMs: nowMs, outcomes },
      });
      return outcomes;
    }
  } finally {
    await releaseStateLock(lockPath, lock);
  }
}

export async function recordOutcome({
  pluginData,
  sessionId,
  kind,
  route = null,
  nowMs = Date.now(),
  maxAgeMs,
}) {
  requireOutcomeNow(nowMs);
  requireOutcomeMaxAge(maxAgeMs);
  if (
    kind !== "retryEscalation" &&
    kind !== "assignmentDenial" &&
    kind !== "smartFallback" &&
    kind !== "lastRoute"
  ) {
    throw new RangeError("outcome kind is invalid");
  }
  if (kind === "lastRoute") {
    if (!routeNames.has(route)) {
      throw new RangeError("lastRoute outcome requires a valid route");
    }
  } else if (route !== null) {
    throw new RangeError("route is valid only for a lastRoute outcome");
  }

  const path = outcomesPath({ pluginData, sessionId });
  await ensureStateDirectory(pluginData);
  const lockPath = `${path}.lock`;
  const lock = await acquireStateLock(lockPath);
  try {
    const current = await readOutcomeRecord({ pluginData, sessionId });
    const outcomes =
      current === null || nowMs - current.updatedAtMs >= maxAgeMs
        ? zeroOutcomes()
        : current.outcomes;
    const next = { ...outcomes };
    if (kind === "lastRoute") {
      next.lastRoute = route;
    } else {
      const key = {
        retryEscalation: "retryEscalations",
        assignmentDenial: "assignmentDenials",
        smartFallback: "smartFallbacks",
      }[kind];
      next[key] = Math.min(99, next[key] + 1);
    }
    await writeOutcomeRecord({
      pluginData,
      sessionId,
      record: { schemaVersion: 2, updatedAtMs: nowMs, outcomes: next },
    });
  } finally {
    await releaseStateLock(lockPath, lock);
  }
  return { recorded: true };
}

export async function claimAgentCall({
  pluginData,
  sessionId,
  expectedDecisionId,
  expectedTurnId = null,
  nowMs = Date.now(),
  maxCalls,
  assignmentId = null,
  isNested = false,
  denyNested = true,
}) {
  if (!Number.isInteger(maxCalls) || maxCalls <= 0) {
    throw new RangeError("maxCalls must be a positive integer");
  }
  requireOptionalDecisionId(expectedDecisionId, "expectedDecisionId");
  if (expectedDecisionId === null || expectedDecisionId === undefined) {
    throw new TypeError("expectedDecisionId must be a non-empty string");
  }
  requireOptionalTurnId(expectedTurnId, "expectedTurnId");
  if (assignmentId !== null && (typeof assignmentId !== "string" || assignmentId.length === 0)) {
    throw new TypeError("assignmentId must be a non-empty string when provided");
  }
  const path = statePath({ pluginData, sessionId });
  const lockPath = `${path}.lock`;
  await ensureStateDirectory(pluginData);
  const lock = await acquireStateLock(lockPath);

  try {
    const record = await readRecord({ pluginData, sessionId });
    if (!record) {
      return {
        claimed: false,
        reasonCode: "missing_decision",
        claimedCalls: 0,
      };
    }
    requireFresh(record, nowMs);
    if (record.decision.decisionId !== expectedDecisionId) {
      return {
        claimed: false,
        reasonCode: "decision_changed",
        claimedCalls: record.claimedCalls,
      };
    }
    if (!matchesExpectedTurn(record.decision, expectedTurnId)) {
      return {
        claimed: false,
        reasonCode: "turn_changed",
        claimedCalls: record.claimedCalls,
      };
    }
    if (denyNested && isNested) {
      return {
        claimed: false,
        reasonCode: "nested_agent_denied",
        claimedCalls: record.claimedCalls,
      };
    }
    let assignment = null;
    if (assignmentId === null) {
      return { claimed: false, reasonCode: "assignment_unknown", claimedCalls: record.claimedCalls };
    }
    {
      assignment = record.decision.delegationPlan?.assignments.find(
        (candidate) => candidate.assignmentId === assignmentId,
      );
      if (!assignment) {
        return {
          claimed: false,
          reasonCode: "assignment_unknown",
          claimedCalls: record.claimedCalls,
        };
      }
      if (record.claimedAssignmentIds.includes(assignmentId)) {
        return {
          claimed: false,
          reasonCode: "assignment_already_claimed",
          claimedCalls: record.claimedCalls,
        };
      }
    }
    if (record.claimedCalls >= maxCalls) {
      return {
        claimed: false,
        reasonCode: "agent_limit_reached",
        claimedCalls: record.claimedCalls,
      };
    }

    const next = {
      ...record,
      claimedCalls: record.claimedCalls + 1,
      claimedAssignmentIds:
        assignmentId === null
          ? record.claimedAssignmentIds
          : [...record.claimedAssignmentIds, assignmentId],
    };
    await writeRecord({
      pluginData,
      sessionId,
      record: next,
    });
    return {
      claimed: true,
      reasonCode: "agent_call_claimed",
      claimedCalls: next.claimedCalls,
      decision: next.decision,
      assignment,
    };
  } finally {
    await releaseStateLock(lockPath, lock);
  }
}

export async function removeSessionState({
  pluginData,
  sessionId,
  expectedDecisionId = null,
  includeOutcomes = false,
  includeModelPin = false,
}) {
  requireOptionalDecisionId(expectedDecisionId, "expectedDecisionId");
  const path = statePath({ pluginData, sessionId });
  const lockPath = `${path}.lock`;
  const outcomePath = includeOutcomes
    ? outcomesPath({ pluginData, sessionId })
    : null;
  const outcomeLockPath = outcomePath === null ? null : `${outcomePath}.lock`;
  const pinPath = includeModelPin
    ? modelPinPath({ pluginData, sessionId })
    : null;
  const pinLockPath = pinPath === null ? null : `${pinPath}.lock`;
  await ensureStateDirectory(pluginData);
  const lock = await acquireStateLock(lockPath);
  let outcomeLock = null;
  let pinLock = null;
  try {
    if (expectedDecisionId !== null) {
      const current = await readRecord({ pluginData, sessionId });
      if (current?.decision.decisionId !== expectedDecisionId) {
        return false;
      }
    }
    if (outcomeLockPath !== null) {
      outcomeLock = await acquireStateLock(outcomeLockPath);
    }
    if (pinLockPath !== null) {
      pinLock = await acquireStateLock(pinLockPath);
    }
    let removed = false;
    for (const target of [
      path,
      ...(outcomePath === null ? [] : [outcomePath]),
      ...(pinPath === null ? [] : [pinPath]),
    ]) {
      try {
        await unlink(target);
        removed = true;
      } catch (error) {
        if (error?.code !== "ENOENT") {
          throw error;
        }
      }
    }
    return removed;
  } finally {
    try {
      if (pinLock !== null) {
        await releaseStateLock(pinLockPath, pinLock);
      }
    } finally {
      try {
        if (outcomeLock !== null) {
          await releaseStateLock(outcomeLockPath, outcomeLock);
        }
      } finally {
        await releaseStateLock(lockPath, lock);
      }
    }
  }
}
