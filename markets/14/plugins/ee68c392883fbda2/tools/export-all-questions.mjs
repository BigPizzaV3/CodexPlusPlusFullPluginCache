#!/usr/bin/env node
/**
 * Export every certification question bank into one combined module for the
 * MCP worker. Handles the different formats across AWS, Azure, GCP, HashiCorp,
 * Kubernetes, and Docker files.
 *
 * Output: max/cloudflare-worker/mcp-worker/data/question-bank.js
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO = join(__dirname, '..', '..', '..');

const TRACKS = [
  { id: 'terraform-associate-003', provider: 'HashiCorp', title: 'Terraform Associate (003)', examCode: 'Terraform-003', file: 'max/certifications/hashicorp/terraform-associate-003-max.html' },
  { id: 'terraform-professional', provider: 'HashiCorp', title: 'Terraform Professional', examCode: 'Terraform-Professional', file: 'max/certifications/hashicorp/terraform-professional-max.html' },
  { id: 'vault-associate-003', provider: 'HashiCorp', title: 'Vault Associate (003)', examCode: 'Vault-003', file: 'max/certifications/hashicorp/vault-associate-003-max.html' },
  { id: 'consul-associate-003', provider: 'HashiCorp', title: 'Consul Associate (003)', examCode: 'Consul-003', file: 'max/certifications/hashicorp/consul-associate-003-max.html' },
  { id: 'opentofu-practitioner', provider: 'OpenTofu', title: 'OpenTofu Practitioner', examCode: 'OpenTofu', file: 'max/certifications/hashicorp/opentofu-practitioner-max.html' },
  { id: 'aws-clf-c02', provider: 'AWS', title: 'Cloud Practitioner', examCode: 'CLF-C02', file: 'max/certifications/aws/aws-clf-c02-max.html' },
  { id: 'aws-saa-c03', provider: 'AWS', title: 'Solutions Architect Associate', examCode: 'SAA-C03', file: 'max/certifications/aws/aws-saa-c03-max.html' },
  { id: 'aws-dva-c02', provider: 'AWS', title: 'Developer Associate', examCode: 'DVA-C02', file: 'max/certifications/aws/aws-dva-c02-max.html' },
  { id: 'aws-sap-c02', provider: 'AWS', title: 'Solutions Architect Professional', examCode: 'SAP-C02', file: 'max/certifications/aws/aws-sap-c02-max.html' },
  { id: 'aws-sysops', provider: 'AWS', title: 'SysOps Administrator Associate', examCode: 'SOA-C02', file: 'max/certifications/aws/aws-cloud-sysops-practice-max.html' },
  { id: 'aws-aif-c01', provider: 'AWS', title: 'AI Practitioner', examCode: 'AIF-C01', file: 'max/certifications/aws/aws-aif-c01-max.html' },
  { id: 'azure-az900', provider: 'Azure', title: 'Azure Fundamentals', examCode: 'AZ-900', file: 'max/certifications/azure/azure-az900-max.html' },
  { id: 'azure-az104', provider: 'Azure', title: 'Azure Administrator', examCode: 'AZ-104', file: 'max/certifications/azure/azure-az104-exam-max.html' },
  { id: 'azure-az204', provider: 'Azure', title: 'Azure Developer Associate', examCode: 'AZ-204', file: 'max/certifications/azure/azure-az204-practice-max.html' },
  { id: 'azure-az305', provider: 'Azure', title: 'Azure Solutions Architect', examCode: 'AZ-305', file: 'max/certifications/azure/azure-az305-max.html' },
  { id: 'azure-az500', provider: 'Azure', title: 'Azure Security Engineer', examCode: 'AZ-500', file: 'max/certifications/azure/azure-az500-practice-max.html' },
  { id: 'azure-ai-900', provider: 'Azure', title: 'Azure AI Fundamentals', examCode: 'AI-900', file: 'max/certifications/azure/azure-ai-900-max.html' },
  { id: 'gcp-ace', provider: 'GCP', title: 'Associate Cloud Engineer', examCode: 'ACE', file: 'max/certifications/gcp/gcp-ace-max.html' },
  { id: 'gcp-pca', provider: 'GCP', title: 'Professional Cloud Architect', examCode: 'PCA', file: 'max/certifications/gcp/gcp-pca-max.html' },
  { id: 'gcp-gen-ai', provider: 'GCP', title: 'Generative AI', examCode: 'GCP-AI', file: 'max/certifications/gcp/gcp-gen-ai-max.html' },
  { id: 'kubernetes-cka', provider: 'CNCF', title: 'Certified Kubernetes Administrator', examCode: 'CKA', file: 'max/certifications/kubernetes/kubernetes-cka-max.html' },
  { id: 'kubernetes-ckad', provider: 'CNCF', title: 'Certified Kubernetes Application Developer', examCode: 'CKAD', file: 'max/certifications/kubernetes/kubernetes-ckad-max.html' },
  { id: 'docker-dca', provider: 'Docker', title: 'Docker Certified Associate', examCode: 'DCA', file: 'max/certifications/docker/docker-dca-max.html' },
  { id: 'docker-fundamentals', provider: 'Docker', title: 'Docker Fundamentals', examCode: 'Docker', file: 'max/certifications/docker/docker-fundamentals-max.html' }
];

function slugify(s) {
  return String(s).toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'general';
}

function findMatchingBracket(str, start, open, close) {
  let depth = 0;
  let inStr = null;
  let inLine = false;
  let inBlock = false;
  for (let i = start; i < str.length; i++) {
    const c = str[i];
    const n = str[i + 1];
    if (inLine) { if (c === '\n') inLine = false; continue; }
    if (inBlock) { if (c === '*' && n === '/') { inBlock = false; i++; } continue; }
    if (inStr) { if (c === '\\') { i++; continue; } if (c === inStr) inStr = null; continue; }
    if (c === '/' && n === '/') { inLine = true; i++; continue; }
    if (c === '/' && n === '*') { inBlock = true; i++; continue; }
    if (c === '"' || c === "'" || c === '`') { inStr = c; continue; }
    if (c === open) depth++;
    else if (c === close) { depth--; if (depth === 0) return i; }
  }
  return -1;
}

function extractQuestions(html) {
  const re = /(?:const|let|var)\s+([A-Za-z0-9_]+)\s*=\s*([\[{])/g;
  const candidates = [];
  let m;
  while ((m = re.exec(html))) {
    if (!/question/i.test(m[1])) continue;
    candidates.push(m);
  }
  // Prefer the variable exactly named "questions" over names like
  // QUESTIONS_PER_MODULE or serviceQuestions.
  candidates.sort((a, b) => Number(!/^questions$/i.test(a[1])) - Number(!/^questions$/i.test(b[1])));
  for (const m of candidates) {
    const open = m[2];
    const start = m.index + m[0].length - 1;
    const close = open === '[' ? ']' : '}';
    const end = findMatchingBracket(html, start, open, close);
    if (end === -1) continue;
    const literal = html.slice(start, end + 1);
    try {
      const val = Function('return (' + literal + ');')();
      if (val && (Array.isArray(val) || typeof val === 'object')) return val;
    } catch {
      // try the next candidate
    }
  }
  return null;
}

function normalizeQuestion(q) {
  const text = q.text || q.question || q.q || q.prompt || null;
  if (!text) return null;
  let options = q.options || q.choices || q.answers || [];
  if (!Array.isArray(options) || options.length < 2) return null;
  options = options.map((o) => String(o).replace(/^[A-E][.)]\s*/, '').trim());

  let correct = -1;
  for (const key of ['correct', 'answer', 'correctIndex', 'answerIndex']) {
    const v = q[key];
    if (typeof v === 'number') { correct = v; break; }
    if (typeof v === 'string') {
      const t = v.trim();
      if (/^[A-Ea-e]$/.test(t)) { correct = t.toUpperCase().charCodeAt(0) - 65; break; }
      if (/^\d+$/.test(t)) { correct = parseInt(t, 10); break; }
    }
  }
  if (correct < 0 || correct >= options.length) return null;

  const explanation = q.explanation || q.explain || q.reason || q.feedback || '';
  return { question: text, options, correct, explanation };
}

