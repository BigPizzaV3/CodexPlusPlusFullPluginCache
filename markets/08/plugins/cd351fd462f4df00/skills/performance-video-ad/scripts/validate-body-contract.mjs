#!/usr/bin/env node
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const EXPLAINER_REQUIRED_ROLES = ["REFRAME", "MECHANISM", "PAYOFF", "CTA"];
const QUALIFIED_CURIOSITY_REQUIRED_ROLES = ["TENSION", "REFRAME", "PRODUCT_CATEGORY", "CTA"];
const PREDICATE_ENDING = /(です|ます|ません|ない|した|する|決める|触らない|言える|作る|やり直す|限らない|分からない)[。！？]?$/;
const POSSIBILITY_MARKER = /(かもしれ|可能性|あり得|may|might|could)/i;
const DEFAULT_PROGRESS_PHRASES = ["抜け出", "別の一手", "同じ場所を回ら", "突破口", "新しい仮説", "前に進", "different next move", "new hypothesis", "breakthrough"];

export function validateBodyContract(contract) {
  assert.equal(contract.schemaVersion, 1, "Body contract schemaVersion must be 1");
  assert.equal(contract.bodyContractVersion, 1, "bodyContractVersion must be 1");
  assert.ok(["DRAFT_NOT_LOCKED", "READY_FOR_HUMAN_REVIEW", "LOCKED"].includes(contract.status), "Body contract status is invalid");
  const hookBodyReuseVersion = contract.hookBodyReuseVersion ?? 0;
  assert.ok([0, 1].includes(hookBodyReuseVersion), "unsupported hookBodyReuseVersion");
  const funnelRoleBodyVersion = contract.funnelRoleBodyVersion ?? 0;
  assert.ok([0, 1].includes(funnelRoleBodyVersion), "unsupported funnelRoleBodyVersion");
  if (funnelRoleBodyVersion === 1) assert.ok(["qualified_curiosity", "full_explainer", "proof_explainer"].includes(contract.stage_role_mode), "stage_role_mode is required for Funnel Role Body v1");
  const qualifiedCuriosity = funnelRoleBodyVersion === 1 && contract.stage_role_mode === "qualified_curiosity";
  const desireArcEnabled = contract.desireArcVersion === 1;
  for (const field of ["jobId", "body_family_id", "promise_family", "hook_question_to_resolve", "belief_to_break", "new_belief", "concrete_payoff", "cta_deliverable"]) {
    assert.ok(typeof contract[field] === "string" && contract[field].trim(), `Body contract ${field} is required`);
  }
  assert.notEqual(contract.belief_to_break, contract.new_belief, "belief_to_break and new_belief must differ");
  if (hookBodyReuseVersion === 1) {
    const entry = contract.hook_entry_contract;
    for (const field of ["signature", "required_viewer_state", "required_open_question", "expected_body_answer"]) {
      assert.ok(typeof entry?.[field] === "string" && entry[field].trim(), `hook_entry_contract.${field} is required`);
    }
    assert.equal(entry.required_open_question, contract.hook_question_to_resolve, "hook entry open question must match hook_question_to_resolve");
    assert.ok(Array.isArray(entry.allowed_variation) && entry.allowed_variation.length > 0, "hook_entry_contract.allowed_variation is required");
    assert.ok(Array.isArray(entry.new_body_triggers) && entry.new_body_triggers.length > 0, "hook_entry_contract.new_body_triggers is required");
    for (const requiredTrigger of ["promise", "open_question", "expected_body_answer", "proof_level", "cta", "desired_relief"]) {
      assert.ok(entry.new_body_triggers.includes(requiredTrigger), `hook_entry_contract must route ${requiredTrigger} changes to a new Body`);
    }
  }
  assert.ok(Array.isArray(contract.mechanism) && contract.mechanism.length > 0, "Body contract requires a product mechanism");
  assert.ok(contract.visible_transformation?.before && contract.visible_transformation?.after, "Body contract requires visible before and after states");
  assert.notEqual(contract.visible_transformation.before, contract.visible_transformation.after, "Visible before and after states must differ");
  assert.ok(Number.isInteger(contract.max_concepts_per_beat) && contract.max_concepts_per_beat >= 1 && contract.max_concepts_per_beat <= 3, "max_concepts_per_beat must be 1-3");
  assert.ok(Array.isArray(contract.matched_hook_ids) && contract.matched_hook_ids.length > 0, "Body contract requires matched_hook_ids");
  assert.equal(new Set(contract.matched_hook_ids).size, contract.matched_hook_ids.length, "matched_hook_ids must be unique");
  assert.equal(contract.comparison_boundary, "WITHIN_BODY_FAMILY_ONLY", "Body comparison must stay within one Body family");
  assert.ok(Number.isFinite(contract.target_duration_seconds) && contract.target_duration_seconds > 0, "target_duration_seconds must be positive");
  if (desireArcEnabled) {
    for (const field of ["desired_relief", "rendered_hope_line", "intentionally_unanswered_question"]) {
      assert.ok(typeof contract.hope_contract?.[field] === "string" && contract.hope_contract[field].trim(), `hope_contract.${field} is required`);
    }
    assert.notEqual(contract.hope_contract.rendered_hope_line, contract.semantic_arc?.product_mechanism, "Hope cannot be replaced by the product mechanism");
  }
  const minimumModules = qualifiedCuriosity ? (desireArcEnabled ? 5 : 4) : 5;
  assert.ok(Array.isArray(contract.modules) && contract.modules.length >= minimumModules, `Body contract requires at least ${minimumModules} modules including CTA`);

  if (contract.semanticStrengthVersion === 1) {
    for (const field of ["human_pain", "failed_response", "surprising_truth", "product_mechanism", "concrete_progress"]) {
      assert.ok(typeof contract.semantic_arc?.[field] === "string" && contract.semantic_arc[field].trim(), `semantic_arc.${field} is required`);
    }
    for (const field of ["proven_deliverables", "mechanism_supported_possibilities", "prohibited_guarantees"]) {
      assert.ok(Array.isArray(contract.claim_ladder?.[field]) && contract.claim_ladder[field].length > 0, `claim_ladder.${field} is required`);
    }
    assert.ok(contract.claim_ladder.mechanism_supported_possibilities.every((claim) => POSSIBILITY_MARKER.test(claim)), "mechanism-supported possibilities must use calibrated possibility language");
    for (const field of ["why_current_workaround_can_fail", "why_offer_changes_view", "aha_line", "open_loop"]) {
      assert.ok(typeof contract.aha_contract?.[field] === "string" && contract.aha_contract[field].trim(), `aha_contract.${field} is required`);
    }
    assert.ok(Array.isArray(contract.aha_contract.source_refs) && contract.aha_contract.source_refs.length > 0, "aha_contract requires source refs");
    assert.ok(contract.over_safety_policy?.minimum_progress_phrases >= 1, "over_safety_policy requires a positive minimum");
    assert.ok(Array.isArray(contract.over_safety_policy?.progress_phrases) && contract.over_safety_policy.progress_phrases.length > 0, "over_safety_policy requires progress phrases");
    assert.equal(contract.comprehension_master?.compression_blocked_until_approved, true, "comprehension Master must block compression until approval");
    assert.ok(contract.comprehension_master.target_duration_max_seconds >= contract.comprehension_master.target_duration_min_seconds, "comprehension Master duration range is invalid");
  }

  if (contract.diagnostic_demo) {
    const demo = contract.diagnostic_demo;
    assert.ok(Array.isArray(demo.observations) && demo.observations.length > 0, "diagnostic_demo requires observations");
    assert.ok(Array.isArray(demo.unknowns) && demo.unknowns.length > 0, "diagnostic_demo requires at least one explicit unknown");
    assert.ok(typeof demo.selected_next_check === "string" && demo.selected_next_check.trim(), "diagnostic_demo requires selected_next_check");
    assert.equal(demo.cause_assertion_requires_evidence, true, "cause assertions must require evidence");
    const unknownStages = new Set(demo.observations.filter((item) => item.evidence_state === "unknown").map((item) => item.stage));
    assert.ok(unknownStages.size > 0, "diagnostic_demo must render at least one unknown stage");
    for (const unknown of demo.unknowns) assert.ok(unknownStages.has(unknown), `diagnostic_demo unknown is not rendered as unknown: ${unknown}`);
    assert.ok(demo.unknowns.some((unknown) => demo.selected_next_check.includes(unknown) || unknown.includes(demo.selected_next_check)), "selected_next_check must come from an explicit unknown, not a declared cause");
    assert.ok(Array.isArray(demo.cause_evidence_refs), "diagnostic_demo requires cause_evidence_refs");
    if (demo.cause_conclusion !== null) {
      assert.ok(typeof demo.cause_conclusion === "string" && demo.cause_conclusion.trim(), "cause_conclusion must be a non-empty string or null");
      assert.ok(demo.cause_evidence_refs.length > 0, "a cause conclusion requires explicit evidence refs");
      for (const unknown of demo.unknowns) {
        assert.equal(demo.cause_conclusion.includes(unknown), false, "unknown evidence may select a first check, but must not assert that unknown as the cause");
      }
    }
  }

  const roles = new Set();
  let predicateBeatCount = 0;
  let previousEnd = null;
  for (const module of contract.modules) {
    assert.ok(module.id && module.role, "Every Body module requires id and role");
    assert.ok(Number.isFinite(module.start_seconds) && Number.isFinite(module.end_seconds) && module.end_seconds > module.start_seconds, `Body module ${module.id}: invalid timing`);
    if (previousEnd !== null) assert.ok(module.start_seconds >= previousEnd, `Body module ${module.id}: modules must not overlap or run backward`);
    previousEnd = module.end_seconds;
    assert.ok(module.screen?.surface && Array.isArray(module.screen.ui_labels), `Body module ${module.id}: screen surface and ui_labels are required`);
    assert.ok(typeof module.visual_action === "string" && module.visual_action.trim(), `Body module ${module.id}: visible action is required`);
    assert.ok(Number.isInteger(module.concept_count) && module.concept_count <= contract.max_concepts_per_beat, `Body module ${module.id}: concept_count exceeds contract limit`);
    assert.ok(Array.isArray(module.spoken_copy), `Body module ${module.id}: spoken_copy must be an array`);
    if (module.role !== "CTA") assert.ok(module.spoken_copy.length > 0, `Body module ${module.id}: non-CTA beat requires spoken copy`);
    if (module.spoken_copy.some((line) => PREDICATE_ENDING.test(line.trim()))) predicateBeatCount += 1;
    roles.add(module.role);
  }
  const requiredRoles = qualifiedCuriosity ? [...QUALIFIED_CURIOSITY_REQUIRED_ROLES, ...(desireArcEnabled ? ["HOPE"] : [])] : EXPLAINER_REQUIRED_ROLES;
  for (const role of requiredRoles) assert.ok(roles.has(role), `Body contract requires a ${role} module`);
  if (qualifiedCuriosity) {
    assert.ok(!roles.has("PAYOFF"), "Qualified-curiosity Body must leave the full payoff to the destination");
    assert.ok(contract.modules.filter((module) => module.role === "MECHANISM").length <= 1, "Qualified-curiosity Body allows at most one mechanism beat");
    assert.equal(Boolean(contract.diagnostic_demo), false, "Qualified-curiosity Body must not include a full diagnostic demo");
  }
  assert.ok(predicateBeatCount >= (qualifiedCuriosity ? 2 : 3), `Body cannot be a sequence of noun lists; at least ${qualifiedCuriosity ? 2 : 3} beats need a complete spoken proposition`);
  assert.equal(contract.modules.at(-1).role, "CTA", "The final Body module must be CTA");
  assert.ok(contract.modules.at(-1).end_seconds <= contract.target_duration_seconds, "Body modules exceed target duration");

  if (contract.semanticStrengthVersion === 1) {
    const viewerText = contract.modules.flatMap((module) => module.spoken_copy).join("\n");
    assert.ok(viewerText.includes(contract.aha_contract.aha_line), "Aha line must be rendered in spoken copy");
    for (const prohibited of contract.claim_ladder.prohibited_guarantees) {
      assert.equal(viewerText.includes(prohibited), false, `Body renders a prohibited guarantee: ${prohibited}`);
    }
    const progressPhrases = [...new Set([...DEFAULT_PROGRESS_PHRASES, ...contract.over_safety_policy.progress_phrases])];
    const matchedProgress = progressPhrases.filter((phrase) => viewerText.includes(phrase));
    assert.ok(matchedProgress.length >= contract.over_safety_policy.minimum_progress_phrases, "Body is over-safe: viewer value is reduced to operational work without a progress or recognition phrase");
    if (contract.comprehension_master.enabled) {
      assert.ok(contract.target_duration_seconds >= contract.comprehension_master.target_duration_min_seconds, "Comprehension Master is shorter than its approved range");
      assert.ok(contract.target_duration_seconds <= contract.comprehension_master.target_duration_max_seconds, "Comprehension Master exceeds its approved range");
      const ctaDuration = contract.modules.at(-1).end_seconds - contract.modules.at(-1).start_seconds;
      assert.ok(ctaDuration >= contract.comprehension_master.minimum_end_card_seconds, "Comprehension Master End Card is too short");
    }
    if (desireArcEnabled) {
      assert.ok(viewerText.includes(contract.hope_contract.rendered_hope_line), "The selected Territory's desired relief must be rendered as a Hope line");
      assert.ok(contract.modules.some((module) => module.role === "HOPE" && module.spoken_copy.includes(contract.hope_contract.rendered_hope_line)), "The Hope line must appear in a dedicated HOPE beat");
    }
  }

  for (const field of ["headline", "brand", "eyebrow", "button", "supporting_line", "trust_note"]) {
    assert.ok(typeof contract.cta?.[field] === "string" && contract.cta[field].trim(), `CTA ${field} is required`);
  }
  return { bodyFamilyId: contract.body_family_id, matchedHooks: contract.matched_hook_ids.length, modules: contract.modules.length };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isMain) {
  const file = process.argv[2] ? path.resolve(process.argv[2]) : null;
  assert.ok(file, "Usage: node scripts/validate-body-contract.mjs <body-contract.json>");
  const result = validateBodyContract(JSON.parse(await readFile(file, "utf8")));
  console.log(`Body contract: PASS (${result.bodyFamilyId} / ${result.matchedHooks} Hooks / ${result.modules} modules)`);
}
