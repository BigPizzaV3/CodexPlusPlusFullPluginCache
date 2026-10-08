#!/usr/bin/env python3
"""Explain a blueprint component in business, UX and governance terms."""
import argparse,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("blueprint",type=Path);p.add_argument("component");a=p.parse_args()
 try:d=json.loads(a.blueprint.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as exc:print(f"ERROR: {exc}");return 2
 found=[]
 for area,key in [("navigation","group"),("forms","name"),("views","name"),("personas","name")]:
  for x in d.get(area,[]):
   if x.get(key)==a.component:found.append((area,x))
 print(f"Explainable Governance: {a.component}")
 if not found:print("- Komponente nicht im Blueprint gefunden; Zweck und Entfernungsauswirkung sind nicht nachweisbar.");return 1
 for area,x in found:
  print(f"- Bereich: {area}")
  print(f"- Zielpersona: {x.get('persona', x.get('name','FEHLT'))}")
  print(f"- Kernaufgabe: {', '.join(x.get('coreTasks',[])) or 'im Blueprint ergänzen'}")
 print(f"- Business Outcome: {d.get('business',{}).get('outcome','FEHLT')}")
 print(f"- KPIs: {', '.join(d.get('business',{}).get('successMetrics',[])) or 'FEHLT'}")
 print("- Entfernungsauswirkung: Navigation, Rollen, Tests und Twin-Report vor einer Entfernung prüfen.")
 return 0
if __name__=="__main__":raise SystemExit(main())
