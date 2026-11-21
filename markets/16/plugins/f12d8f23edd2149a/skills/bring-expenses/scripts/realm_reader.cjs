// Optional local reader for the tested legacy Expend schema. No sync config.
// Install realm@12.14.2 in a separate runtime and set NODE_PATH to its modules.
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const crypto = require('node:crypto');
const Realm = require('realm');
const [input, output] = process.argv.slice(2);
if (!input || !output || fs.statSync(input).size > 100 * 1024 * 1024) throw Error('Invalid Realm input');
const before = crypto.createHash('sha256').update(fs.readFileSync(input)).digest('hex');
const temp = fs.mkdtempSync(path.join(os.tmpdir(), 'PaceRealm-'));
let realm;
try {
  const copy = path.join(temp, 'source.realm'); fs.copyFileSync(input, copy);
  realm = new Realm({path: copy, readOnly: true});
  const schema = realm.schema.find(x => x.name === 'Expend');
  const required = ['compoundKey','originalCurrency','originalCost','date','classify','remark','isIncome','transferType','status','ignore','ignoreFromExpend'];
  if (!schema || required.some(k => !(k in schema.properties))) throw Error('Unsupported Realm schema; export CSV from the originating app');
  const objects = realm.objects('Expend');
  if (objects.length > 100_000) throw Error('Realm row limit exceeded');
  const records = Array.from(objects, row => ({
    id: row.compoundKey, nativeID: row.id, amount: row.originalCost, currency: row.originalCurrency,
    date: row.date.toISOString(), category: row.classify?.name ?? '', note: row.remark ?? '',
    kind: !row.isIncome && row.transferType === 0 && row.status === 0 && !row.ignore && !row.ignoreFromExpend ? 'expense' : row.isIncome ? 'income' : 'transfer',
    subcategory: row.subcategory?.name ?? ''
  }));
  fs.writeFileSync(output, JSON.stringify(records));
} finally {
  realm?.close(); fs.rmSync(temp, {recursive:true, force:true});
  if (crypto.createHash('sha256').update(fs.readFileSync(input)).digest('hex') !== before) throw Error('Source file changed');
}
// Realm's compatibility runtime can retain idle handles after close in Node.
// All output/source-integrity checks above finish synchronously first.
process.exit(0);
