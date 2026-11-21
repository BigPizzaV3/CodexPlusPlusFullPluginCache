#!/usr/bin/env python3
"""Validate portable plugin package, references, benchmark coverage and safety claims.
This validates structure/policy only, NOT installed skill behavior or apps.
"""
from pathlib import Path
from xml.etree import ElementTree
import json,re,sys
r=Path(__file__).resolve().parents[1]
errors=[];checks=0
def ck(ok,msg):
 global checks
 checks+=1
 if not ok:errors.append(msg)
p=json.loads((r/'plugin.json').read_text())
ck(p['name']=='web-mobile-app-builder','plugin name')
ck(re.fullmatch(r'\d+\.\d+\.\d+',p.get('version','')) is not None,'semver')
ck(p.get('$schema')=='https://agent-plugins.org/schemas/1.0.0/plugin.schema.json','schema')
ck(len(p.get('description',''))>30,'description')
ui=p['extensions']['com.openai']['interface']
for k,limit in [('displayName',32),('shortDescription',30),('longDescription',4000)]:
 ck(bool(ui.get(k)) and len(ui[k])<=limit,'ui: '+k)
for k in ['logo','composerIcon']:
 f=r/ui[k].removeprefix('./')
 ck(ui[k].startswith('./') and f.is_file(),'asset path '+k)
 if f.exists():
  try:
   if f.suffix.lower()=='.png':
    import struct
    raw=f.read_bytes()
    valid_png=(raw[:8]==b'\x89PNG\r\n\x1a\n' and len(raw)>=24)
    if valid_png:
     width,height=struct.unpack('>II',raw[16:24])
     valid_png = 48<=width<=4096 and width==height
    ck(valid_png,'asset PNG '+k)
   elif f.suffix.lower()=='.svg':
    root=ElementTree.fromstring(f.read_text())
    ck(root.tag.endswith('svg') and bool(root.attrib.get('viewBox')),'asset SVG '+k)
   else:
    ck(False,'unsupported asset '+k)
  except Exception as e:errors.append(str(e))
onboarding=r/p['extensions']['com.openai']['onboardingSkill'].removeprefix('./')
ck(onboarding.is_file(),'onboarding skill')
skills=list((r/'skills').glob('*/SKILL.md'))
ck(len(skills)>=20,'minimum skill count')
for f in skills:
 t=f.read_text()
 m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
 ck(bool(m),'frontmatter '+f.as_posix())
 if m:
  ck(bool(re.search(r'^name: '+re.escape(f.parent.name)+r'$',m.group(1),re.M)),'name '+f.as_posix())
  ck(bool(re.search(r'^description: .{25,}$',m.group(1),re.M)),'description '+f.as_posix())
 for rel in re.findall(r'`(\.\.?/[^`]+\.md)`',t):
  ck((f.parent/rel).resolve().is_file(),'skill reference '+str(f)+': '+rel)
 ck(len(t.split())>=80,'skill depth '+f.parent.name)
 ck('http://example.com' not in t and 'sk-proj-' not in t,'no placeholder/secret '+f.parent.name)
for unwanted in ('mcp.json','.mcp.json','.app.json','hooks'):
 ck(not (r/unwanted).exists(),'unexpected unconfigured feature: '+unwanted)
refs=list((r/'references').glob('*.md'))
ck(len(refs)>=15,'references >=15')
for v in ('skill-issue.in','onepromptdesign.com','easyui.site','Swift-Charts-Examples','beautifului.dev','libraries.dev','recent.design','bencho.dev','design.google'):
 t=(r/'references/curated-sources.md').read_text()
 ck(v in t,'source missing: '+v)
cases=json.loads((r/'benchmarks/cases.json').read_text())['cases']
ck(len(cases)>=18,'benchmark count')
ck(len({c['id'] for c in cases})==len(cases),'unique benchmark ids')
for c in cases:
 ck((r/'skills'/c['primary_skill']/'SKILL.md').is_file(),'benchmark skill '+c['id'])
 ck(len(c.get('expected',[]))>=2,'benchmark expected '+c['id'])
 ck(c.get('status')=='NOT_RUN','benchmark no fabricated pass '+c['id'])
for template in ['product-brief.md','design-spec.md','screen-state-inventory.md','evidence-report.md','agent-handoff.md']:
 ck((r/'templates'/template).is_file(),'template '+template)
all_text='\n'.join(f.read_text(errors='ignore') for f in r.rglob('*') if f.is_file() and f.suffix in ('.md','.json'))
ck('BEGIN PRIVATE KEY' not in all_text and not re.search(r'\bsk-[A-Za-z0-9]{25,}\b',all_text),'no secrets')
ck('real subagents' in all_text.lower() and 'NOT RUN' in all_text,'capability truthfulness')

for key, expected in {'websiteURL': 'https://tekrislabs.com/', 'supportURL': 'https://tekrislabs.com/contact', 'privacyPolicyURL': 'https://tekrislabs.com/privacy', 'termsOfServiceURL': 'https://tekrislabs.com/terms'}.items():
 ck(ui.get(key)==expected, 'listing URL '+key)
ck(1<=len(ui.get('defaultPrompt', []))<=3 and all(len(p)<=128 for p in ui.get('defaultPrompt', [])), 'prompt limit')

print(json.dumps({'checks':checks,'skills':len(skills),'references':len(refs),'benchmarks':len(cases),'errors':errors},indent=2))
sys.exit(1 if errors else 0)
