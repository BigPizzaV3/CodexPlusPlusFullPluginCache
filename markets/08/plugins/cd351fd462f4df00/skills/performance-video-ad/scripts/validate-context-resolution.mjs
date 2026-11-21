#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const REQUIRED_FUNNEL_FIELDS = [
  "offer_id",
  "traffic_temperature",
  "awareness_stage",
  "funnel_stage",
  "next_destination",
  "primary_conversion",
  "final_conversion",
  "ad_primary_job",
  "ad_cta_action",
];

const isPresent = (value) => value !== null && value !== undefined && (!(typeof value === "string") || value.trim().length > 0);

export function validateContextResolution(record, { requireReady = false } = {}) {
  assert.equal(record.schemaVersion, 1, "context resolution: unsupported schemaVersion");
  assert.equal(record.contextResolutionVersion, 1, "context resolution: unsupported contextResolutionVersion");
  assert.ok(record.jobId, "context resolution: jobId missing");
  assert.ok(["DRAFT", "READY", "NEEDS_USER_INPUT"].includes(record.status), "context resolution: invalid status");
  assert.ok(Array.isArray(record.required_fields), "context resolution: required_fields missing");
  for (const field of REQUIRED_FUNNEL_FIELDS) assert.ok(record.required_fields.includes(field), `context resolution: required field ${field} missing`);
  assert.ok(Array.isArray(record.source_attempts), "context resolution: source_attempts missing");
  assert.ok(Array.isArray(record.field_resolutions), "context resolution: field_resolutions missing");
  assert.ok(Array.isArray(record.unresolved_blocking_fields), "context resolution: unresolved_blocking_fields missing");
  assert.ok(Array.isArray(record.questions_to_user) && record.questions_to_user.length <= 3, "context resolution: ask at most three questions");

  if (record.status === "DRAFT" && !requireReady) return { status: record.status, resolved: 0, unresolved: 0, questions: 0 };

  const attempts = new Map();
  for (const source of record.source_attempts) {
    assert.ok(source.ref && !attempts.has(source.ref), `context resolution: duplicate or missing source ref ${source.ref ?? "<missing>"}`);
    assert.ok(["read", "unavailable", "not_configured"].includes(source.retrieval_status), `context resolution: invalid retrieval status for ${source.ref}`);
    if (source.source_type === "conversation_memory" && source.retrieval_status === "read") {
      assert.equal(source.staleness_checked, true, `context resolution: conversation memory ${source.ref} requires a staleness check`);
      assert.notEqual(source.authority_role, "canonical", `context resolution: conversation memory ${source.ref} cannot be canonical by itself`);
    }
    attempts.set(source.ref, source);
  }

  const questions = new Map();
  for (const question of record.questions_to_user) {
    assert.ok(question.question_id && !questions.has(question.question_id), `context resolution: duplicate or missing question ${question.question_id ?? "<missing>"}`);
    assert.ok(Array.isArray(question.field_ids) && question.field_ids.length > 0, `context resolution: question ${question.question_id} must cover fields`);
    assert.ok(question.question && question.decision_impact, `context resolution: question ${question.question_id} needs wording and decision impact`);
    questions.set(question.question_id, question);
  }

  const resolutions = new Map();
  for (const field of record.field_resolutions) {
    assert.ok(field.field_id && !resolutions.has(field.field_id), `context resolution: duplicate or missing field ${field.field_id ?? "<missing>"}`);
    assert.ok(["resolved", "missing", "conflict", "low_confidence"].includes(field.state), `context resolution: invalid state for ${field.field_id}`);
    if (field.state === "resolved") {
      assert.ok(isPresent(field.value), `context resolution: resolved field ${field.field_id} has no value`);
      assert.ok(Array.isArray(field.source_refs) && field.source_refs.length > 0, `context resolution: resolved field ${field.field_id} has no source refs`);
      assert.notEqual(field.confidence, "unknown", `context resolution: resolved field ${field.field_id} has unknown confidence`);
      assert.equal(field.question_id, null, `context resolution: resolved field ${field.field_id} must not retain a question`);
      for (const ref of field.source_refs) {
        const source = attempts.get(ref);
        assert.ok(source, `context resolution: field ${field.field_id} references unknown source ${ref}`);
        assert.equal(source.retrieval_status, "read", `context resolution: field ${field.field_id} uses unread source ${ref}`);
      }
      if (field.blocking) {
        const authoritative = field.source_refs.map((ref) => attempts.get(ref)).some((source) => !["background_only", "general_only"].includes(source.authority_role));
        assert.ok(authoritative, `context resolution: blocking field ${field.field_id} cannot be resolved only from background/general sources`);
        assert.notEqual(field.confidence, "inferred", `context resolution: blocking field ${field.field_id} cannot rely only on inference`);
      }
    } else if (field.blocking) {
      assert.ok(field.question_id && questions.has(field.question_id), `context resolution: unresolved blocking field ${field.field_id} needs a user question`);
      assert.ok(questions.get(field.question_id).field_ids.includes(field.field_id), `context resolution: question ${field.question_id} does not cover ${field.field_id}`);
    } else {
      assert.ok(Object.hasOwn(field, "fallback_if_nonblocking"), `context resolution: non-blocking unresolved field ${field.field_id} needs an explicit fallback`);
    }
    resolutions.set(field.field_id, field);
  }

  for (const fieldId of record.required_fields) assert.ok(resolutions.has(fieldId), `context resolution: no resolution record for ${fieldId}`);
  const derivedUnresolved = [...resolutions.values()].filter((field) => field.blocking && field.state !== "resolved").map((field) => field.field_id).sort();
  assert.deepEqual([...record.unresolved_blocking_fields].sort(), derivedUnresolved, "context resolution: unresolved_blocking_fields does not match field states");
  for (const question of questions.values()) for (const fieldId of question.field_ids) assert.ok(derivedUnresolved.includes(fieldId), `context resolution: question ${question.question_id} covers a resolved/non-blocking field ${fieldId}`);

  if (record.status === "READY" || requireReady) {
    assert.equal(record.status, "READY", "context resolution: Hook work requires READY status");
    assert.equal(derivedUnresolved.length, 0, "context resolution: READY cannot contain unresolved blocking fields");
    assert.equal(questions.size, 0, "context resolution: READY cannot retain user questions");
  } else if (record.status === "NEEDS_USER_INPUT") {
    assert.ok(derivedUnresolved.length > 0, "context resolution: NEEDS_USER_INPUT requires unresolved blocking fields");
    assert.ok(questions.size >= 1 && questions.size <= 3, "context resolution: unresolved blockers require one to three questions");
  }

  return { status: record.status, resolved: [...resolutions.values()].filter((field) => field.state === "resolved").length, unresolved: derivedUnresolved.length, questions: questions.size };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-context-resolution.mjs <context-resolution.json> [--require-ready]");
  const record = JSON.parse(await readFile(file, "utf8"));
  const result = validateContextResolution(record, { requireReady: process.argv.includes("--require-ready") });
  console.log(`Context resolution: PASS (${result.status}; ${result.resolved} resolved / ${result.unresolved} unresolved / ${result.questions} questions)`);
}
