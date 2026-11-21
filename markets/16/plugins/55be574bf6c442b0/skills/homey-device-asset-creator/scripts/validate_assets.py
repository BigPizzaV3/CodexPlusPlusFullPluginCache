#!/usr/bin/env python3
"""Validate Homey production assets and optional common-master / SVG render checks."""
from pathlib import Path
import argparse
from asset_validation import validate

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('asset_dir', type=Path)
    parser.add_argument('--master', type=Path)
    parser.add_argument('--render-dir', type=Path)
    args = parser.parse_args()
    errors = validate(args.asset_dir, args.master, args.render_dir)
    for error in errors:
        print('FAIL:', error)
    if errors:
        return 1
    print('PASS: structural checks' + ('; common-master comparison' if args.master else '') + ('; SVG render checks' if args.render_dir else ''))
    print('Visually review product fidelity, background interiors, line separation and composition.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
