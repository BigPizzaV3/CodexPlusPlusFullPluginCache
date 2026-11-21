#!/usr/bin/env python3
"""Deterministic checks of plugin source structure; not host runtime tests."""
import json,re,sys
from pathlib import Path
from xml.etree import ElementTree
import struct
r=Path(__file__).resolve().parents[1]
errors=[]; checks=0
def ck(ok,msg):
 global checks
 checks+=1
 if not ok: errors.append(msg)
m=json.loads((r/'plugin.json').read_text())
ck(m.get('name')=='mcp-app-builder','unexpected plugin identity')
ck(re.fullmatch(r'\d+\.\d+\.\d+',m.get('version','')) is not None,'invalid version')
ck(m.get('$schema','').startswith('https://agent-plugins.org/'),'missing portable schema')
ui=m['extensions']['com.openai']['interface']
for k,limit in [('displayName',30),('shortDescription',30),('longDescription',4000)]:ck(bool(ui.get(k)) and len(ui[k])<=limit,'interface '+k)
for k in ['logo','composerIcon']:
 p=ui.get(k,'');f=r/p.removeprefix('./');ck(p.startswith('./') and f.exists(),k+' missing')
 if f.exists():
  try:
   if f.suffix.lower()=='.png':
    raw=f.read_bytes(); ck(raw[:8]==b'\x89PNG\r\n\x1a\n' and 48<=struct.unpack('>I',raw[16:20])[0]<=4096 and struct.unpack('>I',raw[16:20])[0]==struct.unpack('>I',raw[20:24])[0],k+' PNG invalid')
   else:
    svg=ElementTree.fromstring(f.read_text());ck(svg.tag.endswith('svg') and bool(svg.attrib.get('viewBox')),k+' SVG invalid')
  except Exception as e: errors.append(str(e))
skills=list((r/'skills').glob('*/SKILL.md'))
ck(len(skills)>=12,'expected at least 12 skills')
for p in skills:
 s=p.read_text();h=re.match(r'^---\n(.+?)\n---\n',s,re.S)
 ck(bool(h),p.as_posix()+' frontmatter')
 if h:
  meta=h.group(1)
  ck('name: '+p.parent.name in meta,'name mismatch '+str(p))
  ck(bool(re.search(r'^description: \S+',meta,re.M)),'description missing '+str(p))
  for rel in re.findall(r'`(\.\./[^`]+\.md)`',s):
   ck((p.parent/rel).resolve().is_file(),'broken ref '+str(p)+': '+rel)
ck(not (r/'mcp.json').exists(),'unexpected MCP without hosted endpoint')
ck(not (r/'.app.json').exists(),'unsubmittable app ref present')
ck(not (r/'hooks').exists(),'unsubmittable hooks present')
cases=json.loads((r/'benchmarks/cases.json').read_text())['cases'];ids=[c['id'] for c in cases]
ck(len(ids)>=12 and len(ids)==len(set(ids)),'benchmark coverage/duplicates')
for c in cases:ck(bool(c.get('prompt')) and bool(c.get('expected')),'bad benchmark '+str(c))
alltext='\n'.join(x.read_text() for x in r.rglob('*') if x.is_file() and x.suffix in ('.md','.json'))
ck(not re.search(r'\bsk-[A-Za-z0-9]{20,}\b',alltext) and 'BEGIN PRIVATE KEY' not in alltext,'possible embedded secret')
ck(all(x in alltext for x in ['skill-issue.in','onepromptdesign.com','easyui.site','Swift-Charts-Examples','beautifului.dev','libraries.dev','recent.design','bencho.dev','design.google']),'missing reference')

for key, expected in {'websiteURL': 'https://tekrislabs.com/', 'supportURL': 'https://tekrislabs.com/contact', 'privacyPolicyURL': 'https://tekrislabs.com/privacy', 'termsOfServiceURL': 'https://tekrislabs.com/terms'}.items():
 ck(ui.get(key)==expected, 'listing URL '+key)
ck(1<=len(ui.get('defaultPrompt', []))<=3 and all(len(p)<=128 for p in ui.get('defaultPrompt', [])), 'prompt limit')

print(json.dumps({'checks':checks,'skills':len(skills),'benchmark_cases':len(cases),'errors':errors},indent=2))
sys.exit(1 if errors else 0)
