#!/usr/bin/env python3
"""Offline structural checks. Not a runtime/integration test."""
from pathlib import Path
import json,re,sys,zipfile
root=Path(__file__).resolve().parents[1]
checks=0
def check(ok,msg):
 global checks
 checks+=1
 if not ok: raise AssertionError(msg)
manifest=json.loads((root/'plugin.json').read_text(encoding='utf-8'))
check(manifest['name']=='design-game-studio','package name')
check(re.fullmatch(r'\d+\.\d+\.\d+',manifest['version']) is not None,'semantic version')
check(manifest.get('$schema','').startswith('https://agent-plugins.org/'),'portable schema')
check(manifest.get('author',{}).get('name')=='Tekris Labs','publisher')
iface=manifest['extensions']['com.openai']['interface']
check(iface.get('developerName')=='Tekris Labs','developer')
check(iface['displayName']=='Design Game Studio','display name')
check(len(iface['defaultPrompt'])==3,'exactly three starter prompts')
for key in ['websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL']:
 check(iface.get(key,'').startswith('https://tekrislabs.com/'),key)
for key in ['logo','composerIcon']:
 p=root/iface[key][2:]
 check(p.is_file() and p.stat().st_size>1000,key)
 check(p.resolve().is_relative_to(root.resolve()),'safe path '+key)
check((root/manifest['extensions']['com.openai']['onboardingSkill'][2:]).is_file(),'onboarding skill')
check(not (root/'mcp.json').exists() and not (root/'.mcp.json').exists(),'no false server')
check(not (root/'hooks').exists(),'no hooks in public ZIP')
assert (root/'.codex-plugin/plugin.json').is_file()
legacy=json.loads((root/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
check(legacy['name']==manifest['name'],'compat identity')
check(legacy['version']==manifest['version'],'compat version')
check(legacy['skills']=='./skills/','legacy skill path')
check(legacy['interface']['displayName']==iface['displayName'],'compat display name')
check(len(legacy['interface']['defaultPrompt'])==3,'compat prompts')
skills=list((root/'skills').glob('*/SKILL.md'))
check(len(skills)>=18,'missing skills')
for path in skills:
 text=path.read_text(encoding='utf-8')
 lines=text.splitlines()
 check(lines[0]=='---','YAML header at '+str(path))
 check('---' in lines[1:12],'YAML closure at '+str(path))
 name=re.search(r'(?m)^name:\s*(\S+)',text)
 desc=re.search(r'(?m)^description:\s*(.+)',text)
 check(bool(name) and name.group(1)==path.parent.name,'skill name '+str(path))
 check(bool(desc) and len(desc.group(1))>25,'skill description '+str(path))
 check('## ' in text,'instructions structure '+str(path))
 check('../../references/' in text or '##' in text,'meaningful skill references '+str(path))
for p in (root/'references').glob('*.md'):
 check(p.stat().st_size>150,'empty reference '+str(p))
for p in (root/'templates').iterdir():
 check(p.stat().st_size>40,'empty template '+str(p))
bench=json.loads((root/'benchmarks/cases.json').read_text(encoding='utf-8'))
check(len(bench['cases'])>=15,'benchmarks count')
check(all(x['status']=='not-run' for x in bench['cases']),'no false benchmark passes')
check(len(set(x['id'] for x in bench['cases']))==len(bench['cases']),'unique IDs')
print(f'PASS: {checks} structural checks, {len(skills)} skills, {len(bench["cases"])} unexecuted benchmark cases')
