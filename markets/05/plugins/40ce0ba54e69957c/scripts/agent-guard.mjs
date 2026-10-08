import { loadConfig } from "./lib/config.mjs";
import {
  allowToolInputResult,
  denyToolResult,
} from "./lib/hook-io.mjs";
import { runHook } from "./lib/hook-runtime.mjs";
import { validateLiveConfiguredModels } from "./lib/model-catalog.mjs";
import { getProvider } from "./lib/providers/registry.mjs";
import { assignmentIdFromToolInput } from "./lib/providers/codex.mjs";
import {
  claimAgentCall,
  readDecision,
  recordOutcome,
} from "./lib/state.mjs";

const agentToolNames = new Set(["spawn_agent", "Agent"]);
let outcomeTrackingFailureReported = false;

function denial(reason) {
  const prefix = "TokenX denied this Agent call: ";
  const detail = String(reason).replaceAll(/\s+/g, " ").trim();
  let message = `${prefix}${detail}`;
  while (Buffer.byteLength(message, "utf8") > 500) {
    message = message.slice(0, -1);
  }
  return denyToolResult(message);
}

async function withOutcomeTracking(operation) {
  try {
    return await operation();
  } catch {
    if (!outcomeTrackingFailureReported) {
      process.stderr.write("TokenX: outcome tracking failed\n");
      outcomeTrackingFailureReported = true;
    }
    return null;
  }
}

await runHook(
  "PreToolUse",
  async ({ input, pluginData, env }) => {
    try {
      if (!agentToolNames.has(input.tool_name)) {
        return denial(`unexpected tool ${input.tool_name}`);
      }

      const config = await loadConfig({ pluginData, env });
      await validateLiveConfiguredModels(config, {
        homeDir: env.HOME,
      });
      const decision = await readDecision({
        pluginData,
        sessionId: input.session_id,
        nowMs: Date.now(),
      });
      if (!decision) {
        return denial("matching routing decision is missing");
      }
      if (decision.observedTurnId !== input.turn_id) {
        return denial("turn_changed");
      }

      const provider = getProvider(config.provider);
      const assignmentId = assignmentIdFromToolInput(input.tool_input);
      const policy = provider.buildAgentPolicy(
        decision,
        { ...config.routing, routes: config.routes },
      );
      const preliminary = provider.guardAgentCall(
        input.tool_input,
        policy,
        {
          isNested: false,
          depthObservable: false,
          claimed: true,
        },
      );
      if (preliminary.decision === "deny") {
        if (preliminary.reasonCode === "assignment_task_sensitive") {
          await withOutcomeTracking(() =>
            recordOutcome({
              pluginData,
              sessionId: input.session_id,
              kind: "assignmentDenial",
              maxAgeMs: config.routing.decisionMaxAgeMs,
            })
          );
        }
        return denial(preliminary.reasonCode);
      }

      const claim = await claimAgentCall({
        pluginData,
        sessionId: input.session_id,
        expectedDecisionId: decision.decisionId,
        expectedTurnId: input.turn_id,
        nowMs: Date.now(),
        maxCalls: policy.maxCalls,
        assignmentId,
        isNested: false,
        denyNested: policy.denyNested,
      });
      if (!claim.claimed) {
        return denial(claim.reasonCode);
      }
      if (claim.decision.decisionId !== decision.decisionId) {
        return denial("routing decision changed before the Agent call");
      }

      const result = allowToolInputResult(preliminary.updatedInput);
      if (preliminary.residualWarningCode) {
        result.systemMessage =
          "TokenX applied the selected profile. Subagent depth is not exposed " +
          `by the current hook contract; the atomic ${policy.maxCalls}-call ` +
          "sibling budget is enforced.";
      }
      return result;
    } catch (error) {
      const detail =
        error instanceof Error && error.message
          ? error.message
          : "policy verification failed";
      return denial(`could not verify policy: ${detail}`);
    }
  },
  {
    onError(error) {
      const detail =
        error instanceof Error && error.message
          ? error.message
          : "hook protocol verification failed";
      return denial(`could not verify hook protocol: ${detail}`);
    },
  },
);
