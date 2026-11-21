#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as model from './policy-model.mjs';

export function markdown(doc) {
  const lines = [`# ${doc.title}`, '', `**${doc.subtitle}**`, doc.preparedLine, '',
    `**${doc.postureLabel}.** ${doc.postureSummary}`, '', `> ${doc.disclaimer}`, ''];
  const cell = v => String(v).replace(/\|/g, '\\|').replace(/[\r\n]+/g, ' ');
  for (const section of doc.sections) {
    lines.push(`## ${section.number.startsWith('Appendix') ? section.number + ':' : section.number + '.'} ${section.heading}`, '');
    for (const block of section.blocks) {
      if (block.type === 'p') lines.push(block.text, '');
      else if (block.type === 'note') lines.push(`> ${block.text}`, '');
      else if (block.type === 'bullets') lines.push(...block.items.map(s => `- ${s}`), '');
      else if (block.type === 'numbered') lines.push(...block.items.map((s,i) => `${i+1}. ${s}`), '');
      else if (block.type === 'table') {
        lines.push(`| ${block.header.map(cell).join(' | ')} |`, `| ${block.header.map(()=>'---').join(' | ')} |`,
          ...block.rows.map(row=>`| ${row.map(cell).join(' | ')} |`), '');
      }
    }
  }
  lines.push('# Questions your board will ask about AI in fundraising', '');
  doc.boardQuestions.forEach((q,i)=>lines.push(`## ${i+1}. ${q.q}`, '', `*Why they ask:* ${q.why}`, '', q.answer, ''));
  lines.push(`> ${doc.disclaimer}`, '');
  return lines.join('\n');
}

export function decisions(input) {
  return [
    ...(input.sensitiveHandling==='undecided' ? ['Decide whether any sensitive data category may be handled inside an approved platform. Starting rule: sensitive categories excluded.'] : []),
    ...(input.autonomy==='undecided' ? ['Decide whether routine low-risk steps may run under standing approval. Starting posture: draft-only.'] : []),
    ...(input.disclosure==='undecided' ? ['Confirm or change the disclosure rule. Starting rule: disclose when AI produced the substance.'] : []),
  ];
}

function run() {
  const args = process.argv.slice(2);
  if (args.length===1 && args[0]==='--schema') {
    console.log(JSON.stringify(Object.fromEntries([
      ['orgType',model.ORG_TYPES],['revenueBand',model.REVENUE_BANDS],['authorRole',model.AUTHOR_ROLES],
      ['dataScope',model.DATA_CATEGORIES],['sensitiveHandling',model.SENSITIVE_HANDLING],['workflows',model.WORKFLOWS],
      ['autonomy',model.AUTONOMY],['approver',model.APPROVERS],['staffReview',model.STAFF_REVIEWS],
      ['disclosure',model.DISCLOSURES],['vendorRequirements',model.VENDOR_REQUIREMENTS],['reviewCadence',model.REVIEW_CADENCES],
    ]),null,2)); return;
  }
  const flags = new Map();
  for (let i=0;i<args.length;i+=2) {
    if (!['--input','--out-dir','--date'].includes(args[i]) || !args[i+1] || flags.has(args[i])) throw new Error('Usage: node build-policy.mjs --input answers.json --out-dir output --date YYYY-MM-DD');
    flags.set(args[i],args[i+1]);
  }
  if (!flags.has('--input') || !flags.has('--out-dir') || !flags.has('--date')) throw new Error('Input, output directory, and preparation date are required.');
  const dateText=flags.get('--date');
  if (!/^\d{4}-\d{2}-\d{2}$/.test(dateText)) throw new Error('Use a calendar date in YYYY-MM-DD format.');
  const date=new Date(`${dateText}T12:00:00Z`);
  if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0,10)!==dateText) throw new Error('The preparation date is not a valid calendar date.');
  const raw = JSON.parse(fs.readFileSync(flags.get('--input'),'utf8'));
  const allowed=new Set(['version','orgType','revenueBand','authorRole','dataScope','sensitiveHandling','workflows','autonomy','approver','staffReview','disclosure','vendorRequirements','reviewCadence']);
  if (raw && typeof raw==='object' && Object.keys(raw).some(k=>!allowed.has(k))) throw new Error('Answer files may contain only the documented policy choice fields. Remove personal records and unrecognized fields.');
  const parsed=model.parsePolicyInput(raw);
  if (!parsed.ok) throw new Error(parsed.error);
  const doc=model.buildPolicy(parsed.input,date);
  const out=path.resolve(flags.get('--out-dir'));
  const names=['policy.md','policy.json','board-questions.md','board-decisions.md'];
  for (const name of names) if (fs.existsSync(path.join(out,name))) throw new Error('Output files already exist. Choose a new output directory to preserve the previous draft.');
  fs.mkdirSync(out,{recursive:true});
  fs.writeFileSync(path.join(out,'policy.md'),markdown(doc));
  fs.writeFileSync(path.join(out,'policy.json'),JSON.stringify(doc,null,2)+'\n');
  fs.writeFileSync(path.join(out,'board-questions.md'),['# Questions your board will ask about AI in fundraising','',
    ...doc.boardQuestions.flatMap((q,i)=>[`## ${i+1}. ${q.q}`,'',`*Why they ask:* ${q.why}`,'',q.answer,'']),`> ${doc.disclaimer}`,''].join('\n'));
  const open=decisions(parsed.input);
  fs.writeFileSync(path.join(out,'board-decisions.md'),['# Decisions for board review','',doc.postureLabel,'',
    ...(open.length ? open.map(s=>`- ${s}`) : ['No undecided sensitive-data, autonomy, or disclosure choices were selected. The policy still requires board and counsel review before adoption.']),
    '', 'Adoption date, named policy owner, next review date, and actual vendor confirmations remain to be completed by the organization.',''].join('\n'));
  console.log(JSON.stringify({ok:true,outputDirectory:out,files:names,posture:doc.postureLabel,openDecisions:open},null,2));
}

if (process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url)) {
  try { run(); } catch (error) { console.error(error.message); process.exitCode=2; }
}
