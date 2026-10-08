import { validateConfig } from "./config.mjs";
import { validateDelegationPlan, validateRoutingDecision } from "./contracts.mjs";
import {
  effectiveProposalCap,
  validateClassifierAssignment,
  validateDelegationPlanCapacity,
} from "./delegation-contracts.mjs";
import { explicitAgentRequest } from "./smart-classifier.mjs";

const ROLE_CONFIG_KEYS = Object.freeze({ repo_reader: "repoReader", repo_reviewer: "repoReviewer", test_runner: "testRunner", file_editor: "fileEditor", implementer: "implementer" });
const ROUTE_RANK = Object.freeze({ economy: 0, standard: 1, deep: 2 });
const REASON_MINIMUM_ROUTE = Object.freeze({ routine_bounded: "economy", normal_engineering: "standard", complex_engineering: "deep", safety_sensitive: "deep", ambiguous_diagnosis: "deep", parallelizable_work: "economy" });
const EFFORT_RANK = Object.freeze({ low: 0, medium: 1, high: 2, xhigh: 3, max: 4, ultra: 5 });

function explicitProposalIsCompatible(decision, recommendation, config) {
  if (decision.method !== "explicit-control") return true;
  if (!Array.isArray(recommendation.assignments)) return false;
  const profileRoute = config.routing.taskProfiles[recommendation.taskProfile]?.route;
  const reasonRoute = REASON_MINIMUM_ROUTE[recommendation.reason];
  if (recommendation.route !== decision.route || profileRoute === undefined || reasonRoute === undefined) return false;
  if (ROUTE_RANK[profileRoute] > ROUTE_RANK[decision.route] || ROUTE_RANK[reasonRoute] > ROUTE_RANK[decision.route]) return false;
  return recommendation.assignments.every((assignment) =>
    ROUTE_RANK[assignment.profileKey] <= ROUTE_RANK[decision.route] &&
    EFFORT_RANK[assignment.reasoningEffort] <= EFFORT_RANK[decision.reasoningEffort]
  );
}

/**
 * When the user explicitly asks for agents (e.g. "spawn sol agent", "with
 * subagents", "using 2 agents") and the smart classifier did not supply a
 * complete plan, authorize a single implementer assignment at the parent
 * route/effort. Independent multi-unit fan-out still requires a classifier
 * proposal; one child is better than hard-none.
 */
export function buildExplicitSingleAgentRecommendation(decision) {
  if (decision.execution !== "agent") {
    return null;
  }
  const requested = explicitAgentRequest(decision);
  if (requested === null || requested < 1) {
    return null;
  }
  const taskProfile =
    decision.route === "deep" ? "complex_implementation" : "implementation";
  const reason =
    decision.route === "deep" ? "complex_engineering" : "normal_engineering";
  const assignment = validateClassifierAssignment({
    assignmentId: "a1",
    role: "implementer",
    profileKey: decision.route,
    reasoningEffort: decision.reasoningEffort,
    taskProfile,
    promptTemplateKey: "implementer",
    ordinal: 1,
    objectiveKey: "implementation_slice",
    evidenceKey: "diff_and_verification",
  });
  return {
    route: decision.route,
    reason,
    confidence: "high",
    taskProfile,
    delegationMode: "classifier_proposed",
    assignments: [assignment],
  };
}

function recommendationHasAssignments(recommendation) {
  return (
    recommendation?.delegationMode === "classifier_proposed" &&
    Array.isArray(recommendation.assignments) &&
    recommendation.assignments.length > 0
  );
}

export function resolveAssignmentProfile(parentRoute, role, configValue) {
  const config = validateConfig(configValue);
  const profileKey = config.routing.dynamicAgents.profiles[ROLE_CONFIG_KEYS[role]];
  if (profileKey === undefined || !Object.hasOwn(config.routes, parentRoute)) throw new RangeError("parentRoute and role must be supported");
  const ranks = { economy: 0, standard: 1, deep: 2 };
  const selected = ranks[profileKey] <= ranks[parentRoute] ? profileKey : parentRoute;
  return { profileKey: selected, reasoningEffort: config.routes[selected].reasoningEffort, taskProfile: null };
}

