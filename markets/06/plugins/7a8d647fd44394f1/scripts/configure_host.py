#!/usr/bin/env python3
"""Configure this installation, optionally enrolling it in a shared storage registry."""
import argparse
import json
import os
from pathlib import Path
import sys

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from host_adapter import EDITION, SERVER_NAME
import storage_settings


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database',type=Path)
    parser.add_argument('--config',type=Path)
    parser.add_argument('--registry',type=Path)
    parser.add_argument('--shared-root',type=Path)
    parser.add_argument('--bettercontext-root',type=Path)
    parser.add_argument('--private-root',type=Path)
    parser.add_argument('--bundled-runtime',action='store_true')
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    config=(args.config or storage_settings.configuration_path(EDITION)).expanduser().resolve()
    os.environ['BETTERCONTEXT_'+EDITION.upper()+'_CONFIG']=str(config)
    settings=storage_settings.saved_settings(EDITION)
    if args.registry:
        if not args.database or not args.shared_root: parser.error('--registry requires --database and --shared-root')
        plan=storage_settings.configure(str(args.database.parent),'connect',args.check,str(args.registry),str(args.shared_root))
        print(json.dumps(plan,indent=2))
    else:
        for key,value in [('database_path',args.database),('bettercontext_root',args.bettercontext_root),('private_root',args.private_root)]:
            if value: settings[key]=str(value.expanduser().resolve())
        if args.database and settings.get('storage_registry_path'):
            parser.error('This installation is enrolled; use the shared storage tool to change its location')
        if args.bundled_runtime: settings['runtime_mode']='bundled'
        if EDITION=='private' and not settings: parser.error('Private setup requires an existing database or shared registry')
        if settings:
            database=storage_settings.resolve_settings(settings,EDITION)
            if EDITION=='private': storage_settings.inspect_database(database)
            if not args.check: storage_settings.save_settings(EDITION,settings)
        print(json.dumps({'edition':EDITION,'config_path':str(config),'settings':settings,'check_only':args.check},indent=2))
    if args.check:return
    configured_mcp = False
    for name in ('mcp.json','.mcp.json'):
        path=ROOT/name
        if not path.is_file(): continue  # Directory skills-only packages omit MCP configuration.
        configured_mcp = True
        manifest=json.loads(path.read_text(encoding='utf-8'))
        entry=manifest['mcpServers'][SERVER_NAME.replace('-','_')]
        entry['command']=Path(sys.executable).name
        entry.setdefault('env',{})['PATH']=str(Path(sys.executable).parent)+os.pathsep+os.environ.get('PATH','')
        entry['env']['BETTERCONTEXT_'+EDITION.upper()+'_CONFIG']=str(config)
        with path.open('r+',encoding='utf-8') as handle:
            handle.seek(0);handle.write(json.dumps(manifest,indent=2)+'\n');handle.truncate()
    print('Host configured. Reinstall and start a new task to load the updated tools.' if configured_mcp else 'Storage configured for local commands. This skills-only package does not register MCP tools.')


if __name__=='__main__': main()
