#!/usr/bin/env python3
"""Offline heuristics for a Dataverse solution export; never changes Dataverse."""
import argparse, json
from pathlib import Path

def main():
    p=argparse.ArgumentParser(); p.add_argument("solution",type=Path); p.add_argument("--json",action="store_true"); a=p.parse_args()
    forms=list((a.solution/"Entities").rglob("FormXml/main/*.xml")); views=list((a.solution/"Entities").rglob("SavedQueries/*.xml")); sitemap=list((a.solution/"AppModuleSiteMaps").rglob("*.xml"))
    findings=[]
    for f in forms:
        text=f.read_text(encoding="utf-8",errors="ignore"); controls=text.count("<control ")
        if controls>35: findings.append({"area":"performance","severity":"warning","file":str(f),"message":f"{controls} controls; split secondary data into tabs."})
    for f in sitemap:
        text=f.read_text(encoding="utf-8",errors="ignore")
        if "New Group" in text or "new_" in text.lower(): findings.append({"area":"ux","severity":"warning","file":str(f),"message":"Technical or generated navigation label detected."})
    result={"forms":len(forms),"views":len(views),"sitemaps":len(sitemap),"findings":findings,"pass":not any(x["severity"]=="error" for x in findings)}
    print(json.dumps(result,ensure_ascii=False,indent=2) if a.json else json.dumps(result,ensure_ascii=False))
if __name__=="__main__": main()
