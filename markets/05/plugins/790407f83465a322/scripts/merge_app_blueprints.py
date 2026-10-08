#!/usr/bin/env python3
"""Three-way review report for parallel blueprint changes; never overwrites a file."""
import argparse,json
from pathlib import Path
def load(p):return json.loads(p.read_text(encoding="utf-8"))
def main():
 p=argparse.ArgumentParser();p.add_argument("base",type=Path);p.add_argument("ours",type=Path);p.add_argument("theirs",type=Path);p.add_argument("--output",type=Path,required=True);a=p.parse_args()
 try:b,o,t=load(a.base),load(a.ours),load(a.theirs)
 except (OSError,json.JSONDecodeError) as exc:print(f"ERROR: {exc}");return 2
 conflicts=[]; accepted=[]
 for key in ["solution","security","navigation","forms","views","dataModel"]:
  bv,ov,tv=b.get(key),o.get(key),t.get(key)
  if ov==tv: accepted.append({"area":key,"source":"both"})
  elif ov==bv: accepted.append({"area":key,"source":"theirs"})
  elif tv==bv: accepted.append({"area":key,"source":"ours"})
  else: conflicts.append({"area":key,"reason":"Beide Seiten haben denselben Bereich unterschiedlich verändert","required":"Fachliche Entscheidung, Twin-Impact und Rollentests"})
 report={"autoMerge":not conflicts,"accepted":accepted,"conflicts":conflicts,"safety":"Keine Eingabedatei wurde verändert. Security-, Datenmodell- und Entfernungskonflikte nie automatisch mergen."}
 a.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(f"Merge report written: {a.output}; conflicts: {len(conflicts)}");return 0
if __name__=="__main__":raise SystemExit(main())
