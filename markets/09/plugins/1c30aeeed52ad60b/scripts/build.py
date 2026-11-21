"""Reproducible, allowlisted development ZIP. Never marks it submittable."""
import hashlib,json,pathlib,stat,unicodedata,zipfile
root=pathlib.Path(__file__).resolve().parents[1]
files=['LICENSE','assets/icon.png','plugin.json','mcp.json','package.json','README.md','skills/capability-builder/SKILL.md','src/core.mjs','src/body.mjs','src/server.mjs','src/protocol.mjs','src/worker.mjs','src/public-pages.mjs','wrangler.jsonc','wrangler.production.jsonc','scripts/demo.mjs','src/templates.json','src/draft.schema.json','docs/ATTRIBUTION.md','docs/legal/privacy.txt','docs/legal/support.txt','docs/legal/terms.txt','docs/REVIEW-CASES.json','docs/READINESS.md','docs/ASSETS.md','docs/SOURCES.md','scripts/build.py']
manifest=json.loads((root/'plugin.json').read_text());ui=manifest['extensions']['com.openai']['interface']
assert len(manifest['name'])<=64 and len(ui['displayName'])<=30 and len(ui['shortDescription'])<=30 and len(ui['longDescription'])<=4000
assert len(ui['defaultPrompt'])==3 and all(len(s)<=128 and '\n' not in s and '@' not in s for s in ui['defaultPrompt'])
assert len(set(ui['defaultPrompt']))==3
cases=json.loads((root/'docs/REVIEW-CASES.json').read_text());assert len(cases['positive'])==5 and len(cases['negative'])==3
seen=set()
for name in files:
 path=root/name;assert path.is_file() and not path.is_symlink()
 assert len(pathlib.PurePosixPath(name).parts)<=20 and '..' not in pathlib.PurePosixPath(name).parts
 normalized=unicodedata.normalize('NFC',name).casefold();assert normalized not in seen;seen.add(normalized)
 data=path.read_bytes();assert len(data)<=100*1024*1024
 assert (b'/' + b'Users/') not in data and (b'home' + b'Dir') not in data and (b'repo' + b'Root') not in data
out=root/'dist';out.mkdir(exist_ok=True)
archive=out/'scaffolde-capability-builder-0.1.3-policy-candidate.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name in sorted(files):
  info=zipfile.ZipInfo(name,(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.create_system=3;info.external_attr=(stat.S_IFREG|0o644)<<16
  z.writestr(info,(root/name).read_bytes())
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None and len(z.infolist())<=5000
 assert sum(i.file_size for i in z.infolist())<=512*1024*1024
assert archive.stat().st_size<=100_000_000
print(json.dumps({'file':archive.name,'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':len(files),'submittable':False},indent=2))
