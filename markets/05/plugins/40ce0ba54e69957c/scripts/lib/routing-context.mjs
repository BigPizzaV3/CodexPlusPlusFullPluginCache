import { validateRoutingDecision } from "./contracts.mjs";
import { assignmentTaskName } from "./assignment-tokens.mjs";

export function buildRoutingContext(decisionValue) {
  const decision = validateRoutingDecision(decisionValue);
  if (decision.route === "passthrough") {
    return null;
  }

  if (decision.route === "parent") {
    if (decision.reasonCodes.includes("session_model_pin_incomplete")) {
      return "TokenX: parent only; model pin unchanged; specify one supported model and effort or clear the model pin; no automatic routing; do not call spawn_agent.";
    }
    if (decision.reasonCodes.includes("session_model_pin_ambiguous")) {
      return "TokenX: parent only; multiple model/effort pairs are ambiguous; model pin unchanged; no automatic routing; do not call spawn_agent.";
    }
    if (
      decision.reasonCodes.includes("session_model_pin_conflicting_controls")
    ) {
      return "TokenX: parent only; do not clear and replace a model pin in the same control; pin unchanged; no automatic routing; do not call spawn_agent.";
    }
    if (decision.reasonCodes.includes("session_model_pin_unavailable")) {
      return "TokenX: parent only; requested or stored model pin is unavailable and was not substituted; clear or replace it; no automatic routing; do not call spawn_agent.";
    }
    if (decision.reasonCodes.includes("session_model_pin_corrupt")) {
      return "TokenX: parent only; stored model pin is invalid; clear or replace it; no automatic routing; do not call spawn_agent.";
    }
    if (
      decision.reasonCodes.includes("session_model_pin_catalog_unavailable")
    ) {
      return "TokenX: parent only; model catalog could not be verified; pin retained; no automatic routing; do not call spawn_agent.";
    }
    if (decision.reasonCodes.includes("model_catalog_unavailable")) {
      return "TokenX: parent only; configured Codex routing is unavailable; run tokenx doctor.";
    }
    if (decision.reasonCodes.includes("configuration_unavailable")) {
      return "TokenX: parent only; stored configuration is incompatible; run tokenx update.";
    }
    return "TokenX: parent only; do not delegate; be concise.";
  }

  if (decision.method === "session-pin") {
    let context =
      `TokenX: pinned ${decision.model}/${decision.reasoningEffort} for this thread; ` +
      "use only this profile; do not adjust or switch model or effort; " +
      "no delegation is authorized; do not call spawn_agent.";
    if (decision.reasonCodes.includes("session_model_pin_conflict_ignored")) {
      context +=
        " Conflicting one-turn model control ignored; replace or clear the pin explicitly.";
    } else if (
      decision.reasonCodes.includes("session_model_pin_request_incomplete")
    ) {
      context += " Incomplete replacement ignored; current pin retained.";
    } else if (
      decision.reasonCodes.includes("session_model_pin_request_ambiguous")
    ) {
      context += " Ambiguous replacement ignored; current pin retained.";
    } else if (
      decision.reasonCodes.includes(
        "session_model_pin_request_conflicting_controls",
      )
    ) {
      context +=
        " Conflicting clear/replace control ignored; current pin retained.";
    } else if (
      decision.reasonCodes.includes("session_model_pin_request_unavailable")
    ) {
      context +=
        " Unavailable replacement was not substituted; current pin retained.";
    }
    return context;
  }

  let context = `TokenX: ${decision.route} parent ${decision.model}/${decision.reasoningEffort};`;
  if (decision.delegationPlan !== null) {
    const assignments = decision.delegationPlan.assignments
      .map((assignment) =>
        `task_name=${assignmentTaskName(assignment, decision.decisionId)}`,
      )
      .join(" ");
    return (
      `${context} ` +
      `${assignments}; this turn only; new assignment per turn; no reuse; ` +
      "use task_name; omit agent_type/model/effort; see route-agents skill to render."
    );
  }

  if (decision.delegationMode === "none") {
    context += " no delegation is authorized this turn; do not call spawn_agent.";
  } else {
    throw new RangeError("routing decision delegation mode is unsupported");
  }

  if (decision.reasonCodes.includes("safety_floor_overridden")) {
    context += " Explicit profile overrides the automatic safety floor.";
  }
  if (decision.reasonCodes.includes("explicit_tier_conflict_resolved")) {
    context += ` Multiple explicit tiers; using ${decision.route}.`;
  }
  if (decision.method === "smart-fallback") {
    context +=
      " Smart classifier unavailable; deterministic fallback applied.";
  }
  return context;
}
