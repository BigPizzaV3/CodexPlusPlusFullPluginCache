#!/usr/bin/env python3
"""Create an intentionally review-required Dataverse app blueprint draft."""
import argparse,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("brief");p.add_argument("--output",type=Path,required=True);a=p.parse_args()
 d={"appName":a.brief[:100],"status":"DRAFT_REQUIRES_REVIEW","assumptions":["Zielumgebung und Solution unbestätigt","Datenmodell und Rollen fachlich validieren"],"business":{"outcome":a.brief,"successMetrics":[],"nonGoals":[]},"personas":[],"solution":{"uniqueName":"","publisherPrefix":"","environment":""},"dataModel":{"sensitiveData":[],"tables":[]},"navigation":[],"forms":[],"views":[],"customPages":[],"security":{"leastPrivilegeReviewed":False,"roleTaskMatrix":False,"fieldSecurityReviewed":False},"performance":{"expectedRecordVolume":0,"formComponentBudget":"","representativeDataTest":False},"change":{"existingApp":False,"impactReviewed":False,"rollbackPlan":""},"testing":{"roleSmokeTests":False,"keyboardTest":False,"responsiveTest":False,"accessibilityPlan":"","uatOwner":""},"alm":{"devUnmanaged":False,"downstreamManaged":False,"repositoryExport":False,"version":""}}
 a.output.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(f"Draft blueprint written: {a.output}; review before implementation.");return 0
if __name__=="__main__":raise SystemExit(main())
