#!/usr/bin/env node

import {mkdir, readFile, writeFile, rename, rm, realpath} from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import {fileURLToPath, pathToFileURL} from "node:url";
import {loadCatalog} from "./segment_catalog_store.mjs";

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const SKILL_DIR = path.resolve(SCRIPT_DIR, "..");
const SDK_PACKAGE = "segment-designer-sdk";
const ALLOWED_ARGUMENTS = new Set([
  "catalog",
  "catalog-file",
  "organization-id",
  "input",
  "request",
  "script",
  "output",
  "diagnostics",
  "segment-id",
  "name",
  "description",
  "tag",
  "mode",
]);

function parseArgs(argv) {
  const result = {tags: []};
  for (let index = 0; index < argv.length; index += 1) {
    const argumentText = argv[index];
    if (!argumentText.startsWith("--")) throw new Error(`Unexpected argument: ${argumentText}`);
    const optionName = argumentText.slice(2);
    if (!ALLOWED_ARGUMENTS.has(optionName)) throw new Error(`Unsupported argument: --${optionName}`);
    const value = argv[index + 1];
    if (value === undefined || value.startsWith("--")) throw new Error(`Missing value for --${optionName}`);
    if (optionName === "tag") {
      const normalized = value.trim();
      if (!normalized) throw new Error("--tag must be a non-empty string.");
      if (!result.tags.includes(normalized)) result.tags.push(normalized);
    } else {
      if (Object.hasOwn(result, optionName)) throw new Error(`--${optionName} may be provided only once.`);
      result[optionName] = value;
    }
    index += 1;
  }
  return result;
}

function requiredValue(args, name) {
  const value = args[name];
  if (typeof value !== "string" || value.trim().length === 0) {
    throw new Error(`--${name} is required.`);
  }
  return value.trim();
}

function requiredPath(args, name) {
  return path.resolve(requiredValue(args, name));
}

function normalizeSegmentId(value, fieldName = "segment ID") {
  const normalized = String(value ?? "").trim();
  if (!/^\d+$/u.test(normalized) || BigInt(normalized) <= 0n) throw new Error(`${fieldName} must contain decimal digits only.`);
  return normalized;
}

function resolveMode(args) {
  if (args.mode !== undefined) {
    if (args.mode !== "count") throw new Error("--mode supports only count; omit it for create/update.");
    if (["segment-id", "name", "description"].some((name) => args[name] !== undefined) || args.tags.length) {
      throw new Error("Count mode does not accept a segment ID or create metadata.");
    }
    return {mode: "count"};
  }
  const segmentId = args["segment-id"] === undefined
    ? undefined
    : normalizeSegmentId(args["segment-id"], "--segment-id");
  if (segmentId !== undefined) {
    const createOnly = ["name", "description"].filter((name) => args[name] !== undefined);
    if (createOnly.length > 0 || args.tags.length > 0) {
      throw new Error("--name, --description, and --tag are allowed only when creating a segment.");
    }
    return {mode: "update", segmentId};
  }
  return {
    mode: "create",
    name: requiredValue(args, "name"),
    description: typeof args.description === "string" ? args.description : "",
    tags: args.tags.map((name) => ({name})),
  };
}

async function readJson(file) {
  return JSON.parse(await readFile(file, "utf8"));
}

