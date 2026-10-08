#!/usr/bin/env python3
"""Create a safe, offline structural risk report from two app blueprints."""
import argparse, json
from pathlib import Path

def load(path): return json.loads(path.read_text(encoding="utf-8"))
def values(data, path, key): return {x[key] for x in data.get(path, []) if isinstance(x, dict) and x.get(key)}

def main():
    p=argparse.ArgumentParser(description="Simulate Dataverse app change impact")
    p.add_argument("before",type=Path); p.add_argument("after",type=Path); p.add_argument("--output",type=Path,required=True); a=p.parse_args()
    try: before, after=load(a.before), load(a.after)
    except (OSError,json.JSONDecodeError) as exc: print(f"ERROR: {exc}"); return 2
    risks=[]
    for path,key,label in [("personas","name","Persona"),("forms","name","Formular"),("views","name","Ansicht"),("navigation","group","Navigation")]:
        old,new=values(before,path,key),values(after,path,key)
        risks += [{"severity":"HIGH","area":label,"component":x,"change":"removed","action":"Abhängigkeiten, Kommunikation und Rollback prüfen"} for x in sorted(old-new)]
        risks += [{"severity":"MEDIUM","area":label,"component":x,"change":"added","action":"Zugriff und UAT je Persona testen"} for x in sorted(new-old)]
    old={x.get("logicalName") for x in before.get("dataModel",{}).get("tables",[]) if x.get("logicalName")}; new={x.get("logicalName") for x in after.get("dataModel",{}).get("tables",[]) if x.get("logicalName")}
    risks += [{"severity":"CRITICAL","area":"Datenmodell","component":x,"change":"removed","action":"Datenmigration, Backup und bestätigten Rollback verlangen"} for x in sorted(old-new)]
    if before.get("security") != after.get("security"): risks.append({"severity":"HIGH","area":"Security","component":"security","change":"changed","action":"Least-Privilege- und negative Zugriffstests"})
    report={"simulation":"offline-structural","safeToApply":not any(x["severity"]=="CRITICAL" for x in risks),"risks":risks,"requiredTests":["Validate/Publish","Rollentests","Tastatur/Responsive","repräsentative Performance"],"rollback":after.get("change",{}).get("rollbackPlan","FEHLT")}
    a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(f"Digital twin report written: {a.output}"); return 0
if __name__=="__main__": raise SystemExit(main())
