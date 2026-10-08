#!/usr/bin/env node

import { spawn } from "node:child_process";
import readline from "node:readline";

const includeHidden = process.argv.includes("--include-hidden");
const timeoutArg = process.argv.find((arg) => arg.startsWith("--timeout-ms="));
const timeoutMs = timeoutArg ? Number(timeoutArg.split("=")[1]) : 15_000;

if (!Number.isFinite(timeoutMs) || timeoutMs < 1_000) {
  console.error("Invalid --timeout-ms value; use a number of at least 1000.");
  process.exit(2);
}

const child = spawn("codex", ["app-server", "--stdio"], {
  stdio: ["pipe", "pipe", "pipe"],
});
const lines = readline.createInterface({ input: child.stdout });
let settled = false;
let stderr = "";

const timer = setTimeout(() => {
  finishWithError(
    `Timed out after ${timeoutMs}ms while reading the live Codex model catalog.`,
  );
}, timeoutMs);

child.stderr.on("data", (chunk) => {
  stderr += chunk.toString();
});

child.on("error", (error) => {
  finishWithError(`Could not start codex app-server: ${error.message}`);
});

child.on("exit", (code, signal) => {
  if (!settled) {
    const detail = stderr.trim() ? `\n${stderr.trim()}` : "";
    finishWithError(
      `codex app-server exited before returning model/list (code ${code}, signal ${signal}).${detail}`,
    );
  }
});

lines.on("line", (line) => {
  let message;
  try {
    message = JSON.parse(line);
  } catch {
    return;
  }

  if (message.id === 0) {
    if (message.error) {
      finishWithError(`Codex initialization failed: ${message.error.message}`);
      return;
    }
    send({ method: "initialized", params: {} });
    send({
      method: "model/list",
      id: 1,
      params: { limit: 100, includeHidden },
    });
    return;
  }

  if (message.id === 1) {
    if (message.error) {
      finishWithError(`model/list failed: ${message.error.message}`);
      return;
    }

    const data = Array.isArray(message.result?.data)
      ? message.result.data
      : [];
    const normalized = data.map((model) => ({
      id: model.id,
      model: model.model,
      displayName: model.displayName,
      description: model.description ?? null,
      hidden: Boolean(model.hidden),
      isDefault: Boolean(model.isDefault),
      defaultReasoningEffort: model.defaultReasoningEffort ?? null,
      supportedReasoningEfforts: Array.isArray(
        model.supportedReasoningEfforts,
      )
        ? model.supportedReasoningEfforts.map((item) => ({
            effort: item.reasoningEffort,
            description: item.description ?? null,
          }))
        : [],
      inputModalities: model.inputModalities ?? ["text", "image"],
      additionalSpeedTiers: model.additionalSpeedTiers ?? [],
      serviceTiers: Array.isArray(model.serviceTiers)
        ? model.serviceTiers.map((tier) => ({
            id: tier.id,
            name: tier.name,
            description: tier.description ?? null,
          }))
        : [],
      defaultServiceTier: model.defaultServiceTier ?? null,
      upgrade: model.upgrade ?? null,
    }));

    finishWithResult({
      schemaVersion: 1,
      source: "codex-app-server:model/list",
      retrievedAt: new Date().toISOString(),
      includeHidden,
      nextCursor: message.result?.nextCursor ?? null,
      models: normalized,
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "model_compass",
      title: "Model Compass",
      version: "0.1.0",
    },
  },
});

function send(message) {
  if (!child.stdin.destroyed) {
    child.stdin.write(`${JSON.stringify(message)}\n`);
  }
}

function finishWithResult(result) {
  if (settled) return;
  settled = true;
  clearTimeout(timer);
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  child.kill();
}

function finishWithError(message) {
  if (settled) return;
  settled = true;
  clearTimeout(timer);
  console.error(message);
  child.kill();
  process.exitCode = 1;
}
