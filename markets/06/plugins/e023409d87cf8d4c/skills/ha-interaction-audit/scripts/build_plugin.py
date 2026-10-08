#!/usr/bin/env python3
"""Materialize the plugin from the canonical saved skill without creating an archive."""
import argparse
import json
import shutil
import tempfile
import yaml
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('destination',type=Path)
    p.add_argument('--refresh-owned',action='store_true')
    args=p.parse_args()
    skill=Path(__file__).resolve().parents[1]
    manifest=json.loads((skill/'assets/plugin-manifest.json').read_text())
    dest=args.destination.expanduser().resolve()
    if dest.name!=manifest['name']:p.error('Destination folder must match the plugin name')
    if dest.is_relative_to(skill) or skill.is_relative_to(dest):p.error('Plugin and canonical skill must be separate directories')
    existing=dest/'.codex-plugin/plugin.json'
    if dest.exists():
        if not args.refresh_owned or not existing.is_file():p.error('Destination exists; explicit owned refresh required')
        if json.loads(existing.read_text()).get('name')!=manifest['name']:p.error('Existing plugin does not match')
    target=dest/'skills'/manifest['name']
    backup=None
    if target.exists() and not args.refresh_owned:p.error('Skill copy exists; explicit owned refresh required')
    if dest.exists():
        backup_root=dest.parent/'.plugin-backups'
        backup_root.mkdir(exist_ok=True)
        backup=Path(tempfile.mkdtemp(prefix=manifest['name']+'-',dir=backup_root))/'plugin'
        shutil.copytree(dest,backup)
    (dest/'.codex-plugin').mkdir(parents=True,exist_ok=True)
    if target.exists():shutil.rmtree(target)
    shutil.copytree(skill,target,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.git','.pytest_cache'))
    # Personal-skill reconciliation may add product metadata which the plugin
    # agent schema does not accept. Normalize only the materialized copy.
    agent_path=target/'agents/openai.yaml'
    if agent_path.is_file():
        agent=yaml.safe_load(agent_path.read_text())
        if isinstance(agent,dict) and isinstance(agent.get('policy'),dict):
            agent['policy'].pop('products',None)
            if not agent['policy']:agent.pop('policy')
            agent_path.write_text(yaml.safe_dump(agent,sort_keys=False,allow_unicode=True))
    existing.write_text(json.dumps(manifest,indent=2)+'\n')
    shutil.copyfile(skill/'assets/plugin-guide.md',dest/'README.md')
    print(json.dumps({'plugin':str(dest),'skill':str(target),'previousPluginBackup':str(backup) if backup else None}))

if __name__=='__main__':main()
