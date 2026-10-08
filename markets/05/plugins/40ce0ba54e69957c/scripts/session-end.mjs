import { runHook } from "./lib/hook-runtime.mjs";
import { removeSessionState } from "./lib/state.mjs";

await runHook("SessionEnd", async ({ input, pluginData }) => {
  await removeSessionState({
    pluginData,
    sessionId: input.session_id,
    includeOutcomes: true,
    includeModelPin: false,
  });
  return null;
});
