#!/usr/bin/env node

// src/asr-worker.ts
import fs2 from "node:fs/promises";
import { pathToFileURL } from "node:url";

// src/environment.ts
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
var PLUGIN_ROOT = process.env.WANDEO_PLUGIN_ROOT || path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
var configured;
function runtimeConfig() {
  if (!configured) throw new Error("Runtime is not configured. Run wandeo setup.");
  return configured;
}
function runtimeRequire(root) {
  return createRequire(path.join(root || runtimeConfig().depsRoot, "package.json"));
}

// src/util.ts
import fs from "node:fs/promises";
async function readJson(file) {
  return JSON.parse(await fs.readFile(file, "utf8"));
}

// src/asr-worker.ts
var request = await readJson(process.argv[2]);
console.log = (...values) => console.error(...values);
var imported = await import(pathToFileURL(runtimeRequire(request.asrRoot).resolve("@huggingface/transformers")).href);
var module = imported.env ? imported : imported.default;
module.env.allowRemoteModels = false;
module.env.allowLocalModels = true;
module.env.useBrowserCache = false;
module.env.backends.onnx.logLevel = "error";
var pcm = await fs2.readFile(request.pcm);
var audio = new Float32Array(pcm.buffer.slice(pcm.byteOffset, pcm.byteOffset + pcm.byteLength));
var transcriber = await module.pipeline("automatic-speech-recognition", request.model, { device: "cpu", dtype: "q8", local_files_only: true });
try {
  const result = await transcriber(audio, { task: "transcribe", ...request.language ? { language: request.language } : {}, return_timestamps: true, chunk_length_s: 30, stride_length_s: 5 });
  const duration = audio.length / 16e3;
  const cues = (result.chunks || []).map((chunk) => ({ start: Math.max(0, chunk.timestamp[0] || 0), end: Math.min(duration, chunk.timestamp[1] ?? duration), text: chunk.text.trim() })).filter((cue) => cue.text && cue.end > cue.start);
  process.stdout.write(JSON.stringify({ schemaVersion: 1, model: "Whisper-small multilingual q8", durationSeconds: duration, text: result.text, cues, timing: "ASR segment timestamps; inspect uncertain synchronization against audio." }) + "\n");
} finally {
  await transcriber.dispose();
}
