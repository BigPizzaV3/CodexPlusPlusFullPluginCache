#!/usr/bin/env python3
"""Create reviewable CI, integration, test, observability and governance assets from one blueprint."""
import argparse,json
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument("blueprint",type=Path);p.add_argument("--output",type=Path,required=True);a=p.parse_args();d=json.loads(a.blueprint.read_text(encoding="utf-8"));a.output.mkdir(parents=True,exist_ok=True)
 name=d.get("solution",{}).get("uniqueName","solution")
 (a.output/"ci-quality-gates.md").write_text(f"# {name} CI/CD\n- Export/unpack\n- Blueprint and solution validation\n- Solution Checker\n- Managed promotion with approval\n- Retain previous package for rollback\n",encoding="utf-8")
 (a.output/"test-matrix.md").write_text("# Role smoke tests\n"+"\n".join(f"- [ ] {p.get('name')}: {t}" for p in d.get('personas',[]) for t in p.get('coreTasks',[]))+"\n",encoding="utf-8")
 (a.output/"integration-contract.md").write_text("# Integration contract\n- Define owner, authentication, schema version, idempotency key, retry, dead-letter handling and monitoring for every endpoint.\n",encoding="utf-8")
 (a.output/"ai-governance.md").write_text("# AI governance\n- Human approval before irreversible changes.\n- Log prompt intent, validation result and change ID; exclude secrets and unnecessary PII.\n- Fallback to reviewed deterministic plan on low confidence.\n",encoding="utf-8")
 (a.output/"operations.md").write_text("# Operations\n- Monitor capacity, license, environment and permission drift.\n- Aggregate adoption and failure metrics; follow retention policy.\n",encoding="utf-8")
 print(a.output)
if __name__=="__main__":main()
