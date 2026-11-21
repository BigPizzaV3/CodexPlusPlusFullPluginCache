#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SPOKEN_KEYS = new Set(["hookCopy", "spoken_copy", "narration", "subtitle", "headline", "eyebrow", "button", "supporting_line", "trust_note"]);
const UI_KEYS = new Set(["ui_labels", "renderedCopySegments", "copyKeys"]);
const FORBIDDEN = [
  ["成果線", /成果線/u],
  ["営業後工程", /営業後工程/u],
  ["初期見立てを相談する", /初期見立てを相談する/u],
  ["説明できる状態へ", /説明できる状態へ/u],
  ["原因候補を見直す", /原因候補を見直す/u],
  ["〜を実現", /を実現(?:する|します|。|$)/u],
  ["〜を支援", /を支援(?:する|します|。|$)/u],
  ["〜が可能となります", /が可能となります/u]
];

const collectSpoken = (value, pathParts = [], active = false, output = []) => {
  if (typeof value === "string") {
    if (active) output.push({ path: pathParts.join("."), text: value });
    return output;
  }
  if (Array.isArray(value)) {
    value.forEach((item, index) => collectSpoken(item, [...pathParts, String(index)], active, output));
    return output;
  }
  if (!value || typeof value !== "object") return output;
  for (const [key, child] of Object.entries(value)) {
    const nextActive = UI_KEYS.has(key) ? false : active || SPOKEN_KEYS.has(key);
    collectSpoken(child, [...pathParts, key], nextActive, output);
  }
  return output;
};

export function validateJapaneseNaturalness(artifact) {
  const strings = collectSpoken(artifact);
  const errors = [];
  const warnings = [];
  const seen = new Map();
  for (const item of strings) {
    const text = item.text.trim();
    if (!text) continue;
    for (const [label, pattern] of FORBIDDEN) if (pattern.test(text)) errors.push(`${item.path}: forbidden spoken expression ${label}: ${text}`);
    if (text.length > 52) errors.push(`${item.path}: too long for one breath (${text.length} chars): ${text}`);
    else if (text.length > 38) warnings.push(`${item.path}: read aloud and consider shortening (${text.length} chars): ${text}`);
    if (/(?:[一-龥ァ-ヶーA-Za-z0-9]+[・／/]){2,}[一-龥ァ-ヶーA-Za-z0-9]+/u.test(text)) warnings.push(`${item.path}: three or more noun labels may sound like a specification list: ${text}`);
    if (text.length < 18 && /(整理|見直|支援|実現)(する|します)[。]?$/u.test(text)) warnings.push(`${item.path}: abstract verb needs a concrete object or visible change: ${text}`);
    const prior = seen.get(text);
    if (prior) warnings.push(`${item.path}: duplicates viewer-facing copy from ${prior}: ${text}`);
    else seen.set(text, item.path);
  }
  assert.equal(errors.length, 0, `Japanese naturalness failed:\n- ${errors.join("\n- ")}`);
  return { strings: strings.length, warnings };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const files = process.argv.slice(2).map((file) => path.resolve(file));
  assert.ok(files.length > 0, "Usage: node scripts/validate-japanese-naturalness.mjs <artifact.json> [more...]");
  let checked = 0;
  const warnings = [];
  for (const file of files) {
    const result = validateJapaneseNaturalness(JSON.parse(await readFile(file, "utf8")));
    checked += result.strings;
    warnings.push(...result.warnings.map((warning) => `${path.basename(file)}: ${warning}`));
  }
  console.log(`Japanese naturalness: PASS (${checked} viewer-facing strings / ${warnings.length} warnings)`);
  for (const warning of warnings) console.log(`WARN ${warning}`);
}
