#!/usr/bin/env node
import assert from "node:assert/strict";
import { mkdir, writeFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import os from "node:os";
import path from "node:path";
import { resolveFalCredential, FAL_KEYCHAIN_SERVICE } from "./fal-credential-resolver.mjs";

const args = process.argv.slice(2);
const outIndex = args.indexOf("--out");
const outPath = outIndex >= 0 ? path.resolve(args[outIndex + 1]) : null;
assert.ok(outPath, "Usage: node scripts/detect-capabilities.mjs --out <capability-snapshot.json>");

const run = (command, commandArgs = []) => {
  const result = spawnSync(command, commandArgs, { encoding: "utf8" });
  return { ok: result.status === 0, output: `${result.stdout ?? ""}\n${result.stderr ?? ""}`.trim() };
};
const inspectTool = (command, versionArgs = ["--version"]) => {
  const location = run("which", [command]);
  if (!location.ok) return { status: "missing", path: null, version: null };
  const version = run(command, versionArgs);
  return {
    status: version.ok ? "verified" : "installed",
    path: location.output.split("\n")[0],
    version: version.output.split("\n")[0] || null,
  };
};
const secretStatus = (names) => names.some((name) => Boolean(process.env[name])) ? "configured" : "missing";
const falCredential = resolveFalCredential();
const df = run("df", ["-k", process.cwd()]);
const disk = df.output.split("\n").filter(Boolean).at(-1)?.trim().split(/\s+/) ?? [];
const availableDiskBytes = Number(disk[3] ?? 0) * 1024;

const snapshot = {
  schemaVersion: 1,
  checkedAt: new Date().toISOString(),
  host: {
    os: os.platform(),
    osRelease: os.release(),
    architecture: os.arch(),
    cpuModel: os.cpus()[0]?.model ?? null,
    cpuCount: os.cpus().length,
    shell: process.env.SHELL ?? null,
    availableDiskBytes,
    diskStatus: availableDiskBytes >= 25 * 1024 ** 3 ? "verified" : "restricted",
  },
  tools: {
    git: inspectTool("git"),
    node: inspectTool("node"),
    npm: inspectTool("npm"),
    python: inspectTool("python3"),
    ffmpeg: inspectTool("ffmpeg", ["-version"]),
    ffprobe: inspectTool("ffprobe", ["-version"]),
    codex: inspectTool("codex"),
    genmedia: inspectTool("genmedia"),
    falCli: inspectTool("fal"),
  },
  providers: {
    fal: {
      status: falCredential ? "configured" : "missing",
      credentialSource: falCredential?.source ?? null,
      secretNamesChecked: ["FAL_KEY", "FAL_API_KEY"],
      keychainServiceChecked: FAL_KEYCHAIN_SERVICE,
    },
    googleVideo: { status: secretStatus(["GOOGLE_API_KEY", "GOOGLE_APPLICATION_CREDENTIALS"]), secretNamesChecked: ["GOOGLE_API_KEY", "GOOGLE_APPLICATION_CREDENTIALS"] },
    bytePlus: { status: secretStatus(["BYTEPLUS_API_KEY", "BYTEPLUS_ACCESS_KEY"]), secretNamesChecked: ["BYTEPLUS_API_KEY", "BYTEPLUS_ACCESS_KEY"] },
  },
  localGeneration: {
    nvidiaGpu: run("which", ["nvidia-smi"]).ok ? "installed" : "unavailable",
    comfyUi: process.env.COMFYUI_PATH ? "configured" : "missing",
  },
  network: { status: "restricted", note: "No network probe or provider request is performed." },
  secretPolicy: "presence-only; values are never recorded",
};

await mkdir(path.dirname(outPath), { recursive: true });
await writeFile(outPath, `${JSON.stringify(snapshot, null, 2)}\n`, "utf8");
console.log(`Capability snapshot: ${outPath}`);
console.log(`Providers: fal=${snapshot.providers.fal.status}, google=${snapshot.providers.googleVideo.status}, byteplus=${snapshot.providers.bytePlus.status}`);
