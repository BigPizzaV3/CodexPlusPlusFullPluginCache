import argparse
import json
import signal
import threading
from .core import Workspace, DisproError, pipeline

def main():
    parser = argparse.ArgumentParser(description='Dispro: offline fixed-recipe LV2 workflow')
    parser.add_argument('--workspace', required=True, help='Explicit dedicated output directory')
    commands = parser.add_subparsers(dest='action', required=True)
    commands.add_parser('init')
    for action in ('scaffold','run','receipt'):
        command = commands.add_parser(action)
        command.add_argument('project')
        if action == 'run': command.add_argument('--timeout',type=int,default=30)
        if action == 'receipt': command.add_argument('run_id')
    args = parser.parse_args()
    cancel = threading.Event()
    signal.signal(signal.SIGINT,lambda *_: cancel.set())
    signal.signal(signal.SIGTERM,lambda *_: cancel.set())
    try:
        ws = Workspace(args.workspace,initialize=args.action=='init')
        if args.action == 'init': result = {'status':'initialized'}
        elif args.action == 'scaffold': result = ws.scaffold(args.project)
        elif args.action == 'receipt': result = ws.receipt(args.project,args.run_id)
        else: result = pipeline(ws,args.project,args.timeout,cancel)
        print(json.dumps(result,indent=2,sort_keys=True))
        return 0 if result.get('outcome','passed') == 'passed' else 1
    except (DisproError,OSError):
        print(json.dumps({'status':'failed','reason':'invalid input, workspace, or filesystem operation'}))
        return 2

if __name__ == '__main__': raise SystemExit(main())
