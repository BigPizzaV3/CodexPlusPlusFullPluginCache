/* Build_ resource transport only. No network, owner API, imports or engine rewriting.
 * Host adapters: readResource(relativePath, cursor) -> {contents,next_cursor?};
 * runPython(code, inputObject) -> parsed JSON from code's stdout, with inputObject
 * supplied as JSON on stdin. Keep tool-returned strings inside the host runtime.
 * For a plain V8 host, remove ONLY the final export line before evaluating the
 * inspected source with Function(source + '\nreturn bootstrapRuntime;')().
 */

const BRIDGE_SCHEMA = 'build.runtime-bridge/1';
const HELPER_SHA = '40294949b00b3328fbb692ec844e83921c891986bdd378a230c5d4e52b36f199';
const HELPER_BYTES = 11458;
const RUNTIME_NAMES = [
  'deliver.py', 'iteration/__init__.py', 'iteration/engine.py',
  'iteration/layout.py', 'iteration/lifecycle_template.py', 'iteration/logs.py',
  'iteration/mcp.py', 'iteration/records.py', 'iteration/release_contract.py',
  'iteration/runner_template.py', 'iteration/safety.py', 'iteration/store.py',
  'iteration_cli.py', 'release_check.py'
];

// Every invocation accepts bounded structured data, never source interpolated as code.
const PYTHON_BRIDGE = String.raw`import sys,json,hashlib,tempfile,pathlib,os,uuid,subprocess,shutil
HELPER_SHA='40294949b00b3328fbb692ec844e83921c891986bdd378a230c5d4e52b36f199'
HELPER_BYTES=11458
class Blocked(Exception):
 def __init__(self,code,**details):self.code=code;self.details=details
def require(ok,code,**details):
 if not ok:raise Blocked(code,**details)
def load(path):return json.loads(path.read_text(encoding='utf-8'))
def save(path,value):path.write_text(json.dumps(value),encoding='utf-8')
def session(data):
 root=pathlib.Path(data['session']['root']);token=data['session']['token']
 require(root.is_absolute() and root.name.startswith('build-runtime-bridge-') and not root.is_symlink(),'invalid_session')
 require(root.is_dir() and load(root/'.bridge-owner.json').get('token')==token,'invalid_session')
 return root
def main(data):
 op=data.get('op')
 if op=='init':
  require(sys.version_info>=(3,10),'python_version_unsupported')
  root=pathlib.Path(tempfile.mkdtemp(prefix='build-runtime-bridge-'));token=uuid.uuid4().hex
  try:
   save(root/'.bridge-owner.json',{'token':token})
   proof=root/'.write-read';proof.write_bytes(b'build-runtime-bridge');require(proof.read_bytes()==b'build-runtime-bridge','sandbox_unwritable');proof.unlink()
   (root/'source').mkdir()
  except BaseException:
   shutil.rmtree(root);raise
  return {'status':'passed','session':{'root':str(root),'token':token},'python_version':'.'.join(map(str,sys.version_info[:3]))}
 root=session(data)
 if op=='cleanup':
  shutil.rmtree(root);return {'status':'passed'}
 if op=='begin':
  name=data['name'];parts=pathlib.PurePosixPath(name)
  require(isinstance(name,str) and not parts.is_absolute() and '..' not in parts.parts and '\\' not in name and ':' not in name,'invalid_runtime_path')
  helper=data.get('helper') is True
  require((helper and name=='prepare_runtime.py') or (not helper and name in data['allowed_names']),'invalid_runtime_path')
  expected=data['expected_bytes'];digest=data['expected_sha256']
  require(type(expected) is int and 0<expected<=262144 and isinstance(digest,str) and len(digest)==64,'invalid_file_record')
  if helper:require(expected==HELPER_BYTES and digest==HELPER_SHA,'helper_pin_mismatch')
  target=root/name if helper else root/'source'/name
  require(not target.exists() and not (root/'.transfer.json').exists(),'unexpected_existing_file')
  target.parent.mkdir(parents=True,exist_ok=True)
  with (root/'.incoming').open('xb'):pass
  save(root/'.transfer.json',{'name':name,'helper':helper,'bytes':expected,'sha256':digest,'sequence':0,'received':0})
  return {'status':'passed'}
 if op=='chunk':
  record=load(root/'.transfer.json');text=data['text']
  require(type(data['sequence']) is int and data['sequence']==record['sequence'],'chunk_sequence_mismatch')
  require(isinstance(text,str) and len(text)<=4096,'chunk_too_large')
  raw=text.encode('utf-8');received=record['received']+len(raw)
  require(received<=record['bytes'],'resource_size_mismatch',resource=record['name'],expected_bytes=record['bytes'],actual_bytes=received)
  with (root/'.incoming').open('ab') as stream:stream.write(raw)
  record['received']=received;record['sequence']+=1;save(root/'.transfer.json',record)
  return {'status':'passed'}
 if op=='commit':
  record=load(root/'.transfer.json');raw=(root/'.incoming').read_bytes();digest=hashlib.sha256(raw).hexdigest()
  require(len(raw)==record['bytes'] and digest==record['sha256'],'resource_hash_mismatch',resource=record['name'],expected_bytes=record['bytes'],actual_bytes=len(raw),expected_sha256=record['sha256'],actual_sha256=digest)
  target=root/record['name'] if record['helper'] else root/'source'/record['name']
  with target.open('xb') as stream:stream.write(raw)
  (root/'.incoming').unlink();(root/'.transfer.json').unlink()
  return {'status':'passed','verified_bytes':len(raw)}
 if op=='finish':
  helper=root/'prepare_runtime.py';raw=helper.read_bytes()
  require(len(raw)==HELPER_BYTES and hashlib.sha256(raw).hexdigest()==HELPER_SHA,'helper_pin_mismatch')
  require(not (root/'.transfer.json').exists() and not (root/'runtime').exists(),'incomplete_runtime')
  try:
   process=subprocess.run([sys.executable,'-B','-E','-s',str(helper),'--copy-from',str(root/'source'),'--destination',str(root/'runtime'),'--probe'],cwd=root,capture_output=True,timeout=55,check=False)
  except subprocess.TimeoutExpired:raise Blocked('runtime_probe_timeout')
  require(len(process.stdout)<=65536,'runtime_probe_output_too_large')
  try:result=json.loads(process.stdout)
  except (ValueError,UnicodeError):raise Blocked('runtime_probe_invalid_result',exit_code=process.returncode)
  require(process.returncode==0 and result.get('status')=='passed' and result.get('runtime_executable') is True and result.get('files_verified')==14,'runtime_probe_failed',exit_code=process.returncode,missing=result.get('missing',[]),mismatched_files=[item.get('file') for item in result.get('mismatched',[])],unexpected_python_files=result.get('unexpected_python_files',[]))
  return {'status':'passed','workspace_root':str(root),'runtime_root':result['runtime_root'],'helper_path':str(helper),'source_root':str(root/'source'),'entrypoints':result['entrypoints'],'files_verified':14,'command_probes':[{'entrypoint':item['entrypoint'],'status':item['status'],'exit_code':item.get('exit_code')} for item in result['command_probes']]}
 raise Blocked('invalid_operation')
try:
 data=json.load(sys.stdin);result=main(data)
except Blocked as error:result={'status':'blocked','error_code':error.code,**error.details}
except (OSError,ValueError,KeyError,TypeError,UnicodeError):result={'status':'blocked','error_code':'local_runtime_operation_failed'}
print(json.dumps(result,ensure_ascii=True))
`;

