import {
  buildParentDecision,
  buildPinnedDecision,
} from "./lib/classify.mjs";
import {
  DEFAULT_CONFIG,
  isStoredConfigError,
  loadConfig,
} from "./lib/config.mjs";
import { additionalContextResult } from "./lib/hook-io.mjs";
import { runHook } from "./lib/hook-runtime.mjs";
import {
  BUNDLED_MODEL_CATALOG,
  readCodexModelCatalog,
  validateConfiguredModels,
} from "./lib/model-catalog.mjs";
import {
  oneTurnProfileConflicts,
  parseModelPinControl,
  validateModelPinProfile,
} from "./lib/model-pin-controls.mjs";
import { buildRoutingContext } from "./lib/routing-context.mjs";
import { attachDelegationPlan } from "./lib/delegation-plan.mjs";
import { buildSignalsDigest } from "./lib/signals-digest.mjs";
import { classifyPromptWithSmartResult } from "./lib/smart-classifier.mjs";
import {
  isStoredModelPinError,
  readOrResetOutcomesForPrompt,
  readModelPin,
  recordOutcome,
  removeModelPin,
  removeSessionState,
  writeModelPin,
  writeDecision,
} from "./lib/state.mjs";

let outcomeTrackingFailureReported = false;

const retainedRequestReason = Object.freeze({
  session_model_pin_incomplete: "session_model_pin_request_incomplete",
  session_model_pin_ambiguous: "session_model_pin_request_ambiguous",
  session_model_pin_conflicting_controls:
    "session_model_pin_request_conflicting_controls",
});

async function readStoredPinStatus({ pluginData, sessionId }) {
  let profile;
  try {
    profile = await readModelPin({ pluginData, sessionId });
  } catch (error) {
    if (!isStoredModelPinError(error)) {
      throw error;
    }
    return { kind: "corrupt", profile: null };
  }
  return profile === null
    ? { kind: "none", profile: null }
    : { kind: "active", profile };
}

function validateStoredPinStatus(status, catalog) {
  if (status.kind !== "active") {
    return status;
  }
  try {
    return {
      kind: "active",
      profile: validateModelPinProfile(status.profile, catalog),
    };
  } catch (error) {
    if (!(error instanceof RangeError)) {
      throw error;
    }
    return { kind: "unavailable", profile: null };
  }
}

