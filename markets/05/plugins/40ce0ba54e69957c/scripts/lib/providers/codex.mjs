import {
  SUPPORTED_REASONING_EFFORTS,
  validateModelProfile,
} from "../model-catalog.mjs";
import { validateAgentPolicy } from "../contracts.mjs";
import {
  assignmentRoleContractBlock,
  validateAgentPolicyCapacity,
} from "../delegation-contracts.mjs";
import { isSensitiveSubordinateTask } from "../phrases.mjs";
import {
  assignmentTaskName,
  assignmentTaskNameInfo,
} from "../assignment-tokens.mjs";

function requireObject(value, label) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    throw new TypeError(`${label} must be an object`);
  }
}

const routeRank = Object.freeze({ economy: 0, standard: 1, deep: 2 });
const customAgentForkTurnsPattern = /^(?:none|[1-9][0-9]*)$/;
export function assignmentIdFromToolInput(toolInput) {
  requireObject(toolInput, "spawn_agent tool input");
  const taskNameMatch =
    typeof toolInput.task_name === "string"
      ? assignmentTaskNameInfo(toolInput.task_name)
      : null;
  const encoded = taskNameMatch?.assignmentId ?? null;
  return encoded;
}

function isCheaperAssignment(selected, policy) {
  if (selected.profileKey !== policy.parentProfileKey) {
    return routeRank[selected.profileKey] < routeRank[policy.parentProfileKey];
  }
  return (
    selected.model !== policy.model ||
    SUPPORTED_REASONING_EFFORTS.indexOf(selected.reasoningEffort) <
      SUPPORTED_REASONING_EFFORTS.indexOf(policy.reasoningEffort)
  );
}

export function buildAgentPolicy(decision, routing) {
  requireObject(decision, "routing decision");
  requireObject(routing, "routing configuration");

  const allowed = decision.execution === "agent" && decision.delegationMode === "classifier_proposed";
  if (allowed) {
    if (
      !Number.isInteger(decision.agentCount) ||
      decision.agentCount < 1 ||
      decision.agentCount > routing.maxAutomaticAgents
    ) {
      throw new RangeError(
        "routing decision agentCount exceeds the configured limit",
      );
    }
    validateModelProfile({
      model: decision.model,
      reasoningEffort: decision.reasoningEffort,
    });
  }
  const assignments = {};
  if (allowed && routing.dynamicAgents?.enabled === true && decision.delegationPlan) {
    for (const assignment of decision.delegationPlan.assignments) {
      if (routeRank[assignment.profileKey] > routeRank[decision.route]) {
        throw new RangeError("assignment profile exceeds its parent route");
      }
      const route = routing.routes[assignment.profileKey];
      if (route === undefined) {
        throw new RangeError("assignment profileKey has no configured route");
      }
      assignments[assignment.assignmentId] = {
        role: assignment.role,
        profileKey: assignment.profileKey,
        model: route.model,
        reasoningEffort: assignment.reasoningEffort,
        taskName: assignmentTaskName(assignment, decision.decisionId),
        objectiveKey: assignment.objectiveKey,
        evidenceKey: assignment.evidenceKey,
      };
    }
  }

  const policy = {
    schemaVersion: 2,
    decisionId: decision.decisionId,
    allowed,
    model: allowed ? decision.model : null,
    reasoningEffort: allowed ? decision.reasoningEffort : null,
    parentProfileKey: allowed ? decision.route : "economy",
    dynamicEnabled: routing.dynamicAgents?.enabled === true,
    assignments,
    maxCalls: allowed ? decision.agentCount : 1,
    denyNested: routing.denyNestedAutomaticDelegation,
  };
  if (allowed) {
    validateAgentPolicyCapacity({ decision, policy, routing });
  }
  return policy;
}