export function buildDelegationPlan({
  decision: decisionValue,
  recommendation,
  config: configValue,
  allowUndersizedExplicitPlan = false,
}) {
  const config = validateConfig(configValue);
  const decision = validateRoutingDecision(decisionValue);
  if (decision.execution !== "agent" || !config.routing.dynamicAgents.enabled) {
    return { plan: null, delegationMode: "none", diagnosticReasonCodes: ["delegation_disabled"] };
  }
  if (recommendation?.delegationMode !== "classifier_proposed") {
    return { plan: null, delegationMode: "none", diagnosticReasonCodes: ["delegation_proposal_invalid"] };
  }
  if (decision.reasonCodes.includes("invalid_explicit_agent_count")) {
    return { plan: null, delegationMode: "none", diagnosticReasonCodes: ["delegation_count_unverified"] };
  }
  try {
    if (!explicitProposalIsCompatible(decision, recommendation, config)) {
      return { plan: null, delegationMode: "none", diagnosticReasonCodes: ["delegation_proposal_invalid"] };
    }
    const plan = validateDelegationPlan({
      schemaVersion: 2,
      source: "classifier",
      decisionId: decision.decisionId,
      parentRoute: decision.route,
      assignments: recommendation.assignments,
    });
    validateDelegationPlanCapacity({ decision, plan, routing: config.routing });
    const requested = explicitAgentRequest(decision);
    const expectedAssignments = requested === null
      ? null
      : Math.min(requested, effectiveProposalCap({ decision, routing: config.routing }));
    if (expectedAssignments !== null && plan.assignments.length !== expectedAssignments) {
      // Explicit multi-agent requests without a full classifier proposal may
      // still start with one implementer rather than hard-none.
      const allowPartial =
        allowUndersizedExplicitPlan &&
        plan.assignments.length === 1 &&
        expectedAssignments >= 1;
      if (!allowPartial) {
        return { plan: null, delegationMode: "none", diagnosticReasonCodes: ["delegation_count_unverified"] };
      }
    }
    return { plan, delegationMode: "classifier_proposed", diagnosticReasonCodes: [] };
  } catch {
    return { plan: null, delegationMode: "none", diagnosticReasonCodes: ["delegation_proposal_invalid"] };
  }
}

export function attachDelegationPlan(options) {
  const decision = validateRoutingDecision(options.decision);
  let recommendation = options.recommendation;
  let synthesizedExplicit = false;
  if (!recommendationHasAssignments(recommendation)) {
    const explicitRecommendation = buildExplicitSingleAgentRecommendation(decision);
    if (explicitRecommendation !== null) {
      recommendation = explicitRecommendation;
      synthesizedExplicit = true;
    }
  }
  const { plan, delegationMode, diagnosticReasonCodes } = buildDelegationPlan({
    ...options,
    decision,
    recommendation,
    allowUndersizedExplicitPlan: synthesizedExplicit,
  });
  const reasonCodes = [...decision.reasonCodes];
  for (const code of diagnosticReasonCodes) {
    if (reasonCodes.length < 12 && !reasonCodes.includes(code)) reasonCodes.push(code);
  }
  if (
    synthesizedExplicit &&
    plan !== null &&
    reasonCodes.length < 12 &&
    !reasonCodes.includes("explicit_single_agent_plan")
  ) {
    reasonCodes.push("explicit_single_agent_plan");
  }
  return validateRoutingDecision({
    ...decision,
    agentCount: decision.execution === "agent"
      ? (plan === null ? 1 : plan.assignments.length)
      : 0,
    delegationMode,
    delegationPlan: plan,
    reasonCodes,
  });
}
