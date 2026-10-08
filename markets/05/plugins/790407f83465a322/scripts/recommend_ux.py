#!/usr/bin/env python3
"""Conservative UX recommendations; does not modify the app."""
import argparse,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("blueprint",type=Path);p.add_argument("--usage",type=Path);a=p.parse_args()
 try:d=json.loads(a.blueprint.read_text(encoding="utf-8")); usage=json.loads(a.usage.read_text(encoding="utf-8")) if a.usage else {}
 except (OSError,json.JSONDecodeError) as exc:print(f"ERROR: {exc}");return 2
 out=[]
 for f in d.get("forms",[]):
  if len(f.get("primaryTaskFields",[]))>8:out.append(f"Form '{f.get('name')}' verdichten; ersten Tab auf Kernaufgabe fokussieren.")
 for v in d.get("views",[]):
  if len(v.get("columns",[]))>8:out.append(f"View '{v.get('name')}' kürzen; Scanbarkeit testen.")
  if usage.get("views",{}).get(v.get("name"),1)==0:out.append(f"View '{v.get('name')}' ohne Nutzung; vor Entfernen Twin und Fachbereich prüfen.")
 print("UX Optimization Recommendations");[print("- "+x) for x in out or ["Keine strukturelle Optimierung erkannt; Kernaufgaben trotzdem testen."]];return 0
if __name__=="__main__":raise SystemExit(main())
