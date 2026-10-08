import {
  SUPPORTED_REASONING_EFFORTS,
  validateModelProfile,
} from "./model-catalog.mjs";
import { TASK_PROFILE_KEYS } from "./task-profiles.mjs";
import {
  assignmentTaskNameMatchesDecision,
} from "./assignment-tokens.mjs";
import {
  MAX_ASSIGNMENTS_BY_ROUTE,
  validateClassifierAssignment,
  validateDelegationMode,
} from "./delegation-contracts.mjs";

const routes = new Set([
  "passthrough",
  "parent",
  "economy",
  "standard",
  "deep",
]);
const hookEvents = new Set([
  "SessionStart",
  "UserPromptSubmit",
  "PreToolUse",
  "SessionEnd",
]);
const decisionKeys = [
  "agentCount",
  "createdAtMs",
  "delegationMode",
  "delegationPlan",
  "decisionId",
  "execution",
  "expiresAtMs",
  "explicit",
  "method",
  "model",
  "observedTurnId",
  "provider",
  "reasonCodes",
  "reasoningEffort",
  "route",
  "schemaVersion",
  "sessionId",
];
const assignmentKeys = [
  "assignmentId",
  "evidenceKey",
  "objectiveKey",
  "ordinal",
  "profileKey",
  "promptTemplateKey",
  "reasoningEffort",
  "role",
  "taskProfile",
];
const delegationPlanKeys = [
  "assignments",
  "decisionId",
  "parentRoute",
  "schemaVersion",
  "source",
];
const assignmentRoles = new Set([
  "repo_reader",
  "repo_reviewer",
  "test_runner",
  "file_editor",
  "implementer",
]);
const assignmentTaskProfiles = new Set(TASK_PROFILE_KEYS);
const delegationProfileKeys = new Set(["economy", "standard", "deep"]);
const delegationRouteRank = Object.freeze({ economy: 0, standard: 1, deep: 2 });
const policyKeys = [
  "allowed",
  "assignments",
  "decisionId",
  "denyNested",
  "dynamicEnabled",
  "maxCalls",
  "model",
  "parentProfileKey",
  "reasoningEffort",
  "schemaVersion",
];

export function isPlainObject(value) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    return false;
  }
  const prototype = Object.getPrototypeOf(value);
  return prototype === Object.prototype || prototype === null;
}

export function requirePlainObject(value, label) {
  if (!isPlainObject(value)) {
    throw new TypeError(`${label} must be an object`);
  }
}

