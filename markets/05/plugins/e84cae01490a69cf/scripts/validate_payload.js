#!/usr/bin/env node

// Standalone validator for the JSON copied into the Onboarding Wins app.
// Usage: node validate_payload.js payload.json

const fs = require('fs');

function readPayload() {
  const file = process.argv[2];
  const raw = file ? fs.readFileSync(file, 'utf8') : fs.readFileSync(0, 'utf8');
  return raw.replace(/^\uFEFF/, '').replace(/[\u00a0\u2028\u2029\u202f]/g, ' ').replace(/[\u200b-\u200d\u2060]/g, '').replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();
}

function unknown(value) {
  return value === null || value === undefined || (typeof value === 'string' && /^(|null|n\/a|na|unknown|not found|no encontrado|no disponible|sin datos)$/i.test(value.trim()));
}

function normalizeNumber(value) {
  if (unknown(value)) return { value: null, warning: 'missing' };
  if (typeof value === 'number') return Number.isFinite(value) ? { value } : { value: null, warning: 'not-finite' };
  const raw = String(value).trim();
  const match = raw.replace(/,/g, '').match(/\d+(?:\.\d+)?(?:\s*[kmb])?/i);
  if (!match) return { value: null, warning: `could-not-parse: ${raw}` };
  const token = match[0].replace(/\s/g, '').toLowerCase();
  let number = Number(token.replace(/[kmb]$/, ''));
  const suffix = token.slice(-1);
  if (suffix === 'k') number *= 1000;
  if (suffix === 'm') number *= 1000000;
  if (suffix === 'b') number *= 1000000000;
  return Number.isFinite(number) ? { value: number, normalizedFrom: raw } : { value: null, warning: `not-finite: ${raw}` };
}

function first(...values) {
  return values.find(value => !unknown(value));
}

function main() {
  const errors = [];
  const warnings = [];
  let parsed;
  try { parsed = JSON.parse(readPayload()); } catch (error) {
    console.log(JSON.stringify({ ok: false, errors: ['Invalid JSON. Paste only the JSON object.'], warnings }, null, 2));
    process.exitCode = 1;
    return;
  }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) errors.push('Root must be an object.');
  const client = parsed.client || parsed.customer || parsed.account || parsed;
  const metrics = client.metricas_y_datos_cliente || parsed.metricas_y_datos_cliente || client.metrics || parsed.metrics || {};
  const salesforce = client.salesforce || parsed.salesforce || {};
  const view360 = client.view360 || parsed.view360 || client.view_360 || parsed.view_360 || {};
  const account = String(client.accountName || client.name || parsed.cuenta || '').trim();
  if (!account) errors.push('Missing client.accountName or cuenta.');
  if (!String(client.owner || parsed.onboarding_csm || '').trim()) warnings.push('Owner is missing.');
  const arr = normalizeNumber(first(client.arr, client.arr_usd, metrics.arr, metrics.arr_usd, salesforce.arr, salesforce.arr_usd, view360.arr, view360.arr_usd));
  const agents = normalizeNumber(first(client.agents, client.agents_count, metrics.agents, metrics.agentes, metrics.agents_count, salesforce.agents, salesforce.agents_count, view360.agents, view360.agents_count));
  if (arr.warning) warnings.push(`ARR: ${arr.warning}. Use a number or null.`);
  if (agents.warning) warnings.push(`Agents: ${agents.warning}. Use an integer or null.`);
  const subscription = first(client.subscription, client.suscripcion, metrics.subscription, metrics.suscripcion, salesforce.subscription, view360.subscription);
  if (unknown(subscription)) warnings.push('Subscription is not verified.');
  for (const key of ['sessions', 'milestones', 'steps', 'timeline']) if (!Array.isArray(parsed[key])) errors.push(`${key} must be an array.`);
  const calls = Number(first(client.calls, metrics.llamadas_gong_encontradas, metrics.calls));
  const emails = Number(first(client.emails, metrics.correos_gmail_encontrados, metrics.emails));
  if (!Number.isInteger(calls) || calls < 0) warnings.push('Calls should be a non-negative integer.');
  if (!Number.isInteger(emails) || emails < 0) warnings.push('Emails should be a non-negative integer.');
  const expansion = client.expansion || {};
  if (expansion.additionalAgents && !Number.isInteger(normalizeNumber(expansion.additionalAgents).value)) warnings.push('Expansion additionalAgents should be an integer.');
  const result = { ok: errors.length === 0, errors, warnings, normalized: { accountName: account, arr: arr.value, agents: agents.value, subscription: subscription || null, calls: Number.isInteger(calls) ? calls : null, emails: Number.isInteger(emails) ? emails : null } };
  console.log(JSON.stringify(result, null, 2));
  if (!result.ok) process.exitCode = 1;
}

main();
