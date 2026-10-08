"""Install/manage the selected edition's optional per-user relay wake helper."""
from contextlib import closing
import json
import os
from pathlib import Path
import plistlib
import shutil
import sqlite3
import subprocess
import sys

from host_adapter import EDITION, load_host
from wake_dispatcher import find_codex
import chat_tracking


def service_root():
    if os.name == 'nt':
        # Store service files outside packaged-app AppData virtualization so
        # Task Scheduler can see the same files as the desktop plugin process.
        return Path.home()/'.bettercontext'/EDITION/'wake'
    elif sys.platform=='darwin':
        base=Path.home()/'Library/Application Support'
    else:
        base=Path(os.environ.get('XDG_STATE_HOME',str(Path.home()/'.local/state')))
    return base/('BetterContextPrivate' if EDITION=='private' else 'BetterContextPublic')/'WakeDispatcher'


def run(command, check=True):
    result=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=45,
                          creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    if check and result.returncode:
        raise ValueError((result.stderr or result.stdout).strip() or f'Service command exited {result.returncode}')
    return result


def service_action(action):
    root=service_root()
    name='BetterContext '+EDITION.title()+' Wake'
    if os.name=='nt':
        helper=Path(__file__).with_name('wake_windows.ps1')
        result=run(['powershell.exe','-NoProfile','-NonInteractive','-ExecutionPolicy','Bypass','-File',str(helper),
                    '-Action',action,'-Edition',EDITION,'-InstallRoot',str(root)],check=action!='status')
        if result.returncode:
            return {'installed':None,'error':(result.stderr or result.stdout).strip()}
        return json.loads(result.stdout)
    if sys.platform.startswith('linux'):
        unit='bettercontext-'+EDITION+'-wake.service'
        unit_path=Path.home()/'.config/systemd/user'/unit
        if action=='status':
            state=run(['systemctl','--user','is-active',unit],check=False)
            return {'installed':unit_path.exists(),'running':state.stdout.strip()=='active','state':state.stdout.strip()}
        if action=='install':
            settings=json.loads((root/'service.json').read_text(encoding='utf-8'))
            def quote(value):return '"'+str(value).replace('\\','\\\\').replace('"','\\"').replace('%','%%').replace('$','$$')+'"'
            command=' '.join(quote(s) for s in [settings['python'],str(root/'wake_dispatcher.py'),'--config',str(root/'wake-dispatcher.json')])
            unit_path.parent.mkdir(parents=True,exist_ok=True)
            unit_path.write_text('[Unit]\nDescription='+name+'\n[Service]\nExecStart='+command+'\nRestart=on-failure\nRestartSec=5\n[Install]\nWantedBy=default.target\n',encoding='utf-8')
            run(['systemctl','--user','daemon-reload'])
            run(['systemctl','--user','enable',unit])
            run(['systemctl','--user','restart',unit])
        elif action=='uninstall':
            run(['systemctl','--user','disable','--now',unit])
            if unit_path.exists():unit_path.unlink()
            run(['systemctl','--user','daemon-reload'])
        else:run(['systemctl','--user',action,unit])
        return service_action('status')
    if sys.platform=='darwin':
        label='to.unkd.bettercontext.'+EDITION+'.wake'
        plist=Path.home()/'Library/LaunchAgents'/(label+'.plist')
        target=f'gui/{os.getuid()}/{label}'
        if action=='status':
            state=run(['launchctl','print',target],check=False)
            return {'installed':plist.exists(),'running':state.returncode==0 and 'state = running' in state.stdout}
        if action in {'stop','uninstall'}:run(['launchctl','bootout',target],check=False)
        if action=='uninstall' and plist.exists():plist.unlink()
        if action=='install':
            settings=json.loads((root/'service.json').read_text(encoding='utf-8'))
            plist.parent.mkdir(parents=True,exist_ok=True)
            payload={'Label':label,'ProgramArguments':[settings['python'],str(root/'wake_dispatcher.py'),'--config',str(root/'wake-dispatcher.json')],
                     'RunAtLoad':True,'KeepAlive':True,'StandardErrorPath':str(root/'service-error.log')}
            plist.write_bytes(plistlib.dumps(payload))
            run(['launchctl','bootout',target],check=False)
        if action in {'install','start'}:run(['launchctl','bootstrap',f'gui/{os.getuid()}',str(plist)])
        return service_action('status')
    raise ValueError('Automatic service setup supports Windows, Linux systemd, and macOS launchd')


