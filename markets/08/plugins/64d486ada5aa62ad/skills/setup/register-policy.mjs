import { createHash, randomUUID } from 'node:crypto';
import { readFile, lstat, realpath, open, rename, unlink } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { homedir } from 'node:os';
import { pathToFileURL } from 'node:url';

const policies = {
  local: { start: '<!-- BEGIN REMNANT TASK USAGE v1 -->', end: '<!-- END REMNANT TASK USAGE v1 -->', file: './usage-policy.md' },
  central: { start: '<!-- BEGIN REMNANT CENTRAL USAGE v1 -->', end: '<!-- END REMNANT CENTRAL USAGE v1 -->', file: './central-usage-policy.md' },
};
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const missing = error => error.code === 'ENOENT';
async function readSafe(path) {
  try {
    const stat = await lstat(path);
    if (!stat.isFile() || stat.isSymbolicLink() || stat.nlink !== 1 || stat.size > 24000) throw Error('UNSAFE_OR_OVERSIZED_INSTRUCTIONS');
    const bytes = await readFile(path);
    const text = bytes.toString('utf8');
    if (!Buffer.from(text).equals(bytes)) throw Error('INSTRUCTIONS_MUST_BE_UTF8');
    return { bytes, text, mode: stat.mode & 0o777 };
  } catch (error) { if (missing(error)) return { bytes: Buffer.alloc(0), text: '', mode: 0o600 }; throw error; }
}
async function plan(action, codexHome, policy = 'local') {
  if (!['enable', 'disable'].includes(action)) throw Error('ACTION_MUST_BE_ENABLE_OR_DISABLE');
  if (!Object.hasOwn(policies, policy)) throw Error('UNKNOWN_POLICY');
  const { start, end, file } = policies[policy];
  const rule = (await readFile(new URL(file, import.meta.url), 'utf8')).trimEnd();
  const root = await realpath(resolve(codexHome ?? process.env.CODEX_HOME ?? join(homedir(), '.codex')));
  if (!(await lstat(root)).isDirectory()) throw Error('CODEX_HOME_MUST_EXIST');
  const override = join(root, 'AGENTS.override.md');
  const overridden = await readSafe(override);
  let target = overridden.text.length ? override : join(root, 'AGENTS.md');
  const normal = await readSafe(join(root, 'AGENTS.md'));
  if (overridden.text.includes(start) && normal.text.includes(start)) throw Error('MANAGED_RULE_IN_MULTIPLE_FILES_REVIEW_REQUIRED');
  if (action === 'disable' && !overridden.text.includes(start) && normal.text.includes(start)) target = join(root, 'AGENTS.md');
  if (action === 'enable' && target === override && normal.text.includes(start)) throw Error('MANAGED_RULE_IN_INACTIVE_FILE_DISABLE_BEFORE_MOVING');
  const current = target === override ? overridden : normal;
  const a = current.text.indexOf(start), b = current.text.indexOf(end);
  let proposed = current.text;
  if (a !== -1 || b !== -1) {
    if (a < 0 || b < a || current.text.indexOf(start, a + 1) !== -1 || current.text.indexOf(end, b + 1) !== -1
        || current.text.slice(a, b + end.length).replaceAll('\r\n', '\n') !== rule.replaceAll('\r\n', '\n')) throw Error('MANAGED_RULE_CONFLICT_REVIEW_REQUIRED');
    if (action === 'disable') proposed = current.text.slice(0, a > 0 && current.text[a - 1] === '\n' ? a - 1 : a) + current.text.slice(b + end.length);
  } else if (action === 'enable') proposed += '\n' + rule;
  if (Buffer.byteLength(proposed) > 24000) throw Error('GLOBAL_INSTRUCTION_BUDGET_EXCEEDED');
  const change = { schemaVersion: 1, action, policy, target, currentSha256: hash(current.bytes), ruleSha256: hash(rule), proposedSha256: hash(proposed), changed: proposed !== current.text };
  return { root, current, proposed, change: { ...change, previewDigest: hash(JSON.stringify(change)) } };
}
export async function preview(action, codexHome, policy = 'local') { return (await plan(action, codexHome, policy)).change; }
/** Read-only upgrade check. Never creates a rule, connection, consent or upload. */
export async function status(codexHome) {
  const result = {};
  for (const policy of Object.keys(policies)) {
    const p = await preview('enable', codexHome, policy);
    result[policy] = { enabled: !p.changed, target: p.target, ruleSha256: p.ruleSha256 };
  }
  return { schemaVersion: 1, policies: result, connectionChanged: false, uploadAuthorized: false,
    sessionReload: 'Start a fresh host session after installation, update or instruction changes' };
}
export async function apply({ action, codexHome, acceptDigest, policy = 'local' }) {
  if (!/^[a-f0-9]{64}$/.test(acceptDigest ?? '')) throw Error('EXPLICIT_ACCEPTED_PREVIEW_REQUIRED');
  const first = await plan(action, codexHome, policy);
  const lockPath = join(first.root, '.remnant-usage-policy.lock');
  const lock = await open(lockPath, 'wx', 0o600);
  let tmp;
  try {
    const p = await plan(action, codexHome, policy);
    if (p.change.previewDigest !== acceptDigest) throw Error('PREVIEW_CHANGED_REVIEW_REQUIRED');
    if (!p.change.changed) return { ...p.change, status: 'unchanged' };
    tmp = join(p.root, '.remnant-usage-' + randomUUID() + '.tmp');
    const f = await open(tmp, 'wx', p.current.mode);
    try { await f.writeFile(p.proposed, 'utf8'); await f.sync(); } finally { await f.close(); }
    if ((await preview(action, codexHome, policy)).previewDigest !== acceptDigest) throw Error('PREVIEW_CHANGED_REVIEW_REQUIRED');
    await rename(tmp, p.change.target); tmp = undefined;
    return { ...p.change, status: action === 'enable' ? 'enabled' : 'disabled', freshSessionRequired: true };
  } finally {
    if (tmp) await unlink(tmp).catch(() => {});
    await lock.close(); await unlink(lockPath);
  }
}
if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  try {
    const [command, ...args] = process.argv.slice(2);
    let policy = 'local';
    const policyFlag = args.indexOf('--policy');
    if (policyFlag !== -1) {
      if (policyFlag !== args.length - 2) throw Error('POLICY_FLAG_MUST_BE_LAST');
      policy = args[policyFlag + 1]; args.splice(policyFlag, 2);
    }
    let result;
    if (command === 'status' && !args.length) result = await status();
    else if (command === 'preview' && args.length === 1) result = await preview(args[0], undefined, policy);
    else if (['enable', 'disable'].includes(command) && args.length === 2 && args[0] === '--accept-digest') result = await apply({ action: command, acceptDigest: args[1], policy });
    else throw Error('USAGE: status OR preview enable|disable OR enable|disable --accept-digest <digest> [--policy local|central]');
    console.log(JSON.stringify(result));
  } catch (error) { console.error(JSON.stringify({ status: 'refused', reason: error.code ?? error.message })); process.exitCode = 1; }
}
