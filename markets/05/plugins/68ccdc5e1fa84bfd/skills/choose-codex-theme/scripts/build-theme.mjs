#!/usr/bin/env node

import { readFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";

const catalogUrl = new URL("../references/themes.json", import.meta.url);
const catalog = JSON.parse(await readFile(catalogUrl, "utf8"));
const args = process.argv.slice(2);

function option(name) {
  const index = args.indexOf(name);
  if (index === -1) return undefined;
  const value = args[index + 1];
  if (!value || value.startsWith("--")) {
    throw new Error(`${name} requires a value.`);
  }
  return value;
}

function normalize(value) {
  return String(value)
    .normalize("NFKC")
    .trim()
    .toLocaleLowerCase("en-US")
    .replace(/&/g, "and")
    .replace(/[\s_]+/g, "-")
    .replace(/[^\p{L}\p{N}-]+/gu, "")
    .replace(/-+/g, "-");
}

function assertHex(value, label) {
  if (!/^#[0-9A-F]{6}$/i.test(value)) {
    throw new Error(`${label} must be a six-digit hex color; received ${value}.`);
  }
}

function validateTheme(theme) {
  for (const key of ["surface", "ink", "accent"]) {
    assertHex(theme[key], `${theme.slug}.${key}`);
  }
  for (const [key, value] of Object.entries(theme.semanticColors)) {
    assertHex(value, `${theme.slug}.semanticColors.${key}`);
  }
  if (!Number.isInteger(theme.contrast) || theme.contrast < 0 || theme.contrast > 100) {
    throw new Error(`${theme.slug}.contrast must be an integer from 0 to 100.`);
  }
}

for (const theme of catalog.themes) validateTheme(theme);

if (args.includes("--list")) {
  for (const theme of catalog.themes) {
    console.log(`${theme.id}\t${theme.slug}\t${theme.name.en}\t${theme.name.zh}\t${theme.tags.join(",")}`);
  }
  process.exit(0);
}

const query = option("--theme");
if (!query) {
  console.error("Usage: node scripts/build-theme.mjs --list | --theme <id|slug|name> [--preview-path] [--ui-font <font>] [--code-font <font>]");
  process.exit(2);
}

const normalizedQuery = normalize(query);
const theme = catalog.themes.find((candidate) => {
  const aliases = [candidate.id, `0${candidate.id}`, candidate.slug, candidate.name.en, candidate.name.zh];
  return aliases.some((alias) => normalize(alias) === normalizedQuery);
});

if (!theme) {
  const choices = catalog.themes.map((candidate) => `${candidate.id}:${candidate.slug}`).join(", ");
  throw new Error(`Unknown theme "${query}". Choose one of: ${choices}`);
}

if (args.includes("--preview-path")) {
  const previewPath = fileURLToPath(new URL(theme.preview, catalogUrl)).replaceAll("\\", "/");
  console.log(previewPath);
  process.exit(0);
}

const uiFont = option("--ui-font")?.trim() || theme.fonts?.ui || catalog.defaults.fonts.ui;
const codeFont = option("--code-font")?.trim() || theme.fonts?.code || catalog.defaults.fonts.code;

const payload = {
  codeThemeId: catalog.codeThemeId,
  theme: {
    accent: theme.accent,
    contrast: theme.contrast,
    fonts: { code: codeFont, ui: uiFont },
    ink: theme.ink,
    opaqueWindows: catalog.defaults.opaqueWindows,
    semanticColors: theme.semanticColors,
    surface: theme.surface,
  },
  variant: theme.variant || catalog.defaults.variant,
};

console.log(`codex-theme-v1:${JSON.stringify(payload)}`);
