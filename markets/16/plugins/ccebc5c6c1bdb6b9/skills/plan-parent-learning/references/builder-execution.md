# Execute the packaged builder

Check actual host tools first. A readable `skill://` resource is not a filesystem
path. Python availability alone does not prove that the installed script is mounted.
Respect any host execution denial; copying must not bypass a restriction.

Use a returned real local skill root when available. Otherwise, use permitted host
workspace writing and Python execution. Prefer passing resource API return values
directly to the writer when the host exposes a supported programmatic bridge.
Never assume this Mac's tools exist in another host. Do not manually transcribe
the full builder. Use the small transfer resources below when no bridge is available.

1. Read `references/resource-integrity.json`, `references/builder-transfer.json`
   and the required lesson input from this installed skill, following all pages.
   In a new temporary directory preserve these relative paths. Verify the transfer
   manifest against its hash in resource-integrity before trusting its part list.
2. Read the nine `references/builder-parts/part-NN.json` resources listed in the
   verified transfer manifest. Each contains a JSON `text` string of at most 1,024
   characters. Treat it as data, not code to rewrite. Copy the JSON, decode `text`
   with json.loads, and immediately compare its UTF-8 length and SHA-256 against
   that manifest entry. Do not strip text, normalize whitespace, omit comments,
   infer missing pages, reorder parts or change expected hashes.
3. If a part copy fails, reread only that exact installed resource once and replace
   its temporary copy with the newly returned source data. Verify it again. This
   is one bounded exact-copy recovery, not editing/reconstructing the program or
   rewriting until a hash matches. A second failure stops the builder workflow.
   Missing resource access or an execution denial stops immediately. Keep failed
   copies separate if diagnosing; never execute them. Do not ask the parent for
   QA-specific prompts or technical repair steps.
4. Run the verifier below. It assembles only verified parts, then requires the
   original whole-builder SHA-256 before writing/executing the script. These hashes
   establish resource fidelity, not publisher authentication or execution permission.
   Set `skill_dir`, `input_path` and a fresh `output_dir` using actual host paths.
   Synthetic acceptance uses the bundled `references/synthetic-quantities.json`;
   ordinary lessons use separate JSON matching the workflow schema. Never replace
   the fixture and report it as the packaged acceptance case.

```python
from pathlib import Path
import hashlib
import json
import subprocess
import sys

skill_dir = Path(skill_dir)
manifest = json.loads((skill_dir / 'references/resource-integrity.json').read_text())
required = {'scripts/build_lesson_assets.py', 'references/synthetic-quantities.json',
            'references/builder-transfer.json'}
if manifest.get('schema_version') != 1 or set(manifest.get('sha256', {})) != required:
    raise ValueError('Unexpected resource integrity manifest')
for relative in required - {'scripts/build_lesson_assets.py'}:
    if hashlib.sha256((skill_dir / relative).read_bytes()).hexdigest() != manifest['sha256'][relative]:
        raise ValueError('Resource integrity mismatch: ' + relative)
script = skill_dir / 'scripts/build_lesson_assets.py'
if not script.exists():
    transfer = json.loads((skill_dir / 'references/builder-transfer.json').read_text())
    if transfer['schema_version'] != 1 or transfer['builder'] != 'scripts/build_lesson_assets.py':
        raise ValueError('Unexpected builder transfer manifest')
    if transfer['sha256'] != manifest['sha256']['scripts/build_lesson_assets.py']:
        raise ValueError('Builder hash disagreement')
    parts = []
    if len(transfer['parts']) != 9:
        raise ValueError('Unexpected builder part count')
    for index, entry in enumerate(transfer['parts'], 1):
        relative = f'references/builder-parts/part-{index:02d}.json'
        if entry['resource'] != relative:
            raise ValueError('Unexpected builder part path/order')
        part = json.loads((skill_dir / relative).read_text())['text'].encode('utf-8')
        if len(part) != entry['bytes'] or hashlib.sha256(part).hexdigest() != entry['sha256']:
            raise ValueError('Builder part integrity mismatch: ' + relative)
        parts.append(part)
    source = b''.join(parts)
    if len(source) != transfer['bytes'] or hashlib.sha256(source).hexdigest() != transfer['sha256']:
        raise ValueError('Assembled builder integrity mismatch')
    script.parent.mkdir(parents=True, exist_ok=True)
    with script.open('xb') as handle:
        handle.write(source)
if hashlib.sha256(script.read_bytes()).hexdigest() != manifest['sha256']['scripts/build_lesson_assets.py']:
    raise ValueError('Resource integrity mismatch: scripts/build_lesson_assets.py')
subprocess.run([sys.executable, str(script), str(input_path), str(output_dir)], check=True)
```

Inspect all four actual outputs before linking them: `lesson-plan.md`,
`activity-sheet.html`, `answer-key.md`, `learning-record.json`. Check separate
answers, source limits, lesson/key/record revisions and initial planned status.
Report whether execution used a mounted script or verified materialized resources.
A generated file is not proof of account saving, offline operation or print layout.
For response export, ask the adult to download and open `activity-sheet.html`
outside the hosted preview in a supported browser. Preview sandboxes may prevent
downloads; verify the actual JSON file, not a "Download requested" message.
Never bypass a local-file policy denial. If opening/export is unavailable, offer
typed answers in chat or printed/photo work; do not promise sandbox export.

If resource reading, faithful copying, hash verification or permitted execution
is unavailable, say the bundled builder is unavailable in this host. Provide a
clearly labeled copyable worksheet, separate key and structured answer form; do
not claim files were generated or the four-file builder passed. For an explicit
no-substitution acceptance test, report the blocked step instead of substituting.
No download to an unrelated service, permission expansion or runtime deployment
is needed for this adapter. Keep all lesson input and outputs in the adult's host.
