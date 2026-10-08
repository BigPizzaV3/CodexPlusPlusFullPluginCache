export const TASK_PROFILE_KEYS = Object.freeze([
  "read",
  "file_edit",
  "implementation",
  "complex_implementation",
  "analysis",
  "architecture",
  "retry",
]);

export const ROLE_TASK_PROFILES = Object.freeze({
  repo_reader: "read",
  repo_reviewer: "analysis",
  test_runner: "read",
  file_editor: "file_edit",
  implementer: "implementation",
});

const readPattern = /^(?:check|count|explain|find|inspect|list|locate|read|show|verify|what|where|which)\b/i;
const fileEditPattern = /\b(?:add|change|edit|fix|rename|update|write)\b[\s\S]{0,100}\b(?:file|doc(?:ument)?|config|\.\w{1,8})\b/i;
const architecturePattern =
  /\barchitect(?:ure|ing)?\b|\bdesign\b[^.!?\n]{0,100}\b(?:api|integration|pipeline|platform|service|system|workflow)\b/i;
const analysisPattern =
  /\b(?:analy[sz]e|debug|diagnose|investigate|root cause|figure out why)\b/i;
const implementationActionPattern =
  /\b(?:build|implement(?:s|ed|ing|ations?)?|integrate|wire(?: up)?)\b|\b(?:add|create|write)\b[^.!?\n]{0,100}\b(?:capability|endpoint|feature|flow|support|tests?)\b/i;
const broadImplementationPattern =
  /\b(?:across|end-to-end|multi-file|multiple files|multiple modules|multi-module|system-wide)\b/i;
const refactorPattern = /\b(?:refactor|redesign|re-?architect|rewrite)\b/i;
const fixedEffortMethods = new Set([
  "safety-floor",
  "user-depth-request",
  "user-effort-escalation",
]);

export function resolveTaskProfile(config, taskProfile, selectedRoute = "economy") {
  if (!TASK_PROFILE_KEYS.includes(taskProfile)) {
    throw new RangeError(`unsupported task profile: ${String(taskProfile)}`);
  }
  if (!(selectedRoute in config.routes)) {
    throw new RangeError(`unsupported selected route: ${String(selectedRoute)}`);
  }
  const configured = config.routing.taskProfiles[taskProfile];
  return {
    profileKey: selectedRoute,
    model: config.routes[selectedRoute].model,
    reasoningEffort: selectedRoute === configured.route
      ? configured.reasoningEffort
      : config.routes[selectedRoute].reasoningEffort,
  };
}

export function deterministicTaskProfile(prompt, method, reasonCodes = []) {
  if (method === "retry-escalation" || reasonCodes.includes("recurring_failure")) {
    return "retry";
  }
  if (fixedEffortMethods.has(method)) {
    return null;
  }
  if (architecturePattern.test(prompt)) {
    return "architecture";
  }
  if (analysisPattern.test(prompt)) {
    return "analysis";
  }
  if (
    (broadImplementationPattern.test(prompt) &&
      (implementationActionPattern.test(prompt) || refactorPattern.test(prompt)))
  ) {
    return "complex_implementation";
  }
  if (implementationActionPattern.test(prompt)) {
    return "implementation";
  }
  if (fileEditPattern.test(prompt)) {
    return "file_edit";
  }
  if (readPattern.test(prompt)) {
    return "read";
  }
  return null;
}
