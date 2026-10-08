#!/usr/bin/env python3
"""Create a deliberately unconfigured, isolated HA audit workspace."""
import argparse
import json
import re
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--target', required=True)
    args = parser.parse_args()
    root = args.destination.expanduser().resolve()
    if root.exists():
        parser.error('Destination exists; choose a new directory to preserve prior work.')
    source = Path(__file__).resolve().parents[1] / 'assets' / 'harness'
    shutil.copytree(source, root)
    config = {
        'target': args.target, 'runId': 'audit-001', 'passId': 'fast',
        'adapterConfigured': False, 'sourceStatus': 'unverified', 'sourceEvidence': '',
        'expectedTag': '', 'sourcePaths': [], 'entry': '/fixture.html',
        'profile': 'phone-390x844-chromium-emulated', 'seed': 1,
        'depth': 'rigorous',
        'viewport': {'width':390,'height':844,'isMobile':True,'hasTouch':True,'deviceScaleFactor':3},
        'stepTimeoutMs':2500, 'maxPassMs':20000,
        'plan': [{'id':'target.journey','required':True,'expected':'Replace with a specific observable dashboard journey'}],
        'resources': [
            {'path':'/fixture.html','file':'fixture.html','contentType':'text/html'},
            {'path':'/adapter.js','file':'adapter.js','contentType':'application/javascript'},
            {'path':'/mock-hass.mjs','file':'mock-hass.mjs','contentType':'application/javascript'},
            {'path':'/fault-controller.mjs','file':'fault-controller.mjs','contentType':'application/javascript'}
        ]
    }
    (root/'audit.json').write_text(json.dumps(config,indent=2)+'\n')
    catalog=(source.parents[1]/'references/coverage-catalog.md').read_text()
    families=re.findall(r'^\| ([A-Z]+-\d+) \|',catalog,re.M)
    (root/'campaign.json').write_text(json.dumps({
        'schemaVersion':1,'target':args.target,'cases':[],
        'families':{family:{'disposition':'unassessed','reason':'','caseIds':[]} for family in families}
    },indent=2)+'\n')
    (root/'checkpoint.json').write_text(json.dumps({
        'target':args.target,'phase':'adapter-required','live_changes':[],
        'completed_passes':[],'next_action':'Verify active source and implement the isolated adapter and suite.'
    },indent=2)+'\n')
    print(json.dumps({'workspace':str(root),'configured':False}))

if __name__ == '__main__':
    main()