function pinErrorDecision(config, context, reasonCode) {
  return buildParentDecision(config, context, {
    method: "session-pin-error",
    reasonCode,
    explicit: true,
  });
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
  "UserPromptSubmit",
  async ({ input, pluginData, env }) => {
    let ownedDecisionId = null;
    try {
      const context = {
        sessionId: input.session_id,
        turnId: input.turn_id,
        nowMs: Date.now(),
      };
      const pendingDecision = buildParentDecision(DEFAULT_CONFIG, context, {
        reasonCode: "classification_pending",
      });
      await writeDecision({ pluginData, decision: pendingDecision });
      ownedDecisionId = pendingDecision.decisionId;
      const replaceOwnedDecision = async (nextDecision) => {
        await writeDecision({
          pluginData,
          decision: nextDecision,
          expectedDecisionId: ownedDecisionId,
        });
        ownedDecisionId = nextDecision.decisionId;
      };
      let config;
      try {
        config = await loadConfig({ pluginData, env });
      } catch (error) {
        if (!isStoredConfigError(error)) {
          throw error;
        }
        const decision = buildParentDecision(DEFAULT_CONFIG, context, {
          reasonCode: "configuration_unavailable",
        });
        await replaceOwnedDecision(decision);
        return additionalContextResult(
          "UserPromptSubmit",
          buildRoutingContext(decision),
        );
      }
      let decision;
      const control = parseModelPinControl(input.prompt);
      if (control.kind === "clear") {
        await removeModelPin({
          pluginData,
          sessionId: input.session_id,
        });
      }

      let catalog = null;
      let catalogReadFailed = false;
      try {
        catalog = (await readCodexModelCatalog({
          homeDir: env.HOME,
        })) ?? BUNDLED_MODEL_CATALOG;
      } catch {
        catalogReadFailed = true;
      }

      let activePin = null;
      let pinDiagnosticReasonCode = null;
      if (control.kind === "set") {
        if (catalogReadFailed) {
          const prior = await readStoredPinStatus({
            pluginData,
            sessionId: input.session_id,
          });
          if (prior.kind === "corrupt") {
            decision = pinErrorDecision(
              config,
              context,
              "session_model_pin_corrupt",
            );
          } else if (prior.kind === "active") {
            decision = pinErrorDecision(
              config,
              context,
              "session_model_pin_catalog_unavailable",
            );
          } else {
            decision = buildParentDecision(config, context, {
              reasonCode: "model_catalog_unavailable",
            });
          }
        } else {
          let requested;
          try {
            requested = validateModelPinProfile(control.profile, catalog);
          } catch (error) {
            if (!(error instanceof RangeError)) {
              throw error;
            }
            const prior = validateStoredPinStatus(
              await readStoredPinStatus({
                pluginData,
                sessionId: input.session_id,
              }),
              catalog,
            );
            if (prior.kind === "corrupt") {
              decision = pinErrorDecision(
                config,
                context,
                "session_model_pin_corrupt",
              );
            } else if (prior.kind === "active") {
              activePin = prior.profile;
              pinDiagnosticReasonCode =
                "session_model_pin_request_unavailable";
            } else {
              decision = pinErrorDecision(
                config,
                context,
                "session_model_pin_unavailable",
              );
            }
          }
          if (requested !== undefined) {
            activePin = await writeModelPin({
              pluginData,
              sessionId: input.session_id,
              profile: requested,
              nowMs: context.nowMs,
            });
          }
        }
      } else if (control.kind !== "clear") {
        let current = await readStoredPinStatus({
          pluginData,
          sessionId: input.session_id,
        });
        if (current.kind === "corrupt") {
          decision = pinErrorDecision(
            config,
            context,
            "session_model_pin_corrupt",
          );
        } else if (current.kind === "active" && catalogReadFailed) {
          decision = pinErrorDecision(
            config,
            context,
            "session_model_pin_catalog_unavailable",
          );
        } else if (current.kind === "active") {
          current = validateStoredPinStatus(current, catalog);
          if (current.kind === "unavailable") {
            decision = pinErrorDecision(
              config,
              context,
              "session_model_pin_unavailable",
            );
          } else {
            activePin = current.profile;
          }
        }

        if (decision === undefined && control.kind === "invalid") {
          if (activePin === null) {
            decision = pinErrorDecision(config, context, control.reasonCode);
          } else {
            pinDiagnosticReasonCode = retainedRequestReason[control.reasonCode];
            if (pinDiagnosticReasonCode === undefined) {
              throw new RangeError("unsupported invalid model pin reason");
            }
          }
        }
        if (
          decision === undefined &&
          activePin !== null &&
          control.kind === "none" &&
          oneTurnProfileConflicts(input.prompt, config, activePin)
        ) {
          pinDiagnosticReasonCode = "session_model_pin_conflict_ignored";
        }
      }

      if (decision === undefined && activePin !== null) {
        decision = buildPinnedDecision(config, context, activePin, {
          diagnosticReasonCode: pinDiagnosticReasonCode,
        });
      }

      if (decision === undefined) {
        if (catalogReadFailed) {
          decision = buildParentDecision(config, context, {
            reasonCode: "model_catalog_unavailable",
          });
        } else {
          try {
            validateConfiguredModels(config, catalog);
          } catch {
            decision = buildParentDecision(config, context, {
              reasonCode: "model_catalog_unavailable",
            });
          }
        }
      }

      if (decision === undefined) {
        const outcomes = await withOutcomeTracking(() =>
          readOrResetOutcomesForPrompt({
            pluginData,
            sessionId: input.session_id,
            maxAgeMs: config.routing.decisionMaxAgeMs,
          })
        );
        const sessionFloorRoute =
          outcomes !== null && outcomes.retryEscalations >= 2
            ? "standard"
            : null;
        let recommendation = null;
        let effectiveTaskProfile = null;
        ({ decision, recommendation, effectiveTaskProfile } =
          await classifyPromptWithSmartResult(
            input.prompt,
            config,
            context,
            {
              pluginData,
              env,
              sessionFloorRoute,
              buildDigest: (deterministicDecision) =>
                buildSignalsDigest({
                  prompt: input.prompt,
                  deterministicDecision,
                  outcomes,
                  cwd: input.cwd,
                }),
            },
          ));
        decision = attachDelegationPlan({
          prompt: input.prompt,
          decision,
          recommendation,
          effectiveTaskProfile,
          config,
        });
      }
      await replaceOwnedDecision(decision);

      if (
        decision.method === "retry-escalation" ||
        decision.method === "recurring-failure"
      ) {
        await withOutcomeTracking(() =>
          recordOutcome({
            pluginData,
            sessionId: input.session_id,
            kind: "retryEscalation",
            maxAgeMs: config.routing.decisionMaxAgeMs,
          })
        );
      }
      if (decision.method === "smart-fallback") {
        await withOutcomeTracking(() =>
          recordOutcome({
            pluginData,
            sessionId: input.session_id,
            kind: "smartFallback",
            maxAgeMs: config.routing.decisionMaxAgeMs,
          })
        );
      }
      if (decision.execution === "agent") {
        await withOutcomeTracking(() =>
          recordOutcome({
            pluginData,
            sessionId: input.session_id,
            kind: "lastRoute",
            route: decision.route,
            maxAgeMs: config.routing.decisionMaxAgeMs,
          })
        );
      }

      let routingContext = buildRoutingContext(decision);
      if (
        routingContext !== null &&
        decision.delegationPlan !== null &&
        decision.method === "smart-fallback"
      ) {
        routingContext +=
          " Smart classifier unavailable; deterministic fallback applied.";
      }
      return routingContext === null
        ? null
        : additionalContextResult("UserPromptSubmit", routingContext);
    } catch (error) {
      if (ownedDecisionId !== null) {
        await removeSessionState({
          pluginData,
          sessionId: input.session_id,
          expectedDecisionId: ownedDecisionId,
        });
      }
      throw error;
    }
  },
);
