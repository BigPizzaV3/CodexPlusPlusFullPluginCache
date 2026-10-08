#!/usr/bin/env python3
"""Create concise admin and end-user Markdown documentation from a blueprint."""
import argparse,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("blueprint",type=Path);p.add_argument("--output",type=Path,required=True);a=p.parse_args();d=json.loads(a.blueprint.read_text(encoding="utf-8"));
 lines=[f"# {d.get('appName','Dataverse-App')}","","## Zweck",d.get("business",{}).get("outcome",""),"","## Navigation"]
 for n in d.get("navigation",[]): lines.append("- "+n.get("group","Arbeitsbereich")+": "+", ".join(n.get("pages",[])))
 lines += ["","## Datenmodell"]
 for t in d.get("dataModel",{}).get("tables",[]): lines.append("- **"+t.get("displayName",t.get("logicalName",""))+"**: "+", ".join(c.get("displayName","") for c in t.get("columns",[])))
 lines += ["","## Betrieb","- Changes only through the confirmed unmanaged Dev solution.","- Promote managed packages downstream; retain the prior managed package as rollback."]
 a.output.write_text("\n".join(lines)+"\n",encoding="utf-8");print(a.output)
if __name__=="__main__": main()