function utf8Bytes(text) {
  let size = 0;
  for (const character of text) {
    const point = character.codePointAt(0);
    size += point < 0x80 ? 1 : point < 0x800 ? 2 : point < 0x10000 ? 3 : 4;
  }
  return size;
}

class BridgeFailure extends Error {
  constructor(code, details = {}) { super(code); this.code = code; this.details = details; }
}

async function bootstrapRuntime({ readResource, runPython, notify } = {}) {
  let activeSession = null;
  let currentResource = null;
  let currentOperation = 'capability_check';
  const base = { schema: BRIDGE_SCHEMA, network_used: false, owner_api_used: false,
    customer_code_executed: false, application_qualified: false };
  const fail = (code, details) => { throw new BridgeFailure(code, details); };
  const progress = async (stage, details = {}) => {
    if (typeof notify === 'function') {
      try { await notify({ stage, ...details }); } catch { /* Optional progress only. */ }
    }
  };
  const python = async input => {
    currentOperation = input.op;
    const payload = activeSession ? { ...input, session: activeSession } : input;
    if (utf8Bytes(PYTHON_BRIDGE) + utf8Bytes(JSON.stringify(payload)) > 48 * 1024)
      fail('transport_payload_too_large');
    let result;
    try { result = await runPython(PYTHON_BRIDGE, payload); }
    catch { fail('python_execution_unavailable', { operation: input.op }); }
    if (!result || typeof result !== 'object' || Array.isArray(result))
      fail('python_protocol_error', { operation: input.op });
    if (result.status !== 'passed') {
      const details = {};
      for (const key of ['resource', 'expected_bytes', 'actual_bytes', 'expected_sha256', 'actual_sha256', 'exit_code', 'missing', 'mismatched_files', 'unexpected_python_files'])
        if (Object.prototype.hasOwnProperty.call(result, key)) details[key] = result[key];
      fail(typeof result.error_code === 'string' ? result.error_code : 'python_protocol_error', details);
    }
    return result;
  };
  const read = async (relativePath, limit) => {
    currentResource = relativePath;
    const seen = new Set();
    let cursor;
    let text = '';
    for (let page = 0; page < 64; page++) {
      let response;
      try { response = await readResource(relativePath, cursor); }
      catch { fail('resource_read_failed', { resource: relativePath }); }
      if (!response || typeof response.contents !== 'string')
        fail('resource_reader_protocol_error', { resource: relativePath });
      text += response.contents;
      if (utf8Bytes(text) > limit) fail('resource_too_large', { resource: relativePath });
      const next = response.next_cursor;
      if (next === undefined || next === null) return text;
      if (typeof next !== 'string' || !next || next.length > 8192)
        fail('resource_reader_protocol_error', { resource: relativePath });
      if (seen.has(next)) fail('resource_pagination_cycle', { resource: relativePath });
      seen.add(next); cursor = next;
    }
    fail('resource_page_limit', { resource: relativePath });
  };
  const transfer = async (name, record, helper = false) => {
    const text = await read(record.skill_path, Math.min(262144, record.bytes + 4096));
    await python({ op: 'begin', name, helper, allowed_names: RUNTIME_NAMES,
      expected_bytes: record.bytes, expected_sha256: record.sha256 });
    let chunk = '', length = 0, sequence = 0;
    for (const character of text) {
      chunk += character; length++;
      if (length === 4096) {
        await python({ op: 'chunk', sequence: sequence++, text: chunk });
        chunk = ''; length = 0;
      }
    }
    if (chunk) await python({ op: 'chunk', sequence, text: chunk });
    await python({ op: 'commit' });
  };
  try {
    if (typeof runPython !== 'function') fail('python_adapter_unavailable');
    if (typeof readResource !== 'function') fail('resource_adapter_unavailable');
    await progress('checking_execution');
    const initialized = await python({ op: 'init' });
    if (!initialized.session || typeof initialized.session.root !== 'string' || typeof initialized.session.token !== 'string')
      fail('python_protocol_error');
    activeSession = initialized.session;
    let inventory;
    try { inventory = JSON.parse(await read('Automation/EX89.json', 32768)); }
    catch (error) { if (error instanceof BridgeFailure) throw error; fail('inventory_invalid'); }
    const helper = inventory?.materializer;
    const records = inventory?.runtime_files;
    if (inventory?.schema !== 'build.runtime-resources/1' || helper?.skill_path !== 'scripts/prepare_runtime.py' ||
        helper?.sha256 !== HELPER_SHA || helper?.bytes !== HELPER_BYTES || !Array.isArray(records) || records.length !== 14)
      fail('inventory_invalid');
    const names = new Set();
    let bytes = 0;
    for (const record of records) {
      if (!record || !RUNTIME_NAMES.includes(record.path) || names.has(record.path) || record.skill_path !== 'scripts/' + record.path ||
          !Number.isInteger(record.bytes) || record.bytes < 1 || record.bytes > 262144 || !/^[0-9a-f]{64}$/.test(record.sha256))
        fail('inventory_invalid');
      names.add(record.path); bytes += record.bytes;
    }
    if (bytes > 200000) fail('inventory_invalid');
    await progress('copying_verified_resources', { runtime_files: 14 });
    await transfer('prepare_runtime.py', helper, true);
    for (const record of records) await transfer(record.path, record);
    currentResource = null;
    await progress('probing_runtime');
    const result = await python({ op: 'finish' });
    await progress('runtime_ready', { files_verified: result.files_verified });
    return { ...base, ...result, error_code: null };
  } catch (error) {
    let cleanup = 'not_needed';
    if (activeSession && typeof runPython === 'function') {
      try {
        const cleaned = await runPython(PYTHON_BRIDGE, { op: 'cleanup', session: activeSession });
        cleanup = cleaned?.status === 'passed' ? 'completed' : 'unconfirmed';
      } catch { cleanup = 'unconfirmed'; }
    }
    return { ...base, status: 'blocked', error_code: error instanceof BridgeFailure ? error.code : 'bootstrap_failed',
      resource: currentResource, operation: currentOperation,
      ...(error instanceof BridgeFailure ? error.details : {}), cleanup };
  }
}

export { bootstrapRuntime };
