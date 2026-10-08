import { createHash } from "node:crypto";

import { validateConfig } from "./config.mjs";
import { validateModelProfile } from "./model-catalog.mjs";
import { validateModelPinProfile } from "./model-pin-controls.mjs";
import {
  explicitTier,
  matchesModelControlRejection,
  matchesNoDelegation,
  matchesPassthrough,
  matchesRecurringFailure,
  matchesTrivialEdit,
  safetyFloorReasons,
  standardFloorReasons,
} from "./phrases.mjs";

const agentControlNegationBefore =
  /(?:^|[\s,;:]\s*)(?:do not|don['’]?t|never|stop(?:\s+to)?)\s+$/i;
import { matchPathTokens } from "./path-tokens.mjs";
import {
  deterministicTaskProfile,
  resolveTaskProfile,
} from "./task-profiles.mjs";

export const ROUTES = Object.freeze([
  "passthrough",
  "parent",
  "economy",
  "standard",
  "deep",
]);
export const ROUTE_RANK = Object.freeze({
  economy: 0,
  standard: 1,
  deep: 2,
});

const boundedVerbPattern =
  /\b(?:add|check|count|explain|find|fix|inspect|list|locate|read|remove|rename|run|show|test|update|verify)\b/i;
const boundedTargetPattern =
  /\b(?:one|single|this)\s+(?:command|doc(?:ument)?|file|function|test)\b/i;
const readOnlyPattern =
  /^(?:check|count|explain|find|inspect|list|locate|read|run|show|verify|what|where|which)\b/i;
const politePrefixPattern =
  /^(?:please|kindly|(?:could|can|would)\s+you(?:\s+please)?)\s+/i;
const complexEngineeringPattern =
  /\b(?:redesign|re-?architect|rewrite|refactor|architect(?:ure)?|implement(?:s|ed|ing|ations?)?|integrate|migrate|multi-module|multi-system)\b/i;
const broadScopePattern =
  /\b(?:across|end-to-end|multi-file|multiple files|multiple modules|multi-module|system-wide|full architecture)\b/i;
const architectureHeavyPattern =
  /\b(?:full architecture|redesign)\b[^.!?\n]{0,180}\b(?:backend|frontend|multi-module|multi-tenant|pipeline)\b/i;
/** Minimum attainable structural score (base with no bonuses). */
export const STRUCTURAL_SCORE_BASE = 20;
const readOnlyEconomyMaxWords = 20;
const readOnlyEconomyMaxPaths = 2;
const retryEscalationPattern =
  /\b(?:previous|prior|earlier) (?:model|agent|attempt)\b[^.!?\n]{0,120}\b(?:could not|couldn't|did not|failed to|was unable to)\b[^.!?\n]{0,80}\b(?:solve|fix|resolve|diagnose)\b/i;
const userRequestedDeepAnalysisPattern =
  /(?:\bdeep(?:-| )dive\b|\bin(?:-| )?dea?pth\s+(?:analysis|review|audit|investigation|assessment)\b|\b(?:analy[sz]e|review|audit|investigate|assess)\b[^.!?\n]{0,120}\bin(?:-| )?dea?pth\b)/i;
const userRequestedMoreReasoningPattern =
  /\b(?:(?:use|with|apply) more reasoning|think (?:harder|more deeply)|maximum reasoning|more thorough|thoroughly|be exhaustive|go deeper)\b/i;
// Numbered: "spawn 2 agents", "use one high-effort agents", "using 2 agents",
// "with 3 sub-agents".
const explicitAgentCountPattern =
  /\b(?:delegate to|launch|run|spawn|use|using|with)\s+(one|two|three|four|\d+)\s+(?:(?:low|medium|high|xhigh|ultra)(?:-|\s+)effort\s+)?(?:(?:luna|terra|sol)\s+)?(?:sub[- ]?)?agents?\b/gi;
// Singular uncounted: "spawn sol agent", "launch an agent", "spawn a sol agent".
// Require an article and/or model name before singular "agent" so descriptive
// phrases like "spawn agent dynamically" do not invent a count.
const singularAgentRequestPattern =
  /\b(?:delegate to|launch|spawn)\s+(?:(?:a|an|one)\s+(?:(?:low|medium|high|xhigh|ultra)(?:-|\s+)effort\s+)?(?:(?:luna|terra|sol)\s+)?|(?:(?:low|medium|high|xhigh|ultra)(?:-|\s+)effort\s+)?(?:luna|terra|sol)\s+)agent\b/gi;
// Affirmative uncounted agent request: "with subagents", "using agents",
// "spawn subagents", "use subagents". Counts as one so synthesis can authorize
// spawn_agent; multi-unit work still needs a classifier proposal.
const uncountedAgentRequestPattern =
  /\b(?:(?:with|using|via|through)\s+(?:the\s+)?(?:sub[- ]?)?agents?\b|(?:spawn|launch|use)\s+(?:the\s+)?(?:sub[- ]?)?agents\b)/gi;
export const ROUTE_PARALLEL_CAPS = Object.freeze({
  economy: 4,
  standard: 3,
  deep: 2,
});
const countWords = Object.freeze({
  one: 1,
  two: 2,
  three: 3,
  four: 4,
});

function routeProfile(
  route,
  config,
  modelOverride = null,
  reasoningEffortOverride = null,
) {
  if (route === "economy" || route === "standard" || route === "deep") {
    return {
      execution: "agent",
      ...validateModelProfile({
        model: modelOverride ?? config.routes[route].model,
        reasoningEffort:
          reasoningEffortOverride ?? config.routes[route].reasoningEffort,
      }),
    };
  }
  if (route === "parent") {
    return {
      execution: "parent",
      model: null,
      reasoningEffort: null,
    };
  }
  return {
    execution: "none",
    model: null,
    reasoningEffort: null,
  };
}

function stripLeadingPoliteness(prompt) {
  return prompt.replace(politePrefixPattern, "");
}

function wordCount(prompt) {
  return prompt.trim().split(/\s+/).filter(Boolean).length;
}

function structuralScore(prompt) {
  const words = wordCount(prompt);
  let score = STRUCTURAL_SCORE_BASE + Math.min(12, Math.floor(words / 8) * 2);
  if (broadScopePattern.test(prompt)) {
    score += 25;
  }
  if (complexEngineeringPattern.test(prompt)) {
    score += 15;
  }
  if (architectureHeavyPattern.test(prompt)) {
    score += 40;
  }
  if (/\b(?:controller|service|persistence|database|frontend|backend|API)\b/i.test(prompt)) {
    score += 5;
  }
  const paths = matchPathTokens(prompt);
  score += Math.min(15, paths.length * 5);
  return score;
}

export function promptStats(prompt) {
  return {
    wordCount: wordCount(prompt),
    byteLength: Buffer.byteLength(prompt),
    pathCount: matchPathTokens(prompt).length,
    structuralScore: structuralScore(prompt),
  };
}

function isBoundedEconomy(prompt) {
  if (matchesTrivialEdit(prompt)) {
    return true;
  }
  if (broadScopePattern.test(prompt)) {
    return false;
  }
  const working = stripLeadingPoliteness(prompt);
  if (complexEngineeringPattern.test(working)) {
    return false;
  }
  const paths = matchPathTokens(working);
  const words = wordCount(working);
  if (readOnlyPattern.test(working)) {
    // Multi-file independent reads stay economy up to the economy sibling cap
    // (4). Complex redesign/architecture explains are excluded above.
    const maxPaths =
      paths.length > 1
        ? ROUTE_PARALLEL_CAPS.economy
        : readOnlyEconomyMaxPaths;
    return words <= readOnlyEconomyMaxWords && paths.length <= maxPaths;
  }
  if (boundedTargetPattern.test(working) && boundedVerbPattern.test(working)) {
    return true;
  }
  return (
    paths.length > 0 &&
    paths.length <= 2 &&
    boundedVerbPattern.test(working)
  );
}

function parseCount(rawValue) {
  return countWords[rawValue.toLowerCase()] ?? Number(rawValue);
}

function requestedAgentCount(prompt) {
  const counts = new Set(
    [...prompt.matchAll(explicitAgentCountPattern)].map((match) =>
      parseCount(match[1]),
    ),
  );
  if (counts.size > 1) {
    return {
      kind: "conflict",
      count: null,
      reasonCode: "conflicting_explicit_agent_counts",
    };
  }
  if (counts.size === 1) {
    const count = [...counts][0];
    if (!Number.isInteger(count) || count < 1) {
      return {
        kind: "invalid",
        count: null,
        reasonCode: "invalid_explicit_agent_count",
      };
    }
    return {
      kind: "valid",
      count,
      reasonCode: `explicit_agent_count_${count}`,
    };
  }
  // No numbered count: treat affirmative agent/subagent requests as one agent,
  // but ignore spans preceded by do-not / never / stop.
  for (const pattern of [
    singularAgentRequestPattern,
    uncountedAgentRequestPattern,
  ]) {
    for (const match of prompt.matchAll(pattern)) {
      if (agentControlNegationBefore.test(prompt.slice(0, match.index))) {
        continue;
      }
      return {
        kind: "valid",
        count: 1,
        reasonCode: "explicit_agent_count_1",
      };
    }
  }
  return {
    kind: "none",
    count: null,
    reasonCode: null,
  };
}

function decisionId(sessionId, observedTurnId, nowMs) {
  const digest = createHash("sha256")
    .update(`${sessionId}\0${observedTurnId ?? ""}\0${nowMs}`)
    .digest("hex")
    .slice(0, 24);
  return `tx_${digest}`;
}

function buildDecision({
  config,
  context,
  route,
  method,
  reasonCodes,
  explicit,
  prompt,
  explicitAgentCount = null,
  explicitAgentReasonCode = null,
  modelOverride = null,
  reasoningEffortOverride = null,
}) {
  const taskProfile =
    modelOverride === null && reasoningEffortOverride === null &&
    route !== "parent" && route !== "passthrough"
      ? deterministicTaskProfile(prompt, method, reasonCodes)
      : null;
  const taskSelection = taskProfile === null
    ? null
    : resolveTaskProfile(config, taskProfile, route);
  const profile = routeProfile(
    route,
    config,
    modelOverride ?? taskSelection?.model,
    reasoningEffortOverride ?? taskSelection?.reasoningEffort,
  );
  const requestedReasonCode = explicitAgentCount === null
    ? null
    : explicitAgentReasonCode ?? `explicit_agent_count_${explicitAgentCount}`;
  return {
    schemaVersion: 2,
    decisionId: decisionId(
      context.sessionId,
      context.observedTurnId,
      context.nowMs,
    ),
    sessionId: context.sessionId,
    observedTurnId: context.observedTurnId,
    provider: "codex",
    route,
    execution: profile.execution,
    agentCount: profile.execution === "agent" ? 1 : 0,
    model: profile.model,
    reasoningEffort: profile.reasoningEffort,
    method,
    reasonCodes: [
      ...reasonCodes,
      ...(taskProfile === null ? [] : [`task_profile_${taskProfile}`]),
      ...(requestedReasonCode ? [requestedReasonCode] : []),
    ],
    explicit,
    createdAtMs: context.nowMs,
    expiresAtMs: context.nowMs + config.routing.decisionMaxAgeMs,
    delegationPlan: null,
    delegationMode: "none",
  };
}

const modelPinDiagnosticReasons = new Set([
  "session_model_pin_conflict_ignored",
  "session_model_pin_request_incomplete",
  "session_model_pin_request_ambiguous",
  "session_model_pin_request_conflicting_controls",
  "session_model_pin_request_unavailable",
]);

export function buildPinnedDecision(
  configValue,
  contextValue,
  profileValue,
  { diagnosticReasonCode = null } = {},
) {
  if (
    diagnosticReasonCode !== null &&
    !modelPinDiagnosticReasons.has(diagnosticReasonCode)
  ) {
    throw new RangeError("model pin diagnostic reason is unsupported");
  }
  const config = validateConfig(configValue);
  const context = validateContext(contextValue);
  const profile = validateModelPinProfile(profileValue);
  return buildDecision({
    config,
    context,
    route: profile.route,
    method: "session-pin",
    reasonCodes: [
      "session_model_pin",
      ...(diagnosticReasonCode === null ? [] : [diagnosticReasonCode]),
    ],
    explicit: true,
    prompt: "",
    modelOverride: profile.model,
    reasoningEffortOverride: profile.reasoningEffort,
  });
}

export function buildParentDecision(
  configValue,
  contextValue,
  {
    method = "routing-unavailable",
    reasonCode = "routing_unavailable",
    prompt = "",
    explicit = false,
  } = {},
) {
  const config = validateConfig(configValue);
  const context = validateContext(contextValue);
  return buildDecision({
    config,
    context,
    route: "parent",
    method,
    reasonCodes: [reasonCode],
    explicit,
    prompt,
  });
}

function validateContext(context) {
  if (
    context === null ||
    typeof context !== "object" ||
    Array.isArray(context)
  ) {
    throw new TypeError("classifier context must be an object");
  }
  if (
    typeof context.sessionId !== "string" ||
    context.sessionId.trim().length === 0
  ) {
    throw new TypeError("sessionId must be a non-empty string");
  }
  if (
    context.turnId !== undefined &&
    context.turnId !== null &&
    (typeof context.turnId !== "string" || context.turnId.length === 0)
  ) {
    throw new TypeError("turnId must be a non-empty string or null");
  }
  const nowMs = context.nowMs ?? Date.now();
  if (!Number.isSafeInteger(nowMs) || nowMs < 0) {
    throw new TypeError("nowMs must be a non-negative safe integer");
  }
  return {
    sessionId: context.sessionId,
    observedTurnId: context.turnId ?? null,
    nowMs,
  };
}

function classifyPromptWithoutSessionFloor(
  prompt,
  configValue,
  contextValue = {},
) {
  if (typeof prompt !== "string") {
    throw new TypeError("prompt must be a string");
  }
  const normalized = prompt.trim();
  if (normalized.length === 0) {
    throw new TypeError("prompt must not be empty");
  }

  const config = validateConfig(configValue);
  const context = validateContext(contextValue);
  const explicitCount = requestedAgentCount(normalized);
  if (
    explicitCount.kind === "conflict" ||
    explicitCount.kind === "invalid"
  ) {
    return buildParentDecision(config, context, {
      method: "explicit-control",
      reasonCode: explicitCount.reasonCode,
      prompt: normalized,
      explicit: true,
    });
  }

  const noDelegation = matchesNoDelegation(normalized);
  if (noDelegation) {
    return buildParentDecision(config, context, {
      method: "explicit-control",
      reasonCode:
        explicitCount.kind === "none"
          ? "explicit_parent"
          : "conflicting_delegation_controls",
      prompt: normalized,
      explicit: true,
    });
  }

  const floorReasons = safetyFloorReasons(normalized);
  const explicit = explicitTier(normalized, config);
  if (explicit) {
    const reasonCodes = [`explicit_${explicit.route}`];
    if (explicit.conflictResolved) {
      reasonCodes.push("explicit_tier_conflict_resolved");
    }
    if (floorReasons.length > 0) {
      reasonCodes.push("safety_floor_overridden");
    }
    return buildDecision({
      config,
      context,
      route: explicit.route,
      method: "explicit-control",
      reasonCodes,
      explicit: true,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
      modelOverride: explicit.modelOverride,
      reasoningEffortOverride: explicit.reasoningEffortOverride,
    });
  }

  if (matchesPassthrough(normalized)) {
    return buildDecision({
      config,
      context,
      route: "passthrough",
      method: "passthrough",
      reasonCodes: ["conversation_only"],
      explicit: false,
      prompt: normalized,
    });
  }

  // "stop use sol" / "do not use the deep tier" with no alternative must not
  // re-score as economy/luna and inject a cheaper parent profile.
  if (matchesModelControlRejection(normalized)) {
    return buildDecision({
      config,
      context,
      route: "passthrough",
      method: "passthrough",
      reasonCodes: ["model_control_rejection"],
      explicit: false,
      prompt: normalized,
    });
  }

  if (retryEscalationPattern.test(normalized)) {
    return buildDecision({
      config,
      context,
      route: "deep",
      method: "retry-escalation",
      reasonCodes: ["prior_model_failure"],
      explicit: false,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
    });
  }

  if (floorReasons.length > 0) {
    const userEscalated = userRequestedMoreReasoningPattern.test(normalized);
    return buildDecision({
      config,
      context,
      route: "deep",
      method: userEscalated
        ? "user-effort-escalation"
        : "safety-floor",
      reasonCodes: userEscalated
        ? [...floorReasons, "user_requested_more_reasoning"]
        : floorReasons,
      explicit: false,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
      reasoningEffortOverride: userEscalated
        ? config.routing.escalationReasoningEffort
        : null,
    });
  }

  if (userRequestedDeepAnalysisPattern.test(normalized)) {
    const userEscalated = userRequestedMoreReasoningPattern.test(normalized);
    return buildDecision({
      config,
      context,
      route: "deep",
      method: userEscalated
        ? "user-effort-escalation"
        : "user-depth-request",
      reasonCodes: userEscalated
        ? ["user_requested_depth", "user_requested_more_reasoning"]
        : ["user_requested_depth"],
      explicit: false,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
      reasoningEffortOverride: userEscalated
        ? config.routing.escalationReasoningEffort
        : null,
    });
  }

  if (matchesRecurringFailure(normalized)) {
    return buildDecision({
      config,
      context,
      route: "deep",
      method: "recurring-failure",
      reasonCodes: ["recurring_failure"],
      explicit: false,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
    });
  }

  const standardReasons = standardFloorReasons(normalized);
  if (standardReasons.length > 0) {
    return buildDecision({
      config,
      context,
      route: "standard",
      method: "standard-floor",
      reasonCodes: standardReasons,
      explicit: false,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
    });
  }

  if (isBoundedEconomy(normalized)) {
    return buildDecision({
      config,
      context,
      route: "economy",
      method: "bounded-economy",
      reasonCodes: ["bounded_scope"],
      explicit: false,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
    });
  }

  const score = structuralScore(normalized);
  const route =
    score <= config.routing.structuralScoreEconomyMax
      ? "economy"
      : score <= config.routing.structuralScoreStandardMax
        ? "standard"
        : "deep";
  const moreReasoning = userRequestedMoreReasoningPattern.test(normalized);

  // A request to think harder is an explicit effort signal and must not fall
  // through to the cheapest profile. An already-complex task that asks for more
  // keeps the ultra escalation below; a bare request carries no complexity
  // signal of its own, so it is promoted to deep at the normal profile. Bounded
  // scope is checked earlier, which keeps "thoroughly update the changelog"
  // routine.
  if (moreReasoning && route !== "deep") {
    return buildDecision({
      config,
      context,
      route: "deep",
      method: "user-reasoning-request",
      reasonCodes: ["user_requested_more_reasoning"],
      explicit: false,
      prompt: normalized,
      explicitAgentCount: explicitCount.count,
      explicitAgentReasonCode: explicitCount.reasonCode,
    });
  }

  const userEscalated = route === "deep" && moreReasoning;
  return buildDecision({
    config,
    context,
    route,
    method: userEscalated
      ? "user-effort-escalation"
      : "structural-score",
    reasonCodes: userEscalated
      ? [`structural_${route}`, "user_requested_more_reasoning"]
      : [`structural_${route}`],
    explicit: false,
    prompt: normalized,
    explicitAgentCount: explicitCount.count,
    explicitAgentReasonCode: explicitCount.reasonCode,
    reasoningEffortOverride: userEscalated
      ? config.routing.escalationReasoningEffort
      : null,
  });
}

function sessionFloorReasonCodes(reasonCodes, agentCount) {
  let explicitAgentCount = null;
  let hadParallelCount = false;
  const retained = [];
  for (const reasonCode of reasonCodes) {
    const explicitMatch = reasonCode.match(
      /^explicit_agent_count_(?:clamped_)?(\d+)(?:_to_\d+)?$/,
    );
    if (explicitMatch) {
      explicitAgentCount = Number(explicitMatch[1]);
      continue;
    }
    if (/^parallel_agent_count_\d+$/.test(reasonCode)) {
      hadParallelCount = true;
      continue;
    }
    retained.push(reasonCode);
  }
  if (explicitAgentCount !== null) {
    retained.push(
      agentCount === explicitAgentCount
        ? `explicit_agent_count_${explicitAgentCount}`
        : `explicit_agent_count_clamped_${explicitAgentCount}_to_${agentCount}`,
    );
  } else if (hadParallelCount && agentCount > 1) {
    retained.push(`parallel_agent_count_${agentCount}`);
  }
  retained.push("session_retry_floor");
  return retained;
}

export function classifyPrompt(
  prompt,
  configValue,
  contextValue = {},
  { sessionFloorRoute = null } = {},
) {
  const decision = classifyPromptWithoutSessionFloor(
    prompt,
    configValue,
    contextValue,
  );
  if (
    sessionFloorRoute === null ||
    decision.explicit ||
    decision.execution !== "agent" ||
    ROUTE_RANK[decision.route] >= ROUTE_RANK[sessionFloorRoute]
  ) {
    return decision;
  }
  const config = validateConfig(configValue);
  const agentCount = Math.min(
    decision.agentCount,
    ROUTE_PARALLEL_CAPS[sessionFloorRoute],
  );
  return {
    ...decision,
    route: sessionFloorRoute,
    agentCount,
    model: config.routes[sessionFloorRoute].model,
    reasoningEffort: config.routes[sessionFloorRoute].reasoningEffort,
    reasonCodes: sessionFloorReasonCodes(decision.reasonCodes, agentCount),
  };
}
