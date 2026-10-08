#!/usr/bin/env python3
"""Compliance-by-design evidence checks; not legal advice."""
import argparse,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("blueprint",type=Path);a=p.parse_args()
 try:d=json.loads(a.blueprint.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as exc:print(f"ERROR: {exc}");return 2
 s=d.get("security",{});issues=[]
 if d.get("dataModel",{}).get("sensitiveData") and not s.get("fieldSecurityReviewed"):issues.append("Sensible Daten ohne Feldsicherheitsnachweis")
 if not s.get("leastPrivilegeReviewed"):issues.append("Least Privilege nicht nachgewiesen")
 if not s.get("roleTaskMatrix"):issues.append("Rolle-zu-Aufgabe-Matrix fehlt")
 for t in d.get("dataModel",{}).get("tables",[]):
  if t.get("ownership") not in ("userOrTeam","organization"):issues.append(f"Ownership für {t.get('logicalName','?')} fehlt/ist ungültig")
 if not d.get("testing",{}).get("uatOwner"):issues.append("UAT Owner fehlt")
 if not d.get("alm",{}).get("repositoryExport"):issues.append("Repository-Export fehlt")
 print("Compliance by Design: "+("PASS" if not issues else "REVIEW REQUIRED"));[print("- "+x) for x in issues];print("- Organisationsrichtlinien und Rechtsberatung bleiben zusätzlich erforderlich.");return 0 if not issues else 1
if __name__=="__main__":raise SystemExit(main())