function buildDomainsFromArray(arr) {
  const grouped = new Map();
  for (const q of arr) {
    const d = (q.domain && String(q.domain).trim()) || 'General';
    if (!grouped.has(d)) grouped.set(d, []);
    grouped.get(d).push(q);
  }
  const domains = [];
  for (const [title, qs] of grouped) {
    const norm = qs.map(normalizeQuestion).filter(Boolean);
    if (norm.length) domains.push({ key: slugify(title), title, questions: norm });
  }
  return domains;
}

function buildTrack(track, data) {
  let domains;
  if (Array.isArray(data)) {
    domains = buildDomainsFromArray(data);
  } else {
    domains = [];
    for (const [key, arr] of Object.entries(data)) {
      if (Array.isArray(arr)) {
        const norm = arr.map(normalizeQuestion).filter(Boolean);
        if (norm.length) domains.push({ key: slugify(key), title: key, questions: norm });
      }
    }
  }
  if (!domains.length) return null;
  let n = 0;
  for (const d of domains) {
    d.questions = d.questions.map((q, i) => ({ id: `${track.id}:${d.key}:${i}`, ...q }));
    n += d.questions.length;
  }
  return { id: track.id, provider: track.provider, title: track.title, examCode: track.examCode, domains, totalQuestions: n };
}

