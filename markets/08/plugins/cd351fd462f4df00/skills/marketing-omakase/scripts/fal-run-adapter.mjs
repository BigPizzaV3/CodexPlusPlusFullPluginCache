import assert from 'node:assert/strict';
import { constants } from 'node:fs';
import { lstat, mkdir, open, readFile, rename } from 'node:fs/promises';
import path from 'node:path';
import { payloadHash } from './run-contract.mjs';

export async function durableJson(file, value) {
  const tmp = `${file}.tmp`;
  const handle = await open(tmp, constants.O_WRONLY | constants.O_CREAT | constants.O_EXCL | constants.O_NOFOLLOW, 0o600);
  try { await handle.writeFile(`${JSON.stringify(value, null, 2)}\n`); await handle.sync(); } finally { await handle.close(); }
  await rename(tmp, file);
  const directory = await open(path.dirname(file), 'r');
  try { await directory.sync(); } finally { await directory.close(); }
}
async function readJournal(file) {
  try {
    assert.ok((await lstat(file)).isFile() && !(await lstat(file)).isSymbolicLink(), 'journal must be regular file');
    return JSON.parse(await readFile(file, 'utf8'));
  } catch (error) { if (error.code === 'ENOENT') return null; throw error; }
}
export function queueUrl(endpoint, requestId, operation) {
  assert.match(endpoint, /^fal-ai\/[a-zA-Z0-9_-]+(?:\/[a-zA-Z0-9_-]+)*$/);
  if (!requestId) return `https://queue.fal.run/${endpoint}`;
  assert.match(requestId, /^[a-zA-Z0-9_-]{1,160}$/);
  return `https://queue.fal.run/${endpoint}/requests/${requestId}${operation === 'status' ? '/status' : ''}`;
}
export function falTransport({ credential, fetchImpl = fetch, timeoutMs = 30_000 }) {
  assert.ok(typeof credential === 'string' && credential.length >= 20, 'local fal credential required');
  assert.ok(timeoutMs > 0 && timeoutMs <= 60_000);
  return async (method, url, body) => {
    const parsed = new URL(url);
    assert.equal(parsed.origin, 'https://queue.fal.run');
    const response = await fetchImpl(url, { method, redirect: 'error', signal: AbortSignal.timeout(timeoutMs), headers: { Authorization: `Key ${credential}`, 'Content-Type': 'application/json' }, ...(body === undefined ? {} : { body: JSON.stringify(body) }) });
    // No implicit retry: every POST response failure remains ambiguous.
    assert.ok(response.ok, `fal HTTP ${response.status}`);
    return response.json();
  };
}
export function supportedPricingQuantity(request) {
  // Explicit profiles only. Never infer an unknown endpoint's billing from generic field names.
  if (request.model === 'fal-ai/kling-video/v3/pro/text-to-video') {
    assert.equal(request.currency, 'USD', 'unsupported profile currency');
    assert.equal(request.pricing?.sourceUrl, 'https://fal.ai/models/fal-ai/kling-video/v3/pro/text-to-video', 'pricing source does not match profile');
    assert.ok(request.pricing?.unitPriceMicros >= 112000, 'quote below verified audio-off per-second price');
    const input = request.payload;
    // Fix all options explicitly: default generate_audio=true is a more expensive route.
    assert.deepEqual(Object.keys(input).sort(), ['aspect_ratio', 'cfg_scale', 'duration', 'generate_audio', 'negative_prompt', 'prompt', 'shot_type']);
    assert.ok(typeof input.prompt === 'string' && input.prompt.trim() && input.prompt.length <= 2500, 'bounded single prompt required');
    assert.equal(input.duration, '5', 'profile supports exactly five seconds');
    assert.equal(input.generate_audio, false, 'profile supports audio off only');
    assert.equal(input.aspect_ratio, '9:16', 'profile supports portrait only');
    assert.equal(input.shot_type, 'customize', 'profile excludes automatic multi-shot generation');
    assert.equal(input.negative_prompt, 'blur, distort, and low quality');
    assert.equal(input.cfg_scale, 0.5);
    return 5; // One video, five billed seconds; no resolution/voice/multi-output options.
  }
  assert.equal(request.model, 'fal-ai/flux/schnell', 'unsupported fal pricing profile');
  assert.equal(request.currency, 'USD', 'unsupported profile currency');
  assert.equal(request.pricing?.sourceUrl, 'https://fal.ai/models/fal-ai/flux/schnell', 'pricing source does not match profile');
  assert.ok(request.pricing?.unitPriceMicros >= 3000, 'quote below verified rounded-megapixel price');
  const input = request.payload;
  const allowed = new Set(['prompt', 'image_size', 'num_images', 'num_inference_steps', 'seed', 'guidance_scale', 'sync_mode', 'enable_safety_checker', 'output_format', 'acceleration']);
  assert.ok(Object.keys(input).every(k => allowed.has(k)), 'unsupported profile option');
  assert.ok(typeof input.prompt === 'string' && input.prompt.trim());
  assert.ok(input.image_size && typeof input.image_size === 'object' && !Array.isArray(input.image_size), 'profile requires explicit pixel dimensions; preset/default pricing is unsupported');
  assert.deepEqual(Object.keys(input.image_size).sort(), ['height', 'width']);
  for (const value of Object.values(input.image_size)) assert.ok(Number.isSafeInteger(value) && value >= 64 && value <= 4096 && value % 8 === 0, 'unsupported profile dimensions');
  assert.ok(Number.isSafeInteger(input.num_images) && input.num_images >= 1 && input.num_images <= 4, 'explicit supported output count required');
  if (input.num_inference_steps !== undefined) assert.ok(Number.isInteger(input.num_inference_steps) && input.num_inference_steps >= 1 && input.num_inference_steps <= 4);
  if (input.guidance_scale !== undefined) assert.ok(Number.isFinite(input.guidance_scale) && input.guidance_scale >= 0 && input.guidance_scale <= 20);
  if (input.seed !== undefined) assert.ok(Number.isSafeInteger(input.seed));
  if (input.sync_mode !== undefined) assert.equal(input.sync_mode, false, 'history-preserving queue result required');
  if (input.enable_safety_checker !== undefined) assert.equal(input.enable_safety_checker, true);
  if (input.output_format !== undefined) assert.ok(['jpeg', 'png'].includes(input.output_format));
  if (input.acceleration !== undefined) assert.equal(input.acceleration, 'none', 'unreviewed acceleration option');
  return Math.ceil(input.image_size.width * input.image_size.height / 1_000_000) * input.num_images;
}
function validateRequest(request) {
  assert.equal(request.provider, 'fal'); queueUrl(request.model);
  assert.match(request.currency, /^[A-Z]{3}$/);
  assert.ok(Number.isSafeInteger(request.maxCostMicros) && request.maxCostMicros > 0 && request.maxCostMicros <= 2_000_000_000);
  assert.ok(Number.isFinite(request.quantity) && request.quantity > 0 && request.quantity <= 10000);
  assert.ok(request.payload && typeof request.payload === 'object' && !Array.isArray(request.payload));
  assert.equal(request.payloadHash, payloadHash(request.payload), 'provider payload hash mismatch');
  assert.ok(Buffer.byteLength(JSON.stringify(request.payload)) <= 1_000_000, 'provider payload too large');
  assert.equal(request.quantity, supportedPricingQuantity(request), 'reserved quantity must equal the profile billing units');
  assert.equal(request.pricing?.basis, 'fixed_unit');
  assert.ok(request.pricing.unitPriceMicros > 0 && Number.isSafeInteger(request.pricing.unitPriceMicros));
  assert.ok(request.maxCostMicros >= Math.ceil(request.pricing.unitPriceMicros * request.quantity), 'unit cost exceeds reservation');
  assert.ok(['fal.ai', 'api.fal.ai'].includes(new URL(request.pricing.sourceUrl).hostname));
}
export function validatePermit(permit, context, request, spendId) {
  for (const [key, value] of Object.entries({ spendId, runId: context.runId, scopeRevision: context.scopeRevision, stepId: context.stepId, fencingToken: context.fencingToken, payloadHash: request.payloadHash, provider: request.provider, model: request.model, currency: request.currency, maxCostMicros: request.maxCostMicros, quantity: request.quantity })) assert.equal(permit?.[key], value, `permit mismatch: ${key}`);
  assert.ok(Date.parse(permit.expiresAt) > Date.now(), 'submission permit expired');
}
/** Host/custom paid routes must call this same adapter; no function evaluates source text. */
export async function runFal({ journalPath, projectId, context, request, callQuality, transport, dryRun = true }) {
  validateRequest(request);
  assert.ok(context.operationId?.length >= 8 && context.operationId.length <= 90 && /^[A-Za-z0-9_-]+$/.test(context.operationId), 'safe operationId required before journaling');
  assert.ok(typeof context.leaseToken === 'string' && /^[0-9a-f-]{36}$/i.test(context.leaseToken), 'local execution lease token required');
  if (dryRun) return { status: 'dry_run', payloadHash: request.payloadHash, provider: request.provider, model: request.model, maxCostMicros: request.maxCostMicros, currency: request.currency, quantity: request.quantity };
  assert.equal(typeof callQuality, 'function'); assert.equal(typeof transport, 'function');
  const lockPath = `${journalPath}.lock`;
  await mkdir(lockPath, { mode: 0o700 });
  try {
    let journal = await readJournal(journalPath);
    const identity = payloadHash({ projectId, runId: context.runId, scopeRevision: context.scopeRevision, stepId: context.stepId, operationId: context.operationId, request });
    if (journal) assert.equal(journal.identity, identity, 'journal belongs to different scope/payload; never resubmit');
    else {
      journal = { schemaVersion: 1, identity, context, status: 'prepared', createdAt: new Date().toISOString() };
      await durableJson(journalPath, journal);
    }
    const persist = async changes => { Object.assign(journal, changes); await durableJson(journalPath, journal); };
    const call = (name, extra, phase) => callQuality(name, { projectId, ...context, operationId: `${context.operationId}_${phase}`, ...extra });
    const reconcile = async (state, evidence) => call('reconcileMarketingRunSpend', { input: { spendId: journal.spendId, state, ...(journal.requestId ? { requestId: journal.requestId } : {}), actualCostMicros: null, evidence } }, state);
    if (['submitting', 'submission_unknown'].includes(journal.status)) {
      await persist({ status: 'submission_unknown' });
      await reconcile('submission_unknown', 'No durable request ID after a submission attempt; reservation held; manual provider reconciliation required.');
      return { status: 'submission_unknown', spendId: journal.spendId };
    }
    if (journal.status === 'prepared') {
      const { payload, ...input } = request;
      const reserve = await call('reserveMarketingRunSpend', { input }, 'reserve');
      assert.ok(reserve.spendId && reserve.currency === request.currency && reserve.maxCostMicros === request.maxCostMicros, 'invalid reservation');
      await persist({ status: 'reserved', spendId: reserve.spendId });
    }
    if (journal.status === 'reserved') {
      const age = Date.now() - Date.parse(request.pricing.checkedAt);
      assert.ok(age >= -60_000 && age <= 86_400_000, 'refresh pricing before execution');
      // Persist before begin: a crash after the one-shot permit is consumed must never resend.
      await persist({ status: 'submitting', submitAttemptedAt: new Date().toISOString() });
      try {
        const begun = await call('beginMarketingRunSpend', { spendId: journal.spendId, payloadHash: request.payloadHash }, 'begin');
        assert.equal(begun.status, 'submitting', 'invalid begin status');
        validatePermit(begun.permit, context, request, journal.spendId);
        const submitted = await transport('POST', queueUrl(request.model), request.payload);
        assert.match(submitted.request_id ?? '', /^[a-zA-Z0-9_-]{1,160}$/);
        await persist({ status: 'submitted', requestId: submitted.request_id });
      } catch {
        await persist({ status: 'submission_unknown' });
        await reconcile('submission_unknown', 'Submission attempt has no durable request ID; no automatic retry or budget release.');
        return { status: 'submission_unknown', spendId: journal.spendId };
      }
    }
    assert.ok(journal.requestId, 'journal missing provider request ID');
    if (journal.status === 'completed' || journal.status === 'failed') {
      await reconcile(journal.status, 'Provider result recorded locally; actual cost remains unverified.');
      return { status: journal.status, requestId: journal.requestId, result: journal.result, spendId: journal.spendId };
    }
    await reconcile('submitted', 'Provider request ID durably recorded; resume this ID only.');
    const state = await transport('GET', queueUrl(request.model, journal.requestId, 'status'));
    if (state.status === 'IN_QUEUE' || state.status === 'IN_PROGRESS') return { status: state.status, requestId: journal.requestId, spendId: journal.spendId };
    assert.equal(state.status, 'COMPLETED', 'unknown provider status; retain reservation');
    if (state.error) {
      await persist({ status: 'failed' });
      await reconcile('failed', 'Provider reported request failure; actual cost is unknown, reservation is held.');
      return { status: 'failed', requestId: journal.requestId, spendId: journal.spendId };
    }
    const result = await transport('GET', queueUrl(request.model, journal.requestId, 'result'));
    await persist({ status: 'completed', result });
    await reconcile('completed', 'Provider result recorded locally; actual cost remains unverified.');
    return { status: 'completed', requestId: journal.requestId, result, spendId: journal.spendId };
  } finally {
    // A process crash leaves the lock. Inspect the journal and verify no live executor before removing it.
    await (await import('node:fs/promises')).rmdir(lockPath);
  }
}
