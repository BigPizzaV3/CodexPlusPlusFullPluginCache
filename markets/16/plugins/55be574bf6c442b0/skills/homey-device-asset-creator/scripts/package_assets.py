#!/usr/bin/env python3
"""Validate and package exactly the four production files."""
from pathlib import Path
import argparse
import zipfile
from asset_validation import validate

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('asset_dir',type=Path)
    parser.add_argument('zip_path',type=Path)
    parser.add_argument('--master',type=Path,required=True)
    parser.add_argument('--render-dir',type=Path,required=True)
    args = parser.parse_args()
    errors = validate(args.asset_dir,args.master,args.render_dir)
    if errors:
        parser.exit(1,'\n'.join('FAIL: '+e for e in errors)+'\n')
    args.zip_path.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(args.zip_path,'w',zipfile.ZIP_DEFLATED) as archive:
        for name in ('small.png','large.png','xlarge.png','icon.svg'):
            archive.write(args.asset_dir/name,name)
    print(args.zip_path)

if __name__ == '__main__':
    main()