// GCP service quizzes (each file is one domain).
const GCP_DIR = join(REPO, 'max/certifications/gcp');
let gcpQuizzes = [];
try {
  gcpQuizzes = readdirSync(GCP_DIR).filter((f) => /Quiz-max\.html$/i.test(f));
} catch {
  gcpQuizzes = [];
}

const bank = { tracks: [] };
const seenIds = new Set();
for (const t of TRACKS) {
  let html;
  try { html = readFileSync(join(REPO, t.file), 'utf8'); } catch { continue; }
  const data = extractQuestions(html);
  if (!data) continue;
  const track = buildTrack(t, data);
  if (track) { bank.tracks.push(track); seenIds.add(t.id); }
}

// Aggregate GCP service quizzes.
const gcpDomains = [];
for (const f of gcpQuizzes.sort()) {
  let html;
  try { html = readFileSync(join(GCP_DIR, f), 'utf8'); } catch { continue; }
  const data = extractQuestions(html);
  if (!data) continue;
  const title = f.replace(/-max\.html$/i, '').replace(/_/g, ' ').replace(/Quiz$/i, '').trim();
  const domains = Array.isArray(data) ? buildDomainsFromArray(data) : buildTrack({ id: 'gcp-' + slugify(title) }, data)?.domains || [];
  for (const d of domains) {
    const domKey = slugify(title + (domains.length > 1 ? '-' + d.title : ''));
    d.key = domKey;
    d.title = title + (domains.length > 1 ? ': ' + d.title : '');
    d.questions = d.questions.map((q, i) => ({ ...q, id: `gcp-service-quizzes:${domKey}:${i}` }));
    gcpDomains.push(d);
  }
}
if (gcpDomains.length) {
  bank.tracks.push({
    id: 'gcp-service-quizzes',
    provider: 'GCP',
    title: 'GCP Service Quizzes',
    examCode: 'GCP',
    domains: gcpDomains,
    totalQuestions: gcpDomains.reduce((s, d) => s + d.questions.length, 0)
  });
}

const OUT = join(REPO, 'max/cloudflare-worker/mcp-worker/data/question-bank.js');
mkdirSync(dirname(OUT), { recursive: true });
writeFileSync(OUT, `// Generated by tools/export-all-questions.mjs. Do not edit by hand.\nexport const QUESTION_BANK = ${JSON.stringify(bank, null, 2)};\n`, 'utf8');

const total = bank.tracks.reduce((s, t) => s + t.totalQuestions, 0);
console.log(`Wrote ${bank.tracks.length} tracks / ${total} questions to ${OUT}`);
for (const t of bank.tracks) {
  console.log(`  ${t.id} (${t.provider}): ${t.totalQuestions} questions, ${t.domains.length} domains`);
}