function requireExactKeys(value, expected, label) {
  requirePlainObject(value, label);
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

function requireString(value, label) {
  if (typeof value !== "string" || value.length === 0) {
    throw new TypeError(`${label} must be a non-empty string`);
  }
}

function requireOptionalString(value, label) {
  if (value !== null && value !== undefined) {
    requireString(value, label);
  }
}

function clone(value) {
  return structuredClone(value);
}

export function validateAgentAssignment(value) {
  return validateClassifierAssignment(value);
}

export function validateDelegationPlan(value) {
  requireExactKeys(value, delegationPlanKeys, "delegation plan");
  if (value.schemaVersion !== 2) {
    throw new RangeError("delegation plan schemaVersion must be 2");
  }
  if (value.source !== "classifier") throw new RangeError("delegation plan source must be classifier");
  requireString(value.decisionId, "delegation plan decisionId");
  if (!delegationProfileKeys.has(value.parentRoute)) {
    throw new RangeError(
      `unsupported delegation plan parentRoute: ${value.parentRoute}`,
    );
  }
  if (
    !Array.isArray(value.assignments) ||
    value.assignments.length < 1 ||
    value.assignments.length > MAX_ASSIGNMENTS_BY_ROUTE[value.parentRoute]
  ) {
    throw new RangeError("delegation plan assignments must contain 1 to 4 items");
  }
  const assignmentIds = new Set();
  for (const [index, assignment] of value.assignments.entries()) {
    const validated = validateAgentAssignment(assignment);
    if (assignmentIds.has(validated.assignmentId)) {
      throw new RangeError(
        `delegation plan has duplicate assignmentId: ${validated.assignmentId}`,
      );
    }
    assignmentIds.add(validated.assignmentId);
    if (validated.ordinal !== index + 1) {
      throw new RangeError("delegation plan assignment ordinals must be contiguous");
    }
  }
  return clone(value);
}

export function normalizeRoutingDecision(value) {
  requirePlainObject(value, "routing decision");
  return clone(value);
}

export function validateRoutingDecision(value) {
  const normalized = normalizeRoutingDecision(value);
  requireExactKeys(normalized, decisionKeys, "routing decision");
  if (normalized.schemaVersion !== 2) {
    throw new RangeError("routing decision schemaVersion must be 2");
  }
  requireString(normalized.decisionId, "routing decision decisionId");
  if (!/^tx_[a-f0-9]{24}$/.test(normalized.decisionId)) {
    throw new RangeError("routing decision decisionId is invalid");
  }
  requireString(normalized.sessionId, "routing decision sessionId");
  requireOptionalString(
    normalized.observedTurnId,
    "routing decision observedTurnId",
  );
  if (normalized.provider !== "codex") {
    throw new RangeError("routing decision provider must be codex");
  }
  if (!routes.has(normalized.route)) {
    throw new RangeError(`unsupported routing decision route: ${normalized.route}`);
  }
  const expectedExecution = {
    passthrough: "none",
    parent: "parent",
    economy: "agent",
    standard: "agent",
    deep: "agent",
  }[normalized.route];
  if (normalized.execution !== expectedExecution) {
    throw new RangeError(
      `routing decision execution must be ${expectedExecution} for ${value.route}`,
    );
  }
  if (normalized.execution === "agent") {
    if (
      !Number.isInteger(normalized.agentCount) ||
      normalized.agentCount < 1 ||
      normalized.agentCount > MAX_ASSIGNMENTS_BY_ROUTE[normalized.route]
    ) {
      throw new RangeError(
        "agent routing decisions require an agentCount from 1 to 4",
      );
    }
    validateModelProfile({
      model: normalized.model,
      reasoningEffort: normalized.reasoningEffort,
    });
  } else if (
    normalized.agentCount !== 0 ||
    normalized.model !== null ||
    normalized.reasoningEffort !== null
  ) {
    throw new RangeError(
      "non-agent routing decisions must not select agents, a model, or effort",
    );
  }
  requireString(normalized.method, "routing decision method");
  if (
    !Array.isArray(normalized.reasonCodes) ||
    normalized.reasonCodes.length === 0 ||
    normalized.reasonCodes.length > 12
  ) {
    throw new RangeError(
      "routing decision reasonCodes must contain 1 to 12 items",
    );
  }
  for (const reason of normalized.reasonCodes) {
    if (
      typeof reason !== "string" ||
      !/^[a-z0-9_]{1,64}$/.test(reason)
    ) {
      throw new RangeError(`invalid routing reason code: ${String(reason)}`);
    }
  }
  if (typeof normalized.explicit !== "boolean") {
    throw new TypeError("routing decision explicit must be boolean");
  }
  if (
    !Number.isSafeInteger(normalized.createdAtMs) ||
    normalized.createdAtMs < 0 ||
    !Number.isSafeInteger(normalized.expiresAtMs) ||
    normalized.expiresAtMs <= normalized.createdAtMs
  ) {
    throw new RangeError("routing decision timestamps are invalid");
  }
  validateDelegationMode(normalized.delegationMode);
  if (normalized.delegationMode === "none" && normalized.delegationPlan !== null) {
    throw new RangeError("none delegation mode must not include a delegation plan");
  }
  if (normalized.delegationMode === "classifier_proposed" && normalized.delegationPlan === null) {
    throw new RangeError("classifier_proposed delegation mode requires a delegation plan");
  }
  if (normalized.delegationPlan !== null) {
    const plan = validateDelegationPlan(normalized.delegationPlan);
    if (plan.decisionId !== normalized.decisionId) {
      throw new RangeError("delegation plan decisionId must match routing decision");
    }
    if (normalized.agentCount !== plan.assignments.length) {
      throw new RangeError("routing decision agentCount must match its delegation plan");
    }
    if (plan.parentRoute !== normalized.route) {
      throw new RangeError("delegation plan parentRoute must match routing decision");
    }
    if (normalized.execution !== "agent") {
      throw new RangeError("non-agent routing decisions must not include a delegation plan");
    }
    if (plan.assignments.length !== normalized.agentCount) {
      throw new RangeError(
        "delegation plan assignments must match routing decision agentCount",
      );
    }
    for (const assignment of plan.assignments) {
      if (
        delegationRouteRank[assignment.profileKey] >
        delegationRouteRank[normalized.route]
      ) {
        throw new RangeError("delegation plan assignment exceeds its parent route");
      }
      if (
        SUPPORTED_REASONING_EFFORTS.indexOf(assignment.reasoningEffort) >
        SUPPORTED_REASONING_EFFORTS.indexOf(normalized.reasoningEffort)
      ) {
        throw new RangeError(
          "delegation plan assignment effort exceeds its parent effort",
        );
      }
    }
  }
  return clone(normalized);
}

export function validateAgentPolicy(value) {
  requireExactKeys(value, policyKeys, "agent policy");
  requireString(value.decisionId, "agent policy decisionId");
  if (value.schemaVersion !== 2) throw new RangeError("agent policy schemaVersion must be 2");
  if (!/^tx_[a-f0-9]{24}$/.test(value.decisionId)) throw new RangeError("agent policy decisionId is invalid");
  if (typeof value.allowed !== "boolean") {
    throw new TypeError("agent policy allowed must be boolean");
  }
  if (typeof value.dynamicEnabled !== "boolean") {
    throw new TypeError("agent policy dynamicEnabled must be boolean");
  }
  if (!delegationProfileKeys.has(value.parentProfileKey)) {
    throw new RangeError("agent policy parentProfileKey is unsupported");
  }
  requirePlainObject(value.assignments, "agent policy assignments");
  if (
    Object.keys(value.assignments).length >
      MAX_ASSIGNMENTS_BY_ROUTE[value.parentProfileKey]
  ) {
    throw new RangeError("agent policy assignments exceed the selected-route cap");
  }
  for (const [assignmentId, assignment] of Object.entries(value.assignments)) {
    if (!/^a[1-9][0-9]*$/.test(assignmentId)) {
      throw new RangeError("agent policy assignment ID is invalid");
    }
    requireExactKeys(
      assignment,
      ["evidenceKey", "model", "objectiveKey", "profileKey", "reasoningEffort", "role", "taskName"],
      "agent policy assignment",
    );
    if (!delegationProfileKeys.has(assignment.profileKey)) {
      throw new RangeError("agent policy assignment profileKey is unsupported");
    }
    if (!assignmentRoles.has(assignment.role)) {
      throw new RangeError("agent policy assignment role is unsupported");
    }
    validateClassifierAssignment({
      assignmentId,
      role: assignment.role,
      profileKey: assignment.profileKey,
      reasoningEffort: assignment.reasoningEffort,
      taskProfile: assignment.taskProfile ?? ({ repo_reader: "read", repo_reviewer: "analysis", test_runner: "read", file_editor: "file_edit", implementer: "implementation" })[assignment.role],
      promptTemplateKey: assignment.role,
      ordinal: 1,
      objectiveKey: assignment.objectiveKey,
      evidenceKey: assignment.evidenceKey,
    });
    validateModelProfile({
      model: assignment.model,
      reasoningEffort: assignment.reasoningEffort,
    });
    if (!assignmentTaskNameMatchesDecision(
      assignment.taskName,
      assignmentId,
      value.decisionId,
      assignment.role,
    )) {
      throw new RangeError("agent policy assignment taskName is invalid");
    }
  }
  if (
    !Number.isInteger(value.maxCalls) ||
    value.maxCalls < 1 ||
    value.maxCalls > MAX_ASSIGNMENTS_BY_ROUTE[value.parentProfileKey]
  ) {
    throw new RangeError("agent policy maxCalls must be from 1 to 4");
  }
  if (value.denyNested !== true) {
    throw new RangeError("agent policy denyNested must remain true");
  }
  if (value.allowed) {
    validateModelProfile({
      model: value.model,
      reasoningEffort: value.reasoningEffort,
    });
  } else if (value.model !== null || value.reasoningEffort !== null) {
    throw new RangeError(
      "denied agent policy must not select a model or effort",
    );
  }
  return clone(value);
}

export function validateHookInput(value) {
  requirePlainObject(value, "hook input");
  requireString(value.session_id, "hook input session_id");
  requireString(value.cwd, "hook input cwd");
  requireString(value.hook_event_name, "hook input hook_event_name");
  if (!hookEvents.has(value.hook_event_name)) {
    throw new RangeError(
      `unsupported hook event: ${value.hook_event_name}`,
    );
  }
  requireOptionalString(value.transcript_path, "hook input transcript_path");

  if (value.hook_event_name === "SessionStart") {
    if (!["startup", "resume", "clear", "compact"].includes(value.source)) {
      throw new RangeError("SessionStart source is unsupported");
    }
  } else if (value.hook_event_name === "UserPromptSubmit") {
    requireString(value.turn_id, "UserPromptSubmit turn_id");
    if (typeof value.prompt !== "string") {
      throw new TypeError("UserPromptSubmit prompt must be a string");
    }
  } else if (value.hook_event_name === "PreToolUse") {
    requireString(value.turn_id, "PreToolUse turn_id");
    requireString(value.tool_name, "PreToolUse tool_name");
    requireString(value.tool_use_id, "PreToolUse tool_use_id");
    requirePlainObject(value.tool_input, "PreToolUse tool_input");
  } else if (value.reason !== "other") {
    throw new RangeError("SessionEnd reason must be other");
  }

  return clone(value);
}
