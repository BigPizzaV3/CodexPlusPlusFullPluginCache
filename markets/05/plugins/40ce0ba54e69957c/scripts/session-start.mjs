import {
  isStoredConfigError,
  loadConfig,
} from "./lib/config.mjs";
import { additionalContextResult } from "./lib/hook-io.mjs";
import { runHook } from "./lib/hook-runtime.mjs";
import {
  BUNDLED_MODEL_CATALOG,
  validateLiveConfiguredModels,
} from "./lib/model-catalog.mjs";
import { removeSessionState } from "./lib/state.mjs";

await runHook("SessionStart", async ({ input, pluginData, env }) => {
  try {
    if (input.source !== "compact") {
      await removeSessionState({
        pluginData,
        sessionId: input.session_id,
        includeModelPin:
          input.source === "startup" || input.source === "clear",
      });
    }
    let config;
    try {
      config = await loadConfig({ pluginData, env });
    } catch (error) {
      if (!isStoredConfigError(error)) {
        throw error;
      }
      await removeSessionState({
        pluginData,
        sessionId: input.session_id,
      });
      return additionalContextResult(
        "SessionStart",
        "TokenX: parent only; stored configuration is incompatible; run tokenx update.",
      );
    }
    let catalog;
    try {
      catalog = await validateLiveConfiguredModels(config, {
        homeDir: env.HOME,
      });
    } catch {
      return additionalContextResult(
        "SessionStart",
        "TokenX routing unavailable: configured Codex models could not be verified; parent stays in control.",
      );
    }
    if (catalog === BUNDLED_MODEL_CATALOG) {
      return additionalContextResult(
        "SessionStart",
        "TokenX: using bundled model catalog because the live Codex catalog is unavailable; run tokenx doctor.",
      );
    }
    return null;
  } catch (error) {
    await removeSessionState({
      pluginData,
      sessionId: input.session_id,
    });
    throw error;
  }
});