async function writeJson(file, value) {
  await mkdir(path.dirname(file), {recursive: true});
  const temporary = `${file}.${process.pid}.tmp`;
  try {
    await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`, {encoding: "utf8", flag: "wx"});
    await rename(temporary, file);
  } finally { await rm(temporary, {force: true}); }
}

function definitionItems(value) {
  if (Array.isArray(value)) return value;
  if (value && typeof value === "object" && Array.isArray(value.definitions)) return value.definitions;
  throw new Error("The resolved catalog does not contain a definitions array.");
}

async function resolveSdkEntry() {
  return path.resolve(SKILL_DIR, "../../packages", SDK_PACKAGE, "dist/index.js");
}

function mcpErrorMessage(error) {
  if (typeof error === "string" && error.trim()) return error.trim();
  if (error && typeof error === "object" && typeof error.message === "string" && error.message.trim()) {
    return error.message.trim();
  }
  return "MCP tool call failed.";
}

function extractMcpToolPayload(responseBody, toolName) {
  if (!responseBody || typeof responseBody !== "object" || Array.isArray(responseBody)) {
    throw new Error(`${toolName} returned an invalid MCP response body.`);
  }
  if (responseBody.error !== undefined) {
    throw new Error(`${toolName} failed: ${mcpErrorMessage(responseBody.error)}`);
  }
  const result = responseBody.result;
  if (!result || typeof result !== "object" || Array.isArray(result)) {
    throw new Error(`${toolName} MCP response result is missing.`);
  }
  if (result.isError === true) {
    const text = Array.isArray(result.content)
      ? result.content.find((item) => item && typeof item.text === "string")?.text
      : undefined;
    throw new Error(`${toolName} failed: ${text?.trim() || "MCP tool returned an error."}`);
  }
  if (result.structuredContent && typeof result.structuredContent === "object" && !Array.isArray(result.structuredContent)) {
    return result.structuredContent;
  }
  if (Array.isArray(result.content)) {
    for (const item of result.content) {
      if (!item || typeof item !== "object") continue;
      if (item.json && typeof item.json === "object" && !Array.isArray(item.json)) return item.json;
      if (typeof item.text !== "string" || !item.text.trim()) continue;
      try {
        const parsed = JSON.parse(item.text);
        if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) return parsed;
      } catch {
        // Continue looking for a structured MCP content item.
      }
    }
  }
  if (result.data && typeof result.data === "object" && !Array.isArray(result.data)) return result.data;
  throw new Error(`Unable to extract structured payload from ${toolName} MCP response.`);
}

function validateCatalogContext(catalog, mode, organizationId) {
  if (catalog.uiContext?.groupType !== "DYNAMIC") {
    throw new Error("The runner supports only a DYNAMIC segment catalog.");
  }
  const catalogOrganizationId = String(catalog.organizationId ?? "").trim();
  const runtimeOrganizationId = organizationId;
  if (!catalogOrganizationId || catalogOrganizationId !== runtimeOrganizationId) {
    throw new Error("The catalog organization does not match the selected runtime organization.");
  }
  const catalogSegmentId = catalog.segmentId === null || catalog.segmentId === undefined
    ? undefined
    : normalizeSegmentId(catalog.segmentId, "catalog segmentId");
  if (mode.mode !== "update" && catalogSegmentId !== undefined) {
    throw new Error("Create/count mode requires a catalog staged without a segment ID.");
  }
  if (mode.mode === "update" && catalogSegmentId !== mode.segmentId) {
    throw new Error("Update mode requires a catalog staged for the same segment ID passed to the runner.");
  }
}

function requireLiveSchema(segmentResult, segmentId) {
  if (!segmentResult || typeof segmentResult !== "object" || Array.isArray(segmentResult)) {
    throw new Error(`get_segment returned an invalid result for segment ${segmentId}.`);
  }
  if (String(segmentResult.segmentId ?? "") !== segmentId) {
    throw new Error(`get_segment returned a different segment ID than ${segmentId}.`);
  }
  if (segmentResult.type !== "DYNAMIC") {
    throw new Error(`Segment ${segmentId} is not a dynamic segment.`);
  }
  if (!segmentResult.schema || typeof segmentResult.schema !== "object" || Array.isArray(segmentResult.schema)) {
    throw new Error(`get_segment did not return a schema for segment ${segmentId}.`);
  }
  return segmentResult.schema;
}

async function execute(args) {
  const mode = resolveMode(args);
  const outputs = ["output", "request", "diagnostics"].map(optionName => requiredPath(args, optionName));
  const canonical = async file => {
    try { return await realpath(file); }
    catch (error) {
      if (error.code !== "ENOENT") throw error;
      const parent = path.dirname(file);
      return parent === file ? file : path.join(await canonical(parent), path.basename(file));
    }
  };
  const inputs = await Promise.all(["catalog", "catalog-file", "script", ...(args.input ? ["input"] : [])].map(optionName => canonical(requiredPath(args, optionName))));
  const targets = await Promise.all(outputs.map(canonical));
  if (new Set(targets).size !== targets.length || targets.some(file => inputs.includes(file))) throw new Error("Outputs must differ from every input and each other");
  for (const file of outputs) await rm(file, {force: true});
  const catalog = await loadCatalog(await readJson(requiredPath(args, "catalog")), requiredPath(args, "catalog-file"));
  const organizationId = normalizeSegmentId(requiredValue(args, "organization-id"), "--organization-id");
  validateCatalogContext(catalog, mode, organizationId);
  const sdk = await import(pathToFileURL(await resolveSdkEntry()).href);
  const outputSchema = await readJson(path.join(SKILL_DIR, "references", "schema", "segment-output.schema.json"));
  let inputModel;
  if (mode.mode === "update") {
    const raw = await readJson(requiredPath(args, "input"));
    const live = raw.result || raw.content || raw.structuredContent || raw.isError ? extractMcpToolPayload(raw.result ? raw : {result: raw}, "get_segment") : raw;
    inputModel = sdk.hydrateBackendSegmentModel(requireLiveSchema(live, mode.segmentId), definitionItems(catalog), catalog.uiContext);
  }
  const segment = sdk.createSegmentSdk({model: inputModel, definitions: definitionItems(catalog), outputSchema, uiContext: catalog.uiContext});
  const module = await import(pathToFileURL(requiredPath(args, "script")).href);
  const mutate = module.default ?? module.mutate;
  if (typeof mutate !== "function") throw new Error("Mutation module must export a function");
  let finished;
  await mutate(Object.freeze({...segment, finish: async () => {
    if (finished) throw new Error("Call segment.finish() only once");
    finished = await segment.finish();
    return structuredClone(finished);
  }}));
  const result = finished ?? await segment.finish();
  let request;
  if (mode.mode === "count") request = {tool: "count_segment_contacts", arguments: {schema: result.model}};
  else if (mode.mode === "create") request = {tool: "create_dynamic_segment", arguments: {name: mode.name, description: mode.description, tags: mode.tags, schema: result.model}};
  else request = {tool: "update_dynamic_segment", arguments: {segment_id: mode.segmentId, schema: result.model}};
  await writeJson(requiredPath(args, "output"), result.model);
  await writeJson(requiredPath(args, "request"), request);
  const diagnostic = {...result.diagnostics, success: true, formula: result.formula, organizationId,
    mode: mode.mode, phase: "prepared", persisted: false,
    next: "Call the prepared tool through the selected authenticated MCP connection, then verify its receipt."};
  await writeJson(requiredPath(args, "diagnostics"), diagnostic);
  process.stdout.write(`${JSON.stringify(diagnostic)}\n`);
}

if (process.argv.includes("--help")) {
  process.stdout.write("Usage: run_sdk.mjs --catalog <manifest.json> --catalog-file <download.json> --organization-id <id> --script <mutation.mjs> --output <model.json> --request <request.json> --diagnostics <diagnostics.json> [--mode count | --name <name> | --segment-id <id> --input <get_segment.json>]\n");
} else {
  try { await execute(parseArgs(process.argv.slice(2))); }
  catch (error) { process.stderr.write(`${error.message}\n`); process.exitCode = 1; }
}
