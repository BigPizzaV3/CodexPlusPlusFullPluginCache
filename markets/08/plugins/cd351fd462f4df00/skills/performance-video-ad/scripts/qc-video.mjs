#!/usr/bin/env node
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { writeFile } from "node:fs/promises";
import path from "node:path";

const args = process.argv.slice(2);
const file = args[0] ? path.resolve(args[0]) : null;
const value = (flag, fallback) => {
  const index = args.indexOf(flag);
  return index >= 0 ? args[index + 1] : fallback;
};
assert.ok(file, "Usage: node scripts/qc-video.mjs <video.mp4> [--width 1080 --height 1920 --duration 15 --fps 30]");
const expected = {
  width: Number(value("--width", 1080)),
  height: Number(value("--height", 1920)),
  duration: Number(value("--duration", 15)),
  fps: Number(value("--fps", 30)),
};

const probe = spawnSync("ffprobe", ["-v", "error", "-show_streams", "-show_format", "-of", "json", file], { encoding: "utf8" });
assert.equal(probe.status, 0, probe.stderr || "ffprobe failed");
const metadata = JSON.parse(probe.stdout);
const video = metadata.streams.find((stream) => stream.codec_type === "video");
const audio = metadata.streams.find((stream) => stream.codec_type === "audio");
assert.ok(video, "video stream missing");
const [rateNumerator, rateDenominator] = video.avg_frame_rate.split("/").map(Number);
const fps = rateNumerator / rateDenominator;
const duration = Number(video.duration ?? metadata.format.duration);
assert.equal(video.width, expected.width, "unexpected width");
assert.equal(video.height, expected.height, "unexpected height");
assert.ok(Math.abs(fps - expected.fps) < 0.01, "unexpected frame rate");
assert.ok(Math.abs(duration - expected.duration) <= 0.1, "unexpected duration");
assert.equal(video.codec_name, "h264", "final video must use H.264");
assert.ok(["yuv420p", "yuvj420p"].includes(video.pix_fmt), "final video must use 8-bit 4:2:0");

let audioQc = null;
if (audio) {
  assert.equal(audio.codec_name, "aac", "final audio must use AAC");
  const volume = spawnSync("ffmpeg", ["-hide_banner", "-i", file, "-af", "volumedetect", "-f", "null", "-"], { encoding: "utf8" });
  assert.equal(volume.status, 0, "audio QC failed");
  const meanVolumeDb = Number(volume.stderr.match(/mean_volume:\s*(-?[\d.]+) dB/)?.[1]);
  const maxVolumeDb = Number(volume.stderr.match(/max_volume:\s*(-?[\d.]+) dB/)?.[1]);
  assert.ok(Number.isFinite(meanVolumeDb) && meanVolumeDb >= -40, "audio is missing or too quiet");
  assert.ok(Number.isFinite(maxVolumeDb) && maxVolumeDb <= -1, "audio peak is too high");
  audioQc = { codec: audio.codec_name, meanVolumeDb, maxVolumeDb };
}

const report = {
  schemaVersion: 1,
  status: "PASS",
  file: path.basename(file),
  checkedAt: new Date().toISOString(),
  distributionStatus: "LOCAL_QC_ONLY",
  publishAllowed: false,
  activateAdsAllowed: false,
  technical: { width: video.width, height: video.height, fps, duration, codec: video.codec_name, pixelFormat: video.pix_fmt, audio: audioQc },
};
const reportPath = file.replace(/\.[^.]+$/, ".qc.json");
await writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
console.log(`Technical QC: PASS -> ${reportPath}`);