def legacy_installations(with_status=False):
    """Report separately managed private bridges without changing them."""
    if EDITION != 'private':
        return []
    candidates = []
    if sys.platform.startswith('linux'):
        base = Path(os.environ.get('XDG_CONFIG_HOME', str(Path.home()/'.config')))/'bettercontext'
        candidates = sorted(base.glob('wake-dispatcher*.json'))
    elif os.name == 'nt':
        for base in (Path(os.environ.get('LOCALAPPDATA', str(Path.home()/'AppData/Local'))), Path.home()/'AppData/Local'):
            path = base/'BetterContext/WakeDispatcher/wake-dispatcher.json'
            if path.is_file() and path not in candidates:
                candidates.append(path)
    result = []
    for path in candidates:
        entry = {'config_path': str(path), 'managed_externally': True, 'running': None}
        try:
            config = json.loads(path.read_text(encoding='utf-8'))
            entry['local_aliases'] = config.get('local_aliases', [])
        except (OSError, ValueError):
            entry['configuration_readable'] = False
        if with_status and sys.platform.startswith('linux'):
            suffix = path.stem.removeprefix('wake-dispatcher')
            unit = 'bettercontext-wake'+suffix+'.service'
            entry['service'] = unit
            state = run(['systemctl', '--user', 'is-active', unit], check=False)
            entry['state'] = state.stdout.strip()
            entry['running'] = entry['state'] == 'active'
        result.append(entry)
    return result


def plan(aliases):
    if legacy_installations():
        raise ValueError('A legacy private wake installation exists. Inspect and migrate it before enabling this edition service; do not run both.')
    settings,_=load_host()
    database=settings['database_path']
    if not database.is_file():raise ValueError('Initialize or connect this edition database before wake setup')
    if not aliases:raise ValueError('Choose at least one registered local chat to wake')
    targets={}
    with closing(sqlite3.connect(chat_tracking.uri(database),uri=True)) as conn:
        for alias in aliases:
            row=conn.execute('SELECT short_id,uuid FROM chat_aliases WHERE short_id=? COLLATE NOCASE',(alias,)).fetchone()
            if not row:raise ValueError('Alias is not registered: '+alias)
            if not chat_tracking.UUID.fullmatch(row[1]):raise ValueError('Wake needs the real local task UUID for '+row[0])
            if row[1] not in chat_tracking.find_rollouts({row[1]}):
                raise ValueError('This host does not have a local task history for '+row[0]+'; run setup on its destination host')
            targets[row[0].casefold()]=row[1]
    command=find_codex(None)
    run([*command,'queue','--help'])
    return settings,{'edition':EDITION,'database_path':str(database),'bettercontext_root':str(service_root()/'runtime'),
                    **{key:str(settings[key]) for key in ('storage_registry_path','shared_root','instance_id') if key in settings},
                    'local_aliases':list(targets),'local_targets':targets,'codex_command':command,
                    'state_path':str(service_root()/'dispatches.db'),'log_path':str(service_root()/'wake.log'),
                    'poll_seconds':2.0}


def install(aliases,check=False):
    settings,config=plan(aliases)
    if check:return {'validated':True,'installed':False,'plan':config}
    root=service_root()
    root.mkdir(parents=True,exist_ok=True)
    # Stop only this edition before updating the files of a running helper.
    previous=service_action('status')
    if previous.get('running'):service_action('stop')
    runtime=root/'runtime'
    runtime.mkdir(exist_ok=True)
    for name in ('memory.py','database.py','chat_tracking.py','storage_registry.py'):
        shutil.copy2(settings['bettercontext_root']/name,runtime/name)
    shutil.copy2(Path(__file__).with_name('wake_dispatcher.py'),root/'wake_dispatcher.py')
    shutil.copy2(Path(__file__).with_name('storage_registry.py'),root/'storage_registry.py')
    (root/'wake-dispatcher.json').write_text(json.dumps(config,indent=2)+'\n',encoding='utf-8')
    (root/'service.json').write_text(json.dumps({'python':sys.executable},indent=2)+'\n',encoding='utf-8')
    state=service_action('install')
    return {'edition':EDITION,'service':state,'config_path':str(root/'wake-dispatcher.json'),
            'local_aliases':config['local_aliases'],'starts_at_login':True}


def status():
    root=service_root()
    legacy = legacy_installations(with_status=True)
    if not (root/'wake-dispatcher.json').is_file():return {'edition':EDITION,'installed':False,'running':False,'legacy_bridges':legacy}
    config=json.loads((root/'wake-dispatcher.json').read_text(encoding='utf-8'))
    return {'edition':EDITION,'legacy_bridges':legacy,**service_action('status'),'local_aliases':config['local_aliases'],'config_path':str(root/'wake-dispatcher.json')}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['install','start','stop','status','uninstall'])
    parser.add_argument('--alias',action='append',default=[])
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    try:
        result=install(args.alias,args.check) if args.action=='install' else status() if args.action=='status' else service_action(args.action)
        print(json.dumps(result,indent=2))
    except (OSError,ValueError,sqlite3.Error,subprocess.SubprocessError) as error:
        print(str(error),file=sys.stderr)
        raise SystemExit(2)