export function guardAgentCall(toolInput, policy, context = {}) {
  requireObject(toolInput, "spawn_agent tool input");
  const validatedPolicy = validateAgentPolicy(policy);
  const hasTaskName = Object.hasOwn(toolInput, "task_name");
  const hasMessage = Object.hasOwn(toolInput, "message");
  const hasItems = Object.hasOwn(toolInput, "items");
  if (Object.hasOwn(toolInput, "assignment_id")) {
    return { decision: "deny", reasonCode: "assignment_id_unsupported" };
  }
  const assignmentId = assignmentIdFromToolInput(toolInput);
  if (
    hasTaskName &&
    (typeof toolInput.task_name !== "string" ||
      toolInput.task_name.length === 0)
  ) {
    throw new TypeError(
      "spawn_agent tool input task_name must be a non-empty string",
    );
  }
  if (
    hasMessage &&
    (typeof toolInput.message !== "string" ||
      toolInput.message.length === 0)
  ) {
    throw new TypeError(
      "spawn_agent tool input message must be a non-empty string",
    );
  }
  if (
    hasItems &&
    (!Array.isArray(toolInput.items) || toolInput.items.length === 0)
  ) {
    throw new TypeError(
      "spawn_agent tool input items must be a non-empty array",
    );
  }
  if (hasTaskName && !hasMessage) {
    throw new TypeError(
      "Codex V2 spawn_agent input requires a non-empty message",
    );
  }
  if (!hasTaskName && !hasMessage && !hasItems) {
    throw new TypeError(
      "Codex V1 spawn_agent input requires a non-empty message or items",
    );
  }
  if (
    hasTaskName &&
    toolInput.task_name.startsWith("tx_") &&
    assignmentTaskNameInfo(toolInput.task_name) === null
  ) {
    return { decision: "deny", reasonCode: "assignment_token_mismatch" };
  }

  if (!validatedPolicy.allowed) {
    return {
      decision: "deny",
      reasonCode: "agent_not_allowed",
    };
  }
  if (assignmentId === null) return { decision: "deny", reasonCode: "assignment_task_name_required" };
  if (!validatedPolicy.dynamicEnabled) {
    return { decision: "deny", reasonCode: "dynamic_agents_disabled" };
  }
  const assignment = validatedPolicy.assignments[assignmentId];
  if (!assignment) {
    return { decision: "deny", reasonCode: "assignment_unknown" };
  }
  if (
    hasTaskName &&
    toolInput.task_name !== assignment.taskName
  ) {
    return { decision: "deny", reasonCode: "assignment_token_mismatch" };
  }
  if (Object.hasOwn(toolInput, "agent_type")) {
    return { decision: "deny", reasonCode: "assignment_agent_type_forbidden" };
  }
  if (typeof toolInput.message !== "string") {
    return { decision: "deny", reasonCode: "assignment_message_required" };
  }
  if (
    (Object.hasOwn(toolInput, "model") ||
      Object.hasOwn(toolInput, "reasoning_effort"))
  ) {
    return { decision: "deny", reasonCode: "assignment_profile_override_forbidden" };
  }
  if (
    validatedPolicy.denyNested &&
    context.isNested === true
  ) {
    return {
      decision: "deny",
      reasonCode: "nested_agent_denied",
    };
  }
  if (context.claimed === false) {
    return {
      decision: "deny",
      reasonCode: context.claimReasonCode ?? "agent_claim_denied",
    };
  }

  const selected = assignment;
  const cheaperAssignment = isCheaperAssignment(selected, validatedPolicy);
  if (
    cheaperAssignment &&
    isSensitiveSubordinateTask(toolInput.message)
  ) {
    return { decision: "deny", reasonCode: "assignment_task_sensitive" };
  }
  validateModelProfile({
    model: selected.model,
    reasoningEffort: selected.reasoningEffort,
  });
  const updatedInput = { ...toolInput };
  updatedInput.model = selected.model;
  updatedInput.reasoning_effort = selected.reasoningEffort;
  if (
    (typeof updatedInput.fork_turns !== "string" ||
      !customAgentForkTurnsPattern.test(updatedInput.fork_turns))
  ) {
    // An absent fork_turns is a FULL-HISTORY fork, not a bounded one. The
    // advertised contract tells parents to omit it, so leaving it absent
    // hands the child the entire parent conversation and defeats both the
    // injected role contract and the cost bound. Verified against
    // codex-cli 0.146.0: omitted leaks a parent-only codeword to the child;
    // "none" does not.
    updatedInput.fork_turns = "none";
  }
  if (typeof updatedInput.message === "string") {
    updatedInput.message =
      `${assignmentRoleContractBlock(assignment)}\n\n${updatedInput.message}`;
  }
  return {
    decision: "allow",
    reasonCode: "policy_applied",
    residualWarningCode:
      context.depthObservable === true
        ? null
        : "subagent_depth_unobservable",
    updatedInput,
  };
}

export const codexProvider = Object.freeze({
  id: "codex",
  buildAgentPolicy,
  guardAgentCall,
});
